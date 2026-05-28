---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

Hi, I am Zhe Yu (俞哲), currently an undergraduate student pursuing my B.Eng. in Artificial Intelligence at the **Communication University of Zhejiang (CUZ)**, supervised by Dr. Hao Zeng. Since November 2025, I have been serving as a Research Intern at the **[Binjiang Institute of Zhejiang University](https://ifrc-zju.github.io/)** ([IFRC Lab](https://ifrc-zju.github.io/)), supervised by Dr. Meng Han and Dr. Wenpeng Xing. During my undergraduate studies, I also spent time as a Visiting Student at **Westlake University** (supervised by Dr. Ziyang Zhang) and the **University of Malaya**.

> 📢 **Seeking Opportunities:** I am actively looking for **Research Assistant (RA)** positions (on-site or remote) and seeking **Fall 2027 PhD** opportunities. Please feel free to drop me an [email](mailto:zyu@zju-if.com) if you are interested!

📄 **[Download my full CV (English)](/files/CV_Zhe_Yu_EN.pdf) | [获取完整中文简历](/files/CV_Zhe_Yu_CN.pdf)**

My research centers on **trustworthy language models** across three interconnected threads. First, I study the **internal mechanisms of knowledge grounding** — how parametric memory and retrieved evidence interact during generation, and how to detect failures like hallucinations, memory hijacking, and compositional reasoning collapse through white-box monitoring and mechanistic analysis. Second, I work on **representation–action dissociation** in reasoning and agentic systems — probing when and why models encode conflict information internally yet fail to route it into downstream decisions. Third, I explore **verifiable model ownership and decentralized trust** — combining fingerprinting, blockchain, and zero-knowledge proofs to build scalable, privacy-preserving attribution and deployment frameworks.

# 📚 Research Papers

<div class="paper-grid">
<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #1a4d8f, #2d6da8);">DISF</div>
<div class="paper-content">
<div class="paper-title"><a href="/files/disfcr.pdf">DISF: Detecting Hallucinations in Retrieval-Augmented Generation via Dual-path Internal State Forcing Framework</a></div>
<div class="paper-authors"><strong>Zhe Yu</strong>*, <strong>Wenpeng Xing</strong>*, Wenjie Luo, Weize Xu, Lingtong Huang, Yourong Chen, Changting Lin, Meng Han</div>
<div class="paper-desc">A dual-path internal-state forcing framework that detects hallucinations in RAG by leveraging white-box activation signals.</div>
<div class="paper-meta">
<span class="paper-badge accepted">ACL Findings 2026</span>
<span class="paper-links"><a href="/files/disfcr.pdf">[PDF]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #1a4d8f, #2d6da8);">LA</div>
<div class="paper-content">
<div class="paper-title"><a href="https://arxiv.org/abs/2604.05358">LatentAudit: Real-Time White-Box Faithfulness Monitoring for Retrieval-Augmented Generation with Verifiable Deployment</a></div>
<div class="paper-authors"><strong>Zhe Yu</strong>*, <strong>Wenpeng Xing</strong>*, Meng Han</div>
<div class="paper-desc">A real-time white-box auditor that measures Mahalanobis distance between residual-stream activations and evidence representations to judge RAG faithfulness at generation time.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at CoLM 2026</span>
<span class="paper-links"><a href="https://arxiv.org/abs/2604.05358">[arXiv]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #1a4d8f, #2d6da8);">ABS</div>
<div class="paper-content">
<div class="paper-title"><a href="https://arxiv.org/abs/2605.26778">The Attribution Blind Spot: Detecting When Language Models Rely on Memory Rather Than Retrieved Context</a></div>
<div class="paper-authors"><strong>Zhe Yu</strong>*, <strong>Wenpeng Xing</strong>*, Bo Yang, Chen Ye, Gaolei Li, Yunzhao Wei, Meng Han</div>
<div class="paper-desc">Formalizes the attribution blind spot — when parametric memory and retrieved context produce identical surface text — and proposes Computational Reality Monitoring (CRM) to detect internal trajectory divergence.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at ARR / EMNLP</span>
<span class="paper-links"><a href="/files/attribution_blind_spot.pdf">[PDF]</a> <a href="https://arxiv.org/abs/2605.26778">[arXiv]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #1a4d8f, #2d6da8);">FIDES</div>
<div class="paper-content">
<div class="paper-title"><a href="/files/fides.pdf">FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG</a></div>
<div class="paper-authors"><strong>Zhe Yu</strong>*, <strong>Wenpeng Xing</strong>*, Tiancheng Zhao, Mohan Li, Changting Lin, Meng Han</div>
<div class="paper-desc">Reveals token-level conflict concentration in retrieval-memory conflict and proposes a training-free decoder that fuses three complementary internal signals for per-token selective intervention.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at ARR / EMNLP</span>
<span class="paper-links"><a href="/files/fides.pdf">[PDF]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #1a4d8f, #2d6da8);">DINR</div>
<div class="paper-content">
<div class="paper-title"><a href="https://arxiv.org/abs/2605.27157">Detecting Is Not Resolving: The Monitoring–Control Gap in Retrieval-Augmented LLMs</a></div>
<div class="paper-authors"><strong>Zhe Yu</strong>*, <strong>Wenpeng Xing</strong>*, Chen Ye, Xuyang Teng, Bo Yang, Changting Lin, Meng Han</div>
<div class="paper-desc">Demonstrates a structural monitoring–control gap in RAG: models detect contradictory evidence but this awareness fails to constrain final recommendations, and single-turn diagnostics systematically overestimate multi-turn safety.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at ARR / EMNLP</span>
<span class="paper-links"><a href="/files/detecting_is_not_resolving.pdf">[PDF]</a> <a href="https://arxiv.org/abs/2605.27157">[arXiv]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #1a4d8f, #2d6da8);">CORDON</div>
<div class="paper-content">
<div class="paper-title"><a href="https://arxiv.org/abs/2605.26754">Cordon-MAS: Defending RAG against Knowledge Poisoning via Information-Flow Control</a></div>
<div class="paper-authors"><strong>Zhe Yu</strong>*, <strong>Wenpeng Xing</strong>*, Gaolei Li, Shuguang Xiong, Hongzhi Wang, Xuyang Teng, Meng Han</div>
<div class="paper-desc">A multi-agent compartmentalized defense that enforces the Cordon Principle architecturally, reducing knowledge-poisoning attack success rate by 92.4%.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at ARR / EMNLP</span>
<span class="paper-links"><a href="/files/cordon_mas.pdf">[PDF]</a> <a href="https://arxiv.org/abs/2605.26754">[arXiv]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #1a4d8f, #2d6da8);">CC</div>
<div class="paper-content">
<div class="paper-title"><a href="https://arxiv.org/abs/2605.26789">Composition Collapse: Stable Factual Knowledge Does Not Imply Compositional Reasoning</a></div>
<div class="paper-authors"><strong>Zhe Yu</strong>*, <strong>Wenpeng Xing</strong>*, Yunzhao Wei, Hongzhi Wang, Xuyang Teng, Meng Han</div>
<div class="paper-desc">Introduces a double-gate protocol that separates atomic knowledge stability from compositional reasoning, revealing post-training recipes can diverge by >40 pp in composition failure at matched atoms.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at ARR / EMNLP</span>
<span class="paper-links"><a href="/files/composition_collapse.pdf">[PDF]</a> <a href="https://arxiv.org/abs/2605.26789">[arXiv]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #5c3d8f, #7b5aa6);">KINA</div>
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
<div class="paper-thumb" style="background: linear-gradient(135deg, #5c3d8f, #7b5aa6);">WT</div>
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
<div class="paper-thumb" style="background: linear-gradient(135deg, #2d7d5e, #4a9e78);">RETINA</div>
<div class="paper-content">
<div class="paper-title"><a href="https://arxiv.org/abs/2604.05348">From Retinal Evidence to Safe Decisions: RETINA-SAFE and ECRT for Hallucination Risk Triage in Medical LLMs</a></div>
<div class="paper-authors"><strong>Zhe Yu</strong>*, <strong>Wenpeng Xing</strong>*, Meng Han</div>
<div class="paper-desc">A 12,522-sample evidence-grounded benchmark for diabetic retinopathy decision settings and a two-stage white-box detection framework (ECRT) for safe/unsafe risk triage with explicit subtype attribution.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at MICCAI 2026</span>
<span class="paper-links"><a href="https://arxiv.org/abs/2604.05348">[arXiv]</a></span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #6c757d, #8d959d);">FV</div>
<div class="paper-content">
<div class="paper-title">Fingerprint Vector: Enabling Scalable and Efficient Model Fingerprint Transfer via Vector Addition</div>
<div class="paper-authors">Zhenhua Xu, Qichen Liu, Zhebo Wang, <strong>Zhe Yu</strong>, Xixiang Zhao, Wenpeng Xing, Dezhang Kong, Mohan Li, Meng Han</div>
<div class="paper-desc">Enables scalable and efficient model fingerprint transfer via vector addition for ownership verification.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at ARR / EMNLP</span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #6c757d, #8d959d);">ZK-FPE</div>
<div class="paper-content">
<div class="paper-title">ZK-FPE: Blockchain-Verifiable Model Fingerprinting with Zero-Knowledge Privacy for Ownership Attribution</div>
<div class="paper-authors">Zhiguo Ma*, Wenpeng Xing*, <strong>Zhe Yu</strong>*, Yourong Chen, Meng Han</div>
<div class="paper-desc">Combines zero-knowledge proofs and blockchain to build verifiable model ownership attribution while preserving privacy.</div>
<div class="paper-meta">
<span class="paper-badge under-review">Under review at Blockchain: Research and Applications</span>
</div>
</div>
</div>

<div class="paper-card">
<div class="paper-thumb" style="background: linear-gradient(135deg, #6c757d, #8d959d);">IoT</div>
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
<div class="paper-thumb" style="background: linear-gradient(135deg, #6c757d, #8d959d);">Optics</div>
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
<div class="paper-thumb" style="background: linear-gradient(135deg, #6c757d, #8d959d);">Biblio</div>
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
# 📖 Education

- *Nov 2025 - Present*, **[Binjiang Institute of Zhejiang University](https://ifrc-zju.github.io/)** ([IFRC Lab](https://ifrc-zju.github.io/)), Hangzhou, China
  - Research Intern, supervised by Dr. Meng Han and Dr. Wenpeng Xing
  - Part of the Guangdong Provincial Key R&D Program "Multimodal LLM Safety System Research and Application"
  - Part of the National Key R&D Program (Young Scientist Project) "Novel Trust System Based on Blockchain"
- *Jan 2025 - Feb 2025*, **University of Malaya**, Kuala Lumpur, Malaysia
  - Visiting Student
- *Mar 2024 - Sep 2024*, **Westlake University**, Hangzhou, China
  - Visiting Student, Optical Laboratory, supervised by Dr. Ziyang Zhang. Worked on dual all-fiber interferometer systems for orthogonal salinity/temperature detection (published in *Optics Communications*). This early cross-disciplinary research grounded my experimental rigor and shaped my approach to extracting and interpreting internal signals — a methodology central to my current work on LLM mechanistic interpretability and white-box auditing.
- *2023 - Expected 2027*, **Communication University of Zhejiang**, Hangzhou, China
  - B.Eng. in Artificial Intelligence, supervised by Dr. Hao Zeng

# 📜 Patents

- **Zhe Yu**, Wenpeng Xing, Meng Han. *A hallucination detection method based on dual-path internal state forcing logic for retrieval-augmented generation in large language models.* Pending Patent Application No. 202610260408X (Under Review).

<div align="center" style="margin-top: 3em;">
<script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=OTJYDY0Z4P1NmL6mTiI0AdLsTFwNyd0S4UN-urz6AAE&cl=ffffff&w=a"></script>
</div>
