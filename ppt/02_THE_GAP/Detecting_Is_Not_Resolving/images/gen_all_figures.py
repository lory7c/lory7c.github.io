#!/usr/bin/env python3
"""Generate all figures for the EMNLP 2026 paper.

Figures:
  Fig 1: Methodology overview (KEPT AS-IS, not regenerated)
  Fig 2: Multi-turn escalation curves (2×2 facet, 4 models)
  Fig 3: Monitoring-control gap (dual panel: scatter + grouped bars)
  Fig 4: Evidence timing heatmap (danger rate by timing × turn × model)
  Fig 5: Human validation comparison (judge vs human danger rate)
  Fig 6: API model validation (GPT-4o-mini and GPT-4o escalation)

Usage:  python gen_all_figures.py [fig_number]
  fig_number: 2, 3, 4, 5, 6, or "all" (default: all)
"""

import json
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from collections import defaultdict
import sys, os

# ── Publication Styling (merged academic-plotting) ───────────────────────
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "font.size": 6.5,
    "axes.titlesize": 7, "axes.titleweight": "bold",
    "axes.labelsize": 6.5, "legend.fontsize": 5.5,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.7,
    "legend.frameon": False,
    "axes.grid": True, "grid.alpha": 0.12, "grid.linestyle": "-",
    "lines.linewidth": 1.3, "lines.markersize": 3.5,
    "xtick.labelsize": 5.5,
    "ytick.labelsize": 5.5,
})

def save_pub(fig, filename, dpi=600):
    fig.savefig(f"{filename}.pdf", bbox_inches="tight")
    fig.savefig(f"{filename}.png", dpi=dpi, bbox_inches="tight")
    print(f"  Saved: {filename}.pdf, {filename}.png")

# ── Palettes ─────────────────────────────────────────────────────────────
# Ocean Dusk
OCEAN = ["#264653", "#2A9D8F", "#E9C46A", "#F4A261", "#E76F51",
         "#0072B2", "#56B4E9", "#8C8C8C"]
OUR_CORAL = "#E76F51"
BASELINE_GRAY = "#B0BEC5"

# Okabe-Ito (colorblind-safe)
OKABE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]

# NMI Pastel
NMI = ["#E8EDF2", "#F5F0E8", "#E8F2EE", "#F2E8EF", "#EDEDF5"]

# Venue dimensions (EMNLP/ACL: single 3.3in, full 6.8in)
FIG_SINGLE = (3.3, 2.4)
FIG_FULL = (6.8, 2.8)
FIG_FULL_TALL = (6.8, 3.6)

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Model name mapping ──────────────────────────────────────────────────
MODEL_SHORT = {
    'Qwen2.5-1.5B-Instruct': 'Qwen2.5-1.5B',
    'qwen2.5-7b-instruct': 'Qwen2.5-7B',
    'Mistral-7B-Instruct-v0.1': 'Mistral-7B',
    'Meta-Llama-3-8B-Instruct': 'Llama-3-8B',
}
TIMING_LABELS = {
    'constant': 'Constant',
    'early_only': 'Early Only',
    'late_only': 'Late Only',
    'escalating': 'Escalating',
    'deescalating': 'De-escalating',
    'alternating': 'Alternating',
}
MODEL_COLORS = {
    'Qwen2.5-1.5B': OKABE[0],   # orange
    'Qwen2.5-7B': OKABE[1],      # sky blue
    'Mistral-7B': OKABE[2],       # green
    'Llama-3-8B': OKABE[5],       # vermillion
    'GPT-4o-mini': OCEAN[3],      # sandy orange
    'GPT-4o': OCEAN[0],           # deep teal
}
TIMING_COLORS = {
    'constant': OCEAN[0],
    'early_only': OCEAN[1],
    'late_only': OCEAN[2],
    'escalating': OCEAN[3],
    'deescalating': OCEAN[4],
    'alternating': OCEAN[5],
}
MARKERS = ['o', 's', '^', 'D', 'v', '<']

# ── Data Loading ────────────────────────────────────────────────────────
PROJECT_ROOT = os.path.abspath(os.path.join(OUTPUT_DIR, '..', '..'))

def load_multiturn_data():
    """Load pre-extracted plot data or extract from raw files."""
    plot_file = os.path.join(PROJECT_ROOT, 'results', 'plot_data_multiturn.json')
    if os.path.exists(plot_file):
        with open(plot_file) as f:
            return json.load(f)
    raise FileNotFoundError(f"Run data extraction first: {plot_file}")

def load_api_data():
    plot_file = os.path.join(PROJECT_ROOT, 'results', 'plot_data_api.json')
    if os.path.exists(plot_file):
        with open(plot_file) as f:
            return json.load(f)
    raise FileNotFoundError("Run data extraction first")

def parse_data(raw_data, strategy_filter=None):
    """Parse raw plot data into structured form.
    Returns: dict[model][strategy][timing][turn] = {danger_rate, ack_rate}
    """
    result = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    for k, v in raw_data.items():
        parts = k.split('|')
        if len(parts) == 4:
            model_raw, strategy, timing, turn_str = parts
            turn = int(turn_str.split('=')[1])
            model = MODEL_SHORT.get(model_raw, model_raw)
            if strategy_filter and strategy != strategy_filter:
                continue
            result[model][strategy][timing][turn] = v
    return result

# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 2: Multi-Turn Escalation Curves
# ═══════════════════════════════════════════════════════════════════════════
def fig2_escalation():
    """2×2 faceted line plot showing danger rate escalation across turns
    for 4 models × 6 timing patterns."""
    raw = load_multiturn_data()
    data = parse_data(raw, strategy_filter='baseline')

    models = ['Qwen2.5-1.5B', 'Qwen2.5-7B', 'Mistral-7B', 'Llama-3-8B']
    timings = ['constant', 'early_only', 'late_only', 'escalating', 'deescalating', 'alternating']
    turns = [0, 1, 2, 3]

    fig, axes = plt.subplots(2, 2, figsize=FIG_FULL, sharex=True, sharey=True)
    fig.subplots_adjust(hspace=0.08, wspace=0.06)

    for idx, model in enumerate(models):
        ax = axes[idx // 2][idx % 2]
        for ti, timing in enumerate(timings):
            drs = []
            for turn in turns:
                entry = data.get(model, {}).get('baseline', {}).get(timing, {}).get(turn)
                if entry:
                    drs.append(entry['danger_rate'])
                else:
                    drs.append(np.nan)
            color = TIMING_COLORS[timing]
            marker = MARKERS[ti]
            ax.plot(turns, drs, color=color, marker=marker,
                    markersize=3.5, linewidth=1.2,
                    label=TIMING_LABELS[timing] if idx == 0 else "",
                    zorder=3)
        # Shade conflict turn T2
        ax.axvspan(2, 3, alpha=0.06, color='#D4A252', zorder=0)
        ax.axvline(x=2, color='#D4A252', linewidth=0.5, linestyle='--', alpha=0.5)

        ax.set_title(model, fontsize=8, fontweight='bold')
        if idx >= 2:
            ax.set_xlabel('Turn')
            ax.set_xticks(turns)
        if idx % 2 == 0:
            ax.set_ylabel('Danger Rate')
        ax.set_ylim(-0.05, 1.15)
        ax.yaxis.set_major_locator(mticker.MultipleLocator(0.25))

    # Single legend below
    handles, labels = axes[0][0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=6,
               bbox_to_anchor=(0.5, -0.06), frameon=False, fontsize=5.8)

    # Caption handled by LaTeX
    save_pub(fig, f"{OUTPUT_DIR}/fig2_escalation")
    plt.close(fig)

# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 3: Monitoring-Control Gap
# ═══════════════════════════════════════════════════════════════════════════
def fig3_monitoring_control():
    """Dual panel:
    (a) Scatter: contradiction acknowledgement (T2) vs T3 danger rate
    (b) Grouped bars: T3 danger rate by model, baseline vs reconcile
    """
    raw = load_multiturn_data()
    data = parse_data(raw)  # all strategies

    models = ['Qwen2.5-1.5B', 'Qwen2.5-7B', 'Mistral-7B', 'Llama-3-8B']
    timings = ['constant', 'early_only', 'late_only', 'escalating', 'deescalating', 'alternating']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_FULL,
                                     gridspec_kw={'width_ratios': [1, 1]})

    # Panel (a): Scatter — ack rate (T2) vs T3 danger rate
    for model in models:
        for strategy, style in [('baseline', 'o'), ('reconcile_first', 's')]:
            color = MODEL_COLORS[model]
            for timing in timings:
                ack = data.get(model, {}).get(strategy, {}).get(timing, {}).get(2, {}).get('ack_rate')
                t3dr = data.get(model, {}).get(strategy, {}).get(timing, {}).get(3, {}).get('danger_rate')
                if ack is not None and t3dr is not None:
                    alpha = 0.7 if strategy == 'baseline' else 1.0
                    size = 36 if strategy == 'baseline' else 48
                    ax1.scatter(ack, t3dr, c=color, marker=style, s=size,
                               alpha=alpha, edgecolors='white', linewidth=0.3,
                               zorder=3)
    # Add model averages as large markers
    for model in models:
        for strategy, marker, offset in [('baseline', 'o', -0.01), ('reconcile_first', 's', 0.01)]:
            acks, t3drs = [], []
            for timing in timings:
                ack = data.get(model, {}).get(strategy, {}).get(timing, {}).get(2, {}).get('ack_rate')
                t3dr = data.get(model, {}).get(strategy, {}).get(timing, {}).get(3, {}).get('danger_rate')
                if ack is not None and t3dr is not None:
                    acks.append(ack); t3drs.append(t3dr)
            if acks:
                mean_ack = np.mean(acks); mean_t3 = np.mean(t3drs)
                ax1.scatter(mean_ack, mean_t3, c=MODEL_COLORS[model], marker=marker,
                           s=120, edgecolors='#333', linewidth=1, zorder=5,
                           label=f'{model} ({strategy})' if timing == timings[0] else '')

    ax1.set_xlabel('Contradiction Acknowledged (T2)')
    ax1.set_ylabel('Danger Rate (T3)')
    ax1.set_title('(a) Monitoring–Control Gap', fontsize=8, fontweight='bold')
    ax1.set_xlim(-0.05, 1.15); ax1.set_ylim(-0.05, 1.15)
    ax1.axhline(y=0.5, color='#999', linewidth=0.5, linestyle=':', alpha=0.3)
    ax1.axvline(x=0.5, color='#999', linewidth=0.5, linestyle=':', alpha=0.3)

    # Panel (b): Grouped bars — T3 danger rate by model
    x = np.arange(len(models))
    width = 0.35
    for i, strategy in enumerate(['baseline', 'reconcile_first']):
        t3_means = []
        for model in models:
            t3s = []
            for timing in timings:
                dr = data.get(model, {}).get(strategy, {}).get(timing, {}).get(3, {}).get('danger_rate')
                if dr is not None:
                    t3s.append(dr)
            t3_means.append(np.mean(t3s) if t3s else 0)
        color = '#B0BEC5' if strategy == 'baseline' else OUR_CORAL
        label = 'Baseline' if strategy == 'baseline' else 'Reconcile-First'
        bars = ax2.bar(x + (i - 0.5) * width, t3_means, width * 0.85,
                       color=color, edgecolor='white', linewidth=0.3, label=label)
        for bar, val in zip(bars, t3_means):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                    f'{val:.2f}', ha='center', va='bottom', fontsize=5.5, color='#444')

    ax2.set_xticks(x)
    ax2.set_xticklabels(models, fontsize=6.5)
    ax2.set_ylabel('Mean T3 Danger Rate')
    ax2.set_title('(b) Action-Turn Safety', fontsize=8, fontweight='bold')
    ax2.legend(fontsize=6)
    ax2.set_ylim(0, 1.1)

    fig.suptitle('Monitoring–Control Gap: Detecting Conflict ≠ Resolving It Safely',
                 fontsize=9, fontweight='bold', y=1.01)
    save_pub(fig, f"{OUTPUT_DIR}/fig3_monitoring_control")
    plt.close(fig)

# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 4: Evidence Timing Heatmap
# ═══════════════════════════════════════════════════════════════════════════
def fig4_timing_heatmap():
    """Heatmap: danger rate by timing (rows) × turn (cols) for each model."""
    raw = load_multiturn_data()
    data = parse_data(raw, strategy_filter='baseline')

    models = ['Qwen2.5-1.5B', 'Qwen2.5-7B', 'Mistral-7B', 'Llama-3-8B']
    timings_ordered = ['constant', 'early_only', 'late_only', 'escalating', 'deescalating', 'alternating']
    turns = [0, 1, 2, 3]

    fig, axes = plt.subplots(2, 2, figsize=FIG_FULL)
    fig.subplots_adjust(hspace=0.50, wspace=0.30)

    for idx, model in enumerate(models):
        ax = axes[idx // 2][idx % 2]
        # Build matrix: rows=timings, cols=turns
        matrix = np.zeros((len(timings_ordered), len(turns)))
        for ti, timing in enumerate(timings_ordered):
            for tj, turn in enumerate(turns):
                dr = data.get(model, {}).get('baseline', {}).get(timing, {}).get(turn, {}).get('danger_rate', 0)
                matrix[ti, tj] = dr

        im = ax.imshow(matrix, cmap='YlOrRd', aspect='auto', vmin=0, vmax=1.0)

        ax.set_xticks(range(len(turns)))
        ax.set_xticklabels([f'T{t}' for t in turns])
        ax.set_yticks(range(len(timings_ordered)))
        ax.set_yticklabels([TIMING_LABELS[t] for t in timings_ordered], fontsize=5.8)

        # Annotate cells
        for ti in range(len(timings_ordered)):
            for tj in range(len(turns)):
                val = matrix[ti, tj]
                text_color = 'white' if val > 0.5 else '#333'
                ax.text(tj, ti, f'{val:.2f}', ha='center', va='center',
                       fontsize=6.5, color=text_color, weight='medium')

        ax.set_title(model, fontsize=8, fontweight='bold')

    # Single colorbar
    cbar = fig.colorbar(im, ax=axes, shrink=0.7, aspect=25, pad=0.01)
    cbar.set_label('Danger Rate', fontsize=6.5)

    fig.suptitle('Danger Rate by Evidence Timing Pattern (Baseline Strategy)',
                 fontsize=9, fontweight='bold', y=1.01)
    save_pub(fig, f"{OUTPUT_DIR}/fig4_timing_heatmap")
    plt.close(fig)

# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 5: Human Validation
# ═══════════════════════════════════════════════════════════════════════════
def fig5_human_validation():
    """Human vs judge danger rate comparison."""
    import csv

    # Load human annotations (from annotated file)
    csv_path = os.path.join(PROJECT_ROOT, 'results', 'human_eval_sample_annotated_full.csv')
    if not os.path.exists(csv_path):
        print("  WARNING: human annotation file not found, skipping Fig 5")
        return

    rows = []
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)

    # Aggregate human danger rates by model × strategy
    from collections import Counter
    human_agg = defaultdict(lambda: {'total': 0, 'danger_2plus': 0, 'mean': 0, 'scores': []})
    for r in rows:
        key = (r['model'], r['strategy'])
        score = int(r['human_danger']) if r['human_danger'] else 0
        human_agg[key]['total'] += 1
        human_agg[key]['scores'].append(score)
        if score >= 2:
            human_agg[key]['danger_2plus'] += 1

    # Load judge data
    judge_key_path = os.path.join(PROJECT_ROOT, 'results', 'human_eval_judge_key.csv')
    judge_agg = defaultdict(lambda: {'total': 0, 'danger_2plus': 0, 'mean': 0, 'scores': []})
    if os.path.exists(judge_key_path):
        with open(judge_key_path) as f:
            reader = csv.DictReader(f)
            for r in reader:
                model = r.get('model', '?')
                strategy = r.get('strategy', r.get('prompt_strategy', '?'))
                key = (model, strategy)
                score = int(r.get('judge_danger', r.get('danger', 0)))
                judge_agg[key]['total'] += 1
                judge_agg[key]['scores'].append(score)
                if score >= 2:
                    judge_agg[key]['danger_2plus'] += 1

    fig, axes = plt.subplots(1, 2, figsize=FIG_FULL)

    # Panel (a): Grouped bars — human vs judge danger rate per model
    model_list = sorted(set(k[0] for k in human_agg.keys()))
    x = np.arange(len(model_list))
    width = 0.3

    for i, (label, agg_dict, color) in enumerate([
        ('Human', human_agg, OCEAN[1]),
        ('Judge', judge_agg, OCEAN[4])
    ]):
        rates = []
        for model in model_list:
            for strat in ['baseline', 'reconcile_first']:
                entry = agg_dict.get((model, strat), {'danger_2plus': 0, 'total': 1})
                if entry['total'] > 0:
                    rates.append(entry['danger_2plus'] / entry['total'])
                else:
                    rates.append(0)
        # Average across strategies
        avg_rates = []
        for model in model_list:
            model_rates = []
            for strat in ['baseline', 'reconcile_first']:
                entry = agg_dict.get((model, strat), {'danger_2plus': 0, 'total': 0})
                if entry['total'] > 0:
                    model_rates.append(entry['danger_2plus'] / entry['total'])
            avg_rates.append(np.mean(model_rates) if model_rates else 0)

        bars = axes[0].bar(x + (i - 0.5) * width, avg_rates, width * 0.85,
                          color=color, edgecolor='white', linewidth=0.3,
                          label=f'{label} (DR≥2)')
        for bar, r in zip(bars, avg_rates):
            axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                        f'{r:.2f}', ha='center', va='bottom', fontsize=5.5, color='#444')

    axes[0].set_xticks(x)
    axes[0].set_xticklabels([m.replace('Qwen2.5-', 'Qwen-').replace('Llama-3-', 'Llama-') for m in model_list],
                           fontsize=5.5, rotation=15)
    axes[0].set_ylabel('Danger Rate')
    axes[0].set_title('(a) Human vs. Judge Danger Rates', fontsize=8, fontweight='bold')
    axes[0].legend(fontsize=5.5)
    axes[0].set_ylim(0, 0.6)

    # Panel (b): Human score distribution
    all_human_scores = []
    for r in rows:
        s = int(r['human_danger']) if r['human_danger'] else 0
        all_human_scores.append(s)

    from collections import Counter
    dist = Counter(all_human_scores)
    axes[1].bar([0, 1, 2, 3], [dist.get(i, 0) for i in range(4)],
               color=[NMI[0], NMI[1], OCEAN[3], OCEAN[4]],
               edgecolor='white', linewidth=0.3, width=0.6)
    for i in range(4):
        axes[1].text(i, dist.get(i, 0) + 1, str(dist.get(i, 0)),
                    ha='center', fontsize=6, color='#444')
    axes[1].set_xticks([0, 1, 2, 3])
    axes[1].set_xticklabels(['Safe (0)', 'Suspicious (1)', 'Dangerous (2)', 'Severe (3)'], fontsize=5.5)
    axes[1].set_ylabel('Count (n=194)')
    axes[1].set_title('(b) Human Danger Score Distribution', fontsize=8, fontweight='bold')

    fig.suptitle('Human Validation Confirms Monitoring–Control Gap',
                 fontsize=9, fontweight='bold', y=1.01)
    save_pub(fig, f"{OUTPUT_DIR}/fig5_human_validation")
    plt.close(fig)

# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 6: API Model Validation
# ═══════════════════════════════════════════════════════════════════════════
def fig6_api_validation():
    """GPT-4o-mini and GPT-4o escalation curves (baseline strategy)."""
    raw = load_api_data()
    data = parse_data(raw, strategy_filter='baseline')

    api_models = ['GPT-4o-mini', 'GPT-4o']
    timings = ['constant', 'early_only', 'late_only', 'escalating', 'deescalating', 'alternating']
    turns = [0, 1, 2, 3]

    fig, axes = plt.subplots(1, 2, figsize=FIG_FULL, sharey=True)

    for idx, model in enumerate(api_models):
        ax = axes[idx]
        for ti, timing in enumerate(timings):
            drs = []
            for turn in turns:
                entry = data.get(model, {}).get('baseline', {}).get(timing, {}).get(turn)
                drs.append(entry['danger_rate'] if entry else np.nan)
            ax.plot(turns, drs, color=TIMING_COLORS[timing], marker=MARKERS[ti],
                   markersize=3.5, linewidth=1.2,
                   label=TIMING_LABELS[timing] if idx == 0 else "")
        ax.axvspan(2, 3, alpha=0.06, color='#D4A252', zorder=0)
        ax.axvline(x=2, color='#D4A252', linewidth=0.5, linestyle='--', alpha=0.5)
        ax.set_title(model, fontsize=8, fontweight='bold')
        ax.set_xlabel('Turn')
        ax.set_xticks(turns)
        if idx == 0:
            ax.set_ylabel('Danger Rate')
        ax.set_ylim(-0.05, 1.15)
        ax.yaxis.set_major_locator(mticker.MultipleLocator(0.25))

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=6, bbox_to_anchor=(0.5, -0.06),
              frameon=False, fontsize=5.8)
    fig.suptitle('API Model Escalation Curves (Baseline Strategy)',
                fontsize=9, fontweight='bold', y=1.01)
    save_pub(fig, f"{OUTPUT_DIR}/fig6_api_validation")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════
def main():
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'

    figs = {
        '2': ('Fig 2: Escalation Curves', fig2_escalation),
        '3': ('Fig 3: Monitoring-Control Gap', fig3_monitoring_control),
        '4': ('Fig 4: Timing Heatmap', fig4_timing_heatmap),
        '5': ('Fig 5: Human Validation', fig5_human_validation),
        '6': ('Fig 6: API Validation', fig6_api_validation),
    }

    if which == 'all':
        for name, (desc, fn) in figs.items():
            print(f'\n{"="*50}\nGenerating Fig {name}: {desc}')
            try:
                fn()
            except Exception as e:
                print(f'  ERROR: {e}')
                import traceback; traceback.print_exc()
    else:
        if which in figs:
            desc, fn = figs[which]
            print(f'Generating Fig {which}: {desc}')
            fn()
        else:
            print(f'Unknown figure: {which}. Choose from: {list(figs.keys())}, all')

if __name__ == '__main__':
    main()
