#!/usr/bin/env python3
"""
Fig 5: Leave-One-Layer-Out Ablation — Redundancy of Source Information.
Shows that removing any single LTS layer does not substantially decrease AUC,
demonstrating redundant encoding and justifying the multi-layer trajectory.

Per-layer ΔAUC (AUC_removed - AUC_full) for each model.
Positive values = AUC improves when layer is removed (layer contributes noise).
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
    "lines.linewidth": 1.2,
    "lines.markersize": 4,
    "xtick.labelsize": 5.5,
    "ytick.labelsize": 6,
})

FIG_DIR = Path(__file__).resolve().parent
DATA_DIR = FIG_DIR / "data"
FEATURES_DIR = DATA_DIR / "features"

MODELS = [
    ("Mistral-7B", "mistral-base", "#2A9D8F"),
    ("Qwen2.5-7B", "qwen-base-7b", "#E9C46A"),
    ("Llama-8B", "llama-base", "#264653"),
    ("Qwen-14B-Inst", "qwen-14b-instruct", "#E76F51"),
]


def save_pub(fig, filename, dpi=600):
    for ext in ["svg", "pdf", "png"]:
        fig.savefig(FIG_DIR / f"{filename}.{ext}", bbox_inches="tight", dpi=dpi)


def main():
    with open(DATA_DIR / "leave_one_out_ablation.json") as f:
        loo_data = json.load(f)

    fig, axes = plt.subplots(2, 2, figsize=(6.8, 3.8))
    axes = axes.flatten()
    fig.subplots_adjust(hspace=0.45, wspace=0.30)

    for ax, (display_name, model_key, color) in zip(axes, MODELS):
        if model_key not in loo_data:
            continue
        model_data = loo_data[model_key]
        per_layer = model_data["per_layer"]
        baseline = model_data["baseline_auc"]
        peak_hf = model_data.get("peak_hf_layers", [])

        # Load HF layer numbers from NPZ
        import numpy as np
        npz_path = FEATURES_DIR / model_key / "features.npz"
        hf_layers = np.load(npz_path)["layers"]

        # Sort layers by index, map to HF numbers
        sorted_layers = sorted(per_layer.items(), key=lambda x: int(x[0]))
        layer_indices = [int(l) for l, _ in sorted_layers]
        hf_labels = [int(hf_layers[int(l)]) for l, _ in sorted_layers]
        deltas = [v["delta"] for _, v in sorted_layers]
        loo_aucs = [v["loo_auc"] for _, v in sorted_layers]

        # Color bars: positive (improvement) = green, negative (loss) = red
        bar_colors = []
        for d in deltas:
            if d > 0.01:
                bar_colors.append("#2A9D8F")  # improvement
            elif d < -0.001:
                bar_colors.append("#E76F51")  # harmful
            else:
                bar_colors.append("#CCCCCC")  # neutral

        bars = ax.bar(layer_indices, deltas, color=bar_colors, edgecolor="white",
                     linewidth=0.3, zorder=2)

        # Highlight peak layers (HF numbers)
        for i, (li, hf, d) in enumerate(zip(layer_indices, hf_labels, deltas)):
            if hf in peak_hf:
                ax.annotate("*", xy=(li, d), ha="center", va="bottom" if d > 0 else "top",
                           fontsize=7, color="#E76F51", fontweight="bold",
                           xytext=(0, 5 if d > 0 else -8), textcoords="offset points")

        # Baseline line
        ax.axhline(y=0, color="#444", linewidth=0.6, zorder=1)
        ax.axhline(y=np.mean(deltas), color="#888", linewidth=0.5, linestyle="--",
                  zorder=1, alpha=0.5)

        # Annotate max Δ
        max_delta = max(deltas)
        max_idx = layer_indices[deltas.index(max_delta)]
        min_delta = min(deltas)

        # Use HF layer numbers as x-tick labels
        tick_step = max(1, len(layer_indices) // 8)
        tick_pos = layer_indices[::tick_step]
        tick_labs = [f"L{hf_labels[i]}" for i in range(0, len(hf_labels), tick_step)]
        ax.set_xticks(tick_pos)
        ax.set_xticklabels(tick_labs, rotation=30, fontsize=5, ha="right")

        ax.set_title(f"{display_name}  (BL={baseline:.3f})", fontsize=7,
                    fontweight="bold", pad=3)
        ax.set_xlabel("HF Layer", fontsize=6)
        ax.set_ylabel("Δ AUC (removed − full)", fontsize=6)

        # Significance zone
        ax.axhspan(-0.005, 0.005, alpha=0.03, color="#888", zorder=0)
        ax.text(0.98, 0.92, f"max Δ={max_delta:+.3f}\nmin Δ={min_delta:+.3f}",
                transform=ax.transAxes, ha="right", va="top",
                fontsize=5.5, color="#555")

    fig.suptitle("Leave-One-Layer-Out: No Single Layer is Uniquely Causal",
                 fontsize=9, fontweight="bold", y=1.02)

    save_pub(fig, "figA2_loo_ablation")
    plt.close()
    print("Fig 5 saved to", FIG_DIR)


if __name__ == "__main__":
    main()
