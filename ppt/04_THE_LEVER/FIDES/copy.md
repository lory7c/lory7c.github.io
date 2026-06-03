# FIDES
> ARR / EMNLP

## Background
When retrieved evidence contradicts parametric memory, contrastive decoding amplifies context-conditioned output to suppress parametric bias. Existing methods assume this bias is uniform across tokens, over-penalizing safe tokens while under-correcting conflicted ones.

## Content
We reveal token-level conflict concentration and propose FIDES, a training-free decoder that fuses three complementary internal signals—output surface, hidden representations, and prediction trajectory—to govern intervention strength at each decoding step.

## Core Contribution
We reframe contrastive decoding from "how much contrast" to "where to apply it." The three-layer fusion mechanism enables per-token adaptive intervention.

## Experimental Result
FIDES achieves the highest context fidelity in all 12 settings across three benchmarks and four 7B/8B backbones, outperforming the strongest training-free baseline by +3.0 to +12.8 points. At 70B scale, fidelity reaches 92–94% and F1 reaches 62–63%.

## Key Numbers
- +3.0 to +12.8 points over strongest baseline
- 12 settings × 3 benchmarks × 4 backbones
- 70B: 92–94% fidelity, 62–63% F1
