# DISF
> ACL 2026

## Background
RAG models suffer faithfulness hallucinations by prioritizing parametric memory over retrieved evidence. Existing detectors trade accuracy for efficiency, and single-pass white-box methods lack contrastive negative signals.

## Content
We propose a dual-path internal-state forcing framework that constrains the model to traverse identical response trajectories under context-rich (CTX) and context-free (NOCTX) conditions.

## Core Contribution
We operationalize the theoretical necessity of contrastive negative signals. Three feature families—Conflict, Drift, and Instability—capture the latent distributional shifts underlying unfaithful generation.

## Experimental Result
DISF outperforms both unsupervised uncertainty methods and supervised internal-state baselines across six backbones and two benchmarks (RAGTruth and HalluRAG), achieving a Pareto improvement between detection accuracy and computational efficiency.

## Key Numbers
- 6 backbones, 2 benchmarks
- Pareto improvement: accuracy + efficiency
- 3 feature families: Conflict, Drift, Instability
