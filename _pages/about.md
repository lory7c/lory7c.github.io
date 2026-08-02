---
permalink: /
title: ""
excerpt: ""
author_profile: true
published: false
redirect_from:
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

Hi, I am Zhe Yu (俞哲) from Hangzhou, China. I am a Research Assistant at the **Hong Kong University of Science and Technology (Guangzhou)**, advised by **[Prof. Chengwei Qin](https://qcwthu.github.io/)**. I am also a Research Intern at the **[Binjiang Institute of Zhejiang University](https://ifrc-zju.github.io/)** ([IFRC Lab](https://ifrc-zju.github.io/)), where I work on trustworthy language models with **[Dr. Meng Han](https://scholar.google.com/citations?user=TnCrl1cAAAAJ&hl=en)** and Dr. Wenpeng Xing. I am currently pursuing my B.Eng. in Artificial Intelligence at the Communication University of Zhejiang (CUZ). During my undergraduate studies, I also spent time as a Visiting Student at **Westlake University** (supervised by Dr. Ziyang Zhang) and the **University of Malaya**.

> 📢 **Seeking Opportunities:** I am looking for **Fall 2027 PhD** opportunities. Please feel free to drop me an [email](mailto:zyu@zju-if.com) if you are interested!

<p class="cv-links">
  <span aria-hidden="true">📄</span>
  <strong><a href="/files/CV_Zhe_Yu_EN.pdf?v=20260803d">Download my full CV (English)</a> <span class="cv-links__separator">|</span> <a href="/files/CV_Zhe_Yu_CN.pdf?v=20260803d">获取完整中文简历</a></strong>
</p>

<section class="research-hero" aria-labelledby="research-vision-title">
  <p class="research-hero__eyebrow">Research vision</p>
  <h1 id="research-vision-title">From latent knowledge to reliable action, memory, and verifiable trust.</h1>
  <p>My research focuses on trustworthy language models and agentic AI systems. I study how models internally represent knowledge, evidence provenance, conflict, and risk; why these signals often fail to guide generation, tool use, and long-term memory; and how white-box monitoring and system-level safeguards can improve their reliability. I also develop verifiable mechanisms for model ownership and deployment, connecting internal reliability with external accountability.</p>
</section>

<span class='anchor' id='research-agenda'></span>

# 🔬 Research Agenda

Trustworthy agents must not only represent provenance, conflict, and risk internally. These signals should reliably inform what agents say, do, remember, reuse, and learn, while the resulting models and artifacts remain externally verifiable.

<div class="research-path" aria-label="Research progression">
  <article class="research-stage">
    <span class="research-stage__number">01</span>
    <h2>Internal representation</h2>
    <p>Understand how models encode knowledge, retrieved evidence, source provenance, conflict, and hallucination risk through white-box monitoring and hidden-state analysis.</p>
  </article>
  <article class="research-stage">
    <span class="research-stage__number">02</span>
    <h2>Action and memory</h2>
    <p>Study why decodable safety signals fail to guide generation, tool use, and memory updates, and turn monitoring into reliable system safeguards.</p>
  </article>
  <article class="research-stage">
    <span class="research-stage__number">03</span>
    <h2>Verifiable trust</h2>
    <p>Build accountable deployment mechanisms for models and artifacts through information-flow control, fingerprinting, blockchain, and privacy-preserving verification.</p>
  </article>
</div>

<div class="research-focus">
  <h2>Current research themes</h2>
  <ul>
    <li><strong>RLVR reward hacking:</strong> when verifiable rewards are gamed and proxy success diverges from intended success.</li>
    <li><strong>Multi-agent memory consistency:</strong> write validity, conflict, contamination, persistence, propagation, and repair across long-lived memories.</li>
    <li><strong>Multi-agent poisoning defense and credit:</strong> separating the source, amplifier, executor, and most effective remediation target.</li>
    <li><strong>Runtime monitoring of agent skills:</strong> using internal representations to identify risky skills before unsafe tool actions.</li>
  </ul>
</div>

My longer-term goal is to understand **environment–verifier–memory co-evolution in lifelong agents**: how tasks, evaluation, memory, and oversight should adapt together as agents act, learn, and update over time.

<span class='anchor' id='research-papers'></span>

# 📚 Research Papers

<div class="paper-grid">

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="/files/disfcr.pdf" aria-label="Open the DISF paper PDF"><img src="/images/disf-architecture.png" alt="DISF dual-path architecture for hallucination detection" width="1224" height="600" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title"><a href="/files/disfcr.pdf">DISF: Detecting Hallucinations in Retrieval-Augmented Generation via Dual-path Internal State Forcing Framework</a></div>
<div class="paper-authors"><strong>Zhe Yu*</strong>, Wenpeng Xing*, Wenjie Luo, Weize Xu, Lingtong Huang, Yourong Chen, Changting Lin, Meng Han</div>
<div class="paper-desc">A dual-path internal-state forcing framework that detects hallucinations in RAG by leveraging white-box activation signals.</div>
<div class="paper-meta">
<span class="paper-badge accepted">Accepted at ACL 2026</span>
<span class="paper-links"><a href="/files/disfcr.pdf">[PDF]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="/files/plait_aaai2027.pdf" aria-label="Open the PLAIT paper PDF"><img src="/images/plait-framework.png" alt="PLAIT parent-preserving response, claim, and span audit planning framework" width="1092" height="534" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title"><a href="/files/plait_aaai2027.pdf">PLAIT: From Hallucination Scores to Parent-Preserving Audit Plans</a></div>
<div class="paper-authors"><strong>Zhe Yu</strong>, Yunzhao Wei, Wenpeng Xing, Wenjie Luo, Zaobo He, Quan Chen, Meng Han</div>
<div class="paper-desc">PLAIT converts hallucination scores into parent-preserving response–claim–span audit plans, using whole-plan learning and exact budgeted optimization to capture more unsupported content per review minute.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at AAAI 2027</span>
<span class="paper-links"><a href="/files/plait_aaai2027.pdf">[PDF]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="/files/attribution_blind_spot.pdf" aria-label="Open The Attribution Blind Spot paper PDF"><img src="/images/attribution-blind-spot-framework.png" alt="Attribution Blind Spot paired signed interface and frozen-control evaluation framework" width="1202" height="686" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title"><a href="https://arxiv.org/abs/2605.26778">The Attribution Blind Spot: Detecting When Language Models Rely on Memory Rather Than Retrieved Context</a></div>
<div class="paper-authors"><strong>Zhe Yu*</strong>, Wenpeng Xing*, Bo Yang, Chen Ye, Gaolei Li, Yunzhao Wei, Meng Han</div>
<div class="paper-desc">Formalizes the attribution blind spot — when parametric memory and retrieved context produce identical surface text — and proposes Computational Reality Monitoring (CRM) to detect internal trajectory divergence.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at AAAI 2027</span>
<span class="paper-links"><a href="/files/attribution_blind_spot.pdf">[PDF]</a> <a href="https://arxiv.org/abs/2605.26778">[arXiv]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="/files/detecting_is_not_resolving.pdf" aria-label="Open the Calibration Does Not Certify a Contrast paper PDF"><img src="/images/calibration-contrast-gavel-framework.png" alt="GAVEL identical-pair audit and pair-level correction framework for LLM evaluators" width="1146" height="616" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title"><a href="/files/detecting_is_not_resolving.pdf">Calibration Does Not Certify a Contrast: Identification and Correction for LLM Evaluators</a></div>
<div class="paper-authors"><strong>Zhe Yu*</strong>, Wenpeng Xing*, Chen Ye, Xuyang Teng, Bo Yang, Changting Lin, Meng Han</div>
<div class="paper-desc">GAVEL shows item calibration cannot validate experimental contrasts: paired audits reveal that Qwen judges greatly overstate a reminder intervention.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at AAAI 2027</span>
<span class="paper-links"><a href="/files/detecting_is_not_resolving.pdf">[PDF]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="/files/Knowing_Is_Not_Acting.pdf" aria-label="Open the Knowing Is Not Acting paper PDF"><img src="/images/knowing-is-not-acting-framework.png" alt="Knowing Is Not Acting framework: threat channels, early recognition, late action, and matched intervention" width="1010" height="606" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title"><a href="/files/Knowing_Is_Not_Acting.pdf">Knowing Is Not Acting: Representation–Action Dissociation in Indirect Prompt Injection</a></div>
<div class="paper-authors"><strong>Zhe Yu</strong>, Wenpeng Xing, Zhenhua Xu, Xingxing Yang, Meng Han</div>
<div class="paper-desc">Shows that indirect prompt injection failure is not absent source recognition but representation–action dissociation: source role is linearly decodable early, yet tool decisions become causally controllable only in a late commitment band.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at NeurIPS 2026</span>
<span class="paper-links"><a href="/files/Knowing_Is_Not_Acting.pdf">[PDF]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="/files/cot_swap_neurips2026.pdf" aria-label="Open the Whose Thoughts paper PDF"><img src="/images/whose-thoughts-framework.png" alt="Whose Thoughts framework: CoT-Swap input, internal dissociation, behavioral outcome, and mechanistic repair" width="1076" height="518" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title"><a href="/files/cot_swap_neurips2026.pdf">Whose Thoughts? Chain-of-Thought Override in Reasoning-Tuned Language Models</a></div>
<div class="paper-authors"><strong>Zhe Yu</strong>, Wenpeng Xing, Zhenhua Xu, Ruiqi Zhang, Meng Han</div>
<div class="paper-desc">Exposes a structural source-override vulnerability in reasoning-tuned models: when the assistant-side &lt;think&gt; block contains a CoT for a different question, models answer the wrong question in the majority of cases.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at NeurIPS 2026</span>
<span class="paper-links"><a href="/files/cot_swap_neurips2026.pdf">[PDF]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="/files/fides.pdf" aria-label="Open the FIDES paper PDF"><img src="/images/fides-framework.png" alt="FIDES framework for faithful inference under retrieval-memory conflict" width="1218" height="540" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title"><a href="/files/fides.pdf">FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG</a></div>
<div class="paper-authors"><strong>Zhe Yu*</strong>, Wenpeng Xing*, Tiancheng Zhao, Mohan Li, Changting Lin, Meng Han</div>
<div class="paper-desc">Reveals token-level conflict concentration in retrieval-memory conflict and proposes a training-free decoder that fuses three complementary internal signals for per-token selective intervention.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at EMNLP 2026</span>
<span class="paper-links"><a href="/files/fides.pdf">[PDF]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="/files/cordon_mas.pdf" aria-label="Open the CORDON-MAS paper PDF"><img src="/images/cordon-mas-framework.png" alt="CORDON-MAS extractor, auditor, gate, and synthesizer information-flow architecture" width="1218" height="562" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title"><a href="https://arxiv.org/abs/2605.26754">Cordon-MAS: Defending RAG against Knowledge Poisoning via Information-Flow Control</a></div>
<div class="paper-authors"><strong>Zhe Yu*</strong>, Wenpeng Xing*, Gaolei Li, Shuguang Xiong, Hongzhi Wang, Xuyang Teng, Meng Han</div>
<div class="paper-desc">A multi-agent compartmentalized defense that enforces the Cordon Principle architecturally, reducing knowledge-poisoning attack success rate by 92.4%.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at EMNLP 2026</span>
<span class="paper-links"><a href="/files/cordon_mas.pdf">[PDF]</a> <a href="https://arxiv.org/abs/2605.26754">[arXiv]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="/files/composition_collapse.pdf" aria-label="Open the Composition Collapse paper PDF"><img src="/images/composition-collapse-framework.png" alt="Composition Collapse double-gate protocol for atomic stability and compositional reasoning" width="1736" height="980" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title"><a href="https://arxiv.org/abs/2605.26789">Composition Collapse: Stable Factual Knowledge Does Not Imply Compositional Reasoning</a></div>
<div class="paper-authors"><strong>Zhe Yu*</strong>, Wenpeng Xing*, Yunzhao Wei, Hongzhi Wang, Xuyang Teng, Meng Han</div>
<div class="paper-desc">Introduces a double-gate protocol that separates atomic knowledge stability from compositional reasoning, revealing post-training recipes can diverge by >40 pp in composition failure at matched atoms.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at EMNLP 2026</span>
<span class="paper-links"><a href="/files/composition_collapse.pdf">[PDF]</a> <a href="https://arxiv.org/abs/2605.26789">[arXiv]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="/files/fingerprint_vector.pdf" aria-label="Open the Fingerprint Vector paper PDF"><img src="/images/fingerprint-vector-framework.png" alt="Fingerprint Vector model fingerprint construction and verification process" width="1088" height="552" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title">Fingerprint Vector: Enabling Scalable and Efficient Model Fingerprint Transfer via Vector Addition</div>
<div class="paper-authors">Zhenhua Xu, Qichen Liu, Zhebo Wang, <strong>Zhe Yu</strong>, Xixiang Zhao, Wenpeng Xing, Dezhang Kong, Mohan Li, Meng Han</div>
<div class="paper-desc">Enables scalable and efficient model fingerprint transfer via vector addition for ownership verification.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at EMNLP 2026</span>
</div>
</div>
</div>

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="https://arxiv.org/abs/2604.05358" aria-label="Open the LatentAudit paper on arXiv"><img src="/images/latent-audit-framework.png" alt="LatentAudit white-box faithfulness monitor with optional verifiable deployment" width="980" height="416" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title"><a href="https://arxiv.org/abs/2604.05358">LatentAudit: Real-Time White-Box Faithfulness Monitoring for Retrieval-Augmented Generation with Verifiable Deployment</a></div>
<div class="paper-authors"><strong>Zhe Yu*</strong>, Wenpeng Xing*, Meng Han</div>
<div class="paper-desc">A real-time white-box auditor that measures Mahalanobis distance between residual-stream activations and evidence representations to judge RAG faithfulness at generation time.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at CoLM 2026</span>
<span class="paper-links"><a href="https://arxiv.org/abs/2604.05358">[arXiv]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="https://arxiv.org/abs/2604.05348" aria-label="Open the RETINA-SAFE and ECRT paper on arXiv"><img src="/images/retina-safe-ecrt-framework.png" alt="RETINA-SAFE and ECRT framework for retinal-evidence hallucination-risk triage" width="1240" height="596" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title"><a href="https://arxiv.org/abs/2604.05348">From Retinal Evidence to Safe Decisions: RETINA-SAFE and ECRT for Hallucination Risk Triage in Medical LLMs</a></div>
<div class="paper-authors"><strong>Zhe Yu*</strong>, Wenpeng Xing*, Meng Han</div>
<div class="paper-desc">A 12,522-sample evidence-grounded benchmark for diabetic retinopathy decision settings and a two-stage white-box detection framework (ECRT) for safe/unsafe risk triage with explicit subtype attribution.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at MICCAI 2026</span>
<span class="paper-links"><a href="https://arxiv.org/abs/2604.05348">[arXiv]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<a class="paper-thumb paper-thumb--image" href="/files/zkfpe.pdf" aria-label="Open the ZK-FPE paper PDF"><img src="/images/zkfpe-framework.png" alt="ZK-FPE fingerprint injection, zero-knowledge proving, registry, and two-step verification" width="1078" height="632" loading="lazy" decoding="async"></a>
<div class="paper-content">
<div class="paper-title">ZK-FPE: Blockchain-Verifiable Model Fingerprinting with Zero-Knowledge Privacy for Ownership Attribution</div>
<div class="paper-authors">Zhiguo Ma*, <strong>Zhe Yu</strong>, Wenpeng Xing, Yourong Chen, Meng Han</div>
<div class="paper-desc">Combines zero-knowledge proofs and blockchain to build verifiable model ownership attribution while preserving privacy.</div>
<div class="paper-meta">
<span class="paper-badge accepted">Accepted at ACM TURC 2026</span>
<span class="paper-links"><a href="https://www.acmturc.com/2026/cn/callforpaper.html">[CFP]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #006064, #00838f);">IoT</div>
<div class="paper-content">
<div class="paper-title">Trusted Metadata-Coordinated Tiered Off-Chain Storage for Recovery-Safe and Low-Latency IoT Data Management</div>
<div class="paper-authors">Weiping Yu, Weihan Wang, Mingyuan Yan, Keyang He, <strong>Zhe Yu</strong>, Wenpeng Xing, Liyuan Liu, Meng Han</div>
<div class="paper-desc">Trusted metadata-coordinated tiered off-chain storage for IoT data management with recovery safety and low latency.</div>
<div class="paper-meta">
<span class="paper-badge published">Electronics (MDPI)</span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #4a148c, #6a1b9a);">Optics</div>
<div class="paper-content">
<div class="paper-title"><a href="https://doi.org/10.1016/j.optcom.2025.131688">Orthogonal salinity and temperature detection via paralleled dual all-fiber interferometers</a></div>
<div class="paper-authors">F. Zhou, C. Chang, Q. Chang, H. Zhang, <strong>Zhe Yu</strong>, W. Liu, J. Li, J. Yang</div>
<div class="paper-desc">Orthogonal salinity and temperature detection using parallel dual all-fiber interferometers.</div>
<div class="paper-meta">
<span class="paper-badge published">Optics Communications, 2025</span>
<span class="paper-links"><a href="https://doi.org/10.1016/j.optcom.2025.131688">[DOI]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #5d4037, #795548);">Biblio</div>
<div class="paper-content">
<div class="paper-title"><a href="https://doi.org/10.1145/3711403.3711421">Bibliometric analysis of physical education research in China from 2014 to 2024</a></div>
<div class="paper-authors"><strong>Zhe Yu</strong>, H. Zeng, Y. Zhao, X. Zhang, Z. Wang, Y. Tao, M. Yuan, X. Sun</div>
<div class="paper-desc">A bibliometric analysis of physical education research trends, keyword co-occurrence, and institutional collaboration in China over a decade.</div>
<div class="paper-meta">
<span class="paper-badge published">ACM ICETM, 2025</span>
<span class="paper-links"><a href="https://doi.org/10.1145/3711403.3711421">[DOI]</a></span>
</div>
</div>
</div>

</div>

<span class='anchor' id='education'></span>

# Experience & Education

- <img class="institution-mark-inline" src="/images/institutions/hkust-gz.png" alt="" aria-hidden="true" width="500" height="133"> *May 2026 - Present*, **Hong Kong University of Science and Technology (Guangzhou)**
  - Research Assistant, advised by **[Prof. Chengwei Qin](https://qcwthu.github.io/)**
- <img class="institution-mark-inline" src="/images/institutions/zhejiang-university.png" alt="" aria-hidden="true" width="826" height="238"> *Nov 2025 - Present*, **[Binjiang Institute of Zhejiang University](https://ifrc-zju.github.io/)** ([IFRC Lab](https://ifrc-zju.github.io/)), Hangzhou, China
  - Research Intern, supervised by **[Dr. Meng Han](https://scholar.google.com/citations?user=TnCrl1cAAAAJ&hl=en)** and Dr. Wenpeng Xing
  - Part of the Guangdong Provincial Key R&D Program "Multimodal LLM Safety System Research and Application"
  - Part of the National Key R&D Program (Young Scientist Project) "Novel Trust System Based on Blockchain"
- <img class="institution-mark-inline" src="/images/institutions/university-of-malaya.png" alt="" aria-hidden="true" width="180" height="56"> *Jan 2025 - Feb 2025*, **University of Malaya**, Kuala Lumpur, Malaysia
  - Visiting Student
- <img class="institution-mark-inline" src="/images/institutions/westlake-university.png" alt="" aria-hidden="true" width="500" height="149"> *Mar 2024 - Sep 2024*, **Westlake University**, Hangzhou, China
  - Visiting Student, Optical Laboratory, supervised by Dr. Ziyang Zhang. Worked on dual all-fiber interferometer systems for orthogonal salinity/temperature detection (published in *Optics Communications*). This early cross-disciplinary research grounded my experimental rigor and shaped my approach to extracting and interpreting internal signals — a methodology central to my current work on LLM mechanistic interpretability and white-box auditing.
- <img class="institution-mark-inline" src="/images/institutions/communication-university-of-zhejiang.png" alt="" aria-hidden="true" width="500" height="85"> *2023 - Expected 2027*, **Communication University of Zhejiang**, Hangzhou, China
  - B.Eng. in Artificial Intelligence, supervised by Dr. Hao Zeng

<span class='anchor' id='patents'></span>

# 📜 Patents

- **Zhe Yu**, Wenpeng Xing, Meng Han. *A hallucination detection method based on dual-path internal state forcing logic for retrieval-augmented generation in large language models.* Pending Patent Application No. 202610260408X (Under Review).
- Meng Han, **Zhe Yu**, Jiayan Hu, Rongchang Li, Wenpeng Xing, Jingyi Yu, Zhen Hong, et al. *A post-processing method, system, device, and medium for hallucination detection in large language models based on adaptive order statistics aggregation.* Chinese Patent Application No. 2026107898102, filed Jun 3, 2026. (Pending)
- **Zhe Yu**, Jiayan Hu, Jingyi Yu, Weihang Yu, Wenpeng Xing, Jing Xiong, Yourong Chen, Zhen Hong, et al. *A hallucination detection method, system, and device for large language models based on multi-dimensional heterogeneous feature fusion.* Chinese Patent Application No. 2026107899270, filed Jun 3, 2026. (Pending)

<div align="center" style="margin-top: 3em;">
<div style="width: 140px; margin: 0 auto;"><script type="text/javascript" id="mmvst_globe" src="https://mapmyvisitors.com/globe.js?d=IF08ZbsA3iXnyu55Pfppr0C3PFdI45708vUhob6zDgI"></script></div>
<a href="https://mapmyvisitors.com/web/1c73q" title="Visit tracker">Visitor globe</a>
</div>
