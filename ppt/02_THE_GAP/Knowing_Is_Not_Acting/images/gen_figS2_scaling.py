#!/usr/bin/env python3
"""Fig S2: Scaling scatter — model size vs mechanistic detection quality."""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"

PALETTE = {
    "blue_main": "#0F4D92",
    "blue_secondary": "#3775BA",
    "green_3": "#8BCF8B",
    "red_strong": "#B64342",
    "neutral_light": "#CFCECE",
    "neutral_mid": "#767676",
    "neutral_dark": "#4D4D4D",
    "neutral_black": "#272727",
    "teal": "#42949E",
    "cream": "#F5F0E8",
}

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans', 'Liberation Sans']
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams.update({
    'font.size': 7,
    'axes.titlesize': 8,
    'axes.titleweight': 'bold',
    'axes.labelsize': 7,
    'legend.fontsize': 6.5,
    'legend.frameon': True,
    'legend.edgecolor': '#767676',
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'lines.linewidth': 1.2,
    'figure.dpi': 300,
    'savefig.dpi': 300,
})


def load_json(name: str):
    with open(DATA / name, "r", encoding="utf-8") as f:
        return json.load(f)


def finalize_figure(fig, out_path, formats=None, dpi=300, pad=1.5, close=True):
    fig.tight_layout(pad=pad)
    base = Path(out_path)
    if formats is None:
        formats = ['svg', 'pdf', 'png']
    saved = []
    for fmt in formats:
        p = str(base) + f'.{fmt}'
        fig.savefig(p, dpi=dpi, bbox_inches='tight')
        saved.append(p)
    if close:
        plt.close(fig)
    return saved


# ── Panel A: Size vs peak AUROC ───────────────────────────────────────────────
def plot_size_auroc(ax):
    rows = load_json("scaling_summary.json")
    # Filter valid rows
    valid = [r for r in rows if r["peak_abs_AUROC"] is not None and not np.isnan(r["peak_abs_AUROC"])]

    x = [r["n_params_B"] for r in valid]
    y = [r["peak_abs_AUROC"] for r in valid]
    sizes = [r["success_rate"] * 300 + 30 for r in valid]
    colors = []
    for r in valid:
        if "qwen" in r["model"]:
            colors.append(PALETTE["blue_main"])
        else:
            colors.append(PALETTE["teal"])

    # Log scale for x
    ax.set_xscale('log')

    # Regression line
    log_x = np.log(x)
    coeffs = np.polyfit(log_x, y, 1)
    x_fit = np.logspace(np.log10(min(x) * 0.8), np.log10(max(x) * 1.2), 100)
    y_fit = coeffs[0] * np.log(x_fit) + coeffs[1]
    ax.plot(x_fit, y_fit, '--', color=PALETTE["neutral_mid"], linewidth=0.8, zorder=1)

    ax.scatter(x, y, s=sizes, c=colors, alpha=0.75, zorder=3,
               edgecolor='white', linewidth=0.5)

    # Labels
    for r in valid:
        label = r["model"].replace("qwen2.5-", "Q-").replace("llama3-", "L-").replace("qwen3-", "Q3-")
        xytext = (5, 5)
        ha = 'left'
        if label == "Q-3b":
            xytext = (8, 5)
        elif label == "Q-7b":
            xytext = (8, -2)
        elif label == "Q-14b":
            xytext = (8, 5)
        elif label == "Q-1.5b":
            xytext = (15, 6)
            ha = 'right'
        ax.annotate(label, (r["n_params_B"], r["peak_abs_AUROC"]),
                    textcoords="offset points", xytext=xytext, fontsize=5, ha=ha)

    ax.set_xlabel("Parameters (B)")
    ax.set_ylabel("Peak probe AUROC")
    ax.set_ylim(0.55, 1.05)
    ax.set_title("Mechanistic detection scales with model size", fontsize=7, pad=3)

    # Add size legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor=PALETTE["blue_main"],
               markersize=6, label='Qwen'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=PALETTE["teal"],
               markersize=6, label='Llama'),
    ]
    ax.legend(handles=legend_elements, loc="lower left", fontsize=6, frameon=True, edgecolor=PALETTE["neutral_mid"], framealpha=0.9)

# ── Panel B: Size vs peak layer (relative) ────────────────────────────────────
def plot_size_layer(ax):
    rows = load_json("scaling_summary.json")
    valid = [r for r in rows if r["peak_layer"] is not None]

    x = [r["n_params_B"] for r in valid]
    y = [r["peak_layer"] / r["n_layers_estimated"] for r in valid]
    sizes = [r["success_rate"] * 300 + 30 for r in valid]
    colors = []
    for r in valid:
        if "qwen" in r["model"]:
            colors.append(PALETTE["blue_main"])
        else:
            colors.append(PALETTE["teal"])

    ax.set_xscale('log')

    # Horizontal reference lines
    ax.axhline(0.5, color=PALETTE["neutral_light"], linewidth=0.5, linestyle='--', alpha=0.5)
    ax.text(max(x) * 1.3, 0.52, "Mid-layer", fontsize=5, color=PALETTE["neutral_mid"], ha='right')

    ax.scatter(x, y, s=sizes, c=colors, alpha=0.75, zorder=3,
               edgecolor='white', linewidth=0.5)

    for r in valid:
        label = r["model"].replace("qwen2.5-", "Q-").replace("llama3-", "L-").replace("qwen3-", "Q3-")
        xytext = (5, 5)
        ha = 'left'
        if label == "Q-14b":
            xytext = (8, 5)
        elif label == "Q-1.5b":
            xytext = (2, 5)
        ax.annotate(label, (r["n_params_B"], r["peak_layer"] / r["n_layers_estimated"]),
                    textcoords="offset points", xytext=xytext, fontsize=5, ha=ha)

    ax.set_xlabel("Parameters (B)")
    ax.set_ylabel("Peak layer (relative depth)")
    ax.set_ylim(0.25, 1.0)
    ax.set_title("Detection peak shifts deeper", fontsize=7, pad=3)

    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor=PALETTE["blue_main"],
               markersize=6, label='Qwen'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=PALETTE["teal"],
               markersize=6, label='Llama'),
    ]
    ax.legend(handles=legend_elements, loc="upper left", fontsize=6, frameon=True, edgecolor=PALETTE["neutral_mid"], framealpha=0.9)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    fig, axes = plt.subplots(1, 2, figsize=(6.5, 2.8))
    fig.subplots_adjust(wspace=0.32)
    plot_size_auroc(axes[0])
    plot_size_layer(axes[1])

    axes[0].text(-0.10, 1.02, 'a', transform=axes[0].transAxes, fontsize=10,
                 fontweight='bold', ha='left', va='bottom')
    axes[1].text(-0.10, 1.02, 'b', transform=axes[1].transAxes, fontsize=10,
                 fontweight='bold', ha='left', va='bottom')

    out = ROOT / "figS2_scaling"
    saved = finalize_figure(fig, out, formats=['svg', 'pdf', 'png'], dpi=300)
    print("Saved:", " / ".join(Path(p).name for p in saved))


if __name__ == "__main__":
    main()
