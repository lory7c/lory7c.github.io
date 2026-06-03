# Detecting Is Not Resolving
> ARR / EMNLP

## Background
RAG safety is evaluated in single-turn settings, but real deployment involves multi-turn conversations where evidence accumulates.

## Content
We introduce a multi-turn document-accumulation protocol with six temporal patterns to isolate when and how misleading evidence enters persistent cache.

## Core Contribution
We prove a structural "monitoring–control gap": models detect contradictions, yet this awareness fails to constrain final recommendations. The deficit lies in action selection, not detection.

## Experimental Result
Across 50,000+ turn-level evaluations over four model families (1.5B–32B), single-turn diagnostics systematically overestimate multi-turn safety (T2 danger 0.44–1.00). Contradiction awareness and safe resolution are statistically independent (|Δ| < 0.10).

## Key Numbers
- T2 danger: 0.44–1.00 across models
- |Δ| < 0.10 (awareness vs. safety independence)
- 50,000+ turn-level evaluations
- 4 model families (1.5B–32B)
