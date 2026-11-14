# FDE Foundations, Engagement Lifecycle & AI Systems Architecture｜FDE 基础、项目生命周期与 AI 系统架构

> Course: Forward Deployed Engineer for AI Systems (Educative) — Lessons 1–14

<svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="860" height="210" fill="#fff"/>
  <text x="430" y="24" font-size="15" text-anchor="middle" font-weight="bold">FDE Engagement Lifecycle｜FDE 项目生命周期</text>
  <g font-size="12" text-anchor="middle">
    <rect x="15" y="50" width="120" height="64" rx="8" fill="#e8f0fe" stroke="#3367d6"/>
    <text x="75" y="76">Discovery</text><text x="75" y="94">需求调研</text>
    <rect x="155" y="50" width="120" height="64" rx="8" fill="#e8f0fe" stroke="#3367d6"/>
    <text x="215" y="76">Scoping</text><text x="215" y="94">范围界定 / 架构</text>
    <rect x="295" y="50" width="120" height="64" rx="8" fill="#fef7e0" stroke="#e37400"/>
    <text x="355" y="76">POC Sprint</text><text x="355" y="94">概念验证 (~2 wk)</text>
    <rect x="435" y="50" width="120" height="64" rx="8" fill="#fef7e0" stroke="#e37400"/>
    <text x="495" y="76">Pilot</text><text x="495" y="94">试点 (real users)</text>
    <rect x="575" y="50" width="120" height="64" rx="8" fill="#e6f4ea" stroke="#137333"/>
    <text x="635" y="76">Handoff</text><text x="635" y="94">交付移交</text>
    <rect x="715" y="50" width="130" height="64" rx="8" fill="#fce8e6" stroke="#c5221f"/>
    <text x="780" y="76">Field Feedback</text><text x="780" y="94">现场反馈回路</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="135" y1="82" x2="153" y2="82"/><line x1="275" y1="82" x2="293" y2="82"/>
    <line x1="415" y1="82" x2="433" y2="82"/><line x1="555" y1="82" x2="573" y2="82"/>
    <line x1="695" y1="82" x2="713" y2="82"/>
    <path d="M780 116 C780 190, 75 190, 75 118"/>
  </g>
  <g font-size="11" fill="#444" text-anchor="middle">
    <text x="75" y="134">problem + data + owner</text>
    <text x="215" y="134">scope doc (6 parts)</text>
    <text x="355" y="134">Proceed / Pivot / Stop</text>
    <text x="495" y="134">reliability·adoption·trust</text>
    <text x="635" y="134">docs·monitoring·HITL</text>
    <text x="430" y="182">patterns across customers → product roadmap｜跨客户模式 → 产品路线图</text>
  </g>
</svg>

---

## 1. Who Is a Forward Deployed Engineer?｜什么是前线部署工程师

Source: https://www.educative.io/courses/forward-deployed-engineer/who-is-a-forward-deployed-engineer

### 要点 / Key ideas

- **核心问题：部署鸿沟 (deployment gap)**。企业已有强模型和工程团队，但大量 AI 项目卡在 **试点 (pilot)** 无法进 **生产 (production)**。原因往往不是模型，而是：要贴合工作流 (workflows)、接生产数据 (production data)、满足运维约束 (operational constraints)、让用户敢依赖 (user confidence)。
- **起源 (origin)：Palantir**。最早客户是政府/国防 (government & defense)，数据高度敏感、流程任务特定，标准的需求调研/采购渠道收集不到真实需求。Palantir 把工程师 **嵌入 (embed)** 客户现场，直接对真实系统写生产代码。"软件合身，因为是在它要运行的地方造的。"
- **双重职能 (dual function)**：FDE 一边给客户交付 (delivery)，一边把跨客户的 **共性模式 (consistent patterns)** 反馈回核心产品 (product insight)。2010 年代中期 Palantir 的 FDE 数量超过普通软件工程师。
- **为什么 AI 让这个模式复兴**：生成式 AI (generative AI) 和 **智能体系统 (agentic systems)** 让每个行业同时遇到 Palantir 当年的部署问题。模型只是一部分：还要接对数据、遵守 **访问控制 (access controls)**、融入现有流程、处理 **边界情况 (edge cases)**、赢得信任。
- **模型失败 vs 部署失败 (model failures vs deployment failures)**：访问规则不完整、源数据过期 (stale data)、流程没有负责人 (no clear owner) —— 这些都是部署问题，每家都不同，远程产品团队预见不到。
- **行业信号 (industry signals)**：2026 年 5 月 OpenAI 成立企业部署公司 DeployCo；同月 Anthropic 与 Blackstone、Hellman &amp; Friedman、Goldman Sachs 宣布企业 AI 服务公司。2025 年 FDE 职位发布量增长 **800%+**。部署正在成为核心产品与工程能力，而非模型开发后的"交接"。
- **FDE 常建的系统类型 (system types FDEs build)**：

| 系统类型 System type | 作用 What it does |
|---|---|
| 文档问答 Document Q&amp;A tool | 基于检索 (retrieval) + 语言模型，从精选知识库回答问题 |
| 分类流水线 Classification pipeline | 按内容路由/打标签（工单、合同） |
| 知识综合系统 Knowledge synthesis system | 查询多个数据源，生成结构化综合答案 |
| 智能体工作流 Agentic workflow | 接收目标、多步推理、调用工具 (tool calls)，无需逐步指挥完成任务 |

- **基础技能 (baseline)**：LLM API、Agent 流水线设计、**评估 (evaluations)**、生产部署。**FDE 的增量**：在客户环境里运作、处理组织约束、在 **模糊性 (ambiguity)** 下做正确判断、在从未完整定义的条件下可靠交付。
- **技术深度 × 运营判断 (technical depth × operational judgment)**：只有技术没有贴近客户 → 系统孤立地工作；只有贴近客户没有技术 → 建议永远落不了地。FDE 两者兼具，所以难招且价值高。
- FDE 的判断包括：为问题选对架构、理解系统运行环境、识别 **真正有风险的失败模式 (failure modes that carry real risk)**、确定 **何时人工介入 (when a human should step in)**。

<svg viewBox="0 0 760 230" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="760" height="230" fill="#fff"/>
  <text x="380" y="22" font-size="15" text-anchor="middle" font-weight="bold">Why pilots stall: the deployment gap｜部署鸿沟</text>
  <rect x="20" y="50" width="200" height="120" rx="10" fill="#e8f0fe" stroke="#3367d6"/>
  <text x="120" y="80" font-size="13" text-anchor="middle" font-weight="bold">Model capability</text>
  <text x="120" y="98" font-size="12" text-anchor="middle">模型能力</text>
  <text x="120" y="125" font-size="11" text-anchor="middle">works in a demo</text>
  <text x="120" y="141" font-size="11" text-anchor="middle">演示中可行</text>
  <rect x="270" y="40" width="220" height="150" rx="10" fill="#fef7e0" stroke="#e37400" stroke-dasharray="5,4"/>
  <text x="380" y="62" font-size="13" text-anchor="middle" font-weight="bold">Gap = deployment problems</text>
  <g font-size="11" text-anchor="middle">
    <text x="380" y="84">right data / 正确数据接入</text>
    <text x="380" y="102">access controls / 访问控制</text>
    <text x="380" y="120">fits workflow / 融入流程</text>
    <text x="380" y="138">edge cases / 边界情况</text>
    <text x="380" y="156">clear owner / 明确负责人</text>
    <text x="380" y="174">user trust / 用户信任</text>
  </g>
  <rect x="540" y="50" width="200" height="120" rx="10" fill="#e6f4ea" stroke="#137333"/>
  <text x="640" y="80" font-size="13" text-anchor="middle" font-weight="bold">Dependable production</text>
  <text x="640" y="98" font-size="12" text-anchor="middle">可依赖的生产系统</text>
  <text x="640" y="125" font-size="11" text-anchor="middle">people rely on it</text>
  <line x1="220" y1="110" x2="268" y2="110" stroke="#555" stroke-width="1.5"/>
  <line x1="490" y1="110" x2="538" y2="110" stroke="#555" stroke-width="1.5"/>
  <text x="380" y="215" font-size="12" text-anchor="middle" fill="#c5221f">FDE closes this gap from inside the customer｜FDE 在客户内部弥合</text>
</svg>

### 面试怎么说 / How to say it in the interview

**Q: What is an FDE, in your own words? / 你怎么理解 FDE？**
> "An FDE closes the gap between what a model can do in a demo and a system a customer actually relies on in production. Most enterprise AI failures aren't model failures — they're deployment failures: stale data, incomplete access rules, a workflow nobody owns. I sit inside the customer environment, scope the right problem, ship production code against their real systems, and bring the patterns I see back to the product team."
>
> 中文：FDE 弥合"演示可行"与"生产可依赖"之间的鸿沟；大多数失败是部署问题而非模型问题，并且要把现场模式带回产品。

**Q: Model failure or deployment failure? / 给一个例子区分**
> "If a RAG assistant gives a wrong answer because the policy index wasn't re-ingested after last month's update, that's a deployment failure — the model did exactly what it was given. A model failure would be the model misreading a correctly retrieved clause. I always rule out data, access and ownership before I blame the model."
>
> 中文：索引没更新导致答错是部署失败；检索正确但模型误读才是模型失败。先排除数据/权限/负责人。

**Q: How is an FDE different from a solutions engineer or a product engineer?**
> "A solutions engineer usually helps a customer adopt the product pre-sale; a product engineer builds for the average customer from a roadmap. An FDE writes production code inside one customer's environment, owns delivery outcomes, and also acts as a signal source back to product. It's both technical depth and customer proximity at once."
>
> 中文：SE 偏售前；产品工程师面向平均客户；FDE 在单一客户环境写生产代码、对结果负责，同时反哺产品。

---

## 2. Getting Started with This Course｜课程导览

Source: https://www.educative.io/courses/forward-deployed-engineer/getting-started-with-this-course

### 要点 / Key ideas

- 课程两个目标：**做好 FDE 工作**（从第一次调研到最终移交）+ **拿到 FDE offer**（在时间压力下展示同样的判断力）。
- **课程结构 (course map)**：FDE 角色与生命周期 → AI 系统架构（LLM/agentic、**驾驭工程 harness engineering**、编排模式、框架选择）→ FDE 面试与系统设计（可复用方法 + 集成模式）→ 案例研究（金融知识助手到客服 agent）→ 顶级公司准备（Anthropic、Google Cloud、OpenAI、Palantir）→ **Take-home 大师课** → FDE 成长。
- **动手 (hands-on)**：Claude + Agent SDK + MCP；OpenAI Responses API + Agents SDK；Gemini + **ADK (Agent Development Kit)**；Palantir 编码轮的 Python 练习；Cloud labs；Mock interviews。
- **先修要求 (prerequisites) 五项**：

| 领域 Area | 要求 Expectation |
|---|---|
| Python | 熟练编写、运行、调试 |
| LLM API 与提示 LLM APIs &amp; prompting | 代码调用模型 API、写 system prompt、拿 **结构化输出 (structured output)** |
| RAG 与智能体 RAG &amp; agents | 至少做过一个检索流水线和一个用工具的 agent |
| 评估 Evaluation | 用可重复方法衡量输出质量 |
| 集成基础 Integration basics | REST API、认证 (authentication)、JSON/CSV |

- **环境如何改变工作**：内部项目 = 数据熟悉、访问即时、时间线内部、成功由自己定义；客户项目 = 技术工作不变，多了一层 **判断层 (judgment layer)**：做什么、简化什么、早点暴露什么、环境更复杂时怎么维持干系人信心。
- **时间线属于客户 (the timeline belongs to the customer)**：错过演示日，截止日不变，信任受损。要 **按可用时间界定范围 (scope to the time available)**，而不是按理想方案。第一个交付物是 **证明核心价值的最小可用系统 (smallest working system that demonstrates core value)**，用它 "赢得继续做的权利 (earn the right to build more)"。

### 面试怎么说 / How to say it in the interview

**Q: How do you handle a tight customer deadline? / 客户时间紧怎么办？**
> "In a customer engagement the timeline belongs to the customer, so I scope to the time available rather than the ideal solution. I pick the smallest working system that proves the core value, ship it on the date, and use that to earn the right to build more. Missing a demo date doesn't move the deadline — it just costs trust."
>
> 中文：按时间定范围，先交最小可证明价值的系统，用它赢得后续。

---

## 3. Running Customer Discovery｜客户需求调研

Source: https://www.educative.io/courses/forward-deployed-engineer/running-customer-discovery

### 要点 / Key ideas

- 很多企业 AI 项目在 **问题定义 (problem definition)** 阶段就失败：定义错问题、没有清晰 **成功标准 (success criteria)**。调研错了 → 建错系统、范围过大、或六周后发现数据格式不对。
- **调研 = 以对话形式进行的结构化技术调查 (structured technical investigation conducted as a conversation)**。不是销售、不是咨询、不是设计。
- 客户第一次通常描述的是：**症状 (symptom)**（"每周浪费几小时"）、**已定好的方案 (pre-decided solution)**（"我们要个 chatbot"）、或 **高层目标 (high-level outcome)**（"用 AI 提效"）。FDE 要倒推出底下真正的工作流问题。
- **克制 (restraint)**：一旦在调研会上提架构，调查就变成 **推销 (pitch)**。调研的产出不是方案，而是足以写 **范围文档 (scope document)** 的问题、数据、干系人 (stakeholders)、约束的清晰图景。

**谁应在场 (who to get in the room)**：

| 角色 Role | 贡献 Contribution |
|---|---|
| 执行发起人 Executive sponsor | 拥有问题、控制预算，把对话锚定在组织真正会投钱的优先级上 |
| 运营/领域专家 Ops person / domain expert | 实际干活的人，知道流程在哪断；描述系统"实际怎么跑"而非"设计上怎么跑"——往往信息量最大 |
| 技术联系人 Technical contact | 知道涉及哪些系统、数据在哪、访问实际如何——判断 **技术可行性 (feasibility)** 必需 |

缺一个就记录缺失视角，在定稿 scope 前安排定向跟进 (targeted follow-up)。

- **开场 (opening)**：请对方完整讲一遍流程如何崩：什么触发失败、谁介入、哪些工作卡住、团队怎么恢复。叙事比直接问"痛点是什么"能暴露更多系统、交接、手工步骤和失败模式。
- **问变通方案 (ask about the workaround)**：官方流程讲完后问"流程断了时你们实际怎么做"。**变通方案是真实痛点最清晰的信号**。
- **要听的三类信号 (what to listen for)**：
  1. **数据信号 (data signals)**：每个系统名、文件类型、数据源都是技术范围的积木，全记下，不打断。
  2. **量与频率 (volume &amp; frequency)**：多久做一次、一次多久 → 把模糊痛点变成可衡量的 **基线 (baseline)**。
  3. **所有权空白 (ownership gaps)**：没人说得清谁负责的步骤 = 风险，会在构建期最糟糕的时候冒出来。

**五列笔记法 (5-column note framework)**：

| 陈述的痛点 Stated pain | 当前流程步骤 Current workflow steps | 可用数据 Data available | 候选成功指标 Candidate success metric | 访问阻碍 Blockers to access |
|---|---|---|---|---|
| "供应商报价比对耗时" | 收邮件→手工录表→比价→审批 | 邮件 PDF、ERP 供应商表 | 每单处理时间从 X 降到 Y | ERP 只读权限需安全审批 |

- **收尾 (closing)**：复述 —— "核心问题是…，涉及数据是…，成功的样子是…"。复述时错位立刻暴露，在会上发现远好于写完 scope 后。

**离场前清单 (checklist before leaving the session)**：
1. 所需数据是否存在，且能在项目时间内拿到？
2. 是否有具体、可衡量、项目结束前能验证的成功标准？
3. 客户时间线对实际要建的东西是否现实？
4. 组织内是否有 **一个** 拥有问题、有权清除阻碍、全程主要联系人的人？

**识别真正的 AI 机会 (recognizing real AI opportunities)** —— 四个信号：

| 信号 Signal | 说明 Explanation | 典型架构 Fit |
|---|---|---|
| 文档密集的综合与抽取 Document-heavy synthesis &amp; extraction | 大量合同/报告/邮件/政策的阅读、摘要、抽取、比对 | 生成模型 / 结构化抽取 |
| 大规模知识检索 Knowledge retrieval at scale | 从大知识库答题、按政策标准处理请求、按内容路由 | RAG |
| 带条件逻辑的多步流程 Multi-step workflows with conditional logic | 收集输入→应用规则→路由，每步有条件决策 | Agentic 工作流 |
| 高吞吐的重复判断 Repetitive judgment at throughput | 决策模式一致、标准稳定、价值随量增长 | 分类/优先级/路由 |

- 高量场景早算 **推理成本 (inference costs)**：每天上千次调用前沿模型很贵，成本是立项论证的一部分。
- **警告：先建立基线 (establish the baseline first)** —— 当前流程的时间/错误率成本。客户答不上，建立基线就是第一步，否则无法证明改进。

**调研常见失败模式 (what goes wrong in discovery)**：

| 失败模式 Failure pattern | 表现 Symptom | 对策 Fix |
|---|---|---|
| 过早给方案 Solutioning too early | 客户开始对方案反应而不是描述问题 | 设计决策全部放到问题清楚之后 |
| HiPPO 问题 (Highest-Paid Person's Opinion) | 高管讲愿景而非运营痛点 | 不得罪高管，把话题引向干活的人 |
| 调研中范围蔓延 Scope creep in discovery | 客户现场不断加需求 | 以"已记录内容"总结收尾；新需求放到 scope 草稿后单独谈 |
| 调研表演 Discovery theater | 走过场、浅问题、接受模糊回答 | 追问数据和流程细节，直到能写 scope |
| 跳过基线 Skipping the baseline | 不知道当前时间、错误率、预计 token 成本 | 调研阶段建立基线，再提任何方案 |

**Challenge：制造业采购 (Manufacturing company procurement)**
- English problem: *An FDE meets a VP of Operations and a procurement manager who want "AI for procurement." From the conversation, identify the actual workflow bottleneck, the data it depends on, and the manual work done today.*
- 解题思路（课程挑战的核心是"把模糊的 'AI 提升采购' 还原为具体瓶颈"）：用五列笔记法拆解 —— 典型答案形态是"采购专员手工把多家供应商报价（邮件/PDF）录入表格、对照 ERP 中的历史价格与合同条款比对、再人工审批"，瓶颈在 **非结构化报价的抽取与比对**；数据是邮件附件、ERP 供应商/价格表；成功指标是单次比价耗时与错误率。

### 面试怎么说 / How to say it in the interview

**Q: How do you run a discovery session? / 你怎么跑调研？**
> "I treat discovery as a technical investigation, not a pitch, so I don't propose architecture in the room. I try to get three people there — the executive sponsor, the person who actually does the work, and a technical contact — and I open by asking them to walk me through the last time the workflow broke and what they did instead. I capture notes in five columns: pain, workflow steps, data, a candidate metric, and access blockers. Before leaving I play the problem back and check four things: the data exists and is accessible, there's a measurable success criterion, the timeline is realistic, and there's one owner who can clear blockers."
>
> 中文：调研是调查不是推销；三类人在场；以"上次怎么崩、怎么绕"开场；五列笔记；复述 + 四项检查。

**Q: The customer says "we want a chatbot." What do you do?**
> "I treat that as a solution they've already picked, not the problem. I ask what happens today when someone needs that answer — who they ask, how long it takes, how often it happens. Often the real need is something narrower, like extracting fields from contracts, which a structured extraction call handles better than a chatbot."
>
> 中文：把"要 chatbot"当作预设方案，倒推真实工作流问题。

**Q: A senior executive dominates the session. How do you handle it?**
> "That's the HiPPO problem. I acknowledge the executive's vision and tie it to the budget priority, then say something like, 'To make sure we build toward that, can Maria walk me through how a case actually flows today?' That moves the conversation to the people who do the work without sidelining the sponsor."
>
> 中文：认可高管愿景，再礼貌把话题转给一线执行者。

**Q: How do you decide if a problem is really an AI problem?**
> "I look for four signals: document-heavy extraction or synthesis, knowledge retrieval at scale, multi-step workflows with conditional logic, or repetitive judgment at high volume. If none fit, a rules engine or a simple script is often the right answer. And I always establish the baseline cost first — including projected token cost at volume — so I can prove improvement."
>
> 中文：四信号判断是否 AI 问题；先建基线（含 token 成本）。

---

## 4. Scoping and Solution Architecture｜范围界定与方案架构

Source: https://www.educative.io/courses/forward-deployed-engineer/scoping-and-solution-architecture

### 要点 / Key ideas

- 调研产出问题定义 → **范围界定 (scoping)** 把它变成提案：建什么、哪种架构、开工前要处理哪些风险。在开工前把 scope 定对，比 sprint 中途纠正便宜得多。
- **范围文档 (scope document)** = FDE 与客户的 **共识协议 (shared agreement)**，目的是 **对齐 (alignment)**。它 **不是产品规格 (product specification)**：规格描述数月/季度的愿景；scope 描述 **接下来 2–4 周** 建什么、演示什么、怎么衡量。它覆盖 **POC 阶段**（典型 2 周，以演示 + 是否继续的决策结束）。

**范围文档六要素 (six elements of a scope document)**：

| 要素 Element | 内容 Content |
|---|---|
| 问题陈述 Problem statement | 1–2 句，用 **客户自己的语言** 描述具体工作流问题 |
| 成功指标 Success metric | 具体可衡量的质量阈值：精确率/召回率 (precision/recall)、错误降低百分比、处理速度，在 **定义好的测试集 (defined test set)** 上评估 |
| 数据源 Data sources | 读什么数据、在哪、谁控制访问 |
| 技术依赖 Technical dependencies | 内部 API、存储、认证服务、外部模型 API、LLM 供应商、检索/向量存储 (vector store)、要读写的内部系统 |
| 范围之外 Out of scope | 明确列出这一版 **不做** 什么 |
| 时间线 Timeline | 可演示成果的日期 |

- **Out-of-scope 是承重墙 (load-bearing)**：客户中途加需求时，FDE 指向它；没有它，每个新请求都"合理"。

**翻译阶梯 (translation ladder)** —— 五层把业务问题变成可构建的 AI 组件（例：律所每份供应商合同审核 3 小时）：

| 层级 Level | 问题 Question | 合同审核例子 Contract review example |
|---|---|---|
| 1 业务痛点 Business pain | 业务上痛在哪？ | 法务审核瓶颈拖慢供应商入驻数天，积压清不掉 |
| 2 用户流程 User workflow | 人现在怎么做？ | 律师读合同 → 对照标准条款 → 标记偏差 → 路由给审批人 |
| 3 数据流 Data flow | 数据怎么流动？ | 合同以 PDF 邮件到达；标准条款在共享盘；审批在表格里跟踪 |
| 4 系统集成 System integration | 要接哪些系统？ | 邮箱、文档存储、审批流程 |
| 5 AI 组件 AI component | 模型具体做什么？ | 抽取关键条款 → 对比标准条款 → 生成结构化 **偏差报告 (deviation report)** 给律师审 |

- **最小 AI 组件原则 (minimal AI component principle)**：找模型价值最大、集成工作最少的地方。例中条款抽取 + 比对是最重的活；审批路由和邮件集成第一版可保持手工。先攻最费力的一步 → 最可衡量的改进、最低构建复杂度。
- **范围探针 (scoping spike)**：调研后数据情况仍不清楚时，做 1–2 天调查：确认能访问什么、什么格式、是否够干净。是定稿前最后一步信息收集。

**架构选择 (architecture selection)** —— 决定构建复杂度、数据需求、延迟、评估方法、运营成本；写入 scope：

| 问题信号 Problem signal | 架构 Architecture approach |
|---|---|
| 大量文档需抽取、比对、摘要 | 结构化 LLM 抽取 (structured LLM extraction) 或 RAG 流水线 |
| 从大型内部知识库回答问题 | RAG + 语义检索 (semantic retrieval) |
| 多步流程、条件路由、工具调用、系统间交接 | 带定义工具的智能体工作流 (agentic workflow with defined tools) |
| 大批量分类/打标/路由 | 约束输出的结构化 LLM 调用 (structured LLM call with constrained output) |

- 第一版只证明核心能力，不加 POC 不需要验证的复杂度。
- **Token 预算与成本 (token budget &amp; cost)**：Agentic（多次工具调用、长上下文）每事务 token 成本最高；RAG 只送相关上下文，降低成本；结构化抽取可 **批处理 (batch)** 优化。公式：**每事务 token × 预计日量 (tokens per transaction × projected daily volume)**，在定架构前确认可行。POC 规模能跑、生产规模财务不可持续 = 应写入 scope 的风险。
- 与客户技术联系人沟通架构理由：为什么适合、运行需要什么、当前局限在哪。
- **企业集成上下文 (enterprise integration context)**：邮件、Slack、**CRM**、**ERP**、内部 API、SharePoint/Confluence。组件读写的系统和问题本身一样决定架构。

**技术风险登记册 (technical risk register)**：

| 风险 Risk | 说明 Description |
|---|---|
| 数据质量 Data quality | 企业数据不一致、不完整、结构与调研描述不同 —— 最常见的中途意外，也最可早发现 |
| 访问延迟 Access delays | IT 安全审查（API、数据库凭证 (credentials)、云权限）比客户估计的久；两周 POC 可能完全卡住，需第一天前确认 |
| 模型性能差距 Model performance gaps | 基座模型 (foundation model) 在窄领域（法律、医疗、金融术语/缩写/格式）表现差 |
| Token 预算超支 Token budget overrun | 生产量下推理成本超预算 |
| 延迟与吞吐 Latency &amp; throughput | 小测试集可接受，全量日处理不达标 |

每条风险记录四项：**风险本身、可能性 (likelihood)、影响 (impact)、具体缓解计划 (mitigation)**。

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| ERP API access delayed by security review | High | High (blocks POC) | Request access in week 0; build against exported CSV sample meanwhile |
| Clause language too domain-specific | Medium | Medium | Few-shot examples from firm's own contracts; evaluate on 50 real contracts |

- 早沟通风险 = 建立信任：在 scoping 时得知数据访问问题的客户会成为合作者；第三周才发现的会变成沮丧的干系人 (stakeholders)。
- **无解场景检查 (no-win scenario check)**：数据、访问、架构约束下没有现实路径得到可演示结果 → 开工前暂停。开工前退出比中途停滞更专业。

<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="760" height="300" fill="#fff"/>
  <text x="380" y="22" font-size="15" text-anchor="middle" font-weight="bold">Translation Ladder｜翻译阶梯</text>
  <g font-size="12">
    <rect x="40" y="40" width="300" height="40" rx="6" fill="#fce8e6" stroke="#c5221f"/>
    <text x="55" y="65">1 Business pain｜业务痛点</text>
    <rect x="80" y="90" width="300" height="40" rx="6" fill="#fef7e0" stroke="#e37400"/>
    <text x="95" y="115">2 User workflow｜用户流程</text>
    <rect x="120" y="140" width="300" height="40" rx="6" fill="#fffde7" stroke="#b08900"/>
    <text x="135" y="165">3 Data flow｜数据流</text>
    <rect x="160" y="190" width="300" height="40" rx="6" fill="#e8f0fe" stroke="#3367d6"/>
    <text x="175" y="215">4 System integration｜系统集成</text>
    <rect x="200" y="240" width="300" height="40" rx="6" fill="#e6f4ea" stroke="#137333"/>
    <text x="215" y="265" font-weight="bold">5 AI component｜AI 组件</text>
  </g>
  <g font-size="11" fill="#444">
    <text x="520" y="65">review backlog delays onboarding</text>
    <text x="520" y="115">read → compare → flag → route</text>
    <text x="520" y="165">PDF email · shared drive · sheet</text>
    <text x="520" y="215">inbox · doc store · approvals</text>
    <text x="520" y="265">extract clauses → deviation report</text>
  </g>
  <text x="380" y="295" font-size="11" text-anchor="middle" fill="#137333">narrow each level; keep routing/email manual in v1｜逐层收窄，v1 保持路由/邮件手工</text>
</svg>

### 面试怎么说 / How to say it in the interview

**Q: What goes into your scope document? / 你的 scope 文档包含什么？**
> "Six things: a one- or two-sentence problem statement in the customer's words, a measurable success metric against a defined test set, the data sources and who controls access, technical dependencies including the model provider, an explicit out-of-scope list, and a demo date. The out-of-scope list is load-bearing — it's what I point to when someone asks for one more feature mid-sprint."
>
> 中文：六要素；out-of-scope 是承重墙。

**Q: How do you go from a vague business problem to an AI component?**
> "I walk down five levels: business pain, user workflow, data flow, system integration, then the AI component. At the last step I apply the minimal-AI-component principle — put the model where it removes the most effort with the least integration. For contract review, that's clause extraction and comparison; email intake and approval routing stay manual in version one."
>
> 中文：五层阶梯 + 最小 AI 组件原则。

**Q: How do you choose between RAG, an agent, or a single LLM call?**
> "I match the problem signal. Classification at volume is a structured LLM call with constrained output. Questions over a large knowledge base is RAG. Only when the task genuinely needs multi-step conditional routing and tool calls do I reach for an agent — and I check token cost per transaction times daily volume before I commit, because agents are the most expensive per transaction."
>
> 中文：按信号匹配；agent 最贵，先算成本。

**Q: What risks do you put in the register?**
> "Data quality, access delays, domain-specific model gaps, token budget overrun, and latency at full volume. For each I write likelihood, impact, and a concrete mitigation. Access delay is the one I chase hardest, because a two-week POC dies if credentials aren't ready on day one."
>
> 中文：五类风险，每条写可能性/影响/缓解；访问延迟最致命。

---

## 5. The Proof of Concept (POC) Sprint｜概念验证冲刺

Source: https://www.educative.io/courses/forward-deployed-engineer/the-proof-of-concept-poc-sprint

### 要点 / Key ideas

- POC 冲刺回答一个问题：**这个方法，用这些数据，在这个客户环境里，是否可行？** 不相关的一律放到 sprint 范围外。
- 开工前设定预期：sprint 结束时我们会 **知道是否可行**，而 **不会** 得到生产就绪 (production-ready) 系统。客户常以为 POC 是缩小版最终产品，要提前纠正。
- **POC = 有时限的实验 (time-boxed experiment)**，产出是 **答案不是产品**。三种发现都有效：按范围可行 / 需特定调整后可行 / 对此问题和数据不可行。产生清晰答案即成功。
- 时限迫使取舍；做得比核心假设需要的多 → 什么都做不好、答案也弱。

**Sprint 四阶段 (four stages, in sequence; 时长因项目而异但不可跳过)**：

| 阶段 Stage | 做什么 What | 结束条件 / 要点 Exit / notes |
|---|---|---|
| 1 访问与环境搭建 Access &amp; environment setup | 确认模型 API 凭证、数据读权限、代表性测试集样本、与技术联系人的沟通渠道 | 能对真实数据（或可靠近似）写和跑代码；依赖缺失时立即区分能并行做的和必须等的 |
| 2 数据探索与验证 Data exploration &amp; validation | 看格式、结构一致性、样本是否代表生产分布 (production population) | **不可省略**，即使调研时描述很详细 |
| 3 构建到首个可用输出 Building toward a working output | 先让真实输入端到端跑出结果（质量低也行），再对照成功指标在 **约定测试集** 上迭代 | 尽快出第一个输出 &gt; 尽快达到高质量；不靠"看起来不错"的个人判断 |
| 4 评估与演示准备 Evaluation &amp; demo prep | 正式测试集评估、做演示界面、起草 **结论文档 (readout document)** | 每天结束发简短异步更新 (async update)：完成了什么、卡在哪、下一步；早分享粗糙中间结果 |

- 客户长时间听不到消息会用担忧填补沉默。

**应对环境变化 (responding to the environment)**：
- **访问延迟 (access delayed)**：用 **合成输入 (synthetic inputs)** 或 **模拟响应 (mock responses)** 继续建；记录每个 mock：模拟了什么、真实版本替换什么、最终评估用什么。**正式评估必须用真实数据**。
- **数据与描述不符 (data differs from description)**：按实际可用数据构建，记录所有假设，向客户报告差异及具体影响。"数据比预期难"没用；"30% 合同是扫描件无文本层，需要 OCR (optical character recognition)，预计增加 2 天"才有用。
- **版本控制与文档 (version control &amp; docs)**：第一天就用仓库 (repository)，频繁提交、清晰信息，像别人要维护一样写代码 —— 后续移交依赖这个纪律。
- **假设当场记录 (record assumptions as they happen)**：事后重建的记录不完整。

**POC 演示 = 价值叙事 (value narrative)**，不是技术走查或功能巡游，三段：

| 段 Part | 内容 Content |
|---|---|
| 之前 Before | 当前流程：团队怎么做、每件多久、错误率/成本 —— 建立对比基线 |
| 之中 During | 在测试集的 **真实、代表性** 输入上跑系统；典型输入的强结果比精挑输入的完美结果更有说服力，客户看得出区别 |
| 之后 After | 展示输出并连接业务影响：本例省多少时间？按每周量算是多少？ |

- 现场失败：冷静承认 → 切换录制备份 (recorded backup) → 解释原因。现场故障时的镇定比在无挑战问题上的完美演示更显信心。
- **测量与决策**：演示前与客户确认 scope 里的指标和阈值仍是约定标准（防止客户换标准）。话术："我们约定目标是这个指标、这个阈值，这是测量结果。"
- 除主指标外还报告：**延迟 (latency)**、**预计量下每事务成本 (cost per transaction)**、**边界情况表现 (edge-case performance)**。

**三种结局 (three outcomes)**：

| 结局 Outcome | 条件 Condition | 动作 Action |
|---|---|---|
| 继续 Proceed | 指标达成、集成可行、客户有信心 | 离场前约定下一步 |
| 转向 Pivot | 指标未达，但揭示了更具体路径 | 定义下次尝试前要改什么 |
| 停止 Stop | 方法对此问题/数据不可行，或生产规模成本/延迟不可行 | 以最低成本得出的正确答案 |

- Proceed ≠ POC 直接进生产。下一阶段建更完整系统：更广输入、接生产环境、真实用户测试。离场前约定：谁、做什么、何时、客户需提供什么；FDE 写简短跟进文档（下一阶段建什么、首批用户是谁、成功如何定义）。
- **Readout 文档**：一页 —— 建了什么、测了什么、结果如何、建议。

<svg viewBox="0 0 760 240" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="760" height="240" fill="#fff"/>
  <text x="380" y="22" font-size="15" text-anchor="middle" font-weight="bold">POC Sprint → Outcome｜POC 冲刺与结局</text>
  <g font-size="12" text-anchor="middle">
    <rect x="15" y="45" width="130" height="56" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="80" y="68">1 Access setup</text><text x="80" y="86">访问与环境</text>
    <rect x="160" y="45" width="130" height="56" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="225" y="68">2 Data explore</text><text x="225" y="86">数据探索验证</text>
    <rect x="305" y="45" width="130" height="56" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="370" y="68">3 First output</text><text x="370" y="86">首个输出→迭代</text>
    <rect x="450" y="45" width="130" height="56" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="515" y="68">4 Eval + demo</text><text x="515" y="86">评估与演示</text>
    <rect x="610" y="20" width="135" height="40" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="677" y="45">Proceed 继续</text>
    <rect x="610" y="70" width="135" height="40" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="677" y="95">Pivot 转向</text>
    <rect x="610" y="120" width="135" height="40" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="677" y="145">Stop 停止</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="145" y1="73" x2="158" y2="73"/><line x1="290" y1="73" x2="303" y2="73"/><line x1="435" y1="73" x2="448" y2="73"/>
    <line x1="580" y1="73" x2="608" y2="40"/><line x1="580" y1="73" x2="608" y2="90"/><line x1="580" y1="73" x2="608" y2="140"/>
  </g>
  <g font-size="11" fill="#444">
    <text x="20" y="135">daily async update: done / blocked / next｜每日异步更新</text>
    <text x="20" y="155">mocks documented; final eval on real data only｜mock 需记录，正式评估只用真实数据</text>
    <text x="20" y="175">demo: Before → During → After (value narrative)｜演示三段式</text>
    <text x="20" y="195">report: metric + latency + cost/txn + edge cases｜指标+延迟+成本+边界</text>
    <text x="20" y="215">1-page readout: built / measured / result / recommendation｜一页结论</text>
  </g>
</svg>

### 面试怎么说 / How to say it in the interview

**Q: What does a successful POC look like? / 什么是成功的 POC？**
> "A POC is a time-boxed experiment that answers one question — does this approach work with this data in this environment. It succeeds when it produces a clear answer: proceed, pivot, or stop. A stop is still a success if we got there cheaply. I set that expectation on day one so the customer doesn't expect a mini production system."
>
> 中文：POC 回答一个问题，清晰的 Proceed/Pivot/Stop 都算成功；第一天就设定预期。

**Q: Credentials are delayed in week one. What do you do?**
> "I split the build into what depends on that access and what doesn't, and keep moving on the rest using mocks or synthetic inputs. I document every mock — what it stands in for and what will replace it — and I'm explicit that the final evaluation runs on real data only. I also flag the delay in the daily update with the impact on the demo date."
>
> 中文：拆分依赖、用 mock 推进并记录；正式评估只用真实数据；每日更新里报影响。

**Q: How do you structure a demo?**
> "Before, during, after. I start with today's baseline — how long a case takes and the error rate — then run a typical input from the test set, not a cherry-picked one, and close by translating the result into time saved at their weekly volume. If something breaks live, I acknowledge it calmly and switch to a recording."
>
> 中文：基线→典型输入→业务影响；现场失败切录屏。

**Q: The POC missed the metric. Now what?**
> "First I confirm we're measuring against the threshold we agreed in the scope. Then I look at where it failed — if the misses cluster in one input category and there's a clear fix, I recommend a pivot with a specific change. If cost or latency at production scale makes it infeasible, I recommend stop and write it up in the one-page readout."
>
> 中文：先确认标准一致；失败集中且可修 → pivot；规模不可行 → stop。

---

## 6. The Pilot Phase｜试点阶段

Source: https://www.educative.io/courses/forward-deployed-engineer/the-pilot-phase

### 要点 / Key ideas

- POC 问"方法可行吗？"；**试点 (pilot)** 问"更完整版本在终端用户的日常工作流、类生产运营条件下是否可行？" 测试集揭示受控技术表现；真实用户揭示 **组织契合 (organizational fit)**、意外输入、输出是否可信到能改变工作方式。测试集上 91% 准确率仍可能因用户不懂、不信、集成摩擦而无人采用。
- 试点直接先于全面部署；这里学到的决定客户全量上线前需要准备什么。

**试点比 POC 多的三件事 (what the pilot adds)**：

| 新增 Addition | 说明 Description |
|---|---|
| 更广输入覆盖 Broader input coverage | 用户会发送的完整分布，包括测试集里没有的意外、脏数据 |
| 真实系统集成 Live system integrations | 真实认证、实时数据流、**回写 (write-back)** 到用户已用的系统 |
| 错误处理与边界逻辑 Error handling &amp; edge-case logic | POC 排除的情况现在按运营深度处理 |

- **明确排除 (explicit exclusions)**：生产级监控基础设施、完整合规 (compliance) 与审计文档、数据治理 (data governance) 审批、全组织推广的扩容工作 —— 是排除项，不是延期的试点任务；属于移交阶段。

**试点范围文档 (pilot scope) 五项**：能力 (capabilities)、集成 (integrations)、用户（谁、角色、每天做什么）、时间线（构建周数、反馈周期频率、readout 时间）、成功标准（三维：**真实条件下的指标表现、采用率 (adoption rate)、用户信任信号 (trust signals)**）。
- 反馈节奏：每周或双周结构化用户 check-in + 持续错误日志；无结构 check-in 的试点反馈来得太晚。
- **影子模式 (shadow mode)**：AI 处理与现有流程相同的请求，输出在后台记录、不展示给用户，现有流程继续驱动所有决策。FDE 与客户技术团队并排对比两组输出，找失败模式。影子输出稳定可靠后进入 **活跃阶段 (active phase)**：试点用户组在实际工作中使用 AI 输出。

**与真实用户合作 (working with real users)**：
- **设定预期**：沟通三件事 —— 系统做什么、不做什么、怎么报问题。否则用户要么几次好结果后 **过度依赖 (over-reliance)**，要么第一次出错就弃用。不到一小时的 **入门会 (orientation session)**：目的、已知局限、反馈渠道。
- **收集反馈**：共享表单、专用 Slack/Teams 频道、每周 check-in。有用反馈 = 用户输入 + 系统输出 + 哪里错了。FDE 全程审阅，不只在结尾。
- **范围内迭代 (iterating within scope)**：范围内改进就做；新需求记录并延后。试点中途扩范围会延期，并在测试进行中改变被测对象，扭曲评估。

**评估试点表现的三个信号 (three readiness signals)**：

| 信号 Signal | 问题 Question | 证据 Evidence | 弱时说明 When weak |
|---|---|---|---|
| 可靠性 Reliability | 真实条件下行为是否一致？ | 稳定延迟、各输入类型质量可预测、**无静默失败 (no silent failures)**；看 **分布而非均值 (distribution, not mean)** | 平均值好但某类输入集中失败 |
| 采用 Adoption | 用户是否纳入工作流？ | 不再查手工替代、使用规律、团队围绕输出组织工作 | 指标强但采用低 → 信任或可用性问题，非技术问题 |
| 信任 Trust | 用户是否直接依据输出行动？ | 低 **复核率 (re-verification rate)**、低 **覆盖率 (override rate)** | 准确率高但人人复核 → 尚未建立信心 |

**匹配练习 (quiz content)**：
- "8 个用户中 7 个不再查手工流程，主要用 AI 输出" → **采用 (Adoption)**
- "用户即使输出看着正确也逐条复核后才提交" → **信任 (Trust)**
- "高峰日响应延迟增加 4 倍，系统未改动" → **可靠性 (Reliability)**

**试点收尾 (closing the pilot)**：
- **Readout**：试点用户是谁、时长、真实条件下的指标、采用数据（使用模式、回退手工的频率）、信任信号（覆盖率、反馈主题）、建议。
- **两种主要结局**：**继续全面部署 (proceed to full deployment)** —— 三信号都正面，离场前定义部署前提；**延长试点 (extend the pilot)** —— 某信号需要更多时间或特定干预，定义改什么和时间线。罕见情况：出现 POC 时不可见的根本约束（治理限制、数据访问变化、组织决策），FDE 要诚实暴露并与客户确定路径。
- **部署前提 (deployment prerequisites)** —— 客户承诺，不是 FDE 交付物：**指定系统负责人 (named system owner)**、**用户支持渠道 (support channel)**、**FDE 离开后的性能监控计划 (monitoring plan)**。

### 面试怎么说 / How to say it in the interview

**Q: How is a pilot different from a POC?**
> "A POC proves the approach works on a test set. A pilot proves a more complete system works for real users in their daily workflow — broader inputs, live integrations with real auth and write-back, and proper error handling. I'm explicit about what the pilot excludes: production monitoring infrastructure, full compliance docs, and org-wide scaling belong to the handoff."
>
> 中文：POC 证明方法；试点证明真实用户可用；明确排除生产监控、合规、扩容。

**Q: Accuracy is 91% but nobody uses it. What's going on?**
> "Strong metrics with low adoption usually points to trust or usability, not the model. I'd look at override and re-verification rates, sit with a few users, and check whether the integration adds friction — say, they have to copy output into another system. I'd also check the distribution: 91% on average can hide one input category that fails constantly, which kills trust."
>
> 中文：指标高采用低 → 信任/可用性问题；看覆盖率、现场观察、检查分布。

**Q: How would you start a pilot safely?**
> "I'd often start in shadow mode: the AI processes the same requests as the existing process, but its outputs are logged in the background and nobody acts on them. We compare side by side, fix failure patterns, and only move to the active phase once the shadow outputs are consistently reliable."
>
> 中文：先影子模式并排对比，稳定后再进入活跃阶段。

**Q: Pilot users keep asking for new features. How do you respond?**
> "I fix what's inside the agreed scope and log the rest for a later phase, and I tell them that explicitly so they know they were heard. Expanding scope mid-pilot changes what we're testing while the test is running, which makes the readout meaningless."
>
> 中文：范围内的做，范围外的记录延后；中途扩范围会扭曲评估。

---

## 7. The Project Handoff｜项目移交

Source: https://www.educative.io/courses/forward-deployed-engineer/the-project-handoff

### 要点 / Key ideas

- 客户收到什么和建了什么同样重要。没有文档、监控、受训负责人的系统 = 制造 **依赖 (dependency)** 而非 **交付物 (deliverable)**。移交是 FDE 在本项目的最后正式动作：让没参与构建的人能拥有、运营、改进系统。
- 传统软件靠通过/失败的测试验证；AI 系统输出是 **概率性的 (probabilistic)**，行为随输入分布变化，测试套件抓不到 **质量漂移 (quality drift)** 或真实量下的延迟退化。

**部署就绪五维度 (five dimensions of deployment readiness)** —— 移交前与客户约定，每维有 **最低可行水平 (minimum viable level)** 和 **目标水平 (target level)**：

| 维度 Dimension | 就绪标准 Readiness criterion |
|---|---|
| 可靠性 Reliability | 无意外失败、静默错误、未处理边界；**峰值负载 (peak load)** 行为在上线前刻画，而非假设 |
| 输出质量 Output quality | 试点约定的准确率/精确率/召回率在真实部署量和全部输入范围上保持，不只在测试集 |
| 安全 Safety | 任何可能造成下游伤害的输出类型都有人工审核 (human review) 步骤；对 **执行动作 (take actions)** 的 agentic 系统尤其重要 |
| 成本 Cost | 全量下的 token 和基础设施成本在客户承诺预算内 —— 是就绪条件，不是上线后的事 |
| 可观测性 Observability | FDE 离开后运营团队能看到发生了什么、早发现质量退化、独立排查故障 |

- 约定阈值本身就有价值：减少上线后争议，明确客户之后要维护什么。
- **最小可行部署 (minimum viable deployment)**：约定上线的最低负责任阈值，不等理想状态。可用性、流程覆盖可上线后改进；**安全和可观测性必须先达到最低阈值** 才能支持生产决策。

**FDE 移交的四个组件 (four handoff components)**：代码、嵌在代码中的文档、正式移交文档、现场移交会。

- **为别人写的代码 (code written for someone else)**：一致命名、**配置与逻辑分离 (separate configuration from logic)**、不依赖只在 FDE 本地存在的工具、第一天就提交到客户可访问可运行的仓库 (repository)、非显而易见处写注释、README 说明本地搭建和测试。

**移交文档五部分 (handoff document)**：

| 部分 Section | 内容 Content |
|---|---|
| 系统概览 System overview | 做什么、接受什么输入、产出什么、**不处理什么** |
| 数据流 Data flow | 数据从哪来、怎么流动、存什么、发给哪些外部 API |
| 已知失败模式 Known failure modes | 怎么失败、多频繁、触发条件、进行中请求会怎样 |
| 监控设置 Monitoring setup | 跟踪什么、阈值、每个告警 (alert) 在运营上意味着什么 |
| 升级路径 Escalation path | 何时人工介入、找谁、他们要做什么 |

用客户工程团队懂的语言写；需要 FDE 解读的文档等于没移交。

- **移交会 (handoff session)**：给客户工程团队端到端走查（架构、数据流、监控配置、已知失败模式），**录制**。目标不是讲一次就算完，而是确认团队能独立运行、监控、排障，并知道超出 **运行手册 (runbook)** 时找谁。

**部署后监控五类 (five monitoring categories)** —— AI 质量可能逐渐退化而日志里没有任何技术错误：

| 类别 Category | 关注点 What to watch |
|---|---|
| 延迟 Latency | 是否满足运营要求；峰值是否保持；是否随时间上升 |
| 错误率 Error rate | 超时、API 错误、未处理异常；稳定还是上升 |
| 输出质量抽样 Output quality sampling | 每周随机抽样，按试点约定标准审查并记录偏差 —— 不抽样就看不到渐进漂移（新输入分布、数据新鲜度） |
| 每查询成本 Cost per query | 是否在预算内；agentic 系统成本突增常意味着异常行为，如 **重复工具调用 (repeated tool calls)** |
| 用户参与信号 User engagement signals | 是否持续使用；**覆盖率上升 (rising override rate)** 通常意味质量漂移或新边界类别 |

**人在回路兜底 (human-in-the-loop fallback)** —— 不是泛泛的安全声明，而是三部分配置机制：

| 部分 Component | 说明 Description |
|---|---|
| 触发条件 Trigger | 何时转人工：**置信度 (confidence score)** 低于阈值、命中标记类别（高额交易、敏感文档、异常请求模式）、技术失败。部署前约定 |
| 队列 Queue | 转到哪里、谁负责审、多长时间内决定。没有指定审核人和响应时限 = 未解决的漏洞 |
| 日志 Logging | 审核人决定如何结构化记录并用于评估 —— 人工覆盖决定是发现模型失败点的宝贵信号 |

**日志与数据处理 (logging &amp; data handling)**：
- 每请求记录：**唯一请求 ID (request ID)**、时间戳、输入类别/类型（含敏感信息时不记录完整输入）、输出或输出类型、延迟、错误码/失败信号、是否被人工覆盖。
- 完整用户数据、客户身份信息、含 **PII（个人可识别信息）** 的完整输入不得进通用日志；调试需要时从主数据存储在同样访问控制下读取，不在日志中无限期保留。
- **结构化日志 (structured logging)**：每条一致的 JSON 对象。部署前约定 **日志 schema**，确认客户会查询。

```json
{
  "request_id": "req_7f3a91",
  "timestamp": "2026-11-11T14:02:33Z",
  "input_category": "vendor_contract",
  "output_type": "deviation_report",
  "latency_ms": 2140,
  "error_code": null,
  "confidence": 0.62,
  "routed_to_human": true,
  "human_override": "approved_with_edits"
}
```

**移交后关系 (post-handoff relationship)**：
- **内部拥护者 (internal champion)**：客户方懂系统、能带新人、回答常规问题、判断何时需要外部帮助的人；在试点阶段识别和培养。没有 champion 的系统会依赖"谁能找到 FDE 的联系方式"。
- **支持窗口 (support window)**：FDE 可答疑多久、什么算范围内（构建期引入的 bug、对已文档化行为的困惑）、什么属于客户（新需求、客户自己改的基础设施、客户选择应用的模型更新）。未定义 = 无限期依赖。
- **干净退出 (clean exit)**：移交文档完整、监控激活、champion 就绪、支持窗口约定 → FDE 无未结技术义务。

<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="760" height="250" fill="#fff"/>
  <text x="380" y="22" font-size="15" text-anchor="middle" font-weight="bold">Human-in-the-Loop Fallback｜人在回路兜底</text>
  <g font-size="12" text-anchor="middle">
    <rect x="20" y="95" width="110" height="50" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="75" y="116">Request</text><text x="75" y="133">请求</text>
    <rect x="165" y="95" width="120" height="50" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="225" y="116">AI system</text><text x="225" y="133">AI 处理</text>
    <polygon points="380,80 450,120 380,160 310,120" fill="#fef7e0" stroke="#e37400"/><text x="380" y="116">Trigger?</text><text x="380" y="132">触发条件</text>
    <rect x="500" y="40" width="130" height="50" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="565" y="61">Auto output</text><text x="565" y="78">自动输出</text>
    <rect x="500" y="150" width="130" height="50" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="565" y="171">Review queue</text><text x="565" y="188">审核队列 + SLA</text>
    <rect x="655" y="150" width="90" height="50" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="700" y="171">Log decision</text><text x="700" y="188">记录决定</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="130" y1="120" x2="163" y2="120"/><line x1="285" y1="120" x2="308" y2="120"/>
    <line x1="430" y1="108" x2="498" y2="65"/><line x1="430" y1="132" x2="498" y2="175"/>
    <line x1="630" y1="175" x2="653" y2="175"/>
    <path d="M700 202 C700 240, 225 240, 225 147" stroke-dasharray="4,3"/>
  </g>
  <g font-size="11" fill="#444" text-anchor="middle">
    <text x="470" y="78">no</text><text x="470" y="170">yes</text>
    <text x="380" y="190">low confidence · flagged category · failure</text>
    <text x="460" y="236">override data feeds evaluation｜覆盖数据回流评估</text>
  </g>
</svg>

### 面试怎么说 / How to say it in the interview

**Q: When is an AI system ready to hand off? / 什么时候算可以移交？**
> "I agree five thresholds with the customer up front: reliability under peak load, output quality at real volume across all input types, safety — meaning any harmful output type has a human review step — cost within budget at full volume, and observability so their team can diagnose issues without me. Usability can improve after launch, but safety and observability have to meet the minimum before the system supports real decisions."
>
> 中文：五维阈值；安全与可观测性必须先达标。

**Q: How do you monitor an LLM system after launch?**
> "Beyond latency and error rate, I set up weekly random sampling of outputs reviewed against the agreed quality criteria, because quality drifts silently without any errors in the logs. I track cost per query — a spike in an agent often means it's looping on a tool — and the user override rate, which is usually the earliest sign of drift."
>
> 中文：延迟、错误率、每周抽样、每查询成本、覆盖率。

**Q: Design the human-in-the-loop path.**
> "Three parts. A trigger agreed before launch — confidence below a threshold, a flagged category like high-value transactions, or a technical failure. A queue with a named reviewer and a response-time SLA. And structured logging of every reviewer decision, because those overrides are the best evaluation signal we have about where the model fails."
>
> 中文：触发、队列（指定人 + 时限）、结构化记录覆盖决定。

**Q: What do you log, and what don't you log?**
> "Per request: a request ID, timestamp, input category, output type, latency, error codes, and whether a human overrode it — as structured JSON with a schema agreed before launch. I don't put full inputs with PII into general logs; if we need them for debugging, we pull them from the primary store under its own access controls."
>
> 中文：记录元数据结构化 JSON；不把含 PII 的完整输入写进通用日志。

---

## 8. The Field Feedback Loop｜现场反馈回路

Source: https://www.educative.io/courses/forward-deployed-engineer/the-field-feedback-loop

### 要点 / Key ideas

- 产品团队看不到客户环境：产品哪里不足、哪些集成总比预期久、客户反复问什么。FDE 足够近能看到这些模式，**结构化反馈回路 (structured feedback loop)** 把观察变成产品输入。
- **产品情报角色 (product intelligence role)**：FDE 技术够深能看懂客户系统内部，组织上够近能看到产品真实表现 —— 公司里无人有这种组合。基于工单和销售电话的路线图反映客户 **说** 想要什么；FDE 看到客户 **实际遇到** 什么（例：销售电话中的模糊抱怨，嵌入后发现是每个企业客户都要手工搭的缺失连接器 (missing connector)）。
- FDE 责任两部分：**为客户交付价值**（可见、被衡量）+ **把现场情报带回内部**（同等重要但容易被忽视）。

**现场笔记习惯 (field notes habit)** —— 项目中实时记录的结构化日志，非正式报告。记录什么：

| 类别 Category | 说明 Description |
|---|---|
| 产品缺口 Product gaps | 产品没解决、客户绕过或放弃的痛点 |
| 集成摩擦 Integration friction | 比预期久的集成模式及具体原因 |
| 文档缺口 Documentation gaps | 客户反复问、现有文档答不清的问题 |
| 意外失败模式 Unexpected failure modes | 真实使用中出现、评估计划里没有的失败 |
| 客户变通方案 Customer workarounds | 客户为弥补缺失能力自创的步骤 —— 往往比功能请求更清楚揭示未满足需求 |

- **何时记**：实时观察比事后回忆准确；调研会、sprint check-in、用户反馈后立即记一笔，胜过项目结束三周后的长文。
- **隐私 (privacy)**：不写具体客户名、机密业务细节、可识别客户的信息 —— 面向内部学习。
- **格式**：轻到能坚持 —— 共享文档、带日期条目、打类别标签（product gap / integration issue / documentation gap），可搜索、诚实。

**区分信号与噪声 (signal vs noise)**：
- 单项目的大多数观察是 **噪声 (noise)**：某客户特殊配置、某用户误解、不会再现的边界。把所有观察都当产品缺口会浪费产品团队注意力、损害 FDE 信誉。
- **信号 (signal)**：跨客户、行业、用例出现 —— 不同团队独立遇到同一集成问题；互不相识的客户问同一问题；不同行业团队独立搭了同一变通方案。
- **框定问题 (framing question)**：这是此客户特有，还是任何有这种配置的客户都会遇到？客户特殊内部数据结构 = 噪声；很多客户共有的某类企业工具缺标准连接器 = 信号。从"这个客户遇到什么"转为"这类客户一贯遇到什么"。
- **时间维度 (time dimension)**：有些信号第二、三次才显现；项目 3 像一次性的，到项目 5 是明确产品缺口。现场笔记让这种识别成为可能。
- **最强信号**：在 **至少两个不同客户情境** 中见过，且能具体描述共同点。

**有用的产品反馈六要素 (six elements of useful product feedback)**：

| 要素 Element | 说明 Description |
|---|---|
| 观察到的问题 Problem observed | 客户在其运营情境中遇到的具体情况 |
| 频率 Frequency | 发生多频繁、在多少客户中见过 |
| 严重度 Severity | 客户当时不得不做什么；独立搭建变通方案 = 高严重度 |
| 客户尝试过什么 What the customer tried | 到变通方案前的尝试 —— 揭示客户对产品的预期 |
| 什么能解决 What would solve it | 从客户视角描述修复的样子 |
| 预估影响 Estimated impact | 影响多少客户、解决能释放多少业务价值 |

**课程范例 (strong example)**：过去四个项目中三个，客户团队连接本地 (on-premises) 系统时找不到认证流程文档；三个团队都自己写了内部文档绕过。一份结构化的本地认证集成指南预计可为该客户群每个项目节省 2–3 天搭建时间。

- 以 **产品批评** 呈现 → 产品团队防御；以 **带业务影响和建议方向的数据点** 呈现 → 邀请协作。

**与内部团队合作 (working with internal teams)**：

| 团队 Team | 方法 Approach |
|---|---|
| 产品团队 Product team | FDE 不是产品团队的客户，而是 **信号源 (signal source)**；反馈是输入不是指令 (input, not instruction) |
| 工程升级 Engineering escalations | 包含：bug 清晰描述、**复现步骤 (reproduction steps)**、业务术语的客户影响、建议优先级及理由；无上下文的"紧急"请求会被降优先级 |
| 竞争优先级 Competing priorities | 判断哪些等下个版本、哪些客户侧绕过、哪些真需立即处理；升级太频繁会削弱真正重要的升级 |

**Challenge：识别模式并写反馈 (Identify pattern and write feedback)**
- English task: *Given three customer project logs mixing customer-specific observations and one shared gap, identify the strongest signal and write a product feedback entry using the six-element format.*
- 解法：先划掉每个日志里只属于该客户的项（特殊数据结构、单个用户误解），找出 **三个日志都出现** 的项（例如同一类连接器/认证流程缺失且三方都自建变通），然后按六要素写：问题、3/3 频率、严重度（都自建 workaround）、尝试过的方案、修复形态、预估节省天数与受影响客户群。

<svg viewBox="0 0 760 230" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="760" height="230" fill="#fff"/>
  <text x="380" y="22" font-size="15" text-anchor="middle" font-weight="bold">Field Feedback Loop｜现场反馈回路</text>
  <g font-size="12" text-anchor="middle">
    <rect x="20" y="50" width="150" height="56" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="95" y="73">Field notes</text><text x="95" y="91">实时现场笔记</text>
    <rect x="200" y="50" width="160" height="56" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="280" y="73">Signal vs noise</text><text x="280" y="91">≥2 distinct customers</text>
    <rect x="390" y="50" width="160" height="56" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="470" y="73">6-element feedback</text><text x="470" y="91">六要素反馈</text>
    <rect x="580" y="50" width="160" height="56" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="660" y="73">Product roadmap</text><text x="660" y="91">产品路线图</text>
    <rect x="290" y="150" width="180" height="50" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="380" y="171">Next engagement</text><text x="380" y="188">下一个项目更顺</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="170" y1="78" x2="198" y2="78"/><line x1="360" y1="78" x2="388" y2="78"/><line x1="550" y1="78" x2="578" y2="78"/>
    <path d="M660 108 L660 175 L472 175"/><path d="M288 175 L95 175 L95 108"/>
  </g>
</svg>

### 面试怎么说 / How to say it in the interview

**Q: How do you feed field learnings back to product? / 怎么把现场经验反馈给产品？**
> "I keep lightweight field notes during every engagement — dated, tagged as product gap, integration friction, doc gap, failure mode or workaround, with no customer-identifying details. I only escalate something as a product signal once I've seen it in at least two distinct customer contexts. Then I write it up with six elements: the problem, frequency, severity, what the customer tried, what would fix it, and estimated impact — framed as a data point with a business case, not a complaint."
>
> 中文：实时笔记；至少两个不同客户见过才算信号；六要素、以数据点而非批评呈现。

**Q: How do you escalate a customer-blocking bug to an engineering team mid-sprint?**
> "I give them a clear description, reproduction steps, the customer impact in business terms, and a suggested priority with my reasoning. I also say what I can work around on the customer side, so they can judge whether it really needs to break their sprint. I escalate sparingly so the ones I do raise get taken seriously."
>
> 中文：描述 + 复现 + 业务影响 + 建议优先级；说明客户侧可否绕过；少而精地升级。

---

## 9. The AI System Landscape｜AI 系统全景

Source: https://www.educative.io/courses/forward-deployed-engineer/the-ai-system-landscape

### 要点 / Key ideas

- FDE 推荐的系统类型决定之后的一切：非 agentic 系统构建周期短、评估标准收敛、移交快；agentic 系统引入协调复杂度、更大 **失败面 (failure surface)**、远超简单流水线的生产要求。**匹配系统类型与问题是 scoping 中最关键的决定之一。**
- 两大类：**基于 LLM 的非智能体系统 (LLM-based non-agentic systems)** 与 **智能体系统 (agentic systems)**。区别不在模型能力，而在 **运行时如何运作 (how the system operates at runtime)**。

| 维度 Dimension | 非智能体 LLM 系统 LLM-based non-agentic | 智能体系统 Agentic |
|---|---|---|
| 处理路径 Processing path | 固定：同类输入每次同一操作序列 | 不固定：步数和路径事先未定 |
| 自主行动 Autonomous actions | 无，不根据中途观察采取行动 | 决定下一步 → 执行 → 观察 → 纳入下次决策，循环至达成或放弃 |
| 典型用例 Use cases | 文档分类、信息抽取、摘要、结构化问答、内容生成（合同条款摘要、工单路由、检索问答） | 多步研究综合、自主流程执行、与外部 API/数据库交互完成任务、每步条件逻辑的文档处理 |
| FDE 视角 FDE implications | 快速 scope、评估标准直接、易移交；客户能把错误输出追溯到源头 | 更完整的评估框架、失败模式分析、移交须覆盖 **任务中途失败** 怎么办 |

- **什么是 agent**：感知环境、朝目标推理、选择并执行动作、观察结果、重复直到达成或放弃。决定性特征：**自主多步运作 (autonomous multi-step operation)** —— 根据观察自主决定下一步，无需人指挥每一步。
- Agentic 需要 scope：agent 能调哪些工具、工具调用失败怎么办、中间步骤返回模糊/不完整结果怎么办。非 agentic 都不需要。
- **常见误区**：用了 agent 框架就叫 agentic。是否 agentic 取决于是否跨步骤基于观察自主行动。划准这条线才能 scope 对系统、设定诚实预期。

**智能体系统两大结构组件 (two structural components)**：

1. **推理模型 (reasoning model)**：系统中心的 LLM，感知任务状态、决定下一步、在每个推理循环中产生驱动输出/指令。近年出现专为多步推理优化的 **推理模型 (reasoning models)**，输出前进行更审慎的逐步推理，适合规划、分解、条件逻辑。通用模型 (general-purpose model) vs 推理模型是由任务复杂度驱动的 scoping 决定。但模型选择本身不决定生产可靠性。
2. **驾驭工程 (harness engineering)**：设计包裹推理模型的运行环境的学科 —— 工具、记忆、跨步上下文、护栏、可观测性。同一模型在好/坏 harness 中生产表现差别巨大。模型产生 **看似合理的下一步 (plausible next actions)**；harness 决定动作是否安全、失败是否被捕获处理、成本是否受控、客户事后能否理解 agent 做了什么。**大多数企业部署的生产故障源于 harness 而非模型。**

**Harness 组件 (harness components)**：

| 组件 Component | 作用 Role |
|---|---|
| 工具 Tools | Agent 可调用的函数：API、数据库、搜索、代码执行、内部服务。scoping 时定义；工具越多，能力和失败面等比增加 |
| 记忆 Memory | **短期记忆 (short-term)** = 单会话活动上下文；**长期记忆 (long-term)** = 外部存储按需检索（向量库 (vector store)、结构化数据库） |
| 上下文管理 Context management | 每次调用包含什么、会话增长时如何排优先级、接近窗口上限时如何 **压缩 (compress)**；**上下文窗口溢出 (context window overflow)** 是试点要验证的常见故障 |
| 护栏 Guardrails | 能用哪些工具、能做哪些动作、能返回哪些输出、每会话成本/token 上限；**构建前的设计决定，不是事故后的补丁** |
| 可观测性 Observability | 记录每个动作、工具调用、决策点、成本的日志与追踪层；没有它客户团队在 FDE 离开后无法诊断 |
| AI 审核回路 AI review loops | 输出与交付之间的评估步骤：**自我反思 (self-reflection)** 或独立 **评审模型 (critic model)**；不通过则重新生成，超过重试上限转人工 |
| 编排 Orchestration | 多 agent 时的协调层：顺序、并行、循环、中心协调者 (central coordinator)；每个 agent 保留自己的 harness，编排决定如何连接、传递状态、跨边界处理失败 |

- 客户展示内部自建 agent 时，有效问题都关于 harness：能调哪些工具、长会话上下文怎么管、工具调用失败怎么办、哪里能看到 agent 做了什么的记录。**没有可观测 harness 的系统，客户无法安全拥有。**

<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="760" height="330" fill="#fff"/>
  <text x="380" y="22" font-size="15" text-anchor="middle" font-weight="bold">Agentic System = Reasoning Model + Harness｜推理模型 + 驾驭层</text>
  <rect x="210" y="45" width="340" height="270" rx="14" fill="#f8f9fa" stroke="#5f6368" stroke-dasharray="6,4"/>
  <text x="380" y="64" font-size="12" text-anchor="middle" fill="#5f6368">Harness｜驾驭层</text>
  <circle cx="380" cy="180" r="62" fill="#e8f0fe" stroke="#3367d6" stroke-width="2"/>
  <text x="380" y="168" font-size="13" text-anchor="middle" font-weight="bold">Reasoning model</text>
  <text x="380" y="186" font-size="12" text-anchor="middle">推理模型</text>
  <text x="380" y="204" font-size="10" text-anchor="middle">plan → act → observe</text>
  <g font-size="11" text-anchor="middle">
    <rect x="230" y="78" width="95" height="34" rx="6" fill="#fff" stroke="#3367d6"/><text x="277" y="99">Tools 工具</text>
    <rect x="435" y="78" width="95" height="34" rx="6" fill="#fff" stroke="#3367d6"/><text x="482" y="99">Memory 记忆</text>
    <rect x="222" y="163" width="80" height="34" rx="6" fill="#fff" stroke="#3367d6"/><text x="262" y="184">Context 上下文</text>
    <rect x="458" y="163" width="80" height="34" rx="6" fill="#fff" stroke="#c5221f"/><text x="498" y="184">Guardrails 护栏</text>
    <rect x="230" y="255" width="95" height="34" rx="6" fill="#fff" stroke="#137333"/><text x="277" y="276">Observability</text>
    <rect x="435" y="255" width="95" height="34" rx="6" fill="#fff" stroke="#e37400"/><text x="482" y="276">Review loop 审核</text>
  </g>
  <rect x="580" y="140" width="165" height="80" rx="10" fill="#fef7e0" stroke="#e37400"/>
  <text x="662" y="168" font-size="12" text-anchor="middle" font-weight="bold">Orchestration</text>
  <text x="662" y="186" font-size="11" text-anchor="middle">编排 (multi-agent)</text>
  <text x="662" y="204" font-size="10" text-anchor="middle">each agent keeps its harness</text>
  <rect x="20" y="140" width="165" height="80" rx="10" fill="#e6f4ea" stroke="#137333"/>
  <text x="102" y="168" font-size="12" text-anchor="middle" font-weight="bold">External systems</text>
  <text x="102" y="186" font-size="11" text-anchor="middle">APIs · DBs · search</text>
  <text x="102" y="204" font-size="10" text-anchor="middle">外部系统</text>
  <line x1="185" y1="180" x2="220" y2="180" stroke="#555" stroke-width="1.5"/>
  <line x1="550" y1="180" x2="578" y2="180" stroke="#555" stroke-width="1.5"/>
</svg>

### 面试怎么说 / How to say it in the interview

**Q: What makes a system agentic? / 什么才算 agentic？**
> "It's about runtime behavior, not the framework. A system is agentic if it decides its own next action based on what it observes, across multiple steps, without a human directing each one. A fixed pipeline built with an agent framework is still a pipeline. I draw that line during scoping because agentic systems need tool failure handling, a broader eval framework, and a handoff that covers partial failures."
>
> 中文：看运行时是否基于观察自主多步决策，而非用了什么框架。

**Q: What is harness engineering and why does it matter?**
> "The harness is everything around the model — tools, memory, context management, guardrails, observability, review loops, and orchestration. The model proposes plausible next actions; the harness decides whether they're safe, catches failed tool calls, caps cost, and records what happened. In my experience most production agent failures are harness failures, not model failures."
>
> 中文：harness = 模型外的一切；大部分生产故障在 harness。

**Q: A customer shows you an agent they built. What do you ask?**
> "I ask about the harness: which tools can it call and with what permissions, how is context managed in long sessions, what happens when a tool call fails or returns something ambiguous, and where can I see a trace of what it did. If there's no observable record of its actions, the customer can't safely own it."
>
> 中文：问工具权限、上下文管理、工具失败处理、可追踪记录。

---

## 10. LLM-Based Systems｜基于 LLM 的系统

Source: https://www.educative.io/courses/forward-deployed-engineer/llm-based-systems

### 要点 / Key ideas

- LLM-based 系统是企业 AI 部署的支柱；很多最高价值工作流不需要多步推理、工具编排或自主行动。范围合理的 LLM 系统比复杂方案更快交付价值、运营负担更小。

**四种模式 (four patterns)** —— 各有不同输入、输出、评估方式，评估设计在 scoping 时完成：

| 模式 Pattern | 例子 Example | 评估 Evaluation |
|---|---|---|
| 分类 Classification | 工单路由到对应团队 | scoping 定义类别 schema 与 **标注测试集 (labeled test set)**；精确率/召回率 |
| 抽取 Extraction | 合同中抽取当事方、生效日、付款条款 | 用客户真实文档构建 **金标准集 (gold-standard set)** |
| 摘要与综合 Summarization &amp; synthesis | 长报告→高管简报；多文档汇总 | 事先定义覆盖要求 (coverage)、事实准确阈值、输出格式标准 |
| 问答与生成 Question answering &amp; generation | 员工政策问答、基于产品信息起草邮件 | 事实准确 + 格式标准；是否加人工审核是 scoping 决定 |

分类和抽取易于干净衡量；摘要和生成需要更审慎地预先定义"好输出"。

**RAG（检索增强生成 retrieval-augmented generation）**：
- 生成前加检索层：文档预先 **分块 (chunked)**、**嵌入 (embedded)**、索引到 **向量库 (vector store)**；查询到来时按语义相似度取最相关块，组装上下文与查询一起给模型。
- **何时用 RAG**：知识库太大放不进单个上下文窗口；更新频繁需反映最新信息；输出必须 **可溯源 (trace back to source)**（法律、合规、审计）；客户已有结构化文档库可直连。
- **先查检索质量 (retrieval quality first)**：好模型 + 差检索 = 差答案。POC 中先验证真实查询取到了对的文档，再归咎模型。

| RAG 评估重点 Area | 关注 What to check |
|---|---|
| 分块策略 Chunking strategy | 分块不当 → 相关信息被拆到不会一起被检索的块里；scoping 时问、POC 用真实查询验证 |
| 数据新鲜度 Data freshness | 知识库多久更新；索引陈旧对时效性查询的影响 |
| 上下文窗口适配 Context window fit | 最复杂查询的检索结果是否放得下；溢出是只在真实负载下出现的 **静默故障 (silent failure)** |
| 摄取流水线所有权 Ingestion pipeline ownership | 谁负责加新文档、什么触发 **重建索引 (re-index)**；FDE 离开后无人负责 → 系统随知识库增长静默退化 |

**微调 (fine-tuning)**：
- 在领域标注数据上更新预训练模型 (pretrained model) 权重 (weights)，使其在目标任务上优于通用模型 (general-purpose model)。RAG 让系统在查询时访问领域内容；微调改变模型 **行为**（一致的专门输出结构、对特定输入的可靠表现）。
- **何时用**：基座模型 (foundation model) 在领域输入/输出格式上持续表现不佳且 **提示工程 (prompt engineering)** 无法弥补；任务需要通用模型无法稳定维持的输出结构；预计量下 token 成本和延迟使更精简模型比长 system prompt 更实际。

| 方法 Approach | 说明 Description |
|---|---|
| 全量微调 Full fine-tuning | 更新全部权重；适配度最高但算力 (compute)、存储、数据量需求大；企业多数避免 |
| PEFT（参数高效微调 parameter-efficient fine-tuning） | 只更新少量参数；企业微调主流 |
| ↳ LoRA（低秩适配 low-rank adaptation） | 在层中插入小的可训练矩阵，以很小成本接近全量微调质量 |
| ↳ QLoRA（量化 LoRA quantized LoRA） | 对 **量化模型 (quantized model)** 应用 LoRA，进一步降内存，可在小硬件上微调 |

- FDE 不必亲自跑微调，但要懂客户用哪种方法，以 scope 时间线、数据需求、移交后维护负担。
- **仅当 POC 证据显示基座模型无法弥合差距时才 scope 微调**。它增加构建复杂度和客户维护负担：**数据集策展 (dataset curation)**、**重训触发条件 (retraining triggers)**、**模型版本管理 (model version management)**。移交文档要覆盖数据集所有权、评估节奏、领域变化时如何更新模型。

**何时推荐 LLM-based 系统（五信号）**：
1. 单次或少量模型调用即产生有意义输出，无需中途自主行动。
2. 输入类型一致明确，评估标准易事先定义。
3. 无需与外部服务交互或跨多步协调。
4. 客户团队需要不必推理多步执行、工具协调、会话状态就能调试维护的系统。
5. 延迟或成本受限：同类问题 LLM 系统比 agentic 更快更便宜。

- **企业 AI 最常见的 scoping 错误：为 LLM 系统就能可靠解决的问题推荐 agentic 系统。** 从最简单能解决问题的架构开始，只在用例明确需要时加复杂度。

| 信号 Signal | LLM 系统 LLM-based | 智能体 Agentic |
|---|---|---|
| 输出类型 Output type | 单步输出 Single-step | 多步输出 Multi-step |
| 外部交互 External interactions | 无需工具调用 No tool calls | 需要工具调用 Tool calls required |
| 延迟特征 Latency profile | 低且可预测 Low &amp; predictable | 可变 Variable |
| 维护复杂度 Maintenance complexity | 直接 Straightforward | 需要可观测性 Observability required |

<svg viewBox="0 0 760 210" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="760" height="210" fill="#fff"/>
  <text x="380" y="22" font-size="15" text-anchor="middle" font-weight="bold">RAG Pipeline｜检索增强生成流水线</text>
  <text x="20" y="50" font-size="12" fill="#5f6368">Offline ingestion｜离线摄取</text>
  <g font-size="12" text-anchor="middle">
    <rect x="20" y="60" width="110" height="44" rx="6" fill="#f1f3f4" stroke="#5f6368"/><text x="75" y="87">Documents 文档</text>
    <rect x="160" y="60" width="110" height="44" rx="6" fill="#fef7e0" stroke="#e37400"/><text x="215" y="87">Chunk 分块</text>
    <rect x="300" y="60" width="110" height="44" rx="6" fill="#fef7e0" stroke="#e37400"/><text x="355" y="87">Embed 嵌入</text>
    <rect x="440" y="60" width="130" height="44" rx="6" fill="#e8f0fe" stroke="#3367d6"/><text x="505" y="87">Vector store 向量库</text>
  </g>
  <text x="20" y="135" font-size="12" fill="#5f6368">Online query｜在线查询</text>
  <g font-size="12" text-anchor="middle">
    <rect x="20" y="145" width="110" height="44" rx="6" fill="#f1f3f4" stroke="#5f6368"/><text x="75" y="172">Query 查询</text>
    <rect x="300" y="145" width="110" height="44" rx="6" fill="#e8f0fe" stroke="#3367d6"/><text x="355" y="172">Top-k chunks</text>
    <rect x="440" y="145" width="130" height="44" rx="6" fill="#e6f4ea" stroke="#137333"/><text x="505" y="172">LLM + context</text>
    <rect x="600" y="145" width="140" height="44" rx="6" fill="#e6f4ea" stroke="#137333"/><text x="670" y="166">Answer + sources</text><text x="670" y="182">答案 + 来源</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="130" y1="82" x2="158" y2="82"/><line x1="270" y1="82" x2="298" y2="82"/><line x1="410" y1="82" x2="438" y2="82"/>
    <line x1="130" y1="167" x2="298" y2="167"/><line x1="505" y1="104" x2="380" y2="143"/>
    <line x1="410" y1="167" x2="438" y2="167"/><line x1="570" y1="167" x2="598" y2="167"/>
  </g>
  <text x="215" y="160" font-size="10" fill="#444" text-anchor="middle">semantic search 语义检索</text>
</svg>

### 面试怎么说 / How to say it in the interview

**Q: RAG or fine-tuning? / RAG 还是微调？**
> "RAG gives the model access to knowledge at query time; fine-tuning changes how the model behaves. If the problem is a large or frequently updated knowledge base, or answers must cite sources for audit, I use RAG. I only scope fine-tuning when the POC shows the base model can't close a gap with prompting — like a strict output format or dense domain jargon — and even then I'd usually go with LoRA, and make sure the customer owns dataset curation, retraining triggers and model versioning after I leave."
>
> 中文：RAG 管知识、微调管行为；只有 POC 证明提示不够才微调，并移交数据与重训责任。

**Q: The RAG system is giving bad answers. How do you debug?**
> "I check retrieval before I blame the model. For a set of real queries I look at whether the right chunks come back at all. If not, it's usually chunking — related content split across chunks — or a stale index because nobody owns re-ingestion. Then I check whether the retrieved context actually fits the window for the hardest queries, because overflow fails silently."
>
> 中文：先查检索；常见是分块、索引陈旧、上下文溢出。

**Q: When would you not build an agent?**
> "When a single model call or a short fixed pipeline produces the output, inputs are well-defined, there's no need to call external systems mid-task, and the customer's team needs something they can debug easily. Recommending an agent for a problem an LLM pipeline solves is the most common scoping mistake I see — it costs more, has variable latency, and is harder to hand off."
>
> 中文：单次调用可解、输入明确、无需外部交互、团队需易调试时不做 agent。

---

## 11. Harness Engineering: Tools, Memory, and Context｜驾驭工程：工具、记忆与上下文

Source: https://www.educative.io/courses/forward-deployed-engineer/harness-engineering-tools-memory-and-context

### 要点 / Key ideas

- Agentic 系统 = 在工程化环境中运行的推理模型。模型做决定；harness 提供 **行动的工具、向前携带信息的记忆、每步准确推理的上下文**。两者不可分：模型决定做什么，harness 决定能否安全可靠地执行。
- 只关注模型选择、把 harness 当事后补充 → 演示可行、生产失败。Agentic 生产故障几乎都可追溯到 **定义不足、配置错误或缺失** 的 harness 组件。

**推理循环 (reasoning loop)** —— 每次迭代四阶段：

| 阶段 Phase | 说明 Description |
|---|---|
| 感知 Perceive | 接收任务当前状态：已知什么、工具返回了什么、环境新输入、还要完成什么 |
| 推理 Reason | 模型处理状态、决定下一步 —— 模型的贡献点 |
| 行动 Act | 执行所选动作：调工具、检索信息、生成输出 |
| 观察 Observe | 接收结果并更新对任务的认识 |

循环直到：达成目标、命中 **定义的停止条件 (stopping condition)**、或遇到无法自行解决的错误。Harness 管理 agent 每步感知什么、执行模型选择的动作、跨会话保留信息、处理动作失败。
- **Scoping 时问循环边界**：什么让它停？某步失败怎么办？现实任务需要多少次迭代？这些答案揭示系统是为可预测行为设计，还是留下没人规划过的失败模式。

**工具 (tools)** —— 每次调用流程：① 模型选择工具并生成 **参数 (arguments)** → ② harness 执行函数、从外部系统拿结果 → ③ 结果作为下一步推理的新输入。

| 工具类别 Tool category | 例子 Examples | 风险 Risk |
|---|---|---|
| 读工具 Read tools | 查数据库、知识库、文档库、外部 API | 最低 —— 不修改外部状态 |
| 写工具 Write tools | 更新记录、POST API、发通知、触发流程步骤 | 影响外部系统，可能 **不可逆 (irreversible)**，需人工介入修复 |
| 执行工具 Execution tools | 跑脚本、调用计算环境、启动长时间进程 | 最高 —— 副作用可超出 agent 会话 |

- 复杂任务在一个会话中协调多工具：前一个输出作为下一个输入；独立子任务可 **并行 (parallel)**，agent 汇总后继续。
- **最小工具集 (minimum tool set)** 是有意的设计决定；更新生产记录的写工具引入只读工具没有的风险，这个权衡写进 scope。

**记忆 (memory)**：

| 层级 Level | 说明 Description | 实现 Implementation |
|---|---|---|
| 短期记忆 Short-term memory | 单会话的活动上下文窗口：原始目标、之前工具结果、早期观察、任务运行状态；每步直接可用，受窗口大小限制 | Context window |
| 长期记忆 Long-term memory | 跨会话读写的持久存储：回忆之前交互、检索积累知识、从中断处恢复多会话任务 | 向量库 (vector store) 语义检索；结构化数据库精确查找 |

- **记忆架构是 scoping 决定 (memory architecture is a scoping decision)**：调研时看似自包含的用例，真实用户使用后常暴露 **跨会话需求 (cross-session requirements)**（如协助客户账户的 agent 需要回忆上周对话）。试点才发现 = 在时间压力下重构架构。Scoping 时就问 **会话连续性 (session continuity)** 需求。

**上下文管理 (context management)** —— 每步 harness 为模型组装上下文：目标、之前观察、工具结果、检索文档等，组装质量直接决定推理质量。窗口有固定上限，会话推进时工具结果、观察、检索文档不断累积，harness 必须决定全量包含、压缩/摘要、还是丢弃。

| 方法 Approach | 说明 Description |
|---|---|
| 步骤摘要 Step summarization | 窗口填满前把早期步骤压缩成摘要，保留关键结果 |
| 选择性检索 Selective retrieval | 工具结果和文档外部存储，只在与当前步相关时取回，而不是之后每次都带 |
| 运行状态 Running state | 维护每步更新的结构化任务进度摘要，替代逐字携带完整历史 |

- **上下文窗口溢出 (context window overflow)**：窗口满时内容被丢弃，模型 **不会明确提示**；agent 基于不完整图景继续推理，输出看似合理但错误。
- 试点中用 **与真实生产匹配的会话长度和输入量** 验证上下文行为；短演示正确的系统在长会话、工具调用累积时会静默退化。
- 循环、工具、记忆、上下文不是独立层：精简工具集减少上下文噪声；准确上下文让模型基于完整信息推理；记忆架构决定能否应对真实会话长度与数据量。一起 scope、一起验证。

```python
# Minimal agent loop with harness-enforced boundaries (illustrative)
MAX_STEPS = 12
TOKEN_BUDGET = 60_000

def run_agent(goal, model, tools, state_store):
    running_state = {"goal": goal, "done": [], "open_questions": []}
    tokens_used = 0
    for step in range(MAX_STEPS):
        context = build_context(running_state, state_store)   # perceive
        decision = model.decide(context, tools.schemas())      # reason
        tokens_used += decision.tokens
        if tokens_used > TOKEN_BUDGET:
            return escalate("token_budget_exceeded", running_state)
        if decision.is_final:
            return decision.output
        try:
            result = tools.call(decision.tool, decision.args)  # act
        except ToolError as err:
            result = {"error": str(err)}
        running_state = update_state(running_state, decision, result)  # observe
    return escalate("max_steps_reached", running_state)
```

上面代码说明：harness（而非模型）负责停止条件（最大步数、token 预算）、工具失败捕获、以及用 `running_state` 替代完整历史以防上下文溢出。

<svg viewBox="0 0 760 270" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="760" height="270" fill="#fff"/>
  <text x="380" y="22" font-size="15" text-anchor="middle" font-weight="bold">Reasoning Loop｜推理循环</text>
  <g font-size="13" text-anchor="middle">
    <rect x="300" y="40" width="160" height="50" rx="25" fill="#e8f0fe" stroke="#3367d6"/><text x="380" y="62">Perceive</text><text x="380" y="80" font-size="11">感知状态</text>
    <rect x="530" y="110" width="160" height="50" rx="25" fill="#fef7e0" stroke="#e37400"/><text x="610" y="132">Reason</text><text x="610" y="150" font-size="11">模型决策</text>
    <rect x="300" y="185" width="160" height="50" rx="25" fill="#e6f4ea" stroke="#137333"/><text x="380" y="207">Act</text><text x="380" y="225" font-size="11">调用工具</text>
    <rect x="70" y="110" width="160" height="50" rx="25" fill="#fce8e6" stroke="#c5221f"/><text x="150" y="132">Observe</text><text x="150" y="150" font-size="11">观察结果</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <path d="M460 70 Q560 75 600 108"/><path d="M600 162 Q560 205 462 210"/>
    <path d="M298 210 Q190 205 160 162"/><path d="M160 108 Q190 75 298 68"/>
  </g>
  <g font-size="11" fill="#444" text-anchor="middle">
    <text x="380" y="125">stop when: goal met · max steps ·</text>
    <text x="380" y="141">budget hit · unrecoverable error</text>
    <text x="380" y="157">停止：达成 / 步数上限 / 预算 / 不可恢复错误</text>
    <text x="380" y="258">Harness: tools · memory · context · failure handling｜驾驭层负责执行与容错</text>
  </g>
</svg>

### 面试怎么说 / How to say it in the interview

**Q: Walk me through how an agent actually runs. / agent 实际怎么运行？**
> "Each iteration is perceive, reason, act, observe. The harness assembles the current state, the model picks the next action and its arguments, the harness executes the tool and feeds the result back, and it repeats until the goal is met or a stop condition fires — max steps, a token budget, or an error it can't resolve. During scoping I always ask what stops the loop and what happens when a step fails."
>
> 中文：感知-推理-行动-观察；harness 组装状态和执行工具；必须定义停止条件。

**Q: How do you decide what tools to give an agent?**
> "I scope the minimum tool set that solves the problem, and I classify each tool by risk: read tools are low risk, write tools can be irreversible, execution tools have side effects beyond the session. If the use case only needs to look things up, I don't give it a write tool. Any write tool goes into the scope document with its blast radius and how we'd recover from a bad call."
>
> 中文：最小工具集，按读/写/执行分级风险，写工具要写明影响与恢复。

**Q: How do you handle long agent sessions that overflow context?**
> "Overflow is dangerous because nothing errors — content just drops and the agent keeps reasoning from an incomplete picture. I use a structured running state instead of verbatim history, summarize older steps before the window fills, and keep tool outputs in external storage that I retrieve only when relevant. Then I validate it in the pilot with session lengths that match real usage, not demo-length sessions."
>
> 中文：溢出静默；用运行状态、步骤摘要、选择性检索；用真实会话长度验证。

**Q: Short-term vs long-term memory — when do you need the latter?**
> "If the task is self-contained in a session, the context window is enough. If the agent needs to recall a conversation from last week, accumulate findings over time, or resume a multi-session task, long-term memory is a functional requirement — usually a vector store or a structured DB. I ask about session continuity in discovery because finding it in the pilot means re-architecting under time pressure."
>
> 中文：跨会话回忆/积累/恢复才需长期记忆；调研阶段就问。

---

## 12. Harness Engineering: Guardrails, Observability, and Review｜驾驭工程：护栏、可观测性与审核

Source: https://www.educative.io/courses/forward-deployed-engineer/harness-engineering-guardrails-observability-and-review

### 要点 / Key ideas

- 工具、记忆、上下文让循环 **能运行**；**能运行 ≠ 在真实条件下安全可靠运行**。护栏、可观测性、AI 审核回路是 harness 组件（约束、记录、评估行为）；**人工升级 (human escalation)** 是与系统一同设计的运营流程，位于 harness 之外，但属同一 scoping 与移交工作。
- 缺失时系统难以拥有：行为难预测、故障难追踪、客户团队出事时没有可靠干预路径。

**护栏 (guardrails)** —— 运行时允许 agent 做什么，构建前确立安全边界。没有显式约束时，唯一限制是模型每步的判断 —— 在生产规模下不是可靠安全机制。

| 护栏类型 Guardrail type | 作用 Purpose | 防止的失败 Prevents |
|---|---|---|
| 范围限制 Scope limits | 允许调用哪些工具和动作 | 研究型 agent 调用了本不该访问的写工具 |
| 预算上限 Budget ceilings | 每会话/每日 token 与成本上限 | 一个 **失控会话 (runaway session)** 耗掉一个月 API 预算 |
| 输出过滤 Output filters | 输出到达用户前校验内容和格式 | PII (personally identifiable information) 或 **幻觉内容 (hallucinated content)** 直接出现在用户响应中；强制格式、剥离禁止内容、标记超风险阈值输出 |
| 权限控制 Permission controls | agent 能读写哪些数据 | agent 能访问远超任务需要的敏感记录；按 **最小权限 (least privilege)** 限制 |

- 护栏配置是 **scoping 产物 (scoping artifact)**，不是构建后清单：写入 scope → 试点中用边界输入验证 → 写进移交文档并说明客户团队如何随系统演进调整。

**可观测性与追踪 (observability &amp; tracing)**：
- 多步系统的错误输出往往 **不起源于它出现的那一步**，而是几步之前：工具返回意外结果、上下文组装错误、模型基于不完整信息推理。没有 trace 找不到起源点。
- **执行追踪 (execution tracing)**：按顺序记录会话每步 —— 模型收到什么、决定什么、调了什么工具、工具返回什么。

| 六个日志维度 Six logging dimensions | 说明 |
|---|---|
| 工具调用与结果 Tool calls &amp; results | 含错误响应和重试 |
| 模型输入输出 Model inputs &amp; outputs | 每个推理步 |
| 记忆读写 Memory reads &amp; writes | 从长期存储取了什么、写回了什么 |
| Token 用量与成本 Token usage &amp; cost | 每步、每会话 |
| 错误状态 Error states | 超时事件及随后的重试行为 |
| 置信度 Confidence scores | 决策点处系统给出时 |

- **诊断测试 (diagnostic test)**：如果这个 agent 下周产出错误输出，客户团队能否准确重建发生了什么？不能 → harness 未就绪。试点结束前确认 trace 可读且客户能解读。

**AI 审核回路 (AI review loops)**：输出 → 审核步骤按标准检查 → 通过则交付；不通过则带审核反馈重新生成；超过重试次数 → 人工审核。

| 形式 Form | 说明 Description |
|---|---|
| 自我反思 Self-reflection | 提示 agent 在返回前评估自己输出：是否 **有据 (grounded)** 于检索文档、格式是否合规、必需步骤是否完成 |
| 评审模型 Critic model | 独立模型实例或专用 critic prompt 独立评估：接受 / 带具体反馈打回 / 转人工 |

- **适用**：输出质量在 **可验证维度**（格式合规、事实依据、约束满足）上关键，而每步人工审核延迟不可接受。
- 增加每输出的 token 成本与延迟 → 写入 scope 前估算预计量下的成本。审核标准必须 **精确定义**（模糊标准 → 不可靠审核）。试点配置时设 **重试上限 (retry limit)**。
- 审核回路 **减少** 需人工的案例量，**不消除** 人工监督。

**人工升级 (human escalation)**：
- **置信度阈值 (confidence thresholds)**：低于阈值时 agent 不继续，转人工。阈值在试点中按真实输入的输出分布 **校准 (calibrate)**：太高 → 审核负担大；太低 → 系统在不该自主的案例上行动。

| 升级路径四要素 Four components | 说明 Description |
|---|---|
| 谁接收 Who receives it | 指定角色或团队，不能是没有具体负责人的泛指 |
| 附带什么 What accompanies it | 原始输入、该会话的推理 trace、触发升级的置信度或审核失败原因 |
| 如何记录决定 How the decision is recorded | 记录审核人回应；升级案例模式用于校准阈值、发现反复出现的失败 |
| 等待时 agent 做什么 What the agent does while waiting | 暂停并保持任务打开 / 回退默认输出 / 转入现有手工流程 —— 取决于流程能否容忍延迟 |

- 客户能拥有的系统：护栏有文档、可观测层产出可读 trace、升级路径经过测试并被理解。缺任一组件的 harness **不会显眼地失败**，而是在项目结束后某个不可预测的时间点 **静默失败**，且没人有能力诊断。
- 护栏、可观测性、审核回路、升级路径不是加在可用系统上的功能，而是让系统 **可拥有而非脆弱 (ownable rather than fragile)** 的东西。

<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="760" height="250" fill="#fff"/>
  <text x="380" y="22" font-size="15" text-anchor="middle" font-weight="bold">AI Review Loop → Human Escalation｜AI 审核回路与人工升级</text>
  <g font-size="12" text-anchor="middle">
    <rect x="20" y="90" width="120" height="50" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="80" y="111">Agent output</text><text x="80" y="128">agent 输出</text>
    <polygon points="250,70 320,115 250,160 180,115" fill="#fef7e0" stroke="#e37400"/><text x="250" y="111">Review</text><text x="250" y="127">self / critic</text>
    <rect x="380" y="40" width="130" height="44" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="445" y="67">Deliver 交付</text>
    <rect x="380" y="140" width="130" height="44" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="445" y="160">Regenerate</text><text x="445" y="176">重新生成</text>
    <polygon points="610,120 670,162 610,204 550,162" fill="#fce8e6" stroke="#c5221f"/><text x="610" y="159">retries</text><text x="610" y="174">&gt; limit?</text>
    <rect x="620" y="40" width="125" height="50" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="682" y="61">Human queue</text><text x="682" y="78">人工 + trace</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="140" y1="115" x2="178" y2="115"/>
    <line x1="300" y1="100" x2="378" y2="62"/><line x1="300" y1="130" x2="378" y2="160"/>
    <line x1="510" y1="162" x2="548" y2="162"/>
    <line x1="640" y1="142" x2="672" y2="92"/>
    <path d="M580 185 C520 240, 100 240, 80 142" stroke-dasharray="4,3"/>
  </g>
  <g font-size="11" fill="#444" text-anchor="middle">
    <text x="345" y="72">pass</text><text x="345" y="152">fail</text>
    <text x="680" y="120">yes</text><text x="330" y="232">no → back to agent with feedback｜未超限，带反馈重试</text>
  </g>
</svg>

### 面试怎么说 / How to say it in the interview

**Q: What guardrails would you put on a production agent? / 生产 agent 你会加哪些护栏？**
> "Four types. Scope limits on which tools and actions it can call, so a research agent can't hit a write tool. Budget ceilings per session and per day, so one runaway loop can't burn a month's spend. Output filters to catch PII, hallucinated content, and format violations before the user sees anything. And permission controls so it only reads and writes the data this workflow needs. I define them in the scope doc, test them with edge cases in the pilot, and document how the customer adjusts them."
>
> 中文：范围、预算、输出过滤、权限四类；scope 定义、试点验证、文档说明调整方式。

**Q: How do you make an agent debuggable after you leave?**
> "Execution tracing at every step: model input and output, tool calls with results and retries, memory reads and writes, tokens and cost, errors and timeouts, and confidence scores. In a multi-step system the wrong answer usually originates a few steps before it shows up, so you need the whole sequence. My bar before closing the pilot is: if this produces a wrong output next week, can their team reconstruct exactly what happened without me?"
>
> 中文：六维 trace；"下周出错客户能否独立重建"是交接标准。

**Q: When would you use a critic model?**
> "When quality matters on dimensions I can verify — grounding in retrieved documents, format compliance, constraint satisfaction — and putting a human on every output would be too slow. I define the criteria precisely, set a retry limit, and route anything that still fails to a human queue. I also cost it out at projected volume, because a critic roughly adds another model call per output."
>
> 中文：可验证维度 + 人工太慢时用；精确标准、重试上限、超限转人工、先算成本。

**Q: How do you set the confidence threshold for escalation?**
> "I calibrate it in the pilot against the real output distribution. Too high and reviewers drown; too low and the system acts on cases it shouldn't. The escalation itself needs a named owner, the input plus reasoning trace and the reason it escalated, a logged decision, and a defined behavior while waiting — pause, safe default, or the existing manual process."
>
> 中文：试点中按真实分布校准；升级需指定人、完整上下文、记录决定、等待行为。

---

## 13. Multi-Agent Orchestration Patterns｜多智能体编排模式

Source: https://www.educative.io/courses/forward-deployed-engineer/multi-agent-orchestration-patterns

### 要点 / Key ideas

- 多智能体系统把工作分给多个协调的 agent。每个 agent **保留自己的推理模型和 harness**（工具、记忆、上下文管理、护栏），变化的是上层 **协调层 (coordination layer)**，带来新问题：上下文和状态如何在 agent 间流动、一个 agent 失败如何影响其他、整体如何观测和调试。
- **多 agent 不是自动正确的推荐**；仅当用例确实值得协调成本时才提。

**何时用多 agent（满足其一）**：
1. 任务可拆为能 **独立运行** 的子任务，并行显著缩短完成时间。
2. 不同子任务需要 **不同工具集或专门能力**，单 agent 无法高效承载。
3. 所需总上下文即使压缩后也 **超出单 agent 窗口**。

都不满足 → 单 agent + 好 harness 成本更低、调试更简单、移交更容易。多 agent 增加协调复杂度、**成倍增加 token 消耗**、故障更难追踪。推荐前估算预计量下成本与延迟，并在 scoping 时诚实呈现权衡。

**五种编排结构 (orchestration patterns + handoff)**：

| 模式 Pattern | 结构 Structure | 适用 Fits | 关键风险/要求 Key risk / requirement |
|---|---|---|---|
| 顺序 Sequential | 固定流水线，前一个输出传给下一个 | 每步转换上一步输出：研究→分析→起草 | 最易调试，故障定位到某一步 |
| 并行 Parallel | 多 agent 同时处理独立子任务，结果 **聚合 (aggregate)** | 多文档同时处理、多数据源同时研究、大批量评估 | 降低墙钟时间 (wall-clock time) 但 token 按 agent 数成倍；聚合逻辑须优雅处理 **部分失败 (partial failures)**，一个失败不应丢弃全部结果 |
| 循环 Loop | 反复运行直到退出条件：质量达标、最大迭代、审核标记完成 | 迭代精炼（生成-评估-修改）、研究循环（搜索-评估完整性-再搜）、重试 | **退出条件必须精确**；scoping 时设最大迭代数 + token 预算上限，试点用 **对抗性输入 (adversarial inputs)** 验证 |
| 层级 Hierarchical | **编排者 (orchestrator)** 规划协调，**子 agent (subagents)** 执行；子 agent 之间不直接通信；可多层 | 子任务有顺序依赖、规划与执行分离、需要中心状态管理 | **大多数多 agent 故障源于编排者**；试点评估它如何处理子 agent 错误、重试、部分结果 |
| 交接 Agent handoff | 一个 agent 把控制权转给另一个，前者停止；无中心编排者 | 不同阶段需不同能力：客户接入 agent → 技术解决 agent；研究 agent → 结构化分析 agent | 传递的是累积任务上下文（原始目标、已完成内容、相关记忆、约束）；**交接点上下文校验 (context validation)** 是设计要求：故障显现在第二个 agent、起源在第一个；scoping 时定义合法 **交接载荷 (handoff payload)** |

**协调与可靠性四挑战 (coordination &amp; reliability)**：

| 挑战 Challenge | 说明 Description |
|---|---|
| 状态管理 State management | 什么上下文在 agent 间传递、接收方行动前如何校验；层级和交接模式中，转移点上下文不完整/陈旧导致接收方无法自我诊断的故障 |
| 故障隔离 Failure isolation | 一个失败时系统是否、如何不级联地恢复；并行天然隔离；顺序和层级需在每个协调点显式 **回退逻辑 (fallback logic)** |
| 多 agent 可观测性 Multi-agent observability | 需要跨 agent 边界的 **关联 trace (correlated traces)**；每个 agent 的 trace 必须链接到整体会话（如共享 session/trace ID），才能从起源跟到显现处 |
| 成本与延迟 Cost &amp; latency | 并行或循环在每个协调步成倍增加 token 和响应时间；scope 中写每任务成本估算 |

- **选错模式代价高**：任务总在 2 步内结束却用循环 → 每次都烧 token；两个独立步骤用顺序 → 墙钟时间无谓翻倍。在调研中把 **任务结构映射到模式的协调模型**，而不是等试点暴露错配。

<svg viewBox="0 0 800 420" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="800" height="420" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">Orchestration Patterns｜编排模式</text>
  <g font-size="12">
    <text x="20" y="55" font-weight="bold">Sequential 顺序</text>
    <rect x="170" y="38" width="80" height="28" rx="5" fill="#e8f0fe" stroke="#3367d6"/><text x="210" y="57" text-anchor="middle">Agent A</text>
    <rect x="290" y="38" width="80" height="28" rx="5" fill="#e8f0fe" stroke="#3367d6"/><text x="330" y="57" text-anchor="middle">Agent B</text>
    <rect x="410" y="38" width="80" height="28" rx="5" fill="#e8f0fe" stroke="#3367d6"/><text x="450" y="57" text-anchor="middle">Agent C</text>
    <line x1="250" y1="52" x2="288" y2="52" stroke="#555"/><line x1="370" y1="52" x2="408" y2="52" stroke="#555"/>
    <text x="520" y="57" font-size="11" fill="#444">easiest to debug｜最易调试</text>

    <text x="20" y="120" font-weight="bold">Parallel 并行</text>
    <rect x="170" y="105" width="70" height="28" rx="5" fill="#f1f3f4" stroke="#5f6368"/><text x="205" y="124" text-anchor="middle">Split</text>
    <rect x="280" y="85" width="80" height="24" rx="5" fill="#e8f0fe" stroke="#3367d6"/><text x="320" y="102" text-anchor="middle">Agent A</text>
    <rect x="280" y="115" width="80" height="24" rx="5" fill="#e8f0fe" stroke="#3367d6"/><text x="320" y="132" text-anchor="middle">Agent B</text>
    <rect x="280" y="145" width="80" height="24" rx="5" fill="#e8f0fe" stroke="#3367d6"/><text x="320" y="162" text-anchor="middle">Agent C</text>
    <rect x="400" y="105" width="90" height="28" rx="5" fill="#e6f4ea" stroke="#137333"/><text x="445" y="124" text-anchor="middle">Aggregate</text>
    <g stroke="#555"><line x1="240" y1="119" x2="278" y2="97"/><line x1="240" y1="119" x2="278" y2="127"/><line x1="240" y1="119" x2="278" y2="157"/>
    <line x1="360" y1="97" x2="398" y2="119"/><line x1="360" y1="127" x2="398" y2="119"/><line x1="360" y1="157" x2="398" y2="119"/></g>
    <text x="520" y="124" font-size="11" fill="#444">handle partial failure｜处理部分失败</text>

    <text x="20" y="215" font-weight="bold">Loop 循环</text>
    <rect x="170" y="200" width="90" height="28" rx="5" fill="#e8f0fe" stroke="#3367d6"/><text x="215" y="219" text-anchor="middle">Generate</text>
    <rect x="300" y="200" width="90" height="28" rx="5" fill="#fef7e0" stroke="#e37400"/><text x="345" y="219" text-anchor="middle">Evaluate</text>
    <line x1="260" y1="214" x2="298" y2="214" stroke="#555"/>
    <path d="M345 230 C345 255, 215 255, 215 230" stroke="#555" fill="none"/>
    <line x1="390" y1="214" x2="428" y2="214" stroke="#555"/>
    <rect x="430" y="200" width="60" height="28" rx="5" fill="#e6f4ea" stroke="#137333"/><text x="460" y="219" text-anchor="middle">Exit</text>
    <text x="520" y="219" font-size="11" fill="#444">max iterations + budget｜迭代与预算上限</text>

    <text x="20" y="300" font-weight="bold">Hierarchical 层级</text>
    <rect x="270" y="275" width="120" height="28" rx="5" fill="#fce8e6" stroke="#c5221f"/><text x="330" y="294" text-anchor="middle">Orchestrator</text>
    <rect x="180" y="330" width="80" height="24" rx="5" fill="#e8f0fe" stroke="#3367d6"/><text x="220" y="347" text-anchor="middle">Sub A</text>
    <rect x="290" y="330" width="80" height="24" rx="5" fill="#e8f0fe" stroke="#3367d6"/><text x="330" y="347" text-anchor="middle">Sub B</text>
    <rect x="400" y="330" width="80" height="24" rx="5" fill="#e8f0fe" stroke="#3367d6"/><text x="440" y="347" text-anchor="middle">Sub C</text>
    <g stroke="#555"><line x1="330" y1="303" x2="220" y2="328"/><line x1="330" y1="303" x2="330" y2="328"/><line x1="330" y1="303" x2="440" y2="328"/></g>
    <text x="520" y="320" font-size="11" fill="#444">most failures start here｜多数故障在编排者</text>

    <text x="20" y="395" font-weight="bold">Handoff 交接</text>
    <rect x="170" y="378" width="100" height="28" rx="5" fill="#e8f0fe" stroke="#3367d6"/><text x="220" y="397" text-anchor="middle">Intake agent</text>
    <rect x="330" y="378" width="120" height="28" rx="5" fill="#e8f0fe" stroke="#3367d6"/><text x="390" y="397" text-anchor="middle">Resolution agent</text>
    <line x1="270" y1="392" x2="328" y2="392" stroke="#555"/>
    <text x="300" y="374" font-size="10" text-anchor="middle" fill="#c5221f">validated payload</text>
    <text x="520" y="397" font-size="11" fill="#444">first agent stops｜前者停止</text>
  </g>
</svg>

### 面试怎么说 / How to say it in the interview

**Q: When would you use multiple agents instead of one? / 何时用多 agent？**
> "Only when one of three things holds: sub-tasks are independent so parallelism really cuts latency, sub-tasks need genuinely different tool sets, or the total context won't fit one window even with compression. Otherwise a single agent with a good harness is cheaper, easier to debug, and easier to hand off. Multi-agent multiplies token cost and makes failures harder to trace, so I put per-task cost estimates in the scope before recommending it."
>
> 中文：三条件之一才用多 agent；否则单 agent 更好；先算成本。

**Q: Compare hierarchical orchestration and agent handoff.**
> "In hierarchical, an orchestrator stays in charge — it plans, calls subagents, receives their results and decides the next step; subagents don't talk to each other. In handoff, control actually transfers — the first agent stops and the second continues from the context it was given. Hierarchical failures usually start in the orchestrator's error handling; handoff failures show up in the second agent but originate in a bad payload from the first, so I define and validate the handoff payload schema."
>
> 中文：层级 = 编排者始终控制；交接 = 控制权转移；分别关注编排者错误处理和交接载荷校验。

**Q: How do you debug a failure in a multi-agent system?**
> "Each agent emits its own trace, but they all carry a shared session or trace ID so I can follow the failure from where it surfaced back to where it originated, often across an agent boundary. Then I check the state passed at each transfer point, because incomplete or stale context is the most common root cause."
>
> 中文：共享 trace ID 关联各 agent 的 trace；重点检查转移点状态。

**Q: What's the risk with loop orchestration?**
> "A loop without a precise exit condition runs until it burns your budget. I set a quality-based exit, a hard max iteration count, and a token ceiling, and I test it with adversarial inputs in the pilot. I also check that the task actually needs iteration — if it always finishes in two steps, the loop is pure overhead."
>
> 中文：精确退出条件 + 最大迭代 + token 上限；对抗性测试；确认真需要循环。

---

## 14. Choosing an Agentic Framework｜选择智能体框架

Source: https://www.educative.io/courses/forward-deployed-engineer/choosing-an-agentic-framework

### 要点 / Key ideas

- 框架实现编排模式、**工具绑定 (tool binding)**、记忆集成、可观测性钩子 (hooks)。FDE 两种情境：客户已有框架；或从零开始需要推荐。框架选择是 **调研阶段问题 (discovery-phase question)**；选错会在 FDE 离开后以维护问题出现。目标不是抽象上最强，而是匹配问题、编排模式和 **将拥有系统的团队**。
- **框架提供**：编排原语 (orchestration primitives)（循环管理、分支、条件执行）、工具绑定约定、记忆集成模式、追踪/日志钩子 → 显著缩短实现时间。
- **框架不提供设计决策**：哪种编排模式、每个 agent 边界护栏如何配置、agent 间交接载荷包含什么、跨 agent 可观测性如何埋点 —— 框架让这些更快实现，不替代做决定。

**框架全景 (framework landscape)**：

| 框架 Framework | 编排模型 Orchestration model | 最适合 Best fit | 优势 / 取舍 Strength / trade-off |
|---|---|---|---|
| LangChain | 链式流水线 Chain-based pipelines | RAG 工作流、工具增强流水线 | 生态广度：大量 LLM、向量库、API 集成；复杂条件逻辑/循环/持久状态需额外工具 → 用 LangGraph |
| LangGraph | 基于图 + 持久状态 Graph-based with persistent state | 复杂分支、循环、层级编排 | 节点 = agent/函数，边 = 转移；原生支持顺序、条件、循环、持久状态；执行流显式可检查；学习曲线更陡 |
| CrewAI | 基于角色的协作 Role-based coordination | 专家型多 agent 协作 | agent 定义为有角色、目标、工具的专家；内置任务分配/委派；定义可读性好（非技术干系人 (stakeholders) 也能懂）；执行流控制不如 LangGraph 细 |
| AutoGen (Microsoft) | 对话式轮流 Conversational turn-taking | 迭代精炼、评审循环 | 代码生成与审查、文档起草与批评、相互挑战；人可在定义点加入对话；对话结构显式可审计 |
| OpenAI Agents SDK | 工具调用 + agent 交接 Tool-calling, agent handoff | 基于 GPT 模型的 agentic 流水线 | **harness-first** 设计，内置追踪、交接原语；与 OpenAI API 紧耦合；需要模型灵活性时受限 |
| Google ADK | 多 agent 编排 Multi-agent orchestration | Google Cloud 原生部署 | 原生 Gemini、集成 GCP API 与数据服务；无 GCP 的团队面临模型绑定 + 基础设施上手成本 |
| Claude Agent SDK | 工具调用 + agent 交接 Tool-calling, agent handoff | 基于 Claude Sonnet/Opus 的 agentic 流水线 | agent 定义、工具绑定、交接原语、追踪；同样是原生集成深度 vs 模型选择灵活性的权衡 |

**从零推荐的五条标准 (five criteria when recommending from scratch)** —— 组合使用：

| 标准 Criterion | 说明 Description |
|---|---|
| 设计哲学契合 Design philosophy fit | 框架区别在于 **工作流如何表达**：LangGraph = 有向图（偏好显式控制状态与执行流的团队）；CrewAI = 角色与协作任务（以专家协作思考问题的团队）；AutoGen = 对话轮流（迭代精炼） |
| 模型亲和与厂商灵活性 Model affinity &amp; vendor flexibility | 已承诺某模型供应商 → 对齐的框架集成更好；想评估多模型 → 模型无关框架减少 **锁定 (lock-in)** |
| 内置可观测性 Observability built in | 内置追踪少 → FDE 手动埋点、增加构建时间、客户维护自定义工具 |
| 实现速度 Implementation speed | 2–3 周 sprint 时团队能否快速上手；学习曲线 vs 编排收益 |
| 移交后所有权 Post-handoff ownership | 客户团队无法自信运营的框架，不如他们能拥有的更简单方案；明确估算 **上手负担 (onboarding burden)** |

**客户已选框架时的三种情况 (when the customer has already chosen)**：

| 情况 Situation | 应对 Response |
|---|---|
| 适合用例 Fits the use case | 在其中高效工作；先熟悉团队现有模式和约定再提改动 |
| 次优但可行 Suboptimal but workable | 继续使用；在移交文档中说明接受了什么约束、客户应长期监控什么；技术理由不足时 **不要主张切换** |
| 真正阻碍用例 Genuinely blocks the use case | 以 **交付风险 (delivery risk)** 框定推荐切换：具体技术约束、对时间线的影响、切换成本 vs 继续成本；**决定权属于客户** |

<svg viewBox="0 0 760 260" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="760" height="260" fill="#fff"/>
  <text x="380" y="22" font-size="15" text-anchor="middle" font-weight="bold">Framework Decision Flow｜框架选择流程</text>
  <g font-size="12" text-anchor="middle">
    <polygon points="380,40 480,75 380,110 280,75" fill="#fef7e0" stroke="#e37400"/><text x="380" y="72">Customer has</text><text x="380" y="88">a framework?</text>
    <polygon points="170,130 260,165 170,200 80,165" fill="#fef7e0" stroke="#e37400"/><text x="170" y="162">Blocks the</text><text x="170" y="178">use case?</text>
    <rect x="20" y="215" width="140" height="36" rx="6" fill="#e6f4ea" stroke="#137333"/><text x="90" y="238">Work within it 沿用</text>
    <rect x="180" y="215" width="160" height="36" rx="6" fill="#fce8e6" stroke="#c5221f"/><text x="260" y="231">Recommend switch</text><text x="260" y="246">按交付风险，客户决定</text>
    <rect x="500" y="130" width="240" height="110" rx="8" fill="#e8f0fe" stroke="#3367d6"/>
    <text x="620" y="150" font-weight="bold">Score 5 criteria｜五标准</text>
    <text x="620" y="170" font-size="11">design philosophy 设计哲学</text>
    <text x="620" y="186" font-size="11">model affinity 模型亲和</text>
    <text x="620" y="202" font-size="11">built-in observability 可观测</text>
    <text x="620" y="218" font-size="11">speed 速度 · ownership 所有权</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="300" y1="82" x2="200" y2="138"/><line x1="460" y1="82" x2="580" y2="128"/>
    <line x1="130" y1="185" x2="95" y2="213"/><line x1="215" y1="185" x2="250" y2="213"/>
  </g>
  <g font-size="11" fill="#444">
    <text x="225" y="105">yes</text><text x="530" y="100">no (from scratch)</text>
    <text x="80" y="208">no (note trade-off)</text><text x="240" y="208">yes</text>
  </g>
</svg>

### 面试怎么说 / How to say it in the interview

**Q: Which agent framework would you choose? / 你会选哪个框架？**
> "It depends on the problem and on who owns it after me. If the workflow has real branching, loops, and persistent state, I'd lean on LangGraph because the graph makes execution explicit and inspectable. If the customer is committed to one model provider, that provider's SDK — the Claude Agent SDK, OpenAI Agents SDK, or ADK on Google Cloud — gives native tracing and handoffs. But the framework doesn't make the design decisions for me; I still choose the pattern, the guardrails at each boundary, and the handoff payload."
>
> 中文：取决于问题与后续负责人；复杂状态选 LangGraph，绑定供应商选其 SDK；框架不替代设计决策。

**Q: The customer already uses a framework you think is suboptimal. What do you do?**
> "If it's workable, I work within it — the team already knows it, which lowers ramp time and makes the system maintainable after handoff. I document the constraint we accepted and what to watch. I only recommend switching if it genuinely blocks the use case, and then I frame it as delivery risk: the specific constraint, the timeline impact, and the cost of switching versus staying. The decision is theirs."
>
> 中文：可行就沿用并记录约束；真正阻碍才以交付风险建议切换，客户决定。

**Q: LangChain vs LangGraph?**
> "LangChain is the broad integration layer — great for RAG and linear tool-augmented chains, with connectors for almost any vector DB or API. LangGraph adds a graph execution model with nodes, edges, cycles, and persistent state, which is what you need for loops, conditional routing, or hierarchical orchestration. The trade-off is a steeper learning curve, which I factor into the customer team's onboarding."
>
> 中文：LangChain 重集成、线性链；LangGraph 加图、循环、持久状态，学习曲线更陡。

---

## 速查 / Cheat sheet

| # | 要点 Takeaway (中文) | English one-liner |
|---|---|---|
| 1 | FDE 弥合部署鸿沟；多数失败是部署问题（数据、权限、负责人），不是模型问题 | Most enterprise AI failures are deployment failures, not model failures. |
| 2 | 时间线属于客户：按可用时间定范围，先交最小可证明价值的系统 | Scope to the time available; ship the smallest system that proves core value. |
| 3 | 调研是技术调查不是推销；不在调研会上提架构 | Discovery is an investigation, not a pitch — no architecture in the room. |
| 4 | 三类人在场：执行发起人、一线专家、技术联系人；问变通方案 | Get sponsor, operator, and technical contact; ask about the workaround. |
| 5 | 五列笔记：痛点、流程、数据、候选指标、访问阻碍；离场前四项检查 | Five-column notes; leave with data access, metric, realistic timeline, one owner. |
| 6 | 先建基线（时间、错误率、预计 token 成本） | Establish the baseline before proposing anything. |
| 7 | Scope 六要素；out-of-scope 是承重墙 | Six-part scope doc; out-of-scope is load-bearing. |
| 8 | 翻译阶梯五层 + 最小 AI 组件原则 | Pain → workflow → data → integration → AI component; minimal AI component. |
| 9 | 每事务 token × 日量，定架构前算成本；风险登记写可能性/影响/缓解 | Tokens per transaction × daily volume; risk register with likelihood, impact, mitigation. |
| 10 | POC 产出答案不是产品：Proceed / Pivot / Stop；演示 Before→During→After | A POC produces an answer; demos are value narratives. |
| 11 | 试点三信号：可靠性、采用、信任；看分布不看均值；可先影子模式 | Pilot readiness = reliability, adoption, trust; start in shadow mode. |
| 12 | 部署就绪五维：可靠、质量、安全、成本、可观测；安全和可观测必须先达标 | Ready = reliability, quality, safety, cost, observability. |
| 13 | HITL 三件套：触发、队列（指定人 + SLA）、记录覆盖决定 | Trigger, queue with owner + SLA, logged override decisions. |
| 14 | 结构化 JSON 日志；含 PII 的完整输入不进通用日志 | Structured logs with request IDs; never PII in general logs. |
| 15 | 现场信号需在 ≥2 个不同客户见过；反馈六要素，以数据点而非批评呈现 | A signal appears in ≥2 distinct customers; six-element feedback. |
| 16 | Agentic 看运行时自主多步行为，不看框架；生产故障多在 harness | Agentic is runtime behavior; most failures are harness failures. |
| 17 | 先用最简单架构；最常见 scoping 错误是给 LLM 能解决的问题上 agent | Start simple; don't propose an agent for an LLM-pipeline problem. |
| 18 | RAG 管知识、微调管行为；RAG 先查检索、分块、新鲜度、摄取负责人 | RAG for knowledge, fine-tuning for behavior; debug retrieval first. |
| 19 | 护栏四类：范围、预算、输出过滤、权限；"下周出错客户能否重建"是可观测性标准 | Scope, budget, output filter, permission guardrails; traces must be reconstructable. |
| 20 | 多 agent 仅在并行/不同工具/上下文超限时用；层级看编排者，交接看载荷校验 | Multi-agent only when justified; validate handoff payloads; correlate traces. |
