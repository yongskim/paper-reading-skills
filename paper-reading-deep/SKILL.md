---
name: paper-reading-deep
description: "跨领域深入阅读学术论文，按方法、实验、实证、定性、评测、综述、理论或论证等实际研究类型调整中文笔记。讲清叙事、问题、核心认识、研究设计和证据，核对关键来源，输出思源格式；不绑定学科或强套方法论文。"
---

# L2 论文精读

先读 [类型适配](../paper-reading/references/paper-types.md)、[阅读与证据规则](../paper-reading/references/reading-rules.md)、[笔记约定](../paper-reading/references/note-format.md) 和 [思源格式](../paper-reading/references/siyuan-format.md)。默认形成约 5–10 分钟可读完的客观笔记，复杂核心内容可展开。

先根据实际贡献判断主要/次要论文类型，用它决定分析重点，不据此决定思源存放目录。只要求某模块时集中处理该模块及必要前置内容。完整笔记保持以下七项功能，标题与子项按类型适配；不适用的子项省略，不制造论文没有的算法、训练、消融或实验。

读取 [跨领域规则](../paper-reading/references/domain-adaptation.md)，沿用论文自身术语与证据标准，补充必要背景时标明来源。理论、实验、观测、访谈、案例或文本研究按实际设计展开，不默认使用某学科的贡献或评测标准。

## 1. 一句话总结

先给「研究什么、关键做法/认识是什么、得到什么有范围的结果」一句话结论，再放紧凑的 Title / Year / Venue、领域、实际类型与版本信息。贡献有必要时最多三点，区分作者提出的内容与验证或工程工作。

## 2. Narrative Flow（叙事脉络）

按 [叙事规则](../paper-reading/references/narrative-flow.md) 讲清论文如何推进：先界定/观察什么，做了什么测量、设计或论证，再得到什么证据与结论。关键环节附定位，不当成真实科研时间线，不强拼攻击—防御或观察—算法链条。

## 3. Problem & Motivation

说明问题、重要性、已有处理方式、局限和待解决的 Gap。Benchmark 的 Gap 可以是评估缺口，实证可以是尚不清楚的现象，SoK 可以是缺少系统化理解，不强写「现有算法效果差」。区分任务事实与作者贡献叙事；Why now 只解释原文有依据的内容。

## 4. 核心认识与发现

按类型命名为 Core Insight、Key Findings、Design Principles 或 Taxonomy 等。区分作者的研究前假设、观察结果和事后解释；说清依据与提出时间。方法论文可梳理 Observation → Insight → Hypothesis → Design，其他类型按实际论证组织，不补造缺失环节。

## 5. 问题定义与适用条件

按 [类型适配表](../paper-reading/references/paper-types.md) 选择问题形式化、研究问题、任务范围、数据/采样条件、Threat Model、Workload 或定理前提。只列实质影响结论的条件。原文没有优化目标就不编造目标函数，没有说明假设合理性就写未论证。

## 6. 研究设计与技术内容

本部分的标题和结构随类型改变：

- 方法/模型：Method & Mechanism，解释 High-Level Idea、必要流程、关键公式与设计选择，适用时区分训练和推理。
- 实证：Research Design & Measurement，解释变量操作化、样本、测量流程、控制、分析与潜在混杂。
- Benchmark/数据集：Benchmark Design & Construction，解释任务、数据构建、标注质控、划分、指标、评测协议及泄漏控制。
- 综述/SoK：Scope, Taxonomy & Synthesis，解释范围、材料选择、分类维度及综合方式。
- 系统：System Design & Implementation，解释模块、状态、执行路径与关键约束。
- 理论：Definitions & Proof Structure，解释定义、引理依赖与证明思路。
- 观点：Argument & Reasoning，解释论证链及所依据的材料。

讲清为什么采用这些设计，以及从输入/材料到结果的过程，不逐段翻译或罗列无关实现。关键公式保留原 Equation 编号、符号含义、必要维度/范围和前提；解释用推导注明额外假设，不虚构证明。识别可疑时核查页面，无法确认则标记未核实。

### 技术或研究设计来源

对实质技术按 [方法溯源](../paper-reading-lineage/SKILL.md) 核对前作与本文改动，保留双侧证据。实证追查测量/分析协议，Benchmark 追查任务/数据/指标，SoK 追查分类框架；没有实质方法时不硬造算法谱系。标题可为 Method Lineage、Study Design Origins、Benchmark Origins 或 Taxonomy Origins。

先看明确来源，再对关键且来源不明的部分做定向核查；分别表述明确沿用、技术重合与可能来源。未知来源不等于原创；只用已有材料或禁止联网时说明范围。不扩成全领域综述。

## 7. 证据与主要发现

方法/系统可用 Evaluation & Findings，实证可用 Results & Validity，Benchmark 可用 Baseline Results & Coverage，理论可用 Theorems & Scope。重点回答：要支持什么主张，用什么证据，得到什么结果，结论适用于哪里。

关键数字同时记录指标方向、单位、条件、比较对象和 Figure/Table。区分相对百分比与百分点；派生计算标注计算来源，不将均值差异称为统计显著，不把有限观测推广为普遍或因果证明。

只解释实际存在的消融、敏感性、泛化、鲁棒性、覆盖、效度、开销或理论界。未做的评估写未报告，不直接判断方法失效。作者声称、条件下的实证支持与前提下成立的理论结论分别表述。

## 完成与归档

到实际适用内容结束，不追加弱点评审、自检答案或研究方案。用户要求思考题时只给 2–3 个针对性问题而不代答。保留用户批注、已有正确内容与实际材料覆盖。

用户要放入思源时读取 [画廊归档子 skill](../paper-reading-archive/SKILL.md)。未指定目录先问，已指定则直接沿用；按用户选择关联 PDF 首页画廊、文字索引与同一子文档，不自行归类。
