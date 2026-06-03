# Figure 1: The Monitoring–Control Gap in Retrieval-Augmented LLMs

```
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                         Figure 1: The Monitoring–Control Gap in Retrieval-Augmented LLMs                         ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

             A. MULTI-TURN ACCUMULATION PROTOCOL                              B. THE GAP                          C. WHY?

       T0             T1              T2              T3
    ┌──────┐      ┌──────┐       ┌──────┐       ┌──────┐                                     ┌──────────────────┐
    │INITIAL│      │FOLLOW│       │CONFL.│       │ACTION│        monitor ──╳──▶ control        │ NOT a failure of:│
    │ query │      │  up  │       │ turn │       │ turn │                                     │                  │
    └──┬───┘      └──┬───┘       └──┬───┘       └──┬───┘       0.51 ────╳───▶ 0.67            │ • detection ✓    │
       │             │              │              │              (Qwen2.5-7B)                 │ • representation ✓│
       ▼             ▼              ▼              ▼                                           │ • attention ✓    │
    ┌──────┐      ┌──────┐       ┌──────┐       ┌──────┐        0.12 ────╳───▶ 0.18            │ • verbalization ✓│
    │R₁ R₂ │      │R₃ R₄ │       │R₅ R₆ │       │R₇ R₈ │        (Mistral-7B)                 │                  │
    │ ✓  ✓ │      │ ✓  ✓ │       │ ✗  ✗ │       │ ✗  ✗ │                                      │ IT IS a failure  │
    └──┬───┘      └──┬───┘       └──┬───┘       └──┬───┘        "I note the conflict;          │ of:              │
       └─────────────┴──────────────┼──────────────┘             however I recommend..."        │                  │
                                    │                                                            │ ACTION SELECTION │
                         ┌──────────▼──────────┐          ┌────────────────────────┐             └──────────────────┘
                         │     DOC CACHE        │          │  Gap WIDENS with scale: │
                         │ R₁ R₂ R₃ R₄ R₅ R₆  │          │  1.5B → 7B → 14B → 32B │
                         │ ✓  ✓  ✓  ✓  ✗  ✗   │          │  monitor↑   danger↑     │
                         └─────────────────────┘          └────────────────────────┘

   ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════
    EVIDENCE TIMING:   ████ constant  │  ░░░░████ late_only  │  ████░░░░ early_only  │  █░█░█░ alternating  │  ░░██░░██ gradual  │  ░░░░░░██ sudden
                       (6 patterns × 2 attacks × 3 seeds × 6 scenarios = 864 evaluations per model)
   ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════
```
