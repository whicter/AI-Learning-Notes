# Palantir FDE Interview Prep, Part 1: Role, Process & Technical Screen｜Palantir FDE 面试准备（上）：角色、流程与技术筛选

> Section I：课程 "Palantir FDE Interview Prep" 的前 18 课（角色、申请、个人故事、技术筛选）。
> Section II：主课程 "Forward Deployed Engineer for AI Systems" 中 Palantir 模块，只写与 Section I 不同或新增的内容。
> 第二部分（decomposition、learning、re-engineering、coding、system design、behavioral、mock loop）见 Part 2。

---

# Section I — Palantir FDE Interview Prep

## 1. Introduction｜课程导论

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/introduction

**要点 / Key ideas**

- Palantir 前线部署软件工程师 (Forward Deployed Software Engineer, FDSE) 的面试不只考算法。你可能要：拆解一个没有规格说明 (no clear spec) 的混乱运营问题、从文档快速学习一个陌生系统、修改从未见过的代码，并且全程大声讲出推理 (think out loud)。
- 只刷算法题的候选人常在这些轮次里"翻车"。

| 特点 (Why FDSE prep is different) | 含义 (What it means) |
|---|---|
| 推理重于记忆 (Reasoning over recall) | 面试官给"如何澄清 (clarify)、界定范围 (scope)、验证 (verify)"打分，不只看答案对不对 |
| 考学习速度 (Learning speed is tested) | Learning round 测的是你多快理解新东西，而不是你已经知道什么 |
| 调试有陷阱 (Debugging has traps) | Re-engineering 题里有干扰项 (red herrings)，需要系统化方法盯住真正的缺陷 |
| 需求中途变化 (Requirements change mid-interview) | 要区分"保持行为不变的重构 (behavior-preserving refactor)"和"有意的行为变更 (intentional change)"，并用回归测试 (regression tests) 证明两者 |
| 运营型设计 (Operational design) | 系统设计聚焦数据管道 (data pipelines)、集成 (integration)、可靠性 (reliability)、访问控制 (access control)，而不是抽象框图 |
| 你的故事也算分 (Your story counts) | "Why Palantir?"、项目经历、对使命与伦理 (mission and ethics) 的看法都会被评估；行为题也会在技术轮里冒出来 |

- 课程四阶段 (four stages)：① 角色、申请与个人故事 → ② 代表性技术筛选 (technical screens：implementation、algorithm、SQL、分页 API) → ③ 运营问题解决轮 (decomposition、learning、re-engineering、coding、system design) → ④ 行为证据、终面 (hiring manager final)、团队匹配 (team matching)、offer、完整模拟面试 (mock loops) 与四周计划。
- 前提：会写代码、懂基础数据结构。参考代码 Python 3.12，参考 SQL 为 PostgreSQL 16。不需要 Palantir 平台经验。
- 全课核心理念："面试官只能给你**让他看见的东西**打分 (interviewers can only score what you make visible)"。澄清问题、说出假设、测试代码、诚实讲述经历。
- 公开面经显示各人轮次组合不同 → 和招聘方 (recruiter) 确认你自己的流程。

**面试怎么说 / How to say it**

> "Before I start coding, let me restate the problem and the assumptions I'm making, so you can correct me early. Then I'll write a small working version, test it on a couple of edge cases, and talk through what I'd harden next."
>
> 中文：先复述问题和假设，再写最小可用版本、测边界，最后讲下一步加固——把推理过程"可见化"。

---

## 2. Palantir in 10 Minutes: Foundry, Gotham, AIP and the Ontology｜10 分钟了解 Palantir：Foundry、Gotham、AIP 与本体

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/palantir-in-10-minutes-foundry-gotham-aip-and-the-ontology

**要点 / Key ideas**

Palantir 提供把组织数据连接到决策与运营工作 (connecting organizational data to decisions and operational work) 的软件平台。前线部署工程 (forward deployed engineering) = 工程师嵌入客户环境，和用户一起构建并交付运营问题的解决方案。

起点问题永远是实用的：**协调员 (coordinator) 需要看到什么、决定什么、改变什么？**

| 产品 (Offering) | 定位 (Focus) | 维修例子中的作用 (In the maintenance case) |
|---|---|---|
| Foundry | 数据管理 (data management)、逻辑编写 (logic authoring)、本体开发 (Ontology development)、分析 (analytics)、工作流开发 (workflow development) | 把记录汇总起来，构建派工工作流 |
| Gotham | Palantir 最早的平台；面向国防、情报、公共部门 (defense, intelligence, public sector) 的数据集成与运营决策。与 Foundry 的区别是**侧重点**，不是严格的政府/商业界线 | — |
| AIP (Artificial Intelligence Platform) | 安全的大模型连接 (secure LLM connectivity)、智能体开发工具 (agent development tools)、AI 应用、评估 (evaluation) | AI 助手可以推荐技师、总结维修单 |
| Ontology 本体 | **不是**第四个平行平台；它提供应用所用的"互相连接的对象、关系和动作 (connected objects, relationships, actions)" | — |

- 常见错误：把 AIP 当成 Foundry 或 Ontology 的别名。没有模型时工作流照样有用；加入模型只是多了一种其输出需被正确处理的能力。

**本体五个概念 (Five Ontology concepts)** — 维修派工例子：泵 P17 需要维修单 R42；技师 T8（空闲、有泵资质）、T9（空闲、只有电工资质）。

| 概念 (Concept) | 定义 (Definition) | 例子 (Example) |
|---|---|---|
| 对象类型 (Object type) | 现实实体或事件的类型 | Pump, Repair, Technician |
| 对象 (Object) | 类型的一个实例 | P17, R42, T8 |
| 链接类型 (Link type) | 对象类型之间关系的结构 | "Repair concerns Pump" |
| 链接 (Link) | 关系的一个实例 | "R42 concerns P17" |
| 动作 (Action) | 在规则下改变运营状态 | Assign repair（派工） |
| 应用 (Application) | 面向用户的界面，暴露信息与动作 | 协调员的维修队列 (repair queue) |

- 把对象类型类比成表定义 (table definition)、对象类比成一行 (row) 是好的起点，但**漏掉了运营行为 (operational behavior)**：这张单子关于哪台设备？用户能做什么动作？动作成功前必须满足什么？
- Ontology Manager：定义对象类型和动作类型、把数据连到本体、排查数据是否在应用里更新。

**经过验证的动作 (validated action) 的推演**

规则：派工要求技师 **空闲 (available) 且** 具备该设备类型资质 (qualified)。

1. R42 concerns P17，P17 类型 = pump。
2. T8 空闲且有泵资质 → 两项检查都通过。
3. 动作把 R42 的 status 改为 assigned、assignee 改为 T8。
4. R42 仍然 concerns P17 —— 派工**不改变**设备链接。

模型推荐 T9（只看到了空闲，忽略了资质）→ 派工必须被拒绝，R42 保持 open、assignee_id = null。**一个看似合理的建议既不构成资格校验，也不等于执行了动作 (a suggestion neither validates nor executes)。** 推荐 (recommendation) 与校验 (validation) 必须分离。

测验答案：唯一正确选项是"对 R42 和 T8 执行 Assign repair → assigned、assignee T8、设备 P17 不变"。错误选项包括：把设备链接替换成 T8；因为 T9 空闲就派给 T9；把模型建议直接当作派工。

<svg viewBox="0 0 760 260" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="13">
  <rect x="0" y="0" width="760" height="260" fill="#fff"/>
  <rect x="20" y="40" width="130" height="70" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="85" y="65" text-anchor="middle" font-weight="bold">Source records</text>
  <text x="85" y="85" text-anchor="middle">源数据</text>
  <text x="85" y="102" text-anchor="middle" font-size="11">P17, R42, T8, T9</text>
  <rect x="190" y="40" width="150" height="70" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="265" y="62" text-anchor="middle" font-weight="bold">Ontology</text>
  <text x="265" y="80" text-anchor="middle">objects + links 对象+链接</text>
  <text x="265" y="98" text-anchor="middle" font-size="11">R42 concerns P17</text>
  <rect x="380" y="40" width="160" height="70" rx="8" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="460" y="62" text-anchor="middle" font-weight="bold">Action: Assign repair</text>
  <text x="460" y="80" text-anchor="middle">动作 + 校验规则</text>
  <text x="460" y="98" text-anchor="middle" font-size="11">available AND qualified</text>
  <rect x="580" y="40" width="160" height="70" rx="8" fill="#e8f7ee" stroke="#2e9b5a"/>
  <text x="660" y="62" text-anchor="middle" font-weight="bold">New state 新状态</text>
  <text x="660" y="80" text-anchor="middle" font-size="11">R42: assigned, T8</text>
  <text x="660" y="98" text-anchor="middle" font-size="11">link to P17 unchanged</text>
  <line x1="150" y1="75" x2="188" y2="75" stroke="#333" marker-end="url(#a2)"/>
  <line x1="340" y1="75" x2="378" y2="75" stroke="#333" marker-end="url(#a2)"/>
  <line x1="540" y1="75" x2="578" y2="75" stroke="#333" marker-end="url(#a2)"/>
  <rect x="380" y="170" width="160" height="60" rx="8" fill="#f5eefc" stroke="#8a4fd0" stroke-dasharray="5,3"/>
  <text x="460" y="193" text-anchor="middle" font-weight="bold">AIP suggestion (optional)</text>
  <text x="460" y="213" text-anchor="middle">AI 建议（可选）: "T9?"</text>
  <line x1="460" y1="170" x2="460" y2="112" stroke="#8a4fd0" stroke-dasharray="4,3" marker-end="url(#a2)"/>
  <text x="600" y="200" font-size="12" fill="#b3261e">T9 fails qualification → rejected</text>
  <text x="600" y="218" font-size="12" fill="#b3261e">T9 资质不符 → 拒绝</text>
  <rect x="190" y="170" width="150" height="60" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="265" y="193" text-anchor="middle" font-weight="bold">Application</text>
  <text x="265" y="213" text-anchor="middle">维修队列 repair queue</text>
  <line x1="340" y1="200" x2="378" y2="90" stroke="#333" marker-end="url(#a2)"/>
  <defs><marker id="a2" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
  <text x="20" y="25" font-weight="bold">Data-to-workflow with validated actions｜数据到工作流：经过校验的动作</text>
</svg>

- 课程路线：四阶段（角色/申请/故事 → 技术筛选 → 运营问题轮 → 行为/终面/模拟）。每阶段要产出的证据：具体的动机回答与贡献故事；限时解法+可见推理+测试；可落地的工作流设计或经验证的代码改动；模拟面试复盘和针对性计划。
- 正确的变更**只改变预期的运营事实** (a correct action changes only the intended operational facts)——不变的设备链接和改变的 assignee 一样重要。

**面试怎么说 / How to say it**

> Q: "How would you explain Foundry, AIP and the Ontology to a new teammate?"
>
> "Foundry is the data and workflow platform: integration, logic, analytics and app building. The Ontology is the layer inside it that turns rows into business objects, links between them, and actions with validation rules. AIP adds secure LLM access, agents and evals on top. So in a repair workflow, the model can suggest a technician, but only the Ontology action, with its eligibility checks, actually changes the repair's state."
>
> 中文：Foundry 是数据+工作流平台；Ontology 把行变成对象、链接和带校验的动作；AIP 在其上加 LLM 能力。模型只能建议，真正改状态的是带校验的 Action。

---

## 3. The FDSE Role Decoded: Reading the Job Description Line by Line｜逐行解读 FDSE 职位描述

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/the-fdse-role-decoded-reading-the-job-description-line-by-line

**要点 / Key ideas**

- 弱注解："Developing custom applications tailored to customer needs" → "I build customer-focused solutions"。只是复述了承诺，没有指出任何工程工作。好的解读要说明：**谁用这个应用、要完成什么任务；你实现了什么行为、如何和用户核对**。
- 官方 FDSE 职位（2026-10-28 快照）：和客户并肩工作、理解其问题，用业务关键数据 (business-critical data)和 AI 架构并构建方案。列出的职责：协作式架构与设计 (collaborative architecture and design)、大规模数据整理 (large-scale data wrangling)、定制应用 (custom applications)、利益相关方沟通 (stakeholder engagement)、从构想到部署推动项目 (ideation to deployment)。

**职责注解五要素 (Responsibility annotation)**

| 要素 (Element) | 含义 (Meaning) |
|---|---|
| 职位原文 (Posting words) | 雇主的原话 |
| 具体工作 (Concrete work) | 这句话隐含的可观察工程活动 |
| 个人贡献 (Personal contribution) | 你**实际**做了什么 |
| 证据 (Evidence) | 支撑贡献的产物 (artifact) 或观察结果 |
| 局限 (Limits) | 证据**不能**证明什么 |

这是准备工具，不是官方评分标准。

**案例：活动报名工具（你+一个队友）**。主办方给了两份导出：500 行报名、480 行付款（这是行数，不代表唯一参会人数，也不代表一一对应）。真正的运营问题是**重复签到 (duplicate check-ins)**，一上来说"主办方需要一个仪表盘 (dashboard)"就跳过了需要修的行为。

| 职责 (Responsibility) | 具体工作 (Concrete work) | 你的贡献 (Your contribution) | 证据 (Evidence) | 局限 (Limits) |
|---|---|---|---|---|
| 需求发现 (Discovery) | 观察签到流程、解决冲突需求、约定"有效签到"的定义 | 实现前先问主办方：重复报名和缺失付款号怎么处理 | 记录问题和约定规则的会议纪要 (meeting notes) | 只证明和主办方的沟通，**不证明**高管沟通 (executive engagement) |
| 数据 (Data) | 定位数据源、核对标识符 (reconcile identifiers)、校验记录、暴露未匹配项 (unmatched records) | 为 500+480 行写核对与校验逻辑 | 核对报告：列出未匹配引用和重复 ID | 两份小文件，**不能**证明"海量规模"；没用 AI |
| 实现 (Implementation) | 把约定流程翻译成查询和状态变更行为 | 你实现报名查询和签到；队友做页面布局 | 代码变更 + 会议纪要 | 完整应用是团队成果，布局归队友 |
| 架构 (Architecture) | 比较取数方式、评估约束、记录权衡 (tradeoffs) | 你和队友比较"定期导入本地副本" vs "实时报名 API"，因为没有 API 权限而共同选择导入 | 联合设计文档：两种方案、权限约束、后果（迟到的报名需手动更新） | 只证明**参与**共同设计决策，不能说"我独立设计了整个系统" |
| 自主性 (Autonomy) | 独立调查不确定性，识别哪些决策需要利益相关方 | 自己追踪重复 ID，再请主办方裁定模糊的身份规则 | 调查记录 + 纪要 | 证明独立调查和适当上报 (escalation)，身份规则不是你一个人定的 |
| 交付 (Delivery) | 发布约定范围、上线观察、响应反馈 | 参与 40 次试签到的受监督试点 (supervised pilot)；发现可提交第二次签到后加了重复保护 (duplicate guard)，验证重复尝试不改变原签到 | 试点检查表 | 40 是试签次数，不是效率提升；未证明持续生产运维 |

- 为什么选导入：在权限约束下**可行**。选一个拿不到的接口会让试点没有可用数据源。记录下来的局限同时解释了选择和运营代价。
- 测验答案："我核对了两份小导出的标识符并记录了数据质量问题；海量处理尚未证明"。错误：把 500+480 加成 980 个唯一参会者；宣称已测量的效率提升。

**夸大陈述审计 (Inflated claim audit)**：

"I independently architected and deployed an enterprise-scale AI platform, aligned executives and improved check-in efficiency by 80%." —— 有问题的词：independently architected、enterprise-scale、AI platform、aligned executives、improved efficiency by 80%。

修法：**不是**把所有动词都弱化。保留有支撑的动作（实现、部署），写清范围和合作者；**删除**无支撑的说法而不是软化（"有一些效率提升"仍暗示一个没测过的结果）。

证据化重写：
> "I reconciled registration and payment exports and implemented lookup and check-in, while my teammate built the layout. Together we chose an imported copy because API access was unavailable, documenting manual updates for late registrations. During a supervised pilot with 40 trial check-ins, I added a duplicate guard and verified that a repeat attempt preserved the original check-in."

**部分匹配 vs 缺口 (Partial match vs gap)**：有相关行为但缺职位里的某个维度 = 部分匹配；找不到相关动作或观察 = 缺口。专业经验：指出你负责的集成或发布，分开你的动作和团队的整体结果。缺口：选一个有边界的下一步，完成前缺口仍在。

**面试怎么说 / How to say it**（资深工程师版）

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 37 篇）。

---

## 4. FDSE Variants and Adjacent Roles: Commercial, Government, Edge｜FDSE 变体与相邻岗位

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/fdse-variants-and-adjacent-roles-commercial-government

**要点 / Key ideas**

- 岗位族 (role family)：FDSE、部署策略师 (Deployment Strategist)、软件工程师 (SWE)。Commercial / Government 是**客户场景 (customer context)**；Edge 指靠近设备或运营现场的计算（边缘计算），具体含义看职位本身。

**五个独立比较维度 (Five dimensions)**

| 维度 (Dimension) | 内容 (What to extract) |
|---|---|
| 岗位族 (Advertised role family) | 准确的职位名称 |
| 客户场景 (Customer context) | 职位描述的是谁的问题 |
| 工作与交付物 (Work and deliverables) | 你要构建、集成、调查或培训什么 |
| 技术环境 (Technical environment) | 软件、数据、设备、部署环境 |
| 明确约束 (Explicit constraints) | 地点、办公方式、经验年限、出差、资格（如安全许可 (security clearance)） |

记录准确职位名、来源 URL 和查看日期，再把要求放进准备计划。"customer""data""engineering"这类共享词不会在职位之间传递职责或要求。

**各职位要点（2026-10-28 快照）**

| 职位 (Vacancy) | 关键信息 (Key facts) | 注意 (Caveat) |
|---|---|---|
| FDSE - US Government | 华盛顿、纽约、檀香山都有 | "Government"本身不说明许可级别 (clearance level) |
| FDSE Internship - Commercial | 客户场景标签 | "Commercial"不等于零出差或只用某平台 |
| FDSE - US Gov, Federal Health and Civilian（第三方转载） | 数据管道、运营工作流、AI agent 部署 | 非官方核实 |
| Deployment Strategist（芝加哥） | 通过深入客户问题找数据集；与 FDE 合作把数据集成到稳定可扩展管道；定制工作流、培训用户、演示、把一线洞察带回产品 | **明确要求**编程/脚本/统计经验 (Python, R, Matlab, SQL)；出差 25–75%；需在芝加哥地区工作。说它"非技术"是错的 |
| FDSE - Edge Autonomous Systems（华盛顿，hybrid） | 自主软件：导航、传感器融合 (sensor fusion)、执行器 (actuation)；集成传感器、执行器、无人平台；跨边缘/本地/混合云解决网络、安全、硬件、部署、UX 问题 | 要求：网络、Linux/GNU、CI/CD、脚本、自动化、API、边缘硬件；精通 Python/Rust/C++/Java 之一；2 年以上专业开发；2 年以上边缘/自主系统集成部署；学位或相关经验；"现有美国安全许可**或**有资格且愿意获取"；出差 25–75%。AI/ML、传感器处理为"highly desirable"（偏好，不是要求） |
| FDSE - Tactical Edge（华盛顿，on-site） | 只确认全职和现场办公 | 职责、许可、面试流程都未知——写"listing 未确认"，不是"不需要许可" |
| Deployment Strategist - US Government（迈阿密） | 申请页："如果没有指定许可，申请不会被考虑" | 硬性门槛；级别未说明 |
| SWE - Core Interfaces（Palo Alto、纽约）/ SWE - Defense Applications（华盛顿） | 没有完整描述 | 不能写"SWE 从不接触客户"——保持未解决 |

**笔记三栏 (Three fields)**：明确要求 (explicit requirement)、表述的偏好 (stated preference)、待解决问题 (unresolved question)。数字范围和"或"的选项原样保留。

- 测验（无现有许可、资格未确认的候选人）：正确答案是"Edge Autonomous Systems 不因无现有许可而自动排除，资格、意愿和其它要求需确认；迈阿密有明确冲突；Tactical Edge 许可未知"。陷阱：把"存在一条路径"当成"条件已满足"。
- 案例结论：有 Python/SQL/用户培训经验、无许可、无边缘集成经验、出差上限 25% 的候选人 → 优先调查芝加哥 Deployment Strategist 的出差和地点要求（25–75% 的区间不承诺封顶 25%）。这是有依据的调查优先级，不是录用预测。
- 错误比较笔记的逐句修正：许可措辞因职位而异；Tactical Edge 面试流程未确认；芝加哥明确要求编程；Core Interfaces 是否接触用户未知。

**面试怎么说 / How to say it**

> Q (recruiter): "Which team or variant are you most interested in?"
>
> "I'm most interested in the commercial FDSE track, because the posting emphasizes data integration and custom workflows, which is where most of my experience is. I'd like to confirm two things with you: the expected travel for that team, and whether the role is hybrid in the city I'd be based in."
>
> 中文：基于具体职位原文说明兴趣，并把出差、地点等不确定项作为问题提出，而不是凭职位名推断。

---

## 5. Hands-On With Foundry and AIP: What to Explore Before You Interview｜面试前动手体验 Foundry 和 AIP

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/hands-on-with-foundry-and-aip-what-to-explore-before-you

**要点 / Key ideas**

- 场景：服务协调员 (service coordinator) 需要一个设施报修队列 (facilities request queue)，显示关联的服务区域 (service area) 和 AI 建议的类别。探索结束的标志：你能追踪**一条请求从源数据行 → 对象身份 → 区域链接 → 分类输出 → 人工决策**的全过程。
- 75 分钟时间盒 (timebox)：10 分钟选路线、20 分钟映射记录、20 分钟探索分类与审核、15 分钟检查结果、10 分钟写说明。这是课程建议，**不是**面试要求（官方没有要求必须有平台权限或完成教程）。
- 范围要小：排除集成、生产部署、自动派单 (auto-dispatch)、界面美化。分类只是粗粒度路由辅助 (coarse routing aid)，不是安全建议也不是行动授权。
- 官方 AIP 入门路线（可选）：基础学习、15 分钟用例界定 (use-case scoping)课程、60–90 分钟首个工作流 speedrun（PDF 抽取、纳入本体、配置聊天机器人 (chatbot)、交互应用）。

**两条路线 (Two routes)**

| 路线 (Route) | 做法 (What you do) |
|---|---|
| 授权访问路线 (Authorized-access route) | 只检查/构建环境允许的资源；记录哪些导入、链接、函数调用、界面步骤真正运行过；不可用的部分写成"提案 (proposal)" |
| 文档路线 (Documentation route) | 用给定记录和官方文档画映射、手工推演预期行为；平台实际输出记为"未运行 (not run)" |

前 10 分钟耗在权限问题上就切换到文档路线。只使用授权的数据；有雇主环境的权限**不等于**被授权导出数据或截图。

**证据状态四级 (Evidence status)**

| 状态 (Status) | 含义 (Meaning) |
|---|---|
| 已观察 (Observed) | 你亲自检查或执行过，保留了允许的记录 |
| 有文档 (Documented) | 官方文档描述了该能力 |
| 已提议 (Proposed) | 你选定的设计，不一定已实现 |
| 未测试 (Untested) | 预期行为尚未执行验证 |

**输入数据包 (Input packet)**

```text
Areas:
area_id,name
A1,Central
A2,West

Requests:
request_id,area_id,text
Q101,A1,Water is pooling under the sink
Q102,A2,Ceiling light will not turn on
Q103,A1,Please inspect the room
Q104,A9,Outlet sparks when used
```

关键错配：Q104 引用 A9，而 Area 的主键只有 A1、A2。

**映射提案 (Proposed mapping)**：Area.area_id → 字符串主键 (primary key)，name → 显示名；Request.request_id → 字符串主键；Request.area_id → 字符串属性，作外键 (foreign key) 指向 Area；text → description。链接的建立靠"外键属性 ↔ 主键、类型匹配"，**属性名相同本身不建立关系**。Q101、Q103 → Central；Q102 → West；Q104 无匹配 → 保留可见的 `missing_area` 校验标记，**不要凭空造一个 Area 对象**。

**AIP Logic 函数提案**：AIP Logic 是无代码 (no-code) 环境，用于构建、测试和发布可使用本体的 LLM 函数。

- 函数 `suggest_category`：输入 = 请求描述文本；输出 = **恰好一个**小写标签：`plumbing`、`electrical` 或 `needs_review`；规则：类别明确就建议，信息不足返回 `needs_review`。
- Logic 能力：输入文本或本体对象，返回值、对象或本体编辑 (Ontology edit)；可在 Workshop 中使用；本体编辑需要发布 Logic 函数并从 Action 调用。本次范围：只返回字符串，不做编辑。

| 请求 (Request) | 链接结果 (Link result) | 预期类别 (Expected) | 审核决策 (Review) |
|---|---|---|---|
| Q101 | A1 → Central | plumbing | 协调员审核建议 |
| Q102 | A2 → West | electrical | 协调员审核建议 |
| Q103 | A1 → Central | needs_review | 要求补充细节 |
| Q104 | A9 → 无匹配，missing_area=true | electrical | 先澄清区域，再做依赖区域的决策 |

实际输出全部为 "not run"。

<svg viewBox="0 0 760 230" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="13">
  <rect x="0" y="0" width="760" height="230" fill="#fff"/>
  <text x="20" y="24" font-weight="bold">Two independent checks｜两项独立检查</text>
  <rect x="20" y="70" width="130" height="60" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="85" y="95" text-anchor="middle" font-weight="bold">Request row</text>
  <text x="85" y="115" text-anchor="middle">源数据行 Q104</text>
  <rect x="210" y="40" width="200" height="56" rx="8" fill="#e8f7ee" stroke="#2e9b5a"/>
  <text x="310" y="62" text-anchor="middle" font-weight="bold">Data validation 数据校验</text>
  <text x="310" y="82" text-anchor="middle" font-size="12">area_id A9 ∉ {A1, A2}</text>
  <rect x="210" y="120" width="200" height="56" rx="8" fill="#f5eefc" stroke="#8a4fd0"/>
  <text x="310" y="142" text-anchor="middle" font-weight="bold">Model eval 模型评估</text>
  <text x="310" y="162" text-anchor="middle" font-size="12">suggest_category = electrical?</text>
  <rect x="470" y="40" width="130" height="56" rx="8" fill="#fdecea" stroke="#b3261e"/>
  <text x="535" y="62" text-anchor="middle">missing_area</text>
  <text x="535" y="82" text-anchor="middle">= true</text>
  <rect x="470" y="120" width="130" height="56" rx="8" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="535" y="142" text-anchor="middle">Exact string</text>
  <text x="535" y="162" text-anchor="middle">match 精确匹配</text>
  <rect x="630" y="80" width="115" height="60" rx="8" fill="#fff" stroke="#333"/>
  <text x="687" y="104" text-anchor="middle" font-weight="bold">Human review</text>
  <text x="687" y="124" text-anchor="middle">人工审核</text>
  <line x1="150" y1="95" x2="208" y2="70" stroke="#333" marker-end="url(#a5)"/>
  <line x1="150" y1="105" x2="208" y2="148" stroke="#333" marker-end="url(#a5)"/>
  <line x1="410" y1="68" x2="468" y2="68" stroke="#333" marker-end="url(#a5)"/>
  <line x1="410" y1="148" x2="468" y2="148" stroke="#333" marker-end="url(#a5)"/>
  <line x1="600" y1="68" x2="628" y2="100" stroke="#333" marker-end="url(#a5)"/>
  <line x1="600" y1="148" x2="628" y2="120" stroke="#333" marker-end="url(#a5)"/>
  <text x="20" y="210" font-size="12">A category label can never supply a missing area key.｜类别标签无法补上缺失的区域外键。</text>
  <defs><marker id="a5" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**两项检查必须分开 (Keep two checks separate)**

- 数据校验 (data validation)：每个 Request 的 area 键 vs Area 主键 → 预期 3 个解析成功、Q104 未解析。
- 模型评估 (model evaluation)：实际类别 vs 4 个预期标签，每个不一致都保留调查。有 Logic + Evals 权限时，用**精确字符串匹配 (Exact string match)** 评估器 (evaluator)；手工建的 Evals 套件只返回函数输出，要加评估器才有聚合指标 (aggregate metrics)。
- 4 个用例只是示例，**不代表**生产准确率。输出不一致时先检查输入、输出契约 (output contract)和函数配置，**不要偷偷改预期让测试通过**。

**测验：表面成功审计**——精美队列显示 `Q104 | electrical | West`，作者说"成功路由到 West"。正确审计：A9 既不匹配 A1 也不匹配 A2 → 拒绝 West、保留 missing_area；先澄清区域；预期 electrical，但没有执行证据实际输出仍为 not run；路由成功无依据。

**面试怎么说 / How to say it**

> Q: "Have you used Foundry or AIP?"
>
> "I haven't had production access, so I want to be precise. I went through the documentation and traced a small facilities-queue example by hand: requests linked to service areas through a foreign key, plus an AIP Logic function that returns exactly one of three labels. The interesting part was a request whose area key didn't resolve. I kept that as a visible data-quality flag, separate from the model's category, because a correct label can't fix a broken link. What I haven't done is run the Evals suite myself, so I'd treat accuracy as untested."
>
> 中文：诚实区分"看过文档/手工推演"和"实际运行过"；举一个具体机制（外键未解析与模型输出分离）展示理解深度。

---

## 6. The Process End to End: Stages, the Round Pool, Timeline and the No-AI Rule｜全流程：阶段、轮次池、时间线与禁用 AI 规则

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/the-process-end-to-end-stages-the-round-pool-timeline-and-the

**要点 / Key ideas**

- 例子：10 月 28 日收到邀请：11 月 2 日 16:00 UTC 的 30 分钟技术招聘官视频面 (technical-recruiter video chat)，评估细节稍后发送。你只有**一个已确认的预约**和很多未解问题。
- 临时流程图 (provisional process map) 每个阶段记录：形式与时长、时间与时区 (time zone)、工具与辅助权限、证据来源与日期、状态与下一步确认动作。**只把邀请或招聘方明确说的写成"已确认"**。空白日期本身是有用信息——提醒你去问，而不是用别人的时间表填上。

**公开报道的流程（2026-10-28 快照）**

| 来源 (Source) | 描述的流程 (Reported process) |
|---|---|
| 二手转述的官方指南 | 面试数量和形式根据候选人技能和岗位**个性化**；1–2 轮电话面，匹配则进 onsite（现场或虚拟） |
| 校招路径 (early-talent pathway) | HackerRank 挑战 → 30 分钟技术招聘官面 → 30–45 分钟技术面 → 两场 1 小时虚拟 onsite（learning + decomposition，内含行为与技术问题）→ 根据 onsite 反馈定制的招聘经理面 (hiring manager interview) → offer |
| 第三方指南示例 | 招聘官电话 → 技术筛选 → 三场 1 小时 onsite，从 decomposition / learning / coding / re-engineering / system design 五类中抽取 → 招聘经理面；全程常见 3–4 周 |
| 面经汇编（2026-09-23 更新） | 2026 年 8 月一例：20 分钟 decomposition + 20 分钟 coding 合并筛选；跨不同 FDSE 赛道 |

- 把五类技术轮当作**准备池 (preparation pool)**：都要准备，但不要假设你会有全部五轮或某个固定子集。行为题可能嵌入技术轮，所以行为准备要同步做。
- 邀请函细节少但对你的预约更权威；公开指南用来生成具体问题和准备类别。

<svg viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <rect x="0" y="0" width="760" height="200" fill="#fff"/>
  <text x="20" y="22" font-weight="bold" font-size="13">Reported FDSE loop (varies by candidate)｜公开报道的 FDSE 流程（因人而异）</text>
  <g>
    <rect x="15" y="45" width="105" height="55" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
    <text x="67" y="68" text-anchor="middle" font-weight="bold">Recruiter</text>
    <text x="67" y="86" text-anchor="middle">招聘官 30 min</text>
    <rect x="140" y="45" width="125" height="55" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
    <text x="202" y="64" text-anchor="middle" font-weight="bold">Screen 筛选</text>
    <text x="202" y="80" text-anchor="middle">HackerRank OA or</text>
    <text x="202" y="94" text-anchor="middle">live CodePair</text>
    <rect x="285" y="45" width="230" height="55" rx="8" fill="#fff4e5" stroke="#d98a1c"/>
    <text x="400" y="64" text-anchor="middle" font-weight="bold">Onsite 现场（2–3 × 60 min）</text>
    <text x="400" y="80" text-anchor="middle">pool: decomposition, learning,</text>
    <text x="400" y="94" text-anchor="middle">coding, re-engineering, system design</text>
    <rect x="535" y="45" width="110" height="55" rx="8" fill="#e8f7ee" stroke="#2e9b5a"/>
    <text x="590" y="68" text-anchor="middle" font-weight="bold">Hiring mgr</text>
    <text x="590" y="86" text-anchor="middle">招聘经理</text>
    <rect x="665" y="45" width="80" height="55" rx="8" fill="#e8f7ee" stroke="#2e9b5a"/>
    <text x="705" y="76" text-anchor="middle" font-weight="bold">Offer</text>
    <line x1="120" y1="72" x2="138" y2="72" stroke="#333" marker-end="url(#a6)"/>
    <line x1="265" y1="72" x2="283" y2="72" stroke="#333" marker-end="url(#a6)"/>
    <line x1="515" y1="72" x2="533" y2="72" stroke="#333" marker-end="url(#a6)"/>
    <line x1="645" y1="72" x2="663" y2="72" stroke="#333" marker-end="url(#a6)"/>
  </g>
  <rect x="285" y="120" width="230" height="30" rx="6" fill="#f5eefc" stroke="#8a4fd0" stroke-dasharray="4,3"/>
  <text x="400" y="140" text-anchor="middle">Behavioral questions embedded 行为题嵌入</text>
  <text x="20" y="180">Commonly reported total: 3–4 weeks (estimate, not a deadline)｜常见 3–4 周（估计，非承诺）</text>
  <defs><marker id="a6" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**三类时间分开 (Three kinds of timing)**：已确认预约（11/2 16:00 UTC）；个人目标（11/20 完成准备）；报道时长（3–4 周）。目标和估计都**不**确定 offer 日期，不要把"招聘官面 + 3–4 周"当日历截止。

**错误笔记审计**：①"我的 onsite 恰好三轮 1 小时"——把第三方示例当成自己的安排；②"招聘官面后 3–4 周就有 offer"——把估计当承诺；③"Palantir 用 AI 记录员，所以我也能用自己的助手"——把雇主转录 (transcription)当成候选人许可。

**禁用 AI 规则 (No-AI rule)**

- 现有资料**无法证实**存在公开的全公司禁令（某些指南写了绝对禁止，但缺雇主来源）。
- 保守默认：模拟和现场轮**不用任何候选人侧 AI**，直到明确允许。"没有政策证据"不等于许可。
- 逐项问而不是笼统问"能用工具吗"：AI 助手与生成式自动补全 (autocomplete)；普通编辑器补全、IDE、语言选项；浏览器、文档、个人笔记、外部帮助；现场轮与 take-home 分开的规则。
- Deployment Strategist 的 Build to Apply 岗位允许并鼓励在**构建提交作品时**用 AI——仅限那条路线那个活动。

**转录同意 (transcription consent) ≠ 候选人许可**：官方 US Gov FDSE 申请写到 Palantir "may use AI notetakers to transcribe conversations"，选择加入或退出不影响候选资格。主体是 Palantir，活动是转录。三栏分开：雇主转录同意、候选人辅助许可、无障碍安排 (accessibility arrangements)（需要什么、申请流程、批准、如何运作）。

**给招聘官的邮件模板（英文，可直接用）**

> Thank you. I have the 30-minute technical-recruiter video chat on November 2 at 16:00 UTC confirmed. Could you share the anticipated remaining round types and order, durations, formats, scheduling windows, response timing and deadlines? Please also confirm the video platform, coding platform and language options where applicable.
>
> What assistance is permitted separately for live rounds and any take-home work, including AI assistants, autocomplete, browsing, documentation and notes? I will assume no candidate AI assistance unless explicitly permitted.
>
> Separately, how is employer transcription consent handled, and whom should I contact to request and confirm an accessibility arrangement and its setup?

**只更新被回复确认的字段**：招聘官回复"11/5 15:00 UTC 60 分钟 live coding、浏览器编辑器、可用 Python、本场禁用候选人 AI，其他工具说明稍后；onsite 未定；无障碍找招聘官"。正确更新：确认这些筛选字段和无障碍联系人；其它工具权限、无障碍是否批准、onsite 数量、offer 日期都保持未解决；11/20 仍是个人目标；两条记录都保留。陷阱：**能力 ≠ 授权**——浏览器编辑器提供写代码的地方，不等于允许开别的标签页；知道找谁问无障碍 ≠ 已批准。

**面试怎么说 / How to say it**

> Q (recruiter): "Do you have any questions about the process?"
>
> "Yes, a few logistics questions. Which round types should I expect after the screen, and roughly in what order? For the coding screen, which platform and languages are supported? And for each round, what assistance is allowed: is it fully no-AI, and are documentation or personal notes okay? I'll default to no AI tools unless you tell me otherwise."
>
> 中文：问轮次类型/顺序、平台与语言、逐项辅助权限；主动表明默认不用 AI。

---

## 7. New Grad vs Experienced: How the Same Loop Is Judged Differently｜校招与社招：同一流程的不同评判

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/new-grad-vs-experienced-how-the-same-loop-is-judged-differently

**要点 / Key ideas**

- 同样的技术基础，不同的证据。**资历 (tenure) 本身不能证明**编码熟练度 (coding fluency)、生产责任、客户接触或学习能力。准备优先级应基于观察到的表现、与已确认流程的相关性、你能证实的证据。
- 二手转述的 Palantir 工程招聘指南五项能力 (five competencies)：写好代码 (Writing Good Code)、分析代码效率 (Analyzing the Efficiency of Code)、应对开放式问题 (Navigating Open-Ended Questions)、解决技术问题 (Solving Technical Problems)、在现有系统中工作 (Working Inside Existing Systems)。强调可运行实现、边界情况 (edge cases)、时间与空间复杂度 (time and space complexity)。
- 无论资历都要练：把思路变成可运行代码并检查正确性；讲清时空复杂度；沟通选择与权衡；读、调试、扩展别人写的代码。官方 FDSE 职位要求 "Strong coder" 和 "1+ years of relevant, post-college work experience"。没有证据表明校招/社招有不同的数字权重或通过线。

**资深候选人重点：三个术语 (Experienced track: three terms)**

| 术语 (Term) | 定义 (Definition) | 候选人 B 的例子 (Candidate B) | 局限 (Limit) |
|---|---|---|---|
| 持续负责 (Sustained ownership) | 跨时间的责任，包括变更、故障与跟进 | 维护导入服务 8 个月 | 不能证明**当前**限时编码熟练度 |
| 生产判断 (Production judgment) | 在运营约束下做决策 | 实现分阶段发布 (staged rollout) | 团队批准了部署；不是每个决策都是 B 的 |
| 客户影响 (Customer impact) | 用户/客户可观察到的变化 | 重试去重 (retry deduplication) 上线；同事做了监控面板 (monitoring dashboard) | 未测量客户节省时间 |

- 候选人 B：维护导入服务 8 个月，实现重试去重和分阶段发布；同事建了监控面板；团队批准部署。上线前 4 周重复导入事故 9 次，之后 4 周 2 次；未检查输入量和同期变更；未测量客户节省时间。B 的 35 分钟编码练习停在伪代码 (pseudocode)，没完成陌生库练习。
- **B 想说"减少客户工作量 78%"**：(9−2)/9 ≈ 77.8% 是**事故数**的变化，不能变成工作量、不能证明因果 (causation)、不能弥补未检查的输入量和同期变更。可以保留"9 → 2，两个 4 周窗口"及其局限。
- 候选人 A（校招，简述）：三人课程项目中实现去重，通过 18 个测试，队友发现重复 ID 后修改键规则并新增 4 个测试；限时练习失败两个重复输入用例。A 应聚焦实现、验证与学习，不要把项目包装成生产负责或客户节省。

**B 的六个 45 分钟块 (6 × 45 = 270 分钟)**

| 块 (Block) | 产出 (Artifact) |
|---|---|
| 1. 完成一次实现 | 从新题规格写出可运行代码+边界测试，不停在伪代码 |
| 2. 限时重复 | 又一个可运行解、正确性检查、时空分析；记录卡在哪里 |
| 3. 读陌生库 | 契约笔记 (contract note) + 一个验证易混淆行为的最小可运行调用 |
| 4. 扩展陌生代码 | 完成扩展+测试，说明文档或执行如何改变了最初理解 |
| 5. 追溯一个运营决策 | 重试去重、分阶段发布、维护、事故跟进；区分个人实现、同事面板、团队批准 |
| 6. 校验结果边界 | 保留 9→2 计数和 4 周窗口，明确记录未检查的输入量、同期变更、未测客户时间 |

捷径计划为什么失败：A 想把六块都用来排练项目讲述（"校招看潜力"）；B 想六块都讨论架构（"社招已经证明会写代码"）。正确修复：每人恢复 2 个实现块 + 2 个陌生系统块，剩下两块按各自证据补。**只有完成一次编码才能暴露你现在卡在哪里**。

- 练习包 D（社招）：维护内部报表工具 1 年，亲自实现 schema 迁移 (schema migration)和回滚测试 (rollback tests)；分析师同事收集了用户需求；无外部客户接触；最近限时实现未完成，陌生代码扩展通过 5 个测试。→ 优先级：限时实现 > 证据审计（迁移+回滚是 D 的，需求收集不是）> 陌生系统保持。不能说 D 个人收集了需求。

**面试怎么说 / How to say it**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 37 篇）。

---

## 8. Getting In: Resume, Referrals and the Build to Apply Track｜进门：简历、内推与 Build to Apply 通道

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/getting-in-resume-referrals-and-the-build-to-apply-track

**要点 / Key ideas**

- 反例简历句："Led an end-to-end scheduling platform that cut staff workload by 60%." 三个无支撑的说法：领导 (leadership)、端到端负责 (end-to-end ownership)、量化的工作量减少。
- 项目记录（四人排班项目）：个人实现 CSV 校验和冲突审核接口 (conflict-review endpoint)；个人决策：把无效行隔离待审 (quarantine) 而不是悄悄丢弃；写了 12 个测试（缺失 ID、日期格式错误、预约重叠）；队友做界面、另一队友记录导入时间；同一 200 行样本导入时间 15 分钟 → 6 分钟（各一次）；无生产部署、无工作量研究。

**可辩护的两条简历 (Defensible bullets)**

```text
- Implemented CSV validation and a conflict-review endpoint in a four-person scheduling project;
  quarantined invalid rows for review rather than silently discarding them.
- Wrote 12 validation tests covering missing IDs, malformed dates and overlapping bookings.
```

- (15−6)/15 = 60% 只描述两次样本导入时间差，**不能**证明人员工作量下降。要用就说："A teammate measured a 15-minute import before and a six-minute import after on the same 200-row sample, once each." —— 归属和条件比百分比重要。
- 简历背后保留支撑笔记：代码（指向实现）、决策（为什么保留无效行）、测试（12 个测试检查什么）、边界（界面归队友、计时的归属和局限）。好的简历条目可以以具体验证收尾，而不一定是业务指标。
- **贡献证据**和**申请通道资格 (application-channel eligibility)**是两项独立检查，一项强不能弥补另一项缺失。

**内推请求 (Referral request)**：给出准确职位、相关证据、关系背景，并且**容易拒绝**。

> Hi, we worked together on the scheduling project. I'm applying for the New York Forward Deployed Software Engineer vacancy; I've included my resume. My contribution was CSV validation and a conflict-review endpoint, plus 12 validation tests. Would you feel comfortable referring me, or sharing your view on fit? No pressure if you don't have enough context or aren't able to help. Thank you.

- 对不认识你工作的人：请对方简短谈谈对该职位的看法，而不是要求他暗示有一手了解。只分享你有权披露的内容。
- 内推不能替代资格，也不保证被考虑。

**Build to Apply 不是 FDSE 的另一条入口**

| 职位 (Vacancy) | 关键要求 (Key requirements) |
|---|---|
| New York — Forward Deployed Software Engineer（全职、hybrid） | 协作架构设计、定制应用、直接客户沟通、端到端执行 |
| Washington, D.C. — Deployment Strategist, Build to Apply - US Government（现场） | 出差 25–75%；"现有美国安全许可**或**有资格且愿意获取" |
| Colorado Springs — Deployment Strategist, Build to Apply - US Government（现场） | **现有** Top Secret 及以上许可；每周 4–5 天在客户现场 |

- 再强的 Foundry/AIP 演示也不改变广告的岗位和"现有许可"要求。目标是 FDSE 就走 FDSE 职位当前链接的表单，除非明确确认有替代通道。
- Build to Apply（华盛顿）提交清单：简历/CV + 项目；用 DevTier 账号（含 AIP）；工作流同时使用 Foundry 和 AIP；鼓励公开或虚构数据；**构建时允许并鼓励用 LLM/AI**；演示并解释选择的问题、方法、方案；5 分钟以内的**不公开 (unlisted) YouTube 视频**（不是 Short），没有视频不予考虑；开始构建后 7–10 天内提交；流程结束后删除视频。可能"加速考虑"，不承诺加速、面试或 offer。AI 许可只适用于构建项目。

**失败外联的修复**："Please refer me for any engineering role; I led a platform that reduced customer work by 60%, and I will use the expedited FDSE Build to Apply route because I am willing to get clearance." → 用两条有边界的简历、具体的内推请求、FDSE 路线决定替换。"愿意"不能满足 Colorado Springs 的现有 TS 要求。

**面试怎么说 / How to say it**（资深版简历条目示范）

> "Owned the ingestion and validation layer for a high-volume marketplace data pipeline; chose to quarantine malformed records for review instead of dropping them, and added contract tests for missing keys and duplicate events. Partnered with the UI team and SRE on rollout."
>
> 中文：资深简历同样遵循"我做了什么 + 一个设计决策 + 验证证据 + 合作者"，量化数据要能说清口径。

---

## 9. Answering "Why Palantir?" With Specific, Grounded Answers｜用具体、有依据的方式回答 "Why Palantir?"

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/answering-why-palantir-with-specific-grounded-answers

**要点 / Key ideas**

- 动机回答本身就应包含能回答追问"你实际做过什么让你想做这份工作？"的证据。
- 成就 (accomplishment) 说你做了什么；动机 (motivation) 还要说**是什么吸引你去做、接下来想追求什么**。
- 课程例子：食品分发原型（三人项目），和两位志愿协调员聊过捐赠与派送表格，候选人实现 CSV 核对 (reconciliation) + 保留未匹配物品 ID 的审核队列 (review queue)，写了 6 个测试；队友做界面、另一个准备样本数据；未部署、未测量改进、没用过 Foundry/AIP。最吸引他的是"追查记录分歧、决定协调员该审核什么"。
- 审核队列体现了一个**选择**：保留未解决的分歧让人去调查。罗列技术会掩盖这种偏好。
- 第三方指南把背景和动机列为招聘官电话话题，建议给出产品或领域相关的理由；但其"拒绝率"等说法不是官方标准。

**五种陈述类型分开 (Five statement types)**

| 类型 (Type) | 例子 (Example) |
|---|---|
| 个人偏好 (Personal preference) | "I enjoyed tracing record disagreements." |
| 有支撑的个人行动 (Supported personal action) | "I implemented the unmatched-ID review queue." |
| 有出处的公司说法 (Documented company claim) | "The posting describes platforms supporting data-driven decisions and operations." |
| 提议的应用 (Proposed application) | "I would explore using an operational application to present unresolved records." |
| 观察到的结果 (Observed outcome)（含证据局限） | "No delivery or workload improvement was measured." |

**公司证据（纽约 FDSE 职位）**：软件支持 "data-driven decisions and operations"；FDSE 与客户一起理解问题，用业务关键数据和 AI 架构构建方案；示例问题 "How can we analyze and adapt a global food supply chain to deliver life-saving aid on time?"；职责含架构设计、定制应用、直接客户沟通。——这是**广告中的问题**，不代表某客户用了某实现。

**为什么是 FDSE 而不是其他工程岗**：选出吸引你的职责组合（直接和用户理解模糊问题 + 做工程决策 + 实现可用应用）。**不要**贬低其他岗位（"普通 SWE 不接触用户"是错的）。

**反例审计**："Palantir is the leader in AI, its mission perfectly matches mine, and Foundry will eliminate food-delivery errors. I want FDSE because normal software engineers do not work with users." 三种偏差：选择偏差 (selection bias)——只挑食品供应例子就说使命完美契合；幸存者偏差 (survivorship bias)——只看匹配成功的记录就说能消除错误；近因偏差 (recency bias)——刚读的职位权重过高就宣称 AI 领导者。另外"其他工程师不接触用户"是错误对比。

- 检验法：把 "Palantir" 换成别的公司名，如果什么都不用改，说明公司特定的连接不够。目标是具体，不是证明别家都不行。
- 薪酬和声望可以是真实考虑，但不能单独解释为什么选这份工作；不必承诺终身忠诚。
- 证据很少时：如实说"这个组合吸引我，但我还没在客户工作中验证过这种偏好，想了解这个团队里 FDSE 的时间怎么分配"。
- 目标时长约 60–90 秒（准备目标，不是官方要求）。

**面试怎么说 / How to say it**

课程的校招示范答案（结构参考）：兴趣 → 具体项目与个人行动 → 喜欢的部分 → 职位中的具体细节 → 为什么是 FDSE → 诚实说明局限。

资深工程师版本（你的真实经历）：

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 37 篇）。

追问 / Follow-ups：

| 追问 (Follow-up) | 英文回答 (English answer) | 中文要点 |
|---|---|---|
| "What makes this a Palantir connection?" | "The posting frames the job as building customer-specific applications on operational data. That's the regulation-to-workflow work I've liked most, but closer to the user." | 引用职位原文 |
| "Why FDSE rather than a platform role?" | "I've done a lot of platform work. What I want now is to hear the operator's problem first-hand and also ship the fix." | 正面偏好，不贬低其他岗 |
| "Have you used the products?" | "Not hands-on. I've read the Ontology and AIP Logic docs, but I wouldn't claim product experience." | 诚实 |

---

## 10. Talking About Your Projects as a New Grad｜校招生如何讲项目（简述）

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/talking-about-your-projects-as-a-new-grad

**要点 / Key ideas**（校招部分简述；其中"反例 (counterexample)推翻规则"的方法对资深候选人同样适用）

- 项目讲述六要素顺序：问题与目标用户 (problem and intended user) → 个人贡献与合作者 (contribution and collaborators) → 关键决策与备选方案 (decision and alternative) → 验证与结果 (validation and result) → 学到什么与局限 (learning and limits)。先给约 90 秒概览，再按面试官追问展开。
- "我"用于能证实的个人动作，"我们"用于共同工作；区分**需求**（作业规定）和**机制**（你选择如何实现和测试）。
- 不要开口就说"只是个课程项目"——平实说明背景，然后讲工程。

**案例：设备预约冲突检测 (equipment-booking conflict detector)**

Problem (English): Given reservations `(id, device, start, end)` in UTC, flag every pair of reservations on the same device whose time ranges overlap, for a coordinator to review. Back-to-back reservations are allowed. Reject rows whose end is not later than their start. Do not auto-cancel.

```text
Input:
B1 D1 09:00-10:00
B2 D1 09:30-10:30
B3 D1 10:00-11:00
B4 D2 09:30-10:30
B5 D1 11:00-11:00

Output:
conflicts = [(B1, B2), (B2, B3)]
rejected  = [B5]
```

- 最初的规则"只在开始时间相同时标记"被反例 B1–B2 推翻（开始时间不同但重叠）。
- 区间 (interval) 为左闭右开 [start, end)。两条同设备预约重叠当且仅当 `a.start < b.end and b.start < a.end`。B1–B3：10:00 < 10:00 为假 → 相邻允许。B4 在 D2 → 不冲突。B5 长度为 0 → 比较前拒绝。
- 三个保护各对应一个需求：按设备分组 (same-device grouping) 防止不相关设备冲突；严格比较 (strict comparisons) 允许相邻；拒绝零长度区间 (zero-length rejection) 防止无意义比较。如果需求要求设备清洁时间，就需要周转缓冲 (turnaround buffer)，此时相邻不可接受。

Approach：按设备分组；每组按 start 排序；扫描时维护"仍在进行中"的预约（end > 当前 start），与之逐一配对。复杂度 (complexity) O(n log n + k)，k 为冲突对数量；空间 O(n)。

```python
from collections import defaultdict
from datetime import datetime


def find_conflicts(bookings):
    """bookings: list of (booking_id, device_id, start_iso, end_iso)."""
    rejected = []
    by_device = defaultdict(list)
    for booking_id, device_id, start_iso, end_iso in bookings:
        start = datetime.fromisoformat(start_iso.replace("Z", "+00:00"))
        end = datetime.fromisoformat(end_iso.replace("Z", "+00:00"))
        if end <= start:
            rejected.append(booking_id)
            continue
        by_device[device_id].append((start, end, booking_id))

    conflicts = []
    for device_id, items in by_device.items():
        items.sort()
        active = []  # bookings that may still overlap the current one
        for start, end, booking_id in items:
            # Half-open intervals: an active booking ending exactly at start is adjacent, not overlapping.
            active = [entry for entry in active if entry[1] > start]
            for _, _, other_id in active:
                conflicts.append((other_id, booking_id))
            active.append((start, end, booking_id))
    return conflicts, rejected
```

- 结果表述：6 个本地测试通过（分离、部分重叠、完全相同、相邻、不同设备同时间、零长度）；样本运行得到两对冲突和一条拒绝行。**不能**说"消除了重复预约"——未部署、未测量。
- 学习陈述范式："I initially checked only equal start times. The partial-overlap test exposed that mistake, so I replaced the rule with interval comparison. I learned to test the relationship the requirement describes, including its boundaries."

**面试怎么说 / How to say it**

> Q: "How do you know it helped?"
>
> "All six local tests passed, and the sample run flagged two conflict pairs and rejected one bad row. We never deployed it or measured coordinator outcomes, so I wouldn't claim it reduced double bookings."
>
> 中文：说观察到的结果和未验证的部分，不夸大。

---

## 11. Talking About Your Experience: Ownership, Impact and Customer Collaboration｜讲职业经历：负责、影响与客户协作（资深重点）

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/talking-about-your-experience-ownership-impact-and-customer

**要点 / Key ideas**

- 开场情境：发布交接时，负责报表修复的工程师**不能**按生产部署按钮——权限在客户的平台工程师手里。候选人要把变更准备好，并在上线后帮助运营使用。
- **负责 (Ownership)** = 把一项明确的责任贯穿决策、实现、协作和跟进 (follow-through)。实质性责任**不需要**独立完成、不受限的生产权限或对客户业务规则的决定权。
- 功能演示只讲新的校验函数；经历讲述还要讲：谁定义了"完整"、谁批准发布、用户如何从故障恢复、反馈后你改了什么。

**职责与权限分离 (Responsibility vs authority)**

| 角色 (Role) | 负责内容 (Responsibility) |
|---|---|
| 候选人 (Candidate) | 调查丢失记录、实现类别校验 (category validation) 和发布守卫 (publication guard)、写测试、准备发布与回滚说明 (release and rollback instructions)、4 个月每周复盘故障 |
| 客户运营负责人 (Customer operations lead) | 确认规则：未知类别的记录**不能悄悄消失** |
| 客户平台工程师 (Customer platform engineer) | 用自己的授权批准并执行生产发布 |
| 候选人 + 平台工程师（共同） | 校验失败时保留上一份完整报告 |
| 队友 (Teammate) | 构建监控面板 |

**缺陷与修复 (Defect and fix)**

- 旧报表通过类别查表过滤记录。21 条记录中 20 条类别已知，1 条类别 X9 不在批准映射 (approved mapping) 中 → 查表悄悄排除 X9，报告发布 20 条且无警告。
- 测验答案：阻止候选报告发布，写入 X9 异常，保留上一份完整报告并**明显标记为过期 (stale)、保留原时间stamp**。错误选项：把 X9 猜成默认类别（编造业务含义，工程师没有这个权限）；只发布 20 条（重复完整性失败）；删除旧报告并报成功。

修复步骤：
1. 发布前检查批次类别 vs 批准映射。
2. 写异常条目，标识未知类别 X9。
3. 阻止候选报告发布。
4. 保留上一份完整报告，标为 stale，保留原时间戳。
5. 等客户负责人提供批准的映射修正，再批准重跑 (approved rerun)。

**发布守卫 (publication guard)**：当必要条件不满足时，阻止候选输出成为已发布报告的检查。

<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <rect x="0" y="0" width="760" height="300" fill="#fff"/>
  <text x="20" y="22" font-weight="bold" font-size="13">Validation + publication guard (21-record batch)｜校验 + 发布守卫</text>
  <rect x="20" y="110" width="120" height="60" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="80" y="133" text-anchor="middle" font-weight="bold">Batch 批次</text>
  <text x="80" y="152" text-anchor="middle">20 known + 1 X9</text>
  <polygon points="250,100 320,140 250,180 180,140" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="250" y="137" text-anchor="middle">All categories</text>
  <text x="250" y="152" text-anchor="middle">approved?</text>
  <rect x="380" y="40" width="160" height="50" rx="8" fill="#e8f7ee" stroke="#2e9b5a"/>
  <text x="460" y="62" text-anchor="middle" font-weight="bold">Publish candidate</text>
  <text x="460" y="80" text-anchor="middle">发布新报告</text>
  <rect x="380" y="120" width="160" height="80" rx="8" fill="#fdecea" stroke="#b3261e"/>
  <text x="460" y="140" text-anchor="middle" font-weight="bold">Guard 守卫</text>
  <text x="460" y="158" text-anchor="middle">write X9 exception 写异常</text>
  <text x="460" y="174" text-anchor="middle">block publish 阻止发布</text>
  <text x="460" y="190" text-anchor="middle">keep old report: STALE</text>
  <rect x="590" y="120" width="155" height="80" rx="8" fill="#f5eefc" stroke="#8a4fd0"/>
  <text x="667" y="142" text-anchor="middle" font-weight="bold">Ops lead 运营负责人</text>
  <text x="667" y="160" text-anchor="middle">approves mapping fix</text>
  <text x="667" y="178" text-anchor="middle">→ approved rerun 重跑</text>
  <line x1="140" y1="140" x2="178" y2="140" stroke="#333" marker-end="url(#a11)"/>
  <line x1="285" y1="120" x2="378" y2="68" stroke="#333" marker-end="url(#a11)"/>
  <text x="320" y="88" font-size="11">yes</text>
  <line x1="320" y1="150" x2="378" y2="160" stroke="#333" marker-end="url(#a11)"/>
  <text x="335" y="172" font-size="11">no (X9)</text>
  <line x1="540" y1="160" x2="588" y2="160" stroke="#333" marker-end="url(#a11)"/>
  <rect x="20" y="230" width="725" height="50" rx="8" fill="#fafafa" stroke="#999" stroke-dasharray="4,3"/>
  <text x="30" y="250">Release authority: customer platform engineer approves + executes in change window.</text>
  <text x="30" y="268">发布权限：客户平台工程师在变更窗口内批准并执行；候选人准备测试包、回滚步骤、运行手册 (runbook)。</text>
  <defs><marker id="a11" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**在客户控制下交付 (Delivery within customer controls)**：每次发布需要客户操作员 + 批准的变更窗口 (change window)。候选人准备可重复的测试包 (test packet)、回滚流程 (rollback procedure)、运行手册 (runbook)；平台工程师审核并执行；生产数据不离开客户环境。**借用操作员账号 = 绕过访问控制**，不是"足智多谋"。把控制视为交付需求，而不是把客户描述成障碍。

**三类证据分开 (Three kinds of evidence)**

| 类型 (Type) | 内容 (Content) | 能证明 / 不能证明 (Supports / not) |
|---|---|---|
| 实现验证 (Implementation validation) | 测试：全部已知 → 发布；X9 → 异常并阻止；失败时旧报告不变、保留原时间戳、显示 stale | 指定行为 |
| 运营观察 (Operational observation) | 不完整报告：发布前 20 次中 6 次 → 发布后 20 次中 1 次；未检查数据源构成和同期变更 (concurrent changes) | 有边界的前后对比；**不能**证明全部因果 (causation) |
| 客户工作证据 (Customer-work evidence) | 交接时运营负责人按 runbook 自行识别 X9、获取批准的映射修正、请求重跑 | 观察到的恢复流程；不代表广泛采用或量化节省 |

**改变的做法 (Changed practice)**：第一版守卫保留了旧报告但没足够显示其"旧"；运营负责人指出读者可能误以为是新报告 → 加 stale 状态、保留原时间戳并在交接时验证。习惯："I now agree failure-state visibility with users before release, including how retained output shows its age."

**保密 (Confidentiality)**：只用获准讨论的信息；去掉客户名不等于获准披露记录、架构、指标、事故。不能披露就说"I cannot disclose those counts. I can describe the permitted validation and handover evidence." **绝不编造替代数字**。

**面试怎么说 / How to say it**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 37 篇）。

五个追问 / Five probes：

| 追问 (Probe) | 英文回答 (English answer) | 中文要点 |
|---|---|---|
| Why not build your own pipeline? | "We had a launch date and limited resources, and Risk already ran the capability. The cost was a shared batch cadence, which I accepted explicitly." | 取舍 |
| What would you do differently? | "Involve the ETL owner during requirement breakdown, so scope, dependencies and milestones are agreed jointly." | 真实反思 |

---

## 12. Handling Questions on Palantir's Mission, Government Work and Critics｜应对使命、政府业务与批评类问题

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/handling-questions-on-palantirs-mission-government-work-and

**要点 / Key ideas**

- 一个系统可以严格执行所有配置的权限，同时支持一个你会拒绝的目的。回答要把公开证据、工程保障和个人判断连起来，又不假装解决了你没核实的事实。
- 公开面经显示"对使命和客户工作的动机"经常出现 → 值得准备，但没有"标准答案立场"。

**五个要素分开 (Five elements)**

| 要素 (Element) | 含义 (Meaning) |
|---|---|
| 公司说法 (Company claims) | Palantir 如何描述其目的和工作 |
| 外部批评 (External criticism) | 批评者指控、论证或建议什么（带日期和出处） |
| 技术保障 (Technical safeguards) | 具体控制实际限制或揭示了什么 |
| 个人边界 (Personal boundaries) | 你会接受、质疑或拒绝的工作及原因 |
| 未解决问题 (Unresolved questions) | 评估具体岗位还需要什么信息 |

**公开证据**

- 公司描述：US Gov FDSE 职位称软件用于数据驱动的决策与运营；例子：研发救命药物、预测供应链中断、寻找失踪儿童；工程师直接与客户合作处理关键运营，学会理解方案的成本与后果 ("understand the costs and consequences of its solution")。这是公司描述，不是每个部署都有益的独立证据。
- 带日期的批评：国际特赦组织 (Amnesty International) 2020-09-28 发布：Palantir 与 ICE 相关的合同有较高风险助长人权侵犯 (human-rights violations)，公司未证明有足够的人权尽职调查 (human-rights due diligence)。
- 有争议的回应（经 Amnesty 转述）：Palantir 称合同是与国土安全调查局 (Homeland Security Investigations, HSI，ICE 的刑事调查部门) 签的，软件不支持执法与遣返行动处 (Enforcement and Removal Operations, ERO) 的民事移民执法；Amnesty 对此有异议。
- Amnesty 的建议：做人权尽职调查、公开技术与保障措施、考虑暂停支持民事移民执法的活动——这些是**建议**，不是公司现行政策。

**权限和日志为什么不够 (Why controls don't settle it)**

- 访问控制 (access controls) 限制**谁**能执行允许的操作；审计日志 (audit logs) 让记录的活动**可检查**。授权的搜索仍可能使用不当数据、服务有害目的或促成不公正决定；记录本身不能阻止这些后果。
- 人权尽职调查 = 识别和评估潜在危害、采取行动预防或缓解、检查并沟通处理情况。控制可以**支持**它，但仍需有人评估允许的目的是否可接受、发现危害后怎么办。
- 测验答案："访问受限、搜索可检查，但目的和后果仍需评估"。错误：所有允许的目的都合乎伦理；Amnesty 的担忧被推翻；日志能保证有害使用会被阻止。
- 好的追问：允许哪些目的？谁可能受影响？评估过哪些可预见的危害？数据为什么合理？有什么监督和救济 (oversight and recourse)？

<svg viewBox="0 0 760 180" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <rect x="0" y="0" width="760" height="180" fill="#fff"/>
  <text x="20" y="22" font-weight="bold" font-size="13">Technical controls support, but don't decide, ethical acceptability｜技术控制支持而非决定伦理可接受性</text>
  <rect x="20" y="50" width="160" height="60" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="100" y="74" text-anchor="middle" font-weight="bold">Access control</text>
  <text x="100" y="92" text-anchor="middle">who? 谁能操作</text>
  <rect x="20" y="115" width="160" height="50" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="100" y="137" text-anchor="middle" font-weight="bold">Audit log</text>
  <text x="100" y="154" text-anchor="middle">inspectable 可追查</text>
  <rect x="300" y="60" width="200" height="90" rx="8" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="400" y="84" text-anchor="middle" font-weight="bold">Still open 仍需评估</text>
  <text x="400" y="104" text-anchor="middle">purpose 目的</text>
  <text x="400" y="120" text-anchor="middle">affected people 受影响者</text>
  <text x="400" y="136" text-anchor="middle">harm, oversight, recourse</text>
  <rect x="580" y="75" width="160" height="60" rx="8" fill="#e8f7ee" stroke="#2e9b5a"/>
  <text x="660" y="99" text-anchor="middle" font-weight="bold">Your judgment</text>
  <text x="660" y="117" text-anchor="middle">个人边界 boundary</text>
  <line x1="180" y1="80" x2="298" y2="95" stroke="#333" marker-end="url(#a12)"/>
  <line x1="180" y1="140" x2="298" y2="120" stroke="#333" marker-end="url(#a12)"/>
  <line x1="500" y1="105" x2="578" y2="105" stroke="#333" marker-end="url(#a12)"/>
  <defs><marker id="a12" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**推理错误诊断 (Reasoning diagnoses)**

| 陈述 (Statement) | 诊断 (Diagnosis) |
|---|---|
| "I would work on anything because the customer decides." | 回避个人判断 (avoidance of personal judgment) |
| "Amnesty argued in 2020 that ICE-related work posed human-rights risks." | 合理：有日期、有出处的批评 |
| "The software has access controls, so the government work is ethical." | 从技术跳到伦理 (technical-to-ethical leap) |
| "Amnesty proved Palantir broke the law, but that was in 2020, so it must be fixed now." | 无依据的法律结论 + 无依据的"时间已解决"假设 |

**面试怎么说 / How to say it**

Q: "How do you think about Palantir's government work and its critics?"（约 90 秒；结构：吸引点 → 有出处的证据 → 局限 → 边界 → 具体问题）

> "I'm attracted to engineering alongside users on consequential operations. Palantir's government FDSE posting describes work like forecasting supply-chain disruptions and locating missing children, and it emphasizes understanding a solution's costs and consequences.
>
> I also take Amnesty International's September 2020 criticism seriously. Amnesty argued that ICE-related contracts posed human-rights risks and that Palantir hadn't demonstrated adequate due diligence. Palantir's response, as reported there, was that its contracts were with HSI and didn't support ERO's civil immigration enforcement; Amnesty disputed that.
>
> That material doesn't resolve the dispute for me or tell me what today's safeguards are. I'd assess the proposed use, the people affected and the review process. Access controls and audit logs matter, but they don't make an authorized purpose acceptable. I would decline work I judged foreseeably harmful to vulnerable people.
>
> So my question is: how are proposed uses reviewed for potential harm, and how can an engineer raise a concern about an approved use?"
>
> 中文：吸引点+职位原文 → 带日期的批评与公司回应 → 承认资料不能定论 → 控制≠可接受 → 个人边界 → 向招聘方提具体问题。（边界是示例讲者的，你可以持不同立场，但要真实。）

追问 / Follow-ups：

| 追问 (Follow-up) | 英文回答 (English answer) | 中文要点 |
|---|---|---|
| "Access is restricted and searches are logged." | "Those controls address unauthorized access and make searches inspectable. I'd still want to understand the permitted purposes, the consequences for affected people, and how a concern triggers review. A logged, authorized search could still enable a use I'd decline." | 接受前提，指出剩余不确定性 |
| "Does that prove the company acted unlawfully?" | "What I've read doesn't establish a legal conclusion. Amnesty raised human-rights concerns and challenged the company's account; that's the concern I'm referring to." | 不夸大批评 |
| "The customer owns the decision. Would you build it?" | "Customer authority matters, and I'm still responsible for my own contribution. I'd need to understand the actual use and how it's reviewed. I'd decline a use I judged foreseeably harmful to vulnerable people." | 压力下保持边界；不承诺存在内部升级或调岗渠道 |
| "Are you comfortable working on government deployments?" | "Yes, conditionally. I'm comfortable with government work where the purpose and the review process are clear, and I'd want to know how this team assesses harm before an assignment. What wouldn't change with more information is that I won't build something I believe is foreseeably harmful to vulnerable people." | 说出真实立场、一个可能改变判断的未知事实、一个不会变的边界 |

---

## 13. Screen Formats and Time Strategy: HackerRank OA vs Live CodePair｜筛选形式与时间策略：HackerRank OA vs 实时 CodePair

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/screen-formats-and-time-strategy-hackerrank-oa-vs-live-codepair

**要点 / Key ideas**

- 例子邀请："75-minute independent HackerRank assessment; Python 3.12; no candidate-side AI." 没说题目数量。诱人但错误的计划："Coding、SQL、API 各 30 分钟"——已经超过 75 分钟，而且邀请没承诺这些类别。

**公开报道的筛选形式**

| 来源 (Source) | 描述 (Description) |
|---|---|
| 第三方指南 A | 实时 CodePair 或 Karat 面试；或独立 HackerRank 评估，含 coding、SQL、API |
| 第三方指南 B | 约 60 分钟实时（45 技术 + 15 行为），或 90 分钟 coding + SQL + REST API 评估 |
| 面经站（自称证据不全） | 组合式 coding + decomposition 筛选；无法证实存在统一的 SQL 评估 |
| 二手转述官方指南 | 面试数量和形式因人因岗而异；工程电话面可能用 HackerRank 或 Google Docs |

测验——可以进入计划的：总时长 75 分钟；不用候选人 AI；Python 3.12；使用 HackerRank；按独立评估准备（因为邀请**明确写了** independent）。不可以：假设能先看全部题并自由回看；仅凭 HackerRank 名字推断独立模式；按恰好三题分块；因为只禁 AI 就认为文档可用；把 SQL 当必考。

**给招聘方的问题模板**

> Could you confirm whether there are separate task timers; whether I can inspect, switch between and revisit tasks; and which language/runtime choices apply to each task? If task count or categories can be disclosed, that would help me prepare. Please also confirm permitted references and local tools, navigation and submission rules, and how to report a technical failure.

**独立 OA 的 75 分钟分配**（确认单一计时器、可自由切换回看、最后需点 Submit；两题：记录校验 + 分组汇总）

| 分钟 (Minutes) | 活动 (Activity) |
|---|---|
| 0–5 | 检查 (Inspect)：读两题契约、了解提交界面、识别输出要求和边界情况 (edge cases) |
| 5–30 | 记录校验 (record validation)：最简契约正确版本，边写边查 |
| 30–60 | 分组汇总 (grouped totals)：基线实现、运行检查、修正失败 |
| 60–70 | 最终复查 (final review) |
| 70–75 | 提交验证 (submission verification)：点 Submit 并确认完成状态 |

- 时间盒 (timebox) = 预先设定的活动上限，到点检查进度并决定继续、简化或转移。不均等的分配来自你对题目的检查，不是假设的评分权重。
- 不要假设能回到某题、也不要假设未完成能得部分分。
- **第 25 分钟还没有可运行基线**（前 20 分钟在追求更快算法）→ 用剩下 5 分钟写最简契约正确版本并检查；到第 30 分钟记录未解决问题，转向分组汇总。**先有可运行基线，再做可选优化 (baseline before optimization)**。

**实时 CodePair（60 分钟：45 技术 + 15 行为）建议议程**（服从面试官安排）

<svg viewBox="0 0 760 130" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <rect x="0" y="0" width="760" height="130" fill="#fff"/>
  <text x="20" y="22" font-weight="bold" font-size="13">60-min live CodePair agenda｜60 分钟实时编码议程</text>
  <rect x="20" y="40" width="60" height="50" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="50" y="62" text-anchor="middle">0–5</text>
  <text x="50" y="80" text-anchor="middle" font-size="11">Clarify</text>
  <rect x="80" y="40" width="240" height="50" fill="#e8f7ee" stroke="#2e9b5a"/>
  <text x="200" y="62" text-anchor="middle">5–25 Baseline 基线实现</text>
  <text x="200" y="80" text-anchor="middle" font-size="11">runnable + checks 可运行+检查</text>
  <rect x="320" y="40" width="120" height="50" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="380" y="62" text-anchor="middle">25–35 Tests</text>
  <text x="380" y="80" text-anchor="middle" font-size="11">测试与修复</text>
  <rect x="440" y="40" width="120" height="50" fill="#f5eefc" stroke="#8a4fd0"/>
  <text x="500" y="62" text-anchor="middle">35–45 Refine</text>
  <text x="500" y="80" text-anchor="middle" font-size="11">复杂度+交接</text>
  <rect x="560" y="40" width="180" height="50" fill="#fdecea" stroke="#b3261e"/>
  <text x="650" y="62" text-anchor="middle">45–60 Behavioral</text>
  <text x="650" y="80" text-anchor="middle" font-size="11">行为面（保留）</text>
  <text x="20" y="115" font-size="11">Timeboxes become coordination points with the interviewer, not silent task switches.｜时间盒是与面试官协调的节点，而不是默默切换。</text>
</svg>

- 新邀请替换旧邀请后，保留：Python 3.12、禁 AI；改变：模式、平台、时长、行为段；旧的导航/回看/提交规则不再适用。
- 实时面关键变化：面试官可以澄清优先级或改方向 → 时间盒变成**协调点**。
- 沟通"决策点"而不是每次按键：契约、方案、进度、阻塞 (blockers)、**实际**测试结果。"It works"但没运行过 = 掩盖不确定性。

**面试怎么说 / How to say it**

| 时机 (Moment) | 英文说法 (What to say) | 中文要点 |
|---|---|---|
| 开始编码前 | "I understand the required output as one result for each accepted input record. I'll implement the straightforward approach first and check the stated boundary cases before optimizing." | 复述契约+先基线 |
| 第 20 分钟落后 | "The baseline isn't running yet. I can finish the simpler approach and test it before considering optimization. Does that fit the remaining technical time?" | 主动协调 |
| 具体阻塞 | "The empty-input case raises an exception. I checked the iteration path; next I'll fix the initialization and rerun that case." | 现象+已尝试+下一步 |
| 报告结果 | "The ordinary case passed; the empty-input case still fails." | 准确报告 |

- 50 分钟 Karat（35 技术 + 15 行为）练习：不能因为某指南说 90 分钟三段式就预留 SQL/API 时间；邀请没说允许文档就要问；第 18 分钟基线未测试时不能默默继续优化——要说出来并协调。

---

## 14. The Implementation Coding Problem｜实现类编码题

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/the-implementation-coding-problem

**要点 / Key ideas**

- 实现类题目的难点在**歧义 (ambiguity)**：两个各要 3 支笔的请求、库存只有 5 支——"满足这些请求"可能是第二个给 2 支（部分满足 (partial fulfillment)）、两个都对照原始 5 支检查、还是只满足第一个？先把歧义变成精确契约，才能在时间盒内写出小而完整的实现。
- 可运行基线 (working baseline) = 满足**完整**约定契约的最简实现。
- 函数契约 (function contract)：接受的输入、要求的输出、顺序、状态变化、边界行为。要问：请求是按顺序处理吗？可以部分满足吗？函数能修改传入的库存吗？
- 二手转述的 Palantir 编码指南：把算法变成可运行代码、考虑边界情况 (edge cases)、解释时空复杂度。先把干净的解跑通，再优化效率。
- 夹具 (fixture) = 检查用的具体输入数据；可执行规格 (executable specification) = 用独立推导的预期结果检查实际行为。
- 判别性夹具 (discriminating fixture)：让一个看似合理的错误实现产生与正确实现**不同**的结果。5 支要 3 支是 happy path，无法区分 `>` 和 `>=`。

**题目 / Problem (English)**

Implement `fulfill_requests(stock, requests)`. `stock` maps SKU to a nonnegative integer quantity. `requests` is an ordered list of `(request_id, sku, quantity)` with positive quantities and unique IDs. Process requests in order against the stock remaining after earlier fulfillments. Fulfill the whole quantity when current stock is sufficient (including equality); otherwise leave stock unchanged. Return one `(request_id, status)` per request, in order, where status is `fulfilled`, `insufficient_stock` or `unknown_sku`. Do not mutate the caller's `stock`. Inputs are guaranteed valid.

```text
Input:
stock = {"pen": 5, "book": 2}
requests = [("R1","pen",3), ("R2","pen",3), ("R3","pen",2),
            ("R4","map",1), ("R5","book",2), ("R6","pen",1)]

Output:
[("R1","fulfilled"), ("R2","insufficient_stock"), ("R3","fulfilled"),
 ("R4","unknown_sku"), ("R5","fulfilled"), ("R6","insufficient_stock")]
stock is still {"pen": 5, "book": 2}
```

**推导预期 (Derive before running)**：R1：5≥3 → 剩 2，fulfilled；R2：2<3 → 拒绝，**仍剩 2**；R3：2≥2（相等成功）→ 剩 0；R4：map 不存在 → unknown_sku；R5：2≥2 → 书剩 0；R6：0<1 → 拒绝。R3 同时检验"拒绝不扣库存"和"恰好相等可成功"；R5 独立检验相等。

测验答案：R2 被拒绝，剩 2 支；R3 成功。错误选项：R2 拿走剩下 2 支（部分满足）；拒绝时也扣减导致 −1；都对照原始 5 支。

**Approach**：复制库存为 `remaining`；按顺序遍历：未知 SKU → unknown_sku；库存不足 → insufficient_stock（不扣减）；否则扣减并 fulfilled。

```python
def fulfill_requests(stock, requests):
    remaining = stock.copy()
    results = []
    for request_id, sku, quantity in requests:
        if sku not in remaining:
            results.append((request_id, "unknown_sku"))
        elif remaining[sku] < quantity:
            results.append((request_id, "insufficient_stock"))
        else:
            remaining[sku] -= quantity
            results.append((request_id, "fulfilled"))
    return results
```

- 浅拷贝 (shallow copy) 足够：值是不可变整数，没有共享的嵌套可变对象。不需要类、解析器、数据库或网络客户端。

**循环不变式 (Loop invariant)**：每次迭代开始前，`remaining` = 初始库存 − 之前**已满足**请求的数量；`results` 恰好包含之前每个请求的一条有序结果。初始成立（无扣减、无结果）；未知/不足分支只追加结果不改库存；满足分支先确认足够再扣减（保证非负）；每个分支恰好追加一次（保持数量和顺序）。

**测试 (Tests)**

```python
import unittest

from inventory_requests import fulfill_requests


class FulfillRequestsTests(unittest.TestCase):
    def test_ordered_sequence_and_nonmutation(self):
        stock = {"pen": 5, "book": 2}
        before = stock.copy()
        requests = [
            ("R1", "pen", 3), ("R2", "pen", 3),
            ("R3", "pen", 2), ("R4", "map", 1),
            ("R5", "book", 2), ("R6", "pen", 1),
        ]
        expected = [
            ("R1", "fulfilled"),
            ("R2", "insufficient_stock"),
            ("R3", "fulfilled"),
            ("R4", "unknown_sku"),
            ("R5", "fulfilled"),
            ("R6", "insufficient_stock"),
        ]
        self.assertEqual(fulfill_requests(stock, requests), expected)
        self.assertEqual(stock, before)

    def test_boundaries(self):
        cases = [
            ({"pen": 5}, [], []),                                       # empty requests
            ({}, [("X", "pen", 1)], [("X", "unknown_sku")]),            # empty stock
            ({"pen": 0}, [("Z", "pen", 1)], [("Z", "insufficient_stock")]),  # zero stock
            ({"pen": 2}, [("E", "pen", 2)], [("E", "fulfilled")]),      # exact stock
        ]
        for stock, requests, expected in cases:
            with self.subTest(stock=stock, requests=requests):
                before = stock.copy()
                self.assertEqual(fulfill_requests(stock, requests), expected)
                self.assertEqual(stock, before)


if __name__ == "__main__":
    unittest.main()
```

运行：`python3.12 -m unittest -v test_inventory_requests`。

**变异测试 (Mutation testing)**：把 `remaining[sku] < quantity` 改成 `<=`（等价于要求严格大于才满足），六请求结果变为：

```text
[('R1','fulfilled'), ('R2','insufficient_stock'), ('R3','insufficient_stock'),
 ('R4','unknown_sku'), ('R5','insufficient_stock'), ('R6','fulfilled')]
```

R3、R5 错误拒绝相等；R3 没扣减导致 R6 错误成功（连锁状态变化 (cascading state change)）。独立的 exact-stock 用例能直接定位边界错误。另一个常见 bug：拒绝时也扣减 → 笔 5 → 2 → −1，R3 错误失败。

- 回归测试 (regression test)：修复后保留已确立的预期。**修实现，不改断言**——改断言去迎合错误结果等于抹掉契约。

**复杂度 (Complexity)**：m = 库存条目数，n = 请求数。复制 O(m)；每个请求期望 O(1) 字典操作 + 均摊 (amortized) O(1) 追加 → O(n)；总期望时间 **O(m + n)**。辅助空间 (auxiliary space) O(m)（工作库存）+ O(n) 输出。字典操作是**期望** O(1) 而非最坏情况保证。只说 O(n) 漏掉了初始化；去掉拷贝能省空间但违反"不修改输入"契约。

**练习题答案**：stock = {badge: 4, lanyard: 0}；A(badge,5) → insufficient_stock（4<5，仍 4）；B(badge,4) → fulfilled（剩 0）；C(badge,1) → insufficient_stock；D(lanyard,1) → insufficient_stock（零库存）；E(sticker,1) → unknown_sku。

**面试怎么说 / How to say it**

> "Before I code, I want to pin down three rules: requests are processed in order against the remaining stock, a request is all-or-nothing and equality counts as enough, and I shouldn't mutate the caller's map. I'll copy the stock, loop once, and append exactly one result per request. The invariant is that `remaining` reflects only fulfilled requests so far. It's O(m + n) expected time because of the copy plus one pass. I'll test the six-request sequence, then an exact-stock case on its own, because that's what catches a less-than versus less-than-or-equal bug."
>
> 中文：先确认顺序、全有或全无、相等算满足、不修改输入；讲不变式、复杂度 O(m+n)，并说明为什么单独测试相等边界。

> Handoff: "I ran the full sequence test and the four boundary cases; all passed. I didn't test very large inputs, and passing these doesn't prove correctness for every input."
>
> 中文：交接时只报告实际运行过的检查。

---

## 15. Algorithm Problems in the Screen: The Medium-to-Hard Patterns｜筛选中的中高难度算法模式

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/algorithm-problems-in-the-screen-the-medium-to-hard-patterns

**要点 / Key ideas**

- 统计 20 万个有符号读数中和为目标值的连续段，与按先决条件排序任务，需要完全不同的推理——前者依赖**前缀和之间的关系**，后者依赖**有向边 (directed edges)**。选择其不变式 (invariant) 由契约推出的算法，再用约束判断额外机制是否值得。公司标签不能替代推理。
- 公开准备资料：Aced 强调实用的 map 和字符串题、淡化图论；Scaler 包含字符串和图；一位候选人 2026 年 5 月 onsite（非筛选）遇到依赖排序；2024 年 11 月一位 FDSE 候选人在 CodePair 筛选遇到中等哈希表题。**无法**据此得出可靠频率排名。
- 每题的纪律：① 给出正确基线 (baseline) 并指出它违反了哪个约束；② 说出维护的状态和不变式；③ 定义复杂度变量；④ 选一个能把你的解和看似合理的错误区分开的测试。

**模式总览 (Pattern map)**

| 模式 (Pattern) | 维护的状态 (Maintained state) | 基线 → 优化 (Baseline → optimized) | 判别性测试 (Discriminating test) |
|---|---|---|---|
| 哈希表计数 (Frequency map) | 字符 → 次数 | O(n²) → 期望 O(n) | 用 set 会丢失重复次数 (multiplicity) |
| 双指针 (Two pointers) | left/right 下标 | O(n²) → O(n) | left >= right 时停止，不能复用同一位置 |
| 固定窗口 (Fixed window) | 滚动和 (rolling sum) | O(n·w) → O(n) | 全负数：最大值从第一个窗口初始化，不是 0 |
| 可变窗口 (Variable window) | 窗口内字符计数 | O(n²) → 期望 O(n) | "abba"：要 while 收缩，不是只移一步 |
| 前缀和 + 哈希 (Prefix sum + map) | 之前边界的前缀频率 | O(n²) → 期望 O(n) | [0,0] target 0 → 3；set 给 2；先插入后查询给 5 |
| 拓扑排序 (Topological sort, Kahn) | 邻接表 (adjacency list) + 剩余入度 | O(V(V+E)) → O(V+E) | 加 D→A 形成环；菱形图 (diamond graph)不是环 |
| 区间合并 (Interval merge) | 当前组 start + 最大 end | O(n²) → O(n log n) | 嵌套区间要 max(end)；相邻 [1,4),[4,6) 不合并 |
| 有界堆 (Bounded heap) | 大小 ≤ k 的最小堆 (min-heap) | O(n log n) 排序 → O(n log k) | 同分时比较到不可比较的 payload |

**关键陷阱：和阈值窗口的错误收缩 (Invalid contraction)**：[4, −1]，target 3，"因为 4 > 3 就立即收缩"会丢掉唯一合法段 [4, −1]。负数可以让和变小，所以"扩展区间不会降低和"的假设不成立 → 有负数时不能用滑动窗口，要用前缀和。

<svg viewBox="0 0 760 210" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <rect x="0" y="0" width="760" height="210" fill="#fff"/>
  <text x="20" y="22" font-weight="bold" font-size="13">Prefix sums: segment [l, r) sum = P[r] − P[l]｜前缀和：区间和 = 两个边界前缀之差</text>
  <text x="20" y="55">values</text>
  <g font-size="13">
    <rect x="110" y="40" width="60" height="26" fill="#eef4ff" stroke="#3b6fd8"/><text x="140" y="58" text-anchor="middle">1</text>
    <rect x="170" y="40" width="60" height="26" fill="#eef4ff" stroke="#3b6fd8"/><text x="200" y="58" text-anchor="middle">2</text>
    <rect x="230" y="40" width="60" height="26" fill="#eef4ff" stroke="#3b6fd8"/><text x="260" y="58" text-anchor="middle">-1</text>
    <rect x="290" y="40" width="60" height="26" fill="#eef4ff" stroke="#3b6fd8"/><text x="320" y="58" text-anchor="middle">1</text>
    <rect x="350" y="40" width="60" height="26" fill="#eef4ff" stroke="#3b6fd8"/><text x="380" y="58" text-anchor="middle">2</text>
  </g>
  <text x="20" y="100">prefix P</text>
  <g font-size="13">
    <text x="110" y="100" text-anchor="middle">0</text>
    <text x="170" y="100" text-anchor="middle">1</text>
    <text x="230" y="100" text-anchor="middle">3</text>
    <text x="290" y="100" text-anchor="middle">2</text>
    <text x="350" y="100" text-anchor="middle">3</text>
    <text x="410" y="100" text-anchor="middle">5</text>
  </g>
  <path d="M110,112 Q170,140 230,112" fill="none" stroke="#2e9b5a"/>
  <text x="170" y="150" text-anchor="middle" fill="#2e9b5a">[0,2): 3−0</text>
  <path d="M110,112 Q230,175 350,112" fill="none" stroke="#d98a1c"/>
  <text x="230" y="185" text-anchor="middle" fill="#d98a1c">[0,4): 3−0</text>
  <path d="M230,112 Q320,150 410,112" fill="none" stroke="#8a4fd0"/>
  <text x="350" y="160" text-anchor="middle" fill="#8a4fd0">[2,5): 5−2</text>
  <text x="460" y="60">target = 3</text>
  <text x="460" y="85">need P[l] = P[r] − target</text>
  <text x="460" y="110">start map {0: 1}</text>
  <text x="460" y="135">query BEFORE insert</text>
  <text x="460" y="160">先查询后插入 → 排除空段</text>
  <text x="460" y="185">answer = 3</text>
</svg>

### 15.1 First unique character index｜第一个只出现一次的字符

Problem: Given a string (case-sensitive Python code points, no normalization), return the index of the first character that occurs exactly once, or `None` if none.

```text
Input:  "swiss"
Output: 1        # 'w'
Input:  "aabb"
Output: None
```

Approach：先计数，再按原顺序扫描。set 会丢失次数；不保留原顺序会选错。复杂度：期望 O(n) 时间，O(u) 辅助空间（u = 不同字符数）。基线：对每个字符重新计数 O(n²)。

```python
from collections import Counter


def first_unique_index(text):
    counts = Counter(text)
    for index, ch in enumerate(text):
        if counts[ch] == 1:
            return index
    return None
```

### 15.2 Pair sum in a sorted array｜有序数组两数之和

Problem: Given an ascending integer list, return whether two **distinct positions** sum to `target`.

```text
Input:  values = [-4, -1, 0, 3, 5, 8], target = 7
Output: True     # -1 + 8 (sums inspected: 4, then 7)
```

Approach：左右指针。和太小 → 当前 left 与任何更左的 right 配对都太小 → left++ 安全；和太大 → right-- 安全；left >= right 时停止（一个元素不能当两个）。O(n) 时间，O(1) 空间。未排序输入需另定契约或先排序 O(n log n)（若需原下标要保留）。

```python
def sorted_pair_exists(values, target):
    left, right = 0, len(values) - 1
    while left < right:
        total = values[left] + values[right]
        if total == target:
            return True
        if total < target:
            left += 1
        else:
            right -= 1
    return False
```

### 15.3 Maximum fixed-width window sum｜固定宽度窗口最大和

Problem: Return the maximum sum of any contiguous window of exactly `width` elements. Require `1 <= width <= len(values)`; raise `ValueError` otherwise. Values may be negative.

```text
Input:  values = [4, -2, 3, 1], width = 2
Output: 4        # window sums: 2, 1, 4
```

Approach：用第一个窗口初始化和与最大值（不是 0，否则全负数出错）；每次加入新值、减去离开值。O(n) 时间，O(1) 辅助空间（不切片）。

```python
def max_fixed_window_sum(values, width):
    if width < 1 or width > len(values):
        raise ValueError("width must satisfy 1 <= width <= len(values)")
    window = 0
    for i in range(width):
        window += values[i]
    best = window
    for right in range(width, len(values)):
        window += values[right] - values[right - width]
        if window > best:
            best = window
    return best
```

### 15.4 Longest substring without repeated characters｜无重复字符的最长子串

Problem: Return the length of the longest substring with no repeated characters (case-sensitive code points). Empty string returns 0.

```text
Input:  "abba"
Output: 2
```

Approach：维护窗口内字符计数；右扩；若新字符重复，**while** 从左收缩直到其计数为 1；记录最大合法长度。每个指针最多前进 n 次 → 期望 O(n) 时间，O(u) 空间。基线：从每个起点重建 set，O(n²)。

```python
def longest_unique_length(text):
    counts = {}
    left = 0
    best = 0
    for right, ch in enumerate(text):
        counts[ch] = counts.get(ch, 0) + 1
        while counts[ch] > 1:
            counts[text[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

### 15.5 Count target-sum segments (signed values)｜和为目标值的连续子数组个数

Problem: Given signed integers (n up to 200,000) and `target`, count nonempty contiguous segments whose sum equals `target`. Return one integer.

```text
Input:  values = [1, 2, -1, 1, 2], target = 3
Output: 3        # [0,2), [0,4), [2,5)
Input:  values = [0, 0], target = 0
Output: 3
Input:  values = [2, -2, 2, -2], target = 0
Output: 4        # [0,2), [0,4), [1,3), [2,4)
```

基线（O(n²) 时间，n=200,000 时检查 20,000,100,000 个段；O(1) 空间）：

```python
def count_target_segments_baseline(values, target):
    answer = 0
    for left in range(len(values)):
        total = 0
        for right in range(left, len(values)):
            total += values[right]
            if total == target:
                answer += 1
    return answer
```

Approach：P[0]=0，P[i+1]=P[i]+values[i]；区间 [l,r) 的和 = P[r]−P[l]；目标方程 P[l] = P[r] − target。在每个右边界查询之前边界中该前缀的出现次数。用 `{0: 1}` 初始化，让从下标 0 开始的段被计入。**先查询再插入**当前前缀（否则会计入空段）。不变式：查询时 map 恰好包含所有更早边界的前缀频率。期望 O(n) 时间，O(n) 辅助空间。

Trace（[1, 2, −1, 1, 2]，target 3）：前缀 1 需 −2 → 0；前缀 3 需 0 → 1（答 1）；前缀 2 需 −1 → 0；前缀 3 需 0 → 1（答 2）；前缀 5 需 2 → 1（答 3）。

```python
def count_target_segments(values, target):
    prefix = 0
    answer = 0
    frequencies = {0: 1}
    for value in values:
        prefix += value
        answer += frequencies.get(prefix - target, 0)
        frequencies[prefix] = frequencies.get(prefix, 0) + 1
    return answer
```

判别性测试：[0, 0] target 0 → 正确 3；用 set 得 2（丢失相同前缀的不同起点）；先插入后查询得 5（多算两个空段）。[2,−2,2,−2] 验证：前缀 [0,2,0,2,0]，三个 0 → C(3,2)=3 对，两个 2 → 1 对，共 4。

### 15.6 Dependency order (topological sort)｜依赖排序（拓扑排序）

Problem: Given vertices (in supplied order) and directed edges `(prerequisite, dependent)`, return an order where every prerequisite comes first. Include isolated vertices. Raise `ValueError` if a cycle exists.

```text
Input:  vertices = [A, B, C, D, E], edges = [(A,C), (B,C), (C,D)]
Output: [A, B, E, C, D]
Input:  same plus edge (D,A)
Output: ValueError (cycle)   # only B and E can be emitted
```

Approach（Kahn 算法）：为**每个**顶点（含孤立的 E）建邻接表和入度 (indegree)；入度为 0 的按顺序入队；出队一个就输出，并把出边邻居入度减 1，减到 0 入队；输出少于全部顶点 → 有环。不变式：队列中每个任务在未处理任务中没有未满足的先决条件。O(V+E) 时间，O(V+E) 辅助空间 + O(V) 输出。基线：反复扫描所有剩余任务找就绪的，O(V(V+E))。

```python
from collections import deque


def dependency_order(vertices, edges):
    adjacency = {vertex: [] for vertex in vertices}
    indegree = {vertex: 0 for vertex in vertices}
    for prerequisite, dependent in edges:
        adjacency[prerequisite].append(dependent)
        indegree[dependent] += 1
    queue = deque(vertex for vertex in vertices if indegree[vertex] == 0)
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in adjacency[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != len(vertices):
        raise ValueError("cycle detected")
    return order
```

- 重复发现 ≠ 环：菱形图 A→B, A→C, B→D, C→D 共享后代 D，但无环。DFS 判环需三状态：未访问 (unseen)、活跃 (active)、已完成 (finished)；指向 active 的边证明有环，指向 finished 的不一定。
- 验证结果：检查每个顶点出现且每条边的先后关系满足，**不要**和某一个任意合法序列比较。

### 15.7 Merge overlapping intervals (half-open)｜合并重叠区间（左闭右开）

Problem: Merge positive-length half-open intervals that actually overlap; touching endpoints stay separate. Return fresh lists; do not mutate input.

```text
Input:  [[8, 10], [2, 3], [4, 6], [1, 4]]
Output: [[1, 4], [4, 6], [8, 10]]
```

Approach：按 (start, end) 排序副本；维护当前组的 start 和最大 end（frontier）；下一个 start < frontier_end 则合并，end 取 max（处理嵌套 [2,3)）；否则开新组。4 < 4 为假 → [4,6) 独立。排序保证后面的 start 不会回到已完成组之前。O(n log n) 时间（扫描 O(n)），O(n) 辅助 + O(n) 输出。若需求要合并相邻覆盖，用 `<=`。需要来源身份时保留 ID。

```python
def merge_intervals(intervals):
    ordered = sorted((start, end) for start, end in intervals)
    merged = []
    for start, end in ordered:
        if merged and start < merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

### 15.8 Top-k with tie-breaking (bounded heap)｜带平局规则的 Top-k（有界堆）

Problem: Given `(payload, score)` records in arrival order and `k >= 0`, return up to k records in descending quality; on equal score, earlier arrival wins. Payloads may be unorderable.

```text
Input:  records = [("A", 8), ("B", 10), ("C", 10), ("D", 7)], k = 2
Output: [("B", 10), ("C", 10)]
```

Approach：质量 = (score, −arrival_index)。Python heapq 是最小堆：保持最多 k 个元素，根是保留中最差的；新记录质量更好才替换根。堆元素 `(score, -arrival_index, arrival_index, payload)`——唯一的 arrival 下标在 payload 之前，保证同分时不会比较 payload。k=0 立即返回；k=1 线性扫描。选择 O(n log k) 时间、O(k) 堆空间；有序输出再加 O(k log k)。k > n 时用 h = min(k, n) 表示。小数据量一次 O(n log n) 排序是更简单的基线；流式 (streaming)、内存受限时用堆。

```python
from heapq import heappush, heapreplace


def top_k(records, k):
    if k == 0:
        return []
    if k == 1:
        best = None
        best_quality = None
        for arrival_index, (payload, score) in enumerate(records):
            quality = (score, -arrival_index)
            if best_quality is None or quality > best_quality:
                best_quality = quality
                best = (payload, score)
        return [] if best is None else [best]
    heap = []
    for arrival_index, (payload, score) in enumerate(records):
        entry = (score, -arrival_index, arrival_index, payload)
        if len(heap) < k:
            heappush(heap, entry)
        elif (score, -arrival_index) > (heap[0][0], heap[0][1]):
            heapreplace(heap, entry)
    heap.sort(key=lambda item: (item[0], item[1]), reverse=True)
    return [(item[3], item[0]) for item in heap]
```

Trace：A(8)、B(10) 入堆，根是 A，质量 (8, 0)；C(10) 质量 (10, −2) > (8, 0) → 替换 A；此时根是 C (10, −2)（同分时 C 到得晚，质量更差）；D(7) 质量 (7, −3) 不优于根 → 不入。输出按质量降序：B、C。

- 回溯 (backtracking) 和动态规划 (dynamic programming) 作为扩展准备，不是公司题频预测。

**面试怎么说 / How to say it**

> "The values can be negative, so a sliding window doesn't work: extending a segment can make its sum smaller, so I can't safely shrink when the sum is too big. Instead I'll use prefix sums: a segment from l to r sums to target exactly when P[l] equals P[r] minus target. I keep a hash map of how many earlier boundaries had each prefix, seeded with zero once, and I query before inserting so I never count an empty segment. That's expected O(n) time and O(n) space. I'll test [0, 0] with target 0; the answer should be 3, and that case catches both the set bug and the insert-order bug."
>
> 中文：先说明为什么滑窗失效（有负数），再讲前缀和方程、map 初始化 {0:1}、先查后插、复杂度和判别性测试。

---

## 16. The SQL Question｜SQL 题

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/the-sql-question

**要点 / Key ideas**

- 开场：North 在季度内只有 2 个订单，但配送报表算出 6 个——SQL 跑通了，但把每个订单连接到它的配送历史时把被计数的事实**放大**了（连接扇出 (join fan-out)）。核心原则：**先确定行粒度 (row grain)，再算指标**。
- 公开资料把 SQL 连接和聚合 (aggregation)列为可能考点；一份指南提到 orders/customers/deliveries 主题、区域损失。但无法证明有统一的 SQL 评估或必考窗口函数——确认你自己的形式。
- 粒度 (grain)：一行代表什么。主键 (primary key) 唯一标识一行；外键 (foreign key) 关联另一表的行；关系基数 (cardinality，这里是一对多 one-to-many) 预测连接会产生多少组合。

**题目 / Problem (English)**

For each customer region, report Q3 2026 `order_count`, `late_count` (late-delivered orders), `unknown_count` (unknown delivery), `late_loss_cents` (loss of late orders, counted once per order), and `late_share` = late orders / all quarter orders (NULL for a zero-order region). Rules:

- Quarter membership by `placed_at`: include `2026-07-01T00:00:00Z`, exclude `2026-10-01T00:00:00Z`.
- Region comes from `customers`; keep every region, even with no quarter orders.
- Delivery classification uses the **latest eligible update** per order: eligible means `event_at IS NOT NULL`; latest by `event_at`, ties broken by larger `update_id`. Do not filter by status before ranking.
- Late = selected status `delivered` AND `delivered_at > promised_at` (equality is on time).
- Unknown = an actual order with no selected update, a non-delivered selected status, or a NULL `delivered_at`.

Schema (PostgreSQL 16):

```sql
CREATE TABLE customers (customer_id text PRIMARY KEY, name text NOT NULL, region text NOT NULL);
CREATE TABLE orders (order_id text PRIMARY KEY, customer_id text NOT NULL REFERENCES customers(customer_id),
  placed_at timestamptz NOT NULL, promised_at timestamptz NOT NULL,
  loss_cents bigint NOT NULL CHECK (loss_cents >= 0));
CREATE TABLE delivery_updates (update_id bigint PRIMARY KEY, order_id text NOT NULL REFERENCES orders(order_id),
  event_at timestamptz, status text NOT NULL, delivered_at timestamptz);
```

```text
Input:
customers: C1 Alex North | C2 Alex East | C3 Robin South
orders:
  O1 C1 placed 2026-07-01T09:00Z promised 2026-07-02T12:00Z loss 100
  O2 C1 placed 2026-08-01T09:00Z promised 2026-08-02T12:00Z loss 100
  O3 C2 placed 2026-09-01T09:00Z promised 2026-09-02T12:00Z loss 50
  O4 C1 placed 2026-10-01T00:00Z promised 2026-10-02T12:00Z loss 900   (outside Q3)
delivery_updates:
  10 O1 event 2026-07-01T10:00Z in_transit  delivered_at NULL
  11 O1 event 2026-07-03T10:00Z delivered   delivered_at 2026-07-02T11:00Z
  12 O1 event 2026-07-03T10:00Z delivered   delivered_at 2026-07-02T13:00Z
  13 O2 event 2026-08-01T10:00Z in_transit  delivered_at NULL
  14 O2 event 2026-08-02T12:00Z delivered   delivered_at 2026-08-02T11:00Z
  15 O2 event NULL              delivered   delivered_at 2026-08-02T13:00Z

Output:
region | order_count | late_count | unknown_count | late_loss_cents | late_share
East   | 1           | 0          | 1             | 0               | 0
North  | 2           | 1          | 0             | 100             | 0.5
South  | 0           | 0          | 0             | 0               | NULL
```

（重复的名字 Alex 说明不能用名字代替 customer_id。）

**错误的粒度 (Incorrect grain)**：North 季度订单直接连接历史表得到 6 行；每个订单的 100 分出现 3 次 → `COUNT(*)` = 6，`SUM(loss_cents)` = 600（应为订单级 200）。修复的第一步：把历史**先缩减到每个订单至多一行**，然后再聚合。

<svg viewBox="0 0 760 240" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <rect x="0" y="0" width="760" height="240" fill="#fff"/>
  <text x="20" y="22" font-weight="bold" font-size="13">Fix grain before aggregation｜先修粒度，再聚合</text>
  <rect x="20" y="45" width="150" height="60" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="95" y="68" text-anchor="middle" font-weight="bold">delivery_updates</text>
  <text x="95" y="86" text-anchor="middle">many per order 每单多行</text>
  <rect x="200" y="45" width="170" height="60" rx="8" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="285" y="64" text-anchor="middle" font-weight="bold">ROW_NUMBER()</text>
  <text x="285" y="80" text-anchor="middle" font-size="11">PARTITION BY order_id</text>
  <text x="285" y="95" text-anchor="middle" font-size="11">event_at DESC, update_id DESC</text>
  <rect x="400" y="45" width="150" height="60" rx="8" fill="#e8f7ee" stroke="#2e9b5a"/>
  <text x="475" y="68" text-anchor="middle" font-weight="bold">latest_updates</text>
  <text x="475" y="86" text-anchor="middle">≤ 1 per order 每单≤1行</text>
  <rect x="20" y="140" width="150" height="60" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="95" y="163" text-anchor="middle" font-weight="bold">customers</text>
  <text x="95" y="181" text-anchor="middle">all regions 全部区域</text>
  <rect x="200" y="140" width="170" height="60" rx="8" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="285" y="160" text-anchor="middle" font-weight="bold">LEFT JOIN orders</text>
  <text x="285" y="178" text-anchor="middle" font-size="11">quarter filter in ON</text>
  <text x="285" y="192" text-anchor="middle" font-size="11">季度条件放在 ON</text>
  <rect x="400" y="140" width="150" height="60" rx="8" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="475" y="163" text-anchor="middle" font-weight="bold">LEFT JOIN latest</text>
  <text x="475" y="181" text-anchor="middle">no fan-out 无扇出</text>
  <rect x="590" y="140" width="150" height="60" rx="8" fill="#f5eefc" stroke="#8a4fd0"/>
  <text x="665" y="160" text-anchor="middle" font-weight="bold">GROUP BY region</text>
  <text x="665" y="178" text-anchor="middle" font-size="11">COUNT(o.order_id)</text>
  <text x="665" y="192" text-anchor="middle" font-size="11">NULLIF(order_count, 0)</text>
  <line x1="170" y1="75" x2="198" y2="75" stroke="#333" marker-end="url(#a16)"/>
  <line x1="370" y1="75" x2="398" y2="75" stroke="#333" marker-end="url(#a16)"/>
  <line x1="475" y1="105" x2="475" y2="138" stroke="#333" marker-end="url(#a16)"/>
  <line x1="170" y1="170" x2="198" y2="170" stroke="#333" marker-end="url(#a16)"/>
  <line x1="370" y1="170" x2="398" y2="170" stroke="#333" marker-end="url(#a16)"/>
  <line x1="550" y1="170" x2="588" y2="170" stroke="#333" marker-end="url(#a16)"/>
  <text x="20" y="225" font-size="11">Invariant: before aggregation, each actual quarter order carries its loss at most once.｜聚合前每个季度订单的损失最多出现一次。</text>
  <defs><marker id="a16" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**选最新完整行 (Latest complete row)**

- "最新"按 `event_at`，不是到达顺序；`event_at` 为 NULL 的更新无法证明时间先后 → 排除。相同 `event_at` 时本题明确选更大的 `update_id`（ID 本身不代表时间顺序，这是约定的平局规则 (tie-breaking rule)）。
- 窗口函数 (window function)：跨相关行计算但**保留**输入行。`OVER` 定义窗口，`PARTITION BY order_id` 让每个订单独立，`ROW_NUMBER()` 按窗口排序给出不同位置。
- O1：11 和 12 平局 → 12 胜（delivered_at 13:00）；O2：15 的 event_at 为 NULL → 不合格，14 胜（11:00）；O3 无历史；O4 在 10/1 下单 → 不在 Q3。测验答案：只剩 O1/12 和 O2/14。
- PostgreSQL 中降序时 NULL 默认排在**最前**（除非 NULLS LAST）——这里先排除再排名，规则更明确。
- "完整行"= 所有保留字段来自同一条源行。**不要**在排名前过滤 `status = 'delivered'`：之后的非 delivered 更新仍应决定当前分类。
- 行号不能在同一层 WHERE 中过滤，必须用外层查询或 CTE (common table expression)。

**连接与 NULL (Joins and NULL)**

- INNER JOIN 只保留匹配组合；LEFT JOIN 保留未匹配的左行，右侧填 NULL。
- 从 customers 出发 LEFT JOIN 季度订单，**季度条件放在 ON 里**——放在 WHERE 会因为 South 的 NULL 扩展行比较结果为 unknown 而把 South 删掉。
- NULL = 缺失/未知，不是 0 或空串；与 NULL 比较一般得 unknown，WHERE 只保留 true。用 `IS NULL` 而不是 `= NULL`；只有替代值符合业务含义时才用 COALESCE。
- 再 LEFT JOIN latest_updates（每单至多一行 → 不会放大）。不要在 WHERE 里加右表状态过滤，否则丢掉计算 unknown 所需的缺失历史。
- `COUNT(*)` 计数行（含外连接占位行）；`COUNT(o.order_id)` 只计非 NULL 订单。SUM/AVG 忽略 NULL，空集上的 SUM 为 NULL。

**完整解答 (Full solution)**

```sql
WITH ranked_updates AS (
    SELECT du.*,
           ROW_NUMBER() OVER (
               PARTITION BY order_id
               ORDER BY event_at DESC, update_id DESC
           ) AS rn
    FROM delivery_updates AS du
    WHERE event_at IS NOT NULL
), latest_updates AS (
    SELECT update_id, order_id, event_at, status, delivered_at
    FROM ranked_updates
    WHERE rn = 1
), regional_metrics AS (
    SELECT c.region,
           COUNT(o.order_id) AS order_count,
           SUM(CASE WHEN lu.status = 'delivered'
                     AND lu.delivered_at > o.promised_at
                    THEN 1 ELSE 0 END) AS late_count,
           SUM(CASE WHEN o.order_id IS NOT NULL
                     AND (lu.update_id IS NULL
                          OR lu.status <> 'delivered'
                          OR lu.delivered_at IS NULL)
                    THEN 1 ELSE 0 END) AS unknown_count,
           SUM(CASE WHEN lu.status = 'delivered'
                     AND lu.delivered_at > o.promised_at
                    THEN o.loss_cents ELSE 0 END) AS late_loss_cents
    FROM customers AS c
    LEFT JOIN orders AS o
           ON o.customer_id = c.customer_id
          AND o.placed_at >= TIMESTAMPTZ '2026-07-01T00:00:00Z'
          AND o.placed_at <  TIMESTAMPTZ '2026-10-01T00:00:00Z'
    LEFT JOIN latest_updates AS lu ON lu.order_id = o.order_id
    GROUP BY c.region
)
SELECT region, order_count, late_count, unknown_count, late_loss_cents,
       late_count::numeric / NULLIF(order_count, 0) AS late_share
FROM regional_metrics
ORDER BY region;
```

- `o.order_id IS NOT NULL` 守卫防止 South 的占位行被算成 unknown 订单。
- `::numeric` 防止整数除法 (integer division)截断；`NULLIF(order_count, 0)` 把零分母 (zero denominator)变 NULL 而不是报错。
- 结果解释：North O1 晚一小时（13:00 > 12:00）；O2 准时；East O3 无选中更新 → unknown；South 占位行 → 全 0、share NULL。
- 整体占比 = 总晚到 / 总订单 = 1/3。**不要**平均各区域占比（区域订单量不同且 AVG 忽略 NULL）。

**窗口函数注释 (Window annotations)**——替换最后的 SELECT，保留 CTE：

```sql
SELECT region, late_loss_cents,
       SUM(late_loss_cents) OVER () AS total_late_loss_cents,
       RANK()       OVER (ORDER BY late_loss_cents DESC) AS loss_rank,
       DENSE_RANK() OVER (ORDER BY late_loss_cents DESC) AS dense_loss_rank,
       ROW_NUMBER() OVER (ORDER BY late_loss_cents DESC, region) AS position,
       SUM(late_loss_cents) OVER (
           ORDER BY late_loss_cents DESC, region
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS cumulative_late_loss_cents
FROM regional_metrics
ORDER BY late_loss_cents DESC, region;
```

```text
Output:
region | late_loss_cents | total | loss_rank | dense_loss_rank | position | cumulative
North  | 100             | 100   | 1         | 1               | 1        | 100
East   | 0               | 100   | 2         | 2               | 2        | 100
South  | 0               | 100   | 2         | 2               | 3        | 100
```

- RANK 平局后跳号，DENSE_RANK 不跳（第四行更低值：RANK=4，DENSE_RANK=3）。窗口内 ORDER BY 控制计算，最终 ORDER BY 控制显示。
- PostgreSQL 16 中带 ORDER BY 且无 frame 的聚合窗口默认 `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`，**包含同值行 (peers)**：`COUNT(*) OVER (ORDER BY late_loss_cents DESC)` 得 1, 3, 3；显式 `ROWS` + region 平局键得 1, 2, 3。

**看似合理但错误的修复 (Plausible but wrong repairs)**

| 修复 (Repair) | 为什么错 (Why it fails) |
|---|---|
| 直接连接历史表 | 6 行而非 2 行，count 6、loss 600 |
| `COUNT(DISTINCT order_id)` | 修好了计数，但其他聚合仍被放大 |
| `SUM(DISTINCT loss_cents)` | 得 100：把两个**合法**的 100 分订单事实合并了 |
| `MAX(event_at)` 再连回 | O1 的 11 和 12 都匹配最大值 → 返回两行；没有平局规则 |
| 分别取 `MAX(status)`、`MAX(delivered_at)` | 拼出从未在同一源行共存的值 |
| LEFT JOIN 后在 WHERE 过滤季度 | South 的 NULL 扩展行被删，区域消失 |

修复的是查询的**粒度和总体 (grain and population)**，而不是用 DISTINCT 掩盖症状。判别性夹具：相同时间戳暴露 MAX 回连；相同订单损失暴露 SUM(DISTINCT)；South 暴露放错位置的日期过滤。

**练习题答案（新夹具）**：customers C8 Morgan West、C9 Casey North、C10 Taylor South；X1(C8, loss 80)、X2(C8, loss 20)、X3(C9, loss 30)；更新 201/202 平局（X1），203 event NULL（X2），X3 无更新。选中：只有 X1/202（delivered_at 13:00 > promised 12:00 → 晚到）。

```text
region | order_count | late_count | unknown_count | late_loss_cents | late_share | total_late_loss_cents
North  | 1           | 0          | 1             | 0               | 0          | 80
South  | 0           | 0          | 0             | 0               | NULL       | 80
West   | 2           | 1          | 1             | 80              | 0.5        | 80
```

X2 已知的 delivered_at 不能弥补其未知的 event_at（资格与分类分离）。

**面试怎么说 / How to say it**

> "Before I write any joins, let me fix the grain. Orders are one row per order, but delivery updates are many per order, so if I join directly I'll repeat each order's loss once per update. I'll first reduce history to the latest eligible row per order with ROW_NUMBER, partitioned by order and ordered by event time then update ID as a tie-breaker. Then I start from customers so every region survives, left-join quarter orders with the date filter in the ON clause, and left-join the one-row-per-order history. I'll count order IDs, not rows, and use NULLIF for the share so a zero-order region gives NULL instead of a division error."
>
> 中文：先讲粒度和扇出，再讲 ROW_NUMBER 去重与平局规则、LEFT JOIN 与 ON 过滤、COUNT 列而非 COUNT(*)、NULLIF 防除零。

---

## 17. The Paginated REST API Aggregation Task｜分页 REST API 聚合题

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/the-paginated-rest-api-aggregation-task

**要点 / Key ideas**

- `GET /adjustments` 分页返回记录。要求：固定一周内更新的**唯一**调整记录，按区域汇总数量和金额。第一页算出的"看起来合理"的总数只是**临时的 (provisional)**。只有在所需一致性保证 (consistency guarantees)下取回并校验了**每一页**，才能返回精确聚合。
- 公开资料把分页 JSON 获取+聚合列为可能的筛选内容；一份面经提到按最近更新过滤分页记录并讨论故障。端点和夹具为课程自编。

**题目 / Problem (English)**

Call `GET /adjustments` (first request without parameters; continuations send `cursor` and `snapshot`). Every successful response is `{"snapshot": str, "records": [...], "next_cursor": str | null}`; the server documents that a snapshot binds continuations to one immutable view. Group eligible unique adjustments by `region` into `count` and `amount_cents`, only for regions with eligible records. The interval is frozen before retrieval: `[2026-10-21T00:00:00Z, 2026-10-28T00:00:00Z)`. Identity is `id`: ignore repeats whose required fields are identical after timestamp normalization; reject conflicting versions. Retry only timeouts and 429/502/503/504 (3 attempts, 5 s timeout, waits 1 s and 2 s). Any unrecoverable retrieval, validation or consistency failure raises; **never return a partial aggregate**.

Record validation: `id`, `region` nonempty strings; `amount_cents` nonnegative int (not bool); `updated_at` ISO 8601 with explicit offset (Z allowed). Ignore extra fields; reject missing fields, wrong types, malformed JSON and offset-free timestamps.

```text
Input (all pages carry snapshot "s7"):
page {}   : A North 120 2026-10-21T00:00:00Z | C South 999 2026-10-20T23:59:59Z   next "c2"
page c2   : A North 120 2026-10-21T00:00:00Z (exact repeat) | B North 80 2026-10-27T12:00:00Z   next "c3"
page c3   : D South 50 2026-10-28T00:00:00Z | E South 70 2026-10-25T00:00:00+02:00   next null

Requests: {}, {cursor: c2, snapshot: s7}, {cursor: c3, snapshot: s7}

Output:
{"North": {"count": 2, "amount_cents": 200}, "South": {"count": 1, "amount_cents": 70}}
```

- A 在下界（包含）→ 计入；C 太早；重复 A 不加；B 计入；D 恰在上界（排除）；E 归一化为 2026-10-24T22:00:00Z → 计入。C 和 D 不产生 South 分组。

**三层检查 (Three checks)**：HTTP 状态（只接受 200）→ JSON 语法解析 → 应用层校验（字段与业务规则）。静默跳过畸形记录 (malformed records) = 改变被计数的总体。`{"snapshot":"s7","records":[],"next_cursor":"c3"}` 是合法的**空页但仍需继续**。

**游标规则 (Cursor rules)**

- 游标 (cursor) 是**不透明 (opaque)** 的续取令牌：原样传回，不解析、不递增。从第一页捕获 snapshot，之后每个请求都带上它和上一页的 `next_cursor`；每页响应必须保持同一 snapshot。
- 只有 `next_cursor: null` 才停止。空 `records` 不代表结束。
- 两个保护：① 记录已请求的游标，**在发出前**拒绝重复的逻辑游标（同一请求的瞬时重试允许）；② 默认最多 100 个成功页（可配置），第 100 页仍有续取 → 报不完整。
- 编号页 API 有不同契约，按其文档的页范围和元数据处理。
- 测验答案：请求为 `[{}, {"cursor":"c2","snapshot":"s7"}]`，空的首页之后**不能**返回最终聚合。错误：只发一个请求就返回空聚合；续取时漏掉 snapshot。

**遍历不变式 (Traversal invariant)**：已存储的 identity 描述已成功处理页中经过校验的记录；总计中每个合格的已存 identity 恰好计一次。终止前总计只是内部临时状态。**即使记录不在时间区间内也要存储其规范负载**（region、cents、归一化时刻），以便检测后续冲突重复。

<svg viewBox="0 0 760 270" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <rect x="0" y="0" width="760" height="270" fill="#fff"/>
  <text x="20" y="22" font-weight="bold" font-size="13">Snapshot-bound cursor traversal｜绑定快照的游标遍历</text>
  <rect x="20" y="45" width="130" height="50" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="85" y="66" text-anchor="middle" font-weight="bold">Build params</text>
  <text x="85" y="84" text-anchor="middle" font-size="11">{} or cursor+snapshot</text>
  <rect x="180" y="45" width="140" height="50" rx="8" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="250" y="64" text-anchor="middle" font-weight="bold">fetch_page</text>
  <text x="250" y="82" text-anchor="middle" font-size="11">≤3 attempts, retry 429/5xx</text>
  <rect x="350" y="45" width="140" height="50" rx="8" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="420" y="64" text-anchor="middle" font-weight="bold">validate_page</text>
  <text x="420" y="82" text-anchor="middle" font-size="11">JSON + fields + tz 校验</text>
  <rect x="520" y="45" width="220" height="50" rx="8" fill="#e8f7ee" stroke="#2e9b5a"/>
  <text x="630" y="64" text-anchor="middle" font-weight="bold">snapshot same? dedup by id</text>
  <text x="630" y="82" text-anchor="middle" font-size="11">conflict → raise; in window → add</text>
  <polygon points="630,120 700,150 630,180 560,150" fill="#f5eefc" stroke="#8a4fd0"/>
  <text x="630" y="147" text-anchor="middle">next_cursor</text>
  <text x="630" y="162" text-anchor="middle">null?</text>
  <rect x="580" y="205" width="160" height="45" rx="8" fill="#e8f7ee" stroke="#2e9b5a"/>
  <text x="660" y="232" text-anchor="middle" font-weight="bold">Return totals 返回</text>
  <rect x="300" y="125" width="200" height="50" rx="8" fill="#fafafa" stroke="#333"/>
  <text x="400" y="146" text-anchor="middle">repeated cursor / page cap?</text>
  <text x="400" y="163" text-anchor="middle" font-size="11">重复游标/页数上限 → raise</text>
  <rect x="20" y="205" width="260" height="45" rx="8" fill="#fdecea" stroke="#b3261e"/>
  <text x="150" y="224" text-anchor="middle" font-weight="bold">Any failure → raise, no partial</text>
  <text x="150" y="241" text-anchor="middle" font-size="11">任何失败都抛错，不返回部分结果</text>
  <line x1="150" y1="70" x2="178" y2="70" stroke="#333" marker-end="url(#a17)"/>
  <line x1="320" y1="70" x2="348" y2="70" stroke="#333" marker-end="url(#a17)"/>
  <line x1="490" y1="70" x2="518" y2="70" stroke="#333" marker-end="url(#a17)"/>
  <line x1="630" y1="95" x2="630" y2="118" stroke="#333" marker-end="url(#a17)"/>
  <line x1="630" y1="180" x2="650" y2="203" stroke="#333" marker-end="url(#a17)"/>
  <text x="648" y="196" font-size="11">yes</text>
  <line x1="560" y1="150" x2="502" y2="150" stroke="#333" marker-end="url(#a17)"/>
  <text x="520" y="143" font-size="11">no</text>
  <path d="M300,150 L85,150 L85,97" fill="none" stroke="#333" marker-end="url(#a17)"/>
  <defs><marker id="a17" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**重试策略 (Retry policy)**

- 只重试传输超时和 429、502、503、504；每页 3 次、每次超时 5 秒；第二、三次前注入等待 1 秒、2 秒。
- **不**重试 400/401/403 等其他状态、畸形 JSON、校验失败、快照冲突。
- 只在拿到可用页之后处理记录 → 重试不会重复计数。耗尽重试显式抛出不完整错误。
- 本例没有 Retry-After 头；真实客户端要在等待预算内遵守它。
- c2 先 503 后成功：请求序列 initial, c2, c2, c3；503 期间 identities 仍为 {A, C}、North 临时 120、未完成；恢复不会重复处理。
- GET 是幂等的 (idempotent)：方法层面允许重复取，但**不承诺数据不变**。

**危险的提前退出 (Unsafe early exit)**：

```python
try:
    page = fetch_page(params)
except IncompleteRetrieval:
    break   # returns the accumulated prefix as if it were complete
```

c2 永久失败时会返回 North 1/120，漏掉 B 和 E。修复：让错误向上传播，不返回 totals。

**终止游标 ≠ 稳定数据集**：终止值只证明**遍历结束**；文档化的不可变快照 (immutable snapshot)才证明**稳定视图**。一个仅仅叫 snapshot 的字段两者都证明不了。无快照的 offset 分页：[A,B,C,D]、页大小 2 → 取到 A,B；前面插入 X → [X,A,B,C,D]，offset 2 返回 B,C；之后 D 结束。去重能去掉重复的 B，但找不回没看到的 X；"保留每个 identity 的第一个版本"还会掩盖遍历期间的冲突版本。没有稳定视图保证时，要澄清一致性要求，或把结果明确限定为"完成的遍历"而非"某时间点的精确聚合"。

**完整解答 (Full solution, Python 3.12)**

```python
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import re
import time


class IncompleteRetrieval(Exception):
    """Retrieval ended without a complete result."""


class ContractValidationError(Exception):
    """The response or consistency contract was violated."""


@dataclass(frozen=True)
class Response:
    status: int
    headers: Mapping[str, str]
    body: bytes


LOWER = datetime(2026, 10, 21, tzinfo=timezone.utc)
UPPER = datetime(2026, 10, 28, tzinfo=timezone.utc)
RETRY_STATUSES = {429, 502, 503, 504}
# Require a full datetime and a visible numeric offset or Z.
TIMESTAMP = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$"
)


def fetch_page(transport, params, sleep):
    for attempt in range(3):
        try:
            response = transport(dict(params), 5)
        except TimeoutError as error:
            if attempt == 2:
                raise IncompleteRetrieval("Timeout attempts exhausted") from error
        else:
            if response.status == 200:
                return response
            if response.status not in RETRY_STATUSES:
                raise IncompleteRetrieval(f"Unaccepted status: {response.status}")
            if attempt == 2:
                raise IncompleteRetrieval("Status attempts exhausted")
        sleep(attempt + 1)
    raise AssertionError("Unreachable")


def nonempty_string(value):
    return isinstance(value, str) and bool(value)


def parse_timestamp(value):
    if not isinstance(value, str) or not TIMESTAMP.fullmatch(value):
        raise ContractValidationError("Timestamp requires an explicit offset")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as error:
        raise ContractValidationError("Invalid timestamp") from error
    if parsed.utcoffset() is None:
        raise ContractValidationError("Naive timestamp")
    return parsed.astimezone(timezone.utc)


def reject_constant(value):
    raise ValueError(f"Nonstandard JSON constant: {value}")


def validate_page(response):
    try:
        page = json.loads(response.body.decode("utf-8"), parse_constant=reject_constant)
    except (ValueError, UnicodeError, RecursionError) as error:
        raise ContractValidationError("Invalid JSON") from error
    if not isinstance(page, dict) or not {"snapshot", "records", "next_cursor"} <= page.keys():
        raise ContractValidationError("Invalid envelope or missing keys")
    snapshot, records, cursor = page["snapshot"], page["records"], page["next_cursor"]
    if not nonempty_string(snapshot) or not isinstance(records, list):
        raise ContractValidationError("Invalid snapshot or records")
    if cursor is not None and not nonempty_string(cursor):
        raise ContractValidationError("Invalid next_cursor")
    validated = []
    for record in records:
        required = {"id", "region", "amount_cents", "updated_at"}
        if not isinstance(record, dict) or not required <= record.keys():
            raise ContractValidationError("Invalid record or missing fields")
        identity, region, cents = record["id"], record["region"], record["amount_cents"]
        if not nonempty_string(identity) or not nonempty_string(region):
            raise ContractValidationError("Invalid id or region")
        if type(cents) is not int or cents < 0:   # rejects bool, since bool subclasses int
            raise ContractValidationError("Invalid amount_cents")
        instant = parse_timestamp(record["updated_at"])
        validated.append((identity, (region, cents, instant)))
    return snapshot, validated, cursor


def aggregate_adjustments(transport, lower=LOWER, upper=UPPER, *,
                          max_pages=100, sleep: Callable[[float], None] = time.sleep):
    if type(max_pages) is not int or max_pages <= 0:
        raise ValueError("max_pages must be a positive integer")
    for bound in (lower, upper):
        if not isinstance(bound, datetime) or bound.utcoffset() is None:
            raise ValueError("Bounds must be aware datetimes")
    # Freeze the normalized bounds once, before any request.
    lower, upper = lower.astimezone(timezone.utc), upper.astimezone(timezone.utc)
    if lower >= upper:
        raise ValueError("lower must precede upper")

    snapshot = None
    cursor = None
    requested_cursors = set()
    seen = {}
    totals = {}
    pages = 0
    while True:
        if cursor is None:
            params = {}
        else:
            if cursor in requested_cursors:
                raise ContractValidationError("Repeated logical cursor")
            requested_cursors.add(cursor)
            params = {"cursor": cursor, "snapshot": snapshot}
        response = fetch_page(transport, params, sleep)
        page_snapshot, records, next_cursor = validate_page(response)
        if snapshot is None:
            snapshot = page_snapshot
        elif page_snapshot != snapshot:
            raise ContractValidationError("Snapshot changed")
        # The whole page is already validated before any identity is processed.
        for identity, payload in records:
            if identity in seen:
                if seen[identity] != payload:
                    raise ContractValidationError("Conflicting duplicate identity")
                continue
            seen[identity] = payload   # stored even when outside the interval
            region, cents, instant = payload
            if lower <= instant < upper:
                group = totals.setdefault(region, {"count": 0, "amount_cents": 0})
                group["count"] += 1
                group["amount_cents"] += cents
        pages += 1
        if next_cursor is None:
            return totals
        if pages >= max_pages:
            raise IncompleteRetrieval("Page limit reached before completion")
        cursor = next_cursor
```

**脚本化传输做测试 (Scripted transport tests)**——不连真实端点；记录请求参数，返回给定的状态/内容或抛超时。断言**精确聚合和请求序列**，"不报错"本身不能发现只处理了第一页。

```python
import json
import unittest


class ScriptedTransport:
    """Each attempt consumes one supplied Response or TimeoutError."""

    def __init__(self, script):
        self.script = list(script)
        self.calls = []

    def __call__(self, params, timeout):
        self.calls.append((dict(params), timeout))
        if not self.script:
            raise AssertionError("Unexpected extra transport call")
        item = self.script.pop(0)
        if isinstance(item, BaseException):
            raise item
        return item


def json_response(page, status=200):
    return Response(status, {"Content-Type": "application/json"}, json.dumps(page).encode("utf-8"))


def rec(identity, region, cents, ts):
    return {"id": identity, "region": region, "amount_cents": cents, "updated_at": ts}


def pages():
    a = rec("A", "North", 120, "2026-10-21T00:00:00Z")
    return [
        {"snapshot": "s7", "records": [a, rec("C", "South", 999, "2026-10-20T23:59:59Z")], "next_cursor": "c2"},
        {"snapshot": "s7", "records": [dict(a), rec("B", "North", 80, "2026-10-27T12:00:00Z")], "next_cursor": "c3"},
        {"snapshot": "s7", "records": [rec("D", "South", 50, "2026-10-28T00:00:00Z"),
                                       rec("E", "South", 70, "2026-10-25T00:00:00+02:00")], "next_cursor": None},
    ]


class AggregateTests(unittest.TestCase):
    def test_transient_503_then_success(self):
        p1, p2, p3 = pages()
        waits = []
        transport = ScriptedTransport([json_response(p1), Response(503, {}, b""),
                                       json_response(p2), json_response(p3)])
        result = aggregate_adjustments(transport, sleep=waits.append)
        self.assertEqual(result, {"North": {"count": 2, "amount_cents": 200},
                                  "South": {"count": 1, "amount_cents": 70}})
        self.assertEqual([params for params, _ in transport.calls],
                         [{}, {"cursor": "c2", "snapshot": "s7"},
                          {"cursor": "c2", "snapshot": "s7"}, {"cursor": "c3", "snapshot": "s7"}])
        self.assertEqual(waits, [1])

    def test_permanent_middle_failure_raises_not_partial(self):
        p1, _, _ = pages()
        transport = ScriptedTransport([json_response(p1)] + [Response(503, {}, b"")] * 3)
        with self.assertRaises(IncompleteRetrieval):
            aggregate_adjustments(transport, sleep=lambda seconds: None)

    def test_conflicting_duplicate_raises(self):
        p1, p2, p3 = pages()
        p2["records"][0]["amount_cents"] = 121
        transport = ScriptedTransport([json_response(p1), json_response(p2)])
        with self.assertRaises(ContractValidationError):
            aggregate_adjustments(transport, sleep=lambda seconds: None)

    def test_repeated_cursor_raises(self):
        p1, p2, _ = pages()
        p2["next_cursor"] = "c2"
        transport = ScriptedTransport([json_response(p1), json_response(p2)])
        with self.assertRaises(ContractValidationError):
            aggregate_adjustments(transport, sleep=lambda seconds: None)
```

参考测试还覆盖：超时恢复、不可重试状态 (400)、畸形 JSON、缺字段、bool 金额、无时区时间戳、快照变化、空的非终止页、页数上限两侧、时间区间两个边界、等价偏移的重复（带额外字段）被忽略。

**复杂度**：N 条记录、P 页、U 个唯一 identity、G 个输出组 → 期望时间 O(N + P)；保留状态 O(U + P + G)（不含响应缓冲和有界重试）。

**练习题答案**：区间 [2026-10-01, 2026-10-08)，快照 t4；P West 40 在下界 → 计入；Q West 60 恰在上界 → 排除；重复 P 忽略；R East 15 `2026-10-07T23:30:00+02:00` → 21:30Z → 计入。结果 `{"West": {"count": 1, "amount_cents": 40}, "East": {"count": 1, "amount_cents": 15}}`；请求 initial, x, x（503 后重试，两次都带 snapshot t4）。永久失败和重复续取必须抛错，不能返回 West 的临时 40。

**面试怎么说 / How to say it**

> "Before I call anything, I want to agree on what 'done' means. I'll treat the cursor as opaque, carry the snapshot from the first page on every continuation, and stop only when next_cursor is null; an empty page isn't the end. I'll validate each page fully before touching any record, dedupe by ID and compare the normalized payload so a conflicting version raises instead of being silently dropped, and only count records inside the half-open UTC window. I retry only timeouts and 429 or 5xx, with a small bounded backoff, and if a middle page fails permanently I raise rather than return what I have, because a partial total looks plausible and is wrong. One caveat: the null cursor tells me the traversal finished; it's the documented snapshot guarantee that tells me the data didn't shift under me."
>
> 中文：定义"完成"、游标不透明、带快照、空页不终止、整页先校验、按 ID 去重并检测冲突、半开 UTC 区间、只重试瞬时错误、不返回部分结果、区分"遍历完成"与"数据稳定"。

---

## 18. The Live Screen: Coding, Clarifying and Answering Behavioral｜实时筛选：编码、澄清与行为题穿插

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/the-live-screen-coding-clarifying-and-answering-behavioral

**要点 / Key ideas**

- 场景：第 24 分钟，队列汇总函数可运行、两个检查通过、团队转移检查未做。面试官突然问："Tell me about a time you changed your approach after feedback." 切换时必须保住：**约定的契约、代码当前状态、观察到的测试结果、下一步动作**。
- 中断检查点 (interruption checkpoint)：契约、实现状态、已执行的检查、下一个具体动作的简短外部记录。防止"我打算测那个"在记忆里变成"那个通过了"。
- 第三方指南：实时筛选常结合编码和行为讨论，约 60 分钟；格式因赛道而异，向招聘方确认。

**题目 / Problem (English)**

"Summarize open support tickets by team from these updates." Agreed contract: count distinct tickets in their **final** state (not update events). Updates are ordered oldest to newest; the last update for a ticket completely replaces its state, including its team. All fields are valid; status is `open` or `closed`. Return `{team: count}` of final open tickets, omitting zero-count teams. Do not mutate the input.

```text
Input:
R1 North open
R2 South open
R1 North closed
R3 North open
Output: {"North": 1, "South": 1}

Input (team transfer): A West open | B West open | A East open
Output: {"West": 1, "East": 1}
```

**要问的澄清问题 (Clarifying questions)**：计数单位是工单还是更新事件？哪条更新胜出（顺序、平局）？工单能换团队吗？（换团队的 open 工单必须从旧团队移除。）输出是否省略零计数团队？能否修改输入？部署基础设施与本函数契约无关。没有答案时说出临时假设及后果："I'll assume the list is chronological, so the final occurrence wins. Otherwise, I'd need an ordering field and a tie rule."

测验答案：A/West/open, B/West/open, A/East/open → `{"West": 1, "East": 1}`。保留旧团队是在回答另一个问题（历史归属）。

**60 分钟时间盒（可调整，面试官掌控实际议程）**

| 分钟 (Minutes) | 活动 (Activity) |
|---|---|
| 0–6 | 澄清契约 |
| 6–12 | 约定方案、手推夹具 |
| 12–24 | 实现并运行初始检查 |
| 24–36 | 行为题及追问 |
| 36–52 | 恢复编码，测试边界 |
| 52–57 | 解释复杂度与局限 |
| 57–60 | 总结已完成和剩余工作 |

**Approach**：两遍——先保留每个工单的最后状态（team, status），再统计 open 的终态。避免重复计数或把工单留在旧团队。时间 O(n)，保留状态 O(u + g)（n 更新数、u 唯一工单数、g 输出团队数）。

```python
def summarize_open(updates: list[dict[str, str]]) -> dict[str, int]:
    latest: dict[str, tuple[str, str]] = {}
    for update in updates:
        latest[update["ticket_id"]] = (update["team"], update["status"])
    counts: dict[str, int] = {}
    for team, status in latest.values():
        if status == "open":
            counts[team] = counts.get(team, 0) + 1
    return counts


updates = [
    {"ticket_id": "R1", "team": "North", "status": "open"},
    {"ticket_id": "R2", "team": "South", "status": "open"},
    {"ticket_id": "R1", "team": "North", "status": "closed"},
    {"ticket_id": "R3", "team": "North", "status": "open"},
]
assert summarize_open(updates) == {"North": 1, "South": 1}
assert summarize_open([]) == {}

# Added after resuming from the interruption.
transferred = updates + [{"ticket_id": "R2", "team": "East", "status": "open"}]
assert summarize_open(transferred) == {"North": 1, "East": 1}
all_closed = [
    {"ticket_id": "Z1", "team": "West", "status": "open"},
    {"ticket_id": "Z1", "team": "West", "status": "closed"},
]
assert summarize_open(all_closed) == {}
```

**第 24 分钟检查点示例**：

```text
Minute 24: last-update semantics agreed; two-pass implementation runs;
four-update and empty-input checks passed; team transfer NOT tested;
next: add R2/East/open, expect North:1, East:1, no South.
```

实现已支持转移，但此刻该分支的行为**尚未验证**。

<svg viewBox="0 0 760 170" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <rect x="0" y="0" width="760" height="170" fill="#fff"/>
  <text x="20" y="22" font-weight="bold" font-size="13">Interruption checkpoint keeps the technical thread｜中断检查点保住技术线索</text>
  <rect x="20" y="45" width="170" height="80" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="105" y="66" text-anchor="middle" font-weight="bold">Coding 0–24</text>
  <text x="105" y="86" text-anchor="middle">2 checks passed</text>
  <text x="105" y="104" text-anchor="middle">两个检查通过</text>
  <rect x="220" y="45" width="170" height="80" rx="8" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="305" y="66" text-anchor="middle" font-weight="bold">Checkpoint 检查点</text>
  <text x="305" y="84" text-anchor="middle" font-size="11">contract · code state</text>
  <text x="305" y="99" text-anchor="middle" font-size="11">checks run · next action</text>
  <rect x="420" y="45" width="150" height="80" rx="8" fill="#f5eefc" stroke="#8a4fd0"/>
  <text x="495" y="66" text-anchor="middle" font-weight="bold">Behavioral 24–36</text>
  <text x="495" y="86" text-anchor="middle">stop typing</text>
  <text x="495" y="104" text-anchor="middle">停止打字作答</text>
  <rect x="600" y="45" width="145" height="80" rx="8" fill="#e8f7ee" stroke="#2e9b5a"/>
  <text x="672" y="66" text-anchor="middle" font-weight="bold">Resume 36+</text>
  <text x="672" y="86" text-anchor="middle" font-size="11">run saved next test</text>
  <text x="672" y="104" text-anchor="middle" font-size="11">执行保存的下一步</text>
  <line x1="190" y1="85" x2="218" y2="85" stroke="#333" marker-end="url(#a18)"/>
  <line x1="390" y1="85" x2="418" y2="85" stroke="#333" marker-end="url(#a18)"/>
  <line x1="570" y1="85" x2="598" y2="85" stroke="#333" marker-end="url(#a18)"/>
  <text x="20" y="155" font-size="11">"Intended to test" must never become "passed" in memory.｜"打算测"绝不能在记忆中变成"已通过"。</text>
  <defs><marker id="a18" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**行为题插入时**：停止打字，给出约 60–90 秒的有边界回答，留出追问空间（12 分钟块包含追问和过渡，不是独白）。

**流畅叙述掩盖了 bug**：一个候选人边写边念语法、没留检查点，回来说"所有边界都覆盖了"。他的增量计数法加了 East 却没减 South，输出 `{"North": 1, "South": 1, "East": 1}`——违反最后更新语义。恢复方法：找回契约 → 跑转移夹具 → 改为从终态聚合 → 重跑之前的检查。漂亮的行为回答**不能**证明 bug 已修。"大声描述一个断言"不等于执行了它。

- 如果新团队导致 `KeyError: 'East'`：缩小不确定性——"The counter fails when it first encounters East. I'll trace one open ticket and inspect initialization." 用 0 初始化，然后重跑失败和之前的检查。
- 时间紧时：保住可运行基线、说出剩余未测用例、选下一个判别性测试；不要重新规划整个方案或在转移检查前优化。

**练习题答案**（T1 West open, T2 East open, T1 West closed, T3 East open, T2 North open, T4 West closed）：终态 T1 closed、T2 North open、T3 East open、T4 closed → `{"North": 1, "East": 1}`。

**面试怎么说 / How to say it**

| 时机 (Moment) | 英文说法 (What to say) | 中文要点 |
|---|---|---|
| 开始前计划 | "I'll keep the last update per ticket, then count open final states by team. That avoids counting a ticket twice or leaving it on its old team." | 一句话方案 |
| 被行为题打断前 | "Let me jot one line so I don't lose my place: two checks passed, transfer isn't tested yet, that's my next step." | 记检查点 |
| 恢复时 | "The implementation runs; transfer handling is the next unchecked case. I'll add that test now." | 回到保存的下一步 |
| 最终总结 | "The function uses final ticket states and preserves the input. The four-update, empty-input, transfer and all-closed assertions passed in this session. Invalid-data handling wasn't implemented under our valid-input contract." | 只报告实际测试 |

行为题 Q: "Tell me about a time you changed your approach after feedback."

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 37 篇）。

---

# Section II — Palantir module of "Forward Deployed Engineer for AI Systems"（只写新增 / 不同之处）

## II.1 Interview Guide: Palantir Forward Deployed AI Engineers｜Palantir 前线部署 AI 工程师面试指南

Source: https://www.educative.io/courses/forward-deployed-engineer/interview-guide-palantir-forward-deployed-ai-engineers

重叠部分见 Section I 第 2、6 课。**新增 / 不同 / New or different:**

- 这是针对 **Forward Deployed AI Engineer（AI FDE）** 职位的指南，不是 FDSE。职责（据 Palantir 职位描述）：用 AIP 构建 LLM 工作流；在 **AIP Agent Studio**（Foundry 内创建和配置 agent 的工具）中设计部署 AI agent；在 **Workshop**（Foundry 的应用构建层）构建运营应用；在整个交付周期维护 Foundry 数据管道；管理客户关系、与企业利益相关方 (stakeholders)制定 AI 战略。要求：动手构建 AI 系统的经验、数据管道设计、独立编写并交付生产级代码 (production-grade code)、适应快速变化的模糊环境、与技术和非技术人员沟通。
- **两条工程轨道 (two engineering tracks)**：
  - Dev track：构建维护核心平台（Foundry、Gotham、AIP）。
  - **Delta track**：在客户环境中部署这些平台，配置和扩展以适配客户需求。**AI FDE 是 Delta 角色**——不造平台，在平台上为客户构建方案。面试测的是"在问题未定义、工具不熟、截止日期 (deadline)属于别人的组织里有效工作"。

**AI FDE 面试流程（5–6 轮，28–35 天）**——核心评估在虚拟 onsite（"Palantir Day"），把 learning、decomposition、system design 合并为一个多小时的会话。

| 轮次 (Round) | 形式 (Format) | 时长 (Duration) | 考察 (What it tests) |
|---|---|---|---|
| 招聘官筛选 (Recruiter screen) | 电话 | 30 min | 背景、动机、使命契合 |
| 带回家项目 (Take-home project) | 异步 | 3–4 h | 用 Foundry 和 AIP 实际交付 |
| 编码 (Coding) | HackerRank / CodePair | 60 min | 调试、数据处理、SQL、API 集成 |
| 学习面 (Learning interview) | 实时 CodePair | 60 min | 从陌生文档形成心智模型 (mental model) |
| 拆解面 (Decomposition) | 实时 | 60 min | 问题分析与 AI agent 设计 |
| 系统设计 (Systems design) | 实时 | 60 min | 企业条件下的 LLM 工作流与管道设计 |
| 招聘经理 (Hiring manager) | 实时 | 45–60 min | 客户判断与个人负责 |

（Section I 第 6 课提醒：这些都是报道的流程，以你的邀请为准。）

**各轮要点（新增）**

- **Take-home**：开放式需求，3–4 小时用 Foundry/AIP 构建；提交可运行产出 + 书面或录制的讲解。**讲解与代码同等重要**；范围决策 (scoping decisions)本身是评估内容。窄而完整 + 清楚的范围说明 > 覆盖广但没解释。把每个模糊需求当作要在讲解中点名的设计决策；承认没覆盖的部分及原因。
- **Coding**：在大文件中找并修多个 bug；用 Python 解析清洗数据集；**在没有执行环境 (execution environment)的情况下写 SQL**；构建或调用带正确错误处理 (error handling)的 API 端点；偶尔有 LeetCode medium。代码清晰可读优先于优化；凭记忆写 SQL 前先说出查询要返回什么；调试题先通读整个文件再改。
- **Learning interview**：Palantir 独创。开场给一个陌生系统/API/私有查询语法 (proprietary query syntax) + 少量文档，做 **4 道递增难度**的题，面试官是可用资源。常见例子：带私有查询语法的图数据库 (graph database)。考的是学习方式而不是已有知识：多快形成心智模型、问题的质量和具体程度、不熟时是否保持推进。**提具体问题是正面信号**；假装懂和卡住不说话是两大失败行为。练习：30 分钟读陌生 API 文档并做出具体东西。（细节见 Part 2）
- **Decomposition**：Palantir 首创、**权重最高**的一轮，60 分钟。经典题：城市有 911 来电、交通、救护车 GPS 数据，要降低急救响应时间。**2026 AI FDE 变体**：设计一个基于实时天气 API 和 SAP 数据自动改道货运的 AI agent，定义评估框架 (evaluation framework)，确保不超支且保持合同交付率；之后还要说出 agent 调用的工具、选编排模式 (orchestration pattern)、定义输出评估标准。评分信号**主要积累在澄清问题阶段**。前 10 分钟问：终端用户是谁、有什么数据由谁控制、什么阈值算可行；大声说出假设；以比开场更具体的问题陈述收尾。（细节见 Part 2）
- **Systems design**：LLM 工作流和数据管道，场景来自真实客户领域；数据驻留 (data residency)、访问控制、遗留系统集成 (legacy-system integration)、审计要求必须体现在设计中。**评估方法 (evaluation methodology)** 权重很高——说清楚好的输出长什么样、如何测量，是设计的一部分。
- **Hiring manager**：过往客户经历、真实部署中的模糊与冲突、动机；可能追问之前某轮的决策。按"客户约束 → 你做的决定 → 客户发生了什么变化"讲，比讲架构更有信号。用 "I" 而不是 "we"，更深层的信号是能说出具体决策、理由和结果。准备 2–3 个客户情境化的项目例子。

**面试怎么说 / How to say it**

> Q (HM): "Tell me about a customer project you owned."
>
> "The customer's constraint was that operations couldn't trust the daily report because records silently disappeared. I decided to block publication when validation failed and keep the last good report visibly marked as stale, rather than publish a partial one. That meant their reviewers stopped acting on incomplete numbers, and at handover their lead could run the recovery steps without me."
>
> 中文：客户约束 → 我的决定 → 客户的变化；用"我"讲决策。

---

## II.2 Palantir FDSE: Foundry, Gotham, AIP, and the Ontology｜Palantir FDSE：Foundry、Gotham、AIP 与本体

Source: https://www.educative.io/courses/forward-deployed-engineer/palantir-fdse-foundry-gotham-aip-and-the-ontology

重叠部分见 Section I 第 2 课（维修派工例子）。**新增 / 不同 / New or different:**

- 新例子：货运延误派调查员。S41（East，Delayed，owner 未设）、S42（West，准时）、操作员 O7 服务 East；East 协调员可以把 East 货运指派给 East 操作员；查看者 (viewer) 只能读不能指派。目标是指派负责人，不是改道或优化配送。
- **关键规则**：运营上完整的方案 = **具名用户的决策 + 被允许的动作 + 可验证的状态变化** (a named user's decision, a permitted action, and a verifiable change in state)。
- 流程：读源 → 集成（一致的标识符 (identifiers)、哪个事件提供当前状态——**旧事件不能悄悄成为当前事实**）→ 表示运营概念 → 支持协调员（在其授权视图 (authorized view)内）→ 执行配置的动作（校验权限+资格）→ 读结果确认。
- **Apollo**（新）：Palantir 的持续交付 (continuous delivery)与基础设施平台，跨环境部署管理 Foundry、AIP 等软件；与指派逻辑无关。
- Gotham 补充：Palantir 第一个平台，面向国防情报的分析师和操作员，跨数据源找模式并交给运营用户；也有政府其它用途和少量商业用途（如欺诈调查）。
- 对 S41 选择**直接的规则型工作流**：规则已足够，LLM 不提供必要推理。AIP 可用于解析非结构化 (unstructured)事件记录或推荐调查员，但仍需受治理的工具和经验证的动作来完成指派。
- Foundry Actions 可以修改属性、链接和对象，是由用户定义逻辑治理的**事务 (transaction)**。
- **写回边界 (writeback boundary)**：Foundry 文档区分存于写回数据集 (writeback dataset) 的编辑和支撑对象/链接类型的数据源——编辑**不会自动覆盖源记录**。更新上游系统需要显式配置的集成（如 action webhook 或导出）。

**三个不同的问题 (Three separate questions)**

| 问题 (Question) | 含义 (Meaning) |
|---|---|
| 资格 (Eligibility) | O7 与 S41 同属 East → 按规则可被指派 |
| 权限 (Authority) | 同属 East **不**证明协调员有权指派 |
| 执行 (Execution) | 即使授权的选择，在配置的动作成功前 owner 仍未设 |

**失败诊断 (Failure checks)**

| 现象 (Symptom) | 诊断 (Diagnosis) |
|---|---|
| S41 仍无 owner | 只观察/推荐了，没完成状态变化 |
| S41 变了，但 viewer 也能指派 | 结果可达，但权限边界坏了 |
| S42 也变了 | 动作影响了目标外的记录 |
| 指派后协调员看不到 O7 | 先查读路径和编辑访问，再判断动作失败或成功 |

- 诱人方案："红色 Delayed 仪表盘 + LLM 推荐联系 O7"。问一句"S41.owner 现在是什么？"——仍是 unset 就没完成。
- **FDSE 负责的不止按钮**：发现被阻塞的决策 → 检查数据（标识符、事件新鲜度 (freshness)、"East"在不同系统中含义是否相同）→ 构建能力 → 校验访问与行为（允许和拒绝都测）→ 部署并观察使用。"缩短从发现延误到指派的时间"是**待测量**的结果，要先测现状再比较。
- **三类证据**：官方材料（平台、公司、职位期望）、公开面经（准备例子，不是保证的题目）、原创重构（为可解而加的假设不是事实）。日期要分清：发布日期 ≠ 面试日期；不知道面试日期就写未知。

<svg viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <rect x="0" y="0" width="760" height="200" fill="#fff"/>
  <text x="20" y="22" font-weight="bold" font-size="13">Operationally complete = decision + permitted action + verifiable state｜运营完整的三要素</text>
  <rect x="20" y="50" width="150" height="70" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="95" y="75" text-anchor="middle" font-weight="bold">Named user</text>
  <text x="95" y="93" text-anchor="middle">East coordinator</text>
  <text x="95" y="110" text-anchor="middle">具名用户的决策</text>
  <rect x="210" y="50" width="200" height="70" rx="8" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="310" y="72" text-anchor="middle" font-weight="bold">Action: Assign owner</text>
  <text x="310" y="90" text-anchor="middle" font-size="11">checks authority + eligibility</text>
  <text x="310" y="107" text-anchor="middle">被允许的动作</text>
  <rect x="450" y="50" width="160" height="70" rx="8" fill="#e8f7ee" stroke="#2e9b5a"/>
  <text x="530" y="72" text-anchor="middle" font-weight="bold">S41.owner = O7</text>
  <text x="530" y="90" text-anchor="middle" font-size="11">S42 unchanged</text>
  <text x="530" y="107" text-anchor="middle">可验证的状态</text>
  <rect x="640" y="50" width="105" height="70" rx="8" fill="#fafafa" stroke="#999" stroke-dasharray="4,3"/>
  <text x="692" y="75" text-anchor="middle" font-size="11">Source system</text>
  <text x="692" y="92" text-anchor="middle" font-size="11">NOT updated</text>
  <text x="692" y="109" text-anchor="middle" font-size="11">unless webhook</text>
  <line x1="170" y1="85" x2="208" y2="85" stroke="#333" marker-end="url(#a22)"/>
  <line x1="410" y1="85" x2="448" y2="85" stroke="#333" marker-end="url(#a22)"/>
  <line x1="610" y1="85" x2="638" y2="85" stroke="#999" stroke-dasharray="4,3" marker-end="url(#a22)"/>
  <text x="20" y="150" font-size="11">Verify: coordinator sees O7; viewer's attempt rejected; other records unchanged.</text>
  <text x="20" y="168" font-size="11">验证：协调员能看到 O7；查看者的尝试被拒；其他记录不变。写回编辑默认不覆盖源系统。</text>
  <defs><marker id="a22" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**迁移练习答案（机器 M8）**：North 调度员要为 M8 选检查技师；对象 Machine M8、Site North、Technician T3（M8 位于 North，T3 服务 North）；Assign technician 动作检查调度员权限和共享站点后把 T3 指派给 M8；本体中 M8 的技师 = T3，不假设外部维护系统更新；验证：调度员可见、查看者被拒、其他机器不变；Foundry 的集成、本体和工作流能力支持此方案，**AIP 不必要**，因为区域规则已足够。

**面试怎么说 / How to say it**

> Q: "Would you use AIP for this assignment workflow?"
>
> "Not for the core rule. Eligibility here is deterministic: same depot, authorized coordinator. A rule-based Ontology action is simpler, auditable and easy to test. I'd bring in AIP if the input were unstructured, say, parsing an incident note to suggest which operator should investigate, but the assignment itself would still go through the governed action with its permission checks."
>
> 中文：确定性规则用 Action 即可；AIP 适合非结构化输入，但最终状态变化仍走受治理的 Action。

---

## II.3 The Hiring Process: Stages, Timeline, and No-AI Rule｜招聘流程：阶段、时间线与禁用 AI 规则

Source: https://www.educative.io/courses/forward-deployed-engineer/the-hiring-process-stages-timeline-and-no-ai-rule

重叠部分见 Section I 第 6 课（已确认/报道/未解决三分、转录同意≠候选人许可、只更新被确认字段）。**新增 / 不同 / New or different:**

- 三个标签：已确认 (Confirmed)、报道 (Reported)、未解决 (Unresolved)；外加"无依据的说法 (unsupported claim)"，如"每个 FDSE 候选人都有五场 onsite"。原则："Prepare capabilities from the reported pool; schedule and use tools according to instructions confirmed for the candidate's own stage."
- 每条重要说法记录：说了什么、谁提供、日期、范围、未解问题。
- **2025-07-01 的 FDSE 面经**（新）：标注"4 rounds"，实际包含：招聘官电话（无时长）→ 约 45 分钟技术 decomposition → 两场 1 小时（一场 decomposition、一场案例/技术设计）→ 1 小时招聘经理（在行为和 decomposition 式问题间切换）。**"4 轮"里有 5 场面试**——只数轮次会漏掉一场。
- 用六个问题读证据：主体 (actor)、范围 (scope)、日期 (date)、可支持的结论 (supported conclusion)、无依据的推断 (unsupported inference)、补缺问题 (gap-closing question)。测验答案：准备动机、decomposition、设计推理和行为项目证据；自己的顺序和时长仍未解决，去问接下来是什么形式。
- **"Reported Jul 2026"、发布于 2026-09-05 的面经**（新）：招聘官 → decomposition → onsite（coding + learning + decomposition）→ 招聘经理。与前一份重叠 → 加强 decomposition 练习的理由；覆盖不同 → 保留 coding 和 learning。**不要把两份合并成一个更长的必经流程**。
- **三种时钟 (Three clocks)**：面试时长 (interview duration)、阶段间隔 (stage gap)、端到端时长 (end-to-end elapsed time)。指南估计首次接触到 offer 3–4 周；后一份面经报告最终阶段后约 5 周收到拒信——两者端点和结果都不同。时间流逝本身不能说明被拒或会拿 offer。
- **首尔 FDSE 申请**（新）：要求两段各不超过 90 秒的视频——一段讲你构建的东西，一段讲引人思考的 Palantir 报道或内容；重视准备但要求真实、非照稿。只适用于该职位。
- AI 政策（截至 2026 年 11 月初）：公开来源无法确定是否有统一规定；某指南说全程禁止（是报道不是官方）；另一来源称未找到公开的现场面规则，并区分了允许构建时用 AI 的 Build to Apply 赛道。两种错误结论："标题叫 No-AI Rule 所以官方一定有全面禁令"；"没证实禁令所以我可以用助手"。
- 新增实操：工具若**默认开启辅助功能**（如 AI 自动补全），面试前检查设置并关闭未批准的辅助，同时保留被要求使用的环境；有歧义的功能提前问，不要在面试中试探边界。

**确认清单 (Confirmation checklist)**

| 项目 (Item) | 要确认的内容 (What to confirm) |
|---|---|
| 申请 (Application) | 岗位、地点、申请赛道 |
| 顺序 (Sequence) | 下一阶段与预计剩余阶段 |
| 形式 (Format) | 现场或评估；任务类型（是否含 SQL/API） |
| 日程 (Schedule) | 时长、日期、时区、连接信息 |
| 环境 (Environment) | 编码平台、允许语言、环境检查 |
| 材料 (Materials) | 会提供什么、可带或可查什么 |
| 辅助 (Assistance) | 每种工具或帮助来源的许可 |
| 跟进 (Follow-up) | 预计下次更新时间与合适的跟进日期 |

**邮件模板（60 分钟实时筛选邀请）**

> Thanks for the invitation. I have noted the 60-minute live screen, browser coding environment, and recruiter follow-up. Could you confirm the task type, whether SQL or API work is expected, and which programming languages are permitted? Please also confirm what materials and assistance are allowed, including notes, web search, generative AI, and AI autocomplete. Which later formats are currently expected, and when should I expect the next update?

错误计划的修复："预留五个必选 onsite 块、首次接触后恰好四周拿 offer、因为同意了记录员就开 AI 编码助手"——删掉虚构的预约和 offer 截止日、保留准备覆盖面、把工具许可记为未解决直到明确答复。

**面试怎么说 / How to say it**

> Q (recruiter): "Any questions before the screen?"
>
> "Just to make sure I set up correctly: is it fully no-AI, including autocomplete in the editor? I'll turn that off unless you tell me otherwise. And may I keep a blank scratch file open for notes?"
>
> 中文：主动确认自动补全等默认功能，表明会关闭。

---

## II.4 Your Story: Why Palantir, Projects, Mission, and Ethics｜你的故事：Why Palantir、项目、使命与伦理

Source: https://www.educative.io/courses/forward-deployed-engineer/your-story-why-palantir-projects-mission-and-ethics

重叠部分见 Section I 第 9、10、11、12 课。**新增 / 不同 / New or different:**

- 首轮回答三部分：真实动机 + 支撑它的项目 + 对工作后果的有理立场。
- **Edge Autonomous Systems FDSE 申请题**（新，官方）："What has been your favorite project or proudest accomplishment? Why?"、"Why do you want to work at Palantir?"，以及用 3–5 句描述一个**没有现成文档或既定方案**的技术挑战（方法与结果）。
- 2026 年一份 FDSE 面经报道的招聘官问题："Why do you want to work at Palantir?"、"Why forward deployed engineering?"、"Tell me about a time you worked with unclear customer requirements."
- **四个链接 (Four links)**：经历 (Experience) → 偏好 (Preference) → 公司连接 (Company connection) → FDSE 工作 (FDSE work)。不必声称只有 Palantir 能解决运营问题，只需一个具体、有研究依据的理由。

**新案例：设备借用工具 (equipment-loan tool)** —— 三人团队；候选人实现状态核对 (status reconciliation) 和归还状态迁移；队友做界面和导入；初始导入 60 条借用，其中 12 条标记为 late；协调员说已批准的延期会改变到期日，导入的 late 标记**不权威**。

逾期规则三部分：已批准延期提供有效到期日；已归还的不算当前逾期；未归还且过了约定到期边界才逾期。实现最后一条前要澄清：到期是日期还是精确时刻？哪个时区？

**三种实现方案对比 (Status implementation options)**

| 方案 (Option) | 优点 (Pros) | 缺点 (Cons) |
|---|---|---|
| 保留导入的标记 (Preserve imported flags) | 显示简单 | 保留了协调员已说可能错误的值 |
| 读取时推导 (Derive on read) | 使用当前规则，不需同步第二个状态值 | 依赖输入是最新的 |
| 定时更新存储状态 (Scheduled update) | 支持预计算 (precomputed)查询 | 多一个要运维的任务；边界过后到下次更新有延迟 |

候选人选择**读取时推导**。追问"什么会让你重新考虑？"——区分三种情况：规则错误、输入数据过时、查询太贵，各需不同补救；换成定时更新并不能自动解决三者。规模变大时重新评估查询成本和响应时间，预计算可能变得合理，但要明确其新鲜度和核对行为。

- 验证：12 个检查（延期、归还、到期边界、重复归还请求、角色限制），初始 10 过，2 个显示延期借用被错标 late；修正有效到期日处理后全部通过；3 位目标用户完成受监督试点 (supervised pilot)；**未测**处理时间基线 (baseline)。

**弱回答的修复**："I want Palantir because it is prestigious and Foundry and AIP have huge impact. I built our entire loan platform and cut processing time by 80%. Privacy is solved because users log in." → 用证据而不是更强的形容词重写（见下方英文答案）。

**隐私讨论（新）**：利益相关方要求把每个借用人的完整可识别借用历史导出给所有志愿者并无限期保留，以提高归还率。

- 区分有用的目标（找回设备）和提议的手段。风险：不必要的披露 (disclosure)、基于旧的/有争议的/错误分类的记录的不公平判断。志愿者处理今天的归还只需要远少于终身历史的信息。
- 替代方案：给授权协调员一个**受限的当前逾期工作队列**（物品、有效到期日、合适的联系方式）；更广报告用聚合数据（检查小群体或组合是否会重新识别个人）；定义为什么要保留可识别历史、保留多久、何时复审；保留可审查的访问记录并提供纠错渠道 (correction channel)。

| 保障 (Safeguard) | 回答的问题 (Question it answers) |
|---|---|
| 访问控制 (Access control) | 谁可以执行操作 |
| 数据最小化 (Data minimization) | 收集或披露什么 |
| 保留期限 (Retention limits) | 保留多久 |
| 可审计性 (Auditability) | 支持事后审查发生了什么 |

任何一项单独都不能证明用途本身合理；聚合也不能自动消除再识别 (re-identification) 风险。

**使命立场的五要素（新）**：对预期收益的真实看法；受益者与可能受害者；一个重大的可预见风险；区分已知事实与缺失背景；一个会改变决定的条件或边界。合法授权重要，但不能单独解决所有伦理问题。

**面试怎么说 / How to say it**

Why Palantir / Why FDSE（课程示范，60–90 秒）：

> "I became interested in operational software while helping build an equipment-loan tool. The coordinator and our imported data disagreed about what counted as overdue. I clarified that approved extensions changed the effective due date, then implemented status reconciliation and return handling; my teammates built the interface and import process.
>
> I enjoyed that the engineering decision depended on understanding what the user needed to do next. I chose to derive overdue status rather than copy imported flags or maintain scheduled updates. Two extension checks initially failed; after correcting the logic, all 12 passed, and three intended users completed a supervised pilot. We didn't measure a productivity improvement.
>
> That's why Foundry interests me: its operational representation and actions connect data to user workflows. I haven't used the platform yet, so that connection comes from my research. FDSE appeals to me because I want to build alongside users and carry clarified requirements into working software."
>
> 中文：经历 → 偏好 → 公司连接（承认未用过）→ 为什么 FDSE。资深候选人用自己的生产项目替换例子，结构不变。

| 追问 (Follow-up) | 英文回答 (English answer) | 中文要点 |
|---|---|---|
| "Why here rather than any data company?" | "The link between operational concepts and actions gives me a specific reason to look at Foundry. I want to see how engineers use it with customers. I'm not claiming only Palantir can solve this." | 具体但不排他 |
| "What did you decide personally?" | "I chose derived overdue status after clarifying extensions, and implemented that logic and the return transition. The interface and import were my teammates'." | 分清个人与团队 |
| "What proves the result?" | "The corrected logic passed our 12 checks and three users completed the pilot. I can't infer time saved from that." | 证据边界 |
| "What would make you reconsider the design?" | "It depends on what breaks. A wrong rule means fixing the rule; stale extension data means fixing the input feed; slow queries at scale might justify precomputing, as long as freshness and reconciliation are explicit." | 区分三种失败 |
| "Tell me about a time you worked with unclear customer requirements." | "Our imported data said twelve loans were late, but the coordinator told me approved extensions change the due date, so the flag wasn't authoritative. Before writing logic I pinned down the rule, including whether 'due' meant a date or an exact time and in which time zone, then derived status from that rule and tested the boundaries." | 先定规则再写代码 |

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 37 篇）。

隐私场景回答：

> "I support helping coordinators recover equipment, but I wouldn't ship the unrestricted historical export as described. A current overdue queue for authorized coordinators looks sufficient for immediate follow-up. Before retaining identifiable history, I'd ask what decision requires it, who approves access, how long we keep it, and how borrowers can challenge errors. I'd reconsider a limited historical view if a specific need and proportionate safeguards were established; I'd decline disclosure to all volunteers without that."
>
> 中文：支持目标、拒绝手段、给出最小化替代、列出待确认问题、说明什么条件下会改变决定。

Q: "Palantir works with governments and defense customers. How do you feel about that?"（自拟示范，按五要素组织；立场应是你真实的）

> "I'm broadly supportive of public-sector work where the purpose is clear, for example logistics, disaster response or public health, because better data can genuinely help people. I also recognize the people affected by those systems aren't always the users, and the material risk is data being used beyond its stated purpose. I don't know the specifics of individual deployments, so I'd want to understand how purpose, authorization, oversight and redress are handled on the team I'd join. If a project's purpose were foreseeably harmful to vulnerable people, that's where I'd draw the line. How are concerns about data access or intended use raised and reviewed on this team?"
>
> 中文：真实看法 + 受益者与可能受害者 + 主要风险 + 承认未知 + 会改变决定的边界 + 一个调查性问题。

---

## II.5 Screen Formats, Time Strategy, and the Implementation Problem｜筛选形式、时间策略与实现题

Source: https://www.educative.io/courses/forward-deployed-engineer/screen-formats-time-strategy-and-the-implementation-problem

重叠部分见 Section I 第 13、14 课（报道的形式、契约→基线→验证、循环不变式 (loop invariant)、先基线后优化）。**新增 / 不同 / New or different:**

- 开场问题：90 分钟练习评估进行到第 35 分钟，还在打磨实现题，SQL 和 API 没碰、边界未测——什么证据能证明再花 10 分钟是值得的？**答案：只有当你能说出一个预期能修好的具体失败用例、并且其他题已有可运行基线时**。"可以更整洁"不是证据。
- 一份 2025 年 3 月的面经：实用功能实现题，建议交付可运行方案而不是未完成的优化方案（一人经验，不是评分规则）。
- 实时面"在有意义的时刻说话"：契约、计划（数据结构及其为何保住规则）、阻塞、验证。过渡句："I'll group by this identity, accumulate each contribution, then apply the output rules. Does that match the intended behavior?"
- **练习时间分配（新）**：60 分钟实时 = 5 澄清 + 5 计划 + 30 实现 + 10 验证 + 10 缓冲；不受限的 90 分钟三题评估 = 5 检查 + 3 × 25 + 10 最终验证。先确认能否自由切换、是否显示评分信息。
- **截止检查 (Deadline check)**：当前题可运行且通过契约检查？→ 停止打磨。有几分钟能修好的已知失败？→ 修；否则留短注说明剩余问题。其他题还没基线？→ 转过去。保留最终验证时间。不要假设题目等权、能回看或有部分分。

**新题：持仓汇总 (Roll up holdings)**——一份面试指南报道的实现题示例，以下细节为练习重构。

Problem (English): Each row is `(account, symbol, quantity)` with a signed integer quantity. Every row contributes once, including identical rows. Group by account **and** symbol. Keep negative totals; remove only **final** zero totals. Return a list of tuples sorted by account, then symbol. Do not mutate the input; empty input returns `[]`.

"roll up holdings" 的歧义 (ambiguity)：identity 是 symbol 还是 account+symbol？相同行算两次还是重复事件？负数和零要不要显示？顺序？能否修改输入？

```text
Input:
[("A2","XYZ",5), ("A1","XYZ",10), ("A1","XYZ",-4), ("A1","ABC",3),
 ("A1","ABC",-3), ("A2","XYZ",5), ("A1","DEF",-2), ("A1","ABC",2)]
Output:
[("A1","ABC",2), ("A1","DEF",-2), ("A1","XYZ",6), ("A2","XYZ",10)]
```

Trace 要点：A1/ABC 3 → 0（键**保留**）→ 2（重新打开）；A2/XYZ 的相同行再次贡献 → 10；A1/DEF 负数保留。测验 `[('A1','ABC',3), ('A1','ABC',-3), ('A1','ABC',2), ('A2','XYZ',5), ('A2','XYZ',5)]` → `[('A1','ABC',2), ('A2','XYZ',10)]`。

**Approach**：一个以 (account, symbol) 为键的字典累加；循环结束后排序键、输出非零总数。只按 symbol 分组会合并不同账户；对每个键扫描输出列表是多余工作。

**循环不变式**：处理完每一行后，字典包含目前见过的所有 account-symbol 对，每个值等于该对目前的数量之和（**包括零**）。过滤和排序只在全部行处理后进行。

```python
def roll_up_holdings(rows):
    totals = {}
    for account, symbol, quantity in rows:
        key = (account, symbol)
        totals[key] = totals.get(key, 0) + quantity
    return [
        (account, symbol, totals[(account, symbol)])
        for account, symbol in sorted(totals)
        if totals[(account, symbol)] != 0
    ]


def check(name, got, expected):
    ok = got == expected
    print("PASS" if ok else "FAIL", "-", name)
    if not ok:
        print("  got:", got)
        print("  expected:", expected)


rows = [
    ("A2", "XYZ", 5), ("A1", "XYZ", 10), ("A1", "XYZ", -4),
    ("A1", "ABC", 3), ("A1", "ABC", -3), ("A2", "XYZ", 5),
    ("A1", "DEF", -2), ("A1", "ABC", 2),
]
before = rows.copy()
check("full trace", roll_up_holdings(rows),
      [("A1", "ABC", 2), ("A1", "DEF", -2), ("A1", "XYZ", 6), ("A2", "XYZ", 10)])
check("input unchanged", rows, before)
check("empty input", roll_up_holdings([]), [])
check("accounts sorted", roll_up_holdings([("B2", "X", 2), ("A1", "X", 3)]),
      [("A1", "X", 3), ("B2", "X", 2)])
check("repeated rows add", roll_up_holdings([("A2", "XYZ", 5), ("A2", "XYZ", 5)]), [("A2", "XYZ", 10)])
check("final zero removed", roll_up_holdings([("A1", "X", 3), ("A1", "X", -3)]), [])
check("zero then reopened", roll_up_holdings([("A1", "X", 3), ("A1", "X", -3), ("A1", "X", 2)]),
      [("A1", "X", 2)])
check("negative kept", roll_up_holdings([("A1", "X", -2)]), [("A1", "X", -2)])
```

**复杂度**：n 行、k 个不同键；累加 O(n)，排序键 O(k log k)，总计 **O(n + k log k)**；额外空间 O(k)，输出至多 O(k)。基线备选：按键排序行再对相同键的连续段求和——也可以，但字典更容易推理。

**Python 陷阱（新）**

```python
def add_row(row, totals={}):   # BAD: one dict shared by every call
    totals[row[0]] = totals.get(row[0], 0) + row[1]
    return dict(totals)

print(add_row(("XYZ", 4)))   # {'XYZ': 4}
print(add_row(("ABC", 1)))   # {'XYZ': 4, 'ABC': 1}  <- XYZ leaked in
```

- 可变默认参数 (mutable default argument) 只创建一次、被所有调用共享 → 在函数内部创建 totals。
- 缺失 vs 零 (missing vs zero)：不存在的键 ≠ 值为 0 的键；`get(key, 0)` 只在累加时把缺失当零。如果在归零时永久关闭持仓，就会丢掉之后 A1/ABC 的那一行。
- 集合选择：dict = 键控总数和查找；set = 成员与唯一性；list = 有序输出；`collections.deque` = 先进先出（`list.pop(0)` 会移动所有剩余元素，deque 不会）。只用标准库，不要假设有额外包。
- **测试失败时**：把循环改成 `for ... in set(rows):` → 重复行检查返回 `[('A2','XYZ',5)]` 而不是 10。先查契约：没有事件 ID、每行都贡献 → 转 set 删掉了合法行。恢复、重跑该检查、再重跑其余检查。排序看起来贵时先问顺序是否必需——这里是必需的。
- 练习夹具检查点：B1/AAA 7 → 0 → 3 必须出现；B2/AAA 两行相同的行合计 8。输出与预测不一致时，找出不变式第一次不成立的那一行。

**面试怎么说 / How to say it**

> "I'll treat these as additive rows, including repeats. Accounts stay separate, short positions stay, and zeros are removed only from the final output. So the key is the pair of account and symbol, and the invariant is that each stored value is the running sum for that pair, zero included. The scan is linear and the required ordering adds a sort on the distinct keys, so O(n + k log k)."
>
> 中文：先用一句话说清契约（重复行相加、账户分开、负数保留、只在最后去零），再说键、不变式和复杂度。

---

## II.6 Algorithm Patterns That Show Up in the Screen｜筛选中常见的算法模式

Source: https://www.educative.io/courses/forward-deployed-engineer/algorithm-patterns-that-show-up-in-the-screen

重叠部分见 Section I 第 15 课（哈希计数、双指针、可变窗口、前缀和、区间合并、堆）。**新增 / 不同 / New or different:**

- **选模式四问 (Four questions)**：要求的对象是什么（对、连续区间、分组、top-k、路径）？哪些约束改变正确性（有序、负数、重复、端点规则、边权）？保留什么状态、含义是什么（= 不变式）？为什么丢弃某些候选是安全的（丢弃论证 discard argument）？模式靠不变式和丢弃论证来证明，而不是提示词里的熟悉字眼。
- 字典细节：`'east' in totals` 问键是否存在；`totals['east'] == 0` 问值——两个不同的问题。
- 双指针返回值变体 + `[3, 3]` target 6：`left < right` 保证两个下标不同，但相等的值在不同下标可以配对。
- **滑窗失效的新反例 (counterexample)**：在 [1, −1, 3] 中找和 ≥ 3 的最短区间。窗口扩展到整个列表（和 3，长 3），移除 1 后和 2 就停，漏掉 [3]（长 1）。收缩假设"移除一个值不会增加和"，负数打破这一点。
- 前缀和新 trace：[3, −2, 2, −3, 3]，target 3，前缀 [0, 3, 1, 3, 0, 3]；最后一步 +2（前缀 0 出现在边界 0 和 4）；答案 4：[0:1]、[0:3]、[0:5]、[4:5]。新增**暴力对拍 (brute-force cross-check)**：对 −1/0/1 组成的长度 0–4 的所有列表比较两个版本。
- 区间合并变体：**闭区间、相接即合并**，用 `<=`；`sorted()` 返回新列表不改输入（`list.sort()` 会改）；`max` 很重要——(2, 2) 在 (1, 3) 内。
- 堆：未排序的堆要最后排序输出；作业队列推入 `(priority, sequence_number, job)` 避免比较 job 对象。
- **新模式：BFS 图与网格**（Section I 没有）。

### II.6.1 Pair in sorted list (returns the pair)｜有序数组找一对

```text
Input:  [1, 2, 4, 7, 11], target 10   ->  None   (sums: 12, 8, 9, 11)
Input:  [1, 2, 4, 7, 11], target 9    ->  (2, 7)
Input:  [3, 3], target 6              ->  (3, 3)
```

```python
def find_pair(values, target):
    left, right = 0, len(values) - 1
    while left < right:
        total = values[left] + values[right]
        if total == target:
            return (values[left], values[right])
        if total < target:
            left += 1
        else:
            right -= 1
    return None
```

O(n) 时间、O(1) 空间；未排序需先排序 O(n log n) 并保留原下标。

### II.6.2 Count exact-sum ranges with brute-force cross-check｜前缀和计数 + 暴力对拍

```text
Input:  [3, -2, 2, -3, 3], target 3   ->  4
Input:  [0, 0], target 0              ->  3
Input:  [2, -2, 2, 0], target 2       ->  5   # practice: [0:1], [0:3], [0:4], [2:3], [2:4]
```

```python
from itertools import product


def count_target_ranges(values, target):
    prefix = 0
    answer = 0
    counts = {0: 1}  # empty prefix before index 0
    for value in values:
        prefix += value
        answer += counts.get(prefix - target, 0)    # look up first
        counts[prefix] = counts.get(prefix, 0) + 1  # then record
    return answer


def brute_count(values, target):
    answer = 0
    for left in range(len(values)):
        total = 0
        for right in range(left, len(values)):
            total += values[right]
            if total == target:
                answer += 1
    return answer


mismatches = 0
for size in range(5):
    for items in product((-1, 0, 1), repeat=size):
        for target in range(-2, 3):
            sample = list(items)
            if count_target_ranges(sample, target) != brute_count(sample, target):
                mismatches += 1
assert mismatches == 0
```

没有 `{0: 1}`：[3] target 3 返回 0；先记录后查询：[0, 0] target 0 返回 5 而不是 3。O(n) 时间与空间 vs 暴力 O(n²)。练习答案：前缀 [0, 2, 0, 2, 2] → 5 个区间；收缩和窗口不行，因为 −2 会让和变小。

### II.6.3 Merge closed intervals (touching merges)｜合并闭区间（相接合并）

```text
Input:  [(5, 7), (1, 3), (2, 2), (3, 5), (9, 10)]
Output: [(1, 7), (9, 10)]      # input list unchanged
```

```python
def merge_intervals(intervals):
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged
```

安全输出的理由：一旦出现间隙，之后的区间开始得更晚，不会再连回已完成的区间。O(n log n)。（对比 Section I 15.7：半开区间、相接不合并用 `<`。）

### II.6.4 Largest k values (min-heap of size k)｜最大的 k 个值

```text
Input:  [5, 1, 5, 3, 9], k = 3   ->  [9, 5, 5]
Input:  [2], k = 5               ->  [2]
Input:  [4, 1], k = 0            ->  []
```

```python
import heapq


def largest_k(values, k):
    if k <= 0:
        return []
    heap = []
    for value in values:
        if len(heap) < k:
            heapq.heappush(heap, value)
        elif value > heap[0]:
            heapq.heapreplace(heap, value)
    return sorted(heap, reverse=True)
```

O(n log k) 时间、O(k) 空间。需要整体排名就直接排序。

### II.6.5 BFS distances and connected components｜BFS 距离与连通分量（新）

Problem: Given an undirected graph as an adjacency list, return the BFS distance (edge count) from `start` to every reachable node, and count connected components.

```text
Input:  graph = {A: [B, C], B: [A, D], C: [A, D], D: [B, C], E: []}, start = A
Output: distances = {A: 0, B: 1, C: 1, D: 2}
        components = 2
```

Approach：BFS 按层探索 {A} → {B, C} → {D}；边权相同时第一次到达即最短路径 (shortest path)。DFS 能回答可达性但不保证最短。**入队前记录距离**，防止环导致重复入队。对每个未见节点启动一次 BFS，每次启动 = 一个新分量（这样 E 也被计入）。O(V + E)。边权不等时 BFS 不再给最短路径（需 Dijkstra 等）。

```python
from collections import deque


def bfs_distances(graph, start):
    distance = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    return distance


def count_components(graph):
    seen = set()
    count = 0
    for node in graph:
        if node not in seen:
            count += 1
            seen.update(bfs_distances(graph, node))
    return count
```

### II.6.6 Shortest path on a grid｜网格最短路径（新）

Problem: Grid of strings with `S` (start), `G` (goal), `.` (open), `#` (wall). Move up/down/left/right. Return the minimum number of steps from S to G, or `None`.

```text
Input:  ["S..#G",
         ".#..."]
Output: 6        # top row is blocked at (0, 3); detour through the bottom row
Input:  ["S#G"]  ->  None
Input:  ["SG"]   ->  1
```

```python
from collections import deque


def shortest_path(grid):
    if not grid:
        return None
    rows, cols = len(grid), len(grid[0])
    start = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "S")
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        (r, c), steps = queue.popleft()
        if grid[r][c] == "G":
            return steps
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and (nr, nc) not in seen:
                seen.add((nr, nc))
                queue.append(((nr, nc), steps + 1))
    return None
```

O(rows × cols)：每个格子最多访问一次。

### II.6.7 Grid shortest path with up to k wall breaks｜可打破 k 面墙的网格最短路径（扩展）

Problem: Same grid, but you may pass through at most `k` walls. Return the minimum steps or `None`.

```text
Input:  ["S#G"], k = 1   ->  2
Input:  ["S#G"], k = 0   ->  None
```

Approach（课程要点，代码为笔者补充）：格子本身不再是完整状态——同一格子"已用掉一次破墙"和"还没用"是不同的到达。`seen` 存 `(row, col, walls_left)`，否则 BFS 可能丢弃那个仍能到达终点的到达。状态数至多 rows × cols × (k + 1)，时间与空间同阶。

```python
from collections import deque


def shortest_path_with_breaks(grid, k):
    if not grid:
        return None
    rows, cols = len(grid), len(grid[0])
    start = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "S")
    queue = deque([(start[0], start[1], k, 0)])
    seen = {(start[0], start[1], k)}
    while queue:
        r, c, walls_left, steps = queue.popleft()
        if grid[r][c] == "G":
            return steps
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            remaining = walls_left - 1 if grid[nr][nc] == "#" else walls_left
            if remaining < 0:
                continue
            state = (nr, nc, remaining)
            if state not in seen:
                seen.add(state)
                queue.append((nr, nc, remaining, steps + 1))
    return None
```

**面试怎么说 / How to say it**

> "Every move costs the same, so BFS gives me the shortest path: it dequeues cells in order of distance, and the first time I pop the goal I'm done. I mark cells as seen when I enqueue them, not when I pop them, so a cell never goes in twice. If you let me break walls, a cell alone isn't the state anymore; arriving with a break left is different from arriving without one, so I'd track row, column and breaks remaining, which multiplies the state space by k plus one."
>
> 中文：等权用 BFS；入队时标记；允许破墙时状态要加上剩余次数。

---

## II.7 SQL and API Tasks: Queries, Pagination, and Aggregation｜SQL 与 API 题：查询、分页与聚合

Source: https://www.educative.io/courses/forward-deployed-engineer/sql-and-api-tasks-queries-pagination-and-aggregation

重叠部分见 Section I 第 16、17 课（粒度、ROW_NUMBER 去重、LEFT JOIN 条件放 ON、SUM(DISTINCT) 陷阱、不透明游标、去重与冲突检测）。**新增 / 不同 / New or different:**

- 五步：说明输出粒度和合格条件 → 识别贡献实体及其键 → 预测哪些连接会放大行数 → **先确定当前记录再按当前状态过滤** → 聚合后手工核对一个棘手例子；API 题先说明分页契约 (pagination contract)再写循环。
- 用 Python 内置 `sqlite3` 运行（与 PostgreSQL 写法一致），可在面试中自测。日期存为 `YYYY-MM-DD` 文本，按文本比较即按时间比较。
- 新陷阱 **O3**：曾经晚到但当前准时（302 在 13:00），而 ID 最大的事件 303 是一条**更早**的 late 事件——说明"最新"必须按 event_time，不能按 event_id。
- `WHERE` vs `HAVING`：WHERE 在分组前过滤行，HAVING 在分组后过滤组。`HAVING COALESCE(SUM(q.loss), 0) > 20` 只保留 east。
- Palantir Foundry API 使用类似的 `pageToken` / `nextPageToken` 模式（本题端点是练习契约）。
- **完整性和只计一次是两个独立检查**：去重后的总数如果提前停止仍不完整；完整遍历如果每条到达都加仍会重复计算。

### II.7.1 Late-delivery losses by region (SQLite)｜按区域统计晚到损失

Problem (English): Output one row per region in `customers` (including regions with no qualifying orders). An order qualifies if it was placed in `[2026-07-01, 2026-10-01)` and its **latest** delivery event is `late`. Latest = greatest `event_time`; ties go to the larger `event_id`. Orders with no events are unknown and don't qualify. Report `late_orders` and `total_loss`; a region with none shows `0, 0`.

```text
Input:
customers: C1 east | C2 west | C3 north | C4 south
orders (all placed 2026-08-01): O1 C1 loss 40 | O2 C1 15 | O3 C2 25 | O5 C2 10 | O4 C3 0
delivery_events:
  101 O1 late    08-02 10:00 | 102 O1 on_time 08-02 11:00 | 103 O1 late 08-02 11:00
  201 O2 late    08-02 12:00
  301 O3 late    08-02 09:00 | 302 O3 on_time 08-02 13:00 | 303 O3 late 08-02 08:00
  401 O4 late    08-02 12:00
  (O5 has no events)

Output:
('east', 2, 55)
('north', 1, 0)
('south', 0, 0)
('west', 0, 0)
```

**错误查询**（输出 east 95、north 0、west 50，且丢了 south）：

```sql
SELECT c.region, SUM(o.loss) AS total_loss
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
JOIN delivery_events e ON e.order_id = o.order_id
WHERE o.placed_at >= '2026-07-01' AND o.placed_at < '2026-10-01'
  AND e.status = 'late'
GROUP BY c.region
ORDER BY c.region;
```

- 连接后每个事件一行：O1 两条 late → 40 加两次 = 80，加 O2 的 15 → east 95。
- `status = 'late'` 匹配历史中任意 late：O3 当前准时，但两条旧 late 事件 → west 50。
- 内连接 (inner join)丢掉没有订单的客户 → south 消失。
- 另两个陷阱：`LEFT JOIN orders ... WHERE o.placed_at >= ...` 仍会丢 south（NULL 比较不为真）；`SUM(DISTINCT o.loss)` 不能修复重复计算（两个不同订单各损失 40 应合计 80）。

**分阶段的正确查询 (Staged query)**：

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE customers (customer_id TEXT PRIMARY KEY, region TEXT);
CREATE TABLE orders (order_id TEXT PRIMARY KEY, customer_id TEXT, placed_at TEXT, loss INTEGER);
CREATE TABLE delivery_events (event_id INTEGER PRIMARY KEY, order_id TEXT, status TEXT, event_time TEXT);
INSERT INTO customers VALUES ('C1','east'), ('C2','west'), ('C3','north'), ('C4','south');
INSERT INTO orders VALUES ('O1','C1','2026-08-01',40), ('O2','C1','2026-08-01',15),
  ('O3','C2','2026-08-01',25), ('O5','C2','2026-08-01',10), ('O4','C3','2026-08-01',0);
INSERT INTO delivery_events VALUES
  (101,'O1','late','2026-08-02 10:00'), (102,'O1','on_time','2026-08-02 11:00'),
  (103,'O1','late','2026-08-02 11:00'), (201,'O2','late','2026-08-02 12:00'),
  (301,'O3','late','2026-08-02 09:00'), (302,'O3','on_time','2026-08-02 13:00'),
  (303,'O3','late','2026-08-02 08:00'), (401,'O4','late','2026-08-02 12:00');
""")

query = """
WITH ranked AS (
    SELECT e.*, ROW_NUMBER() OVER (
        PARTITION BY order_id ORDER BY event_time DESC, event_id DESC) AS rn
    FROM delivery_events e
),
latest AS (SELECT * FROM ranked WHERE rn = 1),
qualifying AS (
    SELECT o.order_id, o.customer_id, o.loss
    FROM orders o
    JOIN latest l ON l.order_id = o.order_id
    WHERE o.placed_at >= '2026-07-01' AND o.placed_at < '2026-10-01'
      AND l.status = 'late'
)
SELECT c.region,
       COUNT(q.order_id) AS late_orders,
       COALESCE(SUM(q.loss), 0) AS total_loss
FROM customers c
LEFT JOIN qualifying q ON q.customer_id = c.customer_id
GROUP BY c.region
ORDER BY c.region;
"""
for row in db.execute(query):
    print(row)
```

- 最新事件：O1 → 103（late，平局靠 event_id）、O2 → 201、O3 → 302（on_time）、O4 → 401。**在选出最新事件之后**再过滤状态，否则会带回 O3 的旧事件。内连接 latest 丢掉无事件的 O5。
- `COUNT(q.order_id)` 计真实订单，不计占位行；`COALESCE` 把空区域的 NULL 和变 0；从 customers LEFT JOIN 保留所有区域。east 55 = 40 + 15。

**练习 1 答案**：customers U east、V west；P1（loss 7）事件 1 late 10:00、2 on_time 11:00、3 late 11:00；P2（loss 5）事件 4 late 12:00。P1 由事件 3 决定（平局取更大 ID）→ late。预期 `[('east', 2, 12), ('west', 0, 0)]`。把上面的分阶段查询原样套用即可；若 P1 显示事件 2，说明漏了平局规则——先单独 `SELECT * FROM latest` 排查。

### II.7.2 Paginated total with token (dedupe by id)｜令牌分页求总损失

Problem (English): The first request has no token. Each response has `items` (records with `id`, `loss`) and may include `nextPageToken`; pass it as the next token. Traversal is complete **only** when `nextPageToken` is absent (a short or empty page is not the end). The same `id` on two pages is one record; same `id` with a different `loss` is an error. Data is stable during paging.

```text
Input pages:
start: [O1/40]  next "a"
a:     [O1/40]  next "b"
b:     [O2/15]  (no next)
Output: 55
```

测验答案：遍历全部三页、每个稳定 ID 计一次 → 55。错误：因为首页少于 pageSize 就停（40）；每条都加（95）；因 O1 重复就拒绝（重复相同值是合法的）。

```python
PAGES = {
    None: {"items": [{"id": "O1", "loss": 40}], "nextPageToken": "a"},
    "a": {"items": [{"id": "O1", "loss": 40}], "nextPageToken": "b"},
    "b": {"items": [{"id": "O2", "loss": 15}]},
}


def total_loss(fetch, max_pages=100):
    token = None
    seen_tokens = set()
    losses = {}
    for _ in range(max_pages):
        if token in seen_tokens:
            raise RuntimeError("repeated page token")
        seen_tokens.add(token)
        page = fetch(token)
        for item in page["items"]:
            if item["id"] in losses and losses[item["id"]] != item["loss"]:
                raise RuntimeError("conflicting duplicate " + item["id"])
            losses[item["id"]] = item["loss"]
        if "nextPageToken" not in page:
            return sum(losses.values())
        token = page["nextPageToken"]
    raise RuntimeError("page limit exceeded")


def expect_error(pages, label):
    try:
        total_loss(lambda token: pages[token])
        print("FAIL -", label, "returned a total")
    except RuntimeError as error:
        print("PASS -", label, "->", error)


print("total:", total_loss(lambda token: PAGES[token]))   # 55
empty_first = {None: {"items": [], "nextPageToken": "z"}, "z": {"items": [{"id": "O9", "loss": 3}]}}
print("empty page, then data:", total_loss(lambda token: empty_first[token]))   # 3
expect_error({None: {"items": [], "nextPageToken": "a"},
              "a": {"items": [], "nextPageToken": "a"}}, "token loop")
expect_error({None: {"items": [{"id": "O1", "loss": 40}], "nextPageToken": "a"},
              "a": {"items": [{"id": "O1", "loss": 41}]}}, "conflicting O1")
```

不变式：每页之后 `losses` 对每个已见的不同 id 恰好有一条。O(N + P) 时间，O(U + P) 空间。

**各种分页风格的停止信号 (Stop signals by style)**

| 风格 (Style) | 示例 (Example) | 停止条件 (Stop when) |
|---|---|---|
| 令牌/游标 (Token or cursor) | `nextPageToken`, `cursor` | 令牌缺失或为 null |
| 页码 (Page number) | `?page=1, ?page=2` | 到达响应报告的最后一页（如 `total_pages`） |
| 偏移+限制 (Offset and limit) | `?offset=0&limit=10` → `offset=10` | 空页，或达到报告的总数 |
| 标志 (Flag) | `has_more: false` | 标志表示没有更多 |

用文档定义的停止信号；短页只有在文档这么说时才代表结束。（offset 分页在数据变化时会漏记录或重复，见 Section I 第 17 课。）

### II.7.3 Total per category across pages｜跨页按类别汇总（练习 2）

Problem (English): A fake API returns transactions with `id`, `category`, `amount`. Return a sorted list of `(category, total)`, counting each `id` once and following tokens until `nextPageToken` is absent.

```text
Input pages:
start: [T1 fuel 30, T2 parts 20]  next "p2"
p2:    [T2 parts 20]              next "p3"
p3:    []                         next "p4"
p4:    [T3 fuel 5]                (no next)
Output: [("fuel", 35), ("parts", 20)]
```

Approach：用 `seen_ids` 跳过已计 ID；累加到 `totals[category]`；没有 `nextPageToken` 才停；空页继续。parts 40 = T2 加了两次；只有 fuel 30、parts 20 = 在空页或第一页后停了。（完整答案，笔者补充；另加冲突检测与重复令牌保护。）

```python
PAGES = {
    None: {"items": [{"id": "T1", "category": "fuel", "amount": 30},
                     {"id": "T2", "category": "parts", "amount": 20}], "nextPageToken": "p2"},
    "p2": {"items": [{"id": "T2", "category": "parts", "amount": 20}], "nextPageToken": "p3"},
    "p3": {"items": [], "nextPageToken": "p4"},
    "p4": {"items": [{"id": "T3", "category": "fuel", "amount": 5}]},
}


def totals_by_category(fetch, max_pages=100):
    token = None
    seen_tokens = set()
    seen_items = {}
    totals = {}
    for _ in range(max_pages):
        if token in seen_tokens:
            raise RuntimeError("repeated page token")
        seen_tokens.add(token)
        page = fetch(token)
        for item in page["items"]:
            payload = (item["category"], item["amount"])
            if item["id"] in seen_items:
                if seen_items[item["id"]] != payload:
                    raise RuntimeError("conflicting duplicate " + item["id"])
                continue
            seen_items[item["id"]] = payload
            totals[item["category"]] = totals.get(item["category"], 0) + item["amount"]
        if "nextPageToken" not in page:
            return sorted(totals.items())
        token = page["nextPageToken"]
    raise RuntimeError("page limit exceeded")


assert totals_by_category(lambda token: PAGES[token]) == [("fuel", 35), ("parts", 20)]
```

**数据题提交前要能说出三件事 (Recap)**：一行输出代表什么（一个区域/一个类别）；记录何时贡献（每个订单按最新事件一次 / 每个 API id 一次）；什么证明完整（LEFT JOIN 保留每个区域；分页只在文档定义的停止信号处停）。

**面试怎么说 / How to say it**

> "I'll write this in stages so each grain is explicit: first the latest event per order, using event time with event ID as the tie-breaker, because the highest ID isn't necessarily the newest event. Then I filter to late on that latest row only, and finally I left-join from customers so every region shows up, counting order IDs and coalescing the sum to zero. If I filtered for late before ranking, I'd resurrect O3's old late event."
>
> 中文：分阶段、先排名后过滤、最大 ID 不一定最新、从 customers 左连接、COUNT 列 + COALESCE。

---

## II.8 Case Study: A Full Technical Screen, Solved Step by Step｜案例：完整技术筛选逐步求解

Source: https://www.educative.io/courses/forward-deployed-engineer/case-study-a-full-technical-screen-solved-step-by-step

这是 Section I 第 13–17 课和 II.5–II.7 的综合演练（重构的练习，不是真实评估）。**新增 / 不同 / New or different:** 三题合一的时间管理、决策日志 (decision log)、"四种'完成'"的辨析、修复他人提交、NULL 严重度的扩展。

**设定**：90 分钟、三题、可自由切换、可运行自己的代码、不显示评分权重。

| 分钟 (Minutes) | 计划 (Plan) | 实际 (Actual) |
|---|---|---|
| 0–5 | 检查三题，写契约与手算预测 | 同 |
| 5–30 | Task 1 实现 | 22:00 完成（省 3 分钟） |
| 30–55 | Task 2 SQL | 22:00–50:00（38:00 决定先修已知 bug） |
| 55–80 | Task 3 API | 50:00–72:00 |
| 80–90 | 最终验证 | 72:00–90:00（多出 8 分钟用于验证而非打磨） |

- **决策日志**：每个检查点写一行：时间、已验证什么、下一步。例："22:00 — Task 1: 4 checks pass. Switching to Task 2 early." 实时面里大声说同一句。
- 检查时发现每题都有一件必须精确保持的事：Task 1 每行都贡献然后排序；Task 2 由最新事件决定状态，之后才按区域求和；Task 3 每个不可变 ID 计一次，且只有遍历完成总数才有效。

<svg viewBox="0 0 760 210" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <rect x="0" y="0" width="760" height="210" fill="#fff"/>
  <text x="20" y="22" font-weight="bold" font-size="13">90-min screen: one invariant per task｜90 分钟筛选：每题一个不变式</text>
  <rect x="20" y="40" width="230" height="110" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
  <text x="135" y="62" text-anchor="middle" font-weight="bold">Task 1 Implementation</text>
  <text x="135" y="82" text-anchor="middle">every row adds 每行都加</text>
  <text x="135" y="100" text-anchor="middle">→ sorted, drop final zeros</text>
  <text x="135" y="130" text-anchor="middle" fill="#2e9b5a">22:00 4 checks pass</text>
  <rect x="265" y="40" width="230" height="110" rx="8" fill="#fff4e5" stroke="#d98a1c"/>
  <text x="380" y="62" text-anchor="middle" font-weight="bold">Task 2 SQL</text>
  <text x="380" y="82" text-anchor="middle">latest event governs 最新事件</text>
  <text x="380" y="100" text-anchor="middle">→ LEFT JOIN regions</text>
  <text x="380" y="122" text-anchor="middle" fill="#b3261e">30:00 east 8, north 10, no west</text>
  <text x="380" y="140" text-anchor="middle" fill="#2e9b5a">50:00 PASS</text>
  <rect x="510" y="40" width="230" height="110" rx="8" fill="#e8f7ee" stroke="#2e9b5a"/>
  <text x="625" y="62" text-anchor="middle" font-weight="bold">Task 3 API</text>
  <text x="625" y="82" text-anchor="middle">each id once 每个 ID 一次</text>
  <text x="625" y="100" text-anchor="middle">→ only stop at no token</text>
  <text x="625" y="130" text-anchor="middle" fill="#2e9b5a">72:00 total 25</text>
  <rect x="20" y="165" width="720" height="32" rx="6" fill="#f5eefc" stroke="#8a4fd0"/>
  <text x="380" y="186" text-anchor="middle">72–90 final verification; log what was NOT tested｜最终验证，记录未测试项</text>
</svg>

### II.8.1 Task 1: Inventory roll-up per warehouse and SKU｜库存汇总

Problem (English): Rows are `(warehouse, sku, delta)`. Return the net quantity per (warehouse, sku), sorted by warehouse then SKU, without final zero totals. Every row contributes (including identical rows); keep negative totals; don't modify the input.

```text
Input (illustrative fixture matching the lesson's hand prediction):
[("W1","nut",10), ("W2","bolt",4), ("W1","nut",-10), ("W1","gear",-3),
 ("W2","bolt",4), ("W1","nut",6)]
Output:
[("W1","gear",-3), ("W1","nut",6), ("W2","bolt",8)]
```

预测：W1/nut 10 → 0 → 6（重新出现）；W2/bolt 两次 4 → 8；W1/gear −3 保留。不变式：每行之后，每个键的值 = 目前 delta 之和。O(n + k log k)。

```python
def roll_up(rows):
    totals = {}
    for warehouse, sku, delta in rows:
        key = (warehouse, sku)
        totals[key] = totals.get(key, 0) + delta
    return [
        (warehouse, sku, totals[(warehouse, sku)])
        for warehouse, sku in sorted(totals)
        if totals[(warehouse, sku)] != 0
    ]


rows = [("W1", "nut", 10), ("W2", "bolt", 4), ("W1", "nut", -10),
        ("W1", "gear", -3), ("W2", "bolt", 4), ("W1", "nut", 6)]
before = rows.copy()
assert roll_up(rows) == [("W1", "gear", -3), ("W1", "nut", 6), ("W2", "bolt", 8)]
assert rows == before
assert roll_up([]) == []
assert roll_up([("W1", "x", 3), ("W1", "x", -3)]) == []
```

22:00 检查点：4 个检查全过，比预算早 → **停止打磨**，带着省下的 3 分钟转向下一题。

### II.8.2 Task 2: Open tickets and total severity per region｜按区域统计未关闭工单

Problem (English): For every region, count tickets whose **latest** status is `open` and sum their severity. Latest = greatest `event_time`; larger `event_id` wins a tie. Tickets with no events don't count. Every region appears (0, 0 if none).

```text
Input:
regions: R1 east | R2 north | R3 west
tickets: K1 R1 sev 3 | K2 R1 sev 2 | K3 R2 sev 5 | K4 R2 sev 1
ticket_events:
  1 K1 open   09-01 09:00 | 2 K1 closed 09-01 10:00 | 3 K1 open 09-01 10:00
  4 K2 open   09-01 08:00
  5 K3 open   09-01 07:00 | 6 K3 closed 09-01 12:00 | 7 K3 open 09-01 06:00
  (K4 has no events; west has no tickets)
Output:
('east', 2, 5)
('north', 0, 0)
('west', 0, 0)
```

**第一次尝试（30:00）**：直接连接 + `WHERE status = 'open'` → east 8、north 10、west 缺失。与手算预测（east 5 = K1 3 + K2 2，north 0，west 0）对比立即发现：east 8 = K1 的 3 被加两次（扇出 (fan-out)）；north 10 = K3 两条旧 open 事件被计入（按历史过滤）；west 消失 = 内连接。三个常见 SQL 失败各有已知修法。

**38:00 决策**（测验答案 B）：Task 3 还没基线，但修复已知且约 5 分钟 → 先应用修复、重跑检查，再转 Task 3。错误选项：直接放弃 Task 2；重写已通过的 Task 1；在 Task 2 上加大量边界测试。

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE regions (region_id TEXT PRIMARY KEY, name TEXT);
CREATE TABLE tickets (ticket_id TEXT PRIMARY KEY, region_id TEXT, severity INTEGER);
CREATE TABLE ticket_events (event_id INTEGER PRIMARY KEY, ticket_id TEXT, status TEXT, event_time TEXT);
INSERT INTO regions VALUES ('R1','east'), ('R2','north'), ('R3','west');
INSERT INTO tickets VALUES ('K1','R1',3), ('K2','R1',2), ('K3','R2',5), ('K4','R2',1);
INSERT INTO ticket_events VALUES
  (1,'K1','open','2026-09-01 09:00'), (2,'K1','closed','2026-09-01 10:00'),
  (3,'K1','open','2026-09-01 10:00'), (4,'K2','open','2026-09-01 08:00'),
  (5,'K3','open','2026-09-01 07:00'), (6,'K3','closed','2026-09-01 12:00'),
  (7,'K3','open','2026-09-01 06:00');
""")

query = """
WITH ranked AS (
    SELECT e.*, ROW_NUMBER() OVER (
        PARTITION BY ticket_id ORDER BY event_time DESC, event_id DESC) AS rn
    FROM ticket_events e
),
latest AS (SELECT * FROM ranked WHERE rn = 1),
open_tickets AS (
    SELECT t.ticket_id, t.region_id, t.severity
    FROM tickets t
    JOIN latest l ON l.ticket_id = t.ticket_id
    WHERE l.status = 'open'
)
SELECT rg.name,
       COUNT(o.ticket_id) AS open_count,
       COALESCE(SUM(o.severity), 0) AS total_severity
FROM regions rg
LEFT JOIN open_tickets o ON o.region_id = rg.region_id
GROUP BY rg.name
ORDER BY rg.name;
"""
assert db.execute(query).fetchall() == [("east", 2, 5), ("north", 0, 0), ("west", 0, 0)]
```

- K1 最新 = 事件 3（10:00 平局，ID 大者）→ open；K3 最新 = 事件 6（12:00 closed）——ID 最大的 7 是更早的 open；K4 无事件。
- **扩展：严重度未知 (NULL severity)**：若 K3 最新为 open 且 severity 为 NULL，SUM 忽略 NULL → north 悄悄报 0，看起来像已知总数。更安全的最后一列：

```sql
CASE WHEN COUNT(o.ticket_id) > COUNT(o.severity) THEN NULL
     ELSE COALESCE(SUM(o.severity), 0) END AS total_severity
```

此时只能说 east 是"**已知**总数最大"，不能说 east 总体最大（north 的真实总数可能更大）。

### II.8.3 Task 3: Paginated incident cost total｜分页事件成本合计

Problem (English): Sum `cost` across all incidents from a paginated endpoint. Follow `nextPageToken` until it is absent. An incident `id` never changes; the same `id` on two pages is one incident.

```text
Input pages:
start: [I1 12, I2 8]  next "b"
b:     []             next "c"
c:     [I2 8, I3 5]   (no next)
Output: 25        # wrong answers: 33 (I2 twice), 20 (stopped at empty page)
```

```python
PAGES = {
    None: {"items": [{"id": "I1", "cost": 12}, {"id": "I2", "cost": 8}], "nextPageToken": "b"},
    "b": {"items": [], "nextPageToken": "c"},
    "c": {"items": [{"id": "I2", "cost": 8}, {"id": "I3", "cost": 5}]},
}


def total_cost(fetch, max_pages=100):
    token = None
    seen_tokens = set()
    costs = {}
    for _ in range(max_pages):
        if token in seen_tokens:
            raise RuntimeError("repeated page token")
        seen_tokens.add(token)
        page = fetch(token)
        for item in page["items"]:
            if item["id"] in costs and costs[item["id"]] != item["cost"]:
                raise RuntimeError("conflicting duplicate " + item["id"])
            costs[item["id"]] = item["cost"]
        if "nextPageToken" not in page:
            return sum(costs.values())
        token = page["nextPageToken"]
    raise RuntimeError("page limit exceeded")


assert total_cost(lambda token: PAGES[token]) == 25
```

**四种"完成"的含义 (Four meanings of "finished")**——改变 page c 的一处：

| 情况 (Case) | 结果 (Result) | 是否正确 (Correct?) |
|---|---|---|
| 在空页 b 停止 | 20 | 错：I3 从未取回 |
| page c 重试耗尽仍失败 | 已有进度 20 | 无完整结果 → **抛错，不返回 20** |
| page c 确实为空且无令牌 | 20 | 正确且完整 |
| page c 返回 I2 cost 9 | — | 同 ID 两个成本 → 抛错（选一个等于发明规则） |

三种情况都产生数字 20——**数字本身无法区分，只有停止条件和请求轨迹可以**。

**最终验证（72–90）**——用多出的时间验证而不是打磨：Task 1 重跑全部检查（重复行相加、中途归零后重新打开）；Task 2 确认平局规则那一行在、west 显示 0, 0；Task 3 确认 25 与手算一致、没有代码路径提前返回；全部已提交保存、无改变输出的调试打印。若最后一次运行破坏了之前通过的东西，**先撤销最后一次改动**，最后五分钟不要开始新修复。

决策日志最后一行最重要："90:00 All three submitted. Not tested: a NULL severity in Task 2 and API failures in Task 3." ——诚实说明没验证的部分。

**成功要素**：先预测后写代码（Task 2 的每个不一致都靠对比手算答案发现）；每个失败指向一条规则（east 8 = 扇出，north 10 = 历史而非最新，缺 west = 内连接）；检查点决定时间；结论与证据匹配（"已知总数最大"、"因为令牌缺失所以完整"可辩护，"看起来对"不行）。

### II.8.4 Practice: Repair a submission｜修复他人的提交

Buggy submission（返回 sample 20、repeat 4）：

```python
def total_cost(fetch):
    token = None
    total = 0
    while True:
        page = fetch(token)
        if not page["items"]:
            break                       # BUG 1: an empty page is not the end
        for item in page["items"]:
            total += item["cost"]       # BUG 2: the same id is added twice
        if "nextPageToken" not in page:
            break
        token = page["nextPageToken"]
    return total
```

先读 FAIL 输出再读代码："got 20" 说明跳过了页（空页提前停止）；"got 4" 说明同一 id 计了两次。修复：删掉空页 break，只在没有 `nextPageToken` 时停止；按 id 存成本，最后求和（即 II.8.3 的解法），并加重复令牌和页数上限保护。

```python
REPEAT = {None: {"items": [{"id": "X", "cost": 2}], "nextPageToken": "y"},
          "y": {"items": [{"id": "X", "cost": 2}]}}
assert total_cost(lambda t: PAGES[t]) == 25    # using the fixed version from II.8.3
assert total_cost(lambda t: REPEAT[t]) == 2
```

**面试怎么说 / How to say it**

> At a checkpoint: "Twenty-two minutes in: task one passes all four checks, including the zero-then-reopen case. I'm moving to the SQL task now and banking the time."
>
> When the SQL mismatches: "My hand prediction was east 5, but I'm getting 8, so K1's severity is counted twice: that's join fan-out. North is 10 because I'm filtering history instead of the latest event, and west is missing because of the inner join. The fix is small, so I'll rank first, keep row number one, and left-join from regions before moving on."
>
> Final summary: "All three are submitted. Task three returns 25, matching my prediction, and it only stops when the token is absent. What I didn't test: NULL severities in task two and network failures in task three."
>
> 中文：检查点报告进度并决定转题；用手算预测对比定位三个 SQL 错误；最终总结说明未测试项。

---

## 速查 / Cheat sheet

| # | 要点 (Takeaway) | English one-liner |
|---|---|---|
| 1 | 面试官只能给你**可见的**东西打分：复述契约、说假设、测边界、说清未测项 | Interviewers can only score what you make visible. |
| 2 | Foundry = 数据+工作流平台；Ontology = 对象、链接、带校验的动作；AIP = LLM/agent/eval 层；Gotham = 国防情报侧重；Apollo = 持续交付 | Foundry integrates, the Ontology models objects/links/actions, AIP adds LLMs, Apollo deploys. |
| 3 | 运营完整 = 具名用户的决策 + 被允许的动作 + 可验证的状态变化；AI 建议既不校验也不执行 | A suggestion neither validates nor executes; only the governed action changes state. |
| 4 | Ontology 写回编辑默认不覆盖源系统，需显式 webhook/导出 | Writeback edits don't update the source system unless an integration is configured. |
| 5 | 流程因人而异：报道的流程 ≠ 你的流程；五类技术轮是准备池，不是预约 | Prepare from the reported pool; schedule from your own invitation. |
| 6 | 默认不用任何候选人 AI；转录同意 ≠ 候选人许可；能力 ≠ 授权 | Default to no AI; employer transcription consent isn't candidate permission. |
| 7 | 资深候选人仍需练限时编码和陌生代码；资历不证明当前熟练度 | Tenure doesn't prove current coding fluency; still practice timed implementation. |
| 8 | 讲经历：我做了什么 / 谁做了决定 / 证据 / 局限；不编造或夸大指标（9→2 ≠ "节省 78% 工作量"） | Keep the counts and windows; don't turn incident counts into workload savings. |
| 9 | Why Palantir = 经历 → 偏好 → 职位原文中的具体连接 → 为什么 FDSE；承认没用过 Foundry | Connect a real decision to specific posting language; be honest about product experience. |
| 10 | 使命/伦理：区分公司说法、带日期的批评、技术保障、个人边界、未解问题；访问控制+日志 ≠ 用途可接受 | Access controls and audit logs don't make an authorized purpose acceptable. |
| 11 | 时间盒：先可运行基线再优化；第 25 分钟没基线就写最简版本；实时面时间盒是协调点 | Baseline before optimization; timeboxes are coordination points in a live screen. |
| 12 | 实现题：澄清顺序/部分满足/相等/是否修改输入；写不变式；单独测相等边界（< vs <=） | Pin down order, all-or-nothing, equality and mutation; test the exact boundary alone. |
| 13 | 有负数时滑窗失效 → 前缀和 + 哈希，`{0: 1}` 初始化、先查后插 | With negatives, use prefix sums: seed {0:1}, query before insert. |
| 14 | 拓扑排序 Kahn O(V+E)，输出少于 V 即有环；等权最短路用 BFS，入队即标记；状态可能要加维度 | Kahn's for dependencies; BFS for unweighted shortest paths; extend state when needed. |
| 15 | SQL：先定粒度；ROW_NUMBER + 平局键选最新完整行；先排名后过滤状态；LEFT JOIN 条件放 ON；COUNT(列)；NULLIF 防除零 | Fix grain first; rank then filter; put right-table filters in ON; NULLIF the denominator. |
| 16 | DISTINCT 掩盖症状：SUM(DISTINCT) 合并合法事实；MAX 回连有平局问题 | Repair grain, not arithmetic; DISTINCT hides the bug. |
| 17 | 分页：游标不透明、带快照、只在 next 为 null 时停、空页不停、按 ID 去重并检测冲突、只重试瞬时错误、**绝不返回部分结果** | Stop only at the documented signal; dedupe by ID; never return a partial aggregate. |
| 18 | 终止游标证明遍历结束；不可变快照才证明数据稳定 | A null cursor proves traversal ended; a snapshot guarantee proves stability. |
| 19 | 被打断前记检查点（契约、代码状态、已跑检查、下一步）；"打算测"≠"已通过" | Write a one-line checkpoint before switching; intended isn't passed. |
| 20 | 三题筛选：先看全部题、手算预测、决策日志、最后 10 分钟只验证、总结时说出未测项 | Inspect all tasks, predict by hand, log decisions, reserve final verification, name what's untested. |
