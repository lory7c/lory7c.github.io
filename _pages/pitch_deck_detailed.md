# Portfolio Pitch Deck — Detailed Paper Descriptions

> Each paper covered in: Background → Content → Core Contribution → Experimental Result

---

## Slide 1 — THE GAP

### Detecting Is Not Resolving (ARR / EMNLP)

- **Background:** RAG safety is evaluated in single-turn settings, but real deployment involves multi-turn conversations where evidence accumulates.
- **Content:** We introduce a multi-turn document-accumulation protocol with six temporal patterns to isolate when and how misleading evidence enters persistent cache.
- **Core Contribution:** We prove a structural "monitoring–control gap": models detect contradictions, yet this awareness fails to constrain final recommendations. The deficit lies in action selection, not detection.
- **Experimental Result:** Across 50,000+ turn-level evaluations over four model families (1.5B–32B), single-turn diagnostics systematically overestimate multi-turn safety (T2 danger 0.44–1.00). Contradiction awareness and safe resolution are statistically independent (|Δ| < 0.10).

### Knowing Is Not Acting (NeurIPS 2026)

- **Background:** Indirect prompt injection is often framed as a source-recognition failure, yet models sometimes appear to "know" the attack source and still act on it.
- **Content:** We reveal a representation–action dissociation: source-role information is linearly readable early in the residual stream, yet tool-use decisions remain causally insensitive until a late action-commitment band.
- **Core Contribution:** We establish a causal ladder (probe → activation patch → projection-out intervention) and discover channel-conditioned routing: tool output, Slack trace, and memory directions are nearly orthogonal.
- **Experimental Result:** Source role is fully readable at early layers (AUROC = 1.00). Projection steering reduces direct-attack ASR to 8.5% on Qwen-2.5-7B. Cross-channel interventions fail, proving source grounding is not unitary.

---

## Slide 2 — THE LENS

### DISF (ACL 2026)

- **Background:** RAG models suffer faithfulness hallucinations by prioritizing parametric memory over retrieved evidence. Existing detectors trade accuracy for efficiency, and single-pass white-box methods lack contrastive negative signals.
- **Content:** We propose a dual-path internal-state forcing framework that constrains the model to traverse identical response trajectories under context-rich (CTX) and context-free (NOCTX) conditions.
- **Core Contribution:** We operationalize the theoretical necessity of contrastive negative signals. Three feature families—Conflict, Drift, and Instability—capture the latent distributional shifts underlying unfaithful generation.
- **Experimental Result:** DISF outperforms both unsupervised uncertainty methods and supervised internal-state baselines across six backbones and two benchmarks (RAGTruth and HalluRAG), achieving a Pareto improvement between detection accuracy and computational efficiency.

### LatentAudit (CoLM 2026)

- **Background:** Deployed RAG systems need real-time, trustworthy faithfulness auditing. Existing judges like GPT-4o are slow (5.3 s) and opaque, while white-box methods rarely support verifiable deployment.
- **Content:** We introduce a real-time white-box monitor that pools mid-to-late residual-stream activations and measures their Mahalanobis distance to the evidence representation.
- **Core Contribution:** A quadratic faithfulness rule that requires no auxiliary judge model, runs at generation time, and is simple enough for 16-bit fixed-point quantization. The same rule enables Groth16-based public verification without exposing weights or activations.
- **Experimental Result:** On PubMedQA, Llama-3-8B reaches 0.942 AUROC with 0.77 ms overhead. The signal survives across five model families (Llama-2/3, Qwen-2.5/3, Mistral) and four stress-test scenarios. Fixed-point quantization preserves 99.8% of FP16 AUROC.

### The Attribution Blind Spot (ARR / EMNLP)

- **Background:** When retrieved documents overlap with pretraining data, models can produce faithful-looking text entirely from parametric memory. Output-level monitoring cannot distinguish "read-from-context" from "recalled-from-memory."
- **Content:** We formalize the "attribution blind spot" and introduce Computational Reality Monitoring (CRM), adapted from cognitive science's reality-monitoring framework.
- **Core Contribution:** CRM compares internal representations with and without context to detect membership-conditioned representational divergence that output-level monitors systematically miss.
- **Experimental Result:** Output-level signals collapse (likelihood baseline AUC 0.55–0.60), while CRM raises detection to 0.71–0.95 AUC across nine model variants. On BookMIA, AUC reaches 0.84–0.97. The signal collapses on domain-confounded benchmarks, validating boundary conditions.

---

## Slide 3 — THE LEVER

### FIDES (ARR / EMNLP)

- **Background:** When retrieved evidence contradicts parametric memory, contrastive decoding amplifies context-conditioned output to suppress parametric bias. Existing methods assume this bias is uniform across tokens, over-penalizing safe tokens while under-correcting conflicted ones.
- **Content:** We reveal token-level conflict concentration and propose FIDES, a training-free decoder that fuses three complementary internal signals—output surface, hidden representations, and prediction trajectory—to govern intervention strength at each decoding step.
- **Core Contribution:** We reframe contrastive decoding from "how much contrast" to "where to apply it." The three-layer fusion mechanism enables per-token adaptive intervention.
- **Experimental Result:** FIDES achieves the highest context fidelity in all 12 settings across three benchmarks and four 7B/8B backbones, outperforming the strongest training-free baseline by +3.0 to +12.8 points. At 70B scale, fidelity reaches 92–94% and F1 reaches 62–63%.

### CORDON-MAS (ARR / EMNLP)

- **Background:** RAG systems remain vulnerable to knowledge poisoning. Existing defenses assume that detecting poisoned evidence prevents harm, but models can detect contradictions and still act on poisoned claims.
- **Content:** We introduce the Cordon Principle—no agent capable of final natural-language synthesis may access untrusted natural-language evidence—and realize it through CORDON-MAS, a compartmentalized multi-agent framework.
- **Core Contribution:** Asymmetric memory privileges enforce dirty-read isolation, claim-only communication, and certified synthesis. The defense is architectural, not prompt-based.
- **Experimental Result:** Across five BEIR datasets, CORDON-MAS reduces attack success rate from 27.5% to 2.1% (a 92.4% relative drop). Cross-backend evaluation (GPT-4o, DeepSeek, Qwen2.5-32B) shows ASR as low as 0–6%, proving the defense is architectural, not model-specific.

### Whose Thoughts? (NeurIPS 2026)

- **Background:** Reasoning-tuned models rely on an explicit reasoning channel (`<think>` block) intended as internal scratch space. If this channel can influence the answer independently of the user's request, it introduces a source-grounding vulnerability.
- **Content:** We propose the CoT-Swap diagnostic protocol: the user asks question qi, while the assistant-side `<think>` block contains a benign CoT for a different question qj.
- **Core Contribution:** We prove that reasoning-tuned models (7B–70B) overwhelmingly answer the injected trace question, even though source-mismatch probes achieve AUC = 1.000. Rank-k learned-projection steering writes back the missing low-rank signal.
- **Experimental Result:** Post-swap error rates exceed instruct-model baselines by up to +45.5 pp (TriviaQA). Source probes achieve AUC = 1.000, yet fail to prevent wrong answers. Rank-1 projection steering recovers +17.3 pp in STABLE rate on Qwen3-8B.

---

## Slide 4 — THE HORIZON

### RETINA-SAFE (MICCAI 2026)

- **Background:** Hallucinations in medical LLMs are safety-critical, especially when evidence is insufficient or conflicting. Existing evaluation focuses on answer correctness, not on risk triage conditioned by evidence relation.
- **Content:** We build RETINA-SAFE, a 12,522-sample evidence-grounded benchmark for diabetic retinopathy, organized into three tasks: E-Align (consistent), E-Conflict (conflicting), and E-Gap (insufficient). We propose ECRT, a two-stage white-box detection framework.
- **Core Contribution:** Stage 1 performs Safe/Unsafe risk triage. Stage 2 refines unsafe cases into contradiction-driven versus evidence-gap subtypes, enabling explicit subtype attribution.
- **Experimental Result:** ECRT Stage-1 balanced accuracy exceeds external-uncertainty and self-consistency baselines by +0.15 to +0.19, and exceeds the strongest adapted supervised baseline by +0.02 to +0.07 across multiple backbones.

### ZK-FPE (ACM TURC 2026)

- **Background:** Model ownership verification requires disclosing sensitive weights or architecture details, creating a privacy-versus-accountability dilemma.
- **Content:** We combine blockchain and zero-knowledge proofs to build verifiable model ownership attribution. Fingerprint vectors enable scalable transfer via vector addition.
- **Core Contribution:** ZK-FPE achieves privacy-preserving ownership verification: the verifier can confirm fingerprint presence without accessing model internals. ZK-VOT extends this to on-chain/off-chain mutual trust.
- **Experimental Result:** The framework supports scalable, efficient fingerprint transfer and establishes verifiable trust between on-chain contracts and off-chain computation.

### Future Direction: Multimodal Mechanistic Interpretability

- **Background:** Current mechanistic interpretability and white-box monitoring are predominantly text-based. Multimodal systems introduce new failure modes where visual and textual signals may conflict or be misrouted.
- **Content:** Extend the "knowing vs. doing" framework to vision-language models: probe when and why multimodal representations fail to route into downstream decisions.
- **Core Contribution:** Build white-box monitoring and intervention tools for multimodal RAG and agentic systems, ensuring that visual evidence governs generation as reliably as textual evidence.
- **Vision:** Safe AI for high-stakes deployment must be inspectable, intervenable, and accountable across all modalities.
