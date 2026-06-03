#!/usr/bin/env python3
"""
Fig 2: Main Results — CRM vs Baselines Across Nine Models.
Core empirical claim: CRM consistently outperforms likelihood-based baselines
and surface-level features, with architecture-dependent gain margins.
"""

import json
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch


mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,

    "font.size": 7,
    "axes.titlesize": 8,
    "axes.titleweight": "bold",
    "axes.labelsize": 7,
    "legend.fontsize": 5.8,

    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.8,

    "legend.frameon": False,

    "axes.grid": True,
    "grid.alpha": 0.08,
    "grid.linestyle": "-",

    "lines.linewidth": 1.3,
    "lines.markersize": 4,

    "xtick.labelsize": 5.5,
    "ytick.labelsize": 6.5,
})


FIG_DIR = Path(__file__).resolve().parent
DATA_DIR = FIG_DIR / "data"


CRM_COLOR = "#E76F51"
SURFACE_COLOR = "#B0BEC5"
TIER1_COLOR = "#D5DDE2"

FAMILY_COLORS = {
    "Llama": "#264653",
    "Mistral": "#2A9D8F",
    "Qwen": "#E76F51",
}


DISPLAY = [
    ("Qwen2.5-14B-Inst", "qwen-14b-instruct", "Qwen"),
    ("Qwen2.5-32B-Inst", "qwen-32b-instruct", "Qwen"),
    ("Qwen2.5-14B", "qwen-14b-base", "Qwen"),
    ("Mistral-7B-v0.3", "mistral-base", "Mistral"),
    ("Qwen2.5-7B-Inst", "qwen-7b-instruct", "Qwen"),
    ("Qwen2.5-7B", "qwen-base-7b", "Qwen"),
    ("Mistral-7B-Inst", "mistral-instruct", "Mistral"),
    ("Llama-3.1-8B", "llama-base", "Llama"),
    ("Llama-3.1-8B-Inst", "llama-instruct", "Llama"),
]


def save_pub(fig, filename, dpi=600):
    for ext in ["svg", "pdf", "png"]:
        fig.savefig(
            FIG_DIR / f"{filename}.{ext}",
            bbox_inches="tight",
            dpi=dpi,
        )


def main():
    with open(DATA_DIR / "all_results.json") as f:
        main_data = json.load(f)

    with open(DATA_DIR / "comprehensive_baselines.json") as f:
        comp_data = json.load(f)

    models = main_data["models"]

    fig, ax = plt.subplots(figsize=(3.55, 4.05))

    n_models = len(DISPLAY)
    y = np.arange(n_models)
    height = 0.22

    crm_aucs = []
    crm_cis = []
    surf_aucs = []
    tier1_aucs = []
    model_labels = []
    family_labels = []

    for display_name, model_key, family in DISPLAY:
        md = models[model_key]

        crm = md["lr_auc"]

        # 95% CI: 1.96 * std / sqrt(n_folds)
        ci = 1.96 * md["lr_std"] / np.sqrt(5)

        # Best Tier 1 likelihood baseline
        bls = md["baselines"]
        best_name = max(bls, key=lambda x: bls[x]["auc_mean"])
        best_auc = bls[best_name]["auc_mean"]

        # L1+L2 surface baseline
        if model_key in comp_data:
            l1l2 = comp_data[model_key]["baselines"]["L1_L2"]["lr_auc"]
        else:
            l1l2 = 0.5

        crm_aucs.append(crm)
        crm_cis.append(ci)
        surf_aucs.append(l1l2)
        tier1_aucs.append(best_auc)
        model_labels.append(display_name)
        family_labels.append(family)

    # ── Bars ─────────────────────────────────────────────
    ax.barh(
        y + height,
        crm_aucs,
        height,
        color=CRM_COLOR,
        edgecolor="white",
        linewidth=0.4,
        label="CRM-LR",
        zorder=3,
    )

    ax.barh(
        y,
        surf_aucs,
        height,
        color=SURFACE_COLOR,
        edgecolor="white",
        linewidth=0.4,
        label="L1+L2 (surface)",
        zorder=2,
    )

    ax.barh(
        y - height,
        tier1_aucs,
        height,
        color=TIER1_COLOR,
        edgecolor="white",
        linewidth=0.4,
        label="Best likelihood baseline",
        zorder=2,
    )

    # ── Error bars on CRM ────────────────────────────────
    ax.errorbar(
        np.array(crm_aucs),
        y + height,
        xerr=crm_cis,
        fmt="none",
        ecolor="#888888",
        elinewidth=0.6,
        capsize=1.5,
        zorder=4,
    )

    # ── Value labels on CRM bars ─────────────────────────
    # 数字放在橙色柱子中段：
    # 不靠左侧 family 色条/模型名，也不靠右侧 error bar。
    x_left_visible = 0.35

    for yi, auc in zip(y, crm_aucs):
        label_x = x_left_visible + 0.58 * (auc - x_left_visible)

        ax.text(
            label_x,
            yi + height,
            f"{auc:.3f}",
            va="center",
            ha="center",
            fontsize=5.2,
            color="white",
            fontweight="bold",
            zorder=6,
            clip_on=True,
        )

    # ── Δ annotation ─────────────────────────────────────
    for yi, crm_a, t1_a in zip(y, crm_aucs, tier1_aucs):
        delta = crm_a - t1_a

        ax.text(
            max(crm_a, t1_a) + 0.065,
            yi,
            f"$\\Delta$=+{delta:.3f}",
            va="center",
            ha="left",
            fontsize=5.2,
            color="#2A9D8F",
            fontweight="bold",
            clip_on=False,
            zorder=5,
        )

    # Chance line
    ax.axvline(
        x=0.5,
        color="#B0BEC5",
        linewidth=0.7,
        linestyle=":",
        zorder=1,
    )

    # ── Axes ─────────────────────────────────────────────
    ax.set_yticks(y)
    ax.set_yticklabels(model_labels, fontsize=5.7)

    # 关键修改：
    # y 轴标签往左挪，给 family 色条留出单独位置。
    ax.tick_params(axis="y", pad=9, length=0)

    ax.set_xlabel("LR AUC (5-fold CV)", fontsize=6.5)

    # 右侧留更多空间给 Δ
    ax.set_xlim(0.35, 1.13)

    # ── Family color strips on left ──────────────────────
    # 关键修改：
    # 从 -0.06 改到 -0.025，放在模型名和柱图之间，避免压到标签。
    for yi, fam in zip(y, family_labels):
        ax.text(
            -0.025,
            yi,
            "|",
            fontsize=10,
            color=FAMILY_COLORS[fam],
            fontweight="bold",
            va="center",
            ha="center",
            transform=ax.get_yaxis_transform(),
            clip_on=False,
        )

    # ── Title ────────────────────────────────────────────
    ax.set_title(
        "CRM Consistently Exceeds Likelihood and Surface Baselines",
        fontsize=7.5,
        fontweight="bold",
        pad=8,
    )

    # ── Legends outside axes ─────────────────────────────
    method_handles = [
        Patch(color=CRM_COLOR, label="CRM-LR"),
        Patch(color=SURFACE_COLOR, label="L1+L2 (surface)"),
        Patch(color=TIER1_COLOR, label="Best likelihood baseline"),
    ]

    family_handles = [
        Patch(color=color, label=fam)
        for fam, color in FAMILY_COLORS.items()
    ]

    # 方法图例
    fig.legend(
        handles=method_handles,
        ncol=3,
        fontsize=5.5,
        loc="lower center",
        bbox_to_anchor=(0.56, 0.055),
        frameon=False,
        columnspacing=0.9,
        handletextpad=0.4,
    )

    # Family 图例保持原来的 title="Family" 形式
    fig.legend(
        handles=family_handles,
        ncol=3,
        fontsize=5.2,
        title="Family",
        title_fontsize=5.5,
        loc="lower center",
        bbox_to_anchor=(0.56, 0.010),
        frameon=False,
        columnspacing=0.9,
        handletextpad=0.4,
    )

    # 左边距从 0.30 增到 0.34，给模型名和 family 色条留空间
    fig.subplots_adjust(
        left=0.34,
        right=0.96,
        bottom=0.18,
        top=0.92,
    )

    save_pub(fig, "fig2_main_results")

    plt.close(fig)

    print("Fig 2 saved to", FIG_DIR)


if __name__ == "__main__":
    main()