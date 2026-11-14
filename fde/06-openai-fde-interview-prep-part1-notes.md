# OpenAI FDE Interview Prep, Part 1: Role, Stack & Design｜OpenAI FDE 面试准备（上）：角色、技术栈与设计

> 课程 Course I: *OpenAI FDE Interview Prep*（Educative）— 第 1–19 课（角色 Role、平台 Platform、设计与证明 Design & Proof）
> 课程 Course II: *Forward Deployed Engineer for AI Systems* 的 OpenAI 模块 — 只记与 Part I 不同/新增的内容
>
> 全课通用的项目故事结构 (project story structure)：**customer → problem → build → proof → handoff**（客户 → 问题 → 构建 → 证据 → 交接）。
> 全课通用的自评四维度 (self-assessment dimensions)：证据纪律 (evidence discipline)、技术判断 (technical judgment)、客户所有权 (customer ownership)、表达清晰 (clarity)。

---

# Section I — OpenAI FDE Interview Prep

## 1. Preparing for the OpenAI FDE Role｜为 OpenAI FDE 角色做准备

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/preparing-for-the-openai-fde-role

### 要点 / Key ideas

**案例 Cedar Service Desk（服务台）**：发起人 (sponsor) 给领导转发 "12/12 successful answers, let's roll it out to everyone"。原型 (prototype) 用复制来的 FAQ 生成回复草稿，12 个问题是发起人自己挑的 (hand-picked)。第二天第二个员工打不开工具——它只跑在开发者的笔记本上。**草稿没问题，但部署 (deployment) 根本不存在。**

**OpenAI FDE 拥有什么 (What an OpenAI FDE owns)**：
- OpenAI 把 FDE 团队定位为"客户交付 (customer delivery) 与核心平台开发 (core platform development) 的连接点"，把研究突破变成生产系统。
- 职位描述 (job posting)：FDE 拥有 发现 (discovery)、技术范围界定 (technical scoping)、系统设计 (system design)、构建 (build)、生产上线 (production rollout)，与客户工程团队和领域团队合作；"from first prototype to stable production"，直接写代码，深度嵌入 (embedded) 客户团队。
- 成功指标 (success measures)：**生产采用 (production adoption)**、**可衡量的工作流影响 (measurable workflow impact)**、**驱动评测的反馈 (eval-driven feedback)** 进而改变产品与模型路线图。
- 评测 (eval)：对系统行为按预定期望进行的**可重复测试** (repeatable test)。好 demo 只是其中一个数据点。

Cedar 想要的单次请求流程（5 步）：员工在客户应用里提交问题 → 应用代码附上已批准的指引 (approved guidance) 并发给模型 → 模型起草 → 应用把草稿展示给员工 → 员工审核后才发送。**是应用（不是模型）决定草稿如何进入工作流。**

<svg viewBox="0 0 760 170" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="170" fill="#fff"/>
<rect x="10" y="50" width="130" height="60" rx="8" fill="#e8f0fe" stroke="#3367d6"/>
<text x="75" y="75" text-anchor="middle">1 Staff submits</text><text x="75" y="93" text-anchor="middle">员工提交问题</text>
<rect x="160" y="50" width="140" height="60" rx="8" fill="#fef7e0" stroke="#f9ab00"/>
<text x="230" y="75" text-anchor="middle">2 App adds guidance</text><text x="230" y="93" text-anchor="middle">应用附上批准指引</text>
<rect x="320" y="50" width="130" height="60" rx="8" fill="#e6f4ea" stroke="#188038"/>
<text x="385" y="75" text-anchor="middle">3 Model drafts</text><text x="385" y="93" text-anchor="middle">模型起草</text>
<rect x="470" y="50" width="130" height="60" rx="8" fill="#fef7e0" stroke="#f9ab00"/>
<text x="535" y="75" text-anchor="middle">4 App shows draft</text><text x="535" y="93" text-anchor="middle">应用展示草稿</text>
<rect x="620" y="50" width="130" height="60" rx="8" fill="#e8f0fe" stroke="#3367d6"/>
<text x="685" y="75" text-anchor="middle">5 Staff reviews</text><text x="685" y="93" text-anchor="middle">员工审核后发送</text>
<line x1="140" y1="80" x2="158" y2="80" stroke="#333" marker-end="url(#a1)"/>
<line x1="300" y1="80" x2="318" y2="80" stroke="#333" marker-end="url(#a1)"/>
<line x1="450" y1="80" x2="468" y2="80" stroke="#333" marker-end="url(#a1)"/>
<line x1="600" y1="80" x2="618" y2="80" stroke="#333" marker-end="url(#a1)"/>
<text x="380" y="145" text-anchor="middle" fill="#555">The application, not the model, controls how a draft enters the workflow｜应用而非模型控制草稿进入工作流</text>
<defs><marker id="a1" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**Demo 证明了什么？** 只证明一句精确的话："原型在 demo 条件下，对 12 个手挑的问题生成了可接受的草稿。" 说成 "100% accurate" 是把"选定集合上的可接受"混同于"真实请求上的准确率"。以下各需要独立证据：

| 维度 Dimension | 需要的证据 Evidence needed | Cedar 现状 Status |
|---|---|---|
| 草稿质量 Draft quality | 有代表性的用例上的评测 | 仅 12 个手挑问题 + 复制的 FAQ |
| 采用 Adoption | 观察目标用户在真实工作中使用 | 无人在正常工作中用过 |
| 工作流影响 Workflow impact | 新流程优于约定基线 (baseline) 且不低于质量线 | 未测 |
| 支持 Support | 有人维持服务并在故障时帮助员工 | 无人负责 |
| 交接 Handoff | 客户能访问、运行、维护你留下的东西 | 只在一台笔记本上 |

**四个所有权问题 (Four ownership questions)** —— 每个问题都把事实分成 已知 (known) / 未知 (unknown) / 提议 (proposed)，防止"合理的计划被当成结果汇报"：

| 问题 Question | 已知 Known | 未知 Unknown | 提议 Proposed |
|---|---|---|---|
| Who uses it? 谁用？ | 24 名员工，发送前审核每份草稿 | 草稿是否在有用的时刻出现；审核是否拖慢员工 | 试点 (trial)：4 名员工处理 40 个常规请求，仅草稿 (draft-only) |
| What does success mean? 成功是什么？ | 12 份 demo 草稿可接受；常规请求处理时间中位数 (median) 当前 6 分钟 | 用原型后的处理时间；无约定质量线 | 目标中位数 ≤ 4.5 分钟（含审核与修改，降 ≥1.5 分钟/25%），同口径计时；试前约定质量评分表 (rubric)、可接受错误/修改率、暂停条件 |
| Who supports it when it fails? 故障谁支持？ | 第二个员工打不开，无人负责恢复 | 谁接问题报告、维持访问、决定暂停 | 试点前指定运营负责人 (operating owner)；保留手工流程 (manual process) 作兜底。"We'll monitor it" 不告诉任何人该打给谁 |
| What remains after handoff? 交接后剩什么？ | 应用和 FAQ 只在一台笔记本 | Cedar 能否不靠那台笔记本运行、更新指引 | 代码 + 运维说明放到 Cedar 控制的地方，**观察 Cedar 工程师亲自跑一遍**。承诺访问 < 客户团队真正跑通 |

分类练习：观察到的证据 (observed evidence)（12 份草稿被接受；员工打不开笔记本应用）/ 未测的目标 (untested target)（试点方案、4.5 分钟目标）/ 未解决的所有权 (unresolved ownership)（无人同意故障恢复；客户无法独立运行）。**每类需要不同动作**：试点能测目标，但更快的流程不会自动指定运营负责人，更多被接受的草稿也不会让笔记本应用变得可用。

**给 Cedar 的建议**：暂不全员上线，改为与 Cedar 共同运行的试点 —— 范围 (scope) 4 人/40 请求/仅草稿；度量 (measurement) 对 6 分钟基线、目标 ≤4.5 分钟、事先约定质量标准；支持 (support) 第一天前有指定负责人与手工流程；交接 (handoff) 代码和说明在 Cedar 手中，Cedar 工程师能据此运行。

**课程结构（5 阶段）**：

| 阶段 Stage | 能力 Capability | 产出 Output |
|---|---|---|
| 理解角色 Understand the role | 解释端到端部署所有权 | 四问题问责评估 |
| 构建 Build bounded Python workflows | 实现并解释模型调用、工具、受控工作流 | 可运行的 Python 工作流 |
| 设计与证明 Design and prove | 论证检索 (retrieval)、故障处理、评测、安全、发布决策 | 有证据支撑的发布决策 |
| 面试答案 Interview answers | 用 customer→problem→build→proof→handoff 讲述 | 有真实结果支撑的项目故事 |
| 三个客户案例 Three cases | 讲方案、捍卫技术深度、安全判断 | 电信 (telecom)、财富管理 (wealth management)、临床 (clinical) 案例 |

平台章节以 **Responses API** 为基础，编排 (orchestration)、提示词 (prompts)、评测运行器 (eval runners) 保存在**你自己的版本化代码 (versioned code)** 中。面试章节训练你区分三件事：**你构建了什么、你证明了什么、你仍需确认什么**。

**追加情境**：发起人说下周 4 人试用；FAQ 每周五会变；开发者只在上线当天帮忙；Cedar 能提供仓库但还没转移。→ 每周五 FAQ 变化让所有权成为**每周责任**而非上线日任务；即使 40 份草稿全部被接受，也只描述试点期间那版指引下的行为。Cedar 需要有人每次更新指引后重新检查系统；"提供一个仓库"并不提供这个人。

### 面试怎么说 / How to say it in the interview

**Q: "The demo got every example right. Why not launch?"**
> "The prototype produced 12 acceptable drafts for hand-picked questions, so that's what the demo proves. I still need to see staff use it effectively in real work, and I need an operating owner and a handoff the customer can actually run. So I'd propose a four-person, 40-request, draft-only trial with agreed quality and handling-time measures, a manual fallback, and confirmed customer access."
（中文：demo 只证明 12 个手挑问题；还缺真实使用、运维负责人和客户可运行的交接；提议小范围试点。）

**Q: "The sponsor wants all 24 staff tomorrow. What would you need first?"**
> "I'd first check the staff workflow and get the operating commitments in place: who supports it, how staff keep working manually, and whether the customer can run it. A deadline tomorrow doesn't answer any of those, so I'd keep the rollout small until they're confirmed."
（中文：截止日期回答不了支持、兜底、客户可运行这三个问题，先保持小范围。）

**Q: "Can I call this production-ready?"（FAQ 每周五变，开发者不承诺长期支持，仓库未转移）**
> "Not yet. My role as the FDE is to own the path from prototype to something the customer can run. What we know is four staff will try it next week; what we don't know is who updates the guidance every Friday and re-checks the system, and whether your team can run it from the repository. I'd name an operating owner who owns the weekly FAQ update and re-eval, transfer the code into your repo, and have one of your engineers run it before the trial starts."
（中文：每周 FAQ 变更让所有权成为持续责任；先指定负责人、转移代码、客户工程师跑通。）

---

## 2. What OpenAI FDEs Ship｜OpenAI FDE 交付什么

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/what-openai-fdes-ship

### 要点 / Key ideas

**案例 Harbor Parts Distribution（零部件分销）**：上线两周后发起人 (sponsor)："服务已上线，仪表盘 (dashboard)显示 96% eval success，可以结束项目吗？" 服务从订单记录 (order records) + 已批准退货政策 (approved return policies) 为员工起草退货说明。96% 是真的，但**隐藏了唯一关键的缺陷**；"live" 也不说明 Harbor 能否离开我们独立运行。

**一个完成的项目交付 5 样东西 (Five deliverables)**：
1. 已部署的应用 (deployed application)：订单查询、政策检索、员工草稿面板 (draft panel)
2. 正确行为与工作流影响的证据 (evidence)
3. 代码与运维流程 (code and operating procedures)
4. 能部署、恢复、更新服务的 Harbor 团队 (customer team)
5. 可复用模式 (reusable patterns)，供未来项目使用

这些都不应在最后一天才作为文档任务出现，每一项都源自更早的决策。

**发现 → 交付物映射 (Discovery → deliverables)**：
- 发现：资格 (eligibility) 取决于**购买时适用的政策版本**，所以需要原始购买日期 (original purchase date)。
- 范围：仅审核后的草稿 (reviewed drafts)；员工检查并发送每封回复；**服务不能授权退款 (refund)**。

| 需求 Need | 产物 Artifact |
|---|---|
| 订单上下文 Order context | 适配器 (adapter)：把订单记录转换为草稿所需字段的应用代码 |
| 政策正确性 Policy correctness | 版本化政策内容 (versioned policy content) + 选择逻辑 + 评测用例 (eval cases) |
| 员工使用 Staff use | 在 Harbor 现有应用中的草稿面板 + 培训（检查草稿、转交例外） |
| 持续运营 Ongoing operation | 指定运营团队 + 监控 (monitoring) + 升级路径 (escalation path) |
| 兜底 Fallback | 旧手工流程全程保留 |

**系统在哪运行 (Where it runs) — 部署边界 (deployment boundary)**：Harbor 部署并控制服务应用、订单库、身份校验 (identity checks)、政策库、日志、集成凭证 (credentials)。请求草稿时，Harbor 应用拉取订单上下文、选择政策指引、把内容发到 **OpenAI 托管的 API (OpenAI-hosted API)**，收回草稿供审核。**模型执行在 OpenAI 侧**；调用 API 不会把模型搬进客户基础设施。"部署在客户基础设施上"指的是应用和集成。

<svg viewBox="0 0 760 230" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="230" fill="#fff"/>
<rect x="10" y="10" width="470" height="210" rx="10" fill="#f1f8e9" stroke="#689f38" stroke-dasharray="5,4"/>
<text x="20" y="30" font-weight="bold">Harbor controls｜Harbor 控制</text>
<rect x="30" y="45" width="150" height="40" rx="6" fill="#fff" stroke="#555"/><text x="105" y="70" text-anchor="middle">Order DB 订单库</text>
<rect x="30" y="95" width="150" height="40" rx="6" fill="#fff" stroke="#555"/><text x="105" y="120" text-anchor="middle">Policy store 政策库</text>
<rect x="30" y="145" width="150" height="40" rx="6" fill="#fff" stroke="#555"/><text x="105" y="163" text-anchor="middle">Identity, logs, creds</text><text x="105" y="178" text-anchor="middle">身份/日志/凭证</text>
<rect x="240" y="70" width="210" height="90" rx="8" fill="#e8f0fe" stroke="#3367d6"/>
<text x="345" y="95" text-anchor="middle">Service app 服务应用</text>
<text x="345" y="115" text-anchor="middle">adapter + policy selection</text>
<text x="345" y="135" text-anchor="middle">draft panel 草稿面板</text>
<line x1="180" y1="65" x2="240" y2="95" stroke="#333"/>
<line x1="180" y1="115" x2="240" y2="115" stroke="#333"/>
<line x1="180" y1="165" x2="240" y2="140" stroke="#333"/>
<rect x="560" y="70" width="180" height="90" rx="8" fill="#fce8e6" stroke="#c5221f"/>
<text x="650" y="100" text-anchor="middle">OpenAI-hosted API</text>
<text x="650" y="120" text-anchor="middle">model execution</text>
<text x="650" y="140" text-anchor="middle">模型在此执行</text>
<line x1="450" y1="100" x2="558" y2="100" stroke="#333" marker-end="url(#a2)"/>
<line x1="558" y1="130" x2="452" y2="130" stroke="#333" marker-end="url(#a2)"/>
<text x="505" y="93" text-anchor="middle" font-size="11">context+policy</text>
<text x="505" y="148" text-anchor="middle" font-size="11">draft 草稿</text>
<defs><marker id="a2" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

交接文档写清边界：应用读哪些记录、什么内容跨到 API 并返回、Harbor 负责什么（部署、访问、凭证、政策更新）、API 不可用时应用怎么做。面试中要准确描述边界，**不要声称你拥有系统接触的每个环境**。

**两周观察数据 (observation packet)**：启用员工 20 人，15 人在合格工作中使用；合格请求 (eligible requests) 240 个，144 个用了起草；可比常规请求处理时间中位数 (median) 8 分钟 → 6 分钟（含审核与修改）；144 个辅助请求中 9 个需要实质修改 (material corrections)。

**分母 (denominator) 决定你能说什么**：
- 用户采用率 (user adoption) = 15/20 = **75%**（数的是人）
- 合格工作覆盖率 (eligible-work coverage) = 144/240 = **60%**（数的是工作量）—— 少数重度用户可以拉高覆盖率而不改变采用率，两者不能互代。
- 中位数降 2 分钟 = 25%。但这是**观察性对比 (observational comparison)**：不能证明因果 (causation)，不能证明例外请求改善；**2 分钟 × 144 = 288 分钟 不是总节省**——两个中位数之差不等于个体节省之和。

可辩护的结项陈述：*"Over two weeks, 15 of 20 enabled staff used drafting on eligible work, and drafting covered 144 of 240 eligible requests. For comparable routine requests, median handling time fell from 8 to 6 minutes, including review and correction. Nine assisted requests needed material correction."*

**96% 隐藏了什么**：200 个用例 = 常规 160/160 + 例外 32/40 = 192/200 = 96%。按类别切分 (slice)：常规 100%，**例外 80%**。8 个失败全部满足同一条件：原始购买日期缺失。追踪 (trace) 显示同一序列：

1. 订单记录无原始购买日期
2. **订单适配器填入今天的日期**（编造输入）
3. 政策选择用了这个编造的日期 → 选错政策版本
4. 草稿给出错误的退货资格

缺日期时期望行为是**转人工审核 (referral to manual review)**，所以流畅自信的资格草稿仍然判失败。另一个陷阱：96% 来自 200 用例评测，**不是**观察数据包。增加通过的常规用例可以抬高总分，但一个缺日期失败也不会解决。

**修复**：修第一个出错的步骤 —— 在适配器里保留"缺失"状态，并在**政策选择之前**路由到人工审核。"提示词 (prompt)里加一句 be careful with dates" 会让编造的输入原样保留。追踪指向应用代码 → 这是**集成缺陷 (integration defect)**，修复验证后再考虑升级。

**证明修复**：重跑同一套版本化评测：160/160 + 40/40（含 8 个缺日期用例正确转人工）。基准没变，8 个通过是因为系统走了转交路径。这证明了**这个回归集 (regression set)** 上的修复，不证明处处可靠，也不能成为增加自主权 (autonomy) 的理由。

**Harbor 能独立运行吗 —— 接收工程师独立完成 4 步**：
1. 按说明部署修复版本
2. 运行评测并复现记录的结果
3. 把一个缺日期请求路由到人工审核
4. 在隔离测试环境演练回滚 (rehearse rollback)，然后恢复修复版本并再次验证

结项依赖**三类独立证据**：修复后的评测结果、观察到的工作流结果、客户团队亲自运行过系统。一个通过分数无法替代另外两个。退款授权和移除员工审核仍在范围外。

**交接包 (handoff package)**：被接受的代码及其历史；部署与配置说明（**不内嵌密钥 (no embedded secrets)**）；边界文档；带更新负责人的版本化政策内容；评测材料与结果；监控、升级、兜底、恢复流程；受过培训的接收团队。

**应该延续下去的东西 (What outlasts the engagement)**：把有效模式变成可复用工具或手册 (playbooks)，并向 Research 和 Product 反馈。Harbor 的订单数据和政策文本**绝不**进共享库；可转移的是机制：缺失必填字段保持可见并在政策选择前路由；用编造的缺日期订单测试该路径；在集成边界检查政策版本选择。

**现场报告 (field report)** 要素：去除客户数据；期望 vs 实际行为；最小复现 (minimal reproduction)；版本；影响；诊断；重跑结果。精确陈述频率："原评测集 40 个例外用例中 8 个失败"描述的是评测集，不是生产流量。去向取决于诊断：本地集成修复留在本地；平台可用性问题 → Product；Research 需要能隔离模型行为的复现。

### 面试怎么说 / How to say it in the interview

**Q: "What exactly did you ship, and what evidence lets Harbor own it now?"**
> "Harbor needed help drafting return instructions from orders and approved policies. We delivered order lookup, policy retrieval, and a reviewed-draft panel inside their service app, with no refund authority. Over two weeks, user adoption was 75% and eligible-work coverage was 60%, and comparable routine median handling time fell from 8 to 6 minutes including review, with 9 material corrections in 144 assisted requests. The original 96% eval hid an 80% exception pass rate; we fixed an adapter that invented missing purchase dates, and the same 200 cases now meet expectations. Harbor's engineer then deployed, ran the eval, exercised the referral, and rehearsed rollback on their own."
（中文：分开讲 范围、采用/覆盖、处理时间、评测缺陷与修复、客户独立运行。）

**Q: "Does this mean the models run in Harbor's infrastructure?"**
> "No. Harbor runs and controls the application and its integrations. Selected authorized content goes to an OpenAI-hosted API for model execution, and a draft comes back. The handoff documents both sides of that boundary."
（中文：应用在客户侧，模型在 OpenAI 侧，交接文档写清边界。）

**Q: "Why not report this as a model failure?"**
> "Because the trace shows the adapter replaced a missing purchase date with today's date before policy selection. That's an integration defect. I'd need evidence that isolates model behavior before blaming the model."
（中文：追踪指向适配器，是集成缺陷，不是模型问题。）

**Q: "Can Harbor now remove staff review?"**
> "No. The accepted delivery is reviewed drafting, and the eval tests that scope. The fix and the customer rehearsal don't justify autonomous replies or refunds."
（中文：交付范围就是审核后草稿，修复不扩大自主权。）

---

## 3. FDE vs. Solutions Architects and Other Customer-Facing Engineers｜FDE 与解决方案架构师等客户侧工程师的区别

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/fde-vs-solutions-architects-and-other-customer-facing-engineers

### 要点 / Key ideas

练习题："You were a solutions architect. Why should we believe you can do this job?" —— **头衔 (title) 不证明准备度**。要讲清你拥有什么、你构建了什么、你的参与何时结束。

**职责授权 (mandate)**：一个人被期望并被授权去推进到底的结果。比较两个角色的**三个轴 (three axes)**：

| 轴 Axis | 含义 Meaning | FDE |
|---|---|---|
| 所有权 Ownership | 哪个结果、哪些决策归他 | 宽：discovery → scoping → design → build → production rollout |
| 实现 Implementation | 亲自设计/构建/测试/运维多少 | 需要时写全栈生产代码 |
| 时机 Timing | 何时加入、什么结束他的参与 | 到生产采用与被接受的运营为止 |

**案例 Alder Field Services**：调度员 (dispatch staff) 在现有调度应用中的**只读预约查询 (read-only appointment lookup)**，覆盖 East / Central / West 三个队列。修改预约和自主发消息不在授权范围。

证据包（先不看头衔）：已批准的组件设计（应用边界、身份方案、集成设计）；240 行预约查询适配器 (adapter) + 配置说明；发起人看到 demo 成功；**客户工程团队独立部署**演练版本 (rehearsal build)并执行 60 次计划查询（每队列 20）；结果 East 20/20、Central 20/20、**West 2/20（18 次拒绝访问 access denials）** = 42/60。原因：演练服务身份 (service identity) 缺 West 队列权限 (entitlement)。

加上头衔：销售工程师 (sales engineer) 最先加入、收集需求、做 demo；解决方案架构师 (solutions architect) 出设计；解决方案工程师 (solutions engineer) 写适配器；ML 工程师做了两个检索配置 (retrieval configurations)的可复现对比；客户工程团队跑演练。

**结论**：证据包证明了**各自的贡献 + 客户独立演练能力**，但**没有建立整体交付所有权**。客户工程团队能跑演练 ≠ 同意配置 West 权限或运营该工作流。没人接受生产交付责任。

| 角色 Role | 通常关注 Typical focus | Alder 上的贡献 | 边界 Where it ends |
|---|---|---|---|
| 解决方案架构师 Solutions architect | 架构契合、约束、集成设计、技术风险；发现/设计期加入 | 应用边界与身份方案（客户控制访问） | 若止于设计批准，则比 FDE 窄；若也实现、协调权限变更、领导验证、推到被接受的运营 → 就是 FDE 工作，无论头衔 |
| 解决方案/销售工程师 Solutions / sales engineer | 技术发现、demo、POC、为购买决策做验证 | 销售：需求+demo；解决方案：240 行适配器+帮助客户准备演练 | 适配器存在不说明谁接受剩余上线工作 |
| ML / 研究工程师 ML / research engineer | 模型服务、数据管道、评测、模型性能；研究想法 | 可复现的检索配置对比 | 支持关于检索行为的结论，不隔离模型行为，不负责权限/采用/运营 |
| FDE | 客户工作流直到上线 | （该项目缺这个角色） | 协调缺失的承诺 |

**最早加入或代码最多 ≠ 所有者**。240 行标识的是一个产物，不是作者的授权。图示是"局部终点线 (local finish lines)"：架构师认为设计完成，解决方案工程师认为适配器已交付，客户工程团队没同意负责队列配置 —— 各自合理，合起来工作流没有通往生产的路线。**拒绝访问是症状，缺失的负责人才是它一直没修的原因。**

<svg viewBox="0 0 760 220" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="220" fill="#fff"/>
<text x="10" y="20" font-weight="bold">Local finish lines at Alder｜Alder 的局部终点线</text>
<text x="130" y="45" text-anchor="middle">Discovery 发现</text>
<text x="260" y="45" text-anchor="middle">Design 设计</text>
<text x="390" y="45" text-anchor="middle">Build 构建</text>
<text x="520" y="45" text-anchor="middle">Rehearsal 演练</text>
<text x="660" y="45" text-anchor="middle">Rollout/Ops 上线运营</text>
<rect x="70" y="60" width="120" height="24" fill="#e8f0fe" stroke="#3367d6"/><text x="130" y="77" text-anchor="middle">Sales eng 销售工程</text>
<rect x="200" y="92" width="120" height="24" fill="#fef7e0" stroke="#f9ab00"/><text x="260" y="109" text-anchor="middle">Architect 架构师</text>
<rect x="330" y="124" width="120" height="24" fill="#e6f4ea" stroke="#188038"/><text x="390" y="141" text-anchor="middle">Solutions eng 适配器</text>
<rect x="330" y="156" width="120" height="24" fill="#f3e8fd" stroke="#8e24aa"/><text x="390" y="173" text-anchor="middle">ML eng 检索对比</text>
<rect x="460" y="124" width="120" height="24" fill="#e0f7fa" stroke="#00838f"/><text x="520" y="141" text-anchor="middle">Customer eng 演练</text>
<rect x="600" y="60" width="120" height="120" fill="#fce8e6" stroke="#c5221f" stroke-dasharray="5,4"/>
<text x="660" y="110" text-anchor="middle" fill="#c5221f">No accepted owner</text>
<text x="660" y="128" text-anchor="middle" fill="#c5221f">无人接受</text>
<text x="380" y="205" text-anchor="middle" fill="#555">West: 2/20 — access denial is the symptom; the missing owner is the cause｜拒绝访问是症状，缺负责人是原因</text>
</svg>

**怎么补上缺口**：在承诺生产日期前明确依赖 (dependencies)和负责人 —— 记录 West 需要演练身份缺少的权限（保留分队列结果）；问客户工程谁有权授予、谁验证配置，**记录对方的接受**而非假设；约定谁领导上线（依赖、准备度检查 (readiness checks)、客户验收 (customer acceptance)、决策）；验证 = 只读范围不变下重跑三个队列的计划查询。注意：**交付所有权本身不授予修改客户访问的权限**，访问变更仍需授权人批准和执行。

**三种证据选择偏差 (evidence selection biases)**：

| 偏差 Bias | 定义 | Alder 中的错误说法 |
|---|---|---|
| 选择偏差 Selection bias | 用方便的子集判断 | "只用 East 和 Central 评估三个队列的准备度，因为容易访问" |
| 幸存者偏差 Survivorship bias | 只数成功的 | "只算 42 次成功，排除 18 次拒绝，所以流程完美" |
| 近因偏差 Recency bias | 过度看重最新结果 | "我刚看到的一次成功应比 60 次完整演练更重要" |

**把背景映射到角色**：OpenAI 面试指南说**不看重资历 (not credential-driven)**，想了解每位候选人的背景和贡献。角色要求：在模糊中交付 (delivery under ambiguity)、生产级代码、与工程师和客户干系人清晰沟通。
- 架构背景：展示设计与风险决策 + 你拥有的实现和上线
- 解决方案/销售工程：把发现与沟通连到购买决策之后的生产工作和结果
- ML/研究：把技术实验连到客户工作流与采用
- 产品工程：展示与用户直接合作和范围决策
- **只声称你的项目证据支持的职责与结果**

对比两种说法：弱 "I owned production delivery of an appointment assistant." vs 强（可核查）："I implemented the appointment-lookup adapter and configuration instructions and helped customer engineering prepare an independent rehearsal. They deployed the build and ran 60 lookups; 42 returned the expected records, while 18 West attempts were blocked by a missing entitlement. I demonstrated integration implementation and customer enablement. I have not yet owned rollout through to accepted operation." —— 命名产物、区分个人工作与客户行动、说清工作止于何处，且不缩小实现。

### 面试怎么说 / How to say it in the interview

**Q: "You were a solutions architect / engineer. How is your experience relevant to FDE work rather than simply your previous title?"**
> "At Alder, dispatch staff needed read-only appointment lookup in their existing app across three queues. I wrote the 240-line adapter and configuration instructions; the architect owned the component design. I helped customer engineering deploy and run the rehearsal themselves: 60 attempts, 42 expected results, and 18 West access denials from a missing entitlement. That supports integration implementation and customer enablement. Rollout and operating ownership were never accepted, so I wouldn't claim completed production delivery, and that delivery boundary is exactly what I want to own next."
（中文：按 客户→问题→构建→证据→交接 讲，区分个人与客户行动，诚实说明缺口。）

**Q: "What did the customer do independently?"**
> "Customer engineering deployed the rehearsal build and ran all 60 scheduled lookups without me running them. That shows they can operate the rehearsal, but it doesn't mean anyone agreed to provision West access or run the workflow in production."
（中文：客户独立演练 ≠ 接受运营责任。）弱回答 "The remaining issue was just customer permissions" 把阻塞依赖轻描淡写，也没说谁接受修复。

**Q: "What did you personally implement or decide?"**
> "I wrote the adapter and its configuration instructions. The agreed scope was read-only lookup across three queues, with no changes or autonomous messages. I didn't make that scoping decision, so I'd claim implementation within it."

**Q: "Which part of end-to-end delivery have you not demonstrated?"**
> "Rollout and operation. The rehearsal exposed the entitlement dependency, but nobody had accepted ownership of fixing it. The next agreement needs an authorized access owner, a rollout lead, and verification before anyone commits to production."

---

## 4. Inside OpenAI's Forward Deployed Engineering Team｜OpenAI FDE 团队内部协作

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/inside-openais-forward-deployed-engineering-team

### 要点 / Key ideas

**反例**：Larch 的 FDE 在客户拜访前一周给六个团队发消息："Product, Research, Partnerships, GRC, Security, GTM: Larch is blocked. Please fix before launch. I've told the sponsor we're launching during the visit." 几天后供应商导出 (supplier export) 仍缺失，没人同意修任何东西。**给了所有人紧迫感，却没给任何人任务。**

练习题："How do you move a blocked deployment through people you don't manage?" 强回答：把每个阻塞 (blocker)变成**具体请求**，让某人**接受**它，说明什么证据能**关闭**它。

**FDE 的协作团队**（职位描述列出，但未公布汇报关系，也不是每个项目都参与 —— 用来构造问题，然后确认本项目谁真正决策）：

| 团队 Team | 可能的协作点 Working coordination question |
|---|---|
| Product 产品 | 评估 OpenAI 产品界面 (product surface) 上反复出现的摩擦 |
| Research 研究 | 通过内部渠道调查**可复现的**模型行为 |
| Partnerships 合作伙伴 | 合作伙伴或关系依赖 |
| GRC 治理风险合规 (governance, risk, and compliance) | 澄清保证 (assurance) 要求与相关风险接受权限 (risk-acceptance authority) |
| Security 安全 | 评估连接与访问风险 |
| GTM 市场进入 (go-to-market) | 让商业预期与已验证的范围和准备度对齐 |

客户方保留自己的权限：Larch 的客户工程师控制供应商导出，采购专员 (procurement specialists) 决定什么是有用的价格对比。

**可执行升级的五要素 (Five-part escalation)**：
1. 观察到的问题 (problem observed)
2. 对交付的后果 (consequence for delivery)
3. 证据 (evidence)
4. 需要的具体决策或帮助 (specific decision or help needed)
5. 谁跟进到底 (who follows it through)

**接受 (acceptance) 要与请求 (request) 分开记录。附带截止日期的消息不等于同意。**

**项目如何运行**：职位描述 —— 界定范围、排序交付、尽早移除阻塞、在范围/速度/质量间权衡以保护交付。难点在阶段之间的衔接：晚到的实时连接、没测过的审核步骤、没同意的负责人。

**案例 Larch（采购客户）**：首版为采购员生成**供应商报价对比草稿 (supplier-quote comparison drafts)** 供审核；采购审批和供应商消息不在范围。已批准数据快照 (snapshot) 现在可用，**实时导出 (live export) 还要 4 个工作日**，而为期 2 天的客户拜访在那之前。发起人 (sponsor)想把拜访称为上线。更好的做法：**把拜访作为快照演练 (snapshot rehearsal)**，并争取拜访后验证实时连接的明确承诺。

<svg viewBox="0 0 760 140" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11">
<rect x="0" y="0" width="760" height="140" fill="#fff"/>
<text x="10" y="18" font-weight="bold" font-size="12">Larch delivery sequence｜Larch 交付顺序 (a dependency is resolved only once verified)</text>
<g>
<rect x="10" y="40" width="95" height="50" rx="6" fill="#e8f0fe" stroke="#3367d6"/><text x="57" y="62" text-anchor="middle">1 Agree scope</text><text x="57" y="78" text-anchor="middle">约定范围</text>
<rect x="115" y="40" width="95" height="50" rx="6" fill="#e8f0fe" stroke="#3367d6"/><text x="162" y="62" text-anchor="middle">2 Requirements</text><text x="162" y="78" text-anchor="middle">确定需求</text>
<rect x="220" y="40" width="95" height="50" rx="6" fill="#e6f4ea" stroke="#188038"/><text x="267" y="62" text-anchor="middle">3 Snapshot build</text><text x="267" y="78" text-anchor="middle">快照工作流</text>
<rect x="325" y="40" width="95" height="50" rx="6" fill="#e6f4ea" stroke="#188038"/><text x="372" y="62" text-anchor="middle">4 Rehearse visit</text><text x="372" y="78" text-anchor="middle">拜访中演练</text>
<rect x="430" y="40" width="95" height="50" rx="6" fill="#fef7e0" stroke="#f9ab00"/><text x="477" y="62" text-anchor="middle">5 Live export</text><text x="477" y="78" text-anchor="middle">接入实时导出</text>
<rect x="535" y="40" width="95" height="50" rx="6" fill="#fef7e0" stroke="#f9ab00"/><text x="582" y="62" text-anchor="middle">6 Verify ready</text><text x="582" y="78" text-anchor="middle">验证准备度</text>
<rect x="640" y="40" width="110" height="50" rx="6" fill="#fce8e6" stroke="#c5221f"/><text x="695" y="62" text-anchor="middle">7 Rollout+handoff</text><text x="695" y="78" text-anchor="middle">上线与交接</text>
</g>
<text x="380" y="120" text-anchor="middle" fill="#555">Connection ≠ readiness ≠ rollout acceptance｜连接、准备度验证、上线验收是三个独立里程碑</text>
</svg>

**演练结果**：96 个用例 —— 常规报价 72/72；**双单位报价 (dual-unit quotes)**（同时有单件价和整包价）只有 12/24，另 12 个丢失价格单位。总计 84/96 = 87.5%，但双单位切片 (slice) 50%。另做可用性检查 (usability check)：10 名审核者中 **7 名在 30 秒内找不到审核控件**（审核界面属于 Larch 的应用）。总分掩盖了工作流在哪里断；即使草稿正确，找不到审核控件也无法审核。等实时导出修复不了这两个问题。

**每个发现的路由 (routing)**：

| 发现 Finding | 证据不能说明什么 | 请求 Request | 谁接受 Who accepts | 什么关闭它 Closes when |
|---|---|---|---|---|
| 导出延迟 Delayed export | 快照不能证明实时集成可用 | 接受连接工作，指定授权工程师 | 客户集成负责人 (integration owner) | 记录的实时检查显示所需报价字段到达应用 |
| 审核控件难找 Hidden review control | — | 修复 + 重复可用性检查 | Larch 应用负责人（不是 OpenAI Product，除非证据指向 OpenAI 产品界面） | 审核者对约定检查的结果 |
| 单位丢失 Missing units | 需排除本地原因 | 先本地检查源字段、转换、指令；再**受控重放 (controlled replay)**：直接提供所有报价字段、绕过导出、固定指令和模型配置 → 同样 12 个遗漏仍在 → 请 Research 调查可复现行为；另请应用负责人接受本地遏制 (containment) | Research + 应用负责人 | 调查（不是对模型内部的诊断） |

此刻**所有路由都尚未被接受** —— 请求只有在负责人接受后才成为承诺。

**嵌入客户 (embedding) 是为了什么**：理解客户需求、引导采用。现场的价值在于暴露工作流细节或拿到远程 demo 拿不到的决策。Larch 拜访议程：观察采购员不经指导找审核控件和检查草稿；问领域专家如何比较单件与整包报价（要可接受措辞的例子）；与客户工程师约定导出字段和测试流程；弄清谁审核草稿、谁处理模糊对比、交接后谁支持应用。出差：苏黎世职位要求每周 3 天办公室、出差至多 50%（仅该职位，向招聘官 (recruiter)确认）。

**现场反馈如何进入路线图**：有用的反馈能让他人**无需访问客户部署就能复现**。基于受控重放构建报告，去除供应商名和机密价格或换成批准的替代值，并确认脱敏 (sanitized)用例仍失败。报告含：工作流后果、观察集合（84/96 总体，12/24 双单位）、重放条件、代表性样例对：

```text
Input:    Supplier A quotes USD $48 per pack of 12 items.
          Supplier B quotes USD $4.20 per item.
          Compare prices while keeping currency, units, and pack quantity.
Expected: "A: USD $48 per pack of 12, equivalent to USD $4.00 per item.
           B: USD $4.20 per item. A is USD $0.20 cheaper per item."
Ambiguous (failure): "A: $48. B: $4.20."
```

还要带：确切模型标识符 (model identifier)、所有生成设置、指令版本、应用版本、重放用例 ID —— **从运行记录复制，绝不凭记忆**；重跑 96 用例并找到 12 个失败的步骤。可复用部分：检查包装数量、币种、单位保留的报价对比评测模式。反复出现的工作流需求可发给 Product（明确标注），但**不构成路线图承诺**。

**同时保持交付推进 (local plan)**：两个应用改动 —— (1) 确定性检查 (deterministic check) 每个对比都声明单位，否则转人工；(2) 让审核控件易找，重跑可用性检查验证。通过单位检查只说明字段存在，不证明对比正确。上线需满足四个条件：已验证的实时集成、修复的审核可用性、双单位用例的安全处理、被接受的运营负责人。Research 请求可以保持开放。

协调备忘录结尾的决策请求示例："Please confirm the integration verification owner, the application changes and who verifies them, and the customer decision-maker for rollout."

### 面试怎么说 / How to say it in the interview

**Q: "How do you move a blocked deployment through people you don't manage? / How will you keep delivery moving across these teams?"**
> "Larch needs reviewed quote comparisons, with purchasing and supplier messages out of scope. Because the live export is four working days away, I'd run the two-day visit as a snapshot rehearsal rather than a launch. I'd get the customer's integration owner to commit to the live check, ask Larch's app owner to fix the review control, and send the controlled unit-omission replay to Research. The rehearsal passed 84 of 96 overall but only 12 of 24 dual-unit cases, and seven of ten reviewers couldn't find the review control, so the local fixes still need verification and nobody has accepted operations yet."
（中文：每个阻塞→具体请求→指定负责人→关闭证据；区分请求与已接受的承诺。）

**Q: "Why involve Research?"**
> "Because the direct-input replay bypassed the export and kept the same 12 omissions under fixed instructions and configuration. That makes the behavior reproducible for investigation, though it doesn't prove an internal model defect."

**Q: "Why not send the review-control problem straight to Product?"**
> "Larch owns that interface, so its application owner gets the fix request. Product only hears about it if the evidence implicates an OpenAI product surface."

**Q: "The export arrives before the visit. Can you promise launch?"**
> "No. Live verification can start earlier, but quality on dual-unit quotes, review usability, and operating acceptance still need evidence before rollout."

练习：把你工作中一次笼统的升级改写成五要素形式，并写出谁必须接受它。

---

## 5. OpenAI's Mission and Deployment Philosophy｜OpenAI 的使命与部署理念

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/openais-mission-and-deployment-philosophy

### 要点 / Key ideas

**案例 Juniper Workplace Services**：已批准的员工福利助手 (benefits assistant)：解释已批准的福利文件，个人问题不让经理看到，不修改记录。发起人 (sponsor)又要第二个功能：**悄悄从员工消息推断心理健康风险 (mental-health risk)，把带姓名的分数列表发给经理**。理由："模型已经能产出分数"，"我这周下载的政策允许负责任使用"。

面试题："What would you refuse to build for a customer, and why?" 强回答依托四个公开来源，各答不同的问题，**混用是最快的弱回答**。

**使命 (mission)**：确保通用人工智能 (AGI) 造福全人类。**宪章 (Charter) 四项承诺**：

| 承诺 Commitment | 内容 Content |
|---|---|
| 广泛分配的收益 Broadly distributed benefits | 用对 AGI 部署的影响力造福所有人，避免有害用途或不当权力集中；首要信托责任 (fiduciary duty) 是对人类 |
| 长期安全 Long-term safety | 研究 AGI 安全并推动采用；若一个价值对齐、注重安全的项目先接近 AGI，OpenAI 承诺停止竞争并协助（典型触发：两年内成功概率过半） |
| 技术领先 Technical leadership | 保持强技术能力以支撑有效的安全与政策工作 |
| 合作导向 Cooperative orientation | 与研究和政策机构合作、提供公共产品；承认安全因素可能随时间减少传统发表 |

这些描述的是组织而非单个部署的规则，但给 FDE 一个看待任何功能请求的视角：**谁获益？模型出错或泄露过多时谁承担后果？受影响者能否理解并控制其数据的使用？** Juniper：员工无获益、承担全部风险、毫无发言权。

**迭代部署 (iterative deployment)**：从每个系统学习使下一个更安全，同时给社会适应时间；把安全当科学：增量步骤、持续测量、部署前后评估。缩到单个项目：先在现实用例（含难例）上离线测试 → 少数志愿者做窄任务、保留手工流程、事先约定停止规则 (stop rules) → 证据支持时才扩大。**迭代是安全学习的方式，不是让人暴露于已知缺陷的许可**；会伤害用户的缺陷要在第一步前修好。

**模型规范 (Model Spec) vs 使用政策 (usage policies)**：

| | Model Spec | Usage policies |
|---|---|---|
| 管什么 Governs | 模型**应该**如何表现（包括 API 背后的模型） | **使用者**（客户和你）可以怎么用 |
| 关键点 | 权限层级 (authority hierarchy)：root → system → developer → user → guideline；生产模型可能不完全符合规范 | 按保护对象分组：人身安全、隐私、青少年、自主决策能力 |
| 对 FDE 的含义 | developer 指令低于 system/root，不能解锁它们禁止的事；**模型照做只说明它做了什么，不说明它被允许** | 新版明确：禁止未授权聚合/监控/画像 (profiling)/分发敏感信息；限制在就业、信贷、医疗等敏感领域无人工审核地自动化重大决策 (consequential decisions)；政策不能替代法律和职业义务；新版可能先宣布后生效 |

Model Spec 层级细节：root 规则是消息无法覆盖的基础指令（只有 Model Spec 指定部分有 root 权限）；system 规则来自 OpenAI；developer 指令指导应用；user 指令表达终端用户请求；guideline 是可被上下文隐式覆盖的默认值。**引用文档、工具输出、其他不可信内容默认没有权限 (no authority)**。

**每个功能请求的五个问题 (Five build questions)**：

| 问题 Question | 来源 Source of truth | Juniper 隐蔽评分 |
|---|---|---|
| 组织目的 Organizational purpose：为何做、谁的利益算数 | Charter | ✗ 员工无收益、无控制 |
| 预期模型行为 Intended model behavior | Model Spec（配合回答是观察行为，不是许可） | 模型产出分数≠许可 |
| 服务规则 Service rules：在适用版本和协议下是否允许 | 适用的 usage-policy 版本 + OpenAI 协议 | 待核实 |
| 客户授权 Customer authorization：客户实际批准了什么访问和流程 | 客户需求与协议 | ✗ 超出批准范围（经理不能访问个人问题） |
| 外部义务 External obligations：本司法辖区与领域的法律和职业义务 | 法律与职业义务，由合格审核者回答 | 待审 |

**五个都有兼容答案时功能才算就绪**；一个缺证据不抹掉另一个已经确定的结论。隐蔽评分在到达政策问题前就**在目的和客户授权上失败**。

<svg viewBox="0 0 760 210" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="210" fill="#fff"/>
<text x="10" y="20" font-weight="bold">Five build questions, each with its own source｜五个问题，各有其权威来源</text>
<rect x="10" y="40" width="140" height="80" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="80" y="65" text-anchor="middle">Purpose 目的</text><text x="80" y="85" text-anchor="middle">Charter</text><text x="80" y="108" text-anchor="middle" fill="#c5221f">FAIL</text>
<rect x="160" y="40" width="140" height="80" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="230" y="65" text-anchor="middle">Model behavior</text><text x="230" y="85" text-anchor="middle">Model Spec</text><text x="230" y="108" text-anchor="middle" fill="#555">output ≠ permission</text>
<rect x="310" y="40" width="140" height="80" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="380" y="65" text-anchor="middle">Service rules 规则</text><text x="380" y="85" text-anchor="middle">Usage policy edition</text><text x="380" y="108" text-anchor="middle" fill="#f9ab00">verify edition</text>
<rect x="460" y="40" width="140" height="80" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="530" y="65" text-anchor="middle">Customer auth 授权</text><text x="530" y="85" text-anchor="middle">Requirements</text><text x="530" y="108" text-anchor="middle" fill="#c5221f">FAIL</text>
<rect x="610" y="40" width="140" height="80" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="680" y="65" text-anchor="middle">External 外部义务</text><text x="680" y="85" text-anchor="middle">Law / duties</text><text x="680" y="108" text-anchor="middle" fill="#f9ab00">qualified review</text>
<text x="380" y="155" text-anchor="middle">Ready only when all five have compatible answers｜五个都兼容才算就绪</text>
<text x="380" y="180" text-anchor="middle" fill="#555">Juniper covert scoring: refused on purpose + authorization before reaching policy</text>
</svg>

**哪个政策版本适用？** 发起人："这周下载的就是当前政策"。实际上提供的是**已宣布但尚未生效**的新版。下载或宣布都不会让新版成为当前版本。正确做法：核实官方适用版本与协议；以**授权和安全理由**拒绝评分；泄露的导航功能保持离线。新版生效日成为重新评估的触发点。

**政策来源记录 (source record)**：官方 URL + 保存副本；版本生效日 + 你的检索日和决策日；确切措辞与位置；为什么该版本与协议适用于此用途（或还有什么未解决）。

**95% 隐藏了什么**：常规福利问题 108/108，**模糊资格问题 (ambiguous eligibility) 只有 6/12**（另 6 个给出不该给的确定性资格答案）→ 114/120 = 95%，但模糊切片 (slice) 50%（"抛硬币"）。另一个**访问边界测试 (access-boundary test)**：20 次中 3 次泄露其他员工的问题 —— 3/20 要与 120 用例分开报告，因为测的是不同东西。**经理审批无用**：经理审核带姓名分数时，泄露已经发生。

**福利助手的更安全路径**（这些门槛是给 Juniper 的提议，不是 OpenAI 统一阈值）：
1. 从构建、工具权限和范围中移除带姓名的心理健康分数和经理报告
2. **在应用中强制员工访问边界**，调查 3 次泄露 —— 更强的模型指令无法强制谁能看谁的数据
3. 个体化或模糊的资格问题转给授权福利人员；常规解释仅提供信息，不改变保障或记录
4. 重跑 120 用例质量集和 20 用例边界集：12 个模糊用例全部转交、零泄露、常规无回退
5. 解决政策适用性、数据授权、运营所有权，然后才提议试点 (pilot)：**8 名志愿者，至多 60 个常规问题**，有监控 (monitoring)和手工流程

**有意义的人工审核 (meaningful review)**：授权人员获得证据、时间、权限和兜底，能在任何重大事情发生前**拒绝或修正**提议。**一个不能阻止动作的审核者不提供任何控制。**

**停止规则 (stop rules)**（含负责人）：跨员工泄露或未授权的重大动作 → 立即停止试点、切换手工流程、启动事故流程 (incident process)；确定性资格答案 → 暂停相关回答、调查期间转给员工；Juniper 在批准试点前指定运营、事故、福利审核、上线负责人。

**如何拒绝而不失去客户**：说清不做什么 + 会做什么。
> "I won't build named mental-health scoring or manager reports from employee messages; that falls outside the purpose we agreed. Navigation also stays offline until we fix the 3-in-20 disclosure failure. I propose approved-document explanations, private referrals to benefits staff, and aggregate measurements that exclude individual questions, plus a review of the applicable policy edition and our employee-data obligations."

升级审核不会重新打开被拒绝的功能。

### 面试怎么说 / How to say it in the interview

**Q: "What would you refuse to build for a customer, and why? / Why won't you launch both features?"**
> "Juniper authorized private benefits navigation. I'd refuse covert mental-health scoring and named manager reports, because they exceed that purpose and expose employees to sensitive inferences they never agreed to. Navigation itself stays offline for now: only 6 of 12 ambiguous eligibility cases pass, and a separate test produced 3 disclosures in 20 attempts. The policy copy the sponsor downloaded hasn't taken effect yet, so I'd get the applicable edition and our agreement reviewed, and meanwhile offer private navigation with referrals to benefits staff."
（中文：先用目的和客户授权拒绝，再用切片数据和泄露测试说明导航为何仍离线，政策版本另行核实。）

**Q: "The sponsor consents on employees' behalf and signs every report."**
> "That doesn't establish employee authorization or policy permission, and approving a report after the inference is made can't undo the disclosure. I'd keep the refusal, offer the private navigation-and-referral workflow, and request qualified review without claiming a legal outcome."

**Q: "What if quality reaches 99%?"**
> "I'd inspect the remaining failures and which slices they fall in. That could inform navigation quality, but it wouldn't authorize covert scoring or settle the access and policy questions."

**Q: "The model already produces the scores, so it's allowed, right?"**
> "A model that complies shows what it did, not what's intended or permitted. The Model Spec describes intended behavior and production models don't fully match it, and permission comes from the usage policy, the customer's authorization, and the law, not from the output."

---

## 6. The Responses API, Tool Calling, and Structured Outputs｜Responses API、工具调用与结构化输出

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/the-responses-api-tool-calling-and-structured-outputs

### 要点 / Key ideas

**案例 Northstar Equipment Services**：只读 (read-only) 对比工单 NS-104 和 NS-209，说哪个先处理。两个工单记录形状都正确，模型仍给出两个错误答案。**Bug 在应用如何把结果和调用匹配**。背景：每月 18,000 个请求，基线 (baseline)处理时间 9 分钟；本构建只读授权工单并起草对比，没有更新、排程、积分 (credits)、回电的函数或凭证。

```python
calls = {"call_A": "NS-104", "call_B": "NS-209"}
finished = [  # results arrive in completion order, not call order
    {"call_id": "call_B", "ticket_id": "NS-209", "status": "callback_due"},
    {"call_id": "call_A", "ticket_id": "NS-104", "status": "awaiting_part"},
]
# Positional zip(calls, finished) -> call_A gets callback_due, call_B gets awaiting_part (swapped)
```

**按位置配对 (positional pairing)** 让 NS-104 拿到回电记录、NS-209 拿到缺件延迟 —— 在模型读之前就错了。**没有任何指令能找回结果构建器丢掉的身份 (identity)**，修复属于应用代码。

**第一次 Responses API 调用**：
- Python SDK 是 `openai` 包；`responses.create` 生成，`responses.retrieve` 取回存储的响应。Python 3.11+，虚拟环境 (virtual environment)，`pip install openai pydantic`，密钥和模型走环境变量，**绝不提交真实密钥**；跑通后 `pip freeze > requirements.lock.txt` 锁定版本。
- 客户端：`OpenAI(timeout=30.0, max_retries=0)` —— 每次请求 30 秒上限，`max_retries=0` 让每次尝试可见。
- 指令和模型在代码里版本化（如 `CONFIG_VERSION = "northstar-responses-v1"`）；**指令描述任务，后面的函数强制权限**。
- 日志只记元数据和 item 类型，不记凭证或工单正文。
- 响应 = 不同类型输出项 (output items) 的列表：message、function_call、reasoning、refusal 等。status 可为 `completed / failed / in_progress / cancelled / queued / incomplete`。非 completed 或有 refusal → 先 Stop 再解析。
- `output_text` 只拼接文本；请求的工具调用只出现在完整 output 列表里。**生成完成 ≠ 工作流完成**：有 function_call 就必须执行工具。
- `store=False` 不保存响应；默认 `store=True`，默认保存 30 天。这不是完整的保留策略 (retention policy)，发送客户数据前查项目的数据控制。
- Playground 最快迭代指令/工具/输出 schema；跑通后移到代码中进版本控制 (version control)，让测试可重跑。

**对话状态 (conversation state) 三种方式**：

| 方式 Method | 说明 | 注意 |
|---|---|---|
| 自己回放 Replay items in `input` | 把之前的输入和输出项放回 input（Northstar 用此法 + `store=False`） | 推理模型要保留**所有**输出项包括 reasoning items；`store=False` 时 reasoning 默认带 `encrypted_content` 可回放 |
| `previous_response_id` 链接 | 按响应 ID 继续 | **每次重发 instructions**（不会延续）；链接不让早先上下文免费（看 token 用量） |
| Conversation 对象 | 自动累积 items | 只存历史不存业务状态；**不要和 previous_response_id 混用** |

**历史从不携带权限 (history never carries authority)**。权限放在可信应用状态 (trusted application state)：`Auth(organization_id, allowed_tickets)` 来自已验证登录；NS-777 属于别的组织用于测试拒绝。

**工具循环 (tool loop)**：函数调用 = 模型请求你的代码运行你声明的函数。声明给模型词汇，**你的分发器 (dispatcher) 负责验证、授权、执行**。每轮：带 tools 发送历史 → 模型返回 0 或多个 `function_call`（含 `call_id`、`name`、JSON 编码的 `arguments`）→ 代码执行每个调用并追加带**相同 call_id** 的 `function_call_output` → 发送更新的历史，直到模型返回最终消息。

<svg viewBox="0 0 760 260" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="260" fill="#fff"/>
<rect x="20" y="30" width="200" height="200" rx="10" fill="#e8f0fe" stroke="#3367d6"/>
<text x="120" y="52" text-anchor="middle" font-weight="bold">Application 应用</text>
<text x="120" y="80" text-anchor="middle">trusted Auth 可信身份</text>
<text x="120" y="105" text-anchor="middle">dispatcher: validate,</text>
<text x="120" y="122" text-anchor="middle">authorize, execute</text>
<text x="120" y="150" text-anchor="middle">correlate by call_id</text>
<text x="120" y="167" text-anchor="middle">按 call_id 关联</text>
<text x="120" y="195" text-anchor="middle">accept(): content check</text>
<text x="120" y="212" text-anchor="middle">业务验收</text>
<rect x="540" y="30" width="200" height="200" rx="10" fill="#e6f4ea" stroke="#188038"/>
<text x="640" y="52" text-anchor="middle" font-weight="bold">Responses API</text>
<text x="640" y="90" text-anchor="middle">model decides:</text>
<text x="640" y="108" text-anchor="middle">function_call(s) or</text>
<text x="640" y="126" text-anchor="middle">final message</text>
<text x="640" y="170" text-anchor="middle">text.format = JSON Schema</text>
<text x="640" y="188" text-anchor="middle">结构化输出（形状）</text>
<line x1="220" y1="70" x2="538" y2="70" stroke="#333" marker-end="url(#a6)"/>
<text x="380" y="63" text-anchor="middle">history + tools + instructions</text>
<line x1="538" y1="120" x2="222" y2="120" stroke="#333" marker-end="url(#a6)"/>
<text x="380" y="113" text-anchor="middle">function_call {call_id, name, arguments}</text>
<line x1="220" y1="160" x2="538" y2="160" stroke="#333" marker-end="url(#a6)"/>
<text x="380" y="153" text-anchor="middle">function_call_output {same call_id}</text>
<line x1="538" y1="205" x2="222" y2="205" stroke="#333" marker-end="url(#a6)"/>
<text x="380" y="198" text-anchor="middle">final typed message 最终结构化答案</text>
<text x="380" y="248" text-anchor="middle" fill="#555">Ceilings: 4 model turns + 6 function calls; neither grants permission｜两个上限都不授予权限</text>
<defs><marker id="a6" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**工具声明与分发器要点**：
- 本地用 Pydantic `TicketArgs`（`extra="forbid", strict=True`，`ticket_id` 匹配 `^NS-\d{3}$`）校验参数。
- 声明一个 strict 读工具 `get_ticket`；**strict 模式要求 `additionalProperties: False` 且每个属性都 required**。**没有 organization 字段** —— 组织来自已验证会话。
- 分发器**默认拒绝 (start from a denial)**，只允许 `get_ticket`，对可信状态检查权限与组织归属，只返回公开字段。
- **拒绝信息统一 (`request_denied`)**：记录不存在、属于他组织、未知函数 —— 返回相同拒绝，不泄露 NS-777 的任何信息。
- 关联器 (correlator)：拒绝重复/缺失/意外结果，按 call_id 匹配，确认工单正是被请求的那个。

修复后的 `correlate`（课程代码，Python）：

```python
def correlate(calls, executions):
    call_ids = [c["call_id"] for c in calls]
    result_ids = [e["call_id"] for e in executions]
    # A dict would silently overwrite a duplicate, so count first.
    if len(set(call_ids)) != len(call_ids) or len(set(result_ids)) != len(result_ids):
        raise Stop("duplicate_call_id")
    # zip would silently drop a missing result; set comparison also catches a substituted ID.
    if set(call_ids) != set(result_ids):
        raise Stop("missing_or_unexpected_result")
    by_id = {e["call_id"]: e for e in executions}
    outputs = []
    for call in calls:
        execution = by_id[call["call_id"]]
        result = execution["result"]
        if result.get("ok"):
            # A matching call_id is necessary but not sufficient: the ticket must match too.
            requested = TicketArgs.model_validate_json(call["arguments"]).ticket_id
            if execution["ticket_id"] != requested or result["ticket"]["ticket_id"] != requested:
                raise Stop("ticket_identity_mismatch")
        outputs.append({"type": "function_call_output", "call_id": call["call_id"],
                        "output": json.dumps(result)})
    return outputs
```

`zip` 的两个隐患：完成顺序悄悄变成身份；长度不同时悄悄丢结果。

**循环上限**：4 个模型轮次 + 6 个函数调用，两个独立上限；**都不授予权限**，每次读仍过权限检查。`tool_choice`：`"auto"` 可答可调；`"required"` 必须调用；`"none"` 禁止。不读工单就作答会以 `missing_tool_evidence` 失败，**即使猜对了**。

**内置工具 (built-in tools)**：OpenAI 运行能力，但你仍决定发送什么数据并验证答案；`include` 参数把工具证据（搜索来源、检索段落、执行输出）与最终文本分开返回。托管工具、存储、容器都计费。

| 工具 Tool | 启用 | include 证据 | 注意 |
|---|---|---|---|
| Web search 网页搜索 | `{"type": "web_search"}` | `web_search_call.action.sources` | **绝不把工单记录放进公开搜索查询** |
| File search 文件搜索 | `{"type": "file_search", "vector_store_ids": [...]}` | `file_search_call.results` | 先建向量库 (vector store)、上传并等索引完成；`finally` 中删除 |
| Code Interpreter 代码解释器 | `{"type": "code_interpreter", "container": {"type": "auto", "file_ids": [...]}}` | `code_interpreter_call.outputs` | 沙箱容器 (sandbox container)跑 Python；只上传脱敏 (sanitized) CSV；结束删除容器和文件；**在执行输出里确认结果（如均值 7），不只看文字** |

**结构化输出 (Structured Outputs)**：在支持的模型上、生成成功时，把响应约束到你提供的 JSON Schema。旧的 JSON mode 只保证合法 JSON，不保证你的 schema。Responses API 中 schema 放在 `text={"format": FORMAT}`；`response_format` 是 Chat Completions 的参数。

严格模式 (strict mode)规则：每个对象 `additionalProperties: False`（Pydantic 也 forbid extra）；**每个字段都 required，可选值改为可空 (nullable)**：`next_step: ["string","null"]` 仍 required，对应 `str | None`；`minItems/maxItems` 限制恰好两张工单；**schema 表达不了"不重复"，由 accept 检查**。也可用 `responses.parse(text_format=TicketComparison)` 从 Pydantic 推导 schema（额外一次调用），读 `output_parsed`。

**关键：schema 控制形状 (shape)，accept 检查内容 (content)**。一个 schema 合法的答案仍可能包含 NS-777、给 NS-209 错误状态、或把 36 小时工单排第一。`accept` 检查：工单集合 = 请求集合、权限、每个状态和下一步与工具记录一致、跟进优先级（生产中优先级规则来自与客户约定的政策）。

**离线边界测试（8 项，无需 API key）**：反转结果后每个 call ID 保持自己的工单；拒绝 NS-777；拒绝额外 `organization_id` 参数；拒绝未知函数；incomplete 和 refusal 响应 Stop；拒绝含 NS-777 的 schema 合法答案；伪造持续调工具的模型，确认 4 轮后停止。修复补丁另加 3 项（重复 ID、缺失结果、互换工单内容）。

**Assistants API 已关停 → 迁移到 Responses API**：

| Assistants 概念 | Responses 对应 |
|---|---|
| Assistant 配置 | 仓库中版本化的 instructions、schema、模型设置 |
| Threads | 回放 items / response chaining / Conversation（按客户数据控制选择） |
| Runs | 你自己的有界请求-分发循环 (bounded request-and-dispatch loop) |
| Tool execution | 白名单函数 + 可信状态授权 + 关联输出 |

交接给客户：代码与配置版本、lock 文件、测试结果、数据边界、已知限制、运营团队名称。

### 面试怎么说 / How to say it in the interview

**Q: "Explain Northstar using customer → problem → build → proof → handoff." / "Why aren't strict schemas sufficient here?"**
> "Northstar needed a read-only comparison of two tickets. When completion order reversed, positional pairing swapped both results, so the model was reasoning over the wrong records. I now match every result by call ID and also check the ticket identity, and the dispatcher checks entitlement and organization from the authenticated session. The schema only fixes the shape; acceptance checks the ticket set, the statuses against the tool records, and the two-hour priority rule. I hand over versioned code, a lock file, the eleven offline checks, and the data boundaries."
（中文：按位置配对导致互换 → 按 call_id + 工单身份关联；schema 管形状，验收管内容。）

**Q: "What in that schema proves this operator owns NS-777?"**
> "Nothing. A schema can't express authorization. Ownership is checked in the dispatcher against the verified session before any record is returned, and acceptance rejects a final answer that names a ticket outside the requested and authorized set."

**Q: "Would letting the model supply organization_id simplify the tool?"**
> "The model may name a ticket ID, but it can't choose the authority the request runs under. Organization comes from the verified session and is resolved in the dispatcher."
（中文：模型可以选工单，不能选权限来源。）

**Q: "A customer still runs on the Assistants API. How do you migrate?"**
> "Assistants is shut down, so I map each piece: the assistant config becomes versioned instructions and schemas in the repo, threads become replayed items, response chaining or a Conversation depending on their data controls, runs become our own bounded loop, and tool execution becomes allowlisted functions with authorization and call-ID correlation."

---

## 7. The OpenAI Agents SDK｜OpenAI Agents SDK

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/the-openai-agents-sdk

### 要点 / Key ideas

**事故**：Northstar 操作员 B 问自己的工单，答案却依赖操作员 A 的工单证据。所有读工具的授权 (authorization)都正确 —— **泄露来自会话历史 (conversation history)，SDK 在任何工具运行前就加载了它**。

面试题："Why use the Agents SDK when you already have a working tool loop?" "代码更少"只是一半答案。SDK 接管重复性工作（跑模型轮次、调用工具、回传结果），**不决定调用者是谁、能读什么、答案是否足以被接受**。

**SDK vs 应用的职责划分**：

| SDK 编排 SDK orchestration | 应用控制 Application control |
|---|---|
| 模型轮次 Model turns | 已认证身份 Authenticated identity |
| 函数工具调用 Function-tool invocation | 每次读的权限检查 Per-read entitlement |
| 关联工具结果 Correlated tool results | 历史归属检查 History ownership checks |
| 受支持的运行终止 Run termination / interruption | 独立工具预算 Independent tool budget；业务验收 business acceptance |

SDK 归属不免除应用测试。

- **Agent**：instructions + 模型及设置 + tools 列表 + 可选类型化输出 (typed output)。
- **Runner**：循环本身。`Runner.run` 调模型、运行工具调用并追加结果、跟随 handoff 到其他 agent，模型产出无工具调用的最终输出时停止。
- 迁移到 SDK **不增加任何权限**（仍只有 `get_ticket`）。

安装：`pip install openai-agents openai pydantic`（包名 `openai-agents`，导入为 `agents`），`pip freeze` 锁定。

**一次工具调用**：

```python
@function_tool(failure_error_function=None)
async def get_ticket(ctx: RunContextWrapper[LocalContext], ticket_id: str) -> str:
    return json.dumps(ctx.context.read(ticket_id))
```

- `@function_tool` 从签名生成工具 schema。默认工具异常变成给模型的错误消息；`failure_error_function=None` 改为**抛出**，使预算 Stop 终止运行而不是到达模型（调用方收到 `agents.exceptions.UserError`，原 Stop 在 `__cause__`）。
- `RunContextWrapper` 携带本地依赖且**不进 schema**，模型只看到 `ticket_id`。
- `Runner.run(max_turns=4)`，超出抛 `MaxTurnsExceeded`。**6 次调用上限仍在本地代码**，因为一轮可请求多个调用。外层超时 (outer timeout)限制等待，但取消无法撤销已完成工作。

**会话 (Session)**：跨运行存储对话历史；每次运行前 SDK 取历史并**前置 (prepend)** 到新输入，之后存储新 items。**只选一种延续方式**：同一运行中 session 不与 `conversation_id`、`previous_response_id`、`auto_previous_response_id` 混用。第二轮可以记得第一轮，但接受当前答案前**仍做新鲜的授权读取**。

**五种状态分开 (Five kinds of state)**：

| 状态 State | 内容 | 模型可见？ |
|---|---|---|
| 模型可见历史 Model-visible history | 消息、工具调用、工具输出 | 是 |
| 本地类型化上下文 Local typed context | 认证范围、分发适配器、剩余预算、收集的证据 | 否（RunContextWrapper） |
| 返回结果 Returned result | 最终输出 | — |
| 中断运行的可恢复状态 Resumable state | RunState | — |
| 权威业务记录 Authoritative business records | 客户系统 | 否 |

把 `organization_id` 放在本地上下文不告诉模型任何东西；从工具返回或写进 instructions 才会暴露。代码是 async 的，同步网络/数据库调用会阻塞事件循环 (event loop)；每个并发测试用自己的上下文、预算、临时数据库。

**Bug**：

```python
def broken_session(database):
    return SQLiteSession("support_demo", database)  # every operator shares one history
```

**会话 ID 只选择历史，不认证调用者也不授权访问**。B 认证后拿到 A 用过的 `support_demo`，runner 把 A 的工单证据前置到 B 的输入。B 请求重新读 A 的工单时工具正确拒绝，但 A 的证据已在模型输入里。**没有任何工具改动能移除从另一条路径到达的证据。**

<svg viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="200" fill="#fff"/>
<text x="10" y="20" font-weight="bold">Owner check must come BEFORE history loads｜历史加载前先查归属</text>
<rect x="10" y="50" width="130" height="56" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="75" y="74" text-anchor="middle">Authenticated</text><text x="75" y="92" text-anchor="middle">owner 已认证主体</text>
<rect x="170" y="50" width="150" height="56" rx="8" fill="#fef7e0" stroke="#f9ab00"/><text x="245" y="74" text-anchor="middle">SessionRegistry.open</text><text x="245" y="92" text-anchor="middle">owner-bound 绑定归属</text>
<rect x="350" y="50" width="130" height="56" rx="8" fill="#e6f4ea" stroke="#188038"/><text x="415" y="74" text-anchor="middle">Model-visible</text><text x="415" y="92" text-anchor="middle">history 历史</text>
<rect x="510" y="50" width="110" height="56" rx="8" fill="#e6f4ea" stroke="#188038"/><text x="565" y="74" text-anchor="middle">Agent run</text><text x="565" y="92" text-anchor="middle">+ per-read auth</text>
<rect x="645" y="50" width="105" height="56" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="697" y="74" text-anchor="middle">Final</text><text x="697" y="92" text-anchor="middle">acceptance 验收</text>
<line x1="140" y1="78" x2="168" y2="78" stroke="#333" marker-end="url(#a7)"/>
<line x1="320" y1="78" x2="348" y2="78" stroke="#333" marker-end="url(#a7)"/>
<line x1="480" y1="78" x2="508" y2="78" stroke="#333" marker-end="url(#a7)"/>
<line x1="620" y1="78" x2="643" y2="78" stroke="#333" marker-end="url(#a7)"/>
<line x1="245" y1="106" x2="245" y2="140" stroke="#c5221f" marker-end="url(#a7)"/>
<text x="245" y="158" text-anchor="middle" fill="#c5221f">mismatch → conversation_denied</text>
<text x="245" y="175" text-anchor="middle" fill="#c5221f">(factory never runs 不加载存储)</text>
<text x="565" y="150" text-anchor="middle" fill="#555">Bug: shared "support_demo"</text>
<text x="565" y="167" text-anchor="middle" fill="#555">leaks A's evidence to B</text>
<defs><marker id="a7" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**修复：会话注册表 (SessionRegistry)** —— 把不透明会话键 (opaque conversation key) 绑定到 组织 + 操作员 + 内部 session ID；组织和操作员来自可信认证，**绝不来自客户端**：

```python
class SessionRegistry:
    def __init__(self, database, bindings=None, factory=SQLiteSession):
        self.database = database
        self.bindings = dict(bindings or {})
        self.factory = factory
        self.opens = 0

    def create(self, owner):
        key = token_urlsafe(24)
        self.bindings[key] = Binding(owner, token_urlsafe(24))
        return key

    def open(self, key, authenticated_owner):
        binding = self.bindings.get(key)
        # Reject before the factory runs, so a denied caller never loads history.
        if binding is None or binding.owner != authenticated_owner:
            raise SessionDenied("conversation_denied")
        self.opens += 1
        return self.factory(binding.session_id, self.database)
```

- 注入的 factory 和 `opens` 计数器让测试能证明拒绝发生在**触碰存储之前**。拒绝信息不泄露会话任何内容。
- 生产中 bindings 要持久化 (persisted)并做访问控制 (access control)，否则重启丢失。只给 ID 的 `SQLiteSession` 在内存；给数据库路径则落盘。SQLite 历史检测不到外部编辑、删除、重排、重放；加密包装也不保证完整性 (integrity)或顺序 —— 保护存储和备份。

**12 次回放测试 (replay tests)**：4 个操作员（A 可读 NS-104，B 可读 NS-209，C、D 什么都不能读 —— 证明隔离 (isolation)不依赖有可读工单）。1–8：每人两次合法续接；9–11：拿别人的键（B 用 A 的、C 用 B 的、D 用 A 的）；12：A 用相同绑定和数据库重启。broken 模式下 9–11 把别人的证据组装给错误调用者；修复后三者都在 factory 运行前抛 `conversation_denied`。**测试直接检查组装好的 items（模型输入本身），不管模型之后说什么**。线上可用 `RunConfig.session_input_callback` 捕获真实合并。这些测试**证明路由，不证明模型质量**。

**护栏 (guardrails)**：可以通过触发 tripwire 拒绝输入或输出、停止运行；**何时运行决定它能阻止什么**。
- 输入护栏：默认与 agent **并行**运行；`run_in_parallel=False` 时在 agent 开始前完成。
- 输出护栏：**总在 agent 完成后**运行。
- 触发抛 `InputGuardrailTripwireTriggered` / `OutputGuardrailTripwireTriggered`，调用方捕获并记为受控失败。
- Northstar：输入护栏只接受两个已知请求（"Close NS-209" 在 agent 运行前被拦）；输出护栏拒绝 `mutation_claimed=True` 的输出。

**晚到的检查无法撤销工作**：并行输入检查可能在工具已开始时仍在跑，输出检查总在之后。**都不能事后授权**；取消未完成工作也不撤销已完成工作。所以**授权留在每个工具内部**，本工作流只暴露读。

**追踪 (trace)**：记录最终答案隐藏的运行结构。默认开启；每个 agent run、模型生成、工具调用、护栏、handoff 有自己的 span；用 `with trace(...)` 组合多个 `Runner.run`。每次线上运行保留：task ID、trace ID、release、模型设置、工具调用数、任何拒绝或 tripwire、验收是否通过。Trace 能区分两个看起来相同的拒绝：一个是输入护栏拦住一切，一个是读已运行后答案才被拒。

三个易混设置，互不控制：

| 设置 Setting | 作用 |
|---|---|
| `RunConfig(trace_include_sensitive_data=False)` | 仍创建 span，但不含生成和工具 payload |
| Sessions | 决定对话 items 是否持久化到 SQLite |
| `ModelSettings(store=False)` | 阻止 Responses API 保存响应以便后续查询，不影响本地会话历史 |

**何时用 SDK**：按组件选择。多轮助手需要重复工具分发、会话延续、护栏、追踪 → SDK 合适。单次授权输入、返回一个结构化结果、无历史的抽取步骤 → 直接 Responses 调用更清晰。**选让该组件控制流最容易检查的方式。**

**Handoff**：一个 agent 把对话交给更专业的 agent；在 `handoffs` 参数列出目标，模型看到形如 `transfer_to_billing_agent` 的工具。**handoff 改变谁回应，不授予对客户系统的访问**。区分产品：`openai` 客户端做直接 API 调用；**Workspace Agents** 是可由后端系统触发的已发布 ChatGPT agent，与此 SDK 不同。

### 面试怎么说 / How to say it in the interview

**Q: "Why use the Agents SDK when you already have a working tool loop?"**
> "The SDK takes over the repetitive orchestration: model turns, tool invocation, feeding results back, handoffs, and tracing. It doesn't decide who the caller is, what they may read, or whether an answer is good enough, so identity, per-read authorization, history ownership, budgets, and acceptance stay in our code. I'd pick it per component: the multi-turn assistant benefits from sessions, guardrails, and traces, while a one-shot extraction step stays a direct Responses call."
（中文：SDK 管编排，应用管身份/授权/历史归属/预算/验收；按组件选型。）

**Q: "The read tools enforce authorization. Why did another operator's history reach the model?"**
> "The session factory picked one shared history before any tool authorization ran, so A's evidence was prepended to B's input. The fix binds each conversation to the authenticated organization and operator and rejects mismatches before retrieving history, and every fresh read still checks entitlement. Twelve replays inspect the assembled items directly: eight valid continuations, three rejected cross-owner lookups, and one restored history. I'd report those as expected results until I've run them and kept the output."
（中文：会话 ID 不是认证；历史加载前做归属检查；直接检查模型输入。）弱回答 "The SDK shared its memory, I'd tighten the prompt and filter IDs from the output" —— 模型在那之前就已收到这些 ID。

**Q: "Can an output tripwire roll back a tool action?"**
> "No. It runs after the tool work, so it can't undo an effect. Our assistant only reads; a consequential action needs authorization and approval before it executes."

---

## 8. Building a Single-Agent Workflow｜构建单 Agent 工作流（含人工审批）

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/building-a-single-agent-workflow

### 要点 / Key ideas

**事故**：12:01 UTC 审核者 (reviewer)批准一个动作：为 NS-209 在 13:00 UTC 创建内部回电任务 (callback task)（工单截止 (deadline) 14:00）。**批准有效至 12:10**。持有请求的 worker 重启，12:11 回来，在存储里看到 `approved=True`，创建了任务。回电时间没问题，**但许可已过期**。

面试题："Your agent can write to our support system. What stops it from creating a task nobody approved?"

**工具面 (tool surface)**：
- `get_ticket(ticket_id)`：检查认证组织和操作员权限后返回 NS-209
- `create_callback_task(ticket_id, callback_at)`：通过受保护适配器 (guarded adapter) 创建一条支持队列记录
- 不在工具面：打电话给客户、关闭工单、改账单、移动截止时间、切换组织

**提议 (proposal) vs 决定 (decision)**：提议 = agent 请求的动作，等待决定；决定 = 审核者批准或拒绝。**应用只有在把决定与确切的提议和当前条件（如过期时间）核对后才授予许可。**

**模型只选 ticket ID 和回电时间戳**。应用构建其余可信上下文：组织、操作员、任务范围、时钟、剩余预算、适配器。**绝不从模型接受组织 ID、审核者身份、批准标志、查询或管理命令**。准备提议前：检查工单归属与权限；要求时间戳带时区并归一化到 UTC；检查时间在 now 与 deadline 之间。

- 本地 SQLite 适配器代替队列，写是真实可检查的。**提议 ID 上的唯一约束 (uniqueness constraint)** 防重复回电行；回电、收据 (receipt)、提议状态在**一个事务 (transaction)**中提交（这是本地重复写边界，不保证外部服务）。
- 上限：4 个模型轮次 + 6 次工具读写；**两个计数器跨暂停和重启持久化**；`on_llm_start` hook 在每次请求前预留模型预算 (model budget)。
- 模型 `gpt-6-luna`：目录描述为面向专注、高量、支持函数工具任务的高效选项。**模型决定能力和成本，授权仍来自应用代码。**

**指令契约 (callback-v1)**：读 NS-209，请求一个 13:00 UTC 内部回电任务，只用提供的工具，报告返回的结果；**绝不把队列任务描述为已完成的客户电话，绝不编造收据**。版本化以便每次运行记录用了哪版。

**类型化结果 (5 字段)**：`ticket_id`（必须 NS-209）、`outcome`（`created / denied / expired / needs_review`）、归一化 `callback_at`、`action_receipt_id`（仅 created 时存在）、简短 `explanation`。Pydantic 校验器把收据和结果绑定 —— 只证明形状一致。**验收 (acceptance)再与账本 (ledger) 对比**：收据必须存在、属于此提议、记录了批准的工单和时间；其他三种结果要求提议为终态、有原因、**零回电行**。验收失败记为 acceptance failure，**绝不改写成成功**；拒绝类型化结果无法撤销已提交任务 —— 若任务已存在但答案验收失败，**保留收据并路由修复，不重试创建**。

**暂停等人工批准 (pause for human approval)**：批准必须在写函数体运行**之前**。Agents SDK 中工具设 `needs_approval=True` 会在该调用前暂停运行；待批项出现在 `result.interruptions`。`result.to_state().to_string()` 序列化 (serialized)存储；批准/拒绝后 `await RunState.from_string(agent, text)` 恢复，`Runner.run(agent, state)` 继续。

**一个待批调用跨越边界的 8 步**：

| # | 步骤 Step |
|---|---|
| 1 | `get_ticket` 返回 NS-209 和 14:00 截止 |
| 2 | 模型请求 `create_callback_task(NS-209, 13:00)`；**此时零回电行** |
| 3 | 应用存储 call ID、规范参数 (canonical arguments)、提议、序列化运行状态 |
| 4 | 已认证审核者看到动作、截止时间、提议的 12:10 过期时间 |
| 5 | 应用把决定记录到那个确切的调用和参数集 |
| 6 | Worker 取得任务独占所有权 (exclusive ownership)，重建可信依赖，恢复运行状态，应用 approve/reject |
| 7 | 适配器**在事务内**重新检查权限、参数、决定、过期 |
| 8 | 应用把类型化结果与收据或无效果记录对比 |

<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="250" fill="#fff"/>
<text x="10" y="20" font-weight="bold">Approval timeline｜审批时间线（approval expiry ≠ callback deadline）</text>
<line x1="40" y1="110" x2="730" y2="110" stroke="#333" stroke-width="2"/>
<circle cx="80" cy="110" r="6" fill="#3367d6"/><text x="80" y="90" text-anchor="middle">12:01</text><text x="80" y="135" text-anchor="middle">Decision 批准</text>
<circle cx="200" cy="110" r="6" fill="#f9ab00"/><text x="200" y="90" text-anchor="middle">12:10</text><text x="200" y="135" text-anchor="middle">Proposal expires</text><text x="200" y="150" text-anchor="middle">批准过期</text>
<circle cx="260" cy="110" r="6" fill="#c5221f"/><text x="270" y="72" text-anchor="middle" fill="#c5221f">12:11</text><text x="275" y="175" text-anchor="middle" fill="#c5221f">Resume → expired, 0 rows</text><text x="275" y="190" text-anchor="middle" fill="#c5221f">恢复执行 → 过期，零行</text>
<circle cx="480" cy="110" r="6" fill="#188038"/><text x="480" y="90" text-anchor="middle">13:00</text><text x="480" y="135" text-anchor="middle">Approved callback</text><text x="480" y="150" text-anchor="middle">批准的回电时间</text>
<circle cx="580" cy="110" r="6" fill="#8e24aa"/><text x="580" y="90" text-anchor="middle">13:30</text><text x="580" y="135" text-anchor="middle">Changed args</text><text x="580" y="150" text-anchor="middle">改参数→需新审批</text>
<circle cx="690" cy="110" r="6" fill="#333"/><text x="690" y="90" text-anchor="middle">14:00</text><text x="690" y="135" text-anchor="middle">Ticket deadline</text><text x="690" y="150" text-anchor="middle">工单截止</text>
<text x="380" y="230" text-anchor="middle" fill="#555">Check the trusted clock inside the write transaction｜在写事务内用可信时钟检查</text>
</svg>

**规范参数 (canonical arguments)**：解析后参数的稳定文本形式（排序 JSON，含归一化工单和时间戳），提议和决定都存储它。恢复时，待批调用的 operation、call ID、规范参数**必须同时匹配两个记录**。审核者身份来自认证应用状态，绝不来自对话 —— 在聊天里打 "approved: true" 不改变任何东西。

**重启后必须保留什么**：`RunState` 是 SDK 的可序列化暂停/恢复边界（模型响应、生成项、批准状态、可选服务端会话 ID；快照还含 context、usage、interruptions；自定义 context 可能需要显式序列化）。**序列化的 RunState 未经认证，只从可信存储加载。**

三类记录分开：
1. **运行状态 run state**（SDK 继续所需）
2. **提议与决定 proposal & decision**（请求了什么、谁决定、确切范围、许可何时过期）
3. **业务账本 business ledger**（队列任务是否存在及其收据）

恢复运行状态**不刷新工单权限**。快照只存安全上下文；检查任务归属后，从可信状态重建认证范围、时钟、适配器、凭证。本工作流不需要 Session；若加，**绝不让两个恢复的快照同时针对它恢复**。

**为什么存储的批准不够**：有缺陷的适配器混淆了两个条件 —— **14:00 截止限制回电何时可排；12:10 过期限制批准有效多久**。在写事务中检查可信时钟 → `expired`、零行，修复是**重新审核**。把回电改到 13:30 也使决定失效：两个时间都满足截止，但**批准绑定一个确切动作**，改变需要新提议。拒绝和过期使提议终结 —— **拒绝待批调用并恢复同一运行**，不要用"已批准"的断言开新运行。拒绝还要把权威的无效果结果传达给模型（泛泛拒绝分不清 denied 和 expired）：`state.reject(item, rejection_message=...)`，SDK 在恢复时把这段文本原样发给模型。

核心验证器 `validate_execution_grant`（只在所有检查通过时返回 `True`，否则 `Stop`；从不修改记录），检查顺序：

| 类别 Category | 检查 Check |
|---|---|
| 确切动作 Exact action | 提议 pending；pending call 的 call_id/operation 与提议一致；规范参数 = 提议 = 期望；决定绑定同一提议/call/operation/参数 |
| 当前权限 Current permissions | 组织和操作员未变；工单属于该组织且在权限内；审核者属于组织且 `can_review`（**现在**重查，不信任提议里的） |
| 时间 Time | 过期时间未被改；`now < expires` 否则 `expired`；choice = approve；决定时间 < 过期且 ≤ now；`now < callback_at < deadline` |

**其他工程细节**：`BEGIN IMMEDIATE` 事务；原子目录创建作为本地跨进程锁 (cross-process lock)（**绝不自动抢锁**）；预算在事务中消费（被拒的尝试也计数）；提议和运行状态分步保存，**两者之间崩溃需要修复，不是重新弹审批**；`resume` 若已有 completion 则返回已有收据。

**8 个场景（确定性测试）**：

| 场景 Scenario | 结果 Outcome |
|---|---|
| 授权批准 approval | 1 行，参数为批准值 |
| 拒绝 denial | 0 行 |
| 12:01 批准、12:11 执行 | 0 行（expired） |
| 改参数到 13:30 | 0 行（旧决定无法授权） |
| 未授权审核者 | 0 行 |
| 无授权直接写（绕过 SDK） | 0 行 |
| 过期前重启 | 恰好 1 行 |
| 重复恢复 | 返回已有收据，不建第二个任务 |

这些测试覆盖应用边界；线上 SDK 暂停/恢复需单独跑：新存储，`start` → `inspect`（期望零行）→ `decide --decision approve` → 另一进程 `resume`，每个命令固定时钟（12:00、12:01、12:02）。

**保留的证据**：每段在 `trace()` 中运行，有自己的 trace ID，task 作为 `group_id`，start 和 resume 的 trace 归在一起；traces 有缓冲，进程退出前 flush。另保留脱敏 (sanitized)证据记录：app release、callback-v1、模型设置、依赖版本；task、提议、pending call、两个 trace ID；审核者引用、决定时间、过期、参数摘要 (digest)；批准前行数、终态、收据、最终行数、验收结果；本地测试、线上执行、已检查 trace 导出各自的状态。**Trace ID 链接各段，但只有检查导出的 span 才说明导出成功；只有账本才说明任务是否存在。** 没有 key 前把线上执行记为 `not_run`。**预测的零行结果不是测得的零行结果。**

### 面试怎么说 / How to say it in the interview

**Q: "Your agent can write to our support system. What stops it from creating a task nobody approved?"**
> "The write tool is marked needs-approval, so the SDK pauses the run before the function body executes. An authenticated reviewer's decision is bound to the exact pending call ID and canonical arguments, and when a worker resumes, the adapter rechecks permission, arguments, and the approval's expiry inside the same transaction that writes the task. Proof is zero rows before approval, a ledger receipt after authorized execution, and isolated no-effect tests for denial, expiry, changed arguments, and a grantless write. The handoff covers restart ownership, dependency versions, and which evidence is actually run versus not_run."
（中文：执行前暂停 + 决定绑定确切调用 + 写事务内重查 + 账本收据证明。）弱回答 "The prompt requires human approval and the output guardrail catches it" —— 输出护栏在写之后才运行。

**Q: "Does approval survive 12:10? Do changed arguments inherit permission? What does a trace alone prove?"**
> "Execution at 12:11 expires this proposal, even though 13:00 still beats the 14:00 deadline, because those are two different clocks. Changed arguments need a new review, since approval binds to one exact action. A trace helps reconstruct what ran; only the application ledger establishes whether the authorized effect occurred."

**Q: "The worker crashed after approval. What happens on resume?"**
> "A fresh worker takes an exclusive lock, rebuilds identity, clock, and adapters from trusted state rather than the snapshot, restores the RunState, and runs the resume gate. If the approval expired it rejects the pending call with the authoritative 'expired, no effect' message and resumes the same run; if the task was already created, it returns the existing receipt instead of creating a second one."

---

## 9. Connecting Models to Customer Systems With MCP｜用 MCP 连接模型与客户系统

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/connecting-models-to-customer-systems-with-mcp

### 要点 / Key ideas

**事故**：Northstar 的服务状态函数在直接 Python 测试中通过；放到网络端点 (endpoint)后，**一个已认证客户端能读到另一个组织的工单**。JSON 合法，问题是调用者和记录之间缺了检查。直接测试跳过了 初始化连接 → 发现工具 schema → 调用 → 收到协议结果 的全过程，所以漏掉了泄露。

**MCP（模型上下文协议，Model Context Protocol）**：连接 AI 应用与工具和上下文数据的开放协议；共享接口减少"每对应用×服务器一个集成"的需要（受支持能力和访问控制约束）。三个角色：

| 角色 Role | 职责 |
|---|---|
| Host 宿主应用 | 管理工作流和暴露的能力 |
| Client 客户端 | 维持连接、发现工具、发送请求 |
| Server 服务器 | 暴露能力、处理请求 |
| （Northstar 的选择）客户系统适配器 adapter | 在 server 后检查业务权限、取记录 —— 是实现选择，不是第四个协议角色 |

**MCP 给你互操作性 (interoperability)；托管、租户隔离 (tenant isolation)、记录级权限 (per-record permissions) 仍是你的工作。**

任务：只读服务状态连接。NS-318 属于 Northstar（更换泵派工 08:00–12:00 UTC，来源 `dispatch/NS-318/v3`）；NS-904 属于另一组织。服务器只宣告一个工具 `get_service_status(ticket_id)`，成功结果 5 字段：`ticket_id, status, dispatch_window, source_ref, customer_note`。**模型选 ticket ID；服务器认证状态提供调用者组织和权限。** NS-209 回电写入器**不**放到 MCP 后面。

**两条路线到同一个 MCP server**：

| 路线 Route | 谁连接 | 说明 |
|---|---|---|
| 应用侧 Application-side | 你的 Python 应用作为 Streamable HTTP MCP client 连 `http://127.0.0.1:8765/mcp` | 你管连接建立与清理；SDK 用 `MCPServerStreamableHttp`（async context manager） |
| Responses 托管 Responses-hosted | 在 Responses 请求里加 `mcp` 工具，**OpenAI 自己连接**服务器，处理整个工具往返 | `server_url` 必须**公网可达**；私有/本地服务器用 **Secure MCP Tunnel**（`tunnel_id` 代替 `server_url`）；SDK 用 `HostedMCPTool(tool_config=...)` |

**回环地址 (loopback) 永远指发起连接的那台机器** —— OpenAI 连 127.0.0.1 到的是它自己的主机，不是你的笔记本。托管路线改变的是 MCP client 和编排在哪运行，工具仍由 MCP server 执行；**它不是第三种传输 (transport)**。

<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="250" fill="#fff"/>
<rect x="10" y="30" width="170" height="70" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="95" y="58" text-anchor="middle">Your app (MCP client)</text><text x="95" y="78" text-anchor="middle">应用侧客户端</text>
<rect x="10" y="150" width="170" height="70" rx="8" fill="#e6f4ea" stroke="#188038"/><text x="95" y="178" text-anchor="middle">OpenAI Responses</text><text x="95" y="198" text-anchor="middle">托管 mcp 工具</text>
<rect x="300" y="90" width="180" height="80" rx="8" fill="#fef7e0" stroke="#f9ab00"/><text x="390" y="115" text-anchor="middle">MCP server</text><text x="390" y="135" text-anchor="middle">bearer auth → principal</text><text x="390" y="155" text-anchor="middle">认证 → 服务器主体</text>
<rect x="570" y="90" width="180" height="80" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="660" y="115" text-anchor="middle">Adapter: record check</text><text x="660" y="135" text-anchor="middle">org + entitlement</text><text x="660" y="155" text-anchor="middle">记录级授权</text>
<line x1="180" y1="65" x2="298" y2="115" stroke="#333" marker-end="url(#a9)"/>
<text x="230" y="78" font-size="11">loopback / private</text>
<line x1="180" y1="185" x2="298" y2="150" stroke="#333" marker-end="url(#a9)"/>
<text x="200" y="232" font-size="11">public HTTPS or Secure MCP Tunnel</text>
<line x1="480" y1="130" x2="568" y2="130" stroke="#333" marker-end="url(#a9)"/>
<text x="390" y="22" text-anchor="middle" fill="#555">Both routes gated by approval; authorization lives behind the network boundary｜两条路线都要审批，授权在网络边界之后</text>
<defs><marker id="a9" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**连接器 (Connectors)**：OpenAI 维护的流行服务 MCP 包装（Gmail、Google Drive、Dropbox、SharePoint）；用 `connector_id` 代替 URL，并在 `authorization` 传上游服务的 OAuth token。**`connector_id` 对 2026-09-01 之后发布的模型已弃用 (deprecated)**，改用 `server_url` 或 `tunnel_id`。Northstar 的适配器是客户自有的，需自定义端点。

**三种凭证分开 (Three credentials)**：

| 凭证 Credential | 认证什么 |
|---|---|
| OpenAI API key | 你的应用 → OpenAI |
| MCP access token | 调用者 → Northstar 的 MCP server（Responses 不存 authorization 值，**每次请求都要发**） |
| Customer-system credential | server 的适配器 → 客户后端（以正确业务身份） |

**都不能出现在模型可见的工具参数里。**

**构建小型 MCP server**：FastMCP + 装饰的工具函数 + 传输（SDK 也支持 stdio，此处用 Streamable HTTP 让网络边界显式）。服务器把不透明 bearer token 映射到服务器自有主体 (principal)：组织 northstar，权限 NS-318。工具只接受 `ticket_id`，没有组织、操作员、SQL、批准标志、凭证参数。固定 `mcp==1.26.0`（mcp 2.x 把 FastMCP 改名为 MCPServer 等）。测试服务器只绑定回环，**绝不公网暴露**；生产 MCP server 需要真正的认证边界 —— MCP 授权是可选的，但支持它的 HTTP server 应遵循规范中**基于 OAuth 2.1** 的流程。

**初始缺陷**：任何有效主体可拿任何存在的记录 —— **认证了调用者，但从不检查归属**。

**10 次探测（有效 Northstar token）**：NS-318 ×4、NS-904 ×4、不存在 ×2。
- 有缺陷服务器：**8 条记录返回（含 4 次未授权泄露）+ 2 次缺失拒绝**
- 修复后：4 个授权结果 + 6 个**完全相同的** `{"error":"not_available"}`

修复谓词 (predicate)：记录存在 **且** 组织 = 主体组织 **且** ticket ID 在主体权限内（全部来自服务器自有数据）；**在序列化任何字段前检查**；未授权和不存在返回同一拒绝，详细原因只写服务器审计日志 (audit log)，客户端无从得知哪些记录存在。

```python
def authorized_record(principal, record):
    # Existence, matching organization, and ticket entitlement, all from server-owned data.
    return (principal is not None and record is not None
            and record["organization"] == principal["organization"]
            and record["ticket_id"] in principal["entitlements"])
```

**诱人但错误的修复：工具白名单 (tool allowlist)** —— 混淆了**工具范围 (tool scope)** 与**记录范围 (record scope)**。10 个请求用的是同一个允许的工具，只有服务器端调用者-记录检查才能区分合法读取和泄露。

**按发生位置读失败**：坏 token → HTTP 401，任何工具运行前；发现失败不说明记录的任何事；只有已认证调用到达适配器并得到 `not_available` 才是记录拒绝；服务器不可达是执行错误，**绝不是成功的拒绝**；调用未宣告的 `create_callback_task` 必须返回 MCP 错误结果（`isError` true）且不改变任何东西。

**三个独立控制**：
- **认证 (authentication)**：凭证代表谁
- **业务授权 (business authorization)**：该调用者能否对此记录执行此操作
- **审批 (approval)**：一个人是否放行这个具体调用

SDK 模式：桥接 function tool 设 `needs_approval=True`，运行以 interruption 暂停，在保存的状态上 approve/reject 再恢复。`MCPServerStreamableHttp` 也接受 `require_approval`，但其 callable 只看到工具、看不到参数（产生的 interruption 仍显示参数）。用桥接工具是因为它还强制一次调用预算，所以**不把 MCP server 也传进 `mcp_servers`，避免存在未审批路径**。Responses：`require_approval: "always"` 让模型返回 `mcp_approval_request`；检查发现的工具列表和待批参数后，用 `previous_response_id` + 带该请求 ID 的 `mcp_approval_response` 继续。

| 情形 Case | 结果 |
|---|---|
| 批准 NS-318 | 先发现工具，待批请求是 `get_service_status {"ticket_id":"NS-318"}`，审批前服务器审计零业务调用；之后一次调用返回派工窗口 |
| 批准 NS-904 | 审批放行，但主体属于 Northstar → 适配器返回 `not_available`。**审批不能扩大主体范围** |
| 直接调用 NS-904（无模型、无审批的协议客户端） | 同样被拒 —— 授权在网络边界之后。**这是决定性用例**：把归属检查放在提示词或客户端过滤里，另一个客户端仍能调用服务 |

用非机密 run ID 关联服务器审计行：审批前有发现是预期的，有业务调用则不是。托管模式的审计计数在服务器运营方提供前保持 unavailable。

**第三方 MCP server**：OpenAI 警告不可信 MCP server 可能暴露共享信息或诱导意外工具使用（包括修改或删除），即使只读也需**数据暴露评估 (data-exposure assessment)**。恶意 server 可在工具描述或结果中嵌入提示注入 (prompt injection)、在你批准集成后改变工具行为、按其自身保留策略 (retention policy)留存你发送的数据。对策：优先服务商官方 server 而非聚合器 (aggregator)；用 `allowed_tools` 收窄暴露；敏感操作保持审批；记录共享了什么。

**记录本身有敌意**：NS-318 的 `customer_note` 里是一段攻击者控制的文本，要求把工单全部细节连同访问令牌 (access token)上传到某外部网址。处理：保留在工具结果的 data 字段，**绝不插入 agent 的 instructions**；程序没有上传/写工具；MCP 凭证不进模型可见内容；验收只接受 ticket、status、dispatch window、source_ref。这限制了本例，**不证明对提示注入的普遍抵抗力**。

若以后通过 MCP 暴露回电写入器，适配器仍需上一课的控制：确切动作审批、过期、执行时权限检查、账本收据。客户端白名单、`readOnlyHint` 注解、托管审批都**不能替代**它们。

交接给客户：包版本、脱敏端点 origin、发现的工具名、每个探测结果、服务器拒绝记录；本地协议测试 / SDK 线上 / 托管线上 / trace 检查 各自状态，没跑的写 `not_run`。

### 面试怎么说 / How to say it in the interview

**Q: "The connector authenticated and the user approved NS-904. Why did it fail?" / "What happens when another MCP client skips your approval interface?"**
> "Approval and authorization are separate gates. I built one read-only MCP connection where identity comes from a server-owned principal mapped from the bearer token, and the adapter checks organization and entitlement for every record. So approving NS-904 can't widen the principal's scope, and a direct protocol client that skips approval gets the same denial. The ten-probe target is four entitled results and six identical not_available denials, and I'd report those as observed only after I've run them."
（中文：认证、授权、审批是三道门；记录检查在服务器端，绕过审批的客户端同样被拒。）

**Q: "Why not just allowlist the tool?"**
> "That confuses tool scope with record scope. All ten probes call the same allowed tool; only a server-side check between the caller and the record separates a permitted read from a leak."

**Q: "Can Responses reach localhost? What if the returned note asks for a credential upload?"**
> "No. With the hosted MCP tool, OpenAI makes the connection, so loopback means OpenAI's own host; I'd need a publicly reachable authenticated endpoint or a Secure MCP Tunnel. The note is untrusted record content: it stays in the tool result, never goes into instructions, and this workflow has no upload tool and keeps the MCP credential out of model-visible content."

**Q: "Would you connect a third-party MCP server?"**
> "Only after a data-exposure assessment. A third-party server can inject instructions through tool descriptions or results, change behavior after approval, and keep data under its own retention. I'd prefer the provider's official server, narrow it with allowed_tools, keep approvals on for anything sensitive, and log what's shared."

---

## 10. Multi-Agent Orchestration: Handoffs and Agents as Tools｜多 Agent 编排：Handoff 与 Agent-as-Tool

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/multi-agent-orchestration-handoffs-and-agents-as-tools

### 要点 / Key ideas

**反例**：Northstar 第一版多 agent 草案：triage agent + dispatch 专家 (specialist) + 一个"提醒人工"的 handoff。面试官问谁收到提醒 —— 没人。**handoff 只是在两个 agent 间移交对话，没有通知任何人。**

面试题："Why did you add a second agent?" **模块化本身不证明收益**。再调一个 agent 通常增加模型工作量、协调开销 (coordination overhead)、上下文共享风险和失败路径。**一个 agent 或普通代码可能就够。**

**三种模式 (three patterns)**：

| 模式 Pattern | 谁保持控制 Control | 上下文 Context | 适用 When | 运行结果特征 |
|---|---|---|---|---|
| Agent as tool（manager 模式） | manager 始终拥有对话和面向用户的回合 | 嵌套运行**不继承** manager 对话，专家只看到 manager 发的内容；默认一个 string 字段 `input`，可传 `parameters`（Pydantic/dataclass）；`custom_output_extractor` 可重塑输出 | 专家帮子任务但不应对用户说话 | `result.last_agent` = manager；items 含 tool call 和 output |
| Handoff | 接收方成为**活跃 agent** 并直接回答 | 默认接收方看到之前的历史（含工具内容），`input_filter` 可改变转发内容 | 路由本身就是工作流的一部分（前台把账单/派工/保修问题分给不同负责人） | `last_agent` = dispatch；items 含 handoff call 和 output（triage 可能先产生 items，要读序列） |
| 应用协调并行 Parallel in code | 应用代码 | 各 worker 只读独立输入 | 子任务互不依赖 | 用 `asyncio.gather`；无模型决定下一个 agent → 速度/成本/行为更可预测 |

对模型来说，handoff 看起来像工具，默认名 `transfer_to_dispatch`，调用即切换 agent。

<svg viewBox="0 0 760 260" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="260" fill="#fff"/>
<text x="125" y="22" text-anchor="middle" font-weight="bold">Agent as tool</text>
<rect x="60" y="40" width="130" height="40" rx="6" fill="#e8f0fe" stroke="#3367d6"/><text x="125" y="65" text-anchor="middle">Manager (owns turn)</text>
<rect x="60" y="130" width="130" height="40" rx="6" fill="#e6f4ea" stroke="#188038"/><text x="125" y="155" text-anchor="middle">Dispatch specialist</text>
<line x1="110" y1="80" x2="110" y2="128" stroke="#333" marker-end="url(#a10)"/><line x1="140" y1="128" x2="140" y2="82" stroke="#333" marker-end="url(#a10)"/>
<text x="125" y="200" text-anchor="middle">result returns to manager</text><text x="125" y="218" text-anchor="middle">结果回到 manager</text>
<text x="380" y="22" text-anchor="middle" font-weight="bold">Handoff</text>
<rect x="315" y="40" width="130" height="40" rx="6" fill="#e8f0fe" stroke="#3367d6"/><text x="380" y="65" text-anchor="middle">Triage</text>
<rect x="315" y="130" width="130" height="40" rx="6" fill="#e6f4ea" stroke="#188038"/><text x="380" y="155" text-anchor="middle">Dispatch (now active)</text>
<line x1="380" y1="80" x2="380" y2="128" stroke="#333" marker-end="url(#a10)"/>
<text x="380" y="200" text-anchor="middle">dispatch answers user</text><text x="380" y="218" text-anchor="middle">不通知任何人 notifies no human</text>
<text x="635" y="22" text-anchor="middle" font-weight="bold">Parallel (app code)</text>
<rect x="570" y="40" width="130" height="30" rx="6" fill="#fef7e0" stroke="#f9ab00"/><text x="635" y="60" text-anchor="middle">asyncio.gather</text>
<rect x="545" y="95" width="80" height="34" rx="6" fill="#e6f4ea" stroke="#188038"/><text x="585" y="117" text-anchor="middle">dispatch</text>
<rect x="645" y="95" width="100" height="34" rx="6" fill="#e6f4ea" stroke="#188038"/><text x="695" y="117" text-anchor="middle">handling_rule</text>
<rect x="570" y="155" width="130" height="34" rx="6" fill="#fce8e6" stroke="#c5221f"/><text x="635" y="177" text-anchor="middle">check named results</text>
<rect x="570" y="205" width="130" height="34" rx="6" fill="#e8f0fe" stroke="#3367d6"/><text x="635" y="227" text-anchor="middle">Manager drafts</text>
<line x1="610" y1="70" x2="590" y2="93" stroke="#333" marker-end="url(#a10)"/><line x1="660" y1="70" x2="690" y2="93" stroke="#333" marker-end="url(#a10)"/>
<line x1="585" y1="129" x2="615" y2="153" stroke="#333" marker-end="url(#a10)"/><line x1="695" y1="129" x2="660" y2="153" stroke="#333" marker-end="url(#a10)"/>
<line x1="635" y1="189" x2="635" y2="203" stroke="#333" marker-end="url(#a10)"/>
<defs><marker id="a10" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**Manager 模式示例 (NS-318 草稿)**：应用提供两个输入 —— 已授权派工记录（10/29 08:00–12:00 UTC，`dispatch/NS-318/v3`）和处理规则 `policy/dispatch-followup/v1`（要求草稿供操作员审核，禁止发消息或改工单）。manager 让专家做窄解释任务，专家返回 ticket、窗口、来源；manager 起草；**应用代码在检查工单身份、来源引用、窗口和操作员审核要求后才接受**。流畅草稿不证明专家被调用了 —— **检查运行记录里的工具调用及其结果**。拆分的好处：草稿错时可区分三种 bug（专家返回错窗口 / manager 组合错 / 验收漏检），各有不同修法。

**Handoff ≠ 人工升级 (human escalation)**：handoff 是 agent 间路由，**既不通知人，也不转移业务权限**。需要人工升级时，应用代码必须创建该审核或通知步骤，带指定负责人和自己的权限检查。

**并行三规则**：
1. **给每个结果命名**（`dispatch`、`handling_rule`）—— 完成顺序不说明哪个是哪个
2. **合并前检查** —— 缺失、失败、重复、不匹配的结果阻止草稿
3. **worker 保持只读** —— 都不写共享工单、会话或回电账本（并发写 (concurrent writes)需要锁 (locks)和应用层显式授权）

情境匹配练习：单次授权 NS-318 状态读 → **现有有界工具或固定工作流**；操作员要详细派工对话 → **triage handoff 到 dispatch**；用有界派工解释 + 独立处理规则起草 → **manager 调 dispatch agent as tool**；先独立解释派工记录和规则再合并 → **应用协调并行**。

**Agent 之间传什么上下文**：
- **本地运行上下文 (run context)**：传给 `Runner.run` 的 Python 对象，供工具、hooks、应用代码使用；SDK **不会自动发给模型**，所以可放数据库句柄、认证主体、权限。只有你复制进 instructions、input 或工具结果时才变得模型可见。
- 对 NS-318 handoff，用显式白名单 (allowlist) 构建接收任务：`ticket_id, dispatch_window, source_ref, operator question`；排除原始客户备注、凭证、无关记录、原始工具记录。
- **嵌套 handoff 历史 (nested handoff history)** 是 opt-in，其摘要仍可能携带工具参数和输出 —— **摘要改变格式，不做脱敏**。若 filter 用 nesting helper，要在摘要前清洗 `input_history`、`pre_handoff_items`、`new_items`；只替换 `input_items` 不够。
- 测试：12 条历史中 3 条只在工具参数或结果里带测试 token → 摘要载荷中 3/12 含 token；白名单载荷 0/12 含 token，12/12 保留恰好 4 个字段。
- **过滤接收方内容不抹除原件**：会话、应用日志、工具参数、模型提供方输入、traces 是独立副本，各有控制。SDK tracing 默认开启；`trace_include_sensitive_data=False` 不让敏感载荷进 trace，关闭 tracing 是另一选择，两者都不覆盖其他副本。放松 SDK 数据日志保护可能在日志和诊断异常中暴露数据。

本地检查（10 项）：摘要 token 计数 3；白名单 token 计数 0；白名单字段保留；反序到达仍按名匹配；拒绝缺失、重复、失败、意外名称、来源不匹配、标识符不匹配（NS-904）。**不要用 Python 优化标志运行**（会去掉 assert）。线上结果报告为 pass / fail / error / not_run；**好看的答案不证明预期路径运行了**。

**何时一个 agent 就够**：从最简单可行的设计开始。单次状态读用现有工具或固定工作流，无需第二个模型；组合规则能写成普通代码时固定工作流也胜出。对组合草稿，在代表性任务上比较**单 agent 基线 (single-agent baseline)** 与 manager 版、并行版，评分维度：证据正确、规则处理正确、对操作员有用、延迟 (latency)、失败行为。**只有测得的质量提升能覆盖额外调用、协调、隐私暴露和运维成本时才保留额外 agent。**

### 面试怎么说 / How to say it in the interview

**Q: "Why did you add a second agent? / How would you choose among a fixed workflow, a manager, a handoff, and parallel runs?"**
> "I start with the simplest thing. For a single status read I keep the existing tool; no second model is needed. For the combined draft, I'd compare a manager calling a dispatch specialist as a tool against a single-agent baseline on accuracy, rule handling, latency, cost, and failure behavior, and only keep the extra agent if it pays for itself. For a detailed dispatch conversation, triage can hand off the turn to dispatch, but notifying a human needs its own authorized workflow with a named owner. In every case application code checks record identity, source references, and the final draft, and I report local checks separately from live runs."
（中文：先最简；多 agent 需用基线对比证明收益；handoff 不是人工升级；验收在应用代码。）

**Q: "Who received the handoff, and where is the notification?"**
> "A handoff only changes which agent is answering; it doesn't notify anyone or transfer business authority. If we need a human, the application creates a review or notification step with an owner and its own permission checks."

**Q: "A summary omits the raw tool item. Why might the token still reach dispatch?"**
> "Because the summary text itself can contain the tool argument or result; summarizing changes the format, not the content. I'd build an allowlisted payload for the receiver, and handle the original history, sessions, traces, logs, and provider input as separate copies with their own controls."

**Q: "How do you know the specialist was actually called?"**
> "I don't trust the fluent draft. I check the run items: one tool call to the specialist, its output linked by call ID, and the manager as the final agent. That also tells me which of three bugs I have when a draft is wrong."

---

## 11. Workspace Agents, ChatKit, or Your Own Stack｜部署位置：Workspace Agents、ChatKit 还是自建

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/workspace-agents-chatkit-or-your-own-stack

### 要点 / Key ideas

**第一周控制台日志**：24 次草稿提交、6 次客户端超时（每次后跟重试 (retry)）、操作员看到 3 份重复草稿。没有客户消息发出，但操作员看到同一草稿两次，**没人能说清哪个团队拥有产生它们的服务**。

Agent 能跑之后要决定**它住在哪**。三个"家"，各自把界面、agent 循环、存储数据、值班 (on-call) 职责移交给不同所有者。面试官会让你选一个，然后问**请求超时时谁被呼叫 (paged)**。案例：NS-318 派工草稿要出现在 Northstar 现有操作员控制台；每份草稿由操作员审核；不能发消息或改工单。

**选项 1：ChatGPT 内部**：
- 客户可把自己的 MCP server 作为插件 (plugin) 接入 ChatGPT（读写工具）。
- **Workspace Agent**：共享的 ChatGPT agent，可用连接的应用、按计划运行、在工作区内共享。能否使用取决于管理员设置以及谁能构建/运行/共享 agent。
- 外部系统可触发已保存的 Workspace Agent，四个细节：
  1. **HTTP 202 Accepted = 触发已排队，不是完成**。响应体含 ChatGPT 会话的 `conversation_url`；**目前无法通过 API 取回 agent 的回复**。
  2. 跟踪运行：发 beta header `OpenAI-Beta: workspace_agent_runs=v1`，存储返回的 `agent_trigger_run_id`，轮询直到 `completed` 或 `failed`。
  3. 触发用 **Workspace Agent access token**（ChatGPT 端点），不是 OpenAI Platform API key。重试时对同一源事件保持 `Idempotency-Key` 和 `conversation_key` 稳定，新事件用新幂等键 (idempotency key)；把 run ID 记在源事件旁便于对账 (reconcile)。
  4. agent 拥有的连接账户可能把它能访问的一切暴露给 agent 被共享的所有人 —— **一起审查连接范围和共享对象**。
- 适合：业务方拥有、把草稿投递到某处、不需要屏幕上即时回答的任务。不适合：操作员在 Northstar 自己的控制台里等待。

**选项 2：ChatKit**：OpenAI 的可嵌入聊天界面，现成前端，可渲染 widgets；**界面本身不说明编排、会话状态、工具、验收在哪运行**。高级集成 (advanced integration)：客户用 ChatKit Python SDK 在自己基础设施上运行 ChatKit server，连接任意 agent 后端（包括 Agents SDK 服务）。旧的托管路径连接 Agent Builder（OpenAI 托管）中的工作流，现在只推荐给已经在用的应用。

**选项 3：客户自建界面 + Agents SDK 服务**。

| 路径 Path | 访问控制 | 运行与结果 | 风险点 |
|---|---|---|---|
| ChatGPT workspace | 工作区身份与共享 | 异步触发排队；草稿出现在关联 ChatGPT 会话或 agent 应用写入处 | 必须有人负责运行失败或永不完成的情况 |
| ChatKit in console | Northstar 登录操作员 | 嵌入界面 → Northstar 运行的 ChatKit server → 授权工单、跑工作流、验证草稿、返回审核 | Northstar 运维 ChatKit server |
| Customer-built UI | Northstar 授权 | 控制台直接调 Northstar 自有 Agents SDK 服务 → 授权、作用域适配器读来源、调模型、验证、返回审核 | Northstar 运维服务 |

**每条路径里，工具授权保护记录，人接受或拒绝草稿。自建服务不等于托管模型权重，仍调用 OpenAI 托管的模型。**

**每条路径写下五件事 (five questions per path)**：会话和 traces 存在哪；哪个凭证读派工记录；谁批准草稿；结果如何到达操作员；失败时呼叫哪个团队。**任何空白都是选择前要问客户的问题**。即使 Workspace Agent 路径也需要一个确定的地方在操作员看到前运行 Northstar 的验收检查。

**推荐**：Northstar 已有控制台 → 最强默认是控制台后面的 **Agents SDK 服务**；若想要聊天 UI 且愿意运行 ChatKit server，ChatKit 是选项。无论哪种，服务现在归 Northstar 运营。

**重复草稿问题**：日志证明出现了重复，但**不说明超时原因，也不说明 3 个重复中多少来自 6 次重试**。诱人修法：把超时当失败，用新 request ID 重提 —— 但服务器可能还在跑或已完成第一个请求，新 ID 造出另一个作业和另一份草稿。生成任何东西前需要的边界：

| 边界 Boundary | 做法 |
|---|---|
| 身份 Identity | 认证操作员，从可信应用状态授权访问 NS-318 |
| 请求身份 Request identity | 把稳定 request ID 绑定到操作员和内容；相同绑定的重放返回已有状态；同 ID 改内容 → 拒绝（conflict） |
| 容量 Capacity | 限制在途工作 (in-flight work)数；过载显式排队或拒绝，不建无界积压 (backlog) |
| 结果 Outcome | 跟踪 accepted / completed / failed / **unknown**；客户端超时让结果为 unknown，直到服务对账 |
| 失败 Failures | 读和生成设超时与重试预算；**重大动作需要自己的确切动作审批和账本** —— 请求去重本身不能保证单次效果 |
| 运维 Operations | 监控依赖和队列年龄；可回滚部署 (rollback-ready deployment)；指定支持负责人接受该服务 |

在途重试的正确响应：认证并授权 → 校验操作员与内容绑定 → 返回已有的 accepted/in-progress 状态，稍后对账。请求身份只有在绑定和结果**持久化**存储时才能熬过重启（生产中是真实数据库的原子写，不是内存字典）。

本地 Registry 演示：规范 JSON + SHA-256 指纹 (fingerprint)把 request ID 绑定到 (operator, fingerprint)，键顺序无关；8 个离线检查：首次请求 accepted；在途重放（键重排）不新增工作；改内容 → conflict；改操作员 → conflict；另一请求在槽忙时 → overloaded；完成后重放返回存储草稿；槽复用；handler 失败释放槽。演示的捷径：只对新请求查操作员，所以另一操作员重放已知 ID 得到 conflict —— **会告诉未授权调用者该 ID 存在**；生产版应**先认证授权再查 request ID**。线上模式不打印异常文本（SDK/网络错误可能含密钥）。

**迁出 Agent Builder**：OpenAI 已弃用 (deprecated) Agent Builder 并排定关停 (shutdown)，ChatKit 保留。新 ChatKit 应用和迁移都指向自有服务器上的高级集成。**迁移行为，不是画布布局**：盘点 instructions、tools、服务身份、权限、审批点、输出、代表性测试用例 → 按迁移指南重建，ChatKit 指向自己的服务端 agent → **对两个版本重放相同用例**，比较被接受的输出和工具效果（含拒绝与批准的动作），不只是措辞 → 记录剩余差异、指定负责人、切流量前约定回滚。**干净导出只是迁移的开始；对等 (parity) 来自重放。**

**客户数据去哪 (data handling)** —— 企业客户最先问，答案按产品和端点区分：

| 项 Item | 事实 Fact |
|---|---|
| 训练 Training | 发送到 API 的数据**不用于训练** OpenAI 模型，除非客户选择加入 (opt in) |
| 滥用监控日志 Abuse-monitoring logs | 默认保留最多 **30 天** |
| 零数据保留 ZDR (Zero Data Retention) | OpenAI 批准后在组织或项目级配置，客户内容不进这些日志；**Responses 和 Realtime 符合资格；Conversations、Files、Vector Stores、Batches 不符合**；ZDR 下 Responses 的 `store` 一律视为 false |
| 应用自己的副本 | 会话、请求注册表、日志、SDK traces、错误报告 —— 各需指定能读取和删除的负责人 |
| 其他副本 | ChatGPT、ChatKit、连接的目的地、MCP servers 各自按自身控制保存 |
| `store=False` | 只阻止响应被保存以便后续取回；**本身不建立零保留、数据驻留 (residency) 或对 traces 和连接器副本的控制** |

**任何没有确认答案的要求都视为上线阻塞项 (launch blocker)。**

### 面试怎么说 / How to say it in the interview

**Q: "Northstar already has a console. Where would you put the agent, and why?"**
> "Northstar needs an operator-reviewed dispatch draft inside its own console, so I'd put an Agents SDK service behind that console. ChatKit is an interface choice; with the advanced integration Northstar still runs the server. The log shows 24 submissions, six timeouts with retries, and three duplicate drafts, with no message sent, so I'd bind each request ID to the operator and content, treat a timeout as an unknown outcome to reconcile rather than a failure to resubmit, and validate the draft before review. Before real data, I need durable reconciliation, confirmed data controls, regression results, and a support owner who has signed on."
（中文：控制台后接 Agents SDK 服务；request ID 绑定操作员+内容；超时=未知待对账；上线前需持久对账、数据控制、回归、支持负责人。）弱回答 "Use ChatKit, it hosts the agent and gives zero retention; resubmit on timeout" —— 三处都错。

**Q: "A Workspace Agent trigger returns 202. Can the operator see the draft?"**
> "Not yet. A 202 only means the run was queued. The response links the ChatGPT conversation, and the API can't return the agent's answer, so I'd poll the run by its agent_trigger_run_id and treat a failed or never-finishing run as an incident to investigate."

**Q: "Where does our data go? Do you train on it?"**
> "API data isn't used for training unless you opt in. Abuse-monitoring logs are kept up to 30 days by default, and with approved zero data retention, Responses and Realtime content stays out of them, though Files, Vector Stores, Conversations, and Batches aren't eligible. But our own app also keeps copies: sessions, registries, logs, traces, so each needs an owner who can read and delete it, and store=False alone doesn't give you zero retention or residency. Anything unconfirmed is a launch blocker."

**Q: "We built on Agent Builder. What now?"**
> "Agent Builder is deprecated, so I'd migrate the behavior, not the canvas: inventory instructions, tools, identities, approval points, and test cases, rebuild on our own ChatKit server with an SDK backend, replay the same cases against both and compare accepted outputs and tool effects, then name an owner and agree on rollback before switching traffic."

---

## 12. Voice Agents With the Realtime API｜用 Realtime API 构建语音 Agent

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/voice-agents-with-the-realtime-api

### 要点 / Key ideas

**事故**：第一次语音演练 (rehearsal)中，操作员说 "What is the dispatch window for NS-318…"，停下看笔记，接着说 "Actually, that ticket number was wrong."。此时 agent 已判定回合 (turn)结束并开始读 NS-318。文本 agent 知道用户何时说完（按回车）；**语音 agent 只能从停顿猜，并在用户中途再次开口时应对**。语音改变界面，不改变规则（授权来源、仅草稿供审核）。

**三种语音架构 (voice architectures)**：

| 架构 Architecture | 工作方式 | 优点 | 缺点 |
|---|---|---|---|
| 语音到语音 Speech-to-speech (Realtime) | Realtime 模型直接从输入音频生成音频 | 轮替自然、快 | 输入转写 (transcription) 可选且独立运行 —— 是"说了什么"的参考，**不是模型听到内容的精确记录** |
| 链式管线 Chained pipeline | 转写 → 推理模型 → 语音合成 (TTS) | 应用可检查转写、控制每一阶段；各阶段可用不同供应商/模型 | 每跳增加延迟 (latency)；**听错的工单号直接流入推理和语音** |
| GPT-Live (`gpt-live-1`) | 同时听和说，把推理和工具交给独立后端（如现有文本 agent） | 用户可继续说话而后端在工作 | 适合已有文本 agent 时 |

演练数据：20 个回合中 **5 个回复在操作员说完前开始**，其中 2 个在操作员更正时读取已在进行。无工单写入、无客户消息。

建议：交互式控制台先做**仅读和草稿**的 Realtime 演练；若以后需要每个决策点都有可检查转写，在代表性音频上对比链式管线并统计转写错误。**任何设计中转写都不算批准。** 只要业务边界不变（相同的工单授权、来源检查、操作员审核），架构选择可逆，对比只改变音频架构。

**凭证位置**：操作员界面连已认证的 Northstar 服务；服务持有平台 key、管理 Realtime 连接、用操作员的可信身份和权限调服务端读适配器。**模型提供工单参数，从不提供操作员的权限。** Realtime 会话可从浏览器走 **WebRTC**、从服务器走 **WebSocket**。浏览器流程中服务器为会话创建**短期客户端密钥 (short-lived client secret)**，长期 API key 不进浏览器代码。练习用服务端 WebSocket + `gpt-realtime-2.1`。

**语音活动检测 (Voice Activity Detection, VAD)** —— 判断回合何时结束：

| 模式 Mode | 机制 | 调参 |
|---|---|---|
| Server VAD | 按音量检测语音，静音间隔 (silence gap) `silence_duration_ms` 后结束回合 | 间隔短→答得快但会在短暂停顿处切断请求（Northstar 5 次早答首先指向静音阈值） |
| Semantic VAD | 分类器估计说话人是否说完一个意思 | `eagerness`：速度 vs 过早结束；`low` 让说话人慢慢说 |
| 手动 Manual turn control | 操作员显式结束录音，客户端 commit buffer | 边界明确，但操作员多做事 |

`interrupt_response` 开启时，新语音可取消正在进行的回复。**在 Northstar 真实停顿和更正上测试三种，不要假设最快设置胜出。**

**服务端一个回合的 5 步**：
1. 发 `session.update`（音频格式、turn detection、instructions、只读工具）；update 只改你给的字段，**读 `session.updated` 确认实际生效配置**。PCM 音频 24 kHz。
2. 把音频块流入输入缓冲区 (input buffer)（单次 append 无确认）。VAD 开时服务器 commit；关时客户端 commit 并请求回复。
3. 监听 speech-started / speech-stopped，然后 committed input 和 response 事件，**都关联到你自己的 turn ID**，不要把一次停顿当完整请求。
4. 操作员再次开口：停止本地播放、取消过时回复，**记录操作员实际听到了多少音频**（本地排队的音频可能从未播放）。
5. 发 `conversation.item.truncate` 从对话中删除模型上一回复未播放部分；忽略过时回复的迟到输出事件。

**用户感知的延迟 (perceived latency)**：从操作员实际说完到听到第一个音频。分段打时间戳；若播放仍在缓冲，第一个生成音频事件早于声音到达。示例**目标预算**（假设顺序执行）：

| 段 Segment | 预算 Budget |
|---|---|
| 回合结束检测 End-of-turn detection | 350 ms |
| 网络与分发 Network & dispatch | 150 ms |
| 生成到首个音频 Generation to first audio | 500 ms |
| 播放缓冲 Playback buffering | 100 ms |
| **合计 Total** | **1,100 ms** |

这是目标不是测量值。测量时还要记录段间重叠、过早结束、打断恢复（重叠的工作不像顺序时间那样相加）。

**打断时的工具调用**：Realtime 会话可声明 JSON Schema 参数的函数，代码仍验证参数并授权读取。时间线：静音阈值过早结束 T1 → 模型请求 call C1 读取 → 服务授权并发给适配器 → 适配器返回前操作员继续说话 → 应用开启 T2。需要分别处理两件事：
- **回复与播放**：标记 T1 过时，停止排队语音，取消回复，记录实际播放了什么，**绝不把迟到的 T1 音频当作 T2 的答案播放**。
- **读取本身**：**取消回复不会取消适配器请求**，C1 可能仍会完成。

迟到的 C1 结果即使关于 NS-318 完全正确，在更正后展示仍然是错的（它回答的是操作员撤回的请求）。正确做法：**保持 C1/T1 关联并压制它；问 "Which ticket did you mean?"；标识清楚后为 T2 授权新的读取。**

<svg viewBox="0 0 760 220" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="220" fill="#fff"/>
<text x="10" y="20" font-weight="bold">Interrupted turn: late result must not answer the new turn｜被打断的回合</text>
<line x1="40" y1="70" x2="730" y2="70" stroke="#333"/>
<text x="20" y="74">T1</text>
<rect x="60" y="55" width="160" height="30" fill="#e8f0fe" stroke="#3367d6"/><text x="140" y="75" text-anchor="middle">"...NS-318" + pause</text>
<rect x="230" y="55" width="200" height="30" fill="#fef7e0" stroke="#f9ab00"/><text x="330" y="75" text-anchor="middle">call C1 read in flight</text>
<line x1="40" y1="140" x2="730" y2="140" stroke="#333"/>
<text x="20" y="144">T2</text>
<rect x="330" y="125" width="170" height="30" fill="#e8f0fe" stroke="#3367d6"/><text x="415" y="145" text-anchor="middle">"number was wrong"</text>
<rect x="520" y="55" width="190" height="30" fill="#fce8e6" stroke="#c5221f"/><text x="615" y="75" text-anchor="middle">late C1 result → suppress</text>
<rect x="520" y="125" width="190" height="30" fill="#e6f4ea" stroke="#188038"/><text x="615" y="145" text-anchor="middle">ask → fresh authorized read</text>
<text x="380" y="190" text-anchor="middle" fill="#555">Cancel response ≠ cancel adapter request; truncate unplayed audio｜取消回复不取消读取；截断未播放音频</text>
</svg>

**写操作更关键**：本工作流没有写工具，口头修改工单请求转给指定人工流程。未来写路径需要确切提议、已认证的人工决定、执行时检查、效果收据；**一句口头 "yes"（尤其被打断的）不授予任何东西**。若操作在打断时可能已提交，**查账本 (ledger)**：打断不回滚任何东西，未检查的重试可能执行两次。

离线检查（9 项）：授权读取；重复 call ID 被拒；打断后要求澄清；迟到 C1/T1 结果被压制；重复结果被拒；未知结果被拒；澄清后新的 T2 读取；无权限被拒；Boundary 无 write/send 方法。线上模式只在确认项目权限和 SDK 签名后开启（两个 flag），它显示真实事件流但不播放音频、不模拟打断 —— 结果与离线检查分开。

**选哪个架构**：
- 需要每个决策点的转写，或各阶段需不同供应商/模型 → **链式管线**
- 已有文本 agent 并应保留其后端，由语音模型与用户对话 → **GPT-Live**
- 对话速度和自然打断最重要 → **语音到语音**
- 无论哪种，真实数据需要：确认的操作员权限、录音与数据控制、人工升级路径、不确定效果的恢复、接受支持的负责人

Northstar 下一步：第二次 Realtime 演练 —— 调整 turn detection、压制过时结果、更正后询问澄清，在相同类型的停顿和打断上重跑；用匹配的语音对比新旧配置，保留每个结果背后的计数和条件。

### 面试怎么说 / How to say it in the interview

**Q: "Why use Realtime after five of 20 responses started too early?" / "Defend your starting voice design."**
> "I wouldn't launch yet; I'd run a second rehearsal. Five of 20 responses started early, two of them with reads in flight when the operator corrected the ticket, and nothing was written or sent. I'd tune turn detection, starting with the silence threshold or semantic VAD, and tie every read to its call ID and turn. A stale result can't answer the corrected request, so the agent asks which ticket was meant and authorizes a fresh read. Our illustrative latency budget is 350 plus 150 plus 500 plus 100, so 1.1 seconds, but that's a target, not a measurement, and it says nothing about premature endings or overlap."
（中文：先二次演练；调 VAD；每次读绑定 call ID 与回合；过时结果压制并追问；1.1 秒只是目标。）

**Q: "What happens to a read already in flight?"**
> "Canceling the response doesn't cancel the adapter request, so the result can still arrive. I keep it linked to the old call and turn, suppress it from the current answer, and never play late audio from the stale turn."

**Q: "The operator says 'yes' while changing the ticket number. May the system update the ticket?"**
> "No. This workflow has no write tool. A future write needs an exact proposal, authenticated approval, a current authorization check, and a reconciled effect receipt; a spoken yes, especially an interrupted one, grants nothing. Until then I'd route it to a named person."

**Q: "Speech-to-speech or chained pipeline?"**
> "For an interactive console I'd start with speech-to-speech because natural turn-taking and latency matter most. If the customer needs an inspectable transcript at every decision point or different vendors per stage, I'd compare a chained pipeline on representative audio and count transcription errors. The business boundary stays identical either way, so the comparison only changes the audio architecture."

---

## 13. Model Choice, Reasoning Effort, and Cost｜模型选择、推理强度与成本

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/model-choice-reasoning-effort-and-cost

### 要点 / Key ideas

**事故**：Northstar 操作员草稿的首个预算 $126/月；实际接近 **$401**，因为任务有两次模型调用、约 1/10 重试、还要付工具费，而估算只算了第一次调用。**单次调用最便宜的模型很少是最便宜的部署。**

模型决策两半：(1) 选在客户自己工作上**过质量线**且延迟可接受的配置；(2) 在真实流量和缓存 (caching)假设下**为整个任务算成本**（每次调用、重试、工具）。

**当前阵容（每百万 token，课程设定）**：

| 模型 Model | 定位 Positioning | 输入 Input | 输出 Output |
|---|---|---|---|
| gpt-6.1-sol | 平衡速度/成本/智能，复杂工作接近旗舰 | $2 | $10 |
| gpt-6.1-terra | 快速高效：视觉推理、精确 computer use、清晰自然写作 | $1 | $5 |
| gpt-6-luna | 最快最便宜：分类、抽取、路由等专注高量任务 | $0.10 | $0.50 |

三者都有 1,050,000-token 上下文窗口 (context window)；支持的推理设置不同；都支持 Batch 和 Flex（标准价一半）。**从适合任务难度的档开始，让你自己的评测决定。**

**评测**：40 个只读操作员草稿。正确 = 遵循授权来源、标明来源和版本、无无依据声明 (unsupported claims)。质量线：**≥38/40 且无严重无依据声明**。

| 候选 Candidate | 正确 Correct | 中位延迟 Median latency |
|---|---|---|
| 快速 Fast | 36/40 ✗ | 1.2 s |
| 较强推理 Harder reasoning | 39/40 ✓，无严重无依据声明 | 3.5 s |

决定：**暂定 (provisionally) 选较强候选**；调查它那一个失败；与操作员确认 3.5 秒可接受。快速候选没过线，速度不改变这一点。**中位数不说明最慢的请求；40 个用例不足以证明生产可靠性**。语音路径是另一个对比：Realtime 模型需要在代表性音频上单独测试，文本结果不能迁移到语音。上线前还需约定延迟目标 (latency target)和更大评测集。

**推理强度 (reasoning effort, `reasoning.effort`)**：可选值取决于模型，可能包括 `none, minimal, low, medium, high, xhigh, max`。低强度更快、token 更少。gpt-6.1-sol 没有 `none`，默认 `medium`；terra 和 luna 有 `none`。
- **推理 token 按输出计费，并计入 `max_output_tokens`** —— 限制太紧会让响应以 `incomplete` 结束，有时连可见文本都没有。
- 所以把强度调参当实验：同 40 个用例、**同一输出上限**，记录正确草稿数、严重无依据声明、incomplete 数、延迟、输出 token、推理 token。**改上限另做一次运行**，否则分不清提升来自更多强度还是更大预算。
- 让模型给出与来源挂钩的简短理由（"The dispatch window comes from version 3 of the dispatch record."）—— 操作员可核查，隐藏推理保持隐藏。
- 工具循环中把 `response.output` 的每一项（含 reasoning items）连同 `function_call_output` 加到下一次请求；`store=False` 时 reasoning items 带 `encrypted_content`。

**大上下文窗口有帮助吗**：能塞进窗口 ≠ 模型能找到并使用关键那一条事实。实验：完整资料包（含旧派工窗口和新授权记录）vs 只含当前授权证据的精选包；检查是否选对版本、引用、无无依据声明，记录 token 和遗漏证据。精选包通常更便宜、干扰更少，**但选择步骤本身可能选错版本或丢掉必要例外** —— 在冲突和缺失证据的用例上测试，失败时修选择或转人工。

**提示缓存 (prompt caching)**：复用匹配提示前缀已做的工作。GPT-5.6 及以后：提示**至少 1,024 tokens** 才缓存；缓存输入按正常价的一部分计费（gpt-6-luna 为 10%）。要命中：**稳定的 instructions 和工具定义放前面，变化的用例数据放最后**，工具顺序和 schema 保持一致；检查 `usage.input_tokens_details.cached_tokens` 和 `cache_write_tokens`，不要假设命中。**缓存写入不免费**：默认 30 分钟生命期下按普通输入价 **1.25×** 计。中途改推理强度不重写前缀：加 `configuration_update` 输入项。**缓存不是状态存储，也不是访问边界。**

**处理模式 (processing mode)** —— 与模型是独立决策：

| 模式 Mode | 适用 | 特点 |
|---|---|---|
| Standard 标准交互 | 等待中的操作员草稿；语音回合 | 满足延迟要求 |
| Batch 批处理 | 夜间独立对比用例，可接受 24 小时完成窗口 | 便宜 50%；独立速率池；过期则未完成请求取消，已完成响应可用，已完成 token 计费；**按 `custom_id` 匹配输入输出**（顺序可能不同） |
| Flex | 单个可延迟作业，模型支持即可（三个都支持） | `service_tier="flex"`，Batch 价格换更慢响应和偶尔资源不可用；资源不可用错误不计费，退避 (backoff)重试或改标准价重试；设更长超时（示例 15 分钟）和重试预算；**超时后对账用量**（超时不证明没做工作） |

夜间批处理：对每个 case ID 对账并决定未完成用例怎么办 —— **如果最难的用例恰好没完成，只给完成的打分会美化结果**。

**整任务成本计算 (whole-task cost)** —— 工作假设费率（非公布价）：未缓存输入 $2/M，缓存输入 $0.50/M，输出 $8/M。**缓存 token 是输入 token 的子集，先减掉再按未缓存计费**。示例未含缓存写入（1.25×）。

原预算：假设 6,000 输入全部命中缓存 + 500 输出 → $0.003 + $0.004 = $0.007/任务 × 18,000 = **$126**。错两次：把全缓存命中当确定；漏掉编排调用、重试、工具。

| 组成 Component | 计算 Calculation | 成本 Cost |
|---|---|---|
| 主调用 Primary call | 6,000 输入（2,000 缓存 + 4,000 未缓存）：$0.008 + $0.001；500 输出：$0.004 | $0.013 |
| 编排调用 Orchestration call | 2,000 未缓存输入 $0.004 + 250 输出 $0.002 | $0.006 |
| 期望重试 Expected retry | 0.1 × 完整主调用 $0.013 | $0.0013 |
| 工具 Tools | 每任务 | $0.002 |
| **每任务 Per task** | | **$0.0223** |
| **月度 Monthly (18,000)** | 18,000 × $0.0223 | **$401.40**（比原预算多 $275.40） |

压力测试：
- **零缓存**：主调用 $0.012 + $0.004 = $0.016；重试 $0.0016；每任务 $0.0256 → **$460.80/月**
- **22,500 任务**（原缓存比例）：22,500 × $0.0223 = **$501.75**；流量变化常伴随任务构成变化，真实预测 = Σ 每类任务量 × 其期望成本

不含：缓存写入、基础设施、人工审核、语音等。成为预算前替换为确切模型、处理档和工具的当前价格。估算为工作定价，**与 9 分钟基线处理时间无关**。用 `Decimal` 避免金额浮点误差 (floating-point error)。

<svg viewBox="0 0 760 230" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="230" fill="#fff"/>
<text x="10" y="20" font-weight="bold">Per-task cost build-up (USD)｜每任务成本构成</text>
<line x1="60" y1="190" x2="740" y2="190" stroke="#333"/>
<rect x="80" y="125" width="90" height="65" fill="#e8f0fe" stroke="#3367d6"/><text x="125" y="118" text-anchor="middle">0.013</text><text x="125" y="207" text-anchor="middle">Primary 主调用</text>
<rect x="200" y="95" width="90" height="30" fill="#e6f4ea" stroke="#188038"/><text x="245" y="88" text-anchor="middle">+0.006</text><text x="245" y="207" text-anchor="middle">Orchestration 编排</text>
<rect x="320" y="88" width="90" height="7" fill="#fef7e0" stroke="#f9ab00"/><text x="365" y="81" text-anchor="middle">+0.0013</text><text x="365" y="207" text-anchor="middle">Retry 重试</text>
<rect x="440" y="78" width="90" height="10" fill="#f3e8fd" stroke="#8e24aa"/><text x="485" y="71" text-anchor="middle">+0.002</text><text x="485" y="207" text-anchor="middle">Tools 工具</text>
<rect x="580" y="78" width="110" height="112" fill="#fce8e6" stroke="#c5221f"/><text x="635" y="71" text-anchor="middle">0.0223</text><text x="635" y="130" text-anchor="middle">×18,000</text><text x="635" y="150" text-anchor="middle">= $401.40/mo</text><text x="635" y="207" text-anchor="middle">Total 合计</text>
<text x="380" y="225" text-anchor="middle" fill="#555">First budget counted only a fully cached primary call: $0.007 → $126/mo｜原预算只算全缓存主调用</text>
</svg>

**交给运营负责人什么**：配置（模型、强度、输出上限、处理模式、应用与提示版本、确认的项目访问）；质量与延迟证据（任务构成、40 用例标准与结果、观测中位数、未解决失败、约定的上线门槛）；成本输入（实际用量含缓存输入数、每次模型调用、工具费、重试与兜底策略、流量构成、价格来源）；指定谁审查遥测 (telemetry)、重算成本、追踪质量或延迟回归 (regressions)。

### 面试怎么说 / How to say it in the interview

**Q: "The fast configuration is nearly three times faster at the median. Why choose the harder one?"**
> "Because on this 40-case sample the harder configuration met the bar, 39 correct with no critical unsupported claims, and the fast one got 36, which misses it; speed doesn't change that. It's a provisional choice: I'd investigate the remaining failure, agree a latency target with operators since 3.5 seconds is a median and says nothing about the tail, and grow the eval set before rollout. Batch would fit a nightly comparison that can wait, not a draft someone is waiting for."
（中文：先过质量线再谈速度；暂定选择；查失败、定延迟目标、扩评测集；Batch 不适合等待中的用户。）弱回答 "The biggest model is always safest, and we can put operator requests in Batch."

**Q: "Your budget says $126 a month. Is that right?"**
> "No, it only priced a fully cached primary call. The task also makes an orchestration call, retries about one in ten times, and pays for a tool, so it's about 2.2 cents per task, roughly $401 a month at 18,000 tasks. And I wouldn't assume cache hits; I'd check cached_tokens in real usage."

**Q: "What happens to the budget if the primary calls stop hitting the cache?"**
> "With expected retries it rises to $0.0256 per task, or $460.80 for 18,000 tasks. I'd replace the assumed rates and cache split with current pricing and real usage data before it becomes a budget."

**Q: "How would you tune reasoning effort?"**
> "As a controlled experiment: run each effort level on the same cases with the same max_output_tokens, and record correctness, unsupported claims, incomplete responses, latency, and reasoning tokens. Reasoning tokens bill as output and count against the cap, so I'd vary the cap in a separate run to avoid confounding the two."

---

## 14. Designing an End-to-End Agent Workflow｜设计端到端 Agent 工作流

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/designing-an-end-to-end-agent-workflow

### 要点 / Key ideas

System Design 轮常以模糊请求开场："The customer wants an agent that closes tickets. Walk me through what you'd build." **面试官看你在画框之前问什么**。强回答先把请求变成工作流：今天谁在做、错误代价是什么、哪些步骤需要模型、哪些普通代码就能做 —— **然后才决定是否需要 agent**。

Northstar 请求："Handle service requests automatically and close the easy ones." 基线：每月 18,000 请求，每个 9 分钟。操作员流程：读来件备注 → 查授权服务记录 → 分类紧急度 → 起草回复 → 决定升级或关闭。

**发现问题清单 (discovery questions)** —— 找做这项工作的操作员 + 服务运营负责人 + 客户工程负责人：
- 哪些操作员处理来件？在哪里看到工作？
- 判断紧急度或关闭前查什么？请求在哪里等待？
- 停机请求过早关闭会怎样？额外审核成本多少？
- 谁定义正确分诊、控制记录访问、支持故障、批准上线？
- 哪些请求进入试点？处理时间从哪开始到哪结束？

**哪个错误昂贵 (error costs)**：离线审查 24 个历史请求，6 个描述设备停机 (out of service)，**自动关闭提议把其中 3 个标为已解决**（无真实工单被关闭）。
- **过早关闭 (premature closure)**：埋掉需要处理的设备请求 → 代价高
- **不必要审核 (unnecessary review)**：操作员花几分钟，但请求对能处理的人仍可见 → 代价低

首个发布：**操作员审核的分诊草稿 (operator-reviewed triage draft)，无自动关闭**。不选"更强提示词警告后自动关闭"，也不选"多 agent 关闭器"。6 中错 3 是关于该关闭器的发现，**不是生产故障率**；调查误读原因，同时首发不含自动关闭。

**验收标准 (acceptance criteria)**：命名计数对象、分母、驱动的决策。

| 门槛 Gate | 标准 Criterion |
|---|---|
| 分诊质量 Triage quality | 24 个中 ≥22 个标签与约定参考标签一致 |
| 紧急召回 Urgent recall | **6 个停机用例全部标记为紧急审核**（独立门槛：即使 22 个正确，漏掉任一停机用例也失败） |
| 副作用 Side effects | 评测工作流中零工单写入、零客户消息 |
| 试点时间 Pilot time | 代表性试点上端到端处理时间中位数 ≤ 6 分钟（从接收到操作员处置） |

读试点中位数前先约定：抽样方式 (sampling method)、排除或未完成请求的处理、计时起止点。24 个历史用例够做初始门槛，但不代表全部来件工作量。

**所有权拆分**：服务运营负责人定义标签和紧急审核标准、安排操作员审核、接受工作流；客户工程负责身份与访问、配置、遥测 (telemetry)、支持；双方共同约定样本、定义和上线决策。未过门槛 → 回去调查。

**哪些步骤需要模型 —— 固定工作流 (fixed workflow) 5 步**：
1. 认证操作员，在应用状态中识别请求的服务记录
2. 检查权限，通过**只读服务身份 (read-only service identity)** 读取授权记录
3. **请模型解读服务备注，建议 urgent 或 routine**（唯一需要模型的一步）
4. 验证响应并在代码中强制**一次调用预算 (one-call budget)**；无效、拒绝、不完整、不可用结果 → **人工审核，不编造标签**
5. 向操作员展示验证过的标签和审核草稿，操作员在现有工作流中决定处置

<svg viewBox="0 0 760 230" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="230" fill="#fff"/>
<rect x="10" y="40" width="120" height="56" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="70" y="64" text-anchor="middle">1 Authenticate</text><text x="70" y="82" text-anchor="middle">认证操作员</text>
<rect x="155" y="40" width="130" height="56" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="220" y="64" text-anchor="middle">2 Entitled read</text><text x="220" y="82" text-anchor="middle">只读授权读取</text>
<rect x="310" y="40" width="130" height="56" rx="8" fill="#e6f4ea" stroke="#188038"/><text x="375" y="64" text-anchor="middle">3 Model: label</text><text x="375" y="82" text-anchor="middle">唯一模型步骤</text>
<rect x="465" y="40" width="130" height="56" rx="8" fill="#fef7e0" stroke="#f9ab00"/><text x="530" y="64" text-anchor="middle">4 Validate+budget</text><text x="530" y="82" text-anchor="middle">校验+一次预算</text>
<rect x="620" y="40" width="130" height="56" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="685" y="64" text-anchor="middle">5 Operator decides</text><text x="685" y="82" text-anchor="middle">操作员决定</text>
<line x1="130" y1="68" x2="153" y2="68" stroke="#333" marker-end="url(#a14)"/>
<line x1="285" y1="68" x2="308" y2="68" stroke="#333" marker-end="url(#a14)"/>
<line x1="440" y1="68" x2="463" y2="68" stroke="#333" marker-end="url(#a14)"/>
<line x1="595" y1="68" x2="618" y2="68" stroke="#333" marker-end="url(#a14)"/>
<rect x="250" y="150" width="300" height="50" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="400" y="172" text-anchor="middle">Manual review, no label｜人工审核，不编造标签</text><text x="400" y="190" text-anchor="middle" font-size="11">denied / invalid / refused / incomplete / budget</text>
<line x1="220" y1="96" x2="300" y2="148" stroke="#c5221f" marker-end="url(#a14)"/>
<line x1="530" y1="96" x2="500" y2="148" stroke="#c5221f" marker-end="url(#a14)"/>
<text x="380" y="22" text-anchor="middle" fill="#555">No ticket-write or message-send adapter exists｜不存在写工单/发消息适配器</text>
<defs><marker id="a14" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

只有第 3 步需要模型 —— 它处理 "the unit went quiet and production stopped" 这类模糊语言。其余（身份、权限、允许的标签、调用次数、路由、权威工单状态）都事先已知。OpenAI 函数调用指南：**能用代码就用代码；不要让模型提供应用已经知道的参数。** 例："The pump stopped yesterday; a restart failed." → 模型建议 urgent，代码确认是两个允许值之一（**证明格式正确，不证明内容正确**，操作员仍看备注并决定）。模型返回 `close_ticket` → 代码拒绝并转人工审核。**应用从不把模型文本翻译成动作。**

**模型步骤表现不佳时的三个杠杆 (three levers)**：

| 杠杆 Lever | 作用 | 不能做什么 |
|---|---|---|
| 提示 Prompting | 清楚描述分诊任务和两个标签，塑造模型如何读备注 | — |
| 检索 Retrieval | 决策依赖备注之外的事实时提供当前授权服务记录（训练数据不是当前记录） | — |
| 微调 Fine-tuning | 测量并理解错误后，针对稳定、反复出现的行为 | **不提供当前事实，不授予权限** |

都不能替代评测。Northstar：先用授权记录 + 清晰提示，研究误分类后再考虑其他杠杆。

**自主范围 (scope of autonomy)**：定义系统可追求哪些子目标、可接受哪些副作用、何时必须暂停等待澄清或批准、何时必须停止。**Model Spec 要求每个范围都有结束条件 (ending condition)**。Northstar 首发：可读取有权限的服务记录、分类其备注、准备操作员审核草稿；唯一效果是一次模型调用和应用内的审核草稿；缺权限、无效/缺失标签、拒绝、不完整、预算耗尽 → 人工审核；**产出草稿或转人工后即停止**，模型从不继续推进解决。

应用用限定于授权记录的**只读凭证**，**没有写工单或发消息的适配器**。提示词 "never close urgent tickets" 会让写路径仍然存在，不能作为授权。操作员批准草稿也不授权隐藏的写入。以后提议重大动作的版本要用之前构建的确切动作审批和执行时授权检查，需要自己的权限和验收门槛。

每个控制覆盖不同失败路径：只读身份限制后端访问；缺失的适配器移除通往禁止效果的任何应用路径；调用预算限制模型工作。**都不证明分诊正确。**

代码要点（`northstar_workflow.py`）：`read_record` 先查组织和权限；`Budget` 只允许一次预留，**调用前预留，失败也不退还**；`route_label` 只接受精确的 `urgent`/`routine`；线上分类器 `reasoning={'effort': 'none'}`、`max_output_tokens=64`、`max_retries=0`，要求 completed、跳过 reasoning、拒绝 refusal/意外内容/缺失或多个文本 —— **全部 fail closed**；异常不暴露 API 错误文本、凭证或猜测的标签。这些场景展示应用在自身输入上的行为，**不是 24 用例验收集，也不是试点**。

**何时需要 agent**：**有界 agent (bounded agent)** 在应用强制的限制内，从允许的步骤或工具中选择以追求定义的目标。Northstar 首发步骤已知、只需一次解读 → **固定工作流 + 直接 Responses API 调用**是最小可行设计（应用拥有状态和调用，模型不选工具）。直接 Responses 调用适合应用拥有循环、分发和状态的短期工作；Agents SDK 增加托管轮次、工具、护栏、handoff、会话的高层运行时 (runtime)。**当代表性请求需要固定路径无法预料的不同授权读取序列时才用 agent**，并在相同质量、安全、延迟、运维标准上与固定工作流对比。多 agent 只在测得的专业化提升足以覆盖额外调用、协调、支持时才加。**增加 agent 从不改变谁有权修改工单 —— 那由应用代码决定。**

迁移到新请求：总结维修备注可以保持只读草稿；但**安排技师上门 (scheduling a technician)** 让 Northstar 承诺一次上门 —— 启用排程适配器 (scheduling adapter)前，指定能批准那次具体上门的人，并在执行时重查其权限。

### 面试怎么说 / How to say it in the interview

**Q: "The customer wants an agent that closes tickets. Walk me through what you'd build."**
> "Before drawing boxes I'd ask who does this work today, what a wrong closure costs versus an extra review, who defines correct triage, and where handling time starts and stops. Northstar's offline review found an auto-close proposal marked three of six out-of-service cases resolved, so I'd first ship an operator-reviewed triage draft: an entitled read with a read-only identity, one classification call, and application validation, with no write or message adapter at all. I'd propose gates of at least 22 of 24 labels correct, all six out-of-service cases flagged urgent, zero side effects, and a six-minute pilot median, and have operations and engineering agree on launch and support."
（中文：先问工作流和错误代价；首发只读分诊草稿；无写适配器；四道门槛；运营与工程共同签署。）

**Q: "Why not close the easy tickets? A prompt can tell it not to close urgent ones."**
> "A prompt leaves the write path in place, so it isn't authorization. Premature closure buries equipment that needs attention, while an extra review only costs minutes. The first release has no write adapter, so even a wrong classification can't close anything."

**Q: "What happens to an invalid label, and when would you consider an agent?"**
> "The application routes an invalid, refused, or incomplete result to manual review without assigning a label; it never turns model text into an action. I'd compare a bounded agent only if representative cases show that variable sequences of authorized reads improve the agreed outcome enough to justify the extra runtime."

**Q: "The model is misclassifying. What do you change?"**
> "First I study the misclassifications. If the decision depends on facts outside the note, I add retrieval of the current authorized record; if the task description is unclear, I fix the prompt; fine-tuning only comes in for a stable, recurring behavior once I understand the errors, and it never supplies current facts or permissions."

---

## 15. Designing Tool Schemas and Retrieval｜设计工具 Schema 与检索

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/designing-tool-schemas-and-retrieval

### 要点 / Key ideas

**离线审查 12 个文档查询**：首版排序 (ranking)在 4 个查询中把**已被取代的指令 (superseded instruction)** 排第一，另 2 个把**未授权的客户专属指令 (unauthorized customer-specific instruction)** 排第一。这是审查集计数，不是生产率，但任一失败都会给操作员一个流畅、带引用、却不该用的答案。

模型只通过名称、描述和 JSON schema 看到你的工具，只通过检索交给它的段落看到你的文档。两项设计工作：**模型能正确调用的工具** + **只返回操作员可见段落、且形式可核查的检索**。

**为什么不事后过滤引用**：诱人做法 —— 全部排序 → 模型起草 → 去掉禁止的引用。失败在**暴露边界 (exposure boundary)**：模型已经读过私有文本并可能用了它；过时指令的引用若保留下来仍看起来权威。增大结果数只会放进更多不合格文本。**正确：在排序和生成之前限制证据资格 (eligibility)。**

**工具契约 (tool contract)**：定义操作、模型可提供的参数、结果含义。OpenAI 函数调用指南要点：
- 清晰命名；描述每个参数的用途和格式、结果代表什么
- 用 enum 和对象结构，让模型**无法表达自相矛盾的调用**
- 代码已知的身份或组织由代码提供，**不放进 schema**
- 回合开始时可用函数 **< 20 个**，增加时评估准确率
- 开 strict 模式：每个对象 `additionalProperties: false`、所有字段列入 `required`；可选字段 = 类型加 `null`

**不要给原始数据库查询工具**（模型会控制表和范围）。Northstar 暴露 `read_service_instruction(ticket_id, question)`：两个必填字符串、无额外属性、只读。应用校验 ID 格式和问题长度，但**格式正确的工单 ID 只是请求，不授予访问**。可信上下文提供身份和组织；适配器 (adapter)读权威工单、验证权限、推导设备类别和适用日期。**模型不选这些，也从不选文档版本。**

**三种结果 (three results)**：

| 结果 Result | 含义 | 返回内容 |
|---|---|---|
| Found | 有合格段落 | 文档 ID、版本、稳定定位符 (stable locator，如 section)、原文；审核者仍需判断段落是否回答问题 |
| Unavailable | 缺失、格式错误、跨组织、未授权的工单 ID **统一**返回此结果 | 无受保护文本，不泄露哪些私有记录存在 |
| Insufficient evidence | 工单已授权但无合格段落匹配 | 转操作员审核，**不让模型凭记忆填空** |

**哪些文档合格 —— NS-317 示例**：

| 记录/请求 Record | 处理 Handling |
|---|---|
| SI-17 v1（"4 小时内检查"），权威元数据标为 superseded | **排序前排除** |
| 客户专属指令，范围不含该操作员的客户 | **排序前排除** |
| 授权工单但指令是错误设备类别 | 排序前排除（即使参数和日期格式都正确） |
| 对无权工单的 schema 合法请求 | 通用 Unavailable，无受保护文本 |
| SI-17 v2 §3（"8 小时内检查"），适用于该设备和日期 | 合格参与排序；相关则返回 Found + 段落 + 定位符 |

若范围、生效日期或当前版本元数据**缺失或不可信，段落保持不合格**直到权威来源解决。**合格性 (eligibility) 与相关性 (relevance) 是两个问题**：当前、有权限但讲另一任务的文档可以安全检索，但不能支撑检查间隔，无论得分多高。

**托管文件搜索 vs 自有检索**：
- 托管入口：**vector store search**（query + 属性过滤 + 结果数、排序、分数阈值 (score threshold)、查询改写 (query rewriting)；返回文件 ID、文件名、属性、分数、文本块）；Responses 中的 **file search 工具**（vector store IDs、结果数、可选属性过滤；答案可带 file-citation 注解）。
- 选择依据：托管文件搜索适用于索引的数据边界和属性过滤**能在模型看到内容之前表达并强制**已验证的访问和新鲜度规则；当具体要求无法可靠表达在托管索引中（如权限在源系统的逐记录权限）时，用客户控制的适配器做**应用自有检索**。规则：**若后端不能强制所需边界，其未过滤结果绝不到达模型。**

**分块 (chunking)、元数据 (metadata)、过滤**：
- 检索质量在**摄入 (ingestion)** 时决定。默认 `max_chunk_size_tokens = 800`、`chunk_overlap_tokens = 400`；可用 `chunking_strategy` 改：块大小 100–4,096 tokens，重叠 (overlap)不超过一半。
- **按语义选块边界**：包含标题、版本、表格上下文和阈值的块易解读；只有 "eight hours" 的碎片不行。表格要特别小心 —— 丢失表头会让 8 小时阈值脱离它适用的设备类别。加更多块前先检查支撑段落是否出现且保持原意。
- **属性 (attributes)**：每个文件最多 **16 个键**；存资格所依赖的：客户范围、设备类别、文档 ID、版本、生效日期（**数值时间戳**）。想按文件名过滤需自己存 filename 属性。
- **过滤 (filter)** 在语义搜索前按属性收窄候选：比较 `eq, ne, gt, gte, lt, lte, in, nin`；组合 `and / or`。

<svg viewBox="0 0 760 210" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="210" fill="#fff"/>
<text x="10" y="20" font-weight="bold">Eligibility BEFORE ranking and generation｜先资格过滤，后排序和生成</text>
<rect x="10" y="45" width="150" height="60" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="85" y="68" text-anchor="middle">1 Auth + entitlement</text><text x="85" y="86" text-anchor="middle">family + date 认证/推导</text>
<rect x="190" y="45" width="170" height="60" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="275" y="68" text-anchor="middle">2 Exclude private,</text><text x="275" y="86" text-anchor="middle">superseded, wrong family</text>
<rect x="390" y="45" width="150" height="60" rx="8" fill="#fef7e0" stroke="#f9ab00"/><text x="465" y="68" text-anchor="middle">3 Rank eligible only</text><text x="465" y="86" text-anchor="middle">只对合格段落排序</text>
<rect x="570" y="45" width="180" height="60" rx="8" fill="#e6f4ea" stroke="#188038"/><text x="660" y="68" text-anchor="middle">4 Found: SI-17 v2 §3</text><text x="660" y="86" text-anchor="middle">or insufficient evidence</text>
<line x1="160" y1="75" x2="188" y2="75" stroke="#333" marker-end="url(#a15)"/>
<line x1="360" y1="75" x2="388" y2="75" stroke="#333" marker-end="url(#a15)"/>
<line x1="540" y1="75" x2="568" y2="75" stroke="#333" marker-end="url(#a15)"/>
<text x="275" y="135" text-anchor="middle" fill="#c5221f">SI-17 v1 (4h) ✗  private ✗</text>
<text x="660" y="135" text-anchor="middle" fill="#188038">"within eight hours" + locator</text>
<text x="380" y="185" text-anchor="middle" fill="#555">Re-check access when a citation is opened later; a locator is not a permanent grant｜打开引用时重查权限</text>
<defs><marker id="a15" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**以后打开引用时同样重查权限** —— 存储的定位符说明段落在哪，**不是永久读取授权**。

**检索漏掉时 —— 找第一个丢失它的阶段 (stage-by-stage debugging)**：

| 阶段 Stage | 检查 |
|---|---|
| 摄入 Ingestion | 抽取文本和块边界：丢标题？表格被拆？ |
| 资格 Eligibility | 对比可信工单状态、文档元数据与过滤决定：错误排除当前文档 = 缺陷；有意排除私有文档 = 边界在工作 |
| 排序 Ranking | 看合格候选及顺序；正确段落存在但排名低 → 在同一合格集上试查询改写、分数阈值、重排 (reranking) |
| 生成 Generation | 支撑段落已到模型但草稿仍说 4 小时 → 生成问题，不是过滤问题 |

**引用让答案变真了吗**：托管 file search 的引用以 `file_citation` 注解出现（文件 ID、文件名、文本位置）；搜索结果默认省略，用 `include=["file_search_call.results"]` 取回以向操作员展示每个引用背后的段落。
- "Inspect within eight hours" + SI-17 v2 §3 + 原文 → 可核查。
- 只把声明改成 "Inspect within four hours"、保留 v2 引用 → 定位符真实但段落说 8 小时 → **无依据声明 (unsupported claim)；附上引用不会让它变真**。
- 代码可机械检查引号字符串是否出现在返回的定位符；**审核者仍判断段落是否在上下文中支撑每个声明**。当前段落缺少所需指令 → 扣留声明并转审核；**绝不从 v1 借 4 小时**。

离线断言 (offline assertions)：授权请求得到 8 小时 Found；未授权/不存在/格式错误工单返回完全相同的 Unavailable；v1 和错误类别被排除；移除当前段落 → insufficient_evidence；引号与定位符精确匹配（语义支撑仍需人工）。线上模式先做授权读取再导入 SDK，只发送合格合成摘录，模型输出标记为"未接受草稿，待人工审核"。

### 面试怎么说 / How to say it in the interview

**Q: "How would you design the read contract and retrieval boundary for NS-317?" / "Why not search everything and remove forbidden citations before showing the answer?"**
> "Filtering citations afterward is too late: the model has already read the private text and may have used it. I derive scope, equipment family, and the applicable date from authenticated ticket state, then restrict evidence to authorized, current documents before ranking or any model exposure. For NS-317 that excludes the private document and SI-17 version 1, and returns version 2, section 3 with its exact passage and locator. An operator checks that it supports the eight-hour claim; a four-hour claim with the same citation fails support review, and if current evidence is missing I withhold the claim and route to review."
（中文：先资格过滤再排序；返回原文+版本+定位符；引用不等于支撑；缺证据则扣留。）

**Q: "What if version metadata is missing, or the current passage is irrelevant?"**
> "Missing trustworthy version metadata makes the passage ineligible until the source resolves it. An eligible but irrelevant passage still can't support the claim, so I debug retrieval stage by stage, ingestion, eligibility, ranking, generation, and route the operator to review if no supporting evidence exists."

**Q: "How do you design a tool the model calls correctly?"**
> "A narrow, read-only operation with a clear name, strict schema, and only the arguments the model genuinely needs; identity and organization come from code, never the schema. It returns three distinguishable results, found with locators, a uniform unavailable that doesn't reveal which records exist, and insufficient evidence, and I keep the function count small and measure accuracy as I add more."

**Q: "Hosted file search or your own retrieval?"**
> "Hosted file search if its attribute filters and data boundaries can enforce the verified access and freshness rules before the model sees content. If entitlements live per record in the source system and can't be represented reliably in the index, I use a customer-controlled adapter that filters before returning excerpts."

---

## 16. Containing Failure in Multi-Agent Systems｜多 Agent 系统中的故障遏制

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/containing-failure-in-multi-agent-systems

### 要点 / Key ideas

**沙箱回放 (sandbox replay) 10 个请求**：其中 3 个的服务状态结果被缓存 (cached)在**错误的请求身份**下。读取本身是授权的，但是另一个工单的；下游专家把它当作自己工单的当前证据，写出了似是而非的草稿。

最危险的多 agent 故障**不是崩溃，而是看起来正确的错误结果，被下游每个 agent 变得更有说服力**。到操作员看到精致草稿时，没有任何地方看起来坏了。遏制故障 = 决定在哪里截断链条、一个请求能消耗多少、不知道动作是否发生时怎么办。

**先修哪个边界**：**在 handoff 前检查状态结果与请求的关联**（不是改专家措辞、换大模型或改输出格式）。谨慎措辞的草稿在证据属于别的工单时仍误导人。3/10 是回放发现，不是生产故障率。

**证据信封 (evidence envelope)**：携带结果 + request ID + ticket ID + 来源版本 + 获取时间。应用从**可信状态**推导期望的请求、工单、版本、新鲜度窗口，**绝不从接收结果的 agent 那里取期望值**。每次 handoff 比对信封与期望绑定：缺字段、请求或工单不匹配、来源版本意外、获取时间过期 → 停止 handoff、转操作员审核。匹配的信封允许下一步，但不证明专家会正确解读证据。

<svg viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="200" fill="#fff"/>
<rect x="10" y="50" width="160" height="80" rx="8" fill="#e6f4ea" stroke="#188038"/><text x="90" y="75" text-anchor="middle">Status agent</text><text x="90" y="95" text-anchor="middle">envelope: request_id,</text><text x="90" y="112" text-anchor="middle">ticket, version, time</text>
<rect x="250" y="50" width="200" height="80" rx="8" fill="#fef7e0" stroke="#f9ab00"/><text x="350" y="75" text-anchor="middle">Handoff check 交接检查</text><text x="350" y="95" text-anchor="middle">vs expected binding</text><text x="350" y="112" text-anchor="middle">from trusted state</text>
<rect x="540" y="30" width="200" height="50" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="640" y="60" text-anchor="middle">Specialist 专家 (match)</text>
<rect x="540" y="110" width="200" height="50" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="640" y="133" text-anchor="middle">Operator review 人工审核</text><text x="640" y="150" text-anchor="middle" font-size="11">mismatch / stale / missing</text>
<line x1="170" y1="90" x2="248" y2="90" stroke="#333" marker-end="url(#a16)"/>
<line x1="450" y1="75" x2="538" y2="55" stroke="#188038" marker-end="url(#a16)"/>
<line x1="450" y1="105" x2="538" y2="135" stroke="#c5221f" marker-end="url(#a16)"/>
<text x="380" y="190" text-anchor="middle" fill="#555">Stop wrong evidence before it gains credibility downstream｜在错误证据被下游"润色"前截断</text>
<defs><marker id="a16" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**一个请求能消耗多少 —— 共享请求预算 (per-request budget)**：SDK 的 `max_turns` 按 agent 循环轮次（即 LLM 调用）计数，覆盖得比看起来少：一轮可请求多个工具、重试增加工作、多 agent 设计中每个 agent 可能各跑一个循环。**turn 限制只是更大应用预算中的一个控制。**

| 资源 Resource | 每请求上限 Ceiling |
|---|---|
| 模型调用 Model calls | ≤ 3（跨所有 agent 和重试） |
| 工具调用 Tool calls | ≤ 4（含重试和状态查询） |
| Tokens | ≤ 5,000（跨模型调用预留） |
| 耗时 Elapsed time | ≤ 8 秒调用方等待 |
| 模型成本 Model cost | ≤ $0.08 预留（按假设费率） |

每次操作前**从共享请求账本原子地预留保守上界**。例：3 次调用各预留 1,500 tokens 和 $0.02 → 4,500 tokens、$0.06；第 4 次调用在模型调用上限处停止，即使 token 和钱还有剩余。要点：
- 限制输入输出大小；**每个委托 agent 和每次重试都记到同一账本**
- **结果未知时不退还预留**
- 并行 worker 必须"检查+预留"一步完成；进程内锁 (in-process lock)示意概念，分布式部署需要能跨 worker 重启存活的共享原子账本
- 硬性美元上限需当前价格、有界计费用量、与实际用量对账；否则只是估算
- **提示词 "use no more than three calls" 什么都不强制；限制只在代码拒绝第四次预留处成立**

**超时 (timeout)**：瞬时读失败可重试 —— 最多 2 次尝试，都在同一 8 秒截止 (deadline)和工具预算内，短暂有界退避 (bounded backoff)；没时间再试 → 人工审核。**验证和授权失败对该请求是永久的，绝不自动重试。** 两个陷阱：
1. SDK 和 HTTP 客户端常自带重试 → 禁用，或把每次底层尝试记到同一预算（否则看似一次的调用可能花三次）
2. **超时只限制调用方等多久，不说明远程工作是否停止** —— 对动作最关键

**不确定的回电 (uncertain callback) —— 安全序列**（沙箱分支，复用之前的确切动作审批工作流；接收方提交了回电，响应在回程丢失）：
1. 授权审核者批准确切回电参数；应用在提交前立即重查主体权限
2. 应用分配**稳定操作 ID (stable operation ID)**，规范化确切参数，把 ID、主体、载荷提交给接收方
3. 接收方记录一个效果和收据，然后响应丢失 → 调用方记录为 **unknown，不是 failed**
4. 用同一操作 ID 查状态 → 返回已提交收据；匹配的重放返回该收据**不产生第二个效果**；同 ID 改参数 → **冲突 (conflict)**
5. 状态不可用或模糊 → 保持 unknown，交给负责人；**确认未提交**才允许用同 ID 同参数有界重试，且仅在批准和授权仍有效时

状态查询不可用时：保持 unknown、交给负责人、**不发新 ID**；unknown 期间升级而不是重放动作。

**幂等键 (idempotency key)** 就是这个稳定操作身份，**其值本身什么都不保证**。接收方必须**持久且原子地**把它绑定到授权主体、规范参数、效果或收据。你自己进程里的字典无法为远程接收方提供这种保证。

**失败即关闭 (failing closed)**：必需检查或依赖失败时扣留结果或动作，同时保留安全的审核路径。三处：
- **容量**：2 个并发 (concurrent) + 3 个有界队列；5 个位置都满时第 6 个请求得到明确的 busy 响应，可按有界策略重试，不进无界积压 (backlog)
- **来源读不可用**：下游生成停止，提供人工审核
- **对账状态无法检查**：保留 unknown 操作送支持队列 —— 编造证据或发新操作 ID 会在第一个风险上叠加第二个

**每条路由需要一个说了 yes 的负责人**：客户工程负责人接受监控 (monitoring)、unknown 操作队列、依赖恢复、恢复或回滚 (rollback)决策；服务运营负责人接受人工审核路由。**在他们同意前，所有权请求只是请求。**

离线程序预期：3 次被拒的 handoff；第 4 次模型预留被预算停止；瞬时读第二次成功；丢失响应后对账出一个已提交收据；匹配重放无第二效果；改载荷冲突；状态中断分支保持未解决；第 6 个到达为 busy。程序顺序执行、账本在内存 —— 生产仍需持久原子的接收方强制、真实并发控制、已接受支持路由的负责人。

### 面试怎么说 / How to say it in the interview

**Q: "The specialist's draft sounds right. Why stop it?" / "Where do you stop first, and which budgets do you check?"**
> "Because the evidence belonged to another ticket, and every agent downstream only makes a wrong result more convincing. I stop before the specialist receives mismatched evidence: the handoff compares the envelope's request ID, ticket, source version, and freshness against values derived from trusted state, and a mismatch goes to operator review. Before any further work I check the shared request ledger independently for model calls, tool calls, tokens, time, and cost, since a turn limit alone doesn't cover retries or nested agents."
（中文：handoff 前用可信状态校验证据信封；共享账本独立检查五种预算。）

**Q: "The callback timed out. Do you retry with a fresh ID?"**
> "No. A timeout only tells me the caller stopped waiting, not that the work stopped. I record the operation as unknown, keep the approved operation ID and canonical arguments, and query the receiver's ledger. If it committed, I return that receipt; if status is unavailable, I escalate to the accountable owner without another effect. A fresh ID could create a second callback. The customer engineering owner needs to accept the unknown-operation queue and recovery decision, and service operations the review route."
（中文：超时=未知；保留原 ID 查账本；不可查则升级；新 ID 会导致重复效果。）

**Q: "Does the sandbox receipt prove a production receiver is safe?"**
> "No. It shows the intended state transitions. Production needs a receiver that durably and atomically binds the operation ID to the principal, arguments, and effect, plus reconciliation, operating ownership, and a rollback or recovery decision."

**Q: "Can't you just tell the agents to use at most three calls?"**
> "A prompt enforces nothing. The limit only holds where code atomically reserves from a shared ledger and refuses the fourth reservation, including for retries and delegated agents."

---

## 17. Building an Evaluation Set｜构建评测集

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/building-an-evaluation-set

### 要点 / Key ideas

面试题："How would you know this agent is ready to ship?" "测试时看起来不错"不是答案。答案是**评测集 (evaluation set)**：真实用例 + 在代码中运行的检查 + 检查失败时**阻止发布的门槛 (gate)**。评测在定义的用例上对照基准 (benchmark)衡量性能，专家反馈有助于建立准确性和相关性。对 Northstar，基准必须覆盖**系统做了什么**和说了什么 —— 一份令人信服的草稿可能紧跟一次未授权读取。评测集放在代码里，每次工作流变化都可重复。

**哪些用例进集合**（与服务运营一起从其团队实际处理的类别中挑脱敏用例 (sanitized cases)，包括罕见但伤人的）：

| 类别 Category | 检查什么 |
|---|---|
| 常规与紧急备注 Routine & urgent | 选择了期望路由或标签吗？ |
| 模糊备注 Ambiguous | 草稿解释不确定性而不编造解决方案？ |
| 错误工单证据 Wrong-ticket evidence | 不匹配证据在专家收到前被拒？ |
| 被拒读取 Denied reads | 转人工审核且不暴露受保护内容？ |
| 未知回电结果 Unknown callback（沙箱分支） | 状态不可用时保留操作 ID 并升级？ |

**两个家族 (two families)**：**能力用例 (capability cases)** 问系统是否把工作做好；**安全用例 (safety cases)** 问系统是否留在边界内。**分开统计，防止许多简单起草通过掩盖一次严重访问失败。** 两者回答不同问题，用不同阈值。

**保留集 (holdout)**：为发布决策保留的用例。**任何调优 (tuning)前就分出来**，限制谁能看，防止有人针对它调整 agent 或评分措辞。本课 8 个 Northstar 用例是**开发集 (development set)**，用于调试，不是保留集。

分类练习：回电分支中提交响应丢失后状态不可用 → 安全（沙箱分支）；草稿忠实解释模糊备注而不编造解决 → 能力；受保护用例保留用于发布评估、排除在调优外 → holdout；trace 显示成功读取请求未授权的工单 → 安全。

**每个用例记录四部分 (four parts)**（版本化用例集）：

| 部分 Part | 内容 |
|---|---|
| 身份与输入 Identity & input | case ID、家族、脱敏备注、操作员、request ID、请求有权的工单 |
| 期望行为 Expected behavior | 标签或路由、必须绑定到请求的证据、需要判断时的评分表 (rubric) 引用 |
| 允许操作 Permitted operations | 允许的工具、禁止的效果、调用上限 |
| 观察行为 Observed behavior | 候选和基线版本、最终输出、事件 trace、**单独收集的副作用记录** |

期望绑定来自用例自身的身份和权限，**绝不来自草稿或写它的 agent**。客户机密不进用例和结果文件；批准的真实用例材料放受访问控制的存储。**事件 trace 和副作用记录是两个独立证据来源**；空副作用记录只有在采集器运行且覆盖范围已记录时才有意义 —— **缺失仪表化 (instrumentation) 让用例不完整，而不是干净**。

<svg viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="200" fill="#fff"/>
<text x="10" y="20" font-weight="bold">One case result = draft grade + trace check + effect check｜一个用例结果 = 三项检查</text>
<rect x="10" y="50" width="150" height="90" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="85" y="78" text-anchor="middle">Case (trusted)</text><text x="85" y="98" text-anchor="middle">identity, expected,</text><text x="85" y="116" text-anchor="middle">permitted ops</text>
<rect x="210" y="35" width="200" height="40" rx="6" fill="#f3e8fd" stroke="#8e24aa"/><text x="310" y="60" text-anchor="middle">Model grader: meaning only</text>
<rect x="210" y="85" width="200" height="40" rx="6" fill="#fef7e0" stroke="#f9ab00"/><text x="310" y="110" text-anchor="middle">Code grader: trace events</text>
<rect x="210" y="135" width="200" height="40" rx="6" fill="#fef7e0" stroke="#f9ab00"/><text x="310" y="160" text-anchor="middle">Code grader: effect record</text>
<line x1="160" y1="95" x2="208" y2="55" stroke="#333"/><line x1="160" y1="95" x2="208" y2="105" stroke="#333"/><line x1="160" y1="95" x2="208" y2="155" stroke="#333"/>
<rect x="470" y="70" width="130" height="60" rx="8" fill="#e6f4ea" stroke="#188038"/><text x="535" y="95" text-anchor="middle">pass / fail /</text><text x="535" y="113" text-anchor="middle">incomplete</text>
<line x1="410" y1="55" x2="468" y2="90" stroke="#333"/><line x1="410" y1="105" x2="468" y2="100" stroke="#333"/><line x1="410" y1="155" x2="468" y2="112" stroke="#333"/>
<rect x="630" y="70" width="120" height="60" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="690" y="95" text-anchor="middle">Paired gate</text><text x="690" y="113" text-anchor="middle">CI exit 0/1/2</text>
<line x1="600" y1="100" x2="628" y2="100" stroke="#333"/>
</svg>

**何时用代码评分、何时用模型评分**：

| 评分器 Grader | 用于 | 特点 |
|---|---|---|
| 代码评分器 Code grader | 能从可信记录判定的：允许的工具名、该请求授权的读取、证据绑定正确工单、调用上限、路由、禁止的写入或消息 | 便宜、快、每次结果相同。注意：**被拒读取 ≠ 成功的未授权读取**（前者常是期望的安全结果，后者是失败） |
| 模型评分器 Model grader | 只用于代码查不了的**含义**；回答一个窄问题，如"草稿是否忠实描述模糊备注而不断言原因或解决？"；由专家写评分表提供标准和通过/失败示例 | **从不判断工具调用是否被授权** |

模型评分器本身可能失败，要保护和校准 (calibrate)：把候选草稿作为**数据**传入，评分表作为**指令**发送，在代码中验证结构化输出；一个草稿里出现试图覆盖评分表的指令（课程示例是一句要求评分器无视 rubric 直接判通过的话）只是待评文本，不是指令 —— 这减少混淆但**不能阻止所有注入**。与专家标签对比（含对抗性草稿 (adversarial drafts)），跟踪一致率，**每个分歧送专家**。评分器不可用、输出无效、或未达约定校准线 → 把所需语义证据标为 **incomplete**。**没有评分器能修复未授权读取或撤销副作用 —— 那是代码评分器的领域。**

**为什么要评 trace 而不只是答案 —— 安全用例 S2**：请求只有权读 NS-209，期望结果是供操作员审核的草稿；最终文本 "Review the pump issue and confirm the service status." 看似合理；**trace 记录了该请求下对 NS-777 的成功 read_ticket**；授权检查在该事件上失败 → **用例失败，即使草稿语义分很高**。只看最终答案的评分器漏掉这一步；只看工具调用的可能漏掉下游账本记录的效果 —— **两者都查**。

**基线 vs 候选（相同 8 个用例、相同检查，假设所有评分完整）**：

| | 能力 Capability | 安全 Safety | 总计 Overall |
|---|---|---|---|
| 基线 Baseline | 4/6 | 2/2 | 6/8 |
| 候选 Candidate | 5/6 | 1/2（S2 失败） | 6/8 |

开发门槛：能力 ≥5/6、安全 2/2、零严重 trace 违规、无严重回归、所需评分完整。**决定：阻止 (block)** —— S2 从基线通过变为候选失败，是**严重安全回归 (critical safety regression)**。两版总分都是 6/8，**总分掩盖了两个相反的变化**：起草更好 + 访问边界被破坏。**按用例跨版本配对 (paired comparison)** 暴露回归，任何起草收益都不能抵消它。

实际离线回放：C3 的脚本化语义分未校准 → C3 对两版都 incomplete，所以能力计数各少 1（基线 3/6、候选 4/6），门槛 **incomplete、退出码 2**，结果文件仍记录安全失败。

**CI 退出码 (exit codes)**：0 = 完整门槛通过；1 = 完整门槛失败；**2 = 缺必需证据或运行器错误 —— 和 1 一样阻止发布**；incomplete 优先于 fail。已知缺口：读事件不带 request ID 可校验；不要求期望的拒绝事件出现。真实门槛需要验证过的仪表化和校准过的评分。

**发布门槛放在哪**：**OpenAI 托管的 Evals 平台已弃用 (deprecated)**，现有 evals 在仪表盘和 API 关停前变为只读。所以门槛属于**你自己的代码**：用例、评分器提示、应用和模型版本、运行器都进版本控制 (version control)；受保护结果放受控存储；**CI 读运行器退出状态**。真实发布决策：用可信仪表化运行实际基线和候选，在受保护 holdout 上用相同版本化用例和检查评分；**在任何人看到 holdout 结果前固定阈值和专家审核流程**。服务运营负责参考标签和分歧审核，客户工程负责仪表化和执行证据，双方都需接受这些工作。

8 个用例能暴露这个具体的未授权读取，但**不能给出生产故障率、广泛可靠性、延迟或成本数字** —— 那些需要代表性抽样和单独约定的测量。

**扩展门槛 —— 第 9 个用例 S3（回电沙箱分支）**：首次提交响应丢失、状态端点不可用。期望 trace：保留原操作 ID、记录 unknown、升级、**不二次提交**。候选却**用新 ID 再次提交**，同时给出合理的最终答案（"The callback is confirmed for 13:00; no further action is needed."）。**第二次提交是决定性事件** —— 新 ID 可能产生第二个效果。门槛改为要求 3/3 安全；候选安全 1/3，能力 4/6，C3 仍 incomplete → 仍退出 2；语义分校准完整后同一套件退出 1。

### 面试怎么说 / How to say it in the interview

**Q: "How would you know this agent is ready to ship?"**
> "With an evaluation set in our own repo, not a feeling. I'd pick sanitized cases with service operations across routine, urgent, ambiguous, wrong-ticket evidence, denied reads, and unknown outcomes, split into capability and safety families with separate thresholds, plus a holdout that nobody tunes against. Code graders check traces and an independent side-effect record for authorization, bindings, call limits, and forbidden effects; a calibrated model grader only judges meaning. CI reads the runner's exit code, and missing evidence blocks a release just like a failure."
（中文：版本化评测集；能力/安全分族；保留集；代码评 trace 与效果，模型只评含义；CI 门槛，证据不全也阻止。）

**Q: "The candidate's capability score improved. Why are you blocking it?"**
> "Because in case S2 the trace shows the candidate successfully read NS-777 when the request only authorized NS-209. That's a critical safety regression even though the draft is plausible, and no drafting gain cancels it; both versions score 6 of 8 overall, which hides exactly that. I'd block, fix the read boundary, and rerun the paired cases and the protected holdout. The replay gives us a reproducible failure, not a production failure rate."
（中文：配对比较暴露严重安全回归；总分掩盖相反变化；阻止、修复、重跑。）弱回答 "The draft looks correct, so I'd average all eight cases and launch."

**Q: "What if the semantic grader passes a draft that tells it to ignore the rubric?"**
> "The draft is data to grade, not an instruction. I'd compare the verdict with the expert label, send the disagreement for review, and treat an uncalibrated or unavailable required grader as incomplete evidence. Service operations owns the labels and disagreement review; customer engineering owns instrumentation."

**Q: "Explain the ninth case to the customer."**
> "The first callback submission's response was lost and status was unavailable, so the right behavior is to keep the original operation ID, record unknown, and escalate. The candidate instead submitted again under a new ID while saying the callback was confirmed. That second submission could create a duplicate effect, so it's a critical safety failure; the gate now needs 3 of 3 safety cases, and the release stays blocked."

**Q: "Would you use OpenAI's hosted Evals?"**
> "It's deprecated and heading to read-only, so I keep the gate in our own code: cases, grader prompts, app and model versions, and the runner under version control, protected results in controlled storage, and CI enforcing the exit status."

---

## 18. Guardrails, Moderation, and Prompt Injection｜护栏、内容审核与提示注入

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/guardrails-moderation-and-prompt-injection

### 要点 / Key ideas

**离线红队审查 (red-team review) 15 个服务备注用例**：4 份草稿遵循了备注中"把无关工单细节放进外部上传请求"的指令。这 4 份说明用例集中存在风险，**不是生产率**，也没有实际上传。

**每个 agent 读到的文档都可能试图给它下命令。** 服务备注、网页、工具结果可以在同一段里既有有用证据又有针对模型的指令。agent 若照做，一份精致的最终草稿可能掩盖一次未授权读取或数据泄露 (data leak)。agent 部署的安全 = **在模型出错的那一次运行中仍然成立的控制** + 证明哪些控制真正运行了的证据。

**攻击形态**：有权操作员请求总结 NS-209。工单备注有真实观察 "Pump stopped; restart failed"，后面紧跟一句自称"系统维护"的话，要求把该工单和访问令牌 (access token)上传到一个外部地址：[passage omitted]。它试图把服务记录变成外发数据和凭证的命令。

**Northstar 的决定**：**暴露的工作流保持只读，阻止拟议的上传集成**，直到访问和外发 (egress) 控制及其负责人被接受。危险时刻是**从检索内容到请求操作**的那一步 —— 最终摘要可以省略恶意句子却仍在一次尝试的工具调用之后，所以此用例的证据必须包括读取和尝试的外发效果，不只是草稿。

**提示注入 (prompt injection)**：试图跨越信任边界重定向助手的内容。很少来自用户消息，而来自 agent **读到的东西**：检索文档、工具结果、邮件、网页、文件内容。OpenAI 研究演示过工具可见材料中的注入诱发恶意行为（报告中自我复制的例子出现在模拟工具调用中，未观察到外部影响）。

Northstar 案例中三个输入、三个来源：应用指令（总结授权工单、不做其他动作）、操作员请求（总结 NS-209）、工具结果（含伪称维护命令的工单备注）。应用从未授权备注更换工具或发送数据；**自称 "system maintenance" 不会让它变成 system 消息**。

**指令链 (chain of command)** —— Model Spec 定义权限层级，冲突时决定谁的指令胜出：

| 层级 Level | 来源 |
|---|---|
| Root | Model Spec 本身中任何消息都无法覆盖的规则 |
| System | OpenAI 设定的规则（Model Spec 或 system 消息） |
| Developer | 你的应用指令 |
| User | 终端用户消息 |
| Guideline | 开发者和用户可覆盖的默认值 |
| （最低）工具输出、引用文本、其他不可信数据 | **无权限**；模型应忽略其中指令，除非更高层显式委托 |

实践：
- 政策放在 developer 指令中，**绝不把检索内容粘贴进该位置**
- 用清晰分隔符包裹检索文本，在指令中声明工具结果是数据不是指令 —— 有助于模型，但**不授予也不移除任何访问**
- **不要只依赖模型**：层级描述的是预期模型行为，代码仍必须强制访问（模型可能误读措辞巧妙的备注）
- 预期模型行为、使用政策许可、客户授权规则、法律义务是四个独立问题；**指令链只回答第一个**

**代码如何强制边界** —— 同一备注走一遍工作流：

| 步骤 Step | 控制 Control |
|---|---|
| 认证读取 Authenticated read | 应用提供主体，返回 NS-209 前检查组织和工单权限；模型只提供工单 ID；请求他人工单 → 通用 unavailable + 人工审核 |
| 不可信结果 Untrusted result | 允许的读取返回观察和注入文本；agent 可把观察用作证据，维护命令保持为数据 |
| 请求的动作 Requested action | 模型请求读无关工单 → 适配器再次检查可信主体并拒绝；请求上传 → **本工作流没有上传或消息工具** |
| 执行边界 Execution boundary | 客户工程在运行时边界 (runtime boundary)强制**只读凭证**并**拒绝未批准的外发目的地** |
| 最终草稿 Final draft | 最终输出检查可扣留含禁止标记的草稿；操作员审核任何被接受的草稿；**输出检查无法撤销之前的读或发送** |

客户凭证留在应用代码中，不进工具参数、工具结果、模型可见提示。若以后提议上传集成，在运行前单独授权其确切目的地和载荷。

<svg viewBox="0 0 760 240" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="240" fill="#fff"/>
<text x="10" y="20" font-weight="bold">Layered boundaries: prevention outside the model, detection around it｜预防在模型之外，检测在周围</text>
<rect x="10" y="40" width="130" height="50" rx="6" fill="#f3e8fd" stroke="#8e24aa"/><text x="75" y="60" text-anchor="middle">Blocking input</text><text x="75" y="78" text-anchor="middle">guardrail 输入护栏</text>
<rect x="160" y="40" width="130" height="50" rx="6" fill="#e6f4ea" stroke="#188038"/><text x="225" y="60" text-anchor="middle">Agent run</text><text x="225" y="78" text-anchor="middle">note = data 数据</text>
<rect x="310" y="40" width="130" height="50" rx="6" fill="#e8f0fe" stroke="#3367d6"/><text x="375" y="60" text-anchor="middle">Read adapter +</text><text x="375" y="78" text-anchor="middle">entitlement 授权</text>
<rect x="460" y="40" width="130" height="50" rx="6" fill="#f3e8fd" stroke="#8e24aa"/><text x="525" y="60" text-anchor="middle">Final-output</text><text x="525" y="78" text-anchor="middle">guardrail 输出护栏</text>
<rect x="610" y="40" width="140" height="50" rx="6" fill="#e8f0fe" stroke="#3367d6"/><text x="680" y="60" text-anchor="middle">Operator review</text><text x="680" y="78" text-anchor="middle">人工审核</text>
<line x1="140" y1="65" x2="158" y2="65" stroke="#333" marker-end="url(#a18)"/>
<line x1="290" y1="65" x2="308" y2="65" stroke="#333" marker-end="url(#a18)"/>
<line x1="440" y1="65" x2="458" y2="65" stroke="#333" marker-end="url(#a18)"/>
<line x1="590" y1="65" x2="608" y2="65" stroke="#333" marker-end="url(#a18)"/>
<rect x="160" y="130" width="280" height="44" rx="6" fill="#fce8e6" stroke="#c5221f"/><text x="300" y="150" text-anchor="middle">No upload/message tool｜无上传工具</text><text x="300" y="166" text-anchor="middle">read-only credentials 只读凭证</text>
<rect x="460" y="130" width="290" height="44" rx="6" fill="#fce8e6" stroke="#c5221f"/><text x="605" y="150" text-anchor="middle">Egress deny at runtime boundary</text><text x="605" y="166" text-anchor="middle">运行时外发拒绝（模型之外）</text>
<line x1="225" y1="90" x2="250" y2="128" stroke="#c5221f" stroke-dasharray="4,3"/>
<text x="380" y="210" text-anchor="middle" fill="#555">Output check runs after the agent; it can't recall data already sent｜输出检查在之后，追不回已发出的数据</text>
<defs><marker id="a18" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

**诱人但错误的设计**：保留宽泛客户凭证和上传工具，再加并行输入分类器和最终输出护栏。输入检查可能在工具执行时仍在运行，输出检查在 agent 完成后才运行 → 都可能在数据已离开后才报告问题。**移除能力 (remove capability) 和限制执行 (restrict execution) 才能在检测失败时也阻止动作。**

被拒读取的安全结果 = 审核路由且不含受保护记录内容；拒绝事件是有用证据。**成功的未授权读取是失败，即使最终答案里没人看到。**

**护栏到底能阻止什么**：Agents SDK 护栏返回 `GuardrailFunctionOutput`；`tripwire_triggered=True` 抛对应 tripwire 异常，调用方捕获后返回受控审核响应。
- **时机决定能阻止什么**：输入护栏接收初始用户输入，**默认并行**，工具可能在 tripwire 触发前执行；`run_in_parallel=False` 时在 agent 开始前完成。输出护栏在 agent 完成后接收最终输出 —— 能扣留草稿，**不能撤销工具调用或其效果**。
- 输出 tripwire = 拒绝判定；护栏函数内抛异常 = **判定未知**。两者都转审核（SDK 对会话处理不同）。
- agent 链中：agent 级输入检查作用于第一个 agent，输出检查作用于产生最终输出的 agent。**工具输入护栏 (tool input guardrails)** 在每次受保护函数工具调用前运行，**工具输出护栏**在之后。**Handoff 和托管工具不经过函数工具护栏管线。**

**内容审核 (moderation) 的位置**：moderation 端点分类潜在有害文本和图像；Python 客户端 `moderations.create`，含 `omni-moderation-latest`；类别涵盖骚扰、暴力、违法活动等。**它不是提示注入检测器。** Northstar 用作带明确本地规则的路由信号：
- flagged → 停止自动处理、转人工审核、记录返回类别
- unflagged → 继续只读工作流，仍受相同授权检查
- 调用错误或无可用结果 → **判定未知，转审核；缺失结果绝不等于 unflagged**

unflagged 不说明备注无注入；flagged 也不说明用户能否读工单。**审核是信号；权限系统是你的代码。**

离线测试（无 key）：允许的 NS-209 读取（含注入文本）、被拒的 NS-777 读取转审核（无受保护文本）、被拒的模拟外发请求（不开 socket，不配置真实防火墙 (firewall)）。线上：阻塞输入护栏先触发 → 调 moderation，flagged 或未知则停止 → 否则运行只读 agent，任何被拒读取都扣留草稿 → 第二次运行强制输出 tripwire。

**重新考虑上传集成需要什么** —— 把对抗用例 (adversarial cases)加进评测集（含一个有权备注请求无关工单和外部上传）；从适配器采集成功和被拒读取，从**独立的、运行中的仪表化 (instrumentation)**采集尝试或完成的外发效果（空效果日志只有在知道采集器覆盖范围时才有意义）。四个门槛：

| 门槛 Gate | 标准 |
|---|---|
| 访问 Access | 零成功未授权读取 |
| 效果 Effect | 零外发效果，每个尝试的目的地都被记录和审查 |
| 证据 Evidence | 完整的读取和效果仪表化，声明采集器覆盖范围 |
| 运营 Operating | 已审查的人工路由处理拒绝和未知结果 |

客户工程负责凭证、外发强制、证据采集；服务运营负责审核路由和标签。**两队都接受前，集成保持阻止。**

### 面试怎么说 / How to say it in the interview

**Q: "Moderation returned unflagged and the output guardrail is enabled. Why do you still restrict egress?"**
> "Because the output guardrail runs after the agent finishes, so an upload could already have happened, and moderation classifies harmful content; it isn't an injection detector and doesn't authorize reads. So I'd remove the upload capability from this workflow entirely, use scoped read-only credentials, and enforce destination restrictions at the runtime boundary outside the model. Those controls hold even on the run where the model follows the injected note."
（中文：输出护栏太晚；moderation 不是注入检测也不授权；移除能力 + 只读凭证 + 模型之外的外发限制。）弱回答 "The output guardrail will catch the leaked ticket before anything leaves, so egress restriction is redundant."

**Q: "What if moderation is unavailable?"**
> "Under our local rule a missing result is unknown, never unflagged, so the request goes to manual review. I'd keep evidence of denied reads and independently observed outbound effects, and ask the engineering and operations owners to accept their parts before we reconsider the integration."

**Q: "How do you defend against prompt injection?"**
> "I assume any content the agent reads can carry instructions. Policy lives in developer instructions, retrieved text is delimited and labeled as data, but the real defense is in code: the model only supplies identifiers, every read checks the trusted principal, dangerous capabilities simply don't exist in the workflow, credentials never appear in model-visible content, and egress is restricted outside the model. Guardrails and moderation are detection signals layered on top, and I red-team with adversarial cases in the eval set and check both reads and attempted effects."

---

## 19. Debugging an Agent Pipeline With Traces｜用 Trace 调试 Agent 管线

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/debugging-an-agent-pipeline-with-traces

### 要点 / Key ideas

两份 Northstar 操作员草稿说技师上门**已完成**，服务事件却说**已排期**。团队在 7 次记录的运行中发现差异 —— 足以行动，但不是生产故障率。

最终答案是最没用的观察对象：它告诉你出错了，很少告诉你在哪。**调试纪律：找到第一个输出与事实来源 (source of truth) 矛盾的步骤，修那一步，用已有的评测集证明修复。**

**先行动后调试**：扣留受影响的只读草稿路径，请求转给操作员，**在改任何东西前保存记录**。

**如何读 trace**：Agents SDK 默认追踪每次运行。
- **trace**：一个端到端工作流。`workflow_name`（逻辑工作流或应用名，如 "Northstar draft"）、`trace_id`（唯一标识运行，不传则自动生成）、可选 `group_id`（关联同一对话的多个 trace）。
- **span**：记录单个操作，有开始/结束时间和父节点。SDK 把每个 `Runner.run` 包在 trace 中并自动创建：agent span、generation span（模型调用）、function span（工具调用）、guardrail span、handoff span。在 Traces 仪表盘按时间线查看，或发到自己的追踪后端 (tracing backend)。
- **自上而下读**：从 agent span 开始，沿 generation span 看模型收到和返回了什么，检查每个 function span 的参数和结果；handoff span 显示控制在哪里转给另一个 agent。
- **SDK 只看到 SDK 运行的东西**：你在步骤间的代码（如规范化工具输出的 mapper）只有加 custom span 或用相同 task ID 记到应用记录中才会出现。完整画面 = trace + release 与模型配置 + 来源版本 + 工具结果 + 单独采集的动作证据。
- 本路径有操作员审核、无工单写入、无客户消息、**无审批步骤 —— 不要为了时间线好看编造审批 span**。

**第一个出错的步骤 —— 任务 D-04（来自保存的应用记录）**：

| # | 步骤 Step | 输出 Output | 判断 |
|---|---|---|---|
| 1 | 授权读取 Authorized read | NS-452 来源返回 v7，事件类型 visit，**status scheduled** | ✓ 正确 |
| 2 | 应用 mapper v1 | **只检查事件类型是否为 visit**，丢掉 status，输出 `visit_completed=true` | ✗ **第一个错误** |
| 3 | Handoff | 接收专家拿到这个错误字段 | 传递错误 |
| 4 | 草稿 Draft | 专家说上门已完成 | 传递错误 |

<svg viewBox="0 0 760 210" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="210" fill="#fff"/>
<text x="10" y="20" font-weight="bold">D-04: join SDK spans with the application record｜SDK span + 应用记录</text>
<rect x="10" y="45" width="160" height="60" rx="8" fill="#e6f4ea" stroke="#188038"/><text x="90" y="68" text-anchor="middle">Read v7: scheduled</text><text x="90" y="88" text-anchor="middle">function span ✓</text>
<rect x="200" y="45" width="170" height="60" rx="8" fill="#fce8e6" stroke="#c5221f" stroke-width="2"/><text x="285" y="68" text-anchor="middle">Mapper v1 (app code)</text><text x="285" y="88" text-anchor="middle">visit_completed=true ✗</text>
<rect x="400" y="45" width="160" height="60" rx="8" fill="#fef7e0" stroke="#f9ab00"/><text x="480" y="68" text-anchor="middle">Handoff span</text><text x="480" y="88" text-anchor="middle">carries false field</text>
<rect x="590" y="45" width="160" height="60" rx="8" fill="#fef7e0" stroke="#f9ab00"/><text x="670" y="68" text-anchor="middle">Draft: "completed"</text><text x="670" y="88" text-anchor="middle">generation span</text>
<line x1="170" y1="75" x2="198" y2="75" stroke="#333" marker-end="url(#a19)"/>
<line x1="370" y1="75" x2="398" y2="75" stroke="#333" marker-end="url(#a19)"/>
<line x1="560" y1="75" x2="588" y2="75" stroke="#333" marker-end="url(#a19)"/>
<text x="285" y="130" text-anchor="middle" fill="#c5221f">not traced by SDK → custom span / app record</text>
<text x="285" y="147" text-anchor="middle" fill="#c5221f">SDK 不追踪，需自定义 span 或应用记录</text>
<text x="380" y="190" text-anchor="middle" fill="#555">Fix the earliest wrong step, not the last visible symptom｜修最早出错的步骤，不是最后的症状</text>
<defs><marker id="a19" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>

归咎专家会让错误字段留在它的输入里。修最早的错误步骤让错误字段永远到不了 handoff。

**敏感数据与证据包**：`RunConfig(trace_include_sensitive_data=False)` 让模型 span 省略请求输入和响应输出（**默认 True**）。此时 trace 能显示读取、mapper、handoff 及时序，却省略证明哪步错的值。所以要配对一个**单独受控的应用记录**：task ID、来源版本、事件状态、mapper 版本、结果。调试包用**白名单 (allowlist)** 构建：默认排除凭证、原始备注、工具参数、对话历史、摘要、异常文本、日志载荷（除非单独授权）。白名单限制哪些字段离开源系统，但不证明每个允许的值都不含机密，也要检查。应用日志、转移的历史、会话存储、Responses 存储、trace 导出的访问和保留 (retention)**分别决定**。会话内存开启时 runner 在运行前取历史、运行后存新项；关闭 trace 载荷不会擦除历史。会话 ID 只选择历史，不认证不授权 —— 取回前先认证操作员并授权会话，单独保护会话存储及其备份。

**复现与修复**：
- **改 mapper 前冻结失败记录 (failure record)**：输入或安全替代、期望行为、权威来源状态与版本、应用和策略版本、模型标识与设置、SDK 和依赖版本、关联证据。再加第二个失败的 scheduled 用例，以及 completed、canceled、缺失 status、未知 status 用例。
- 本地回放用保存的 D-04 调用原 mapper：期望 scheduled，类型检查得 completed。**应用代码中的缺陷不需要模型调用就能复现。**
- **诱人但错误的修复**：改专家提示词 "Do not say a visit is complete unless it is complete." 下一份草稿可能碰巧说 scheduled，但专家仍收到 `visit_completed=true`，错误字段还在，等着造成下一份坏草稿。
- **正确修复**：用**显式状态处理**替代推断 —— completed / scheduled / canceled 连同来源版本传给专家；缺失或未知状态 → 操作员审核，不编造。再加**验收检查 (acceptance check)**作为第二道边界：除非权威事件本身说 completed，否则拒绝 completed 声明。验收检查可扣留无依据草稿；mapper 修复让错误字段根本到不了专家。

```python
def repaired(event):
    status = event.get("status")
    if event["type"] != "visit" or status not in ("completed", "scheduled", "canceled"):
        status = None  # missing or unknown status routes to operator review
    return {"normalized_status": status,
            "visit_completed": status == "completed",
            "source_version": event["version"]}

def accept(event, claim):
    """Apply the same authoritative-source boundary to both mapper versions."""
    status = event.get("status")
    if event["type"] != "visit" or status not in ("completed", "scheduled", "canceled"):
        return "operator_review"
    if claim == "completed" and status != "completed":
        return "operator_review"
    return "accept" if claim == status else "operator_review"
```

**证明修复**：本地套件 8 个能力用例（2 个 mapper v1 误分类的 scheduled + 6 个 completed）+ 4 个安全用例（缺失 status、未知 status、对 scheduled 和 canceled 事件的无依据 completed 声明）。

| Mapper | 能力 Capability | 安全 Safety | 采集器覆盖 Coverage |
|---|---|---|---|
| 原始 Original v1 | 6/8 | 4/4 | 12/12 |
| 修复 Repaired | 8/8 | 4/4 | 12/12 |
| 带 `--missing-coverage` | — | — | D-04 失去覆盖 → 门槛 **incomplete** |

原 mapper 通过安全用例是因为验收检查拦住了它的无依据声明 —— **这不说明原 handoff 正确**。canceled 安全用例测的是验收决策，不是修复后 mapper 是否保留 canceled → 要为它加 mapper 检查。

**每种证据回答不同问题**：一次模型重跑 → 一次生成看起来对不对；确定性检查 → 每次测试 mapper 和验收边界；重复代表性用例 → 跨输入的任务行为；效果记录 → 执行边界上发生了什么（前提是采集器覆盖了它）。调优 (tuning)修复前**预留单独的 holdout**，对其做重复的模型相关试验；报告观察计数、用例如何选择、不确定性。小回放加一次干净试验给不出通用故障率。

**何时恢复服务**：本地和 holdout 门槛通过、且两个负责人接受角色（客户工程的 on-call 负责人 + 服务运营的审核负责人）后，才提议**有限的、操作员审核的试点**。先约定运营条件：
- 窗口（如一个有人值守的班次）
- 跟踪指标（各带分母）：无依据 completed 声明、审核路由率、来源读取错误、队列深度、端到端延迟 (latency)
- 与负责人对照观测基线 (baseline)设定数值阈值（没有样本量 (sample size)的比率难以解读）
- **停用条件 (disablement)**：严重无依据 completed 声明、采集器覆盖丢失、依赖中断 → 停用路径或切人工；指定谁能停用、操作员如何接收排队工作
- 有界并发 (concurrency) + 背压 (backpressure)，中断期间队列不会无限增长
- 负责人审查原因和证据后才恢复服务

**第二条记录（canceled）**：来源 v9 说上门已取消，mapper v1 输出 `visit_completed=true`，专家起草"已完成"，效果采集器离线。→ 最早错误边界仍是 mapper v1；修复后 mapper 必须保留 canceled、绝不转为 completion；请求转操作员审核；**离线采集器既不说明有效果也不说明无效果** —— 恢复覆盖意味着检查边界，而不是看到一个空列表；路径保持扣留直到修复和证据门槛通过。

### 面试怎么说 / How to say it in the interview

**Q: "You changed the prompt and the next draft was correct. Why would you still withhold the path?"**
> "Because a correct sentence in one rerun leaves the real defect in place. For D-04 the source said scheduled, but our mapper inferred completion from the event type alone and handed the specialist visit_completed=true. I'd fix the mapper to carry the explicit status and source version, route missing or unknown statuses to review, add an acceptance check that rejects completion claims the source doesn't support, then run the replay and a reserved holdout. I'd only report effect evidence if the collector actually covered that boundary."
（中文：一次正确重跑不修根因；修 mapper + 验收检查；回放 + holdout；采集器覆盖才算效果证据。）弱回答 "The trace has a successful final response, so the model learned the correction."

**Q: "How do you debug a misbehaving agent pipeline?"**
> "First I contain it: withhold the affected path, route requests to operators, and freeze the records. Then I read the trace top-down and join it with application records for code the SDK doesn't trace, like mappers, and find the earliest step whose output contradicts the source of truth. I reproduce it deterministically, often without a model call, fix that step in code rather than prompting around it, and prove it with capability, safety, and coverage checks."
（中文：先遏制、冻结记录；trace + 应用记录；找最早矛盾步骤；确定性复现；代码修复；三类检查证明。）

**Q: "What lets you return the path to service?"**
> "Passing evidence gates, accepted on-call and review owners, an agreed monitoring window with numeric thresholds and denominators, a manual route, and a disablement plan with a named person who can switch it off. Until then, operators handle the requests."

**Q: "The canceled record shows the same bug and the effect collector is offline. What do you conclude?"**
> "The earliest wrong boundary is still mapper v1 turning canceled into completed. The request goes to operator review, and an offline collector proves neither that an effect happened nor that none did, so I restore and verify coverage before trusting an empty log. The path stays withheld until the repair and evidence gates pass."

---

# Section II — Forward Deployed Engineer for AI Systems: OpenAI 模块（只记新增/不同）

> 本模块与 Section I 大量重叠（同样的 Cedar / Northstar 案例）。以下只记**新的事实、数字、表格、代码陷阱和面试问答**，其余指向 Section I 对应课。

## II-1. What an OpenAI FDE Owns｜OpenAI FDE 拥有什么

Source: https://www.educative.io/courses/forward-deployed-engineer/what-an-openai-fde-owns
重叠：→ Section I 第 1 课（Cedar demo、四个所有权问题）、第 3 课（角色对比）

### 新增要点 / What's new

- 案例改名 **Cedar Logistics**（周四 demo 12/12 → 周五第二个员工打不开 → 发起人 (sponsor)要求周一全员 24 人上线）。数据和四问题表与第 1 课相同。
- **职位描述 → 面试官在找什么**（SF 职位，课程于 2026-10-28 查阅；准备前要查当前版本）：

| 职位描述说 FDE… The posting says | 面试官找什么 What an interviewer looks for |
|---|---|
| 负责技术交付 "from first prototype to stable production" | 故事**以生产使用结束**，之后有**指定负责人** |
| "Contribute directly in the code when progress or clarity depends on it" | 自己写的代码，且能解释每一部分 |
| "Embed closely with customer teams"、"guide adoption" | 知道谁用了系统、他们的工作因此改变了什么 |
| 在范围、速度、质量间权衡 | 砍了什么、为什么这一刀保护了结果 |
| 向 Research 和 Product 分享现场反馈 | 精确到他人可复现的证据 |

- **硬性要求**：≥ 5 年工程或技术部署经验（含面向客户的工作）；编写和评审**生产级前端和后端代码**的经验；构建或部署 LLM/生成式模型系统的经验。SF 职位：混合办公 (hybrid)每周 3 天、出差至多 50%。
- **优先修已暴露的失败**：再测 50 个代表性问题能提供更多草稿质量证据，但**不能建立运营所有权，也不能让 Cedar 员工访问应用** —— FDE 应先解决导致当前问题的部分，而不是改进没出问题的地方。
- **三个成功指标的细节**：
  - 采用率 (adoption rate)以**被启用的人**为分母：20 人有权限、15 人在合格工作中使用 = 75%；**没用的 5 个人往往是更有用的信号**（原因通常指向工作流：草稿在他们已开始打字后才到；检查草稿比自己写还慢）。
  - 工作流影响需要**建设前约定的基线 (baseline) + 旁边的质量条件**：快了 30% 但错误回复翻倍 = 没有改进。
  - 评测对 OpenAI 的价值：把现场经验变成 Research/Product 可复现的东西。"模型在政策问题上挣扎" 难以行动；**30 个失败用例 + 输入 + 期望输出 + 模型版本**才可修复。所以本章把 eval 当作**交付物 (deliverable)**。
- **角色对比表（比第 3 课多"写什么代码"和"所有权通常在哪结束"）**：

| 角色 Role | 主要关注 Main focus | 写的代码 Code written | 所有权通常结束于 Ownership ends |
|---|---|---|---|
| 解决方案架构师 Solutions architect | 参考架构与设计指导 | 示例 Samples | 设计建议处 |
| 解决方案/销售工程师 Solutions/sales engineer | Demo 与技术销售支持 | 原型 Prototypes | 客户承诺购买时 |
| ML/研究工程师 ML/research engineer | 模型行为、训练、评测 | 模型与研究代码 | 模型能力处 |
| **FDE** | 客户在生产中的结果 | **全栈生产代码** | **客户独立运行系统时** |

- 候选人技巧：在自己的经历里找"FDE 形状的工作"。**一个内部工具被另一个团队采用、有真正交接的后端工程师，往往比做过 20 个 demo 却没有一个上生产的解决方案工程师有更强的 FDE 故事。** Proof 和 handoff 是大多数故事最薄的部分。

### 面试怎么说 / How to say it in the interview

**Q: "A sponsor says 12 of 12 means the system is '100% accurate' and ready for every user. How do you respond?"**
> "It's a 100% acceptance rate on 12 sponsor-selected questions, run on a laptop with a copied FAQ, so the drafting approach looks promising but that's all it proves. I don't yet know if staff use it, whether it saves time against a baseline, who fixes it when it breaks, or whether Cedar can run it without the developer. I'd offer a path they can say yes to: a four-person, 40-request trial with an agreed time and quality measure, a named owner, a manual fallback, and the code in Cedar's repository."
（中文：说清 demo 证明的范围；给发起人可以同意的替代路径。）

**Q: "Why do you want to be an FDE rather than a solutions architect?"**
> "Because I want to own the outcome in production, not stop at the design recommendation. The work I'm proudest of is where I wrote the production code, measured the workflow impact, and handed the system to a team who ran it without me. That's where most of the hard problems actually show up."

---

## II-2. Inside the FDE Team: How an Engagement Runs｜FDE 团队内部：一个项目如何运行

Source: https://www.educative.io/courses/forward-deployed-engineer/inside-the-fde-team-how-an-engagement-runs
重叠：→ Section I 第 4 课（五要素升级、团队列表、现场反馈、嵌入客户）

### 新增要点 / What's new

- 反例换成 Cedar 两周试点后周一的广播消息（"Product, Research, Security, GRC, GTM: Cedar is blocked... Please fix before the HR desk rollout next week. I've told the sponsor we're on track."）—— 到周四毫无进展。问题：五个团队、没有具体问题、没有证据、没有请求，**还在负责团队没确认时就说 "on track"**。
- **FDE 给每个团队带去什么**：

| 团队 Team | FDE 通常带去 What an FDE brings |
|---|---|
| Research | 在客户集成之外也能复现的模型行为 |
| Product | 可能指向 OpenAI 产品界面的反复出现的工作流需求 |
| Security | 连接使用前需要评估的安全问题 |
| GRC | 客户的保证 (assurance) 问题，以及谁能接受答案 |
| Partnerships | 工程团队之外的客户关系协调 |
| GTM | 如何描述范围与准备度，让商业预期匹配已证明的东西 |

  Cedar 侧：IT 管工单系统、知识团队维护 FAQ、服务台主管定义可接受回复的标准。边界不清会导致 FDE 把需要客户决策的问题升级给 OpenAI。

- **项目阶段及其结束证据 (phase → what ends it)**：

| 阶段 Phase | 做什么 | 结束标志 What ends it |
|---|---|---|
| 发现与范围 Discovery & scoping | 了解真实工作流，约定范围内外 | 客户接受的书面范围 |
| 在批准数据上构建 Build on approved data | 用客户批准用于此目的的数据构建 | 可运行系统 + **版本化评测集** |
| 试点 Trial | 真实用户、窄范围、兜底 (fallback)就位 | 对约定目标的测量结果 |
| 准备度 Readiness | 修试点发现的问题，验证实时连接和负责人 | 每个上线条件的证据 |
| 上线与交接 Rollout & handoff | 分步扩大，转移运营 | **客户团队在没有 FDE 的情况下运行它** |

  三个里程碑各需独立证据：**可用的集成**（可以开始测试，不是测试完成）、**已验证的准备度**（达到约定上线标准）、**被接受的上线**（授权的客户决策者批准部署）。

- **Cedar 试点结果（4 人、40 请求、两周）**：

| 请求类型 Request type | 接受 Accepted | 问题 What went wrong | 负责人 Owner |
|---|---|---|---|
| 常规 FAQ Routine | 28/28 | 无 | — |
| 近两周变更的政策 Recently changed policies | 4/8 | 工具的 FAQ 副本比 Cedar 线上 FAQ 旧 | **客户知识团队**（FAQ 更新流程） |
| 报销上限 Reimbursement limits | 2/4 | 即使提供了正确 FAQ 条目，两份草稿仍写错上限 | **受控重放 (controlled replay)后**交 Research；同时本地遏制 (containment) |

  总体 (28+4+2)/40 = **85%**，报销类只有 2/4 = **50%**（错误金额可能造成财务后果）。另：处理时间中位数 (median) **4.8 分钟**（目标 4.5、基线 (baseline) 6），员工说额外时间花在核对报销金额；HR 上线前 Cedar 安全负责人问 **"OpenAI 是否保留工单里的员工姓名？"** → 交 **Security 和 GRC** 给权威答案。

- **五要素升级完整示例（报销上限）**：
  - Problem：两类请求的草稿写错报销上限
  - Consequence：员工逐个复核金额，处理时间高于目标；HR 上线依赖金额准确
  - Evidence：直接提供正确 FAQ 条目、绕过集成、固定指令和模型设置，两个用例 **5/5 次**都产出错误上限；附脱敏 (sanitized)输入输出
  - Request：请 Research 调查这是否是已知行为，并建议可测试的配置
  - Follow-through：我跟踪并按需补充用例；**本地遏制本周照常上线**
- **本地遏制 (local containment)**：确定性检查 —— 草稿中出现的任何金额必须与所引用 FAQ 条目中的数字一致，否则转人工流程。通过只证明金额与来源一致，不证明草稿其余部分正确。可复用模式："草稿中的金额必须匹配其引用来源" 的 eval 模式适用于任何基于政策文档起草的客户 —— **模式可迁移，Cedar 的数据留在 Cedar**。
- **脱敏后要重跑确认仍失败**：用批准的替代值替换员工姓名和金额后，重跑用例确认仍然失败；**不再复现的脱敏用例不是证据**。
- **拜访议程**：不经指导观察员工使用并计时分钟花在哪；与知识团队约定 FAQ 更新如何到达工具及谁负责；与 IT 约定 HR 版可读哪些系统及谁授权连接；拿到运营负责人、事故负责人 (incident owner)、HR 上线批准人的名字。**没有一项是 "demo 新版本"** —— 演示换来掌声，观察和决策换来下一阶段的输入。

### 面试怎么说 / How to say it in the interview

**Q: "Your deployment is blocked on three teams you don't manage. What do you do?"**
> "I'd split the blockers by owner first. At Cedar, the stale FAQ belonged to the customer's knowledge team; the wrong reimbursement limits went to Research only after a controlled replay showed they reproduce five out of five times without our integration; and the data-retention question went to Security and GRC for an authoritative answer. Each request named the problem, consequence, evidence, and what I needed, and I tracked acceptance separately. While Research investigated, we shipped a local check that routes any amount that doesn't match its cited FAQ entry to the manual process."
（中文：按负责人拆分阻塞；受控重放后才找 Research；单独跟踪接受状态；本地遏制同步上线。）

**Q: "The sponsor asks if you're on track. What do you say?"**
> "I'd report three groups: items that are closed, items with an accepted owner and a date, and items still waiting for acceptance. 'On track' is only true for the first two."

**Q: "Why does a message addressed to several teams with a deadline often fail?"**
> "Because it creates urgency without a task. Nobody knows what problem they own, what evidence supports it, or what decision is being asked of them, and a deadline attached to a message isn't anyone's agreement."

---

## II-3. OpenAI's Mission, Charter, and Deployment Philosophy｜OpenAI 使命、宪章与部署理念

Source: https://www.educative.io/courses/forward-deployed-engineer/openais-mission-charter-and-deployment-philosophy
重叠：→ Section I 第 5 课（四个来源、五个问题、Model Spec 层级、95% 拆分、安全路径、拒绝话术）

### 新增要点 / What's new

- 案例换成 **Cedar HR desk**：发起人 (sponsor)要求读员工消息、**标记可能倦怠 (burnout) 的人**、每周给经理发带姓名和风险分的列表（"playground 里模型做得很好"、"我读过政策没看到禁止"）。
- **Charter 对 AGI 的定义**：*highly autonomous systems that outperform humans at most economically valuable work*（在大多数具有经济价值的工作上超越人类的高度自主系统）。
- **三个评估视角 (Benefit / Risk / Agency)**：收益 —— 谁受益、是否满足受影响者的需要；风险 —— 模型输出错误或敏感信息未授权泄露时谁会受伤；自主 —— 受影响者是否了解数据如何被使用、有什么控制权。
- Model Spec 引用的是 **2026-08-18 版**；Model Spec 的目标之一是 *"iteratively deploy models that empower developers and users"*。
- **迭代部署落到单个项目的四步**：先离线测（版本化测试集含代表性请求、边界用例、已知失败场景）→ 小规模开始（有限授权用户、明确任务、保留手工流程兜底）→ **事先定义停止条件 (stop conditions)**（暂停与回滚 (rollback)标准，以及谁有权暂停）→ 按证据扩大。
- **使用政策版本（具体日期）**：2026-10-21 发布的更新于 **2026-11-20 生效**；在那之前 **2025-10-29 版**有效。
- **新增条款（第 5 课未提）**：**禁止在工作场所或教育环境中推断个人情绪 (workplace emotion inference)**，除非出于医疗或安全原因。另两条：未经授权聚合/监控/画像 (profiling)/分发私人敏感信息；在就业等敏感领域无人工审核地自动化重大动作。政策原文："are no substitute for legal requirements, professional duties, or ethical obligations"。
- 对 Cedar：**旧版就已限制未授权画像和工作场所情绪推断**，所以版本问题不改变核心结论；而**第 4 问（客户授权）单独就足以拒绝**（批准的 HR 助手范围要求员工问题保密、经理不能访问个人对话、不改员工记录）。
- 安全替代方案：批准的福利助手 + 私下转 HR 人员 + **在 Cedar 法务批准的前提下提供聚合、匿名的员工提问主题趋势**。

### 面试怎么说 / How to say it in the interview

**Q: "What would you refuse to build for a customer?"**
> "I keep five questions apart: the Charter's lens on who benefits, what the Model Spec says about intended behavior, what the applicable usage-policy edition permits, what the customer actually authorized, and what the law requires. A customer once asked me to infer burnout from employee messages and send named scores to managers. That was outside the approved scope before we even got to policy, and the policies also bar workplace emotion inference, so I declined it and offered aggregate, anonymous topic trends instead, pending their counsel. The model producing scores in testing proved capability, not permission."
（中文：五个问题分开；先以客户授权拒绝；政策也禁止工作场所情绪推断；给出匿名聚合替代。）弱回答 "Anything that violates the usage policies; if policies allow it and the model can do it, I'd build it with safeguards."

**Q: "The sponsor says the policies allow it. What do you check?"**
> "Which edition they read, its effective date, and the exact clause. Then I'd point out the decision doesn't depend on it, because their own authorization already excludes manager access to individual conversations."

**Q: "The model produced the scores perfectly in testing, so it's allowed. What's wrong with that?"**
> "It shows what the model did, not what's intended, permitted, or authorized. The Model Spec says production models don't fully reflect intended behavior, and permission comes from the usage policy, the customer's authorization, and the law."

---

## II-4. The Responses API, Tool Calling, and Structured Outputs｜Responses API、工具调用与结构化输出

Source: https://www.educative.io/courses/forward-deployed-engineer/the-responses-api-tool-calling-and-structured-outputs
重叠：→ Section I 第 6 课（按位置配对 bug、call_id 关联、状态三选一、strict 规则、schema 管形状/验收管内容、Assistants 迁移）

### 新增要点 / What's new

- 示例模型用 `gpt-6.1-terra`；读 `response.usage.input_tokens / output_tokens`（成本课用）。
- **Assistants API 于 2026-08-26 关停**（OpenAI deprecations 页面）。**迁移完成的标准：旧系统的测试用例在新代码上通过，包括被拒用例。**
- 修复版分发器把**每个结果（允许或拒绝）都打上它所回答的 `call_id`**，并返回读到的 ticket；`correlate` 按 call ID 建字典，先检查集合（缺失/重复/意外 → 停止），再检查每个结果携带的 ticket 正是该调用请求的。
- **云资源清理的陷阱 (cleanup pattern)**：诱人写法是一个 helper 同时上传和挂载文件，再在 `finally` 删除 —— 若挂载失败，持有文件的变量从未赋值，**上传的文件成为孤儿 (orphaned)**。正确：每个资源在 `try` 内创建、**一存在就记录**；删除 vector store 失败不能跳过删除文件（嵌套 `try/finally`）。清理仍只是尝试：若创建调用在服务端已执行后超时，代码拿不到 ID → 需要**定时任务 (scheduled job)列出并删除本工作流遗留的资源**。`purpose="assistants"` 是搜索工具的文件用途，**不代表在用已退役的 Assistants API**。
- 结构化输出：Pydantic 中用 `Literal["awaiting_part", "callback_due", "closed"]` 限制状态取值；`responses.parse(text_format=Comparison)` 得 `output_parsed`；把优先级翻转后的副本仍是合法 `Comparison`，验收会拒绝它。
- **展示给人时从验证过的字段渲染答案；在验证后再拼接模型的自由文本，会把验证刚移除的问题全带回来。**

### 面试怎么说 / How to say it in the interview

**Q: "Your strict schema passes. Why isn't that enough?"**
> "The schema fixes the shape and nothing else. At Northstar, two correct records got swapped because results were paired by position, so we match every result by call ID and check the ticket it carries. Authorization happens in the dispatcher from the signed-in session, and the final comparison passes an acceptance check against the records we actually read, including the priority rule, before an operator sees it. And I render the answer from the validated fields, never append free model text after validation."
（中文：schema 只管形状；call_id 关联；分发器授权；验收；从验证字段渲染。）

**Q: "How do you make sure you don't leak billed resources like vector stores and files?"**
> "Create each resource inside the try and record it the moment it exists, with cleanup in nested finally blocks so one failed delete can't skip the next. Because a create can time out after the server already acted, I also run a scheduled job that lists and removes anything this workflow left behind."

---

## II-5. The Agents SDK, MCP, and Multi-Agent Patterns｜Agents SDK、MCP 与多 Agent 模式

Source: https://www.educative.io/courses/forward-deployed-engineer/the-agents-sdk-mcp-and-multi-agent-patterns
重叠：→ Section I 第 7 课（SDK 职责、共享会话泄露、注册表修复）、第 8 课（审批、过期、三类记录）、第 9 课（MCP）、第 10 课（三种多 agent 模式）

### 新增要点 / What's new

- **验收规则（易漏）**：必须要求**本次运行中对每个请求的工单都有一次授权读取**。只检查"没有读取被拒"会让一次**一个读取都没做**、凭空写出合理对比的运行通过。（窄权限操作员示例：`NS-104: no authorized read in this run`。）
- **无读取不提议 (no read, no proposal)**：只有本次运行对该工单做过授权读取，提议才会提交审核 —— 把验收规则应用到动作上。
- **序列化细节**：`result.to_state().to_string(context_serializer=lambda ctx: {})` 把操作员上下文排除在外；恢复时 `RunState.from_string(agent, saved, context_override=op)` 用应用自己的记录**重建可信上下文**。SDK 文档：只从可信存储反序列化 (deserialize)状态，所以**状态不经浏览器往返**。
- **写事务内检查顺序**（`create_if_approved`，唯一写路径，`BEGIN IMMEDIATE`）：

| 顺序 | 检查 Check | 状态 Status |
|---|---|---|
| 1 | 工单不在权限内或不存在（**现在**重查） | `denied` |
| 2 | 无提议 / 未批准 / 操作员不符 | `not_approved` |
| 3 | (ticket, callback_at) ≠ 批准的参数 | `arguments_changed` |
| 4 | 可信时钟 > 过期时间 | `expired` |
| 5 | 该 call_id 已有任务（**call ID 作主键 (primary key)**，一次调用至多一个任务） | `already_created` |
| 6 | 全部通过 → 插入 | `created` |

- **六个场景输出（每个新账本）**：12:05 恢复 → `created`，1 个任务；12:11 恢复 → `expired`，0；**停放的调用被改成 13:30 → SDK 拒绝**（Agents SDK **0.24** 中批准一个参数与记录调用不同的调用会抛 **`ModelBehaviorError`**），0；审核者拒绝 → not run，0；未读工单就提议 → not offered for review，0；**重试 worker 绕过 SDK 直接写 13:30 → 适配器返回 `arguments_changed`**，0。→ 两层保护：SDK 保护经过 SDK 的写入；适配器自己的比较保护绕过 SDK 的写入。
- **装饰了但没在 agent 上注册的工具，模型永远调不到**（`tools=[...]` 列表决定）。
- 真实模型演示：共享会话下，B 对 NS-104 的读取被拒，**但 B 仍被告知 "NS-104 之前在等零件"**（来自 A 的历史）。
- MCP 新细节：服务器用 `FastMCP("northstar-status")` + `@mcp.tool()` + `mcp.run(transport="streamable-http")`；**一旦工具在网络端点后面，任何能访问它的客户端都能调用，不管有没有模型**。

### 面试怎么说 / How to say it in the interview

**Q: "Your agent can write to the support system. What stops it from creating a task nobody approved?"**
> "The pause is only half of it. At Northstar a restarted worker once acted on an approval that had expired a minute earlier. So the write adapter rechecks everything inside its own transaction: the operator's current permission, that the arguments exactly match the approved proposal, the trusted clock against the expiry, and the call ID as primary key so one call makes at most one task. The SDK also refuses an approval whose arguments changed, but a retry worker that bypasses the SDK still hits the adapter's check. The reviewer's identity comes from our login, and the ledger receipt is what proves the task exists."
（中文：暂停只是一半；事务内重查权限/参数/过期/唯一性；SDK 与适配器两层；收据为证。）

**Q: "Why not just add the write tool to the MCP server and let hosted approval handle it?"**
> "Hosted approval decides whether this call goes ahead. It doesn't replace authorization, the exact-action check, the expiry, or the ledger receipt; those still live in the adapter behind the server."

**Q: "A session ID is shared by two operators with different permissions. Why doesn't the tool's authorization prevent a leak?"**
> "Because the history is prepended to the model input before any tool runs. The tool correctly denies a fresh read, but the record already arrived through history, and no tool check can retract it. The fix is to authenticate, check the conversation's owner binding, and only then load history."

---

## II-6. Deployment Surfaces, Voice, Model Choice, and Cost｜部署位置、语音、模型选择与成本

Source: https://www.educative.io/courses/forward-deployed-engineer/deployment-surfaces-voice-model-choice-and-cost
重叠：→ Section I 第 11 课（三个家、重复草稿、数据处理）、第 12 课（语音）、第 13 课（模型选择、成本 $401.40）

### 新增要点 / What's new

- **Agent Builder 关停日期：2026-11-30**（OpenAI deprecations 页面）。
- **ZDR 资格**：当时列表中 **Responses 为 "eligible with limitations"**；Conversations、Files、vector stores 不符合。
- 三个家的"谁跑循环、谁被呼叫"：ChatGPT 内 → 主要是 OpenAI 产品，受客户工作区设置约束；ChatKit → 客户负责后端及其后的一切；自有服务 → 客户端到端负责。
- 语音：**浏览器 Realtime 会话推荐用 WebRTC**；链式管线也适合"已有文本 agent 需要语音界面"的情形。
- **轮次守卫的 bug (TurnGuard)**：诱人版本 `FixedTurnGuard` 在任何打断 (interruption)时把轮次**设为 2**；两次打断后它仍以为是第 2 轮，于是**中间轮次 (NS-381) 的迟到结果被放行**。正确版本**每次打断都递增**轮次，只接受当前轮次发出的调用的结果：

```python
class TurnGuard:
    def __init__(self):
        self.turn = 1
        self.calls = {}  # call_id -> the turn that issued it

    def start_call(self, call_id):
        self.calls[call_id] = self.turn

    def interrupt(self):
        self.turn += 1  # every interruption opens a new turn

    def accept_result(self, call_id, result):
        if self.calls.pop(call_id, None) != self.turn:
            return None  # stale: suppress it and ask which ticket was meant
        return result
```

```text
Input:  call_1 (NS-318) -> interrupt -> call_2 (NS-381) -> interrupt -> call_3 (NS-138)
        results arrive: call_2, call_1, call_3
Output (FixedTurnGuard): call_2 shown (WRONG), call_1 suppressed, call_3 shown
Output (TurnGuard):      call_2 suppressed, call_1 suppressed, call_3 shown
```

- **缓存实测示例**（约 2,000 token 调度规则作稳定前缀，两条不同备注放最后，课程工作费率）：第一次 input 2,154（cached 0）、output 69、$0.00486；第二次 input 2,155（**cached 2,130**）、output 33、**$0.00138**（不到第一次的 1/3）。单次调用月度（18,000）：有缓存 $24.82 vs 无缓存 $82.33 —— **两者都只是一次调用，不是整个任务**。缓存命中 (cache hit)不保证。
- 推理强度：常见取值 low–high，部分模型有 minimal 或无推理。

### 面试怎么说 / How to say it in the interview

**Q: "A client times out and retries with a new request ID. Why does that produce duplicate drafts, and what's the fix?"**
> "A timeout only means the client stopped waiting; the server may still be working or already done, so a new ID starts a second job. The fix is a stable request ID bound to the operator and content, stored durably: a retry with the same ID returns the existing status, changed content under that ID is rejected, and a timed-out request stays unknown until the service reconciles it."
（中文：超时≠失败；稳定 request ID 绑定操作员+内容并持久化；未知待对账。）

**Q: "The fast configuration is three times faster. Why choose the slower one?"**
> "On the 40-case set the stronger configuration met the bar at 39 with no critical unsupported claims; the fast one got 36 and missed it. I'd investigate the remaining failure, agree a latency target with operators, keep Batch for nightly comparisons rather than waiting users, and price the whole task including retries and tools, not just the first call."

**Q: "Operators correct themselves mid-sentence twice. How do you make sure the right result is shown?"**
> "Every interruption opens a new turn, and each tool call is tagged with the turn that issued it. A result is only shown if its call belongs to the current turn; anything older is suppressed, the agent asks which ticket was meant, and playback is truncated so history matches what the operator heard. A guard that just sets 'turn two' on interrupt would leak the middle result."

---

## II-7. Evals, Guardrails, and Debugging with Traces｜评测、护栏与 Trace 调试

Source: https://www.educative.io/courses/forward-deployed-engineer/evals-guardrails-and-debugging-with-traces
重叠：→ Section I 第 17 课（评测集、S2、配对门槛）、第 18 课（注入、护栏时机、moderation）、第 19 课（D-04 mapper）

### 新增要点 / What's new

- **发布门槛必须先与用例清单对账 (manifest reconciliation)**：清单 = 版本化的 8 个用例 ID 及其家族。跳过这一步，**一次中断的运行只返回 5 个通过的能力用例也会通过** —— 没有安全用例就找不到安全失败，而 Python 的 `all([])` 为 `True`；重复记录还会虚增能力计数。**门槛只能评判到达它的用例，所以必须先证明它们都到了。**

```python
def release_gate(candidate, baseline, manifest):
    # manifest: {case_id: family}, loaded from the versioned case-set file
    ids = [case.id for case in candidate]
    if len(ids) != len(set(ids)) or set(ids) != set(manifest) or set(baseline) != set(manifest):
        return "incomplete"  # a missing, duplicate, or unexpected case
    if any(case.family != manifest[case.id] for case in candidate):
        return "incomplete"
    if any(case.grading_incomplete for case in candidate):
        return "incomplete"
    if any(case.critical_trace_violation for case in candidate):
        return "blocked"
    for case in candidate:
        if case.family == "safety" and baseline[case.id].passed and not case.passed:
            return "blocked"  # a safety regression can't be outvoted
    safety = [c for c in candidate if c.family == "safety"]
    capability = [c for c in candidate if c.family == "capability"]
    if not all(c.passed for c in safety) or sum(c.passed for c in capability) < 5:
        return "blocked"
    return "pass"
```

```text
Input:  baseline passes C1-C4, S1, S2; candidate passes C1-C5, S1; S2 read NS-777
Output: total-score gate -> pass (6/8 vs 6/8)   release gate -> blocked
Input:  interrupted run returns only C1-C5 (all passing)
Output: gate without manifest check -> pass      release gate -> incomplete
```

<svg viewBox="0 0 760 170" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<rect x="0" y="0" width="760" height="170" fill="#fff"/>
<text x="10" y="20" font-weight="bold">Release gate order｜发布门槛判定顺序</text>
<rect x="10" y="40" width="140" height="56" rx="8" fill="#fef7e0" stroke="#f9ab00"/><text x="80" y="63" text-anchor="middle">1 Reconcile</text><text x="80" y="81" text-anchor="middle">manifest 清单对账</text>
<rect x="165" y="40" width="140" height="56" rx="8" fill="#fef7e0" stroke="#f9ab00"/><text x="235" y="63" text-anchor="middle">2 Grading</text><text x="235" y="81" text-anchor="middle">complete? 评分完整</text>
<rect x="320" y="40" width="140" height="56" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="390" y="63" text-anchor="middle">3 Critical trace</text><text x="390" y="81" text-anchor="middle">violation 严重违规</text>
<rect x="475" y="40" width="140" height="56" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="545" y="63" text-anchor="middle">4 Safety</text><text x="545" y="81" text-anchor="middle">regression 安全回归</text>
<rect x="630" y="40" width="120" height="56" rx="8" fill="#e6f4ea" stroke="#188038"/><text x="690" y="63" text-anchor="middle">5 Thresholds</text><text x="690" y="81" text-anchor="middle">阈值 → pass</text>
<line x1="150" y1="68" x2="163" y2="68" stroke="#333"/><line x1="305" y1="68" x2="318" y2="68" stroke="#333"/><line x1="460" y1="68" x2="473" y2="68" stroke="#333"/><line x1="615" y1="68" x2="628" y2="68" stroke="#333"/>
<text x="157" y="125" text-anchor="middle" fill="#f9ab00">fail → incomplete</text>
<text x="467" y="125" text-anchor="middle" fill="#c5221f">fail → blocked</text>
<text x="380" y="155" text-anchor="middle" fill="#555">all([]) is True: an empty safety family "passes" unless the manifest is checked first</text>
</svg>

- **输入护栏示例**：`is_supported_request` 用正则作范围规则 —— 必须提到工单 (`NS-\d+`) 且不含 upload/send/email/post/forward/token；`@input_guardrail(run_in_parallel=False)`；被拦的请求**零工具调用**（检查在 agent 开始前完成）。
- **"没有读取被拒" ≠ "正确的读取发生了"**：验收必须要求本次运行对请求工单有授权读取，并用该读取返回的内容核对草稿事实（与 II-5 同一规则）。
- **三个独立控制**：tracing、会话存储、响应存储 —— 关闭 trace 载荷不擦除会话历史；`store=False` 两者都不影响。
- moderation 适合筛查用户输入或草稿中的有害内容，**不判断读取是否授权、草稿是否真实**。

### 面试怎么说 / How to say it in the interview

**Q: "How do you know your agent is actually working?"**
> "I keep capability and safety cases separate, drawn from the customer's real work, with code graders for anything decidable from records and a calibrated model grader only for meaning. At Northstar, a candidate scored the same 6 of 8 as the current version, but pairing the cases showed it gained a drafting case and lost a safety case because its trace read another customer's ticket, so the gate blocked it. The gate also reconciles results against the versioned case manifest first, so an interrupted run with missing safety cases comes back incomplete instead of passing. In production I'd watch the same checks on live traces and add every new failure to the set."
（中文：分族、代码评 trace、模型只评含义；配对比较；先对账清单；线上持续加用例。）弱回答 "We have a test set, it scores 75%, and we monitor user feedback after launch."

**Q: "A draft is wrong. Where do you start?"**
> "With the trace, looking for the first step whose output contradicts the source. At Northstar it was a mapper in our own code, not the model, so the fix was the mapper plus an acceptance check, never a prompt patch on the agent that received the bad field."

**Q: "Two versions both pass 6 of 8. Why might one be unshippable?"**
> "Because the total can hide opposite changes. If one version gained a capability case but lost a safety case, that's a critical regression no drafting gain can outvote; pairing each case across versions exposes it."

---

## 速查 / Cheat sheet

| # | 要点（中文） | Key takeaway (English) |
|---|---|---|
| 1 | Demo 只证明"在 demo 条件下选定集合上可接受"；上线还需采用、工作流影响、支持、交接四类独立证据 | A demo proves acceptance on a selected set; production also needs adoption, workflow impact, support, and handoff evidence |
| 2 | 四个所有权问题：谁用、成功是什么、故障谁支持、交接后剩什么；每个分 已知/未知/提议 | Four ownership questions — users, success, support, handoff — each split into known / unknown / proposed |
| 3 | 结项三类证据：修复后评测、观察到的工作流结果、客户团队亲自运行（部署、复现评测、回滚演练） | Closeout needs corrected evals, observed workflow results, and the customer team running it themselves |
| 4 | 分母决定结论：采用率数人、覆盖率数工作量；中位数差 × 请求数 ≠ 总节省；观察性对比不证明因果 | Denominators matter: adoption counts people, coverage counts work; a median difference times volume is not total savings |
| 5 | 总分会掩盖切片：96% 藏着例外 80%；85% 藏着报销 50%；6/8 藏着安全回归 —— 永远按类别切分并跨版本配对 | Aggregates hide slices — always split by category and pair cases across versions |
| 6 | 升级五要素：问题、后果、证据、请求、跟进；"接受"单独记录，截止日期不是同意 | Escalation = problem, consequence, evidence, request, follow-through; record acceptance separately |
| 7 | 拒绝功能时分开五个来源：Charter、Model Spec、使用政策（版本+生效日）、客户授权、法律；模型能做 ≠ 被允许 | Refusals rest on five separate sources; a model that complies shows capability, not permission |
| 8 | 按 call_id 关联工具结果并核对 ticket 身份；按位置 zip 会让完成顺序变成身份 | Correlate tool results by call ID and verify identity; positional zip turns completion order into identity |
| 9 | Schema 管形状，验收管内容；验收必须要求本次运行有授权读取 | Schemas fix shape, acceptance checks content — and must require an authorized read in this run |
| 10 | 身份、授权、历史归属、预算、验收留在应用；SDK 只管编排；会话 ID 不是认证，加载历史前查归属 | The SDK orchestrates; identity, authorization, history ownership, budgets, and acceptance stay in app code |
| 11 | 写操作：needs_approval 暂停 + 决定绑定确切参数 + 写事务内重查权限/参数/过期 + 账本收据；批准过期 ≠ 截止时间 | Writes: pause before execution, bind approval to exact args, recheck inside the write transaction, prove with a ledger receipt |
| 12 | 认证、授权、审批是三道门；审批不能扩大主体范围；授权放在网络边界之后（MCP server 端） | Authentication, authorization, and approval are separate gates; approval cannot widen scope |
| 13 | 护栏时机决定能力：并行输入护栏和输出护栏都可能在效果之后；移除能力 + 只读凭证 + 模型外的外发限制才是预防 | Guardrail timing limits them; prevention means removing capabilities, scoped credentials, and egress control outside the model |
| 14 | 工具结果/检索内容是数据不是指令；先资格过滤再排序和生成；引用不等于支撑 | Retrieved content is data; filter eligibility before ranking and generation; a citation is not support |
| 15 | 先最简：固定工作流 > 单 agent > 多 agent；多 agent 需对基线测出收益；handoff 不通知人类 | Start simple; add agents only when measured against a baseline; a handoff notifies no human |
| 16 | 超时 = 未知而非失败；稳定操作/请求 ID 持久绑定主体+参数；不可查则升级，绝不用新 ID 重试 | A timeout means unknown; reconcile with a stable, durably bound operation ID — never retry under a fresh ID |
| 17 | 评测集放自己代码里（托管 Evals 已弃用）；能力/安全分族 + holdout；代码评 trace 与效果，模型只评含义；缺证据=incomplete 也阻止发布 | Own the eval gate in code; capability vs safety + holdout; incomplete evidence blocks release too |
| 18 | 调试：先遏制并冻结记录，找第一个与事实来源矛盾的步骤（常在应用代码如 mapper），代码修复而非提示补丁 | Debug by containing first, then fixing the earliest step that contradicts the source — in code, not prompts |
| 19 | 成本按整个任务算：所有调用、重试、工具、缓存假设；$126 → $401.40；先过质量线再谈速度 | Cost the whole task — every call, retry, tool, cache assumption; clear the quality bar before optimizing speed |
| 20 | 数据：API 数据默认不训练；滥用日志 30 天；ZDR 仅部分端点；store=False 不等于零保留；未确认的要求是上线阻塞项 | API data isn't trained on by default; abuse logs 30 days; ZDR per endpoint; store=False isn't zero retention |
