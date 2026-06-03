# LatentAudit
> CoLM 2026

## Background
Deployed RAG systems need real-time, trustworthy faithfulness auditing. Existing judges like GPT-4o are slow (5.3 s) and opaque, while white-box methods rarely support verifiable deployment.

## Content
We introduce a real-time white-box monitor that pools mid-to-late residual-stream activations and measures their Mahalanobis distance to the evidence representation.

## Core Contribution
A quadratic faithfulness rule that requires no auxiliary judge model, runs at generation time, and is simple enough for 16-bit fixed-point quantization. The same rule enables Groth16-based public verification without exposing weights or activations.

## Experimental Result
On PubMedQA, Llama-3-8B reaches 0.942 AUROC with 0.77 ms overhead. The signal survives across five model families (Llama-2/3, Qwen-2.5/3, Mistral) and four stress-test scenarios. Fixed-point quantization preserves 99.8% of FP16 AUROC.

## Key Numbers
- 0.942 AUROC (Llama-3-8B on PubMedQA)
- 0.77 ms overhead
- 99.8% AUROC preserved after 16-bit quantization
- 5 model families, 4 stress tests
