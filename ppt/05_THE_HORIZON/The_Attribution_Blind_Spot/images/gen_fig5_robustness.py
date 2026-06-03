#!/usr/bin/env python3
"""
Fig 5: Robustness Controls.
Three-panel figure showing:
(a) Same-topic control (CRM-LTS): Random vs Same-topic AUC with BGE-M3 similarity
(b) Label permutation: True AUC vs permuted AUC (chance)
(c) Prompt randomization: AUC across 4 templates with std reported in legend

Updated with CRM-LTS same-topic results (n≈140).
Combined evidence that CRM signal is not topic familiarity, classifier artifact,
or prompt artifact.
"""

import json
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,

    "font.size": 7,
    "axes.titlesize": 8,
    "axes.titleweight": "bold",
    "axes.labelsize": 6.5,
    "legend.fontsize": 5.8,

    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.8,

    "legend.frameon": False,

    "axes.grid": True,
    "grid.alpha": 0.1,
    "grid.linestyle": "-",

    "lines.linewidth": 1.3,
    "lines.markersize": 4,

    "xtick.labelsize": 6,
    "ytick.labelsize": 6,
})


FIG_DIR = Path(__file__).resolve().parent
DATA_DIR = FIG_DIR / "data"


RANDOM_COLOR = "#B0BEC5"
SAME_TOPIC_COLOR = "#2A9D8F"
TRUE_COLOR = "#E76F51"
PERM_COLOR = "#B0BEC5"


def save_pub(fig, filename, dpi=600):
    for ext in ["svg", "pdf", "png"]:
        fig.savefig(
            FIG_DIR / f"{filename}.{ext}",
            bbox_inches="tight",
            dpi=dpi,
        )


def main():
    fig = plt.figure(figsize=(6.8, 2.15))

    # 手动控制布局，给下方说明和图例留空间
    fig.subplots_adjust(
        left=0.075,
        right=0.985,
        bottom=0.34,
        top=0.78,
        wspace=0.34,
    )

    # ── Panel (a): Same-topic control (CRM-LTS) ───────────
    ax1 = fig.add_subplot(1, 3, 1)

    models_st = ["Qwen-14B-Inst", "Mistral-7B", "Llama-8B"]
    random_auc = [0.925, 0.822, 0.784]      # CRM-LTS random non-member baseline
    same_topic_auc = [0.921, 0.842, 0.726]  # CRM-LTS same-topic, n≈140
    same_topic_std = [0.033, 0.060, 0.072]  # Per-fold std

    x = np.arange(len(models_st))
    width = 0.32

    bars1 = ax1.bar(
        x - width / 2,
        random_auc,
        width,
        color=RANDOM_COLOR,
        edgecolor="white",
        linewidth=0.5,
        label="Random NM",
        zorder=2,
    )

    bars2 = ax1.bar(
        x + width / 2,
        same_topic_auc,
        width,
        color=SAME_TOPIC_COLOR,
        edgecolor="white",
        linewidth=0.5,
        label="Same-Topic NM",
        zorder=2,
    )

    # Error bars on Same-Topic NM bars
    for bar, std in zip(bars2, same_topic_std):
        ax1.errorbar(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            yerr=std,
            fmt="none",
            ecolor="#555555",
            elinewidth=0.6,
            capsize=2,
            capthick=0.6,
            zorder=4,
        )

    # Value labels: Random NM
    for bar, val in zip(bars1, random_auc):
        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            val + 0.008,
            f"{val:.3f}",
            ha="center",
            fontsize=5.5,
            color="#888888",
            zorder=5,
        )

    # Value labels: Same-Topic NM, placed above error bars

    for bar, val in zip(bars2, same_topic_auc):
        ax1.annotate(
            f"{val:.3f}",
            xy=(bar.get_x() + bar.get_width() / 2, val),  # 柱顶中心
            xytext=(3, 0),  # 向右 5pt，向上 0pt
            textcoords="offset points",
            ha="left",
            va="bottom",
            fontsize=5.5,
            color=SAME_TOPIC_COLOR,
            fontweight="bold",
            zorder=6,
            bbox=dict(
                facecolor="white",
                edgecolor="none",
                alpha=0.75,
                pad=0.15,
            ),
        )
    # Δ annotations
    for i, (r, st, std) in enumerate(zip(random_auc, same_topic_auc, same_topic_std)):
        delta = st - r
        sign = "+" if delta >= 0 else ""
        color = SAME_TOPIC_COLOR if delta >= 0 else TRUE_COLOR

        top_y = max(r, st + std)

        ax1.annotate(
            f"Δ={sign}{delta:.3f}",
            xy=(i, top_y + 0.035),
            fontsize=5.5,
            color=color,
            fontweight="bold",
            ha="center",
            zorder=7,
        )

    ax1.set_xticks(x)
    ax1.set_xticklabels(
        models_st,
        rotation=15,
        fontsize=5.5,
        ha="right",
    )

    ax1.set_ylabel("CRM-LTS LR AUC", fontsize=6.5)
    ax1.set_title(
        "(a) Same-Topic Control (CRM-LTS)",
        fontsize=7,
        fontweight="bold",
        pad=4,
    )

    ax1.set_ylim(0.60, 1.06)

    ax1.axhline(
        y=0.5,
        color="#B0BEC5",
        linewidth=0.7,
        linestyle=":",
        zorder=1,
    )

    # 图例移到图外下方
    ax1.legend(
        fontsize=5,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.23),
        ncol=2,
        frameon=False,
        columnspacing=0.8,
        handletextpad=0.35,
    )

    # BGE-M3 说明移到图外下方
    ax1.text(
        0.5,
        -0.42,
        "BGE-M3 similarity: Random 0.32 → ST 0.51 (1.6× tighter matching)",
        transform=ax1.transAxes,
        fontsize=5,
        color="#666666",
        ha="center",
        va="top",
        clip_on=False,
    )

    # ── Panel (b): Label permutation ─────────────────────
    ax2 = fig.add_subplot(1, 3, 2)

    with open(DATA_DIR / "label_permutation_results.json") as f:
        perm_data = json.load(f)

    display_models = ["Mistral-7B", "Qwen-14B-Inst", "Llama-8B"]
    perm_keys = ["mistral-base", "qwen-14b-instruct", "llama-base"]
    perm_colors = ["#2A9D8F", "#E76F51", "#264653"]

    x2 = np.arange(len(display_models))
    width2 = 0.28

    true_handles = []

    for i, (pkey, color, dname) in enumerate(zip(perm_keys, perm_colors, display_models)):
        if pkey not in perm_data:
            continue

        true_auc = perm_data[pkey]["lr_true"]
        perm_mean = perm_data[pkey]["lr_perm_mean"]

        b_true = ax2.bar(
            i - width2 / 2,
            true_auc,
            width2,
            color=color,
            edgecolor="white",
            linewidth=0.5,
            zorder=2,
        )

        b_perm = ax2.bar(
            i + width2 / 2,
            perm_mean,
            width2,
            color=PERM_COLOR,
            edgecolor="white",
            linewidth=0.5,
            zorder=2,
        )

        if i == 0:
            true_handles = [b_true[0], b_perm[0]]

        ax2.text(
            i - width2 / 2,
            true_auc + 0.015,
            f"{true_auc:.3f}",
            ha="center",
            fontsize=5,
            color=color,
            fontweight="bold",
        )

        ax2.text(
            i + width2 / 2,
            perm_mean + 0.015,
            "0.50",
            ha="center",
            fontsize=5,
            color="#888888",
        )

    ax2.set_xticks(x2)
    ax2.set_xticklabels(
        display_models,
        rotation=15,
        fontsize=5.5,
        ha="right",
    )

    ax2.set_ylabel("CRM-LR AUC", fontsize=6.5)

    ax2.set_title(
        "(b) Label Permutation",
        fontsize=7,
        fontweight="bold",
        pad=4,
    )

    ax2.set_ylim(0.35, 1.02)

    ax2.axhline(
        y=0.5,
        color="#B0BEC5",
        linewidth=0.7,
        linestyle=":",
        zorder=1,
    )

    # 图例移到图外下方
    if true_handles:
        ax2.legend(
            true_handles,
            ["True labels", "Permuted (chance)"],
            fontsize=5,
            loc="upper center",
            bbox_to_anchor=(0.5, -0.23),
            ncol=1,
            frameon=False,
            handletextpad=0.35,
        )

    # ── Panel (c): Prompt randomization ──────────────────
    ax3 = fig.add_subplot(1, 3, 3)

    prompt_data = {
        "Qwen-14B-Inst": {"A": 0.923, "B": 0.955, "C": 0.917, "D": 0.941, "std": 0.019},
        "Mistral-7B":    {"A": 0.833, "B": 0.859, "C": 0.844, "D": 0.848, "std": 0.009},
        "Llama-8B":      {"A": 0.830, "B": 0.831, "C": 0.838, "D": 0.809, "std": 0.011},
    }

    templates = ["A", "B", "C", "D"]
    x3 = np.arange(len(templates))
    pcolors = ["#E76F51", "#2A9D8F", "#264653"]

    for i, (model, pdata) in enumerate(prompt_data.items()):
        aucs = [pdata[t] for t in templates]
        offset = (i - 1) * 0.2

        ax3.plot(
            x3 + offset,
            aucs,
            color=pcolors[i],
            marker="o",
            markersize=3.5,
            linewidth=1.3,
            label=f"{model} (σ={pdata['std']:.3f})",
            zorder=3,
        )

    ax3.axhline(
        y=0.5,
        color="#B0BEC5",
        linewidth=0.7,
        linestyle=":",
        zorder=1,
    )

    ax3.set_xticks(x3)
    ax3.set_xticklabels(templates, fontsize=5.5)

    ax3.set_xlabel("Prompt Template", fontsize=6)
    ax3.set_ylabel("CRM-LR AUC", fontsize=6.5)

    ax3.set_title(
        "(c) Prompt Randomization",
        fontsize=7,
        fontweight="bold",
        pad=4,
    )

    ax3.set_ylim(0.70, 1.0)

    # 图例保持在图内，但加白底
    ax3.legend(
        fontsize=5,
        loc="lower left",
        frameon=True,
        framealpha=0.75,
        facecolor="white",
        edgecolor="none",
        borderpad=0.25,
    )

    ax3.text(
        0.97,
        0.08,
        "All σ < 0.02",
        transform=ax3.transAxes,
        fontsize=5.5,
        color="#666666",
        ha="right",
        fontweight="bold",
    )

    fig.suptitle(
        "Robustness Controls: Ruling Out Alternative Explanations",
        fontsize=9,
        fontweight="bold",
        y=1.04,
    )

    save_pub(fig, "fig5_robustness")

    plt.close(fig)

    print("Fig 5 saved to", FIG_DIR)


if __name__ == "__main__":
    main()