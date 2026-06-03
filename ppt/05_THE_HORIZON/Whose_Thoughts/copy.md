# Whose Thoughts?
> NeurIPS 2026

## Background
Reasoning-tuned models rely on an explicit reasoning channel (`<think>` block) intended as internal scratch space. If this channel can influence the answer independently of the user's request, it introduces a source-grounding vulnerability.

## Content
We propose the CoT-Swap diagnostic protocol: the user asks question qi, while the assistant-side `<think>` block contains a benign CoT for a different question qj.

## Core Contribution
We prove that reasoning-tuned models (7B–70B) overwhelmingly answer the injected trace question, even though source-mismatch probes achieve AUC = 1.000. Rank-k learned-projection steering writes back the missing low-rank signal.

## Experimental Result
Post-swap error rates exceed instruct-model baselines by up to +45.5 pp (TriviaQA). Source probes achieve AUC = 1.000, yet fail to prevent wrong answers. Rank-1 projection steering recovers +17.3 pp in STABLE rate on Qwen3-8B.

## Key Numbers
- +45.5 pp error rate increase (TriviaQA)
- Source probe AUC = 1.000 (perfect detection, zero prevention)
- Rank-1 steering: +17.3 pp STABLE recovery (Qwen3-8B)
- 7B–70B scale
