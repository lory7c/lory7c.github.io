#!/usr/bin/env python3
"""Fig 5 advanced: Slope chart / connected dot plot for sampling robustness."""
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


def add_panel_label(ax, label, x=-0.08, y=1.02, fontsize=10, color='black'):
    ax.text(x, y, label, transform=ax.transAxes, fontsize=fontsize,
            fontweight='bold', color=color, ha='left', va='bottom')


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


# ── Panel A: Slope chart ASR ──────────────────────────────────────────────────
def plot_slope_asr(ax):
    obj = load_json("sampling_robustness_qwen7b.json")
    conds = obj["conditions"]
    strategies = [c["decoding"] for c in conds]
    x = np.arange(len(strategies))

    # No defense
    no_def = [c["no_defense_asr_percent"] for c in conds]
    no_def_err = [(c["no_defense_asr_ci95"][1] - c["no_defense_asr_ci95"][0]) / 2 for c in conds]
    # Defense
    def_ = [c["defense_asr_percent"] for c in conds]
    def_err = [(c["defense_asr_ci95"][1] - c["defense_asr_ci95"][0]) / 2 for c in conds]

    # Connected dots with slope lines
    ax.errorbar(x, no_def, yerr=no_def_err, fmt='o', color=PALETTE["neutral_mid"],
                markersize=6, capsize=3, capthick=0.8, zorder=3, label="No intervention")
    ax.errorbar(x, def_, yerr=def_err, fmt='s', color=PALETTE["blue_main"],
                markersize=6, capsize=3, capthick=0.8, zorder=3, label="Projection-out")

    # Connect corresponding points with arrows
    for i in range(len(strategies)):
        ax.annotate("", xy=(x[i], def_[i]), xytext=(x[i], no_def[i]),
                    arrowprops=dict(arrowstyle='->', color=PALETTE["green_3"], lw=1.5,
                                    connectionstyle='arc3,rad=0'))
        # Annotate reduction
        reduction = no_def[i] - def_[i]
        mid_y = (no_def[i] + def_[i]) / 2
        ax.text(x[i] + 0.12, mid_y, f"−{reduction:.1f}", fontsize=5.5,
                color=PALETTE["green_3"], fontweight='bold', va='center')

    ax.set_xticks(x)
    ax.set_xticklabels(strategies, fontsize=6)
    ax.set_ylabel("ASR (%)")
    ax.set_ylim(20, 58)
    ax.legend(loc="upper left", handlelength=1.2, fontsize=6)
    ax.set_title("Intervention effect across decoding", fontsize=7, pad=3)


# ── Panel B: Slope chart utility ──────────────────────────────────────────────
def plot_slope_utility(ax):
    obj = load_json("sampling_robustness_qwen7b.json")
    conds = obj["conditions"]
    strategies = [c["decoding"] for c in conds]
    x = np.arange(len(strategies))

    no_def = [c["no_defense_utility_percent"] for c in conds]
    no_def_err = [(c["no_defense_utility_ci95"][1] - c["no_defense_utility_ci95"][0]) / 2 for c in conds]
    def_ = [c["defense_utility_percent"] for c in conds]
    def_err = [(c["defense_utility_ci95"][1] - c["defense_utility_ci95"][0]) / 2 for c in conds]

    ax.errorbar(x, no_def, yerr=no_def_err, fmt='o', color=PALETTE["neutral_mid"],
                markersize=6, capsize=3, capthick=0.8, zorder=3, label="No intervention")
    ax.errorbar(x, def_, yerr=def_err, fmt='s', color=PALETTE["blue_main"],
                markersize=6, capsize=3, capthick=0.8, zorder=3, label="Projection-out")

    for i in range(len(strategies)):
        ax.plot([x[i], x[i]], [no_def[i], def_[i]], color=PALETTE["neutral_light"],
                linewidth=1.0, linestyle='--', zorder=1)
        delta = no_def[i] - def_[i]
        ax.text(x[i] + 0.12, def_[i] + 0.5, f"−{delta:.1f}", fontsize=5.5,
                color=PALETTE["neutral_mid"], va='bottom')

    ax.set_xticks(x)
    ax.set_xticklabels(strategies, fontsize=6)
    ax.set_ylabel("Utility success (%)")
    ax.set_ylim(82, 92)
    ax.legend(loc="upper right", handlelength=1.2, fontsize=6)
    ax.set_title("Utility preservation", fontsize=7, pad=3)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    fig, axes = plt.subplots(1, 2, figsize=(6.0, 2.6))
    fig.subplots_adjust(wspace=0.32)
    plot_slope_asr(axes[0])
    plot_slope_utility(axes[1])

    add_panel_label(axes[0], 'a', x=-0.10)
    add_panel_label(axes[1], 'b', x=-0.10)

    out = ROOT / "fig5_slope"
    saved = finalize_figure(fig, out, formats=['svg', 'pdf', 'png'], dpi=300)
    print("Saved:", " / ".join(Path(p).name for p in saved))


if __name__ == "__main__":
    main()
