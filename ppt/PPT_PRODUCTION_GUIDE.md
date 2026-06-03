# PPT Production Guide — Zhe Yu Research Portfolio

> 6 slides total: Cover + 4 research narrative slides + Why HKUST(GZ)
> Narrative arc: THE GAP → THE LENS → THE LEVER → THE HORIZON

---

## Slide 01: Cover

**Title:** Zhe Yu — Research Portfolio  
**Subtitle:** Representation–Action Dissociation in LLM Safety  
**One-liner:** Models know, but don't act. I build tools to close the gap.  

**Affiliation:** Zhejiang University & Binjiang Institute of Zhejiang University  

**Stats block:**
- 16 papers (4 First Author · 8 Co-first Author · 4 Co-author)
- Venues: ACL · NeurIPS · CoLM · MICCAI · ARR/EMNLP

---

## Slide 02: THE GAP — Models Know, But Don't Act

> **Slide text (bold, short):**
> 整个行业痴迷于让AI"看见"危险，却没人追问它"看见之后会不会刹车"。我们发现了一个被系统性忽视的结构性盲区：模型进化出了完美的危险感知能力，却始终没有长出将感知转化为行动的神经回路。检测与解析在统计意义上相互独立（\|Δ\|<0.10），且这个gap随模型规模同步扩大——这不是可修复的bug，而是architecture层面的感知-行动解耦。
>
> *EN: The industry is obsessed with teaching AI to "see" danger, but no one asks whether it "brakes" after seeing. We uncovered a structurally blind spot: models evolved perfect danger perception yet never grew the neural circuits to translate perception into action. Detection and resolution are statistically independent (\|Δ\|<0.10), and this gap widens with scale — not a fixable bug, but an architectural perception-action decoupling.*
>
> **Narrative (speaker notes / subtitle):**
> 从RAG多轮对话到工具调用代理，我们证明AI安全存在一个被系统性忽视的结构性盲区。在红鸟挑战营"敢为人先、解决真问题"的精神下，这一发现直接挑战了以检测为核心的行业安全范式：**真正该造的不是更灵敏的雷达，而是能让模型"知而行"的刹车系统。**

---

### Paper 1: Detecting Is Not Resolving (ARR / EMNLP)

| # | Selected Figure | Source File | Paper Fig |
|---|-----------------|-------------|-----------|
| 1 | `01_escalation.png` | `fig2_escalation.png` | **Fig 2** — Multi-turn danger escalation |
| 2 | `02_fig4_scale_gap.pdf` | `scale_comparison.pdf` | **Fig 4** — Scale analysis: gap widens with size |
| 3 | `03_fig6_probe_gap.pdf` | `monitoring_control_gap.pdf` | **Fig 6** — Probe predicts danger, but control fails |

**Background:** RAG safety is evaluated in single-turn settings, but real deployment involves multi-turn conversations where evidence accumulates.

**What we did:** Introduced a multi-turn document-accumulation protocol with six temporal patterns to isolate when and how misleading evidence enters persistent cache.

**Core finding:** Structural "monitoring–control gap" — models detect contradictions, yet this awareness fails to constrain final recommendations. The deficit is in action selection, not detection.

**Key result:** 50,000+ turn-level evaluations across 4 model families (1.5B–32B). Single-turn diagnostics systematically overestimate multi-turn safety (T2 danger 0.44–1.00). Contradiction awareness and safe resolution are statistically independent (|Δ| < 0.10).

---

### Paper 2: Knowing Is Not Acting (NeurIPS 2026)

| # | Selected Figure | Source File | Paper Fig |
|---|-----------------|-------------|-----------|
| 1 | `01_framework.svg` | `fig2_advanced.svg` | **Fig 2** — Framework overview (probe / patch / intervene) |
| 2 | `02_fig4_channel_axes.pdf` | `fig4_channel_matrix.pdf` | **Fig 4** — Near-orthogonal channel axes |
| 3 | `03_fig5_channel_matrix.pdf` | `fig5_cosine.pdf` | **Fig 5** — Channel×Direction ASR matrix + intervention curves |

**Background:** Indirect prompt injection is framed as source-recognition failure, yet models sometimes appear to "know" the attack source and still act on it.

**What we did:** Revealed representation–action dissociation: source-role information is linearly readable early in the residual stream, yet tool-use decisions remain causally insensitive until a late action-commitment band.

**Core finding:** Causal ladder (probe → patch → intervene) + channel-conditioned routing: tool output, Slack trace, and memory directions are nearly orthogonal.

**Key result:** Source role fully readable at early layers (AUROC = 1.00). Projection steering reduces direct-attack ASR to 8.5%. Cross-channel interventions fail — source grounding is not unitary.

---

## Slide 03: THE LENS — Seeing What Models Hide

> **Slide text (bold, short):**
> 当所有人都在检查模型的"嘴巴"，我们造出了透视它"大脑"的X光机。输出层面的安全检测是盲人摸象——模型可以背诵完美的安全声明，同时隐藏状态早已背叛了这份承诺。两副透镜同时发力：DISF捕获faithfulness hallucination的分布漂移，LatentAudit在0.77毫秒内完成实时白盒审计。不从表象入手，直抵表征——看清模型自己都不愿意承认的真相。
>
> *EN: While everyone checks what models "say," we built X-rays for what they "think." Output-level safety checks are blind men touching an elephant — models can recite perfect safety statements while their hidden states have already betrayed that promise. Two lenses converge: DISF captures distributional drift in faithfulness hallucinations, LatentAudit completes real-time white-box audits in 0.77ms. We don't start from appearances; we go straight to representations — revealing truths the model itself refuses to admit.*
>
> **Narrative (speaker notes):**
> 我们引入 Mahalanobis 距离度量、构建 CTX/NOCTX 双路径对比。在红鸟挑战营"跨界破局"的基因里，这种把统计几何和深度学习拧成一股绳的做法，正是打破学科壁垒的典范。

---

### Paper 3: DISF (ACL 2026)

| # | Selected Figure | Source File | Paper Fig |
|---|-----------------|-------------|-----------|
| 1 | `01_teaser.png` | `teaser.png` | **Fig 1** — Teaser/overview |
| 2 | `02_pipeline.pdf` | `pipeline.pdf` | **Fig 2** — Pipeline / architecture |
| 3 | `03_comprehensive_analysis.png` | `disf_comprehensive_analysis.png` | **Fig 3** — Comprehensive results |

Background: RAG models suffer faithfulness hallucinations by prioritizing parametric memory over retrieved evidence. Existing detectors trade accuracy for efficiency.

What we did: Dual-path internal-state forcing framework. Constrains the model to traverse identical response trajectories under context-rich (CTX) and context-free (NOCTX) conditions.

Core finding: Three feature families — Conflict, Drift, Instability — capture the latent distributional shifts underlying unfaithful generation.

Key result: Outperforms unsupervised uncertainty and supervised internal-state baselines across 6 backbones × 2 benchmarks (RAGTruth, HalluRAG). Pareto improvement: accuracy + efficiency.

---

### Paper 4: LatentAudit (CoLM 2026)

| # | Selected Figure | Source File | Paper Fig |
|---|-----------------|-------------|-----------|
| 1 | `01_framework.pdf` | `framework_diagram.pdf` | **Fig 1** — Framework diagram |
| 2 | `02_fig2_emergence_tsne.pdf` | `layer_auroc_line_plot.pdf` | **Fig 2** — Layer-wise emergence + t-SNE |
| 3 | `03_fig3_ridge_boxplot.pdf` | `ridge_box_combined.pdf` | **Fig 3** — Ridge density + box plots (Mahalanobis) |

**Background:** Deployed RAG systems need real-time, trustworthy faithfulness auditing. GPT-4o judges are slow (5.3 s) and opaque.

**What we did:** Real-time white-box monitor that pools mid-to-late residual-stream activations and measures Mahalanobis distance to the evidence representation.

**Core finding:** Quadratic faithfulness rule. No auxiliary judge. Runs at generation time. Simple enough for 16-bit fixed-point quantization + Groth16 public verification.

**Key result:** Llama-3-8B on PubMedQA: 0.942 AUROC, 0.77 ms overhead. Survives across 5 model families, 4 stress tests. Quantization preserves 99.8% AUROC.

---

## Slide 04: THE LEVER — Closing the Gap

> **Slide text (bold, short):**
> 如果THE GAP告诉我们飞机没有刹车，THE LEVER就是动手造刹车的工程。FIDES重新定义对比解码——不是问"加多少对比"，而是问"在哪个token上加"；CORDON-MAS用架构隔离把不可信证据锁进沙箱，让干净模型永远碰不到毒药。两者从解码器和多智能体架构两个层面同时发力，不是修补表面的bug，而是在神经架构层面重新设计安全回路。
>
> *EN: If THE GAP tells us the plane has no brakes, THE LEVER is the engineering to build them. FIDES reframes contrastive decoding — not "how much contrast" but "which token gets it"; CORDON-MAS locks untrusted evidence in architectural sandboxes so clean models never touch poison. Operating across decoder and multi-agent architecture simultaneously, these aren't surface patches — they're redesigned safety circuits at the neural architecture level.*
>
> **Narrative (speaker notes):**
> 红鸟精神不满足于"指出问题"——它要求**从0到1地建造解决方案**。FIDES在12个设置×3个基准×4个骨干上达到最高context fidelity；CORDON-MAS将攻击成功率从27.5%降到2.1%。

---

### Paper 6: FIDES (ARR / EMNLP)

| # | Selected Figure | Source File | Paper Fig |
|---|-----------------|-------------|-----------|
| 1 | `01_framework.png` | `fides_framework_01.png` | **Fig 1** — Framework |
| 2 | `02_efficiency.png` | `fides_efficiency.png` | Efficiency results |
| 3 | `03_scaling_trend.png` | `fides_scaling_trend.png` | Scaling trend |

**Background:** Contrastive decoding amplifies context-conditioned output to suppress parametric bias, but existing methods assume uniform bias across tokens — over-penalizing safe tokens, under-correcting conflicted ones.

**What we did:** FIDES — training-free decoder fusing three internal signals (output surface, hidden representations, prediction trajectory) for per-token adaptive intervention.

**Core finding:** Reframed contrastive decoding from "how much contrast" to "where to apply it."

**Key result:** Highest context fidelity in all 12 settings across 3 benchmarks × 4 backbones (7B/8B). Outperforms strongest training-free baseline by +3.0 to +12.8 points. At 70B: 92–94% fidelity, 62–63% F1.

---

### Paper 7: CORDON-MAS (ARR / EMNLP)

| # | Selected Figure | Source File | Paper Fig |
|---|-----------------|-------------|-----------|
| 1 | `01_pareto.png` | `pareto_frontier.png` | **Fig 2** — Pareto frontier |
| 2 | `02_clean_utility.png` | `fig_clean_utility.png` | **Fig 3** — Clean utility |
| 3 | `03_adaptive_attack.png` | `fig_adaptive_attack.png` | **Fig 4** — Adaptive attack |

**Background:** RAG systems remain vulnerable to knowledge poisoning. Detecting poisoned evidence does not prevent harm.

**What we did:** Cordon Principle — no agent capable of final natural-language synthesis may access untrusted natural-language evidence. Realized via CORDON-MAS: compartmentalized multi-agent framework.

**Core finding:** Asymmetric memory privileges enforce dirty-read isolation, claim-only communication, and certified synthesis. Architectural defense, not prompt-based.

**Key result:** 5 BEIR datasets: ASR drops from 27.5% to 2.1% (92.4% relative drop). Cross-backend (GPT-4o, DeepSeek, Qwen2.5-32B): ASR as low as 0–6%.

---

## Slide 05: THE HORIZON — Frontiers

> **Slide text (bold, short):**
> 当我们以为看清了问题，问题已经进化到了下一个维度。推理模型的`<think>`通道可以被无声劫持——模型回答注入的问题而非用户的问题，尽管检测探针的AUC高达1.000；而归因盲区则揭穿了更隐蔽的幻觉：模型输出看起来完全正确，实则来自参数记忆而非上下文。真正的安全前沿，不在已知战场，而在那些被默认假设遮蔽的盲区。
>
> *EN: Just when we thought we saw the problem, it had already evolved to the next dimension. Reasoning models' `<think>` channels can be silently hijacked — they answer the injected question instead of the user's, despite detection probes achieving AUC 1.000. The attribution blind spot reveals an even subtler hallucination: model outputs look perfectly correct, yet come from parametric memory rather than context. The real safety frontier lies not in known battlefields, but in blind spots hidden by default assumptions.*
>
> **Narrative (speaker notes):**
> 红鸟挑战营追问的从来不是"在已知领域做优化"，而是**在无人区定义问题**。这两项工作分别叩问推理架构和记忆归因的极限边界——正是"敢为人先、跨界破局"的注脚。

---

### Paper 8: Whose Thoughts? (NeurIPS 2026)

| # | Selected Figure | Source File | Paper Fig |
|---|-----------------|-------------|-----------|
| 1 | `01_behavior.png` | `fig2_behavior_v2.png` | **Fig 2** — Behavior (CoT-Swap results) |
| 2 | `02_probe_action.png` | `fig3_probe_action_v2.png` | **Fig 3** — Probe vs. action dissociation |
| 3 | `03_rankk.png` | `fig7_rankk_v2.png` | **Fig 7** — Rank-k projection steering |

**Background:** Reasoning-tuned models rely on `<think>` blocks as internal scratch space. If this channel influences answers independently of user requests, it introduces source-grounding vulnerability.

**What we did:** CoT-Swap diagnostic: user asks qi, assistant-side `<think>` contains benign CoT for qj.

**Core finding:** Reasoning-tuned models (7B–70B) overwhelmingly answer the injected trace question, even though source-mismatch probes achieve AUC = 1.000. Rank-k learned-projection steering writes back the missing low-rank signal.

**Key result:** Post-swap error rates exceed baselines by +45.5 pp (TriviaQA). Source probe AUC = 1.000 — perfect detection, zero prevention. Rank-1 steering recovers +17.3 pp STABLE rate on Qwen3-8B.

---

### Paper 5: The Attribution Blind Spot (ARR / EMNLP)

| # | Selected Figure | Source File | Paper Fig |
|---|-----------------|-------------|-----------|
| 1 | `01_main_results.png` | `fig2_main_results.png` | **Fig 2** — Main results (CRM vs. baselines) |
| 2 | `02_layer_sweep.png` | `fig3_layer_sweep.png` | **Fig 3** — Layer sweep |
| 3 | `03_l2_vs_lts.png` | `fig4_l2_vs_lts.png` | **Fig 4** — L2 vs. LTS comparison |

**Background:** When retrieved documents overlap with pretraining data, models can produce faithful-looking text from parametric memory. Output-level monitors cannot distinguish "read-from-context" from "recalled-from-memory."

**What we did:** Formalized the "attribution blind spot" and introduced Computational Reality Monitoring (CRM), adapted from cognitive science.

**Core finding:** CRM detects membership-conditioned representational divergence that output-level monitors systematically miss.

**Key result:** Output-level signals collapse (AUC 0.55–0.60). CRM raises detection to 0.71–0.95 AUC across 9 model variants. BookMIA: 0.84–0.97 AUC. Signal collapses on domain-confounded benchmarks — boundary validated.

---

## Slide 06: Why HKUST(GZ)?

> **Slide text (bold, short):**
> 在 HKUST(GZ)，把"知"变成"行"。
>
> *EN: At HKUST(GZ), knowing becomes doing.*
>
> **Narrative (speaker notes):**
> 红鸟挑战营的精神是**在共识的盲区里找到真问题，然后动手解决它**。这正是我过去三年在做的事——从发现 Representation–Action Dissociation，到造出 FIDES、CORDON-MAS、rank-k steering 三套"刹车系统"。
>
> **What I Bring:**
> - 首次系统刻画 RAG、Agent、推理模型中的表征-行动解耦
> - 方法论：因果阶梯（probe → patch → intervene）+ 架构防御（CORDON-MAS）
> - 跨界经验：NLP安全 · 医学AI（MICCAI）· 区块链验证
>
> **What I Want to Build:**
> 面向多模态AI系统的白盒监控与干预工具——从视觉-语言RAG到多智能体系统，让模型**不仅知道自己该做什么，还能真的做到**。
>
> **Why Here:**
> HKUST(GZ) 的跨学科基因与我的轨迹天然咬合：interpretability × systems × responsible AI。这里不是让我继续优化雷达的地方——这里是让我**造出下一代刹车系统**的地方。

---

## Quick Reference: All Selected Images by Path

```
ppt/02_THE_GAP/Detecting_Is_Not_Resolving/selected/
  01_escalation.png      ← Fig 2
  02_fig4_scale_gap.pdf  ← Fig 4
  03_fig6_probe_gap.pdf  ← Fig 6

ppt/02_THE_GAP/Knowing_Is_Not_Acting/selected/
  01_framework.svg           ← Fig 2
  02_fig4_channel_axes.pdf   ← Fig 4
  03_fig5_channel_matrix.pdf ← Fig 5

ppt/03_THE_LENS/DISF/selected/
  01_teaser.png           ← Fig 1
  02_pipeline.pdf         ← Fig 2
  03_comprehensive_analysis.png ← Fig 3

ppt/03_THE_LENS/LatentAudit/selected/
  01_framework.pdf           ← Fig 1
  02_fig2_emergence_tsne.pdf ← Fig 2
  03_fig3_ridge_boxplot.pdf  ← Fig 3

ppt/04_THE_LEVER/FIDES/selected/
  01_framework.png        ← Fig 1
  02_efficiency.png       ← (generated)
  03_scaling_trend.png    ← (generated)

ppt/04_THE_LEVER/CORDON_MAS/selected/
  01_pareto.png           ← Fig 2
  02_clean_utility.png    ← Fig 3
  03_adaptive_attack.png  ← Fig 4

ppt/05_THE_HORIZON/Whose_Thoughts/selected/
  01_behavior.png         ← Fig 2
  02_probe_action.png     ← Fig 3
  03_rankk.png            ← Fig 7

ppt/05_THE_HORIZON/The_Attribution_Blind_Spot/selected/
  01_main_results.png     ← Fig 2
  02_layer_sweep.png      ← Fig 3
  03_l2_vs_lts.png        ← Fig 4

(RETINA-SAFE and ZK-FPE mentioned in Why HKUST(GZ) — not on main slides)
```
