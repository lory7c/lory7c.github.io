# CORDON-MAS
> ARR / EMNLP

## Background
RAG systems remain vulnerable to knowledge poisoning. Existing defenses assume that detecting poisoned evidence prevents harm, but models can detect contradictions and still act on poisoned claims.

## Content
We introduce the Cordon Principle—no agent capable of final natural-language synthesis may access untrusted natural-language evidence—and realize it through CORDON-MAS, a compartmentalized multi-agent framework.

## Core Contribution
Asymmetric memory privileges enforce dirty-read isolation, claim-only communication, and certified synthesis. The defense is architectural, not prompt-based.

## Experimental Result
Across five BEIR datasets, CORDON-MAS reduces attack success rate from 27.5% to 2.1% (a 92.4% relative drop). Cross-backend evaluation (GPT-4o, DeepSeek, Qwen2.5-32B) shows ASR as low as 0–6%, proving the defense is architectural, not model-specific.

## Key Numbers
- ASR: 27.5% → 2.1% (92.4% relative drop)
- 5 BEIR datasets
- Cross-backend: GPT-4o, DeepSeek, Qwen2.5-32B
- ASR as low as 0–6%
