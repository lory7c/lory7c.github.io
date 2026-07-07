# Portfolio Pitch Deck — 4 Research Slides

> For HKUST(GZ) Red Bird Challenge Camp. Minimal text, image-driven.

---

## Slide 1 — THE GAP

**Models know, but don't act.**

- **RAG:** Models detect contradictions, yet keep recommending dangerously.
- **Agents:** They recognize attacks early, yet execute them anyway.
- **Insight:** *Safety is a routing problem, not just recognition.*

### Visual Suggestion
Split-screen image:
- **Left:** A glowing brain / neural network (labeled "Internal State ✓")
- **Right:** A disconnected output wire or broken action arrow (labeled "External Action ✗")
- **Center:** A gap / crack between them

### Figures to Extract
- From *Detecting Is Not Resolving*: the multi-turn danger-rate chart (T2 danger 0.44–1.00)
- From *Knowing Is Not Acting*: the early-layer vs. late-layer causality diagram

---

## Slide 2 — THE LENS

**We look inside to see why.**

- **DISF** *(ACL 2026)*: Dual-path internal-state forcing constructs contrastive negative signals.
- **LatentAudit** *(CoLM 2026)*: Residual-stream geometry reads faithfulness in 0.77 ms.
- **Attribution Blind Spot** *(EMNLP)*: Internal-trajectory divergence exposes parametric memory.
- **Insight:** *From guessing outputs → inspecting internals.*

### Visual Suggestion
Three vertical panels showing an X-ray / cross-section view of a model:
- **Panel 1:** Two parallel paths (CTX vs. NOCTX) — DISF
- **Panel 2:** A magnifying glass over residual-stream activations — LatentAudit
- **Panel 3:** Diverging trajectories inside the model — Attribution Blind Spot

### Figures to Extract
- From *DISF*: Figure 1 (dual-path architecture with CTX / NOCTX)
- From *LatentAudit*: Figure 1 (pipeline overview: Monitor → ZK Proof)
- From *Attribution Blind Spot*: The with-context vs. without-context trajectory diagram

---

## Slide 3 — THE LEVER

**We intervene to fix it.**

- **FIDES** *(EMNLP)*: Token-selective decoding unlocks suppressed capability. 92–94% fidelity.
- **CORDON-MAS** *(EMNLP)*: Architectural isolation blocks poison. ASR ↓ 92.4%.
- **Whose Thoughts?** *(NeurIPS)*: Projection steering recovers lost routing. +17.3 pp.
- **Insight:** *From passive detection → active control.*

### Visual Suggestion
A lever / gear mechanism transforming input to safe output:
- **Left:** Unsafe input entering
- **Center:** Three intervention gears (Token Selective / Isolation / Projection)
- **Right:** Safe output exiting

### Figures to Extract
- From *FIDES*: The three-layer signal fusion diagram (Output / Hidden / Trajectory)
- From *CORDON-MAS*: The multi-agent architecture (Extractor → Auditor → Gate → Synthesizer)
- From *Whose Thoughts?*: The rank-k projection steering diagram

---

## Slide 4 — THE HORIZON

**We deploy where it matters.**

- **RETINA-SAFE** *(MICCAI)*: 12,522-sample benchmark for diabetic retinopathy risk triage.
- **ZK-FPE**: Blockchain-verifiable model ownership without exposing weights.
- **Future**: Multimodal mechanistic interpretability for accountable AI.
- **Insight:** *Safe AI must be inspectable and accountable.*

### Visual Suggestion
Three horizon panels fading from lab to world:
- **Left:** A medical retina scan with heatmap overlay — RETINA-SAFE
- **Center:** A blockchain / shield icon with zero-knowledge circuit — ZK-FPE
- **Right:** A multimodal AI system (vision + language) with internal pathways lit up — Future

### Figures to Extract
- From *RETINA-SAFE*: The E-Align / E-Conflict / E-Gap taxonomy diagram
- From *ZK-FPE*: The fingerprint verification flow diagram
- Concept art: Multimodal model internals (can be a simple diagram)

---

## Navigation Bar (Optional)

Place at the top or bottom of every slide for continuity:

```
THE GAP  →  THE LENS  →  THE LEVER  →  THE HORIZON
    ■           □            □             □      (Slide 1)
    ■           ■            □             □      (Slide 2)
    ■           ■            ■             □      (Slide 3)
    ■           ■            ■             ■      (Slide 4)
```

## Color & Typography Notes

| Element | Suggestion |
|---|---|
| **Titles** | All caps, bold, large (e.g., `THE GAP`) |
| **Subtitles** | Sentence case, lighter weight (e.g., `Models know, but don't act.`) |
| **Bullets** | One line each, no wrapping |
| **Insight line** | Italic, accent color (e.g., red or gold) |
| **Background** | Dark navy or clean white; let figures provide color |
