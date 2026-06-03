#!/usr/bin/env python3
"""
Cross-Task Generalization: Continuation -> Summarization

Fixes:
- Keep original output filename: figA3_cross_task
- Separate title and explanatory text to avoid overlap.
- Move legend outside bottom.
- Move delta labels away from bars/error bars.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,

    "font.size": 8,
    "axes.titlesize": 9,
    "axes.titleweight": "bold",
    "axes.labelsize": 8,

    "legend.fontsize": 7,
    "legend.frameon": False,

    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.9,

    "axes.grid": True,
    "grid.alpha": 0.10,
    "grid.linestyle": "-",

    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
})


FIG_DIR = Path(__file__).resolve().parent

CONT_COLOR = "#2A9D8F"
SUMM_COLOR = "#E76F51"


def save_pub(fig, filename, dpi=600):
    for ext in ["svg", "pdf", "png"]:
        fig.savefig(
            FIG_DIR / f"{filename}.{ext}",
            bbox_inches="tight",
            dpi=dpi,
        )


def main():
    # Data from the shown figure
    models = ["Qwen2.5-7B", "Mistral-7B-v0.3"]

    continuation = np.array([0.784, 0.869])
    summarization = np.array([0.791, 0.744])

    # Error bars shown on summarization bars
    summarization_err = np.array([0.070, 0.037])

    x = np.arange(len(models))
    width = 0.28

    fig, ax = plt.subplots(figsize=(6.8, 2.45))

    # ── Bars ─────────────────────────────────────────────
    bars_cont = ax.bar(
        x - width / 2,
        continuation,
        width,
        color=CONT_COLOR,
        edgecolor="white",
        linewidth=0.6,
        label="Continuation",
        zorder=3,
    )

    bars_summ = ax.bar(
        x + width / 2,
        summarization,
        width,
        color=SUMM_COLOR,
        edgecolor="white",
        linewidth=0.6,
        label="Summarization",
        yerr=summarization_err,
        error_kw={
            "ecolor": "#888888",
            "elinewidth": 0.9,
            "capsize": 3,
            "capthick": 0.9,
        },
        zorder=3,
    )

    # ── Value labels ─────────────────────────────────────
    for bar, val in zip(bars_cont, continuation):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            val + 0.012,
            f"{val:.3f}",
            ha="center",
            va="bottom",
            fontsize=7,
            color=CONT_COLOR,
            fontweight="bold",
            zorder=5,
        )

    for bar, val, err in zip(bars_summ, summarization, summarization_err):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            val + err + 0.012,
            f"{val:.3f}",
            ha="center",
            va="bottom",
            fontsize=7,
            color=SUMM_COLOR,
            fontweight="bold",
            zorder=5,
        )

    # ── Chance line ──────────────────────────────────────
    ax.axhline(
        y=0.5,
        color="#B0BEC5",
        linewidth=0.8,
        linestyle=":",
        zorder=1,
    )

    # ── Delta labels ─────────────────────────────────────
    qwen_delta = summarization[0] - continuation[0]
    mistral_delta = summarization[1] - continuation[1]

    ax.text(
        x[0],
        0.845,
        f"Δ={qwen_delta:+.3f}",
        ha="center",
        va="bottom",
        fontsize=7,
        color=CONT_COLOR,
        fontweight="bold",
        zorder=6,
    )

    ax.text(
        x[1] + 0.00,
        0.925,
        f"Δ={mistral_delta:+.3f}",
        ha="center",
        va="bottom",
        fontsize=7,
        color=SUMM_COLOR,
        fontweight="bold",
        zorder=6,
    )

    # ── Axes ─────────────────────────────────────────────
    ax.set_xticks(x)
    ax.set_xticklabels(models)

    ax.set_ylabel("CRM-LTS LR AUC")
    ax.set_ylim(0.40, 0.98)

    # ── Title and explanatory text separated ─────────────
    fig.suptitle(
        "Cross-Task Generalization: Continuation  →  Summarization",
        fontsize=9,
        fontweight="bold",
        y=0.97,
    )

    fig.text(
        0.50,
        0.875,
        "Qwen: full signal preservation (Δ=+0.007)\n"
        "Mistral: partial transfer (AUC 0.744, still >> 0.5)",
        ha="center",
        va="top",
        fontsize=7,
        color="#555555",
    )

    # ── Legend outside bottom ────────────────────────────
    ax.legend(
        fontsize=7,
        loc="upper center",
        bbox_to_anchor=(0.82, -0.16),
        ncol=2,
        frameon=False,
        columnspacing=0.9,
        handletextpad=0.4,
    )

    fig.subplots_adjust(
        left=0.09,
        right=0.985,
        bottom=0.28,
        top=0.74,
    )

    # 保持原保存文件名，不改
    save_pub(fig, "figA3_cross_task")

    plt.close(fig)

    print("Saved to", FIG_DIR)


if __name__ == "__main__":
    main()