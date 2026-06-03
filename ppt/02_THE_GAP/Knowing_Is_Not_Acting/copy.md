# Knowing Is Not Acting
> NeurIPS 2026

## Background
Indirect prompt injection is often framed as a source-recognition failure, yet models sometimes appear to "know" the attack source and still act on it.

## Content
We reveal a representation–action dissociation: source-role information is linearly readable early in the residual stream, yet tool-use decisions remain causally insensitive until a late action-commitment band.

## Core Contribution
We establish a causal ladder (probe → activation patch → projection-out intervention) and discover channel-conditioned routing: tool output, Slack trace, and memory directions are nearly orthogonal.

## Experimental Result
Source role is fully readable at early layers (AUROC = 1.00). Projection steering reduces direct-attack ASR to 8.5% on Qwen-2.5-7B. Cross-channel interventions fail, proving source grounding is not unitary.

## Key Numbers
- AUROC = 1.00 @ early layers (L4–L8)
- L16→L18 inflection (two orders of magnitude)
- ASR reduced to 8.5% (matched intervention)
- Cross-channel cosine < 0.15 (near-orthogonal)
