# 俞哲（Zhe Yu）第一作者论文列表

> 以下按研究方向分类，涵盖 RAG 可信性、表示–行动分离、医学场景落地及早期探索工作。DISF 未包含在内。

---

## 一、RAG 可信性与幻觉检测主线

### 1. LatentAudit

| 项目 | 内容 |
|---|---|
| **英文标题** | LatentAudit: Real-Time White-Box Faithfulness Monitoring for Retrieval-Augmented Generation with Verifiable Deployment |
| **中文标题** | LatentAudit：面向检索增强生成的实时白盒忠实度监控与可验证部署 |
| **作者** | Zhe Yu*, Wenpeng Xing*, Meng Han |
| **机构** | Binjiang Institute of Zhejiang University (IFRC Lab), Zhejiang University |
| **发表** | Under review at **CoLM 2026** |
| **论文内容（一句话）** | 提出一种无需辅助裁判模型、在生成时即可运行的白盒监控器，通过测量残差流激活与证据表示的马氏距离来实时判断 RAG 输出是否忠实于检索证据，并支持 Groth16 零知识公开验证。 |
| **核心贡献** | • 提出基于残差流几何的二次型忠实度判别规则，无需辅助模型，运行时开销仅 0.77 ms。<br>• 证明该信号跨架构（Llama-2/3、Qwen-2.5/3、Mistral）和真实检索失败场景保持稳定。<br>• 设计 16-bit 定点审计规则，保留 99.8% FP16 AUROC，实现不暴露权重/激活的公开可验证部署。 |
| **实验效果** | 在 PubMedQA 上，Llama-3-8B 达到 **0.942 AUROC**；四路压力测试（矛盾、检索遗漏、部分支持噪声）下，PubMedQA **0.9566–0.9815 AUROC**，HotpotQA **0.9142–0.9315 AUROC**。 |

---

### 2. The Attribution Blind Spot

| 项目 | 内容 |
|---|---|
| **英文标题** | The Attribution Blind Spot: Detecting When Language Models Rely on Memory Rather Than Retrieved Context |
| **中文标题** | 归因盲区：检测语言模型何时依赖参数记忆而非检索到的上下文 |
| **作者** | Zhe Yu*, Wenpeng Xing*, Yunzhao Wei, Bo Yang, Chen Ye, Gaolei Li, Meng Han |
| **机构** | Binjiang Institute of Zhejiang University (IFRC Lab), Zhejiang University, National Fintech Evaluation Center, Hangzhou Dianzi University, Shanghai Jiao Tong University |
| **发表** | Under review at **ARR / EMNLP** |
| **论文内容（一句话）** | 当检索文档与预训练数据重叠时，模型可能完全凭记忆生成与上下文一致的文本，输出级监控无法区分"读过"与"记起"；本文提出计算现实监控（CRM），利用有/无上下文条件下内部表示的差异来检测这种归因盲区。 |
| **核心贡献** | • 形式化"归因盲区"：输出级监控在检索–记忆表面一致时失效。<br>• 提出 CRM，比较 with-context 与 no-context 内部轨迹的成员条件化偏移，发现该信号集中在架构特定的层模式。<br>• 通过块级噪声干预提供因果证据，验证 CRM 识别的层确实参与保存成员条件化信息。 |
| **实验效果** | 在 9 个模型变体上，似然基线 AUC 仅 0.55–0.60，而 **CRM-LR 达 0.71–0.95**；监督均值差方向比无监督 PC1 提升 **∆AUC +0.024–0.144**；BookMIA 上 AUC **0.84–0.97**；跨任务（摘要、QA）和数据集泛化良好，在域混淆基准上信号坍缩，验证边界条件。 |

---

### 3. FIDES

| 项目 | 内容 |
|---|---|
| **英文标题** | FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG |
| **中文标题** | FIDES：基于深层证据信号的 RAG 检索–记忆冲突忠实推理 |
| **作者** | Zhe Yu*, Wenpeng Xing*, Tiancheng Zhao, Mohan Li, Changting Lin, Meng Han |
| **机构** | Binjiang Institute of Zhejiang University (IFRC Lab), Zhejiang University |
| **发表** | Under review at **ARR / EMNLP** |
| **论文内容（一句话）** | 发现检索–记忆冲突在解码步骤上极度不均（token-level conflict concentration），提出无训练解码器 FIDES，融合输出表面、隐藏表示和预测轨迹三层内部信号，在冲突关键 token 上精准施加对比干预。 |
| **核心贡献** | • 揭示 token 级冲突集中现象：风险集中在少量答案关键 token，均匀全局对比会过度惩罚安全 token。<br>• 设计三层互补内部信号（输出层、表示层、轨迹层）的融合机制，实现逐 token 自适应干预强度。<br>• 将对比解码从"加多少"转化为"在哪里加"的 token 级控制问题。 |
| **实验效果** | 在 3 个知识冲突基准和 4 个主干预 backbone（7B/8B）上，**FIDES 在所有 12 个 setting 中取得最高上下文忠实度（CF）**，比最强无训练基线 AdaCAD 高 **+3.0–+12.8 points**，比标准 RAG 高 **+14.2–+28.3 points**；70B 规模上 fidelity 达 **92–94%**，F1 达 **62–63%**；token 选择性 AUROC = **0.923**。 |

---

### 4. Detecting Is Not Resolving

| 项目 | 内容 |
|---|---|
| **英文标题** | Detecting Is Not Resolving: The Monitoring–Control Gap in Retrieval-Augmented LLMs |
| **中文标题** | 检测不等于解决：检索增强大语言模型中的监控–控制差距 |
| **作者** | Zhe Yu*, Wenpeng Xing*, Chen Ye, Xuyang Teng, Bo Yang, Changting Lin, Meng Han |
| **机构** | Binjiang Institute of Zhejiang University (IFRC Lab), Zhejiang University, Hangzhou Dianzi University, National Fintech Evaluation Center |
| **发表** | Under review at **ARR / EMNLP** |
| **论文内容（一句话）** | 证明 RAG 系统的单轮安全评估会系统性地高估多轮对话中的安全性：模型能识别矛盾证据，但这种认知并不约束其最终推荐行为，存在结构性的"监控–控制差距"。 |
| **核心贡献** | • 提出多轮文档累积协议，通过 6 种时间模式控制误导证据何时进入持久化缓存，隔离监控–控制差距。<br>• 证明矛盾认知与安全解决在统计上独立（\|Δ\| < 0.10），且该差距随模型规模单调扩大。<br>• 通过隐藏状态探测、注意力分析和响应策略分类，定位缺陷核心在"行动选择"阶段而非检测或表示阶段。 |
| **实验效果** | 在 4 个模型族（1.5B–32B）上完成 **50,000+ turn-level 评估**；单轮诊断系统高估安全（T2 danger **0.44–1.00**）；Qwen2.5-7B 的 Uncertainty-OK 策略降低 danger **48%**（0.671→0.352），但无通用提示修复；32B 模型 pseudo-reconciliation 达 **100%**（自动评估）/ **91%**（人工标签，κ=0.66）。 |

---

### 5. CORDON-MAS

| 项目 | 内容 |
|---|---|
| **英文标题** | CORDON-MAS: Defending RAG against Knowledge Poisoning via Information-Flow Control |
| **中文标题** | CORDON-MAS：基于信息流控制的 RAG 知识投毒防御 |
| **作者** | Zhe Yu*, Wenpeng Xing*, Gaolei Li, Shuguang Xiong, Hongzhi Wang, Xuyang Teng, Meng Han |
| **机构** | Binjiang Institute of Zhejiang University (IFRC Lab), Zhejiang University, Shanghai Jiao Tong University, Zhejiang Lab, Harbin Institute of Technology, Hangzhou Dianzi University |
| **发表** | Under review at **ARR / EMNLP** |
| **论文内容（一句话）** | 发现 RAG 投毒防御的深层漏洞——模型能检测矛盾证据却仍执行投毒主张（监控–控制差距），提出"隔离原则"并通过多智能体架构（提取器-审计器-门-合成器）实现信息流隔离，将投毒攻击成功率降低 92.4%。 |
| **核心贡献** | • 识别并实证验证 RAG 安全中的监控–控制差距：检测矛盾≠行动安全。<br>• 提出 Cordon 原则：任何能进行最终自然语言合成的智能体不得访问不可信的自然语言证据。<br>• 设计非对称记忆权限的多智能体架构，通过脏读隔离、声明-only 通信和认证合成三层可证伪不变量实现该原则。 |
| **实验效果** | 在 5 个 BEIR 数据集上，CORDON-MAS 将攻击成功率（ASR）从 Vanilla RAG 的 **27.5%** 降至 **2.1%**，相对降低 **92.4%**；独立种子 123 复现平均 ASR 仅 **0.8%**；消融实验显示 Auditor 为最关键组件（移除后 ASR 增加 **4–16×**）。 |

---

### 6. Composition Collapse

| 项目 | 内容 |
|---|---|
| **英文标题** | Composition Collapse: Stable Factual Knowledge Does Not Imply Compositional Reasoning |
| **中文标题** | 组合坍塌：稳定的事实知识不意味着组合推理能力 |
| **作者** | Zhe Yu*, Wenpeng Xing*, Yunzhao Wei, Jie Chen, Hongzhi Wang, Xuyang Teng, Meng Han |
| **机构** | Binjiang Institute of Zhejiang University (IFRC Lab), Zhejiang University, Hong Kong Baptist University, Harbin Institute of Technology, Hangzhou Dianzi University |
| **发表** | Under review at **ARR / EMNLP** |
| **论文内容（一句话）** | 证明后训练效果的聚合基准评估存在盲区：原子知识统计无差异的后训练配方，在组合推理上可相差 40+ 百分点；提出双门控协议将后训练收益分解为原子稳定性、残余组合和临界深度三个独立通道。 |
| **核心贡献** | • 提出双门控协议：先验证原子事实的稳定性（跨释义一致），再测量残余组合失败，将评估从聚合差距转为原子受控的组合残差。<br>• 揭示后训练配方在原子稳定性饱和后，残余组合失败仍有 0%–47% 的跨度差异。<br>• 发现推理时计算约束（而非静态知识缺失）是组合失败的主要来源：CoT 恢复 70–75% 的通过门控后的失败。 |
| **实验效果** | 在 D4 V2 基准（390 题，深度 2–11）上评估 6 个 7–13B 模型和 4 种后训练配方；原子稳定性差异 <2 pp，但 depth 2 残余组合失败从 **0% 到 47%**； outcome-verified RL 在同等数据和计算下大幅优于 SFT 蒸馏；CoT 使残余失败降低 **3–5×**。 |

---

## 二、表示–行动分离主线

### 7. Knowing Is Not Acting

| 项目 | 内容 |
|---|---|
| **英文标题** | Knowing Is Not Acting: Representation–Action Dissociation in Indirect Prompt Injection |
| **中文标题** | 知而不行：间接提示注入中的表示–行动分离 |
| **作者** | Zhe Yu, Wenpeng Xing, Zhenhua Xu, Xingxing Yang, Meng Han |
| **机构** | Binjiang Institute of Zhejiang University (IFRC Lab), Zhejiang University |
| **发表** | Under review at **NeurIPS 2026** |
| **论文内容（一句话）** | 证明间接提示注入的失败并非源于模型无法识别攻击来源，而是来源角色信息在早期层已可被线性解码，但直到晚期动作承诺带才因果控制工具决策——存在"表示–行动分离"，且该路由具有通道条件性。 |
| **核心贡献** | • 建立因果阶梯：探针检测信息可用性 → 激活补丁检测因果可用性 → 投影干预验证局部化动作路径。<br>• 证明来源角色在 early residual stream 已线性可读（cross-template AUROC=1.00），但工具决策直到 late commitment band 才因果可控。<br>• 发现来源 grounding 是通道条件化的：工具输出、Slack 轨迹、持久记忆三个通道的方向近乎正交，跨通道干预失效。 |
| **实验效果** | 在 Qwen-2.5 (1.5B/7B) 和 Llama-3.1-8B 上，探针于 L4（大模型）/L8（1.5B）达到 AUROC=1.00；投影干预在直接攻击下将 Qwen-2.5-7B 的 ASR 降至 **8.5%**；匹配混淆方向可将 ASR 控制在 **22.4–34.2%**；通道错配干预基本无效。 |

---

### 8. Whose Thoughts?

| 项目 | 内容 |
|---|---|
| **英文标题** | Whose Thoughts? Chain-of-Thought Override in Reasoning-Tuned Language Models |
| **中文标题** | 谁的想法？推理微调语言模型中的思维链覆盖 |
| **作者** | Zhe Yu, Wenpeng Xing, Zhenhua Xu, Ruiqi Zhang, Meng Han |
| **机构** | Binjiang Institute of Zhejiang University (IFRC Lab), Zhejiang University |
| **发表** | Under review at **NeurIPS 2026** |
| **论文内容（一句话）** | 发现推理微调模型存在结构性源覆盖漏洞：当 assistant-side 的 `<think>` 块包含另一问题的思维链时，模型在绝大多数情况下回答错误的问题而非用户问题——源冲突信息被表示但未被路由进答案策略。 |
| **核心贡献** | • 提出 CoT-Swap 诊断协议：用户问 qi，`<think>` 块包含 qj 的良性 CoT，精确测试源覆盖。<br>• 证明推理微调模型（7B–70B）大规模回答注入的 trace 问题，而匹配的 instruct-tuned 对应模型显著更稳定。<br>• 通过 rank-k 学习投影引导（learned-projection steering）写回缺失的低秩信号，部分恢复全状态干预效果。 |
| **实验效果** | 在 10 个 open-weight 模型（7B–70B）上，推理微调模型 swap 后回答错误问题的比率显著高于 instruct 模型（TriviaQA gap **+45.5 pp**，PopQA **+18.1 pp**，GSM8K **+18.9 pp**，Fisher p < 10⁻¹²）；源探针 AUC = **1.000 ± 0.000**；Qwen3-8B 上 rank-1 引导提升 STABLE 率 **+17.3 pp**。 |

---

## 三、医学场景落地

### 9. RETINA-SAFE

| 项目 | 内容 |
|---|---|
| **英文标题** | From Retinal Evidence to Safe Decisions: RETINA-SAFE and ECRT for Hallucination Risk Triage in Medical LLMs |
| **中文标题** | 从视网膜证据到安全决策：医学大语言模型幻觉风险分级的 RETINA-SAFE 基准与 ECRT 框架 |
| **作者** | Zhe Yu*, Wenpeng Xing*, Meng Han |
| **机构** | Binjiang Institute of Zhejiang University (IFRC Lab), Zhejiang University |
| **发表** | Under review at **MICCAI 2026** |
| **论文内容（一句话）** | 针对糖尿病视网膜病变决策场景中医学 LLM 的幻觉问题，构建 12,522 样本的证据对齐/冲突/缺失三任务基准 RETINA-SAFE，并提出两阶段白盒检测框架 ECRT，实现安全/不安全风险分类与亚型归因。 |
| **核心贡献** | • 构建 RETINA-SAFE 基准：12,522 样本，按证据关系分为 E-Align（一致）、E-Conflict（冲突）、E-Gap（缺失）三类。<br>• 提出 ECRT 两阶段白盒框架：Stage 1 安全/不安全风险分类，Stage 2 将不安全案例细分为矛盾驱动型与证据缺失型。<br>• 利用 CTX/NOCTX 条件下的内部表示和 logit 偏移，结合类平衡训练实现鲁棒学习。 |
| **实验效果** | 在多个 backbone 上，ECRT Stage-1 平衡准确率比外部不确定性和自一致性基线高 **+0.15–0.19**，比最强适配监督基线高 **+0.02–0.07**；一致超过单阶段白盒消融。 |

---

## 四、早期探索工作

### 10. Bibliometric Analysis

| 项目 | 内容 |
|---|---|
| **英文标题** | Bibliometric Analysis of Physical Education Research in China from 2014 to 2024 |
| **中文标题** | 2014–2024 年中国体育教育研究文献计量分析 |
| **作者** | Zhe Yu, H. Zeng, Y. Zhao, X. Zhang, Z. Wang, Y. Tao, M. Yuan, X. Sun |
| **机构** | Communication University of Zhejiang |
| **发表** | In *Proceedings of the 2024 7th International Conference on Educational Technology Management*, **ACM**, 2025 |
| **论文内容（一句话）** | 对 2014–2024 年间中国体育教育研究领域的发文趋势、关键词共现和机构合作进行文献计量分析。 |
| **核心贡献** | • 系统梳理中国体育教育研究十年发文趋势。<br>• 分析高频关键词共现网络与研究热点演变。<br>• 识别主要研究机构与合作模式。 |
| **实验效果** | 基于 CNKI/WoS 数据库进行统计分析与可视化，具体量化指标见论文正文。 |

---

## 汇总表

| # | 论文 | 方向 | 投稿目标 |
|---|---|---|---|
| 1 | LatentAudit | RAG 白盒监控 | CoLM 2026 |
| 2 | Attribution Blind Spot | RAG 归因检测 | ARR / EMNLP |
| 3 | FIDES | RAG 忠实解码 | ARR / EMNLP |
| 4 | Detecting Is Not Resolving | RAG 监控–控制差距 | ARR / EMNLP |
| 5 | CORDON-MAS | RAG 投毒防御 | ARR / EMNLP |
| 6 | Composition Collapse | 组合推理评估 | ARR / EMNLP |
| 7 | Knowing Is Not Acting | 表示–行动分离（Agent 安全） | NeurIPS 2026 |
| 8 | Whose Thoughts? | 表示–行动分离（CoT 安全） | NeurIPS 2026 |
| 9 | RETINA-SAFE | 医学 LLM 幻觉检测 | MICCAI 2026 |
| 10 | Bibliometric Analysis | 文献计量（早期工作） | ACM 2025 |
