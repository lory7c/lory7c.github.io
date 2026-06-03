#!/usr/bin/env python3
"""Fig S1: Per-attack bubble scatter — vulnerability landscape."""
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


# ── Bubble scatter: base ASR vs defense ASR ───────────────────────────────────
def plot_bubble_scatter(ax):
    obj = load_json("idea3_per_attack_qwen7b.json")
    rows = obj["rows"]

    # Categorize attacks by text content
    categories = {
        "Output string": ["PWNED", "SECRET", "INJECTED", "STAGE_2", "1492", "1234567", "JSON", "override"],
        "Harmless task": ["haiku", "joke", "chicken", "Pig Latin", "foo"],
        "Compliance": ["compromised", "help you", "TASK ABANDONED", "hello attacker"],
    }

    def categorize(text):
        text_lower = text.lower()
        for cat, keywords in categories.items():
            if any(k.lower() in text_lower for k in keywords):
                return cat
        return "Other"

    cat_colors = {
        "Output string": PALETTE["red_strong"],
        "Harmless task": PALETTE["teal"],
        "Compliance": PALETTE["blue_main"],
        "Other": PALETTE["neutral_mid"],
    }

    x_vals = []
    y_vals = []
    sizes = []
    colors = []
    labels = []
    cats = []

    for row in rows:
        base = row["base_asr"] * 100
        defense = row["def_asr"] * 100
        n = row["n"]
        cat = categorize(row["attack_text"])

        x_vals.append(base)
        y_vals.append(defense)
        sizes.append(20 + n * 2.5)
        colors.append(cat_colors[cat])
        labels.append(row["attack_text"][:30])
        cats.append(cat)

    # Diagonal reference (no effect)
    ax.plot([0, 100], [0, 100], '--', color=PALETTE["neutral_light"], linewidth=0.8, zorder=1)
    ax.fill_between([0, 100], [0, 100], [0, 0], color=PALETTE["green_3"], alpha=0.06, zorder=0)
    ax.text(85, 5, "Effective intervention zone", fontsize=5.5, color=PALETTE["green_3"],
            ha='right', style='italic', alpha=0.8)

    # Scatter
    for cat in cat_colors:
        mask = [c == cat for c in cats]
        xv = [x_vals[i] for i in range(len(x_vals)) if mask[i]]
        yv = [y_vals[i] for i in range(len(y_vals)) if mask[i]]
        sz = [sizes[i] for i in range(len(sizes)) if mask[i]]
        ax.scatter(xv, yv, s=sz, c=cat_colors[cat], alpha=0.7, zorder=3,
                   edgecolor='white', linewidth=0.5, label=cat)

    ax.set_xlabel("Base ASR (no intervention, %)")
    ax.set_ylabel("Intervention ASR (projection-out, %)")
    ax.set_xlim(-5, 105)
    ax.set_ylim(-5, 80)
    ax.legend(loc="upper left", handlelength=1.0, fontsize=5.5, title="Attack family",
              title_fontsize=5.5)
    ax.set_title("Per-attack vulnerability landscape", fontsize=7, pad=3)


# ── Horizontal lollipop: attack ranking ───────────────────────────────────────
def plot_attack_ranking(ax):
    obj = load_json("idea3_per_attack_qwen7b.json")
    rows = sorted(obj["rows"], key=lambda r: r["base_asr"] - r["def_asr"], reverse=True)

    y = np.arange(len(rows))
    reductions = [(r["base_asr"] - r["def_asr"]) * 100 for r in rows]
    base_asrs = [r["base_asr"] * 100 for r in rows]

    # Stems
    ax.hlines(y, xmin=0, xmax=reductions, color=PALETTE["neutral_light"], linewidth=0.8, zorder=1)
    # Bulbs sized by base ASR
    ax.scatter(reductions, y, s=[20 + b * 0.8 for b in base_asrs],
               c=[PALETTE["blue_main"] if r > 10 else PALETTE["neutral_mid"] for r in reductions],
               zorder=3, edgecolor='white', linewidth=0.5)

    # Labels (shortened attack text)
    short_labels = []
    for r in rows:
        text = r["attack_text"]
        if len(text) > 35:
            text = text[:32] + "..."
        short_labels.append(text)

    ax.set_yticks(y)
    ax.set_yticklabels(short_labels, fontsize=4.5)
    ax.set_xlabel("ASR reduction (pp)")
    ax.set_xlim(-5, max(reductions) + 5)
    ax.set_title("Intervention effect by attack", fontsize=7, pad=3)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    fig = plt.figure(figsize=(8.5, 3.2))
    gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.1], wspace=0.5)
    ax_a = fig.add_subplot(gs[0, 0])
    ax_b = fig.add_subplot(gs[0, 1])

    plot_bubble_scatter(ax_a)
    plot_attack_ranking(ax_b)

    ax_a.text(-0.10, 1.02, 'a', transform=ax_a.transAxes, fontsize=10,
              fontweight='bold', ha='left', va='bottom')
    ax_b.text(-0.10, 1.02, 'b', transform=ax_b.transAxes, fontsize=10,
              fontweight='bold', ha='left', va='bottom')

    out = ROOT / "figS1_bubble_scatter"
    saved = finalize_figure(fig, out, formats=['svg', 'pdf', 'png'], dpi=300)
    print("Saved:", " / ".join(Path(p).name for p in saved))


if __name__ == "__main__":
    main()
