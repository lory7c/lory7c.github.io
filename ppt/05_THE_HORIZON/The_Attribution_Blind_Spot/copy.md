# The Attribution Blind Spot
> ARR / EMNLP

## Background
When retrieved documents overlap with pretraining data, models can produce faithful-looking text entirely from parametric memory. Output-level monitoring cannot distinguish "read-from-context" from "recalled-from-memory."

## Content
We formalize the "attribution blind spot" and introduce Computational Reality Monitoring (CRM), adapted from cognitive science's reality-monitoring framework.

## Core Contribution
CRM compares internal representations with and without context to detect membership-conditioned representational divergence that output-level monitors systematically miss.

## Experimental Result
Output-level signals collapse (likelihood baseline AUC 0.55–0.60), while CRM raises detection to 0.71–0.95 AUC across nine model variants. On BookMIA, AUC reaches 0.84–0.97. The signal collapses on domain-confounded benchmarks, validating boundary conditions.

## Key Numbers
- CRM: 0.71–0.95 AUC (vs. 0.55–0.60 baseline)
- BookMIA: 0.84–0.97 AUC
- 9 model variants tested
- Signal collapses on domain-confounded benchmarks (boundary validated)
