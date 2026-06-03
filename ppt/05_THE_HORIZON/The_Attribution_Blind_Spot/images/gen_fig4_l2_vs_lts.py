#!/usr/bin/env python3
"""
Fig 4: Signal Type Comparison — L2 Magnitude vs CRM-LTS Directional.
Shows that CRM-LTS matches or exceeds L2 Multilayer AUC with the same
dimensionality while providing layer-localized interpretability.
L2 captures isotropic magnitude; CRM-LTS captures directional displacement.
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
    "axes.titlesize": 7.5,
    "axes.titleweight": "bold",
    "axes.labelsize": 6.5,
    "legend.fontsize": 5.5,

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
    "ytick.labelsize": 6,
})


FIG_DIR = Path(__file__).resolve().parent
DATA_DIR = FIG_DIR / "data"


MEAN_COLOR = "#B0BEC5"
L2_COLOR = "#7BA7BC"
CRM_COLOR = "#E76F51"
RAW_COLOR = "#2A9D8F"


def save_pub(fig, filename, dpi=600):
    for ext in ["svg", "pdf", "png"]:
        fig.savefig(
            FIG_DIR / f"{filename}.{ext}",
            bbox_inches="tight",
            dpi=dpi,
        )


def main():
    with open(DATA_DIR / "pca_variance_analysis.json") as f:
        pca_data = json.load(f)

    with open(DATA_DIR / "all_results.json") as f:
        main_data = json.load(f)

    with open(DATA_DIR / "comprehensive_baselines.json") as f:
        comp_data = json.load(f)

    models = main_data["models"]
    sweep = pca_data["pca_sweep"]

    rep_models = [
        ("Mistral-7B-v0.3", "mistral-base", "#2A9D8F"),
        ("Qwen2.5-14B-Inst", "qwen-14b-instruct", "#E76F51"),
        ("Llama-3.1-8B", "llama-base", "#264653"),
    ]

    fig, axes = plt.subplots(
        1,
        3,
        figsize=(6.8, 2.05),
    )

    fig.subplots_adjust(
        left=0.075,
        right=0.99,
        bottom=0.30,
        top=0.78,
        wspace=0.36,
    )

    categories = [
        "Mean LTS\n(1 dim)",
        "L2 Multi\n(L dim)",
        "CRM-LTS\n(L dim)",
        "Raw Probe\n(~4000 dim)",
    ]

    for ax, (display_name, model_key, color) in zip(axes, rep_models):
        md = models[model_key]
        cb = comp_data[model_key]["baselines"]

        crm_auc = md["lr_auc"]
        crm_ci = 1.96 * md["lr_std"] / np.sqrt(5)

        l2_multi = sweep[model_key]["l2"]
        mean_lts = cb["Mean_TRI_scalar"]["lr_auc"]

        raw_probe_path = DATA_DIR / f"hidden_baselines_{model_key}.json"

        raw_auc = None

        try:
            with open(raw_probe_path) as f:
                hb = json.load(f)

            raw_auc = hb.get("lr_auc", hb.get("full_raw_lr_auc", None))

        except FileNotFoundError:
            raw_auc = None

        if raw_auc is None:
            raw_auc = sweep[model_key]["8d"]

        values = [
            mean_lts,
            l2_multi,
            crm_auc,
            raw_auc,
        ]

        colors = [
            MEAN_COLOR,
            L2_COLOR,
            CRM_COLOR,
            RAW_COLOR,
        ]

        x = np.arange(len(categories))

        bars = ax.bar(
            x,
            values,
            color=colors,
            edgecolor="white",
            linewidth=0.4,
            width=0.55,
            zorder=2,
        )

        # Value labels
        for bar, val in zip(bars, values):
            label_y = min(val + 0.025, 1.045)

            ax.text(
                bar.get_x() + bar.get_width() / 2,
                label_y,
                f"{val:.3f}",
                ha="center",
                va="bottom",
                fontsize=5.5,
                color="#444444",
                fontweight="bold",
                zorder=5,
            )

        # CRM error bar
        ax.errorbar(
            2,
            crm_auc,
            yerr=crm_ci,
            fmt="none",
            ecolor="#888888",
            elinewidth=0.8,
            capsize=3,
            zorder=4,
        )

        # CI text: 保留灰色，贴在 CRM error bar 下端正下方
        ax.text(
            2,
            crm_auc - crm_ci - 0.004,
            f"95% CI\n[{crm_auc - crm_ci:.3f},\n{crm_auc + crm_ci:.3f}]",
            ha="center",
            va="top",
            fontsize=4.8,
            color="black",
            linespacing=1.1,
            zorder=6,
        )

        ax.axhline(
            y=0.5,
            color="#B0BEC5",
            linewidth=0.6,
            linestyle=":",
            zorder=1,
        )

        ax.set_xticks(x)

        ax.set_xticklabels(
            categories,
            fontsize=5,
            rotation=0,
        )

        ax.set_ylim(0.35, 1.08)

        ax.set_title(
            display_name,
            fontsize=7,
            fontweight="bold",
            pad=4,
        )

        if ax == axes[0]:
            ax.set_ylabel("LR AUC", fontsize=6.5)

        # Dimension label:
        # 放到坐标轴外右上角，避免和 Raw Probe bar / 数值标签重叠
        dim = md["feature_dim"]

        ax.text(
            0.98,
            1.015,
            f"L={dim}",
            transform=ax.transAxes,
            fontsize=5.5,
            color="#888888",
            ha="right",
            va="bottom",
            clip_on=False,
            zorder=7,
        )

        # Highlight CRM-LTS bar
        bars[2].set_edgecolor("#C0392B")
        bars[2].set_linewidth(1.2)

    legend_patches = [
        Patch(color=MEAN_COLOR, label="Mean LTS (1d scalar)"),
        Patch(color=L2_COLOR, label="L2 Multilayer (magnitude)"),
        Patch(color=CRM_COLOR, label="CRM-LTS (directional)"),
        Patch(color=RAW_COLOR, label="Raw probe / PCA-8d (ceiling)"),
    ]

    fig.legend(
        handles=legend_patches,
        ncol=4,
        fontsize=5.2,
        bbox_to_anchor=(0.5, 0.13),
        loc="upper center",
        frameon=False,
        columnspacing=0.9,
        handletextpad=0.4,
    )

    fig.suptitle(
        "Same Dimensionality, Different Signal: Magnitude vs. Direction",
        fontsize=9,
        fontweight="bold",
        y=1.03,
    )

    save_pub(fig, "fig4_l2_vs_lts")

    plt.close(fig)

    print("Fig 4 saved to", FIG_DIR)


if __name__ == "__main__":
    main()