#!/usr/bin/env python3
"""Publication-quality figures for FIDES paper.
   All dimensions: ACL/EMNLP single-col 3.3in, full-width 6.8in."""

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ── Publication defaults ──────────────────────────────────────────
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "font.size": 7,
    "axes.titlesize": 8,
    "axes.titleweight": "bold",
    "axes.labelsize": 7,
    "legend.fontsize": 6.5,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.8,
    "legend.frameon": False,
    "axes.grid": True,
    "grid.alpha": 0.15,
    "grid.linestyle": "-",
    "lines.linewidth": 1.5,
    "lines.markersize": 4,
})

FIG_SINGLE = (3.25, 2.5)
FIG_FULL   = (6.75, 2.8)

# ── Ocean Dusk palette ────────────────────────────────────────────
COLORS = ["#264653", "#2A9D8F", "#E9C46A", "#F4A261", "#E76F51",
          "#0072B2", "#56B4E9", "#8C8C8C"]
OUR_COLOR   = "#E76F51"    # burnt coral – FIDES
RAG_COLOR   = "#B0BEC5"    # cool gray – Standard RAG
CAD_COLOR   = "#2A9D8F"    # teal – CAD
ADA_COLOR   = "#E9C46A"    # gold – AdaCAD

OUTDIR = "generated"

def save_pub(fig, filename, dpi=600):
    for fmt, ext in [("svg", "svg"), ("pdf", "pdf"), ("png", "png")]:
        fig.savefig(f"{OUTDIR}/{filename}.{ext}", bbox_inches="tight",
                    dpi=dpi if ext != "svg" else None)

# ═══════════════════════════════════════════════════════════════════
# FIGURE 1: Scaling Trend (CF + F1 vs Model Size)
# ═══════════════════════════════════════════════════════════════════

model_sizes = ["7B\n(LLaMA2-7B)", "13B\n(LLaMA2-13B)", "70B\n(LLaMA3-70B)"]
x_pos = [0, 1, 2]

# NQ-Swap CF
cf_data = {
    "Standard RAG":   [66.83, 69.12, 73.54],
    "CAD":            [75.46, 78.34, 83.92],
    "AdaCAD":         [77.94, 80.95, 86.82],
    "FIDES (Ours)":   [81.67, 84.82, 92.45],
}
# NQ-Swap F1
f1_data = {
    "Standard RAG":   [35.41, 36.82, 42.15],
    "CAD":            [31.13, 33.05, 36.88],
    "AdaCAD":         [40.71, 42.16, 48.95],
    "FIDES (Ours)":   [46.24, 48.23, 61.82],
}

colors_map = {"Standard RAG": RAG_COLOR, "CAD": CAD_COLOR,
              "AdaCAD": ADA_COLOR, "FIDES (Ours)": OUR_COLOR}
markers = {"Standard RAG": "s", "CAD": "^", "AdaCAD": "D", "FIDES (Ours)": "o"}
styles = {"Standard RAG": "--", "CAD": "-.", "AdaCAD": ":",
          "FIDES (Ours)": "-"}

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.25, 3.2))

for method, vals in cf_data.items():
    c = colors_map[method]
    m = markers[method]
    ls = styles[method]
    lw = 2.2 if method == "FIDES (Ours)" else 1.3
    z = 5 if method == "FIDES (Ours)" else 2
    ax1.plot(x_pos, vals, marker=m, color=c, linestyle=ls, linewidth=lw,
             markersize=5 if method == "FIDES (Ours)" else 3.5, zorder=z,
             label=method, markeredgecolor="white", markeredgewidth=0.5)

ax1.set_xticks(x_pos)
ax1.set_xticklabels(model_sizes, fontsize=6.5)
ax1.set_ylabel("Context Fidelity (CF, %)", fontsize=7)
ax1.set_title("(a)  Context Fidelity", fontsize=8, fontweight="bold")
ax1.set_ylim(30, 97)

for method, vals in f1_data.items():
    c = colors_map[method]
    m = markers[method]
    ls = styles[method]
    lw = 2.2 if method == "FIDES (Ours)" else 1.3
    z = 5 if method == "FIDES (Ours)" else 2
    ax2.plot(x_pos, vals, marker=m, color=c, linestyle=ls, linewidth=lw,
             markersize=5 if method == "FIDES (Ours)" else 3.5, zorder=z,
             label=method, markeredgecolor="white", markeredgewidth=0.5)

ax2.set_xticks(x_pos)
ax2.set_xticklabels(model_sizes, fontsize=6.5)
ax2.set_ylabel("Token-Level F1 (%)", fontsize=7)
ax2.set_title("(b)  Token-Level F1", fontsize=8, fontweight="bold")
ax2.set_ylim(28, 66)

handles, labels = ax2.get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=4, fontsize=6.5,
           bbox_to_anchor=(0.5, -0.02))
fig.tight_layout(rect=[0, 0.02, 1, 1])
save_pub(fig, "fides_scaling_trend")

# ═══════════════════════════════════════════════════════════════════
# FIGURE 2 + 3: Noisy Retrieval + Signal Complementarity (merged, 1×2)
# ═══════════════════════════════════════════════════════════════════

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(FIG_SINGLE[0] * 1.6, 2.4),
                          gridspec_kw={'width_ratios': [0.82, 1.18]})

# --- Panel (a): Noisy Retrieval ---
noise_levels = ["Clean\n(0%)", "20%\nNoise", "50%\nNoise"]
methods = ["Standard RAG", "CAD", "FIDES"]
data = {
    "Standard RAG": [28.4, 22.1, 15.6],
    "CAD":          [26.5, 19.3, 12.4],
    "FIDES":        [29.2, 26.8, 23.5],
}
bar_colors = [RAG_COLOR, CAD_COLOR, OUR_COLOR]

x = np.arange(len(noise_levels))
n = len(methods)
width = 0.18
for i, (method, vals) in enumerate(data.items()):
    offset = (i - n / 2 + 0.5) * width
    bars = ax1.bar(x + offset, vals, width * 0.90, label=method,
                  color=bar_colors[i], edgecolor="white", linewidth=0.5, zorder=3)
    for bar, v in zip(bars, vals):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                f"{v:.1f}", ha="center", va="bottom", fontsize=5, color="#444",
                fontweight="bold")

ax1.annotate("FIDES\nretains", xy=(2, 24.0), xytext=(2.3, 32),
            fontsize=5, color=OUR_COLOR, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=OUR_COLOR, lw=0.8))

ax1.set_xticks(x)
ax1.set_xticklabels(noise_levels, fontsize=5.5)
ax1.set_ylabel("Accuracy (%)", fontsize=6.5)
ax1.set_ylim(0, 36)
ax1.legend(loc="upper right", fontsize=5)
ax1.set_title("(a)  Noisy Retrieval", fontsize=7, fontweight="bold")

# --- Panel (b): Signal Complementarity ---
variants = ["Opp\nonly", "Opp\n+ Shift", "Opp\n+ Noise", "Full\n(3)"]
cf_vals   = [73.61, 82.96, 79.52, 87.65]
em_vals   = [33.92, 39.21, 37.85, 42.88]
f1_vals   = [37.52, 46.73, 42.65, 52.91]

x2 = np.arange(len(variants))

bars_cf = ax2.bar(x2 - width, cf_vals, width * 0.90, color=COLORS[0],
                 edgecolor="white", linewidth=0.5, label="CF", zorder=3)
bars_em = ax2.bar(x2, em_vals, width * 0.90, color=COLORS[1],
                 edgecolor="white", linewidth=0.5, label="EM", zorder=3)
bars_f1 = ax2.bar(x2 + width, f1_vals, width * 0.90, color=OUR_COLOR,
                 edgecolor="white", linewidth=0.5, label="F1", zorder=3)

for bar, v in zip(bars_cf, cf_vals):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
            f"{v:.1f}", ha="center", va="bottom", fontsize=5, color=COLORS[0],
            fontweight="bold")
for bar, v in zip(bars_em, em_vals):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
            f"{v:.1f}", ha="center", va="bottom", fontsize=5, color=COLORS[1])
for bar, v in zip(bars_f1, f1_vals):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
            f"{v:.1f}", ha="center", va="bottom", fontsize=5, color=OUR_COLOR,
            fontweight="bold")

for bar in bars_cf[3], bars_em[3], bars_f1[3]:
    bar.set_edgecolor("#222")
    bar.set_linewidth(1.0)
    bar.set_zorder(5)

ax2.set_xticks(x2)
ax2.set_xticklabels(variants, fontsize=5.5)
ax2.set_ylabel("Score (%)", fontsize=6.5)
ax2.set_ylim(0, 98)
ax2.legend(loc="upper left", ncol=3, fontsize=5)
ax2.set_title("(b)  Signal Complementarity", fontsize=7, fontweight="bold")

fig.tight_layout(w_pad=0.5)
fig.subplots_adjust(left=0.04)
save_pub(fig, "fides_noisy_retrieval")

# ═══════════════════════════════════════════════════════════════════
# FIGURE 4: Efficiency Overhead (Horizontal Bar)
# ═══════════════════════════════════════════════════════════════════

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_FULL)

backbones = ["LLaMA3-8B", "Qwen3-8B"]
data = {
    "LLaMA3-8B": {
        "Standard RAG": 31.42, "CAD": 59.63, "AdaCAD": 61.15, "FIDES": 64.52,
    },
    "Qwen3-8B": {
        "Standard RAG": 33.15, "CAD": 60.17, "AdaCAD": 62.11, "FIDES": 66.92,
    },
}

for i, backbone in enumerate(backbones):
    ax = [ax1, ax2][i]
    methods = list(data[backbone].keys())
    latencies = list(data[backbone].values())
    colors = [RAG_COLOR, CAD_COLOR, ADA_COLOR, OUR_COLOR]
    bars = ax.barh(methods, latencies, color=colors, height=0.55,
                   edgecolor="white", linewidth=0.5)
    for bar, v in zip(bars, latencies):
        ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height() / 2,
                f"{v:.1f} ms", va="center", fontsize=6.5, color="#444")
    ax.set_title(backbone, fontsize=8, fontweight="bold")
    ax.set_xlabel("Latency (ms/token)")
    ax.set_xlim(0, 78)
    ax.invert_yaxis()

fig.suptitle("Per-Token Inference Latency", fontsize=9, fontweight="bold", y=1.02)
fig.tight_layout()
save_pub(fig, "fides_efficiency")

print("All 3 figures generated in figs/generated/")
print("  fides_scaling_trend.{svg,pdf,png}")
print("  fides_noisy_retrieval.{svg,pdf,png}")
print("  fides_efficiency.{svg,pdf,png}")
