# RETINA-SAFE
> MICCAI 2026

## Background
Hallucinations in medical LLMs are safety-critical, especially when evidence is insufficient or conflicting. Existing evaluation focuses on answer correctness, not on risk triage conditioned by evidence relation.

## Content
We build RETINA-SAFE, a 12,522-sample evidence-grounded benchmark for diabetic retinopathy, organized into three tasks: E-Align (consistent), E-Conflict (conflicting), and E-Gap (insufficient). We propose ECRT, a two-stage white-box detection framework.

## Core Contribution
Stage 1 performs Safe/Unsafe risk triage. Stage 2 refines unsafe cases into contradiction-driven versus evidence-gap subtypes, enabling explicit subtype attribution.

## Experimental Result
ECRT Stage-1 balanced accuracy exceeds external-uncertainty and self-consistency baselines by +0.15 to +0.19, and exceeds the strongest adapted supervised baseline by +0.02 to +0.07 across multiple backbones.

## Key Numbers
- 12,522 samples
- 3 tasks: E-Align, E-Conflict, E-Gap
- +0.15 to +0.19 over uncertainty/self-consistency baselines
