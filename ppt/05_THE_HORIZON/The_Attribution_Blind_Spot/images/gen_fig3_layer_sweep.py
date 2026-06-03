#!/usr/bin/env python3
"""
Fig 2: Layer-wise Source Signal Localization.
Core empirical discovery: source information is non-monotonically localized
to specific layers in architecture-dependent patterns.

4 panels: Mistral-7B, Qwen2.5-7B, Qwen2.5-14B-Inst, Llama-3.1-8B
X-axis: HuggingFace layer number
Y-axis: Single-layer LTS probe LR AUC (5-fold CV)
"""
import json
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler

# --- Publication defaults (EMNLP 2-col) ---
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "font.size": 7,
    "axes.titlesize": 8,
    "axes.titleweight": "bold",
    "axes.labelsize": 7,
    "legend.fontsize": 6,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.8,
    "legend.frameon": False,
    "axes.grid": True,
    "grid.alpha": 0.12,
    "grid.linestyle": "-",
    "lines.linewidth": 1.5,
    "lines.markersize": 3.5,
    "xtick.labelsize": 6.5,
    "ytick.labelsize": 6.5,
})

SEED = 42
FIG_DIR = Path(__file__).resolve().parent
DATA_DIR = FIG_DIR / "data"
FEATURES_DIR = DATA_DIR / "features"

# Ocean Dusk palette
COLORS = {
    "mistral": "#2A9D8F",
    "qwen7b": "#E9C46A",
    "qwen14b": "#E76F51",
    "llama": "#264653",
}

MODELS = [
    ("Mistral-7B-v0.3", "mistral-base", COLORS["mistral"], "Mid-layer peak\n(L18, AUC 0.892)"),
    ("Qwen2.5-7B", "qwen-base-7b", COLORS["qwen7b"], "Early-mid peak\n(L10, AUC 0.902)"),
    ("Qwen2.5-14B-Inst", "qwen-14b-instruct", COLORS["qwen14b"], "Bimodal\n(L6 + L21)"),
    ("Llama-3.1-8B", "llama-base", COLORS["llama"], "Scattered late\n(L28, AUC 0.753)"),
]


def compute_per_layer_auc(features_path):
    data = np.load(features_path)
    X_full = data["X"]
    y = data["y"]
    layers = data["layers"]
    X = X_full[:, 3:]  # L3 per-layer LTS features
    n_layers = X.shape[1]

    results = []
    for l in range(n_layers):
        X_single = X[:, l:l + 1]
        X_single = np.nan_to_num(X_single, nan=0.0, posinf=1e6, neginf=-1e6)
        X_single = np.clip(X_single, -1e6, 1e6)
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_single)
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
        aucs = []
        for train_idx, test_idx in skf.split(X_scaled, y):
            X_train, X_test = X_scaled[train_idx], X_scaled[test_idx]
            y_train, y_test = y[train_idx], y[test_idx]
            lr = LogisticRegression(C=1.0, max_iter=2000, class_weight="balanced",
                                    random_state=SEED)
            lr.fit(X_train, y_train)
            aucs.append(roc_auc_score(y_test, lr.predict_proba(X_test)[:, 1]))
        results.append({
            "layer_hf": int(layers[l]),
            "auc": float(np.mean(aucs)),
            "std": float(np.std(aucs)),
        })
    return sorted(results, key=lambda x: x["layer_hf"])


def save_pub(fig, filename, dpi=600):
    for ext in ["svg", "pdf", "png"]:
        fig.savefig(FIG_DIR / f"{filename}.{ext}", bbox_inches="tight", dpi=dpi)


def main():
    fig, axes = plt.subplots(1, 4, figsize=(6.8, 1.8), sharey=False)
    fig.subplots_adjust(wspace=0.35)

    for ax, (display_name, model_key, color, pattern_label) in zip(axes, MODELS):
        features_path = FEATURES_DIR / model_key / "features.npz"
        per_layer = compute_per_layer_auc(features_path)

        layers = [p["layer_hf"] for p in per_layer]
        aucs = [p["auc"] for p in per_layer]
        stds = [p["std"] for p in per_layer]

        # AUC curve
        ax.plot(layers, aucs, color=color, linewidth=1.8, marker="o",
                markersize=3, markeredgecolor="white", markeredgewidth=0.5,
                zorder=3)
        ax.fill_between(layers,
                        [a - s for a, s in zip(aucs, stds)],
                        [a + s for a, s in zip(aucs, stds)],
                        color=color, alpha=0.1)

        # Chance line
        ax.axhline(y=0.5, color="#B0BEC5", linewidth=0.7, linestyle="--", zorder=1)

        # Annotate peak (manual x-offsets to avoid overlap)
        peak_idx = np.argmax(aucs)
        peak_layer = layers[peak_idx]
        peak_auc = aucs[peak_idx]
        x_offset = {14: 10, 16: 10}.get(peak_layer, 0)
        ax.annotate(f"L{peak_layer}", xy=(peak_layer, peak_auc),
                    xytext=(x_offset, 8), textcoords="offset points",
                    ha="center", fontsize=6, fontweight="bold", color=color)

        # Style
        ax.set_title(display_name, fontsize=7.5, fontweight="bold", pad=4)
        ax.set_xlabel("Layer", fontsize=6.5)
        if ax == axes[0]:
            ax.set_ylabel("Single-Layer AUC", fontsize=6.5)
        ax.set_ylim(0.40, 0.88)
        ax.tick_params(labelsize=6)

        # Pattern label (inside plot, top-right)
        ax.text(0.97, 0.93, pattern_label, transform=ax.transAxes,
                ha="right", va="top", fontsize=5.8, color="#555",
                linespacing=1.3)

    # Super-title
    fig.suptitle("Layer-wise Source Signal Localization", fontsize=9,
                 fontweight="bold", y=1.03)

    save_pub(fig, "fig3_layer_sweep")
    plt.close()
    print("Fig 2 saved to", FIG_DIR)


if __name__ == "__main__":
    main()
