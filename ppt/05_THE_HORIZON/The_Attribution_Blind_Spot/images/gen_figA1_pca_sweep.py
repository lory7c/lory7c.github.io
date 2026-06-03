#!/usr/bin/env python3
"""
Fig 3: PCA Dimension Sweep — Dimensionality of Source Information.
Shows that PC1 alone is insufficient (architecture-dependent, chance→ceiling),
and that 4 PCs is the critical threshold for reliable source discrimination.

Multi-line plot: AUC vs PCA dimensions (1d, 2d, 4d, 8d)
One line per model, grouped by family (color).
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
    "axes.labelsize": 7,
    "legend.fontsize": 5.8,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.8,
    "legend.frameon": False,
    "axes.grid": True,
    "grid.alpha": 0.12,
    "grid.linestyle": "-",
    "lines.linewidth": 1.3,
    "lines.markersize": 4,
    "xtick.labelsize": 6.5,
    "ytick.labelsize": 6.5,
})

FIG_DIR = Path(__file__).resolve().parent
DATA_DIR = FIG_DIR / "data"

# Family colors: Llama=teal, Mistral=ocean, Qwen=coral range
FAMILY = {
    "llama-base": ("Llama", "#264653", "s"),
    "llama-instruct": ("Llama-Inst", "#264653", "o"),
    "mistral-base": ("Mistral", "#2A9D8F", "D"),
    "mistral-instruct": ("Mistral-Inst", "#2A9D8F", "^"),
    "qwen-base-7b": ("Qwen-7B", "#E76F51", "p"),
    "qwen-7b-instruct": ("Qwen-7B-Inst", "#E9C46A", "v"),
    "qwen-14b-base": ("Qwen-14B", "#F4A261", "h"),
    "qwen-14b-instruct": ("Qwen-14B-Inst", "#E76F51", "X"),
    "qwen-32b-instruct": ("Qwen-32B-Inst", "#F4A261", "d"),
}


def save_pub(fig, filename, dpi=600):
    for ext in ["svg", "pdf", "png"]:
        fig.savefig(FIG_DIR / f"{filename}.{ext}", bbox_inches="tight", dpi=dpi)


def main():
    with open(DATA_DIR / "pca_variance_analysis.json") as f:
        data = json.load(f)

    sweep = data["pca_sweep"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 2.6))
    fig.subplots_adjust(wspace=0.30)

    dims = ["1d", "2d", "4d", "8d"]
    x_positions = [1, 2, 3, 4]

    # --- Panel (a): All models overlay ---
    for model_key, (label, color, marker) in FAMILY.items():
        if model_key not in sweep:
            continue
        aucs = [sweep[model_key][d] for d in dims]
        ls = "--" if "instruct" in model_key else "-"
        ax1.plot(x_positions, aucs, color=color, marker=marker, markersize=3.5,
                linewidth=1.2, linestyle=ls, label=label, alpha=0.85)

    ax1.axhline(y=0.5, color="#B0BEC5", linewidth=0.7, linestyle=":", zorder=1)
    ax1.set_xticks(x_positions)
    ax1.set_xticklabels(["PC1", "PC2", "PC4", "PC8"])
    ax1.set_ylabel("LR AUC")
    ax1.set_title("(a) All Models", fontsize=7.5, fontweight="bold", pad=4)
    ax1.set_ylim(0.40, 1.02)
    ax1.legend(
        ncol=2,
        fontsize=4.8,
        loc="lower right",
        frameon=True,
        framealpha=0.75,
        facecolor="white",
        edgecolor="none",
        borderpad=0.25,
        columnspacing=0.5,
        handletextpad=0.35,
    )

    # --- Panel (b): Family means with spread ---
    families = {
        "Llama": ["llama-base", "llama-instruct"],
        "Mistral": ["mistral-base", "mistral-instruct"],
        "Qwen": ["qwen-base-7b", "qwen-7b-instruct", "qwen-14b-base",
                  "qwen-14b-instruct", "qwen-32b-instruct"],
    }
    fam_colors = {"Llama": "#264653", "Mistral": "#2A9D8F", "Qwen": "#E76F51"}
    fam_offsets = {"Llama": -0.12, "Mistral": 0.0, "Qwen": 0.12}

    for fam_name, fam_keys in families.items():
        fam_aucs = {d: [] for d in dims}
        for mk in fam_keys:
            if mk in sweep:
                for d in dims:
                    fam_aucs[d].append(sweep[mk][d])

        means = [np.mean(fam_aucs[d]) for d in dims]
        stds = [np.std(fam_aucs[d]) for d in dims]
        offset = fam_offsets[fam_name]
        x_off = [x + offset for x in x_positions]

        ax2.errorbar(x_off, means, yerr=stds, color=fam_colors[fam_name],
                     linewidth=1.5, marker="o", markersize=4,
                     markeredgecolor="white", markeredgewidth=0.5,
                     capsize=2, capthick=1, label=fam_name)

    ax2.axhline(y=0.5, color="#B0BEC5", linewidth=0.7, linestyle=":", zorder=1)
    ax2.set_xticks(x_positions)
    ax2.set_xticklabels(["PC1", "PC2", "PC4", "PC8"])
    ax2.set_ylabel("LR AUC")
    ax2.set_title("(b) Family Means (±1σ)", fontsize=7.5, fontweight="bold", pad=4)
    ax2.set_ylim(0.40, 1.02)
    ax2.legend(fontsize=6, bbox_to_anchor=(0.97, 0.15), loc="lower right")

    # Annotate critical transition
    ax2.annotate(
        "2d→4d\ncritical transition",
        xy=(3, 0.88),
        xytext=(3.72, 0.88),
        arrowprops=dict(
            arrowstyle="->",
            color="#888",
            lw=0.8,
        ),
        fontsize=5.8,
        color="#666",
        ha="left",
        va="center",
    )
    fig.suptitle("Dimensionality of Source Information", fontsize=9,
                 fontweight="bold", y=1.03)

    save_pub(fig, "figA1_pca_sweep")
    plt.close()
    print("Fig 3 saved to", FIG_DIR)


if __name__ == "__main__":
    main()
