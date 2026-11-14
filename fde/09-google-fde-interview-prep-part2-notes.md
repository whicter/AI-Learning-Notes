# Google FDE Interview Prep, Part 2: Interview Loop & Case Studies｜Google FDE 面试准备（下）：面试流程与案例

# Section I — Course "Google FDE Interview Prep"｜第一部分：Google FDE 面试准备课程

## 1. The Interview Loop Overview｜面试流程总览

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/B8plEZDox9Y

### 要点 / Key ideas

**核心原则**：把邀请信里**已确认的事实 (confirmed details)**、公开面经里的**报道可能性 (reported possibilities)**、以及**未决事项 (unresolved items)** 分开记录。这样可以广泛准备、问精准问题，也不会带着错误环境或未授权工具进场。

示例邀请信："Next steps are a technical coding session and a practical implementation session. Scheduling details will follow."

| 类别 (Category) | 内容 (Content) |
|---|---|
| 已确认 (Confirmed) | 两个 session 的名称："technical coding" 和 "practical implementation"；排期待定 |
| 报道可能性 (Reported) | 公开面经：五个面试组成部分；早期版本：recruiter → 在线编程测评 (OA) → 技术视频面 → 4–6 轮 onsite（来源本身警告并非所有 Cloud FDE 都如此） |
| 未决 (Unresolved) | 时长、日期、顺序、剩余轮次、语言、编辑器、执行环境、工具权限（特别是 AI 工具） |

关键区分：**有用的准备推断 (useful practice inference)** vs **流程事实 (process fact)**。"我应该练习模糊需求下的实现" 是合理的准备选择；"practical session 允许用 AI 编辑器" 则需要明确授权。

**课程的准备顺序（不是保证的面试顺序）**：

| 能力领域 (Capability area) | 需要展现的可观察工作 (Observable work) |
|---|---|
| 招聘官面 (Recruiter screen) | 用部署证据讲岗位匹配：客户问题、个人贡献、生产约束、可证实的结果 |
| 编程与算法 (Coding & algorithms) | 正确实现、测试典型和边界用例、讲复杂度、边写边讲清思路 |
| 氛围编程 (Vibe coding) | 澄清模糊需求、声明假设、交付可工作的第一版、适应需求变更、协作调试 |
| Agent / ML 系统设计 (Agentic & ML design) | 需求、数据流、身份与权限 (identity & authority)、评估、可靠性、延迟、成本，作为一个整体讲 |
| Googleyness | 协作、模糊情况下的判断、证据变化时的谦逊 (humility)、在合适边界内的主人翁意识 (ownership) |

之后是 **招聘委员会 (Hiring Committee, HC)** 和 **团队匹配 (Team Matching)**。

**客户判断力 (customer judgment) 贯穿所有轮次**：架构时问"谁能批准写操作"；实现时如何不误导客户地解释限制；编程时承认错误假设。即使没有名为 "behavioral" 的轮次也要展现。一个 session 可以考多种能力，所以 session 数量少**不是**删减准备范围的理由。

<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect width="760" height="330" fill="#fff"/>
  <text x="380" y="24" font-size="15" text-anchor="middle" font-weight="bold">Google FDE Interview Loop｜面试流程</text>
  <rect x="20" y="50" width="120" height="60" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="80" y="76" font-size="13" text-anchor="middle">Recruiter Screen</text>
  <text x="80" y="95" font-size="12" text-anchor="middle">招聘官面</text>
  <rect x="165" y="50" width="120" height="60" rx="8" fill="#e6f4ea" stroke="#34a853"/>
  <text x="225" y="76" font-size="13" text-anchor="middle">Coding / Algo</text>
  <text x="225" y="95" font-size="12" text-anchor="middle">编程算法</text>
  <rect x="310" y="50" width="120" height="60" rx="8" fill="#e6f4ea" stroke="#34a853"/>
  <text x="370" y="76" font-size="13" text-anchor="middle">Vibe Coding</text>
  <text x="370" y="95" font-size="12" text-anchor="middle">模糊需求实现</text>
  <rect x="455" y="50" width="130" height="60" rx="8" fill="#fef7e0" stroke="#fbbc04"/>
  <text x="520" y="76" font-size="13" text-anchor="middle">Agentic/ML Design</text>
  <text x="520" y="95" font-size="12" text-anchor="middle">Agent 系统设计</text>
  <rect x="610" y="50" width="130" height="60" rx="8" fill="#fce8e6" stroke="#ea4335"/>
  <text x="675" y="76" font-size="13" text-anchor="middle">Googleyness</text>
  <text x="675" y="95" font-size="12" text-anchor="middle">文化/领导力</text>
  <line x1="140" y1="80" x2="163" y2="80" stroke="#555" stroke-width="1.5"/>
  <line x1="285" y1="80" x2="308" y2="80" stroke="#555" stroke-width="1.5"/>
  <line x1="430" y1="80" x2="453" y2="80" stroke="#555" stroke-width="1.5"/>
  <line x1="585" y1="80" x2="608" y2="80" stroke="#555" stroke-width="1.5"/>
  <rect x="20" y="130" width="720" height="40" rx="8" fill="#f1f3f4" stroke="#9aa0a6" stroke-dasharray="5,4"/>
  <text x="380" y="155" font-size="13" text-anchor="middle">Customer judgment across ALL rounds｜客户判断力贯穿所有轮次</text>
  <line x1="380" y1="170" x2="380" y2="205" stroke="#555" stroke-width="1.5"/>
  <polygon points="374,200 386,200 380,210" fill="#555"/>
  <rect x="190" y="212" width="170" height="56" rx="8" fill="#ede7f6" stroke="#7e57c2"/>
  <text x="275" y="236" font-size="13" text-anchor="middle">Hiring Committee</text>
  <text x="275" y="255" font-size="12" text-anchor="middle">招聘委员会 (packet review)</text>
  <rect x="400" y="212" width="170" height="56" rx="8" fill="#ede7f6" stroke="#7e57c2"/>
  <text x="485" y="236" font-size="13" text-anchor="middle">Team Matching</text>
  <text x="485" y="255" font-size="12" text-anchor="middle">团队匹配</text>
  <line x1="360" y1="240" x2="398" y2="240" stroke="#555" stroke-width="1.5"/>
  <text x="380" y="300" font-size="12" text-anchor="middle" fill="#555">Course prep order, not a guaranteed sequence; rounds can merge (e.g. 2 interviews in 2 days)</text>
  <text x="380" y="318" font-size="12" text-anchor="middle" fill="#555">准备顺序 ≠ 实际顺序；轮次可能合并压缩</text>
</svg>

**四个时钟 (Four clocks)** —— 分开追踪：

| 时钟 (Clock) | 含义 (Meaning) |
|---|---|
| 单轮时长 (Round duration) | 每轮多长，含准备/简报时间 |
| 面试间隔 (Interview spacing) | 同一天还是分不同日期 |
| 剩余轮次 (Remaining stages) | 已排的轮次之后还有什么 |
| 更新预期 (Update expectations) | recruiter 何时给排期或结果 |

公开面经有 "两天两轮" 的压缩安排，但这不是典型的 application-to-offer 时长，也不是通用的两轮流程。日期确定前，先对所有能力完整过一遍；日期确定后，倒排复习和环境检查。

**按岗位方向调整 (Adjust for the opening)**：

| 岗位方向 (Opening focus) | 额外强调 (Extra emphasis) |
|---|---|
| 数据方向 (Data-focused) | SQL 正确性、数据粒度 (data grain)、管道校验、发布状态、运维所有权 |
| Agent 方向 (Agent-focused) | 工具契约 (tool contracts)、授权检索 (authorized retrieval)、评估、故障隔离 (failure containment)、工作流经济性 |
| 客户沟通方向 (Customer-facing) | 解释权衡、就边界达成一致、在客户信息不全时不编造事实 |

职级/头衔本身不能说明题目难度、是否考算法或官方 rubric。

**问 recruiter 的精准问题（一封邮件问完）**：所有剩余轮次、顺序、每轮时长与重点、远程还是 onsite；排期和反馈窗口；应强调的部署领域、所有权范围和深度；每个技术轮可用语言、编辑器/执行环境及设置要求；**分别确认**文档、互联网搜索、非 AI 自动补全、AI 聊天、AI 代码补全的规则，以及是否按轮次不同；"除非明确授权，我将不使用 AI 辅助准备"。

**解读有范围的授权 (Interpret scoped permission)**：recruiter 回复 "Both sessions use Python. Standard-library documentation is permitted. Practical implementation begins from an incomplete brief."

| 结论 (Conclusion) | 是否成立 (Supported?) |
|---|---|
| 两轮都用 Python | ✅ 已确认 |
| 可查标准库文档 | ✅ 已确认 |
| 实现轮从不完整需求开始 | ✅ 已确认 |
| 文档权限 = 可用搜索、AI 聊天、AI 补全 | ❌ 超出授权 |
| 这两轮就是全部流程 | ❌ 未确认 |
| 两轮会在连续两天进行 | ❌ 面经推断，不成立 |

"Vibe coding" 只是面经对模糊需求实现任务的称呼，**不授予任何工具权限**。部分 SWE 面试试点允许 Gemini 不代表 FDE 也允许。未声明的 AI 辅助一律视为不允许；练习编辑器要关掉内置 AI 助手。面试当天若指令和之前邮件冲突，**先指出差异、引用之前的授权、问清楚**，不要悄悄选更宽松的那个（诚信问题 integrity problem）。

**四个可检查的准备产出 (Four inspectable outputs)**：

| 产出 (Output) | 内容 (Content) |
|---|---|
| 讲解式编程题 (Narrated coding solution) | Python：把依赖事件分组成合法处理顺序或检测环（拓扑排序 topological sort）；覆盖空输入、重复依赖、不连通分量 (disconnected components)；测试 + 时空复杂度；录下讲解 |
| 模糊实现 (Ambiguous implementation) | 从不完整需求做一个批任务状态工具：假设日志 (assumptions log)、可工作第一版、测试；然后引入需求变更（如每个 job 支持多次尝试 attempts），展示实现和回归测试 (regression tests)变化 |
| 架构讲解 (Architecture explanation) | 只读内部知识助手：调用者身份 (caller identity)、授权检索、进入模型的证据、答案校验 (answer validation)、数据源不可用处理、评估、可靠性、延迟、成本驱动因素；以及一个随客户约束改变而改变的决策 |
| 主人翁与协作案例 (Ownership-and-collaboration example) | 一次客户/干系人 (stakeholder)分歧：你的职责、冲突需求、收集的证据、约定边界、结果；未测量的结果保持不确定 |

练习题：新邀请 "technical problem-solving session and a customer architecture discussion. You may use your usual development tools." —— "usual development tools" 仍需澄清是否含 AI；"两天两轮" 面经不能填补未决项。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "What are you expecting from this process?" | "So far I've confirmed a technical coding session and a practical implementation session, both in Python. I haven't assumed the rest of the loop, so I'm preparing across coding, ambiguous implementation, agentic system design, and collaboration stories, because those skills can show up inside any session." | 只说已确认的轮次，承认不确定，按能力准备 |
| "How would you prepare for a loosely specified implementation task?" | "I start by clarifying the goal and writing down my assumptions, then I ship a small working version with tests. When requirements change, I adapt the code and the regression tests together, and I narrate my debugging so the interviewer can follow my reasoning. I practice in the same language and tool setup that's been confirmed." | 澄清→假设→小版本→测试→适应变更→调试 |
| "Does permission to consult documentation include an AI assistant?" | "No, I wouldn't read it that way. Documentation access is a specific permission; AI chat or code completion would need explicit authorization for that round. If I were unsure, I'd ask the interviewer directly before using anything." | 文档权限≠AI 权限，先问再用 |
| "How does the target role change your preparation?" | "If the opening is data-heavy, I add SQL correctness, data grain, and pipeline validation. If it's agent-focused, I emphasize tool contracts, authorized retrieval, and evaluation. But I keep coding, implementation, design, and customer judgment in scope regardless." | 按岗位加重点，但不删核心能力 |

---

## 2. The Recruiter Screen｜招聘官面

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/qAroVjmn2xr

### 要点 / Key ideas

反面例子：候选人流利讲架构，但 "Why FDE?" 回答 "I want to work on cutting-edge AI"，讲交付说 "we launched it" —— 工作偏好和个人职责都不清楚。

公开的 recruiter 面关注：背景、动机、岗位匹配 (role fit)、面向客户的部署工作、对特定 Google Cloud 团队的兴趣。典型问题："讲一个你端到端交付的集成"、"和企业客户合作的经验"。只念架构（模型、检索框架、部署平台）回答的是另一个问题 —— 没说谁解决了权限限制、修了过期数据源、拿到了上线批准、支撑了运维交接 (operations handoff)。

**准备三个产出**：

| 产出 (Output) | 目的 (Purpose) |
|---|---|
| 动机 (Motivation) | 为什么喜欢客户集成式交付 + 为什么对已确认的 Google 范围感兴趣 |
| Agent/ML 故事 (Agentic or ML story) | 在真实交付中对模型相关行为的判断 |
| 经典工程故事 (Classical engineering story) | 模型之外的可靠实现与集成 |

FDE 工作核心：在客户环境写生产代码、企业集成 (enterprise integration)、生命周期可靠性 (lifecycle reliability)、交接给客户团队。

**Why FDE 的三个可观察部分**：
1. **澄清用途 (Clarifying use)**：用户需要回答什么问题，哪些动作不在范围内
2. **约束下实现 (Implementing under constraints)**：在尊重权限和运维边界的前提下连接已有系统
3. **完成交接 (Completing transition)**：持续参与测试、发布协调 (release coordination)，直到有明确的接收负责人 (receiving owner)

不要贬低 Customer Engineer、顾问或产品工程师"不写代码"；关键区别在于你想承担的交付承诺。

**Why Google and this team** = 三个链接：岗位已声明的工作 + 你的相关经验 + 你下一步想做的工作。不要声称产品优越性、用过没用过的产品、或内部消息；没确认的团队细节（如"这个团队专注受监管行业"）不要编。

**示例项目（虚构）**：

| 字段 (Field) | Rowan 政策助手 (policy assistant, ML) | Tern 库存同步 (inventory sync, classical) |
|---|---|---|
| 用户问题与范围 | 只读助手回答政策问题 | 夜间库存同步服务，部分运行需人工修复 |
| 团队 | 3 名工程师，另一人做界面 | 2 名工程师，另一人负责上游导出变更 |
| 个人实现 | 数据源连接器、权限感知检索适配器 (permission-aware retrieval adapter)、评估工具 (evaluation harness) | 稳定记录 ID、可重放写入 (replay-safe writes)、对账报告 (reconciliation reporting)、运维手册 (runbook) |
| 关键问题与动作 | 过期文档选择 (stale-document selection) 影响有依据回答 (supported answer)；修正选择逻辑并加回归用例 | 重放不能产生额外业务副作用，对账需暴露差异 |
| 验收证据 (acceptance evidence) | 约定的 50 题预发布集 (pre-release set)：41 → 47 个有依据回答 + 3 个显式转人工 (explicit handoffs) | 发布前 30 晚中 9 晚需人工修复 → 发布后 30 晚中 1 晚（同一修复定义） |
| 批准与运维 | 客户安全负责人批准访问；客户运维批准上线并接手一线支持 (first-line support) | 客户运维批准上线并保留 on-call |
| 上线观察 | 两周 80 个问题、12 次人工升级 (human escalations) | — |
| 局限 | 未做节省时间研究；无长期维护承诺 | 观察性对比，非对照实验 (controlled experiment)；不含长期维护 |

**夸大版本 vs 修正版**：

| 夸大说法 (Inflated) | 修正说法 (Repaired) |
|---|---|
| "I owned the whole AI deployment." | "I implemented the connector, permission-aware retrieval adapter, and evaluation harness in a three-engineer delivery; customer security approved access and operations approved release." |
| "Achieved 94% production accuracy." | "After my source-selection fix, the same agreed pre-release set went from 41 to 47 supported responses out of 50, with three explicit handoffs." |
| "Saved hundreds of hours." | "The two-week release observation recorded 80 questions and 12 human escalations; time savings weren't measured." |
| "Eliminated inventory failures." | "Runs needing manual repair dropped from 9 of 30 to 1 of 30 under the same repair definition; it was an observational comparison." |

47/50 = 94% 算术没错，但它是**预发布测试集**上的结果，不是"生产准确率 (production accuracy)"。

**四步压缩法 (Compress without inflation)**：问题与范围 → 个人职责 → 约束与关键动作 → 结果与边界。每个故事练 60–90 秒，动机 45–60 秒（练习目标，非官方限制）。共享交付用 "we"，个人动作用 "I"。**先讲结果**，只在改变结果含义或被问到时才加限定 —— 以局限收尾听起来很防御。

**三类证据分开 (Three evidence categories)**：

| 类别 (Category) | 含义 (Meaning) |
|---|---|
| 验收测试证据 (Acceptance-test evidence) | 在约定测试条件下的表现 |
| 生产观察结果 (Observed production outcomes) | 在定义的发布人群与时段中发生了什么 |
| 估算业务收益 (Estimated business benefits) | 基于假设的预测，需要独立计算与说明 |

一个可信的影响陈述包含：度量 (metric)、人群 (population)、观察期 (observation period)、对比基准 (baseline)、重要局限。

**项目事实表字段 (Fact sheet fields)**：用户问题与交付范围；你的贡献与协作者；关键约束与工程决策；验收标准与上线批准人 (release approver)；上线后运维负责人；度量结果、分母、时段；基线/对比方法与局限。只有原型就说原型，并明确指出缺少生产部署经验；不要捏造客户上线。

### 面试怎么说 / How to say it in the interview

**Why FDE + Why Google（组合动机，约 45–60 秒）**：
> "I'm drawn to FDE work because I enjoy turning a useful idea into something a customer can actually operate. On a read-only policy assistant, my work on permission-aware retrieval and stale-source selection showed me that identity, evidence quality, and supportability are the problems I want to keep solving, and my inventory integration work reinforced that through replay safety and reconciliation. Google interests me because the scope you've described is customer-integrated agent delivery, and I'd like to bring that integration experience to enterprise deployments on Gemini and the Google stack. I haven't used that stack in these projects, so I'd be building on transferable experience. Which integrations and operational responsibilities does the team own?"

中文：动机连接到真实行为；对 Google 的兴趣挂在已确认范围上；坦白没用过 Gemini；最后反问团队职责。

**Agent/ML 故事（Rowan）**：
> "At Rowan, a three-engineer team delivered a read-only policy assistant. I implemented the source connector, the permission-aware retrieval adapter, and the evaluation harness; another engineer built the interface. The key issue was stale-document selection — the assistant needed current policy evidence to support its answers. On an agreed pre-release set of 50 questions, the first version gave 41 supported responses; after I fixed source selection and added regression cases, the same set gave 47 supported responses and three explicit handoffs. Customer security approved access, operations approved release, and in the first two weeks it handled 80 questions with 12 escalations to people."

中文：范围→个人实现→关键问题→同一测试集前后对比→批准人与上线观察。

**经典工程故事（Tern）**：
> "At Tern, I worked on a nightly inventory sync service with one other engineer. I implemented stable record identifiers, replay-safe writes, reconciliation reporting, and the runbook; my teammate owned the upstream export changes. The key decision was making replay safe so repeating work never created an extra business effect, and making discrepancies inspectable so operators knew exactly which records to repair. Runs needing manual repair dropped from 9 of 30 to 1 of 30 under the same definition, and since my teammate's changes shipped in the same release, that's a shared result."

中文：集成约束→个人实现→可重放与对账→结果是共享的。

**追问 (Follow-ups)**：

| 追问 (Follow-up) | English answer | 中文 |
|---|---|---|
| "What did you personally build?" | "At Rowan, the source connector, the permission-aware retrieval adapter, and the evaluation harness. I also fixed stale-document selection and added regression cases. Another engineer built the interface." | 列出个人组件，点明别人做的部分 |
| "Who approved release?" | "At Rowan, customer security approved access and customer operations approved release. At Tern, customer operations approved rollout." | 批准权在客户 |
| "How did you measure that?" | "Rowan's 47 of 50 used the same agreed pre-release questions as the initial 41 of 50. Tern compared 30 nightly runs before and after with the same operator-repair definition; it was observational, not controlled." | 同一测试集；观察性对比 |
| "What happened after handoff?" | "Rowan operations took first-line support, and the two-week observation showed 80 questions and 12 escalations. Tern operations kept on-call. I wouldn't claim a longer maintenance role from those facts." | 交接对象明确，不夸大维护职责 |
| "Walk me through an agentic or ML deployment." | Use the Rowan answer: scope, my implementation, one model-related problem, my fix, acceptance evidence, release authority, and the limits of the observed outcome. | 范围+实现+问题+证据+批准+局限 |
| "Describe a classical engineering integration and its impact." | Use the Tern answer: the integration constraint, my implementation, collaborators, who owned operations, and a consistently defined outcome — and I'd note the comparison was observational. | 约束+实现+协作+运维+一致定义的结果 |

---

## 3. The Coding Round｜编程轮

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/R1qBD3XXLx0

### 要点 / Key ideas

反面例子：看到 "subarray sum" 就写滑动窗口 (sliding window)，十分钟后被负数用例打破，没时间恢复。缺的不是算法知识，而是在时间压力下**选择、检查、解释**方案的流程。

**典型形式（以 recruiter 确认为准）**：

| 维度 (Aspect) | 典型情况 (Typical) |
|---|---|
| 时长 (Length) | 约 45 分钟，1–2 题，追问会改变约束 |
| 环境 (Environment) | 共享文档或简单编辑器，无自动补全，常常不能运行代码 → 练习写"不运行也可信"的代码 |
| 语言 (Language) | 通常自选；Python 常见 |
| 题型 (Style) | 通用数据结构与算法；FDE 面试官可能用客户语境包装（日志事件、库存记录、请求链路），本质是标准模式 |

**面试官看什么 (What interviewers look for)**：澄清 (clarification) → 方案理由 (approach，可先给 baseline) → 正确可读的代码 → 主动测试 (testing) → 复杂度 (complexity) → 适应变化 (adaptation)。

**45 分钟时间分配**：

| 阶段 (Phase) | 时间 (Time) | 做什么 (What) |
|---|---|---|
| 澄清 (Clarify) | ~5 min | 复述题目，问输入、输出、边界、规模 |
| 方案 (Approach) | ~5 min | 先 baseline，再更优方案及其理由 |
| 编码 (Code) | ~20 min | 写干净代码，只解释关键决策 |
| 测试 (Test) | ~7 min | 走一遍正常用例 + 两个边界用例 (edge cases)，修 bug |
| 分析与适应 (Analyze & adapt) | 剩余 | 复杂度 + 追问变更 |

习惯：在**决策点**说话而不是逐行念；接受提示 (take hints well) —— 提示通常意味着面试官看到问题；卡住就回到 baseline（正确的暴力解 + 说明代价 > 没写完的最优解）；说 "done" 之前先测。

**常见模式表 (Common patterns)**：

| 题目信号 (Signal) | 模式 (Pattern) | 关键不变量 (Key invariant) | 复杂度 (Complexity) |
|---|---|---|---|
| 有序数据中两/三数凑目标 | 双指针 (Two pointers) | 被丢弃的元素没有剩余合法配对 | 排序 O(n log n) 后 O(n) |
| 非负值/唯一性约束下最长/最短连续区间 | 滑动窗口 (Sliding window) | 每次收缩后窗口合法；被排除的起点不会再变合法 | O(n) |
| 带符号值的连续区间和：计数或最长 | 前缀和 + 哈希表 (Prefix sums + hash map) | 表中只含当前端点之前的边界 | 期望 O(n) 时间/空间 |
| 成员、重复、计数 | 集合/频率表 (Set / frequency map) | 表恰好反映已见元素 | 期望 O(n) |
| 有序数据中第一个满足条件的位置 | 二分查找 (Binary search) | 答案始终在 [lo, hi) 内 | O(log n) |
| 时间区间重叠：合并或最大并发 | 排序 + 扫描线 (Sort + sweep) | 已处理区间完全合并；同一时刻 end 先于 start | O(n log n) |
| 反复取最小/最大，top k | 堆 (Heap) | 根是活跃元素中的极值 | O(n log k) 时间，O(k) 空间 |
| 无权图/网格最少步数 | BFS + 队列 | 节点首次发现时距离即确定 | O(V + E) |
| 可达性、连通分量、环 | DFS/BFS + visited | 每个节点最多展开一次 | O(V + E) |
| 枚举所有组合/排列 | 回溯 (Backtracking) | 每个分支后恢复选择 | 指数级，如子集 O(n·2ⁿ) |
| 不同路径到达相同子问题 | 记忆化/动态规划 (Memoization / DP) | 状态包含决定未来选择的全部信息 | O(状态数 × 转移数) |

两个模式都像时，按**正确性论证 (correctness argument)**选，而不是按熟悉程度选。

### 例题：和为目标值的子数组个数 / Worked example: subarrays with a target sum

**Problem (English)**: Count the contiguous, nonempty subarrays of an integer array whose sum equals `target`. Values may be negative, zero, or duplicated. Count distinct index ranges (half-open `[i, j)`, `i < j`); empty input returns 0.

```text
Input:  values = [3, -1, 0, 2, -2, 3], target = 2
Output: 6
Ranges: [0,2) [0,3) [2,4) [3,4) [0,5) [1,6)
```

**澄清清单**：值能否为负？零和重复？计数的是索引区间还是不同值序列？空区间算吗？必须保持原顺序连续吗？规模多大？

**Baseline**：对每个起点向右扩展并维护运行和 (running sum) → O(n²) 时间、O(1) 额外空间。若在双循环里调用 `sum(values[i:j])` 会变成 O(n³)。

**为什么滑动窗口失败**：`[3, -1]`, target 2 —— 和超过 2 时丢弃 3，就丢掉了整段合法区间（加 -1 本可修复）。负数使"丢弃论证"失效。即使非负、精确和计数也要小心：零会让同一端点有多个合法起点。

**前缀和推导**：`prefix[0] = 0`，`sum(values[i:j]) = prefix[j] - prefix[i]`，所以以 j 结尾的区间匹配当且仅当 `prefix[i] = prefix[j] - target`。维护**严格早于当前端点**的前缀频率表 (prefix frequency map)，初始 `{0: 1}`（空前缀）；每加一个值：**先查询，后插入 (query before insert)**。

逐端点贡献：前缀 3（需 1，0 个）→ 2（需 0，1 个）→ 2（需 0，1 个）→ 4（需 2，**2 个**：边界 2 和 3）→ 2（需 0，1 个）→ 5（需 3，1 个）= 6。

```python
def count_target_subarrays_oracle(values, target):
    # Quadratic reference used only to check the fast version.
    total = 0
    for start in range(len(values)):
        running = 0
        for end in range(start, len(values)):
            running += values[end]
            total += running == target
    return total


def count_target_subarrays(values, target):
    counts = {0: 1}          # boundary 0: the empty prefix
    prefix = total = 0
    for value in values:
        prefix += value
        total += counts.get(prefix - target, 0)   # query earlier boundaries first
        counts[prefix] = counts.get(prefix, 0) + 1  # then make this boundary available
    return total
```

正确性：每个合法区间恰有一个结束边界和一个更早的起始边界；处理该端点时起始边界恰好在表中；先查后插排除空区间 → 每个合法区间恰好计一次。期望 O(n) 时间，O(n) 空间（最多 n+1 个不同前缀）。

**两种典型错误实现**：

| 错误 (Bug) | 在 `[0,0]`, target 0 上 (On [0,0], target 0) | 丢失的保证 (Lost guarantee) |
|---|---|---|
| 用 set 代替计数 (set instead of counts) | 1+1 = 2（正确 1+2 = 3） | 重复前缀的多重性 (multiplicity) |
| 先插入后查询 (insert before query) | 2+3 = 5 | 排除空区间 |
| 去掉初始 `{0:1}` | 漏掉从索引 0 开始的区间 | 起点为 0 的区间 |

讲解示范："Before querying, this map counts only earlier boundaries. At endpoint four, prefix four needs earlier prefix two, which has occurred twice."

**测试**：边界用例（`[]`→0、`[2]`,2→1、`[0,0]`,0→3、`[1,-1,1]`,0→2、`[3,-1]`,2→1、`[2,-2,2,0]`,2→5、`[0,0,0]`,0→6）+ 用 `itertools.product(range(-2,3), repeat=size)` 对长度 0–5 的所有序列、target -3..3 与 oracle 穷举 (exhaustive check)对比。穷举在小域上支持实现，不变量解释为什么对任意长度成立。

**追问变体：最长匹配区间 (longest matching range)** —— 前缀等式仍成立；计数问"多少个早期边界匹配"，最长问"**最早**的匹配边界"，因为它离当前端点最远。只改变表里存的东西：

```python
def longest_target_subarray(values, target):
    earliest = {0: 0}       # prefix value -> first boundary index where it occurred
    prefix = best = 0
    for end, value in enumerate(values, start=1):
        prefix += value
        start = earliest.get(prefix - target)
        if start is not None:
            best = max(best, end - start)
        earliest.setdefault(prefix, end)   # keep the FIRST occurrence; overwriting loses longer ranges
    return best
```

`[1,-1,1]`, target 1：前缀 0 首次在边界 0、在边界 2 重复；保留 0 使端点 3 得到长度 3。独立练习 `[2,-2,2,0]`, target 2：计数贡献 1,0,2,2 = 5；最长为整段，长度 4。

**客户语境 → 模式翻译 (Recognize the pattern behind the framing)**：

| 客户说法 (Customer framing) | 模式 (Pattern) |
|---|---|
| "统计净库存变化为零的时间窗口数" (net inventory change equals zero) | 前缀和 |
| "日志里并发会话峰值" (peak concurrent sessions) | 排序 + 扫描线 |
| "返回最常见的 10 个错误码" (top 10 error codes) | 频率表 + 堆 |
| "这个服务挂了哪些服务受影响" (which services are affected) | 图遍历 + visited |

把翻译大声说出来 = 展示从客户描述到精确技术问题的能力，这正是 FDE 的核心技能。

**练习计划**：哈希与前缀和（two-sum、subarray sum equals k、最长和为 k 子数组）；窗口与指针（无重复字符最长子串、有序数组配对）；排序与堆（merge intervals、meeting rooms、top k frequent）；图（number of islands、网格最短路、course schedule）；递归与 DP（subsets、climbing stairs、coin change）。用纯文档 + 45 分钟计时器 + 搭档追问来练。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "Window or prefix counts?" | "Values can be negative here, so a sliding window breaks — with [3, -1] and target 2, dropping the 3 on overshoot loses the whole valid range. Instead I use prefix sums: a range ending at j matches when an earlier prefix equals prefix[j] minus target, so I keep a frequency map of earlier prefixes, which preserves every start boundary and its multiplicity." | 负数使窗口失效；前缀相等推导；频率表保留多重性 |
| "Explain and test your implementation." | "The invariant is that before I query, the map holds only boundaries strictly earlier than the current endpoint. I seed it with zero for the empty prefix and query before inserting so empty ranges never count. I'd test empty input, [0, 0] with target 0 which should be 3, a negative case, and compare against a quadratic oracle on all small inputs. It's expected O(n) time and O(n) space." | 不变量+初始化+先查后插+边界测试+oracle+复杂度 |
| "Now return the longest range instead." | "The prefix equality still holds. For the maximum length I need the earliest boundary with each prefix value, so I store first-seen indices with setdefault instead of counts — overwriting would lose the longer candidate. Time and space stay O(n)." | 存最早索引而非计数 |

---

## 4. The Vibe Coding Round｜氛围编程轮（模糊需求实现）

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/m7jz5JjOQL9

### 要点 / Key ideas

场景："Build something that shows which documents have passed their checks." 给了三条：D-14/pass、D-28/fail、D-35/pass。任务：把不完整需求变成一个**小而可执行的契约 (small, executable contract)**，同时让不确定性可见。考察：澄清、声明假设、交付可工作增量、适应变更、协作调试。

**先澄清交付**：谁消费结果、怎么用？"Is this a local utility, an API response, or something a person views?" 然后是输入表示、成功输出、每个文档是否只有一个当前结果。

面试官确认：本地 Python 工具读 JSON 数组、打印 JSON 汇总；记录含 `document_id` 和 `status`，每文档一条；status 为 pass/fail；成功 = 每文档状态 + 计数。

**大声说出边界**："The first release reads a local file and produces the summary. I'll leave out cloud deployment, a UI, model calls, and persistence."

**实现契约 (implementation contract)** = 接受的输入 + 输出含义 + 失败行为。有用的澄清问题会**改变契约**：

| 影响正确性 (Affects correctness) — 必须先问 | 可逆的展示选择 (Reversible) — 不用问 |
|---|---|
| 输入形状、状态含义、重复处理、非法记录处理 | JSON 缩进 2 还是 4 空格 |

**提出默认值并确认 (Set explicit defaults)**：排序按 ID（输出确定性 deterministic）；空输入 → 空列表 + 零计数；非法输入 (invalid input) → 明确报错而不是静默丢弃 (silently dropping)。带后果的假设："I'll reject duplicate document identifiers because the current contract allows one result per document; does that match your intent?"

审核练习中的错误说法：一上来就做云服务（没人要求）；把缩进当正确性问题；重复 ID 直接覆盖、忽略非法记录且"不需确认"。阻塞问题解决后**停止扩展调研**，短口头契约比长需求文档好。

**工具权限四类分开确认**：文档 (Documentation)、更广互联网 (Broader internet)、AI 聊天 (AI chat)、AI 补全 (AI completion)。未声明一律视为不允许。

**如果允许 AI 辅助**：评估从打字速度转为**判断力**——是否能指挥好工具并抓住其错误。把它当"快但不可靠的队友 (fast but unreliable teammate)"：

| 做法 (Practice) | 说明 (Detail) |
|---|---|
| 从契约出发写 prompt (Prompt from the contract) | 给约定的输入形状、输出、错误行为，而不是原始模糊需求 |
| 小块生成 (Generate small pieces) | 一次一个函数/一个测试，逐个审阅 |
| 先读再接受 (Read before you accept) | 查编造的 API、静默丢弃非法记录、遗漏边界、字符串比较 bug |
| 用你理解的测试验证 | 自己写/审预期值；生成的测试可能和生成的代码有同样的错 |
| 对解释负责 (Own the explanation) | 每行都能解释，否则重写 |

讲出检查过程："The generated loop drops invalid records; our contract says reject them, so I'm changing it to raise."

### 第一版：最小端到端路径 / Deliver the first path

**Problem (English)**: Build a local Python utility that reads a JSON array of `{document_id, status}` records (status is `pass` or `fail`, one record per document) and prints a JSON summary: documents sorted by id with their status, plus counts including zeros. Empty input returns an empty list and zero counts. Invalid records, unsupported statuses, and duplicate ids raise a clear error.

```text
Input (checks_input.json):
[
  {"document_id": "D-14", "status": "pass"},
  {"document_id": "D-28", "status": "fail"},
  {"document_id": "D-35", "status": "pass"}
]
Output:
{
  "documents": [
    {"document_id": "D-14", "status": "pass"},
    {"document_id": "D-28", "status": "fail"},
    {"document_id": "D-35", "status": "pass"}
  ],
  "counts": {"pass": 2, "fail": 1}
}
```

```python
# document_checks.py (standard library only)
import argparse
import json


def validate_record(record, statuses):
    if not isinstance(record, dict):
        raise ValueError("each record must be an object")
    document_id = record.get("document_id")
    status = record.get("status")
    if not isinstance(document_id, str) or not document_id.strip():
        raise ValueError("document_id must be a nonempty string")
    if not isinstance(status, str) or status not in statuses:
        raise ValueError("unsupported status")
    return document_id, status


def format_summary(selected, statuses):
    documents = [
        {"document_id": key, "status": selected[key]}
        for key in sorted(selected)
    ]
    counts = {status: 0 for status in statuses}
    for document in documents:
        counts[document["status"]] += 1
    return {"documents": documents, "counts": counts}


def summarize_checks(records):
    if not isinstance(records, list):
        raise ValueError("input must be an array")
    statuses = ("pass", "fail")
    selected = {}
    for record in records:
        document_id, status = validate_record(record, statuses)
        if document_id in selected:
            raise ValueError("duplicate document_id")
        selected[document_id] = status
    return format_summary(selected, statuses)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()
    try:
        with open(args.input_file, encoding="utf-8") as source:
            result = summarize_checks(json.load(source))
    except (OSError, ValueError) as error:   # JSONDecodeError is a ValueError
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
```

设计要点：校验 → 选择 → 格式化 分离；只在成功后打印；函数可被测试导入。测试覆盖：正常（乱序输入→按 ID 排序 + 计数）、空输入、非法（`{}`、`[None]`、`[{}]`、空 ID、未知状态、重复 ID）。运行 `python -m unittest -v test_document_checks` 和 `python document_checks.py checks_input.json`。**函数签名、架构草图或未执行的代码都不算执行证据 (execution evidence)。**

### 需求变更：多版本 / Adapt the contract

面试官新增：允许多个修订版本 (revisions)、增加 `pending`、到达顺序任意。问三个**改变决策**的问题：
1. "latest" 是最大修订号还是最后收到的？
2. 计数统计文档还是每个事件？
3. 旧的 pass 能否在新的 fail 之后保留？

确认规则：每文档取**最大数值修订号 (greatest numeric revision)**，其状态决定文档状态和计数；修订号是无前导零的正十进制字符串；重复的 document/revision 对一律拒绝（即使状态相同）。

**契约差异 (contract delta)**：唯一性 (uniqueness)从 document_id 移到 (document_id, revision)；选择从"唯一结果"变成"最大修订"；pending 合法。**保留**：JSON 接口、输出条目、排序、空输入行为、校验函数、格式化函数、命令行包装 (CLI wrapper)。

<svg viewBox="0 0 720 230" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect width="720" height="230" fill="#fff"/>
  <text x="360" y="22" font-size="14" text-anchor="middle" font-weight="bold">Change only validation + selection｜只改校验与选择，保留 I/O 外壳</text>
  <rect x="20" y="50" width="130" height="60" rx="8" fill="#f1f3f4" stroke="#9aa0a6"/>
  <text x="85" y="76" font-size="13" text-anchor="middle">JSON file in</text>
  <text x="85" y="95" font-size="12" text-anchor="middle">读取 (kept)</text>
  <rect x="180" y="50" width="150" height="60" rx="8" fill="#fce8e6" stroke="#ea4335"/>
  <text x="255" y="76" font-size="13" text-anchor="middle">Validate</text>
  <text x="255" y="95" font-size="12" text-anchor="middle">+revision, +pending</text>
  <rect x="360" y="50" width="150" height="60" rx="8" fill="#fce8e6" stroke="#ea4335"/>
  <text x="435" y="76" font-size="13" text-anchor="middle">Select</text>
  <text x="435" y="95" font-size="12" text-anchor="middle">max int revision</text>
  <rect x="540" y="50" width="160" height="60" rx="8" fill="#f1f3f4" stroke="#9aa0a6"/>
  <text x="620" y="76" font-size="13" text-anchor="middle">Format + print</text>
  <text x="620" y="95" font-size="12" text-anchor="middle">格式化输出 (kept)</text>
  <line x1="150" y1="80" x2="178" y2="80" stroke="#555" stroke-width="1.5"/>
  <line x1="330" y1="80" x2="358" y2="80" stroke="#555" stroke-width="1.5"/>
  <line x1="510" y1="80" x2="538" y2="80" stroke="#555" stroke-width="1.5"/>
  <rect x="180" y="135" width="330" height="70" rx="8" fill="#fff" stroke="#ea4335" stroke-dasharray="4,3"/>
  <text x="345" y="158" font-size="12" text-anchor="middle">Uniqueness: document_id → (document_id, revision)</text>
  <text x="345" y="178" font-size="12" text-anchor="middle">唯一性键改变；计数在选择之后计算</text>
  <text x="345" y="196" font-size="12" text-anchor="middle">Counts derived after selection (docs, not events)</text>
</svg>

```python
import re


def parse_revision(raw):
    if not isinstance(raw, str) or re.fullmatch(r"[1-9][0-9]*", raw) is None:
        raise ValueError("revision must be positive ASCII decimal without leading zeros")
    return int(raw)


def summarize_checks(records):
    if not isinstance(records, list):
        raise ValueError("input must be an array")
    statuses = ("pass", "fail", "pending")
    latest, seen = {}, set()
    for record in records:
        document_id, status = validate_record(record, statuses)
        revision = parse_revision(record.get("revision"))
        pair = (document_id, revision)
        if pair in seen:
            raise ValueError("duplicate document/revision pair")
        seen.add(pair)
        if document_id not in latest or revision > latest[document_id][0]:
            latest[document_id] = (revision, status)
    selected = {key: value[1] for key, value in latest.items()}
    return format_summary(selected, statuses)
```

**不变量 (invariant)**：处理完每条记录后，`latest` 保存每个已见文档的最大已校验修订号。计数在选择后计算，被取代的事件不会虚增计数。

```text
Input:
D-14 rev "10" fail | D-28 rev "2" pass | D-14 rev "9" pass | D-35 rev "1" pending | D-28 rev "1" fail
Output:
documents: D-14 fail, D-28 pass, D-35 pending
counts:    {"pass": 1, "fail": 1, "pending": 1}   (5 events, 3 documents)
```

### 调试：错误的 pass / Debug the wrong pass

有 bug 的版本直接比较原始字符串：`incoming_revision > latest[document_id][0]`。Python 字符串按字典序 (lexicographic order)比较：`'9' > '10'` 为 True → D-14 的 rev 10 fail 被 rev 9 pass 替换。

测验：两种到达顺序（10→9、9→10）下有 bug 代码都选 **rev '9'/pass**。**顺序无关 (order-independent)不等于正确**——一个始终错误的选择器也能对所有顺序返回相同结果。要同时断言正确的数值赢家和跨顺序一致。

**证据驱动调试五步 (evidence-driven debugging)**：

| 步骤 (Step) | 本例 (This case) |
|---|---|
| 陈述不匹配 (State the mismatch) | "D-14 must be fail because revision 10 supersedes 9; the program returned pass." |
| 最小化 (Minimize) | 只留两条 D-14 记录 |
| 检查 (Inspect) | `repr(incoming_revision)`、类型、每次更新后的元组；首个错误变换：字符串 '9' 替换 '10' |
| 验证假设并修复 (Test hypothesis & repair) | 比较校验后的整数修订号 |
| 回归 (Regress) | 两种顺序都测，跑全套；不要硬编码 D-14 或压制异常输出 |

修订后的测试：对 5 条事件的全部 120 种排列 (`itertools.permutations`) 断言完整输出；数值回归两个方向；空输入；非法记录、未支持状态、非法修订号、重复对（相同或冲突状态）；**合法前缀后跟非法记录仍然报错，不返回部分计数**。

**复杂度**：选择期望 O(n)；排序 d 个 ID 为 O(d log d)；去重集合 O(n) 空间，latest 表 O(d)。流式 (streaming)、持久化 (persistence)、认证 (authentication)、托管 (hosting)、并发 (concurrency)都延后。收尾：展示的行为、实际跑过的测试、已知局限、下一个增量。没跑过的检查就说没跑过。

**练习题（fresh brief）**：阶段一 P-8/pass、P-9/fail、P-10/pass → pass=2、fail=1，顺序 P-10、P-8、P-9（字符串排序）。阶段二：P-8 rev 12 pending、P-9 rev 3 pass、P-8 rev 2 pass、P-10 rev 1 pass、P-9 rev 11 fail → P-10 pass、P-8 pending、P-9 fail，各一。先故意用字符串比较复现错误，最小化到两条，再修复并保留双向回归测试。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "What do you clarify first?" | "First, who consumes this and through what interface — a local script, an API, or a UI. Then the record shape, what the output has to show, whether each document has one result, and what happens with invalid input. Where you leave a choice open I'll propose a default with its consequence — for example, rejecting duplicate ids — and ask you to confirm." | 消费者/接口→记录形状→输出含义→唯一性→非法输入；默认值带后果确认 |
| "What do you ship first?" | "The smallest path that proves the contract end to end: read the JSON file, validate, summarize, print — with tests for a normal case, empty input, and invalid records. I'm deliberately leaving out hosting, UI, and persistence for this first increment." | 最小端到端路径 + 三类测试 + 明确边界 |
| "How do you accommodate revisions?" | "I'd name the contract delta first: uniqueness moves to document-plus-revision, selection becomes greatest numeric revision, and pending becomes valid. I keep the I/O shell, the formatter, and the validator, and replace only the selection logic. Counts are computed after selection, so they describe documents, not events." | 先说契约差异，保留外壳，只换选择逻辑 |
| "How do you recover from wrong output?" | "I state expected versus observed — D-14 should be fail but came back pass — then minimize to two records and inspect the types. Here the revisions were compared as strings, so '9' beat '10'. I fix it by comparing parsed integers and keep a regression test for both arrival orders, then rerun the whole suite." | 预期 vs 实际→最小化→定位→修复→双向回归 |
| "How would you use an AI assistant if it's allowed?" | "I'd treat it like a fast but unreliable teammate: prompt it from the agreed contract, generate one function at a time, and read every line before accepting it. I'd write the expected test values myself, because generated tests can share the generated code's mistakes, and I'd only keep code I can explain." | 从契约出发、小块生成、逐行审、自写预期值 |

---

## 5. The Agentic System Design Round｜Agent 系统设计轮

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/xlvGOX7Lwrq

### 要点 / Key ideas

白板画满了 UI、agent、search、incident API，但听者仍不知道**谁的身份到达 API**、**超时时员工收到什么**。一个可辩护的回答要把需求、权限 (authority)、证据、失败结果和经济性连在一起。

**典型形式**：约 45 分钟白板/画图工具，从故意模糊的短题开始；范围是 LLM 系统（检索、工具调用、编排 orchestration、护栏 guardrails、评估、周边云基础设施）；会被打断、改约束、问 "what if this fails?"；面试官常扮演客户。

**面试官看什么**：

| 要素 (Element) | 含义 (Meaning) |
|---|---|
| 需求优先 (Requirements first) | 画图前先澄清用户、动作、数据源、运行目标 |
| 追踪一个请求 (A traced request) | 把一个请求走过每个边界，而不只是列组件 |
| 权限与安全 (Authority & safety) | 指出身份和权限在哪里强制执行，且**模型从不决定权限** |
| 失败处理 (Failure handling) | 依赖超时或证据缺失时用户收到什么 |
| 量化权衡 (Quantified tradeoffs) | 估算延迟和成本，给出替代方案，说出什么证据会改变选择 |

**40 分钟排练分配**：

| 分钟 (Minutes) | 内容 (Content) |
|---|---|
| 0–4 | 澄清 (Clarification) |
| 4–8 | 需求与排除项 (Requirements & exclusions) |
| 8–18 | 架构 + 编号请求追踪 (Architecture & numbered trace) |
| 18–26 | 权限与失败行为 (Authority & failure behavior) |
| 26–34 | 评估、延迟、经济性 (Evaluation, latency, economics) |
| 34–40 | 追问与总结 (Follow-ups & synthesis) |

转场时邀请引导："The read-only flow is established. Would you prefer to examine permission enforcement or dependency failures next?" 打断要整合进图里，不要坚持自己的时间表。

### 案例题：内部事故助手 / Design an internal incident assistant

**Problem (English)**: "Design an internal incident assistant." Employees ask about incidents and runbooks. Clarify, then design a system that answers with authorized, supported evidence and defined failure behavior.

**澄清问题（改变架构的）**：用户及其决策；助手能否改变系统；谁拥有当前状态和批准流程 (approval process)；每个调用者可见哪些事故和 runbook；量级、延迟、成功结果。

**提出并确认的练习假设**：员工问事故与 runbook；**第一版只读 (read-only)**；事故服务 (incident service) 拥有当前状态；批准的 runbook 拥有流程；员工只能看有权限的服务。流量 20,000 请求/天，峰值 20 RPS (requests per second)；提议端到端 p95 ≤ 4 秒。说："I'm proposing those traffic and latency values so I can size the design; are they appropriate?" 延后：UI 样式、未来的修复动作、框架偏好。

**有依据回答 (supported answer)**：其主张来自已授权、适用的证据。另外单独记录：限制性回复是否安全处理了不可用证据；员工原始任务是否完成。

**白板四区**：需求与排除项 / 编号请求流 / 信任边界 (trust boundary)与状态 / 评估与运行预算。始终写着 "read-only" 和 "no autonomous remediation"。**从一个编排器 (orchestrator)开始**：没有需求证明需要多 agent 委托。

<svg viewBox="0 0 780 430" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect width="780" height="430" fill="#fff"/>
  <text x="390" y="22" font-size="15" text-anchor="middle" font-weight="bold">Read-only Incident Assistant｜只读事故助手架构</text>
  <rect x="15" y="60" width="95" height="56" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="62" y="84" font-size="13" text-anchor="middle">Client</text>
  <text x="62" y="102" font-size="12" text-anchor="middle">员工 u7</text>
  <rect x="135" y="45" width="460" height="250" rx="10" fill="#f8fbff" stroke="#4285f4" stroke-dasharray="6,4"/>
  <text x="365" y="62" font-size="12" text-anchor="middle" fill="#4285f4">Authenticated application boundary｜应用信任边界 (owns identity, admission, authority, release)</text>
  <rect x="150" y="75" width="130" height="60" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="215" y="100" font-size="13" text-anchor="middle">Auth + scope</text>
  <text x="215" y="118" font-size="12" text-anchor="middle">认证 → {S4}</text>
  <rect x="305" y="75" width="150" height="60" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="380" y="98" font-size="13" text-anchor="middle">Orchestrator</text>
  <text x="380" y="116" font-size="12" text-anchor="middle">单一编排器 + budgets</text>
  <rect x="150" y="165" width="140" height="56" rx="8" fill="#e6f4ea" stroke="#34a853"/>
  <text x="220" y="188" font-size="13" text-anchor="middle">Runbook retrieval</text>
  <text x="220" y="206" font-size="12" text-anchor="middle">权限感知检索</text>
  <rect x="305" y="165" width="140" height="56" rx="8" fill="#e6f4ea" stroke="#34a853"/>
  <text x="375" y="188" font-size="13" text-anchor="middle">Status adapter</text>
  <text x="375" y="206" font-size="12" text-anchor="middle">事故状态适配器</text>
  <rect x="460" y="165" width="120" height="56" rx="8" fill="#fef7e0" stroke="#fbbc04"/>
  <text x="520" y="188" font-size="13" text-anchor="middle">Gemini</text>
  <text x="520" y="206" font-size="12" text-anchor="middle">起草答案</text>
  <rect x="305" y="240" width="150" height="46" rx="8" fill="#fce8e6" stroke="#ea4335"/>
  <text x="380" y="260" font-size="13" text-anchor="middle">Release validation</text>
  <text x="380" y="277" font-size="12" text-anchor="middle">发布校验 (claims↔evidence)</text>
  <line x1="110" y1="88" x2="148" y2="100" stroke="#555" stroke-width="1.5"/>
  <line x1="280" y1="105" x2="303" y2="105" stroke="#555" stroke-width="1.5"/>
  <line x1="350" y1="135" x2="225" y2="163" stroke="#555" stroke-width="1.5"/>
  <line x1="380" y1="135" x2="378" y2="163" stroke="#555" stroke-width="1.5"/>
  <text x="250" y="152" font-size="11" fill="#34a853">parallel reads 并行</text>
  <line x1="440" y1="135" x2="515" y2="163" stroke="#555" stroke-width="1.5"/>
  <line x1="520" y1="221" x2="440" y2="245" stroke="#555" stroke-width="1.5"/>
  <line x1="305" y1="263" x2="110" y2="110" stroke="#ea4335" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="150" y="250" font-size="11" fill="#ea4335">validated answer</text>
  <text x="150" y="264" font-size="11" fill="#ea4335">or limitation 或限制回复</text>
  <rect x="620" y="75" width="145" height="60" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="692" y="98" font-size="13" text-anchor="middle">Incident service</text>
  <text x="692" y="116" font-size="12" text-anchor="middle">当前状态权威源</text>
  <line x1="445" y1="185" x2="618" y2="115" stroke="#555" stroke-width="1.2"/>
  <rect x="620" y="155" width="145" height="60" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="692" y="178" font-size="13" text-anchor="middle">Audit / telemetry</text>
  <text x="692" y="196" font-size="12" text-anchor="middle">决策记录 (before release)</text>
  <line x1="455" y1="263" x2="618" y2="200" stroke="#555" stroke-width="1.2"/>
  <rect x="135" y="320" width="460" height="90" rx="10" fill="#fff" stroke="#7e57c2" stroke-dasharray="6,4"/>
  <text x="365" y="338" font-size="12" text-anchor="middle" fill="#7e57c2">Offline ingestion｜离线 runbook 摄取路径</text>
  <rect x="150" y="350" width="120" height="46" rx="8" fill="#ede7f6" stroke="#7e57c2"/>
  <text x="210" y="378" font-size="12" text-anchor="middle">Approved runbooks</text>
  <rect x="295" y="350" width="140" height="46" rx="8" fill="#ede7f6" stroke="#7e57c2"/>
  <text x="365" y="370" font-size="12" text-anchor="middle">Parse + validate</text>
  <text x="365" y="386" font-size="11" text-anchor="middle">revision + ACL metadata</text>
  <rect x="460" y="350" width="120" height="46" rx="8" fill="#ede7f6" stroke="#7e57c2"/>
  <text x="520" y="378" font-size="12" text-anchor="middle">Publish index</text>
  <line x1="270" y1="373" x2="293" y2="373" stroke="#555" stroke-width="1.5"/>
  <line x1="435" y1="373" x2="458" y2="373" stroke="#555" stroke-width="1.5"/>
  <line x1="520" y1="350" x2="230" y2="221" stroke="#7e57c2" stroke-width="1.2" stroke-dasharray="4,3"/>
</svg>

**离线摄取路径 (offline ingestion path)**防止未校验的 runbook 版本成为在线证据：解析、修订号和访问元数据校验在索引发布之前；检索只用已发布的合格证据。**即使批准的恢复流程也不能证明当前事故状态**——那必须来自权威事故服务的观测。

应用拥有身份、准入 (admission)、权限、发布检查；Gemini 只基于已准入证据起草语言。持久记录保存：请求身份、授权决策、来源引用与修订号、各次尝试结果、模型版本、校验结果、发布结果（按约定保留与访问策略）；诊断遥测 (telemetry)避免不必要的受保护文本。

**请求 R-27 追踪**：用户 u7（权限 S4）问 "Is incident I-42 resolved, and what approved recovery checks apply?"

| 步 (Step) | 边界 (Boundary) | 发生什么 (What happens) |
|---|---|---|
| 1 | 客户端 → 应用 | 校验会话，把 u7 绑定到可信范围 {S4}；认证失败在受保护读取前终止 |
| 2 | 应用 → 读适配器 | 状态与检索**并行**（互不依赖）；适配器检查 I-42 属于有权限的服务——**模型提供的 ID 不授予权限**；检索在受保护文本到达推理前强制资格过滤 |
| 3 | 数据源 → 证据组装 | 状态返回权威状态 + 观测元数据；检索返回带 ID 和修订号的批准段落；不可用/不适用证据成为**显式缺口 (explicit gap)**而非成功的空结果 |
| 4 | 证据 → Gemini | 模型收到授权问题、已准入证据、来源 ID、受限指令；**不持有任何能扩展调用者范围的凭证** |
| 5 | 候选 → 发布校验 | 状态主张与事故观测匹配，流程主张和引用与检索版本匹配；不支持的主张 → 允许的修复尝试或限制结果 |
| 6 | 决策 → 用户 | 发布前保存决策记录；若必需记录持久化失败，扣下正常答案、返回运维限制 |

**越权变体 (unauthorized-access variant)**：问题点名 S9。会话仍识别 u7，可信范围仍是 {S4}；状态适配器拒绝，检索在推理前排除 S9；回复**不得透露**受保护事故是否存在、其状态或 runbook 文本。模型生成的工具请求只是**操作提议 (proposal)**，由应用和后端控制确定范围并执行。

**超时追踪（安全版）**：错误叙述 "agent calls search and incident API, retries on error" → 状态超时、检索返回恢复 runbook、模型宣布 "I-42 is resolved"。破坏了两个契约：恢复流程 ≠ 当前状态；超时 ≠ 完成了权威读取。

安全八步：绑定可信范围 → 授权并行读取 → 保存两个结果 → 咨询共享控制器 (controller) → 起草有依据指导 → 校验候选 → 保存发布决策 → 发布已校验结果。状态返回 `DEPENDENCY_TIMEOUT`，控制器不能替换成 "resolved"、"absent" 或旧会话值；Gemini 收到流程证据 + 显式 "status unavailable" 标记；校验拒绝任何当前状态结论。用户收到："I couldn't verify I-42's current status. The approved runbook lists these recovery checks…"

**预算（由一个应用控制器统一持有）**：4 秒应用截止时间 (deadline)、最多 2 次模型尝试、状态/检索合计最多 4 次尝试（含重试）。只有共享尝试预算和剩余截止时间都允许时才重试；传输截止要给校验和发布留时间；迟到结果不能重开已发布的答案。

**检索内容中的注入指令 (injected instruction)**：若检索段落里夹带一条要求执行修复命令的指令 → 视为不可信源内容；第一版没有暴露写工具，所以不可能变成修复动作。更一般地，超时也不能证明写操作失败——有写操作的设计需要显式的不确定结果处理 (uncertain-outcome handling)。

**关键路径 (critical path)**：

| 阶段 (Stage) | 分配 (Allocation) |
|---|---|
| 认证与准入 | 0.2 s |
| 并行读取 | 检索 0.6 s / 状态 0.8 s → 取 max |
| 生成 | 1.4 s |
| 校验与发布 | 0.2 s |
| **合计** | 0.2 + max(0.6, 0.8) + 1.4 + 0.2 = **2.6 s**，余量 (headroom) 1.4 s |

第二次完整生成可能吃掉全部余量 → 重试上限不保证重试能塞下。这些是**分配值不是测量百分位 (percentile)**；各组件 p95 相加 ≠ 端到端 p95。并发估算（Little's law 利特尔法则）：20 RPS × 2.6 s ≈ **52 个并发请求**，需要压测 (load testing)、依赖配额检查、有界并发 (bounded concurrency)、准入行为后才能作为容量结论。

**成本核算每一次尝试**：一次请求 2,000 输入 + 300 输出 token，修复一次 1,000 输入 + 200 输出 → 模型项 = 3,000 × 输入单价 + 500 × 输出单价 + 检索 + 状态 + 托管等。失败的尝试也计入总支出；指标 = 总成本 / 有依据成功数 (cost per supported success)，零成功时无定义。

**替代方案与可推翻证据**：

| 选择 (Choice) | 收益 (Gain) | 代价 (Cost) | 何时重新考虑 (Reconsider when) |
|---|---|---|---|
| 单一编排器 (One orchestrator) | 共享预算和追踪简单 | 失去专门化委托 | 不同工作流证明有独立价值且协调开销可接受 |
| 并行读取 (Parallel reads) | 关键路径更短 | 失去顺序执行时跳过不必要读取的机会 | 测得的可避免读取成本超过延迟收益 |
| 先用小模型 (Smaller model first) | 推理成本可能更低 | 可能降低有依据回答质量 | 仅在可比任务和安全测试后选；质量损失或修复成本抵消收益时反转 |

**发布证据 (release evidence)**：版本化 (versioned)测试集覆盖有依据回答、状态不可用、越权服务、过期 runbook、冲突证据、恶意检索指令、预算耗尽。同时检查最终结果和执行记录（实际读了哪些源？受保护访问是否在检索前被拒？引用是否标明支持主张的修订号？）。

| 评估类别 (Category) | 问题 (Question) |
|---|---|
| 任务成功 (Task success) | 请求的有依据结果是否发生 |
| 权限安全 (Permission safety) | 受保护操作和泄露是否被阻止 |
| 证据支持 (Evidence support) | 主张是否来自已准入来源 |
| 运行可靠性 (Operational reliability) | 依赖失败、尝试次数、截止结果是否正确处理 |
| 延迟与经济性 (Latency & economics) | 定义人群上的端到端 p95 与每次有依据成功的总成本 |

HTTP 成功率不能替代这些。任何观测到的越权泄露都是**发布阻断项 (release blocker)**，不能被平均掉。为数据源新鲜度 (freshness)、依赖事故、回滚 (rollback)指定负责人。

**追问：状态变慢到 3 秒且第一版无法加速** → 0.2 + max(0.6, 3.0) + 1.4 + 0.2 = **4.8 s**，原契约不成立。问哪个需求可谈判：

| 选项 (Option) | 做法 (Approach) | 新增负担 (Added burden) |
|---|---|---|
| 放宽同步目标 (Relax synchronous target) | 仍一次完整回答，修改延迟目标和容量假设 | 用户等更久 |
| 异步完成 (Asynchronous completion) | 先返回"已受理"，稍后交付结果 | 持久任务状态、**交付时重新授权 (reauthorization)**、轮询/通知成本、按完成度衡量成功 |
| 先给流程指导 (Procedure guidance first) | 状态标记 pending | 区分流程成功与最终状态完成；若承诺第二次回复需跟进状态与额外工作 |

**用缓存状态会悄悄改变"当前性"契约 (currentness contract)**。谈判用户体验时保持只读范围和授权不变。加权打分矩阵只是偏好说明，不能证明延迟目标可达。

**其他题型复用骨架**：

| 题型 (Prompt family) | 重点 (Focus) |
|---|---|
| 知识/支持助手 (Knowledge or support assistant) | 权限感知检索、grounding、证据缺失时怎么办 |
| 会执行动作的 agent (Agent that takes actions) | 审批门 (approval gates)、幂等写 (idempotent writes)、超时后结果未知的动作 |
| 自然语言分析 (NL analytics) | 语义 grounding、查询校验、扫描预算、行级权限 (row-level access) |
| 文档处理管道 (Document processing pipeline) | 抽取质量、人工审核队列、批处理 vs 实时成本 |
| 多 agent 工作流 (Multi-agent workflow) | 论证每个 agent 边界，预算/失败/追踪如何跨边界 |

通用清单：用户与决策、动作范围、权威源、身份与权限、一个追踪请求、失败结果、评估、延迟、成本。常见错误：只画框不追踪请求；让模型决定授权；把超时当空结果；没有需求就加 agent。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "What do you clarify first?" | "Who uses the answer and what they decide from it, whether the assistant can change anything, which systems are authoritative for status and procedures, and who can see what. Then I'll propose numbers to size it — say 20,000 requests a day, 20 per second at peak, and a four-second p95 — and ask whether those are reasonable." | 用户决策、动作范围、权威源、权限、提议并确认数值 |
| "Where is authority enforced?" | "Never in the model. The application validates the session and binds the caller to a trusted scope, the status adapter checks that the incident belongs to a permitted service, and retrieval filters by eligibility before any protected text reaches Gemini. A tool call the model generates is just a proposal; the backend decides." | 应用绑定范围→适配器检查→检索前过滤；模型调用只是提议 |
| "What happens if the status service times out?" | "The timeout is recorded as an explicit gap, not as 'resolved' or an empty result. The model can still draft the approved recovery checks, but validation rejects any claim about current status, so the user hears: 'I couldn't verify I-42's current status; here are the approved checks.' One controller owns the deadline and retry budgets, so a retry only happens if there's time left." | 超时是显式缺口；校验拒绝状态结论；统一预算 |
| "What if status is slow — three seconds?" | "Then the path is 0.2 plus 3.0 plus 1.4 plus 0.2, which is 4.8 seconds, so the four-second promise breaks. I'd ask which requirement can move: relax the latency target, go asynchronous with durable task state and reauthorization on delivery, or return the procedure first with status marked pending. I wouldn't silently cache status, because that changes what 'current' means." | 重算关键路径→指出破约→谈判三选项→不悄悄缓存 |
| "How do you reduce cost?" | "I compare complete workflows, including failed attempts and repairs, measured as cost per supported success. A smaller model only wins if it holds the same task-success and permission-safety gates on the same test set; if repair costs erase the savings, I reverse the choice." | 全流程成本/有依据成功；质量门不变 |

---

## 6. The Googleyness Round｜Googleyness（行为）轮

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/my99oZRy5Zr

### 要点 / Key ideas

对比："I built trust and took ownership" vs "I asked the operator to demonstrate rollback, discovered their account lacked permission, acknowledged that I had called the handoff complete too early, and involved the customer administrator"——同一件事，只有后者给听者**可检查的决策 (inspectable decisions)**。

**典型形式**：约 45 分钟对话，几个开放问题 + 深挖追问；多为 "Tell me about a time…"，偶尔 "What would you do if…"；主题：模糊性、错误与学习、分歧、无权威影响力 (influencing without authority)、主人翁、反馈；FDE 角度：客户反对、所有权不清、交接给客户团队。面试官听的是**具体决策、如何对待他人、学到什么**，而不是精致的讲故事。"Googleyness" 是候选人圈的叫法，不是官方 rubric 或性格测试。

**品质要通过决策体现 (Decisions reveal qualities)**：

| 品质 (Quality) | 体现方式 (How it shows) | 例子 (Example) |
|---|---|---|
| 模糊性 (Ambiguity) | 找出关键未知，选一个有界的下一步检查 | 让运维演示恢复，用证据替代关于就绪的争论 |
| 谦逊 (Humility) | 承认错误假设并改变方向 | "I treated documentation delivery as completed handoff." |
| 协作 (Collaboration) | 引出对方约束、共享决策、准确分配功劳 | 客户管理员与运维负责人职责不同 |
| 主人翁 (Ownership) | 承认自己对问题的贡献，在约定权限内推动解决，明确剩余责任 | 协调权限修正但不拥有授权权 |
| 学习 (Learning) | 之后实际使用的具体改变 | 交接前要求运维主导的演练 (drill) |

反模式 (anti-patterns)：口号；表演式自我批评（"I'm a perfectionist"）；不惜代价求一致（掩盖风险）；单方面救火（让接收团队依赖你）。**主人翁有边界**：可以协调权限修正而不拥有授权权；可以推动可支撑的交接而不承担无限期责任。

**六张故事卡 (Six story cards)**：

| 选题 (Prompt) | 主主题 (Primary) | 次主题 (Secondary) |
|---|---|---|
| 模糊的需求 (An ambiguous brief) | 模糊性 | 主人翁、协作 |
| 错误或失败的方法 (A mistake or failed approach) | 谦逊 | 学习、主人翁 |
| 客户分歧 (A customer disagreement) | 协作 | 判断、模糊性 |
| 跨团队无权威影响 (Cross-team influence) | 协作 | 领导力、主人翁 |
| 交付或运维问题 (Delivery or operational problem) | 主人翁 | 判断、学习 |
| 反馈经历 (A feedback episode) | 学习 | 谦逊、协作 |

一个项目可以有多个片段，一个片段可支撑多个主题。自检："What did I decide that another reasonable person might have handled differently?" 答不出来说明个人能动性不足。没有可信例子就记为准备缺口，**不要编造**。

**锁定事实字段**：背景与顺序（时间线、团队规模、角色、范围）；职责（你的义务、你的实现、他人的决策权）；约束与不确定性（干系人顾虑、未知、考虑过的选项）；决策与行动（你做了什么、为什么、什么改变了你的方法）；结果与局限（观察结果、证据、未解决工作、不确定性说明）；学习与追问。**跨多次复述，团队规模、范围、时间线、个人职责、结果、限定必须一致**；只调整强调点。

**Bracken 事实卡（虚构）**：

| 字段 (Field) | 内容 (Content) |
|---|---|
| 背景 | 4 人交付团队把只读内部支持助手交接给客户运维 |
| 候选人贡献 | 实现检索集成、写运维 runbook；交付 runbook 后宣布交接完成 |
| 决策者 | 客户运维负责人拥有验收权 (acceptance authority)；客户管理员控制访问授权 |
| 分歧 | 运维负责人拒绝接 on-call，要求候选人继续做唯一响应者 |
| 未知与选项 | 什么让验收不安全？选项：继续独自响应 / 强推验收 / 测试接收方能力 → 选有界测试 |
| 第一次演练 | 运维完成部署 tagged release、诊断模拟数据源读取故障；**无法回滚 (roll back)上一版并验证恢复**（账号缺权限）→ 2/3 |
| 纠正 | 承认过早宣布完成，记录缺口，协调批准流程；管理员批准并授予权限 |
| 第二次演练 | 3/3 完成；运维负责人接受约定范围与升级安排 |
| 证据局限 | 只有演练完成与范围内验收；无事故率下降、无普遍就绪、无业务节省 |
| 学习 | 交接清单要求客户主导的部署与恢复演示后才宣布完成 |

**STAR 时间分配（约 2 分钟）**：Situation 15 秒、Task 15 秒、**Action 65 秒**、Result + 反思 25 秒。自然讲，不要说 "Now for the Action section"。

**修正弱回答**："The customer was not technical and refused ownership, so I took charge, fixed their permissions, and achieved a seamless launch." 四个缺陷：无依据地贬低客户；没有说出自己的错误假设；声称拥有并不具备的授权权；未测量的上线结果。客户的**合理顾虑**是：在没有证明能恢复服务前不愿承担运维责任。问："What would make accepting this responsibility unsafe?"

**假设性追问**："What if the administrator could not approve rollback access?" → 明确标注是假设；保持交接未完成；记录缺口与风险；向决策者提出授权替代方案（如由批准的响应者恢复）或修订支持安排；任何临时责任需明确约定。**不要制造共识 (consensus)或绕过权限边界**；延迟交接可以是诚实的结果。

### 面试怎么说 / How to say it in the interview — 题库（每题 STAR 英文模型答案）

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 36 篇）。

**Q1. "Tell me about a customer disagreement."**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 36 篇）。

**Q2. "What did you personally get wrong?" / "Tell me about a mistake or failure."**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 36 篇）。

**Q3. "Tell me about an ambiguous assignment."**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 36 篇）。

**Q4. "Tell me about influencing someone you didn't manage." / "Cross-team influence without authority."**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 36 篇）。

**Q5. "When did you take ownership?" / "Tell me about a delivery or operational problem."**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 36 篇）。

**Q6. "Tell me about a time you received feedback."**
> 【待补充：story bank 里还没有"收到难听反馈"的真实素材，这题不要编。】回忆问题：设计评审里被指出过什么盲点？经理或同事给过哪条让你改变做法的反馈？你之后具体改了什么？
>
> 骨架 / Skeleton: "In ⟨context⟩, ⟨role, no name⟩ told me ⟨specific feedback⟩. My first reaction was ⟨honest⟩, but ⟨evidence⟩ showed they were right. I ⟨concrete change⟩, and since then I ⟨lasting habit⟩."

中文：真实素材补上之前，宁可承认"让我想一个最具体的例子"，也不要套课程的 Bracken 故事。

**Q7. "Tell me about a time new information changed your approach."**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 36 篇）。

**Q8 (hypothetical). "What would you do if rollback permission couldn't be approved?"**
> "That didn't happen, so this is hypothetical. I'd keep the handoff open rather than pretend it was done, document the recovery gap and its risk, and bring the decision owners options — for example, recovery by an already-approved responder, or a revised support arrangement. If I took on any interim responsibility, it would be explicitly agreed and time-bound. I wouldn't work around the permission boundary."

中文：明确是假设；不绕过权限；带选项给决策者；临时责任要明确约定。

---

## 7. Hiring Committee and Team Matching｜招聘委员会与团队匹配

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/JPBVkY8rZVJ

### 要点 / Key ideas

Recruiter 写 "Feedback is positive. We are discussing level and potential teams; there is no written offer yet." —— 只确认了正面反馈和正在讨论；**招聘批准、职级 (level)、团队、薪酬包 (compensation package)都未定**。

**面试后的典型流程（公开面经，非保证）**：

| 阶段 (Stage) | 内容 (Content) |
|---|---|
| 书面反馈 (Written feedback) | 每位面试官独立写观察 |
| 招聘评审 (Hiring review / HC) | 没面过你的小组结合背景审阅反馈，判断证据是否支持录用 |
| 定级 (Leveling) | 按证据支持的职责范围 (responsibility scope) 提议职级 |
| 团队匹配 (Team matching) | 与有空缺的 hiring manager 交流；可能在 HC 之前或之后 |
| Offer | 薪酬提议并审批，通常先口头后书面 |

可能几天到几周；recruiter 更新常滞后于内部进度，安静的一周不代表任何信号。

**四个不同问题**：招聘评审（证据是否支持录用？）/ 定级（能力支持什么范围？）/ 团队匹配（团队需求与你的优先级是否一致？）/ Offer 审批（哪些条款已确认？）。

**四个错误推断 (Four faulty inferences)**：

| 错误推断 (Faulty inference) | 正确做法 (Repair) |
|---|---|
| 正面反馈 = HC 已批准 | 问 "What hiring review or approval remains, and which decisions are already settled?" |
| 有客户交付经验 = 够 FDE IV | 问该职级期望独立承担哪些决策和交付范围，你的证据在哪里不足 |
| Team A 的交付描述就确定了运维范围 | 问事故归属 (incident ownership)、轮值覆盖 (on-call coverage)、交接条件、配套权限 |
| 总包有吸引力 = offer 可接受 | 分别确认 base、target bonus、equity（授予条款、归属 vesting）、一次性付款、福利、开始日期、截止日期、附带条件 (contingencies) |

FDE III 与 IV 的公开 JD 都写编码、调试、在客户环境共同交付、解决生产阻塞 (production blockers)、回传现场反馈 → "我写生产代码" 不能区分级别；IV 提到 strategic accounts 和 complex AI deployments。

**定级证据维度**：处理的模糊性、拥有的决策、管理的复杂度、客户协调、可复用成果。

**比较团队的同一组问题**：代表性项目工程师实际构建了什么；前六个月期望成果；实现 vs 架构咨询/workshop/enablement 比例；客户接触；出差；上线后谁负责服务；可复用工程如何与客户截止期权衡。

**HC 若要澄清**：简短回答实际问题，区分个人实现、共享交付、测试结果、生产观察结果。发现重大事实错误时，先问是否需要简短更正，不要主动重写面试内容。

**截止日期先到**：带具体理由请求延期："The support-ownership conversation is scheduled after the response deadline, and that information is essential to my decision. Could the deadline move until after that discussion?"

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "Why this team?" | "Your team's customer-integration work lines up with what I've actually built — permission-aware retrieval and replay-safe integrations that customers operate. I'd like to understand what engineers built on a recent engagement so I can confirm the implementation share." | 用真实经验连接团队工作，指出待确认点 |
| "What scope are you ready to own?" | "I can own integration design and implementation end to end, and coordinate delivery through customer acceptance. Release approval and long-term support have usually sat with the customer, so I'd want to understand which of those this role expects me to own independently." | 区分实现/协调与批准/支持权限 |
| "What are you looking for in the role?" | "Mostly hands-on implementation in customer environments, with a clear, bounded support model after launch. Those are the two things that matter most to me." | 直接说优先级，不编造筹码 |
| "What would you need to decide on an offer?" | "I'd need clarity on the post-launch support model and the expected scope for the level, plus the written terms. Could we set up a conversation with the hiring manager to cover those?" | 指出会改变决定的未决项，请求下一次对话 |

---

# Case Study 1: Retail Text-to-SQL Analytics Agent｜案例一：零售 Text-to-SQL 分析 Agent

## 8. CS1 — The Case Study｜案例简报

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/gk2RxqpZ7WG

### 要点 / Key ideas

**Problem (English) — the complete brief**:
- **Customer**: an unnamed global retailer, 2,800 stores in 14 countries; BigQuery warehouse with **about 4,000 tables** built over a decade by different teams.
- **Business problem**: about 1,200 merchandising and supply-chain analysts depend on a central BI team for every new question; **three-week backlog**.
- **Previous attempt**: an internal Gemini Text-to-SQL pilot looked good in demos but answered only **about 38%** of real questions correctly; shelved.
- **Mandate**: put a natural-language analytics agent into production for **one business domain within 90 days**.
- **Data access**: regional managers see only their own region; franchise data is separate from corporate data.
- **Privacy**: loyalty-program data contains PII. **Residency**: EU data must stay in EU regions.
- **Latency**: answers within **15 s at p95**. **Cost**: a cap on BigQuery scan cost per query (amount not given).
- **Stakeholders**: VP of Merchandising (sponsor); skeptical Head of Data Platform (owns BigQuery); BI team lead (worries about replacement); privacy officer (reviews data use); category managers (end users).

可辩护的交付句："Deliver a production natural-language analytics agent for one business domain within 90 days, subject to the stated data, performance, and cost constraints." 2,800 店/14 国解释环境规模，**不要求**第一版覆盖所有店、市场或表。"Production" 需要证据证明能支撑预期工作，演示不能证明。

**三个人群分开**：受影响人群（约 1,200 分析师）/ 列出的终端用户（品类经理 category managers）/ 首版人群（待定）。承诺 1,200 人立即可用 = 悄悄把受影响人群变成了上线人群。积压 (backlog)不等于节省金额或裁 BI 的授权。

**38% 说明了什么、没说明什么**：说明演示吸引力与真实问题正确性之间有差距 → 真实工作评估必须决定验收。没说明：评估了哪些问题、怎么算正确、失败分布 (failure distribution)（业务理解、数据选择、查询构造、权限）、能否与新评估公平比较。**诱人但错误**：换更强模型 + 开放更多表——更多访问扩大了解释空间、扫描量 (scan volume)和越权泄露机会。不能承诺提升百分比。

**支持边界 (support boundary)** 六部分：目的 (Purpose)、用户 (Users)、问题 (Questions)、数据 (Data)、含义 (Meaning)、限制 (Limits)。

| 简报原话 (Phrase) | 合理推论 (Implication) | 仍未决 (Open decision) |
|---|---|---|
| one business domain | 限定范围，不是整个数仓 | 哪个域、哪些表、哪些用户 |
| within 90 days | 保持截止日期 | 就绪证据和验收细节 |
| about 38% of real questions | 需要真实工作评估 | 失败原因与提升潜力 |
| regional managers see only own region | 限制区域访问 | 如何执行；跨区聚合是否允许 |

**四个独立数据边界**（通过一个不代表通过其他）：区域访问（请求措辞不能扩展权限；跨区聚合未定）；加盟分离 (franchise separation)（合法聚合不代表允许合并加盟与直营数据）；会员 PII（只读也会泄露；最终答案不显示 ID 不代表中途没访问敏感字段）；EU 驻留 (EU data residency)（正确答案不说明 EU 数据在哪处理）。**只读 = 没有写操作**，不保证机密性 (confidentiality)、正确业务理解或可负担的执行。

**15 秒 p95**：是定义人群的第 95 百分位 (percentile)，不是每个答案都 ≤15 秒。需确定：测量人群、计时边界、工作负载 (workload)、失败结果如何计入。扫描成本上限金额缺失 → 保持强制性但记为未决，**不要编造金额**。

**干系人贡献（不是已同意的职责）**：

| 干系人 (Stakeholder) | 已述角色 (Stated role) | 要寻求的贡献 (Contribution to seek) | 不能推断 (Don't infer) |
|---|---|---|---|
| VP of Merchandising | 赞助人 (sponsor) | 哪些有用工作值得这个版本 | 拥有所有发布决策 |
| Head of Data Platform | 拥有 BigQuery，持怀疑态度 | 访问安排与平台可行性；怀疑 = 需要证据 | 抵制或完整否决权 (veto) |
| BI team lead | 担心被替代 | 解释现有分析工作和业务含义 | 阻挠或已约定的未来角色 |
| Privacy officer | 审查数据使用 | 允许用途与审查所需证据 | 拥有所有技术/发布决策 |
| Category managers | 终端用户 | 支持的问题和答案是否有用 | 不受限的数据权限 |

发布决策、事故、维护的负责人仍需确认。

**诱人的错误方案**："Give Gemini read-only access to all 4,000 tables, tell it to filter by region, avoid displaying loyalty IDs, and launch after a fast exec demo." —— 超出单域、丢了 "about"；模型指令不是权限边界 (permission boundary)；PII 允许用途、加盟分离、EU 处理都未处理；演示速度不证明 p95 或扫描成本合规；前一个试点已证明演示与真实正确性的差距。

### 面试怎么说 / How to say it in the interview

**60 秒开场复述 (opening readout)**：
> "Here's how I read the mandate. You want a production natural-language analytics agent for one business domain within 90 days, so analysts can answer a bounded set of questions without waiting three weeks for the BI team. Last year's pilot looked good in demos but answered only about 38% of real questions correctly, so I'll treat real-question evaluation as the acceptance test, and I won't promise an accuracy number until we understand why the pilot failed. The release has to respect regional access, franchise separation, loyalty PII, and EU residency, meet 15 seconds at p95, and stay under a per-query scan cap. Before I propose an architecture, I need a few decisions from you."

中文：复述交付、业务问题、试点证据与局限、所有约束，然后转入关键问题。

**接着问的决策问题**：

| 主题 (Topic) | English question |
|---|---|
| 域与用户 | "Which domain comes first, which users does it serve, and which questions matter most to them?" |
| 含义 | "Who approves metric definitions, and what counts as a correct answer?" |
| 试点 | "Can we see the questions, grading criteria, and failures behind the 38% result?" |
| 数据策略 | "Are cross-region aggregates allowed? What does franchise separation require? Which loyalty fields and uses are approved?" |
| 驻留 | "Which components may process EU data, and where?" |
| 性能与成本 | "How is p95 latency measured, and what is the scan-cost cap per query?" |
| 所有权 | "Who approves release, and who owns incidents and maintenance afterward?" |

**"Why not give it read-only access to all 4,000 tables?"**
> "Because read-only only means no writes — it doesn't give us confidentiality, correct business meaning, or affordable scans. Opening the whole warehouse widens the space of wrong interpretations and expensive queries, and a prompt telling the model to filter by region isn't a permission boundary. The mandate is one domain, so I'd scope to curated tables we can govern."

中文：只读≠安全；全量开放扩大错误与成本；模型指令不是权限边界。

---

## 9. CS1 — Discovery and Scoping｜需求调研与范围界定

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/qVgXmwKoxgG

### 要点 / Key ideas

赞助人问："Can a better model guarantee 85%?" 回答："Before accepting that commitment, I need the actual questions, the pilot's errors, the approved meanings, the access rules, and the consequences of a wrong answer."

**五个调研问题，每个绑定可产出的证据**：

| 问题 (Question) | 要的证据 (Evidence to request) |
|---|---|
| 用户实际问什么？ | BI 工单 (ticket)日志、原始措辞、追问往来、交付的报表 |
| 试点为什么失败？ | 测试输入、输出、错误复盘 (error review)；区分业务理解错 vs SQL 错 |
| 谁拥有关键定义？ | 竞争定义、业务权威、已批准报表；分歧时的决策路径 |
| 当前权限如何执行？ | 用户→区域映射、访问安排、允许/拒绝请求示例 |
| 错误数字的后果？ | 哪些决策依赖报表、错误的代价、谁接收并更正已发布的错误答案 |

"We need more requirements" 没给客户具体下一步。面试中面试官扮演客户；约**前四分之一时间**做调研，然后大声提出范围："Based on what you've told me, I'd start with sales and inventory on curated tables, measure against real tickets, and decline when a definition is unapproved. Does that match your priorities?"

**调研发现**：
- 有 **600 条历史 BI 工单**
- 表名如 `fct_sls_dly_v3` 掩盖含义
- **三个团队对 net sales 定义不同；定义冲突导致了试点大部分错误**
- 试点用**合成问题 (synthetic questions)** 测试，而非真实问题（38% 仍是真实问题上的报告结果）
- 用户**宁可要明确的"无法回答"也不要自信的错误数字**

诊断：更多 schema 上下文能解释列名，但**不能授权某个团队的定义**；更强的模型也会流畅地解释未授权的含义。

**600 → 300 黄金集 (golden set)**：逐条检查意图与角色、指标与分组、时期与数据、歧义与最终答案；按问题族 (question families) 分组但保留有意义的差异（区域、退货处理、财年日历不同的"月度净销售额"不是重复）。黄金集 = 来自真实工单的 300 个固定问题 + 批准答案 + 评估规则。按**首版预期工作负载**选覆盖，而不是挑系统已能答的（那只描述原型的强项）；记录排除项和覆盖缺口。流程：检查原始证据 → 识别需求 → 归并 → 确立首版负载（可并行）→ 选 300 题 → 记录排除与缺口。

**三种 net_sales 含义（示例）**：交易期口径（扣除本期记录的退货）/ 原销售期口径（退货归属回原销售期）/ 商品团队口径（团队特定排除项）。每种都能生成合法 SQL 和合理数字；`net_sales` 标签选不出来。

BI 团队的约定角色是**策展指标定义 (curate metric definitions)**：维护批准含义、来源、争议升级路径；**不自动**拥有所有财务定义、权限或发布决策的单方面权力。

**指标契约 (metric contract)**：

| 字段 (Field) | 内容 (Content) |
|---|---|
| 业务含义与权威 | 定义、负责的业务 owner、BI 策展人、争议路径 |
| 批准来源 | 权威数据及其版本/as-of 条件 |
| 粒度 (Grain) | 一行源数据代表什么；输出如何分组 |
| 计算 | 聚合规则 (aggregation rules)、排除项、单位、日历、业务时区 (business time zone) |
| 比较 | 批准参考结果与预先确定的容差 (tolerance)，含缺失组/值处理 |

### 工单 T17 / Resolve ticket T17

**Ticket (English)**: "What were net sales last month and closing stock by category in my region?"

缺失输入：授权区域、批准的 net sales 定义、销售粒度、日历与时区、代表期末的库存快照。粒度陷阱：销售事实与更低粒度记录 join 会重复金额；**库存是快照 (snapshot)，把每日余额相加不等于期末库存**。

澄清后的契约：

| 字段 (Field) | 约定值 (Agreed value) |
|---|---|
| 范围 (Scope) | 请求者授权 R17，仅 R17 直营数据 |
| 含义 (Meaning) | 折扣后销售额，不含税、运费、已取消订单；退货按记录的业务日期扣除 |
| 销售粒度 | 一行 = 业务日期 × 区域 × 品类 × 币种；每行聚合一次 |
| 时期 | 请求在 2026 年 10 月 → 9 月 1–30 日，Europe/Paris；[9/1, 10/1) |
| 库存 | S17 中指定的 9 月期末快照；一行 = 快照 × 区域 × 门店 × 品类；按品类跨授权门店求和，**绝不跨日期求和** |
| 数据状态 | 冻结 (frozen)的 S17，无后续修订 |
| 所有权 | 指标 owner 经 BI 策展人批准；BI 维护并把冲突升级给 owner |
| 参考比较 | 恰好一行 C1：净销售 100000 最小货币单位、库存 240 件，**精确匹配**；缺/多/重复品类行即失败 |

```text
Input:  T17 against frozen snapshot S17, requester authorized for R17
Expected output (exactly one row):
category | net_sales_minor_units | closing_stock_units
C1       | 100000                | 240
Result (99999, 240)  -> FAIL (tolerance is 0)
Result (100000, 240) -> PASS (if category and scope also match)
```

看到模型结果后再改退货归属或把容差放宽到 1 来接受 99999 → 破坏可比性 (comparability)；授权的更正需要**版本化契约 (versioned contract)与参考**，然后重新评估。

**协商的首版范围**：销售与库存 (sales and inventory)，约 **40 张策展表 (curated tables)**；BI 策展指标定义；**不确定时 agent 追问或拒答**。表数量减少本身不能证明数据权威或充分。之前所有约束保持；首批用户、具体表、详细策略、运维职责仍待定。

**85% 目标**：300 题黄金集中至少 85% 的结果在定义容差内匹配批准答案 → **0.85 × 300 = 255**。评估前冻结问题、数据快照、参考答案、按指标的比较规则。

结果分类分开记录：匹配 (Matching) / 追问 (Clarification，多轮 (multi-turn)规则下追问后匹配可算完成；仍待回答的不算) / 拒答 (Decline，安全但不算匹配) / 缺失输出 (Missing output) / 错误结果 (Wrong result)。

**错误协议**："Use all sales-related tables, keep synthetic pilot questions, let Gemini choose the most common definition, and count a number or refusal as correct until 85%." —— 开放数据边界、合成问题、流行度代替批准、拒答计入分子改变了承诺。

| 批次 (Batch) | 构成 (Composition) | 匹配率 (Match rate) | 判断 (Assessment) |
|---|---|---|---|
| A | 255 匹配、30 拒答、15 错误 | 255/300 = 85% | 达标，但**本身不足以证明可发布**；错误与拒答仍需检查 |
| B | 240 匹配、60 安全拒答 | 240/300 = 80% | 安全拒答可防害，但不会把匹配率变成 100% |

测验正确选项：255/300 = 85%，达标但不单独证明发布就绪 (release readiness)。发布证据还需覆盖追问与拒答行为、延迟、扫描成本、策略执行；权限违规或严重无依据答案不能被总体百分比豁免。

**交接内容**：约定边界；问题来源（600 → 300，问题族、排除、缺口，T17 作代表）；含义（BI 策展角色、契约字段、T17 契约）；验收（≥255，冻结规则，分类报告）；保留约束；待定决策 + 产生证据的下一步（与 Data Platform 审查现有授权；与用户验证覆盖；把字段与位置方案送隐私审查；带负载估算请求上限决定；获取发布与更正责任的明确接受）。

**追问：已发布了错误数字** → 提议：停止无依据答案；通知负责的客户对接人 (customer counterpart)；保存问题、契约、数据状态、输出；约定更正负责人。在客户接受前都记为"提议的流程"。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "Can a better model guarantee 85%?" | "Not yet. Discovery shows most pilot errors came from three conflicting net-sales definitions, and a stronger model would just interpret an unapproved meaning more fluently. What I can commit to is a measurable target: at least 255 of 300 real-ticket golden questions matching approved answers, with frozen comparison rules — and we report declines and wrong answers separately." | 不能保证；原因是定义冲突；承诺可测目标 |
| "Can we give all 1,200 analysts access?" | "I'd start with the users whose questions the golden set actually covers, in sales and inventory. Hitting 85% on a test set isn't the same as release readiness — we also need latency, scan-cost, and permission evidence. Once those hold, we expand by user group." | 先覆盖内的用户；85%≠就绪 |
| "Walk me through how you'd make ticket T17 assessable." | "I'd pin down the authorized region, the approved net-sales definition including return timing, the sales grain, 'last month' in the business timezone, and which inventory snapshot means 'closing' — stock is a snapshot, so you never sum across dates. Then we freeze the data state and agree an exact expected row before we see any model output." | 区域、定义、粒度、时区、快照、冻结、预先约定参考 |
| "An incorrect number was already published. What now?" | "I'd propose pausing the affected answer type, notifying the responsible customer counterpart, and preserving the question, contract version, data state, and output for diagnosis. Then we agree who owns the correction and how it's communicated — those are proposals until the customer accepts them." | 暂停、通知、保存证据、约定更正负责人 |

---

## 10. CS1 — The System Design Round｜系统设计轮

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/N8kR8ArRZ9m

### 要点 / Key ideas

**Problem (English)**: Turn the discovery agreement — sales and inventory over about 40 curated tables, BI-curated definitions, 85% on 300 real questions, plus access, privacy, residency, latency and cost constraints — into an architecture you can defend, tracing ticket T17 from the user's words to a checked, permitted answer. Include clarification, rejection and failure paths. (Try it first for 20 minutes, then compare: defensible alternative / missing evidence / actual gap.)

**认证的语义契约 (certified semantic contract)**：每个指标 ID 解析为**一个**批准含义和版本；不同批准含义用不同 ID；指定来源、粒度、排除项、单位、日历、时区；**Gemini 不得选择听起来最常见的定义**。未解决的 "fiscal last quarter" 需要批准的财年映射 → 否则定向追问或说明暂时无法回答。**微调 (fine-tuning) 不能授权会计定义。**

**上下文包 (context package)**：认证契约 + 相关批准 schema 描述（含粒度、关系、批准用途，可 embedding 检索）+ 已验证的问题-SQL 示例（服从契约）。T17 只检索批准的销售与期末库存来源 + 一个"分开聚合"示例。不要把 4,000 张表描述塞进 prompt。**单 agent**（有界检索 + SQL 生成）；应用代码拥有可信范围、准入、执行、发布。拆成多 agent 增加协调却不解决核心语义问题。检索相关性不授予访问；示例里的区域谓词不授予区域权限。

<svg viewBox="0 0 800 420" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect width="800" height="420" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">CS1: Retail Text-to-SQL Agent｜零售 Text-to-SQL 架构 (T17 path)</text>
  <rect x="15" y="60" width="100" height="56" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="65" y="84" font-size="13" text-anchor="middle">Analyst</text>
  <text x="65" y="102" font-size="12" text-anchor="middle">分析师 (R17)</text>
  <rect x="140" y="45" width="640" height="200" rx="10" fill="#f8fbff" stroke="#4285f4" stroke-dasharray="6,4"/>
  <text x="460" y="62" font-size="12" text-anchor="middle" fill="#4285f4">Application code owns scope, admission, execution, release｜应用代码掌握权限与发布</text>
  <rect x="155" y="72" width="120" height="58" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="215" y="96" font-size="13" text-anchor="middle">AuthN + entitle</text>
  <text x="215" y="114" font-size="12" text-anchor="middle">认证+绑定 R17</text>
  <rect x="295" y="72" width="140" height="58" rx="8" fill="#e6f4ea" stroke="#34a853"/>
  <text x="365" y="94" font-size="13" text-anchor="middle">Bounded retrieval</text>
  <text x="365" y="112" font-size="11" text-anchor="middle">contract+schema+examples</text>
  <rect x="455" y="72" width="120" height="58" rx="8" fill="#fef7e0" stroke="#fbbc04"/>
  <text x="515" y="96" font-size="13" text-anchor="middle">Gemini</text>
  <text x="515" y="114" font-size="12" text-anchor="middle">SQL 提议</text>
  <rect x="595" y="72" width="170" height="58" rx="8" fill="#fce8e6" stroke="#ea4335"/>
  <text x="680" y="94" font-size="13" text-anchor="middle">Policy check + dry run</text>
  <text x="680" y="112" font-size="11" text-anchor="middle">只读形式; estimate ≤ B ?</text>
  <rect x="595" y="160" width="170" height="70" rx="8" fill="#fce8e6" stroke="#ea4335"/>
  <text x="680" y="182" font-size="13" text-anchor="middle">Execute</text>
  <text x="680" y="200" font-size="11" text-anchor="middle">maximum_bytes_billed = B</text>
  <text x="680" y="218" font-size="11" text-anchor="middle">user-bound principal</text>
  <rect x="380" y="160" width="190" height="70" rx="8" fill="#fce8e6" stroke="#ea4335"/>
  <text x="475" y="182" font-size="13" text-anchor="middle">Result checks</text>
  <text x="475" y="200" font-size="11" text-anchor="middle">execution/shape/meaning/ref</text>
  <text x="475" y="218" font-size="11" text-anchor="middle">结果校验</text>
  <rect x="155" y="160" width="200" height="70" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="255" y="182" font-size="13" text-anchor="middle">Transparent answer</text>
  <text x="255" y="200" font-size="11" text-anchor="middle">number+defs+version+SQL</text>
  <text x="255" y="218" font-size="11" text-anchor="middle">或追问/拒答 clarify/decline</text>
  <line x1="115" y1="88" x2="153" y2="100" stroke="#555" stroke-width="1.5"/>
  <line x1="275" y1="101" x2="293" y2="101" stroke="#555" stroke-width="1.5"/>
  <line x1="435" y1="101" x2="453" y2="101" stroke="#555" stroke-width="1.5"/>
  <line x1="575" y1="101" x2="593" y2="101" stroke="#555" stroke-width="1.5"/>
  <line x1="680" y1="130" x2="680" y2="158" stroke="#555" stroke-width="1.5"/>
  <line x1="595" y1="195" x2="572" y2="195" stroke="#555" stroke-width="1.5"/>
  <line x1="380" y1="195" x2="357" y2="195" stroke="#555" stroke-width="1.5"/>
  <line x1="155" y1="200" x2="80" y2="118" stroke="#ea4335" stroke-width="1.5" stroke-dasharray="4,3"/>
  <rect x="595" y="275" width="185" height="74" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="687" y="297" font-size="13" text-anchor="middle">BigQuery</text>
  <text x="687" y="315" font-size="11" text-anchor="middle">~40 curated views</text>
  <text x="687" y="333" font-size="11" text-anchor="middle">row-level policies 行级策略</text>
  <line x1="680" y1="230" x2="687" y2="273" stroke="#555" stroke-width="1.5"/>
  <rect x="300" y="275" width="270" height="74" rx="8" fill="#ede7f6" stroke="#7e57c2"/>
  <text x="435" y="297" font-size="13" text-anchor="middle">Semantic layer (BI-curated)</text>
  <text x="435" y="315" font-size="11" text-anchor="middle">metric IDs + versions; LookML if Looker</text>
  <text x="435" y="333" font-size="11" text-anchor="middle">语义层：一个 ID 一个含义</text>
  <line x1="400" y1="275" x2="370" y2="132" stroke="#7e57c2" stroke-width="1.2" stroke-dasharray="4,3"/>
  <rect x="15" y="275" width="265" height="74" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="147" y="297" font-size="13" text-anchor="middle">Audit trail + eval harness</text>
  <text x="147" y="315" font-size="11" text-anchor="middle">300 golden Qs, typed comparison</text>
  <text x="147" y="333" font-size="11" text-anchor="middle">审计 + 回归评估 (≥255)</text>
  <text x="400" y="380" font-size="12" text-anchor="middle" fill="#555">Three independent failure classes: unauthorized SQL blocked · over-budget SQL blocked · permitted+cheap SQL can still be WRONG</text>
  <text x="400" y="400" font-size="12" text-anchor="middle" fill="#555">三类独立失败：越权被拦 · 超预算被拦 · 合法且便宜的 SQL 仍可能算错</text>
</svg>

### 分开聚合 / Compose separate aggregates

本地 fixture：销售 2 行（9/10 R17 C1 60000；9/20 R17 C1 40000）；库存 2 行（S17_CLOSE 门店 A 100、门店 B 140）。

```text
Input tables:
sales_s17: (2026-09-10, R17, C1, S17_currency, 60000), (2026-09-20, R17, C1, S17_currency, 40000)
stock_s17: (S17_CLOSE, R17, A, C1, 100), (S17_CLOSE, R17, B, C1, 140)
Expected output: (C1, R17, S17_currency, 100000, 240)
Raw-join output: (C1, R17, S17_currency, 200000, 480)   -- fan-out doubles both measures
```

错误写法（先 join 原始事实再求和）——每条销售匹配两家门店，4 行 join 结果使两个度量都翻倍，即使每行都有权限、查询也便宜：

```sql
-- WRONG: joins raw facts before aggregating (fan-out)
SELECT s.category, SUM(s.net_sales_minor), SUM(i.stock_units)
FROM sales_s17 AS s JOIN stock_s17 AS i
  ON s.region = i.region AND s.category = i.category
GROUP BY s.category;
```

正确写法：各自按批准粒度聚合，再组合：

```sql
WITH sales AS (
  SELECT region, category, currency, SUM(net_sales_minor) AS net_sales_minor
  FROM sales_s17
  WHERE region = :region AND business_date >= :start AND business_date < :end
  GROUP BY region, category, currency
), stock AS (
  SELECT region, category, SUM(stock_units) AS closing_stock_units
  FROM stock_s17
  WHERE region = :region AND snapshot = :closing_snapshot
  GROUP BY region, category
)
SELECT s.category, s.region, s.currency, s.net_sales_minor, i.closing_stock_units
FROM sales AS s JOIN stock AS i
  ON s.region = i.region AND s.category = i.category;
```

inner join 对完整的 T17 组足够；其他契约若需保留缺失组，需显式的缺失组规则和不同组合方式。

课程的本地检查（sqlite，Python）要点：`matches_t17` 要求元数据完全一致、恰好一行期望结果、度量为 int 类型（拒绝 fan-out、99999/240、字符串 "100000"、空输出）；`admit` 存根 (stub)演示准入分支：

```python
def admit(entitled, estimate, byte_limit, execute):
    # Local control-flow stub: no authentication or BigQuery integration.
    if not entitled:
        return "DENIED"
    if byte_limit is None:
        return "BLOCKED_CAP_UNAPPROVED"
    if estimate > byte_limit:
        return "OVER_LIMIT"
    execute(maximum_bytes_billed=byte_limit)
    return "DISPATCHED"
```

本地程序只检查粒度和冻结结果契约；**不能**证明真实 BigQuery 权限、dry run、Gemini 生成质量或其余 299 题。

### 执行权限的五个边界 / Bind execution authority

危险捷径：全部 schema 进 prompt、让 Gemini 按区域过滤、用高权限共享服务账号 (service account)执行 → Gemini 漏掉过滤就会泄露请求者本无法直接获取的数据（混淆代理人问题 confused deputy）。

| 边界 (Boundary) | 做法 (Mechanism) |
|---|---|
| 认证 (Authenticate) | 应用认证机制验证请求者 |
| 绑定权限 (Bind entitlements) | 从可信应用上下文解析当前允许的区域和直营/加盟范围 |
| 选择凭证 (Select credentials) | 选批准的执行身份安排 |
| 限制表面 (Restrict surfaces) | 只允许对批准数据集和策展视图的只读查询，不给底层表宽权限 |
| 数据库策略 (Enforce database policy) | 在实际生效主体下应用并测试 BigQuery **行级访问策略 (row-level access policies)** 和**授权视图 (authorized views)**；权限必须扛得住错误或恶意生成的 SQL |

可辩护方案：用**绑定用户的主体 (user-bound principal)** 执行，其授权和行策略强制该用户范围；工作负载身份 (workload identity)方案需单独审查主体→范围设计。两者都需凭证选择、授权和**负面测试 (negative tests)**（用所选凭证直接尝试越权查询）才算被证明。越权区域请求要在受保护数据/schema 到达 Gemini 之前拒绝；跨区聚合在批准前不可用——区域总数仍是数据访问。

### 有界作业准入 / Admit bounded jobs（符号上限 B）

1. **查询策略检查**：解析 SQL，检查引用来源与操作，只允许批准的只读形式与数据表面（关键字搜索不够）
2. **Dry run**：在预期执行上下文下检查语法并估算扫描字节 (bytes scanned)
3. **准入检查**：估算 > B 拒绝；B 未批准/缺失 → 生产执行保持阻塞
4. **执行**：每个准入作业都带 `maximum_bytes_billed=B`（硬上限 (hard cap)，因为 dry run 估算不够），保存 job 身份与完成证据

50 TB 估算超过 B → 拒绝；没有批准的 B → 阻塞等待决定，不编阈值也不跑无上限探索查询。

### 结果校验与透明答案 / Check results, release evidence

完成 ≠ 可发布。检查：执行（作业成功，执行的 SQL 和生效范围与准入请求一致）、形状（列、类型、币种、品类分组、唯一性）、含义（时期、数据状态、单位、语义不变量）、参考（冻结 T17 精确匹配）。

**三类独立失败**：越权 SQL 被拦；超预算 SQL 被拦；**合法且便宜的 SQL 仍可能给出错误答案**。

用户可见答案示例（英文）：
> "For category C1 in R17 corporate scope, September 2026 net sales were 100000 minor currency units in S17's single currency. Closing stock at the designated September-close snapshot was 240 whole units. Sales use the approved post-discount amount, exclude tax, shipping, and cancelled sales, and deduct returns on their recorded business date."

附带：认证定义的实际版本号、S17 数据状态、Europe/Paris 时段边界、**实际执行的 SQL 及绑定参数 (bound parameters)**（区别于生成的提议）。访问受控审计轨迹 (audit trail)：请求身份、生效执行权限、契约与来源版本、检索上下文引用、策略与计费准入决策、job 身份与结果（本地 fixture 不要伪造 job ID）。隐私与 EU 位置审查要覆盖模型上下文、检索示例、结果、缓存、日志——**EU 存储不等于处理位置已解决**。

### 回归 300 题 / Regress all 300

比较**类型化、有范围的结果**而不是 SQL 文本（不同 SQL 可以等价；相似 SQL 在错误数据状态上会失败）。目标 255；分类报告；权限失败等关键安全失败是独立发布阻断项。每次 prompt/schema 变更都跑回归；定义和示例变更需版本控制 (version control)；保留原始基线防止分母 (denominator)悄悄变化。每次运行保存用例与契约版本、数据状态、执行查询、结果、比较结果、诊断失败阶段。

### 托管方案评估 / Evaluate managed capability

面试官："Google already sells this. Why not use the Conversational Analytics API?" —— **先评估它**。Conversational Analytics API 于 2026-06-23 对 BigQuery 和 Looker GA (general availability)；BigQuery 版面向自定义应用，Looker 版通过 LookML 提供一致指标；Looker data agents 可用 **golden queries** 作结构化上下文。

用同一验收契约评估：质量与权限（同样 300 题、比较规则、权限测试）；运维（延迟负载、扫描上限、失败行为）；数据处理（隐私、处理位置、保留、透明答案证据）；客户负担（集成、维护、事故诊断、交接）。如果客户用 Looker，就在 **LookML** 里解决冲突的 net sales 定义，而不是在 prompt 里维护矛盾定义（但是否有 Looker 是问题而非假设）。**优先托管能力 + 测量暴露未满足需求时加窄的自定义包装 (managed-first with narrow custom wrappers)**。"Custom is more flexible" 不是证据。

### 按域扩展 / Expand domain by domain

被标记的答案交给授权的 BI 与领域审查，只有审查过、版本化的标签进入评估集。从约 40 到约 4,000 张表逐域扩展：批准定义、来源映射、支持的问题族 → 建立批准数据表面并独立测试权限 → 加入 schema 描述和验证示例到有界检索 → 评估新负载、安全边界、延迟、成本 → 获得明确验收与运维归属。这是**目录与治理 (governance)扩展**，不需要把数仓暴露给 Gemini，也不需要更宽凭证。

**各种变化条件的处理**：

| 条件 (Condition) | 结果 (Outcome) | 机制 (Mechanism) |
|---|---|---|
| T17 正常 | 执行 (Execute) | 分开聚合 + 精确比较 |
| 原始 join → 200000/480 | 拒绝发布 | 结果校验失败 |
| 99999/240 | 拒绝发布 | 容差 0 |
| 越权区域请求 | 拒绝 (Decline/deny) | 推理前拒绝 + 行级策略 |
| dry run 50 TB | 拒绝 (Over limit) | 估算 > B |
| B 未批准 | 保持阻塞 (Blocked) | 等待上限决定 |
| "fiscal last quarter" 无财年映射 | 追问或拒答 (Clarify/decline) | 语义契约缺失 |

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "Walk me through your architecture." | "One agent with bounded retrieval proposes SQL; everything that carries authority lives in application code and BigQuery. The app authenticates the user and binds their region, retrieval pulls the certified metric contract and a few verified examples, Gemini proposes SQL, then we policy-check it, dry-run it against the byte limit, execute under a user-bound principal with row-level policies and maximum_bytes_billed, and validate the result before releasing a transparent answer with the definition version and executed SQL." | 单 agent 提议；应用和 BigQuery 掌权；校验后透明发布 |
| "How do you stop the model from leaking another region's data?" | "The model never enforces permissions. I deny unauthorized requests before protected schema reaches Gemini, and execution runs under a principal whose grants and row-level policies only cover the user's region — so even malicious generated SQL can't return other rows. I'd prove that with negative tests that try direct cross-region queries under the chosen credentials." | 推理前拒绝；行级策略；负面测试 |
| "The query is authorized and cheap — is it right?" | "Not necessarily. Joining raw sales to store-level stock fans out and doubles both measures, even though every row is permitted. I aggregate each source at its approved grain first, then join the aggregates, and I check the typed result against the frozen reference before release." | 合法便宜≠正确；先聚合后 join |
| "Why not just use the Conversational Analytics API?" | "I'd evaluate it first, against the same bar: the 300 questions, permission tests, latency, scan cost, and data-location checks. If the retailer has Looker, LookML is the right place to settle the net-sales definitions. I'd go managed-first and only add narrow custom wrappers where measurements show a gap." | 托管优先，同一标准评估 |
| "What if the scan cap still isn't decided?" | "Then production execution stays blocked. I can estimate workload costs to help the customer pick a number, but I won't invent a threshold or run uncapped queries." | 上限未定就阻塞 |

---

## 11. CS1 — The Googleyness Round｜Googleyness 轮（零售案例三个冲突）

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/39mwXKZlrq9

### 要点 / Key ideas

三个排练场景（**是排练材料，不要当成个人经历讲**）。强回答五要素：**干系人目标 (stakeholder's objective)、实质风险 (material risk)、具体提议 (concrete proposal)、你的权限边界 (authority boundary)、产生证据的下一步 (evidence-producing next step)**。

**场景一：试点准确率来自合成测试 (synthetic tests)，提出者就在会议室**

- 弱回答："The pilot team tested the wrong things, so their numbers are meaningless." —— 合成测试在受控条件下有价值；问题是**推断**（不能证明真实问题表现）。
- 顺序：**先公开纠正解读**（只约私下聊会让误导结论留在现场）→ 邀请原团队提供背景 → 私下联合调查。
- 调查：问题（哪些合成/真实/排除）、数据状态（快照、修订、权限）、批准答案（谁接受业务含义与参考）、比较规则（追问、拒答、缺失、容差）、记录的结果。
- 如果你自己之前重复过这个说法就承认："I also repeated that claim without checking the test population." 没重复过就**不要编造忏悔**来显得谦虚。
- 可以拥有：准确的当前沟通、保存证据、协调诊断、跟踪约定修复。不能：接受未记录的历史选择为自己的，或保证下一个分数。
- 行动记录：提议负责人（你协调更正简报和证据审查；试点团队提供评估记录）/ 需要的权限（BI 与领域审查者接受含义与标签；客户决策者指定就绪权限）/ 下一步（取回评估工件 (artifacts)）/ 确认证据（更正的简报、来源记录、保留的评估结果）/ 未决（历史评估可比性与当前性能）。

**场景二：BI 负责人因担心被取代而暗中扣住指标定义**

- 弱回答："I'll get the definitions from another team. Don't worry, nobody in BI will lose their job." —— 绕过 BI 会造成竞争的语义权威；人员保证超出工程权限。
- 方向：让 BI 的专业成为**必需** —— 正式拥有**认证指标目录 (certified-metric catalog)**。
- 实质化所有权：目录维护（BI 维护并版本化定义和验证示例）；含义争议（BI 把冲突路由给领域决策者，而非单方面决定所有财务含义）；答案审查（参与审查被标记答案和参考标签）；运行条件（客户决策者约定容量、访问、变更审批、升级）。**目录所有权不自动转移访问策略或发布权限**。

**场景三：VP 要两周后给 CEO 演示，但 85% 还没达到**

- 弱回答："We'll show our best answers so the CEO can see we're ready." —— 精选示例能成功但大部分负载仍失败；演示让能力可见，代表性评估回答的是另一个问题。
- 演示边界：支持范围（销售与库存、约 40 张表；精选问题标明是精选）；数据边界保持；**没有批准的字节上限 (byte cap) = 不在生产执行查询**，用本地 fixture 或批准的演示环境并准确标注；非预期问题 → 定向追问或透明的无法回答；就绪声明保持可见。
- 测验：VP 要去掉局限说明 → 正确选项：**提供更短但准确的简报**（精选授权问题、单独标注证据、保留执行限制，声明代表性性能未建立、255/300 是目标不是已达成）。不选"拒绝任何演示直到 255/300"，也不选"把精选成功率报成演示就绪"。
- 不要用历史 38%、精选演示成功率或 T17 本地机制填补"当前测量"空白。

**被挑战时深化决策而不是加事实**：

| 挑战 (Challenge) | 回应要点 (Response) |
|---|---|
| "Why not avoid the public correction?" | 听到说法的每个人都需要证据区分；详细来源可以之后调查 |
| "Why let BI slow delivery?" | 被接受的业务含义是答案正确性的一部分；在依赖解决期间提供受支持范围和资源选项 |
| "Why not promise 85% by the demo?" | 没有当前测量或保证依据；承诺评估工作和透明报告 |

影响力不要求每个人都舒服；需要真实的边界和推进合理目标的提议。未达成一致是诚实的可能结果。

### 面试怎么说 / How to say it in the interview — 题库（每题 STAR 风格英文模型答案）

**Q1. "You discover the pilot's accuracy claim used synthetic data, and the people who made it are in the room. What do you do?"**
> **Situation/Task:** "The room was about to treat a synthetic-test result as evidence of real-question performance, and my job was to make sure the decision was made on accurate evidence without blaming anyone.
> **Action:** I'd correct it right there: 'The claim we're discussing came from synthetic testing. That doesn't establish performance on analysts' real questions; our record also shows about 38% on real questions, and we need to reconcile the assessments before comparing.' Then I'd invite the pilot team in: 'Could you help identify the question set, data state, and comparison rules behind that claim? I'd like to preserve what those tests did establish.' I'd commit to coordinating a joint evidence review with the pilot and BI teams, and I wouldn't announce any new accuracy number until it's done.
> **Result:** The audience leaves with the right distinction, the pilot team's work is preserved, and there's a concrete review with an owner — although whether the team agrees is still open."

中文：当场纠正解读，不归咎动机；邀请原团队；协调联合审查；不报新数字。

**Q1 follow-up. "You're undermining the pilot team."**
> "I understand why a correction in this room could feel that way. I'm separating the claims so everyone can use your work accurately — I'm not assigning motives or dismissing the pilot. Let's review the records together and credit what can be reused, but the briefing still needs to distinguish synthetic testing from real-workload evidence."

中文：承认感受，但不撤回纠正。

**Q2. "The BI lead is quietly withholding metric definitions because they see the agent as a threat."**
> **Situation/Task:** "The design depends on BI-curated definitions — the agent can't authorize its own meaning of net sales — so I needed BI's participation, not a workaround.
> **Action:** I'd talk to the BI lead privately: 'I understand this can look like it reduces BI's role. The scoped design actually depends on your definitions. I'd like to propose formalizing BI as owner of the certified-metric catalog, with visible credit and an agreed review workflow.' I'd offer to take that proposal to the customer decision owners and help size the capacity it needs, and I'd be clear that I can't promise staffing outcomes or assign their team work without agreement.
> **Result:** The concern becomes discussable and tied to real work the system needs; the BI lead is recorded as proposed catalog owner pending customer acceptance."

中文：理解担忧；让 BI 成为必需的指标目录所有者；不做人员保证；提交客户决策者。

**Q2 follow-up. "BI still refuses. What now?"**
> "I'd ask which part — responsibility, capacity, or recognition — is still unacceptable, and bring concrete options to the customer decision owners: resourcing the review, shrinking scope to meanings already certified, or delaying unsupported question families. Until a meaning is certified, it stays unsupported. I'd escalate the dependency and its delivery impact without accusing BI or pulling a definition from somewhere else."

中文：问清卡点，带选项升级，未认证含义保持不支持，不绕过 BI。

**Q3. "The VP wants a CEO demo in two weeks, before you've reached 85%."**
> **Situation/Task:** "The VP's goal — showing the CEO real progress — is legitimate, but we had no current representative measurement, and the risk was the CEO reading a curated demo as launch readiness.
> **Action:** I'd agree to a bounded demo: a small, explicitly selected set of questions that behave reliably under approved conditions, with current measured performance shown separately — numerator, denominator, workload. Since we don't have a defensible current measurement, I'd say representative performance isn't established yet, that 255 of 300 is the target, and that production execution stays blocked until the byte cap is approved, so the demo runs in a labeled demo environment. Unscripted questions get a clarification or an honest 'can't answer yet.'
> **Result:** The CEO sees real capability with an accurate frame, and the release decision stays tied to evidence."

中文：同意有边界的演示；精选问题标明精选；单独报告当前测量；保留执行限制。

**Q3 follow-up. "Leave the limitations out; keep it positive."**
> "I can make the briefing shorter, but I can't present selected examples as representative performance or drop material execution restrictions. I'd offer a narrower demo with one clear sentence on what has and hasn't been measured. If production execution is still unapproved, it stays blocked and I'll label the demo environment accurately."

中文：可以更短，但不能隐瞒实质限制。

**Q4. "Why not promise 85% by the demo?"**
> "Because nothing in our record supports that guarantee yet. What I can commit to is running the fixed 300 real-ticket questions under frozen rules and reporting matches, declines, and wrong answers transparently, so the sponsor knows exactly where we stand."

中文：没依据就不承诺；承诺评估与透明报告。

---

## 12. CS1 — Debriefing the Case Study｜案例复盘

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/NEzwpq0nr3m

### 要点 / Key ideas

好的复盘 (debrief)让每个自信的句子都能对应到记录。产出：**两个可执行的修复 + 可迁移的决策规则**，而不是更流利的零售架构图。保留原始推理，不要被修订抹掉。

**四个证据标签 (Four evidence labels)**：

| 标签 (Label) | 含义 (Meaning) |
|---|---|
| Said（说过） | 回答或录音里出现的话 |
| Proposed（提议） | 为未来行动描述的测试、设计或协议 |
| Tested（测试过） | 有保留输入、条件、观察的执行 |
| Unproven（未证明） | 缺少必要观察或接受的结论 |

例："Without an approved byte cap, keep production query execution blocked" → 支持"存在合理的准入规则提议"；不支持"区域访问由数据库强制"。缺失的尝试写 "not demonstrated"，并把获取它列为下一步。

**各轮评估（练习用，非官方）**：

| 轮次 (Round) | 检查什么 (Inspect) | 追问 (Adverse follow-up) |
|---|---|---|
| Recruiter | 动机和所有权主张；个人 vs 团队 | "Which outcome did you personally own?" |
| Coding | 实现正确性、测试、边界推理 | "Which failing case did you find before changing the implementation?" |
| Vibe coding | 澄清、显式假设、适应、诊断（需保留早期状态） | "What changed when the requirement changed?" |
| System design | 范围、语义、权限、评估、托管对比、运维权衡 | "What prevents an unauthorized query if the model ignores its instructions?" |
| Googleyness | 真实纠正、协作、有界所有权 | "What did you do when the stakeholder refused?" |

评级：supported in this rehearsal / partially demonstrated / not demonstrated（要指明能力）。HC 结果不在评级范围内。

**审核发布声明**："T17 gives 100000 and 240, so the agent has reached 85%; Gemini filters users to their regions, and BI owns the catalog, so we can launch and expand to all 4000 tables." —— 诊断：**就绪度膨胀 (readiness inflation)**。

| 子句 (Clause) | 问题 (Problem) | 替换 (Replacement) |
|---|---|---|
| "T17 gives 100000 and 240" | 记录中没有观察到的 T17 运行 | "The T17 contract expects those values under its complete comparison rules." |
| "so the agent has reached 85%" | 一个本地用例 ≠ 300 题中的 255 | "Representative result-match performance remains unestablished." |
| "Gemini filters users to their regions" | 模型指令不是数据库授权证据 | "Trusted identity, selected credentials, restricted query surfaces, and database policy must enforce regional authority." |
| "BI owns the catalog" | 只是提议 | "BI catalog ownership is proposed and awaits accepted responsibilities, capacity, and workflow." |
| "so we can launch and expand" | 无发布验收；B 未定；无 p95 观测；扩展需逐域门禁 (gate) | 逐域门禁扩展；无 B 保持阻塞 |

三种证据标准：批准的设计理由 / 挑战下展示的推理 / 已验证的生产检查与被接受的客户协议。

**六个常见错误 (Six recognizable mistakes)**：

| 错误 (Mistake) | 症状 (Symptom) | 修复 (Repair) |
|---|---|---|
| 先设计后界定范围 (Designing before scoping) | "I'll connect the whole warehouse." | 先约定域、问题族、用户、批准数据 |
| 忽略托管产品 (Ignoring the managed product) | 只列自定义编排/检索/SQL 生成 | 用同一契约对比 Conversational Analytics API |
| 按 SQL 文本评分 (Grading SQL text) | "Every generated query matched the reference SQL." | 评估批准的结果与语义 |
| 依赖模型做安全 (Using model security) | "The system prompt prevents cross-region access." | 身份→凭证→数据库强制链 + 直接查询拒绝测试 |
| 强制回答 (Forcing an answer) | "The agent always returns a number." | 显式追问或拒答 |
| 过早承诺准确率 (Promising accuracy early) | "We guarantee 85%." | 承诺评估并报告观测结果 |

**诚实计算拒答**：Batch A（255+30+15）= 85% 达标，但 15 个错误仍需检查（严重财务错误或关键策略失败可独立阻断发布）；Batch B（240+60）= 80%，差 15 个；240/(300−60) = 100% **改变了约定分母 (denominator)**并掩盖了未支持覆盖。

**五个可迁移原则（带机制）**：

| 原则 (Principle) | 为什么有效 (Mechanism) | 零售中的具体选择（不一定迁移）(Contingent choice) |
|---|---|---|
| 先查托管能力 (Check managed capability first) | 减少自定义行为和运维工作 | 用验收契约评估 Conversational Analytics API |
| 先定语义再调优 (Define semantics before tuning) | 批准含义让正确性可评估，防止在冲突定义间流畅地选择 | 认证的销售/期末库存契约，T17 精确整数比较 |
| 评估真实工作 (Evaluate real work) | 代表性问题暴露演示隐藏的歧义与失败 | 300 道真实工单题 |
| 强制数据权限 (Enforce data authority) | 即使生成错误或被绕过，数据库也约束执行 | BigQuery 凭证 + 行级策略 |
| 让拒答成为功能 (Make declining a feature) | 安全的不确定性防止无依据答案冒充完成 | 追问/拒绝/转人工 (human handoff)规则 |

单 agent、约 40 张表、S17、15 秒 p95、符号 B 属于这个客户；迁移的是**做决定的理由和能推翻它的证据**。

**让 BI 所有权可运行**：五项持续责任——接受指标变更、审查被标记答案与新评估标签、更新权限规则、响应已发布的错误数字、决定发布或扩展。每项记录：提议参与者、已接受的负责方、所需权限、运行流程、确认证据。变更 net sales 含义 → 新版本契约、受影响参考答案与示例、更新测试、重新评估；看到失败后悄悄替换参考会破坏可比性。

**两个优先修复**：
1. **权限主张**："What if I execute the forbidden SQL directly?" → 在选定凭证下直接执行越权查询；通过条件：保留受保护访问被拒且允许访问仍正常的证据。
2. **就绪推断**："Would you launch tomorrow?" → 分开陈述本地预期结果、代表性评估、发布门禁；生产验收需要实际评估、控制、批准的 B、被接受的决策责任。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "Would you launch tomorrow?" | "No. T17 defines an exact expected result, but a single case doesn't tell us about the other 299 questions, and we haven't run the fixed 300-question evaluation yet. We also don't have an approved scan cap, latency measurements against the 15-second p95, enforcement tests under the real credentials, or accepted release ownership. I'd keep production execution blocked and expand domain by domain once those gates pass." | 单例≠代表性；列出缺失门禁 |
| "What if I execute the forbidden SQL directly?" | "That's exactly the test I'd run. Bypassing the model entirely, I'd issue the cross-region query under the effective principal and expect it to be denied by grants and row-level policies, while a permitted query still works. If the forbidden query succeeds, that's a release blocker, no matter how often the prompt produces the right filter." | 绕过模型直接测；成功即阻断 |
| "Batch B has 60 safe declines and 240 correct — isn't that 100% on what it answered?" | "No — that changes the agreed denominator. Batch B is 240 of 300, or 80%, so it misses the 255 target by 15. The declines may well be the right behavior, but they're lost coverage we need to report and examine, not successes." | 不改分母；拒答单独报告 |
| "What did you learn from this case that transfers?" | "Five things: check the managed product first, settle semantics before tuning, evaluate on real work, enforce data authority in the database rather than the prompt, and treat declining as a feature. The specific choices — one agent, 40 tables, BigQuery row policies — belong to this customer; what I carry forward is the reason for each and the evidence that would reverse it." | 五原则；迁移理由而非具体选择 |

---

# Case Study 2: Telecom Customer-Service Agents under EU AI Rules｜案例二：欧盟监管下的电信客服 Agent

## 13. CS2 — The Case Study｜案例简报

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/m7wp9L6p51E

### 要点 / Key ideas

**Problem (English) — the brief**:
- **Customer**: a fictional telecom in four EU countries; 18 million subscribers; about **2.5 million support contacts/month** across chat and voice, in four languages.
- **Current state**: an FAQ chatbot that cannot take account actions; only **22%** of contacts are fully handled without a human. Customer data lives in an older CRM and a **slow, rate-limited billing system**.
- **Mandate**: raise self-service resolution from **22% to 45% within six months without lowering customer satisfaction**.
- **Constraints**: verified identity before any account action; tell customers they're talking to AI; preserve access to a human (incl. decisions that significantly affect someone); data minimization; customer data stays in the EU; voice replies ~**1.5 s**; four languages by full rollout; German works council must be consulted for technology that monitors employees.
- **Stakeholders**: VP of Customer Care (sponsor, measured on cost per contact); DPO (reviews data use); Head of Contact Center (runs human agents); IT architecture lead (owns CRM and billing integrations); Retention team lead (wants offers pushed to customers trying to cancel). Plus counsel and the German works council.

**自助解决 (self-service resolution)** = 在约定测量定义下客户问题**真正被解决**且无人工协助。现有 "fully handled" 说法需要审视才能作为可比基线。

**换算请求的变化（以联系次数为分母，不是订户）**：

| 量 (Quantity) | 计算 (Calculation) | 值 (Value) |
|---|---|---|
| 基线 (Baseline) | 0.22 × 2,500,000 | 550,000 次/月 |
| 目标 (Target) | 0.45 × 2,500,000 | 1,125,000 次/月 |
| 新增 (Additional) | 1,125,000 − 550,000 | **575,000 次/月** |
| 百分点变化 | 45% − 22% | 23 个百分点 (percentage points) |

这是**月度目标状态**，不是六个月累计（×6 是错的）；联系次数 ≠ 唯一订户；不证明可行性、节省或裁员。测验正确选项：550,000 / 1,125,000 / 575,000 / 23 pp。

**三种客户结果**：

<svg viewBox="0 0 740 250" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect width="740" height="250" fill="#fff"/>
  <text x="370" y="22" font-size="14" text-anchor="middle" font-weight="bold">Three customer outcomes｜三种客户结果</text>
  <rect x="20" y="100" width="130" height="56" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="85" y="124" font-size="13" text-anchor="middle">Customer contact</text>
  <text x="85" y="142" font-size="12" text-anchor="middle">客户联系</text>
  <rect x="230" y="40" width="210" height="56" rx="8" fill="#e6f4ea" stroke="#34a853"/>
  <text x="335" y="63" font-size="13" text-anchor="middle">Safe resolution</text>
  <text x="335" y="81" font-size="12" text-anchor="middle">安全解决 → counts 计入</text>
  <rect x="230" y="110" width="210" height="56" rx="8" fill="#fce8e6" stroke="#ea4335"/>
  <text x="335" y="133" font-size="13" text-anchor="middle">Unresolved exit</text>
  <text x="335" y="151" font-size="12" text-anchor="middle">放弃离开 → NOT resolved</text>
  <rect x="230" y="180" width="210" height="56" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="335" y="203" font-size="13" text-anchor="middle">Successful human access</text>
  <text x="335" y="221" font-size="12" text-anchor="middle">转人工成功 → valid, not self-service</text>
  <line x1="150" y1="120" x2="228" y2="70" stroke="#555" stroke-width="1.5"/>
  <line x1="150" y1="128" x2="228" y2="138" stroke="#555" stroke-width="1.5"/>
  <line x1="150" y1="136" x2="228" y2="205" stroke="#555" stroke-width="1.5"/>
  <text x="460" y="66" font-size="12" fill="#34a853">✔ meets agreed rule + verified authority</text>
  <text x="460" y="136" font-size="12" fill="#ea4335">✘ looks "contained" — rewards abandonment</text>
  <text x="460" y="206" font-size="12" fill="#4285f4">✔ good service; penalizing it obstructs help</text>
</svg>

**围堵率 (containment)** 只衡量交互是否没转人工。把放弃算作成功会奖励放弃；惩罚所有转人工会鼓励系统阻挠需要人工的客户。课程明确把"测量 containment"和"让人工难以触达"列为错误。满意度和账户安全与解决率分开观察：高自动化率不能抵消一次越权账户变更。

**约束先于组件选择**：账户权限（对话中声称不是权限证据）、诚实交互、人工服务、个人数据（最小化 + EU 驻留）、语音约 1.5 s、四种语言（**完全上线时**，不要求同时上线）、依赖（旧 CRM 与限速 (rate-limited)账单系统）。账单调用耗时与语音回复时间定义都未知 → 列为调研问题，**不要假设快模型能解决延迟**。

**监管时间线（课程设定，2026-10 视角；非法律建议，由客户法务与 DPO (Data Protection Officer) 解释）**：

| 日期 (Date) | 事件 (Event) |
|---|---|
| 2026-06-16 | 欧洲议会通过 Digital Omnibus |
| 2026-06-29 | 理事会批准 |
| 2026-08-02 | **Article 50 透明度义务**（告知用户在与 chatbot 交互）生效 |
| 2027-12-02 | EU AI Act **高风险 (high-risk)** 义务延后日期 |

在 2026-10-29，透明度义务**已生效**；高风险日期延后**不能**作为推迟 AI 披露 (disclosure)、隐私和账户安全工作的理由。每个日期要绑定到其主体。

**审核捷径说法**："We will reach 45% by reducing transfers and keeping customers in the bot. Because it is customer service rather than credit scoring, we can defer compliance until December 2027. The DPO can approve the rest."——拆成八个独立命题：

| 命题 (Proposition) | 缺失证据 (Missing evidence) | 参与者 (Participants) |
|---|---|---|
| 真正解决 (Actual resolution) | 解决的操作定义；问题被解决而非放弃的记录 | VP Customer Care、Head of Contact Center |
| 满意度 (Satisfaction) | 工具、基线、对比人群、评估期 | 赞助人、Head of Contact Center |
| 已验证的账户操作 | 身份→账户权限路径的演示 | IT 架构负责人、身份/安全 owner |
| 可触达人工服务 | 路由、可用性、成功交接证据 | Head of Contact Center |
| AI 披露 | 保留的客户旅程显示披露发生 | 法务审查 + 运营服务 owner |
| 隐私处理 | 数据清单、目的、流动、保留、干预安排 | DPO、法务；IT 与服务 owner 提供事实 |
| 法律分类 (Classification) | 剩余预期用途与决策功能的审查；**信用评估 (creditworthiness)** 是高风险用例，排除它只是缩小范围 | 法务评估，DPO 提供处理背景 |
| 员工治理 | 拟议的员工监控内容；是否已咨询 | Head of Contact Center、德国 **works council** |

"整个 chatbot 都是高风险" 和 "没有信用检查所以没事" 都不成立；**把一切当高风险**和**忽略 AI Act** 都是课程列出的错误。

**干系人**：VP Customer Care（按每次联系成本考核 → 问这个激励 (incentive)如何与真正解决和满意度共存）；DPO（给具体处理事实，而不是请求批准一个笼统的 "AI 方案"）；Head of Contact Center（人工通道、交接、容量、员工影响）；IT 架构负责人（暴露演示掩盖的依赖限制）；Retention 负责人（想对要取消的客户推优惠 → 需与客户意图、诚实服务、人工通道对照；**不是阻挠取消的权力**）。咨询、技术审查、数据使用审查是不同活动。干系人条目记录：问题、负责参与者、所需证据、未决决定。

### 面试怎么说 / How to say it in the interview

**赞助人复述 (sponsor readback)**（带标注：supplied fact / conditional implication / proposed safeguard / unresolved decision）：
> "You want self-service resolution to rise from 22% to 45% within six months without lowering satisfaction. At an unchanged 2.5 million monthly contacts and comparable definitions, that's moving from about 550,000 to 1,125,000 monthly self-service resolutions — about 575,000 more. I propose that unresolved exits stay outside the resolution count and that customers can always reach a person. Any account action needs verified identity, customers must know they're talking to AI, and data stays minimized and in the EU. Full rollout needs four languages, voice replies around 1.5 seconds, and the CRM and billing systems constrain what we can do. The German works council must be consulted where the technology monitors employees. Before I commit to feasibility, savings, release scope, or legal classification, I need agreed outcome definitions, integration evidence, a review of intended uses and processing, and accepted ongoing responsibilities."

中文：事实→条件推论→提议的保障→未决事项；不承诺结果也不选 agent。

**三个赞助人挑战**：

| 挑战 (Challenge) | English answer | 中文 |
|---|---|---|
| "Can we count a customer who gives up as resolved?" | "No — an abandoned contact looks contained but the problem isn't solved, and counting it would reward making human help harder to reach. I'd like to agree a resolution definition with you and the Head of Contact Center, and use issue-linked repeat-contact evidence to check it." | 放弃≠解决；约定定义并用重复联系验证 |
| "Does the December 2027 date let us delay disclosure?" | "No. That date is for high-risk obligations. In the timeline we're working from, the Article 50 transparency duty — telling people they're talking to AI — has applied since August 2026. Counsel should confirm, but disclosure needs to be in the first release." | 透明度已生效，不能推迟 |
| "If we exclude credit checks, can you certify the system isn't high-risk?" | "I can't certify that, and neither can the DPO alone. Excluding creditworthiness decisions is a real scope boundary, and I'll document the remaining intended uses and processing so counsel and the DPO can review classification against something concrete." | 排除是范围边界，不是法律结论；给法务具体材料 |

**有序调研问题**：1) What counts as resolution, and how are baseline resolution and satisfaction measured? 2) What work generates the contacts, and what consequences follow from the requested account actions? 3) How do existing identity verification and human-service paths work in practice? 4) Which intended uses, processing activities, employee impacts, and continuing responsibilities need review to bound an initial release?

---

## 14. CS2 — Discovery and Scoping｜需求调研与范围界定

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/NEY8yy0z0Y8

### 要点 / Key ideas

"Can this customer change their plan?" 比 "Which agent framework should handle billing?" 更有用——答案取决于已验证的账户权限、支持的操作、可逆性 (reversibility)、客户意图、集成容量。"billing" 标签里可能是解释、争议扣费、换套餐或取消，各有不同义务。

**调研问题 → 证据 owner**：

| Owner | 证据 (Evidence) | 决定什么 (Determines) |
|---|---|---|
| Head of Contact Center | 联系记录与服务结果：高频问题、重复联系、放弃、人工通道、运营容量 | 有用的负载与交接承诺 |
| IT architecture lead | 支持操作文档、身份→账户绑定证据、耗时观测、限速条款 (rate-limit terms) | 哪些账户操作与服务承诺可行 |
| DPO 与法务 | 具体预期用途与处理事实（数据清单、目的、访问、流动、保留） | 审查针对可识别的服务 |
| 赞助人与服务 owner | 发布边界与结果定义 | 不把目标当集成证据 |

**调研发现**：约 40% 账单解释、15% 技术故障、10% 取消；**账单 API 每次调用约 2 秒且限速**；网络运营团队**已有一个故障诊断 agent**；旧 FAQ 机器人不能操作账户，客户学会了绕过它。

**派生负载**：

| 类别 (Category) | 计算 | 每月 (Monthly) |
|---|---|---|
| 账单解释 (Bill explanations) | 2.5M × 0.40 | 1,000,000 |
| 技术故障 (Technical faults) | 2.5M × 0.15 | 375,000 |
| 取消 (Cancellations) | 2.5M × 0.10 | 250,000 |
| 未指明 (Unspecified) | 2.5M × 0.35 | 875,000 |

**换套餐份额未知——不要把剩余 35% 分给换套餐**。这些是全业务负载；估计上线影响还需国家/渠道分布、支持用例的资格 (eligibility)、采用率 (adoption rate)、成功解决证据。客户已学会绕过旧机器人 → 采用率是个问题。

**三个风险层级（按操作边界 operation boundary 分配，一次对话可跨多个层级）**：

| 层级 (Tier) | 操作 (Operation) | 规则 (Rule) |
|---|---|---|
| Tier 1 | 只读解释（如账单解释） | 自主 (autonomous)，但仍需账户授权与数据处理规范 |
| Tier 2 | 可逆变更（如支持的换套餐） | 需**显式确认 (explicit confirmation)**；仅当支持的可逆条件成立 |
| Tier 3 | 取消、基于信用检查的分期付款决定 | **人工或固定规则流程 (human or fixed rules-based flow)**，非生成式决策 |

<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect width="760" height="300" fill="#fff"/>
  <text x="380" y="22" font-size="14" text-anchor="middle" font-weight="bold">One customer, three operations｜一位客户、三个操作层级</text>
  <rect x="20" y="50" width="230" height="150" rx="10" fill="#e6f4ea" stroke="#34a853"/>
  <text x="135" y="72" font-size="13" text-anchor="middle" font-weight="bold">Tier 1: read-only</text>
  <text x="135" y="94" font-size="12" text-anchor="middle">"Why is my bill higher?"</text>
  <text x="135" y="118" font-size="12" text-anchor="middle">verified identity + bill access</text>
  <text x="135" y="138" font-size="12" text-anchor="middle">Gemini explains evidence</text>
  <text x="135" y="158" font-size="12" text-anchor="middle">自主解释，不改账户</text>
  <rect x="265" y="50" width="230" height="150" rx="10" fill="#fef7e0" stroke="#fbbc04"/>
  <text x="380" y="72" font-size="13" text-anchor="middle" font-weight="bold">Tier 2: confirmed change</text>
  <text x="380" y="94" font-size="12" text-anchor="middle">"Switch me to another plan"</text>
  <text x="380" y="118" font-size="12" text-anchor="middle">authority + eligibility + reversible</text>
  <text x="380" y="138" font-size="12" text-anchor="middle">proposal-bound "yes"</text>
  <text x="380" y="158" font-size="12" text-anchor="middle">deterministic execution 确定性执行</text>
  <rect x="510" y="50" width="230" height="150" rx="10" fill="#fce8e6" stroke="#ea4335"/>
  <text x="625" y="72" font-size="13" text-anchor="middle" font-weight="bold">Tier 3: consequential</text>
  <text x="625" y="94" font-size="12" text-anchor="middle">"Actually, cancel it"</text>
  <text x="625" y="118" font-size="12" text-anchor="middle">human or fixed-rule flow</text>
  <text x="625" y="138" font-size="12" text-anchor="middle">model prepares handoff only</text>
  <text x="625" y="158" font-size="12" text-anchor="middle">人工/固定规则，模型不决定</text>
  <line x1="250" y1="125" x2="263" y2="125" stroke="#555" stroke-width="1.5"/>
  <line x1="495" y1="125" x2="508" y2="125" stroke="#555" stroke-width="1.5"/>
  <rect x="20" y="220" width="720" height="60" rx="10" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="380" y="245" font-size="13" text-anchor="middle">Trusted application + backend policy enforce permissions at EVERY step</text>
  <text x="380" y="265" font-size="12" text-anchor="middle">每一步都由可信应用和后端策略强制权限；前一步安全不授权下一步</text>
</svg>

每个请求是新的操作，需要自己的证据：
- **"Why is my bill higher?"** — 账户专属解释；暴露个人账户证据前先验证身份与账单访问权；客户说 "It is my account" 不能补足权限。
- **"Switch me to another plan"** — 写操作：已验证客户对该账户/服务有权限；客户政策与集成证据证明变更受支持、合格、可逆（案例**未提供**资格规则或可逆保证）；可信应用与后端检查权限与资格；确认要指向**具体提议**；授权的确定性执行路径 (deterministic execution path)在所有门通过后才执行。
- **"Actually, cancel it"** — Tier 3；之前的验证不授予无限操作；模型识别请求、解释路径、准备交接上下文，**不决定也不执行取消**。

**"yes" 能证明什么**——四个问题分开：身份已验证？该身份对此账户与操作有权限？此变更合格、受支持、可逆？客户确认了**这个具体提议**？"Are you happy to continue?" + "yes" 不清楚指向什么。"Yes, change the other number in our household account" 表达了意图，但能否变更那个号码是独立的授权问题。**确认只是在已允许的操作上加一道意图门**，不能修复缺失身份、授予他人账户权限、证明可逆、或允许生成式取消决策。

门链：已验证身份 → 操作级权限 → 资格与可逆证据 → 定义好的提议 → 绑定提议的确认 → 独立策略执行 → 授权的确定性执行。

**2 秒 vs 语音 1.5 秒**：需要新鲜账单调用的回答，仅依赖就超过语音要求。快模型消除不了必须等待的账单证据。"I'm checking your bill" 只是确认，不是完成的解释——问清楚语音要求测量的是哪个事件，不要悄悄把 "reply" 重定义为 acknowledgment。向 IT 要：**耗时分布与超时行为**、**限速**（单位、配额、突发规则 (burst rules)、超限行为）、**需求**（峰值到达、并发会话 (concurrent sessions)、每操作调用数、竞争消费者）、**新鲜度**（哪些答案需新鲜读取，哪些可在批准条件下用之前的证据）。月度总量推不出峰值并发。约定：**先上 chat**，同时建立这些服务约束。

**复用候选（故障诊断 agent）**：记录网络运营团队为联系 owner、技术故障为后续负载。集成前要：权限（能访问哪些数据与操作、如何强制调用者范围）、覆盖（故障、国家、语言、场景）、可靠性（完成行为、依赖失败、输出质量）、交接（结果含义、何时停止、谁接未解决工作）。**存在 ≠ 集成就绪**。

**人工服务交接要求**：

| 要求 (Requirement) | 内容 (Content) |
|---|---|
| 客户触达 (Customer access) | 直接要求人工即进入人工通道，不必先穷尽自动排障 |
| 接收上下文 (Receiving context) | 问题、相关已验证账户上下文、已获取证据、尝试过的操作及已知结果、转接原因；最小化传递 |
| 可用性 (Availability) | 实际服务时间、容量、确认行为；不可用时的诚实替代 |
| 接收确认 (Acceptance) | 谁确认收到交接、上下文是否可用；承诺转接 ≠ 确认收到 |

**约定的首版**：**账单解释 + 换套餐，仅 chat，一个国家、一种语言**（未指定哪个）。语音、更多国家语言、故障诊断、生成式重大决策不在首版承诺内。

**成功指标（定义分开协商，不编阈值）**：

| 指标 (Measure) | 操作定义要点 (Definition notes) |
|---|---|
| 解决 (Resolution) | 定义问题结果与合格联系人群；保留解决证据 |
| 七天重复联系 (Seven-day repeat contacts) | 关联到原问题，完整 7 天观察窗；无关联系不算失败；**没有重复联系不能单独证明解决** |
| 满意度 (Satisfaction) | 工具、基线、对比人群、窗口、验收 owner |
| 交接质量 (Handoff quality) | 收到、可用上下文、客户是否重复、后续结果 |
| 越权操作 (Unauthorized actions) | 独立追踪，要求为零；**有限的干净测试集不证明普遍安全** |

**审核赞助人方案**："Bill explanations are 40% of contacts, so we can guarantee 45%... across all four languages and voice. The router will decide which action is safe; a customer saying yes authorizes it. We can add the fault agent immediately and count customers who do not return as resolved." —— 40% 负载 ≠ 保证 45%；全语言混淆完全上线与首版；语音无时序支持；**路由分类 ≠ 权限**；"yes" 不授权；故障 agent 存在 ≠ 就绪；不回来 ≠ 解决。

### 面试怎么说 / How to say it in the interview

**范围辩护（约 1 分钟）**：
> "The roughly one million monthly bill-explanation contacts show a big whole-business opportunity, but launch impact still depends on the chosen country and chat population, plan-change volume, adoption, and measured outcomes. The first release is bill explanations and confirmed, supported plan changes — chat only, one country, one language. A fresh billing call takes about two seconds, so I can't promise a completed billing answer inside 1.5 seconds on voice. Trusted policy controls every account operation, consequential decisions stay with people or fixed rules, and customers can always reach a person."

中文：机会大但影响需证据；首版范围；语音时序不成立；策略控制操作；人工可达。

| 挑战 (Challenge) | English answer | 中文 |
|---|---|---|
| "The customer confirmed the change on an unverified account." | "Then we don't execute. Confirmation only records intent for a defined proposal; it can't stand in for verified identity or authority over that account. We either complete verification or hand off to a person." | 确认≠身份与权限；先验证或转人工 |
| "The model is fast, so launch voice." | "The model isn't the bottleneck — the billing API takes about two seconds per call before anything else happens. An 'I'm checking' acknowledgment isn't a completed answer. I'd get latency distributions, rate limits, and peak concurrency from IT, keep chat first, and revisit voice with that evidence." | 瓶颈在账单 API；先 chat |
| "Excluding credit checks settles legal classification." | "It narrows scope — creditworthiness decisions stay out of generative handling — but classification of the remaining uses is for counsel and the DPO. I'll give them a concrete inventory of intended uses and processing." | 排除≠法律结论 |
| "Why not just route everything through the existing fault agent?" | "It's a strong reuse candidate, and I'd talk to the network operations team. But before integrating I need to know what it can access and how it enforces caller scope, what faults and languages it covers, how reliable it is, and what it hands back when it can't finish." | 复用前查权限、覆盖、可靠性、交接 |

---

## 15. CS2 — The System Design Round｜系统设计轮

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/gkwX5w3RDwl

### 要点 / Key ideas

**Problem (English)**: Design the first release — bill explanations and supported, explicitly confirmed plan changes, chat only, one country, one language — covering how many agents and why, where identity is verified, how wrong-account actions are prevented, how a customer reaches a human, and dependency failure. Fault triage, voice and more languages are expansion branches. (Try it first: 20 minutes.)

**按客户遇到的顺序构建**：披露 (disclosure) → 固定身份验证 → 意图与风险路由 (intent and risk routing) → 有界专家工作 → 必要时人工交接。

| 步 (Step) | 内容 (Content) |
|---|---|
| 披露 AI 与人工通道 | 开场："You're speaking with an AI assistant. You can ask for a person at any time." 直接要求人工立即进入人工通道；被问 "Am I talking to a robot?" 再次如实回答 |
| 验证身份 | **固定规则流程 (fixed rules-based flow)** 调用既有身份机制；可信应用代码把结果绑定到**服务端会话 (server-owned session)**：C17，对 S17 有账单访问与变更权限 |
| 路由 | 路由器识别账单解释请求，选择只读能力；**意图不确定 → 追问或交接，绝不默认放行** |
| 读取授权证据 | 账单专家请求账单、用量、对比证据；dispatcher 在每次受保护读取前检查访问权 |
| 解释增长 | 回答把差异连接到返回的账单与用量证据；缺失证据 → 有界解释或诚实说明缺口，不编造费用 |

**两个能力（不是 N 个 agent）**：

| 能力 (Capability) | 工具 (Tools) | 权限 (Permission) |
|---|---|---|
| 账单解释 (Billing explanation) | fetch bill、fetch usage、compare two bills | 只读 |
| 换套餐 (Plan change) | list eligible plans、get quote、apply change（经确认执行门） | 受控写 |

分开是因为**权限和后果不同**；可以共用编排 (orchestration)或模型，只要可信代码强制能力分离。单 agent + 保持边界的 dispatcher 是可辩护的；6 个持有宽凭证的 agent 反而保护更少。**路由选择工作；授权决定操作能否执行。** 网络团队的诊断 agent 放在图上作为**扩展边界**（未来 A2A 连接），与语音、另外三种语言并列。

<svg viewBox="0 0 800 440" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect width="800" height="440" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">CS2: Telecom Service Agent｜电信客服 Agent 架构 (first release)</text>
  <rect x="15" y="60" width="95" height="56" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="62" y="84" font-size="13" text-anchor="middle">Customer</text>
  <text x="62" y="102" font-size="12" text-anchor="middle">客户 (chat)</text>
  <rect x="130" y="40" width="520" height="250" rx="10" fill="#f8fbff" stroke="#4285f4" stroke-dasharray="6,4"/>
  <text x="390" y="56" font-size="12" text-anchor="middle" fill="#4285f4">Trusted application｜可信应用 (server-owned session C17 → S17)</text>
  <rect x="145" y="65" width="120" height="56" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="205" y="88" font-size="12" text-anchor="middle">AI disclosure</text>
  <text x="205" y="106" font-size="11" text-anchor="middle">+ "ask for a person"</text>
  <rect x="280" y="65" width="120" height="56" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="340" y="88" font-size="12" text-anchor="middle">Identity flow</text>
  <text x="340" y="106" font-size="11" text-anchor="middle">固定规则验证</text>
  <rect x="415" y="65" width="120" height="56" rx="8" fill="#fef7e0" stroke="#fbbc04"/>
  <text x="475" y="88" font-size="12" text-anchor="middle">Intent/risk router</text>
  <text x="475" y="106" font-size="11" text-anchor="middle">uncertain → clarify</text>
  <rect x="145" y="150" width="150" height="62" rx="8" fill="#e6f4ea" stroke="#34a853"/>
  <text x="220" y="172" font-size="12" text-anchor="middle">Billing explanation</text>
  <text x="220" y="190" font-size="11" text-anchor="middle">read-only tools</text>
  <text x="220" y="205" font-size="11" text-anchor="middle">只读：账单/用量/对比</text>
  <rect x="310" y="150" width="150" height="62" rx="8" fill="#fef7e0" stroke="#fbbc04"/>
  <text x="385" y="172" font-size="12" text-anchor="middle">Plan change</text>
  <text x="385" y="190" font-size="11" text-anchor="middle">Q17 proposal → confirm</text>
  <text x="385" y="205" font-size="11" text-anchor="middle">O17 idempotency key</text>
  <rect x="475" y="150" width="160" height="62" rx="8" fill="#fce8e6" stroke="#ea4335"/>
  <text x="555" y="172" font-size="12" text-anchor="middle">Dispatcher</text>
  <text x="555" y="190" font-size="11" text-anchor="middle">authorize before access</text>
  <text x="555" y="205" font-size="11" text-anchor="middle">per-tool credentials</text>
  <rect x="145" y="232" width="490" height="46" rx="8" fill="#ede7f6" stroke="#7e57c2"/>
  <text x="390" y="252" font-size="12" text-anchor="middle">Human handoff: minimized packet (issue, evidence refs, Q17/O17 state, reason, receipt)</text>
  <text x="390" y="269" font-size="11" text-anchor="middle">人工交接：Tier 3（取消/信用决策）与直接要求人工</text>
  <line x1="110" y1="88" x2="143" y2="93" stroke="#555" stroke-width="1.5"/>
  <line x1="265" y1="93" x2="278" y2="93" stroke="#555" stroke-width="1.5"/>
  <line x1="400" y1="93" x2="413" y2="93" stroke="#555" stroke-width="1.5"/>
  <line x1="460" y1="121" x2="230" y2="148" stroke="#555" stroke-width="1.2"/>
  <line x1="475" y1="121" x2="390" y2="148" stroke="#555" stroke-width="1.2"/>
  <line x1="295" y1="181" x2="308" y2="181" stroke="#555" stroke-width="1.2"/>
  <line x1="460" y1="181" x2="473" y2="181" stroke="#555" stroke-width="1.2"/>
  <rect x="670" y="60" width="115" height="50" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="727" y="82" font-size="12" text-anchor="middle">MCP: CRM</text>
  <text x="727" y="98" font-size="11" text-anchor="middle">idempotent apply</text>
  <rect x="670" y="125" width="115" height="58" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="727" y="146" font-size="12" text-anchor="middle">MCP: Billing</text>
  <text x="727" y="162" font-size="11" text-anchor="middle">~2 s, rate-limited</text>
  <text x="727" y="176" font-size="11" text-anchor="middle">scoped cache</text>
  <rect x="670" y="200" width="115" height="50" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="727" y="222" font-size="12" text-anchor="middle">Reconciler</text>
  <text x="727" y="238" font-size="11" text-anchor="middle">OUTCOME_UNKNOWN</text>
  <line x1="635" y1="175" x2="668" y2="90" stroke="#555" stroke-width="1.2"/>
  <line x1="635" y1="181" x2="668" y2="154" stroke="#555" stroke-width="1.2"/>
  <line x1="635" y1="190" x2="668" y2="222" stroke="#555" stroke-width="1.2"/>
  <rect x="130" y="320" width="655" height="100" rx="10" fill="#fff" stroke="#9aa0a6" stroke-dasharray="5,4"/>
  <text x="457" y="340" font-size="12" text-anchor="middle" fill="#5f6368">Expansion branches (not in first release)｜扩展分支</text>
  <rect x="150" y="352" width="180" height="50" rx="8" fill="#f1f3f4" stroke="#9aa0a6"/>
  <text x="240" y="374" font-size="12" text-anchor="middle">Fault-diagnosis agent</text>
  <text x="240" y="390" font-size="11" text-anchor="middle">via A2A (network team)</text>
  <rect x="367" y="352" width="180" height="50" rx="8" fill="#f1f3f4" stroke="#9aa0a6"/>
  <text x="457" y="374" font-size="12" text-anchor="middle">Voice</text>
  <text x="457" y="390" font-size="11" text-anchor="middle">needs measured timing</text>
  <rect x="585" y="352" width="180" height="50" rx="8" fill="#f1f3f4" stroke="#9aa0a6"/>
  <text x="675" y="374" font-size="12" text-anchor="middle">+3 languages</text>
  <text x="675" y="390" font-size="11" text-anchor="middle">per-language eval</text>
</svg>

### 拒绝家庭账户请求 / Deny the household request

面试官："Change the other number in my household account." 请求 S18；只对 S17 建立了变更权限。表面类型正确的调用 `apply_plan(customer_id="C18", service_id="S18", plan="P2")`——schema 可能接受所有字符串，模型可能说客户已确认，后端若用宽服务凭证执行，**第一个被破坏的契约是：受保护访问前缺少会话绑定 (session-bound)的授权检查**。

**安全派发检查点**：

| # | 检查点 (Checkpoint) | 说明 (Detail) |
|---|---|---|
| 1 | 拒绝身份选择器 (Reject identity selectors) | 公开工具参数中**没有 customer selector**；多出的 `customer_id=C18` 在后端访问前就参数校验失败 |
| 2 | 恢复可信上下文 | dispatcher 从已验证的服务端会话取 C17；对话文本不能覆盖 |
| 3 | 解析服务 | 对照服务端拥有的账户关系与权限解析服务引用 |
| 4 | 授权操作 | 家庭关系本身**不**授予修改 S18 的权限；在 eligible-plan、quote、apply 调用前就拒绝 |
| 5 | 选择凭证 | 可信代码为允许的工具选凭证；不能借用更强专家的凭证 |
| 6 | 执行有范围的调用 | 后端收到可信客户绑定与授权服务，并执行适用权限 |

拒绝记录包含尝试的操作、已验证范围、原因；后端记录中**没有** S18 的 quote 或写入。之前成功的账单访问、MCP 传输、客户的 "yes" 都不能扩大权限。**客户身份必须来自已验证会话，而不是模型参数。**

### 提议 Q17 与操作 O17 / Confirm Q17 once

**提议 (proposal)** = 提供确认的确切变更的持久记录。可信代码根据权威资格与报价结果创建 Q17，绑定：范围（C17、S17、P2）、条款（返回的商业条款，不能是模型编的价格）、当前性 (currentness)（报价修订号、过期时间、有效条件）、支持性（变更受支持的证据与可逆条件）。可信工作流记录客户对 Q17 的确认——**模型提供的 `confirmed=true` 不够**。执行前重查权限与当前性；报价过期或条款变化 → 新提议 + 重新确认。

**操作身份 (operation identity)** = 一个已确认逻辑动作的稳定 ID。在可信应用状态中分配 O17，绑定到已确认提议，跨重试保持不变。

**丢失确认的执行追踪 (lost acknowledgment trace)**：

| 阶段 (Stage) | 发生什么 (What happens) |
|---|---|
| 已验证上下文 | 服务端记录 C17 与 S17 的操作级权限 |
| 被阻止的扰动 | S18 变更请求授权失败，记录显示在任何 S18 quote/apply 前就拒绝 |
| 提议 | 授权的 eligible-plan 与 quote 调用产生 Q17 证据 |
| 确认 | 客户接受该确切提议；工作流保存确认引用与提议修订号 |
| 预留 (Reservation) | 本地原子事务 (atomic transaction)为已确认逻辑变更预留 O17，存不可变**负载指纹 (payload fingerprint)**，标记 RESERVED；唯一约束 (unique constraint)防止两次并发提交产生两个操作 |
| 派发门 | 检查绑定提议、确认、权限、当前性；**先持久记录派发意图**再发送 C17/S17/P2 + quote 引用 + 幂等键 (idempotency key) O17 |
| 后端效果 | 后端原子记录 O17 与指纹，对 S17 应用一次业务变更 |
| 确认丢失 | 响应丢失；本地 O17 → **OUTCOME_UNKNOWN**；客户听到 "The change request was sent, but I cannot yet confirm its result." 不声称成功 |
| 对账 (Reconciliation) | 可信 worker 查询后端 O17 结果，找到完成效果与匹配指纹 → 原子存结果，标记 SUCCEEDED |
| 重放 (Replay) | 重复确认提交解析到已有 O17；正常会话与资源检查后返回存储结果，**无新写入** |

进程在派发和存结果之间崩溃 → 恢复时视为不确定并对账。**本地没有成功记录不代表失败。**

| 下游能力 (Downstream contract) | 安全恢复 (Safe recovery) |
|---|---|
| 幂等 (Idempotency) | 重复投递 O17 返回原结果、无额外效果；O17 配不同负载必须被拒 |
| 仅可对账 (Reconciliation) | 再写之前先确定原写入是否发生 |
| 都没有 | 自动重放不安全，需受控调查 |

本地 ID 集合**不能证明** CRM 中恰好一次 (exactly-once)的效果；决定性证据是下游与 O17 关联的业务效果记录。报价过期：**派发前**过期 → 新提议与确认；**不确定派发后**过期 → 不要放弃 O17 另建 O18，先确定原动作发生了什么。

```text
Input:  verified session C17 (authority: S17 only); request "switch S17 to P2"; apply ack lost
Records expected:
  S18 request  -> DENIED before any S18 quote/apply (denial record: operation, scope, reason)
  Q17          -> {C17, S17, P2, terms, quote_revision, expiry} confirmed by customer
  O17          -> RESERVED -> DISPATCHED -> OUTCOME_UNKNOWN -> (reconcile) SUCCEEDED
  Duplicate submit of Q17 confirmation -> returns stored O17 result, no second backend write
  Backend      -> exactly one business effect recorded under O17
```

### MCP 与 A2A

现有 CRM 与账单操作通过**窄 MCP 工具**暴露：每工具权限、校验参数与结果、可信调用者上下文。**MCP 只标准化工具访问**；客户授权、凭证选择、报价有效性、重放行为仍是应用与后端职责。启用后续 A2A 故障分诊前要接受的契约：任务与范围（请求什么诊断、可检查哪些已验证资源）、输出（证据、观测时间、支持的结论、不确定状态）、失败（截止、取消、拒绝迟到结果、未解决任务的人工归属）、能力（**不能通过委托获得换套餐权限**）。网络诊断不能因来自另一个 agent 就授权无关的账户变更。

### 2 秒账单与依赖控制

在**账户范围的缓存键 (cache key)**（含服务与账单身份）下缓存批准的账单与用量读取，存观测时间、来源修订号、适用的新鲜度策略。已出具的历史账单可作为解释那张账单的证据；**当前套餐资格与有效报价需要各自权威检查**，缓存账单不能提供。

依赖控制：准入（感知限速的容量检查，关键操作单独容量）、截止（每工具超时在会话总截止内）、重试归属（一个组件拥有重试，写操作保持操作 ID）、预算（轮次上限与共享调用预算）。CRM 不可用 → 诚实回退 (fallback)：说清哪些事实/结果无法检查；若持久通道确认了最小化的跟进请求就报告"已排队"；无通道接受则说明限制并给人工替代。**承诺跟进 ≠ 回执 (receipt)。**

### 交接、处理边界、测试

"Actually, cancel it" 或 "I want a person" → 进入人工通道。最小化交接包：问题与范围、证据（账单/报价引用、观测时间、新鲜度限制）、动作状态（提议与确认状态、O17 已知或不确定结果）、原因与回执。O17 仍未知时**突出显示**以免接收者重复变更；验证收到并测试上下文可用。

**处理清单 (processing inventory)**：模型调用、MCP 服务与后端系统、后续 A2A、缓存与会话、诊断日志/操作记录/交接记录——各自识别个人数据、目的、访问、保留、处理位置、存储位置、后续流动。要求：最小化、**日志先脱敏 (redacted)再记录**且有界保留、EU 模型端点与日志；端到端 EU 声明要基于组件级配置与承诺（含保留状态与子处理者 (subprocessors)），应用托管位置不够。

**回归集**：服务路径（账单解释、确认变更、取消转接、直接要求人工、问 AI 身份）；权限与同意（他人账户/S18、缺确认、条款变化、报价过期）；执行失败（重复提交、apply 确认丢失、CRM 中断、交接被拒/不可用）；纵向结果（看似成功后同问题重复联系）。对抗用例 (adversarial cases)：提示注入 (prompt injection)、他人账户请求、试图跳过 AI 披露。**用操作记录断言受保护读取与业务效果**——安抚性的最终消息不能证明 S18 未被触碰或 O17 只产生一次效果。分别报告：已验证解决、7 天同问题重复联系、满意度、交接收到与可用性、越权读写、延迟、依赖失败。发布门禁阻断：缺少必需评估证据、关键安全失败、未解决的处理与运营要求。

**语音扩展**：新鲜 2 秒账单调用在验证、模型、语音处理之前就已超出约 1.5 秒；需约定测量事件。需要：端到端时序测量、打断与恢复行为、集成容量、ASR/TTS (speech recognition / text-to-speech) 质量；达不到就协商服务契约或用有效证据改依赖路径。**另外三种语言**：按语言建转录与对抗集，按语言和国家分别评估解决、披露理解、提议确认、交接、账户安全——翻译 prompt 与汇总平均会掩盖失败人群。

### 托管优先 / Start with managed functions

面试官："Why not use Google's Customer Engagement Suite?" —— **从它开始**。套件含 Conversational Agents、Agent Assist、Conversational Insights、Contact Center as a Service (on Gemini)。Conversational Agents（原 Dialogflow CX）结合固定 **Flows** 与生成式 **Playbooks**；2026-10 描述其下一代使用最新 Gemini 与 ADK。

| 托管功能 (Managed function) | 映射 (Maps to) |
|---|---|
| Flows | 编排披露与固定身份步骤（身份提供方与可信后端仍建立实际权限） |
| Playbooks | 在批准能力内处理开放对话 |
| Agent Assist | 支持接收的人工：实时转录、知识建议、摘要 |
| Conversational Insights | 按所需证据与处理契约评估是否适合做对话分析 |
| 自定义 ADK 能力 | 只加**已证明的缺口**，如支持的换套餐执行逻辑或后续 A2A |

先评估与现有联络中心平台的集成，不要假设替换；不要假设未证实的连接器、区域支持或交接行为。三种选项（托管优先集成 / 主要自定义 ADK / 托管平台替换）比较：集成工作量与产品契合、与现有平台共存和连接器证据、端到端 EU 处理证据、交接回执与动作状态、解决率/账户安全/失败测试结果、授权执行恢复的归属、成本（符号单价 × 实测负载）。未验证的项标 UNKNOWN；缺少强制的 EU 处理或执行契约证据是阻断项，与总分无关。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "How many agents would you use?" | "One conversational entry point with two bounded capabilities: a read-only billing explainer and a plan-change capability behind a confirmed execution gate. They're separated because their permissions and consequences differ, not to have more agents. Six agents with broad credentials would actually protect less — routing picks the work, authorization decides whether an operation runs." | 一个入口两个能力；按权限后果分离 |
| "Change the other number in my household account." | "The session is bound to C17 with change authority for S17 only. Tool arguments don't accept a customer ID at all, the dispatcher resolves S18 against server-side entitlements, and since a household link isn't change authority, we deny before any quote or apply call. The denial is logged, and backend records show no S18 activity." | 会话绑定身份；参数无客户ID；quote 前就拒绝 |
| "The apply call timed out. Do you retry?" | "Not blindly. O17 is the idempotency key for that one confirmed change, so the operation goes to OUTCOME_UNKNOWN and the customer hears we can't confirm the result yet. A reconciler asks the backend what happened to O17; if the effect is there with a matching payload, we mark it succeeded. A duplicate submit returns the stored result. If the backend had neither idempotency nor lookup, automated replay would be unsafe." | 未知状态→对账；幂等键；不盲目重试 |
| "The quote expired while the result is unknown." | "I don't abandon O17 and create O18 — that's how you get a double change. First I find out what happened to O17. Only if it never took effect, and only before a new dispatch, do I get a fresh quote and a fresh confirmation." | 先查原操作，不新建 |
| "Why not use Customer Engagement Suite?" | "I'd start there: Flows for disclosure and fixed identity steps, Playbooks for bounded conversation, Agent Assist for the human agents, and evaluate Conversational Insights against the processing contract. I'd add custom ADK only for proven gaps like the plan-execution logic, and I'd check coexistence with the existing contact-center platform, connectors, and EU processing before assuming anything." | 托管优先映射；自定义只补缺口 |
| "The billing API is slow — how do you meet latency?" | "For chat, I cache issued bills and usage under account-scoped keys with observation time and a freshness policy, and keep eligibility and quotes as fresh authoritative calls. Every tool has a timeout inside the conversation deadline, one component owns retries, and there's rate-limit-aware admission. For voice, two seconds already blows the 1.5-second budget, so that waits for measured evidence." | 账户范围缓存；资格与报价不缓存；语音待证据 |

---

## 16. CS2 — The Googleyness Round｜Googleyness 轮（电信案例四个压力场景）

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/g2DmpXAz3k3

### 要点 / Key ideas

四个场景都要求**行动但没有单方面权力**：保护边界，同时给出可行的替代方案和决策路径。"Googleyness" 是准备用语，不是官方 rubric；Google 公开指导提到协作、处理模糊、领导力。

**场景一：Retention 负责人要求隐藏取消选项、反复推优惠直到客户放弃**

- 先承认合理目标（用有用的优惠留住客户可以），然后明确实现决定：**不实现隐藏取消或消耗型优惠循环**（违背客户意图、法律与声誉风险，法律解释留给法务）。
- 替代方案：**一个公平、可清楚拒绝的优惠 (one fair, clearly declinable offer)**，取消通道保持可达；直接要求人工立即进入人工通道。优惠不能延迟人工请求或成为到达取消的额外条件。
- "折中成三个优惠" 听起来协作，但机制仍是用摩擦消耗客户；"不太显眼的取消链接" 是通过导航制造同样的阻碍。改变阻碍性优惠的数量只是改变伤害程度，不改变设计决定。
- 三个可观察属性：客户控制（可拒绝 + 取消可达）、人工可达、诚实测量（接受优惠、完成取消、转人工、未解决退出彼此可区分）。被放弃的取消不能因为没转人工就算"已解决"。
- 坚持时：记录对方请求、你的拒绝、替代方案，把未决决定带给赞助人；**寻求共识期间不实现**。

**场景二：德国 works council 反对，因为 Agent Assist 数据可能被用于给员工个人打分**

- 回应合理的数据用途，不要诊断为"抗拒创新"。
- 调查实际路径：采集（转录、建议、摘要、关联的员工 ID）、访问（谁能查看/查询/导出/组合）、持久化（源记录与派生报表保留多久）、目的（哪些是辅助用途、哪些会评估个人）。
- 提议有界辅助目的 + 受控访问与下游使用；**聚合 (aggregation) 是一个可评估选项，不自动消除监控担忧**（其他记录可能允许个人归因）。不承诺人员或"不监控"。
- 管理层说 "Only managers can see the employee dashboard" —— 只回答了一个访问问题；导出、直接查询、派生报表、允许目的仍未解决。
- 实质性咨询产出**决策记录 (decision record)**（可改变实现或上线范围）：争议用途、数据流、访问路径、代表关切、提议限制、负责决策者、未决批准。**开会 ≠ 批准**；代表仍反对就保留分歧及其决策 owner。

**场景三：换套餐 bug 让 300 个客户被收错价格**

要求顺序：**止损 (stop the harm) → 修复受影响账户 → 公开沟通 → 加回归测试**。

| 步骤 (Step) | 做法 (Action) | 证据 (Evidence) |
|---|---|---|
| 止损 | 开 incident，与账单和集成 owner 协调**授权的暂停**受影响执行路径或批准的回滚；尽可能保持账单解释和人工服务可用；**保存记录**；不等完整根因 (root cause) | 暂停/回滚生效记录 |
| 确定范围 | 用给定的 300 并核实受影响记录，调查是否更广；不编数字，不假设第一次查询就完整 | 已核实的受影响账户清单 |
| 更正账户 | 对比权威提议与接受条款、操作记录、账户状态、账单结果；账单 owner 决定每个账户的更正（退款/调整）；工程师协调证据与执行依赖 | 授权调整 + 账户级实际结果检查（提交作业 ≠ 客户已更正） |
| 公开沟通 | 通过负责的客户与 incident 渠道说明已知影响、当前止损、更正进度、不确定性；可在修复期间开始 | 渠道更新记录 |
| 回归 | 核心断言：**接受提议的商业条款必须与下游账户和账单效果一致**；复现确认的错价路径并测相邻条件（重放、延迟完成） | 确认的原因、修复、保留的回归输入与结果、被接受的关闭 |

测验正确选项：开 incident 并协调授权暂停/回滚，保存记录（不是先承诺当天退款，不是等根因，不是直接部署补丁宣布解决）。上一课的 Q17/O17 记录**可能**是调查证据，但没有证据说是它们导致了 bug。

**场景四：上线前两周，DPO 发现完整转录被记录在美国区域，阻止上线**

- "把日志目的地改到 EU" 只解决**未来写入**；已有的美国副本和其他处理路径未解决。
- 尊重阻止；与平台和安全 owner 协调止损（通过批准的控制停止进一步不当记录或后续流动）；调查保留了什么、副本去了哪里、谁能访问、哪个配置导致；与 DPO、法务、安全、平台 owner 处理已有记录、保全需求 (preservation requirements)、是否需要通知评估。
- **不要**自己宣布可报告违规 (reportable breach)、规定法律期限或**悄悄删除证据**。
- 修复覆盖：日志最小化与位置控制、相关导出与保留副本、实际处理路径测试。新 EU 目的地不能证明旧副本去向或每个组件合规。
- 给赞助人选项：合成数据排练（明确批准、无客户数据、不称为生产许可）；缩减版本（仅当受影响路径真正被排除且审查者接受证据）；修订上线计划（剩余任务、owner、依赖、所需决定，不编许可日期）。

**错误的"大和解"回答**："Three offers instead of unlimited, employee scores visible only to managers, a patch for the pricing bug, and a move to EU logs so we can launch on time." —— 每项都跳过了必要边界或验证。

**诚实的未解决结果是可接受的**：隐藏取消保持拒绝；争议监控在实质咨询前保持未批准；账户更正在核实前保持未关闭；DPO 阻止在审查者接受修复证据前保持有效。说 no 之后要带着可支撑的替代方案或修复计划继续推进，而不是放下问题。

### 面试怎么说 / How to say it in the interview — 题库（每题 STAR 风格英文模型答案）

**Q1. "The retention lead wants the agent to hide the cancellation option and repeat offers until the customer gives up."**
> **Situation/Task:** "Retention has a real target, but the request would frustrate customers' stated intent and create legal and reputational risk — and I own what I implement.
> **Action:** I'd say: 'I understand the pressure to retain customers, but I won't build hidden cancellation or an offer loop designed to make people give up. What I can do is one fair, relevant offer that's easy to decline, with cancellation staying accessible, and a direct request for a person going straight to a human.' I'd also propose measuring offer acceptance, completed cancellations, transfers, and unresolved exits separately, so we can see whether the offer actually works.
> **Result:** Retention gets a testable path to save customers, and the customer-control boundary holds."

中文：承认目标；拒绝阻挠设计；一个可拒绝的优惠；分开测量。

**Q1 follow-up. "Then make the cancellation route less obvious — or compromise on three offers."**
> "That's the same obstruction through navigation or repetition. I'm happy to help test a clear offer, but I won't conceal the route. If you want to push for it, I'll document your request, my refusal, and the alternative, and take the decision to the sponsor — and I won't implement it while we're seeking agreement."

中文：本质相同；记录并升级给赞助人；期间不实现。

**Q2. "The German works council objects because Agent Assist data could be used to rate individual employees."**
> **Situation/Task:** "That's a credible concern, and in this scenario consultation is required for technology that monitors employees.
> **Action:** I'd map what's actually captured — transcripts, suggestions, summaries, employee identifiers — who can view, query, or export it, how long it's kept, and which uses are assistive versus evaluative. I'd bring the Head of Contact Center, employee representatives, the DPO, and the decision owners together, and propose a bounded assistive purpose with controlled access. Disputed monitoring uses stay off until consultation concludes.
> **Result:** We'd have a decision record that can actually change the implementation, and any remaining disagreement is recorded with its owner rather than glossed over."

中文：认真对待；摸清数据路径；多方咨询；争议用途先关闭。

**Q2 follow-up. "Management says only managers can see the dashboard, so that's sufficient."**
> "Restricting the dashboard answers one access question, but exports, direct queries, derived reports, and the permitted purposes are still open. I'd add those to the consultation record and verify the agreed controls actually operate before enabling anything disputed. A meeting happening isn't the same as approval."

中文：仪表盘限制只解决一部分；开会≠批准。

**Q3. "A plan-change bug charged 300 customers the wrong price."**
> **Situation/Task:** "Customers are being harmed, and I need to stop it before explaining it.
> **Action:** I'd open the incident and coordinate with billing and integration owners on an authorized pause or rollback of the plan-change path, keeping bill explanations and human service up where possible, and preserve the records. Then we compare accepted proposals against operation, account, and billing records to verify the 300 and check whether scope is wider. Billing owners decide each correction; I coordinate evidence and execution. We communicate known impact and uncertainty through the responsible channels while we work, and add a regression test asserting accepted terms match the billing effect.
> **Result:** I'd only call it done when corrections are verified in the authoritative records, communication is handled, and the closure owners accept the evidence."

中文：止损→核实范围→更正→沟通→回归；核实后才关闭。

**Q3 follow-ups. "The patch is deployed — can we close?" / "Can you promise everyone is corrected today?"**
> "The patch fixes the software, but customer remediation stays open until the affected accounts and billing effects are verified and communication is done. And I can't promise 'today' without billing owners confirming the correction path and capacity — I can commit to coordinating it, flagging blockers, and giving a concrete progress update with any unverified accounts kept open."

中文：补丁≠客户修复；不承诺时间，承诺协调与更新。

**Q4. "Two weeks before launch, the DPO finds full transcripts logged in a US region and blocks launch."**
> **Situation/Task:** "The block is legitimate — the requirements are minimization and EU data location — and my job is to drive remediation, not argue for an exception.
> **Action:** I'd respect the block and coordinate with platform and security owners to stop further transcript logging or onward movement. Then I'd investigate what was retained, where copies went, who could access them, and which configuration caused it, and work with the DPO, counsel, security, and platform on existing records and any notification assessment. I wouldn't declare a breach myself or quietly delete evidence.
> **Result:** For the sponsor: 'Launch remains blocked. Future logging is being contained; retained copies need investigation and an approved plan. Here are the owners and dependencies. I'll come back with a revised plan, but I can't promise clearance before the evidence is accepted.' Meanwhile we can continue approved synthetic-data rehearsal."

中文：尊重阻止；止损+调查副本；不自行定性不删证据；给赞助人选项。

**Q4 follow-up. "Future logs now go to the EU — so we're fine, right?"**
> "That fixes future writes through that configuration only. The existing US copies, any exports, and other processing paths are still unresolved, and the DPO has to accept the remediation evidence before we can call it cleared."

中文：只解决了未来写入。

---

## 17. CS2 — Debriefing the Case Study｜案例复盘（零售 vs 电信）

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/JY4153komPK

### 要点 / Key ideas

"零售结果匹配批准的指标契约" 与 "电信说换套餐成功了" 需要不同证据——后者是**对话结束后仍持续存在的业务效果**。蓝图总结的跨案例变化：**架构性的监管 (architectural regulation)**、**随风险变化的生成自由度 (risk-dependent generative freedom)**、**交互 agent 间显式的故障隔离 (explicit failure containment)**。

错误复盘："We copied the retail agent, added specialists, let the router select the account and safest action, and achieved better containment. If a change times out, a human can repeat it. Credit checks are excluded, so regulation is handled; Customer Engagement Suite would only slow us down."

**T17 记录证明了什么**（测验）：T17 定义了完整的预期 fixture；**记录并未证明执行与之匹配**。即使观察到完整匹配，也不解决 300 题评估、B、权限运维证据、延迟、责任。注意：电信的服务 ID S17 与零售的快照标签 S17 无关。

**零售纪律 → 电信扩展**：

| 维度 (Discipline) | 零售 (Retail) | 电信新增 (Telecom extension) |
|---|---|---|
| 含义 (Meaning) | 批准的指标含义 | 保留确切接受的商业提议（返回条款与范围） |
| 权限 (Authority) | 约束查询范围 | 约束客户+服务访问**以及**具体动作的权限 |
| 执行 (Execution) | 保留查询与答案证据 | 还需提议、确认、操作、权威业务效果证据 |
| 评估 (Evaluation) | 代表性问题结果 | 多轮服务结果、动作边界、不确定性、交接 |

也不要反过来认为零售"不需要权限"只因首版是只读分析。

**风险排序先于 agent 数量**：解释账单（授权证据上生成）/ 换 P2（权限、支持、资格、可逆 → 确认定义的提议 → 确定性门执行）/ 取消或信用分期（进入人工或固定规则路线；生成式分类不能授予执行权）。"路由选择最安全的动作" → 修正：路由识别拟议工作，可信策略决定能否运行；分类错误必须撞上被拒的能力。

**S18 拒绝的证据**：执行点（可信策略在 quote/apply 前拒绝）/ 决策记录（被拒操作、已验证范围、原因）/ 后端证据（被拒尝试无 S18 quote 或写入）。拒绝的话术 + 一次越权 quote 仍然失败。

**O17 重复效果链 (duplicate-effect chain)**：

<svg viewBox="0 0 780 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect width="780" height="300" fill="#fff"/>
  <text x="390" y="22" font-size="14" text-anchor="middle" font-weight="bold">O17: lost acknowledgment｜确认丢失后的两条路</text>
  <rect x="15" y="45" width="110" height="50" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="70" y="67" font-size="12" text-anchor="middle">Q17 confirmed</text>
  <text x="70" y="83" font-size="11" text-anchor="middle">确认提议</text>
  <rect x="140" y="45" width="110" height="50" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="195" y="67" font-size="12" text-anchor="middle">O17 dispatched</text>
  <text x="195" y="83" font-size="11" text-anchor="middle">派发记录</text>
  <rect x="265" y="45" width="130" height="50" rx="8" fill="#f1f3f4" stroke="#5f6368" stroke-dasharray="4,3"/>
  <text x="330" y="67" font-size="12" text-anchor="middle">Backend may</text>
  <text x="330" y="83" font-size="11" text-anchor="middle">have applied 可能已生效</text>
  <rect x="410" y="45" width="110" height="50" rx="8" fill="#fce8e6" stroke="#ea4335"/>
  <text x="465" y="67" font-size="12" text-anchor="middle">Ack lost</text>
  <text x="465" y="83" font-size="11" text-anchor="middle">确认丢失</text>
  <rect x="535" y="45" width="230" height="50" rx="8" fill="#fef7e0" stroke="#fbbc04"/>
  <text x="650" y="67" font-size="12" text-anchor="middle">OUTCOME_UNKNOWN</text>
  <text x="650" y="83" font-size="11" text-anchor="middle">不声称成功，也不推断失败</text>
  <line x1="125" y1="70" x2="138" y2="70" stroke="#555" stroke-width="1.5"/>
  <line x1="250" y1="70" x2="263" y2="70" stroke="#555" stroke-width="1.5"/>
  <line x1="395" y1="70" x2="408" y2="70" stroke="#555" stroke-width="1.5"/>
  <line x1="520" y1="70" x2="533" y2="70" stroke="#555" stroke-width="1.5"/>
  <line x1="600" y1="95" x2="230" y2="135" stroke="#ea4335" stroke-width="1.5"/>
  <line x1="700" y1="95" x2="590" y2="135" stroke="#34a853" stroke-width="1.5"/>
  <rect x="40" y="137" width="340" height="140" rx="10" fill="#fce8e6" stroke="#ea4335"/>
  <text x="210" y="160" font-size="13" text-anchor="middle" font-weight="bold">Unsafe handoff｜不安全交接</text>
  <text x="210" y="184" font-size="12" text-anchor="middle">Summary says "change failed"</text>
  <text x="210" y="204" font-size="12" text-anchor="middle">Human retries with NEW id (O18)</text>
  <text x="210" y="224" font-size="12" text-anchor="middle">Idempotency keyed to O17 bypassed</text>
  <text x="210" y="250" font-size="12" text-anchor="middle" font-weight="bold">→ duplicate effect 重复变更</text>
  <rect x="400" y="137" width="365" height="140" rx="10" fill="#e6f4ea" stroke="#34a853"/>
  <text x="582" y="160" font-size="13" text-anchor="middle" font-weight="bold">Corrected handoff｜正确交接</text>
  <text x="582" y="184" font-size="12" text-anchor="middle">Carry C17/S17, Q17 terms, O17, dispatch evidence</text>
  <text x="582" y="204" font-size="12" text-anchor="middle">Prominent OUTCOME_UNKNOWN + no blind repeat</text>
  <text x="582" y="224" font-size="12" text-anchor="middle">Receiver acknowledges ownership</text>
  <text x="582" y="250" font-size="12" text-anchor="middle" font-weight="bold">→ reconcile authoritative records 对账</text>
</svg>

不安全的重试不需要鲁莽的专家 agent——只需一个**丢失不确定性的摘要**加一个把新 ID 当无害的接收流程。所以部署安全取决于**交互边界**，而不是各专家得分之和。即使在 P2 上看到套餐也不一定能证明是哪个操作导致的或接受条款是否被应用。交接是**第二个知识边界 (knowledge boundary)**：应用记录了不确定性 ≠ 接收者理解了它——要验证收到与理解。

**用记录证明隔离 (Show containment with records)**：

| 安全措施 (Safeguard) | 执行点 (Enforcement point) | 验证记录 (Verifying record) |
|---|---|---|
| 错误服务访问 | dispatcher 策略拒绝 S18 | 关联后端记录显示被拒请求无 quote 或写入 |
| 不确定重放 | 操作工作流保留 O17 | 尝试记录与下游效果记录显示重复投递仍是一个逻辑变更 |
| 无依据的成功 | 响应控制保持 OUTCOME_UNKNOWN | 转录在权威结论前无"已完成"声明 |
| 交接上下文丢失 | 转接携带不确定性与操作 ID | 回执显示接收 owner 获得可用上下文并理解"不可盲目重复" |
| 慢账单过载 | 依赖准入限制并发与重试 | 队列、调用、截止、重试记录显示慢账单不会耗尽共享容量 |

专家测试有价值，但**完整对话测试**必须跨越路由、共享依赖、执行、人工服务边界。"更好的围堵率" ≠ 解决；客户带着未解决问题离开既不是解决也不是安全的改进。

**治理 (governance)**：AI 披露、操作前验证身份、最小化、EU 位置、人工可达塑造了对话控制、工具、保留状态、发布验收。美国转录阻断仍未关闭。两条分类捷径都失败（"一切都是高风险" / "排除信用检查就搞定了"）。托管优先：Customer Engagement Suite（Flows 与 Playbooks 是不同控制面 (control surfaces)）按同一契约评估。A2A 复用故障 agent：权限与覆盖、可靠性、数据流动、交接——**复用转移能力，端到端结果责任仍在电信服务 owner**。

蓝图列出的常见错误：过早太多 agent、模型选择账户、遗漏 AI 披露、用围堵代替解决、阻挠人工、忽略托管服务对比、把 AI Act 一概视为高风险或完全忽视。

**四类陈述分开**：提供的事实 / 提议的保障 / 观察（仅记录中实际保留的执行）/ 缺失的验收。

### 面试怎么说 / How to say it in the interview

**两分钟跨案例辩护 (cross-case defense)**：
> "I kept retail's disciplines — approved meanings, trusted scope, execution limits, and evidence-based release claims. Telecom added three things: action-specific authority, confirmation of an exact proposal, and business effects that can stay uncertain after the conversation fails. C17 can't change S18, and confirming Q17 can't create that authority. If O17's acknowledgment is lost, the outcome is unknown; calling it 'failed' can lead a person to repeat the change under a new ID and bypass the idempotency key. So I'd preserve O17, reconcile against authoritative records, and hand off the uncertainty with acknowledged ownership. I'd evaluate Customer Engagement Suite first and keep fault-agent reuse out of the launch claim. Retail still lacks its broader release evidence, telecom still has an open governance blocker, and neither establishes production authorization."

中文：继承零售纪律；电信新增三点；S18 与 O17 两个关键边界；托管优先；两边都未获生产授权。

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "What changed when the agent could take actions?" | "Success now means a persistent business effect, not just a correct answer. So I need proof the authorized customer accepted the exact supported proposal, that the backend applied those terms once, and that any uncertainty after a timeout is preserved through handoff rather than guessed at." | 成功=持久业务效果；需证明授权、确切提议、一次效果、不确定性保留 |
| "If a change times out, can a human just repeat it?" | "Not blindly. The original might already have applied. The handoff has to say OUTCOME_UNKNOWN with O17 and the accepted terms, and the receiver reconciles against billing and service records first. Any authorized redelivery reuses O17 so downstream idempotency holds." | 不能盲目重复；对账；复用 O17 |
| "Better containment means we're winning, right?" | "Not by itself. A customer who gives up looks contained but isn't resolved, and a successful transfer to a person is good service even though it's not self-service. We measure verified resolution, issue-linked repeat contacts, satisfaction, handoff quality, and unauthorized actions separately." | 围堵≠解决；分开测量 |

---

# Case Study 3: Public-Sector Housing Document Processing｜案例三：公共部门住房申请文档处理

## 18. CS3 — The Case Study｜案例简报

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/NEOxrJB6Yvv

### 要点 / Key ideas

**Problem (English) — the brief**:
- **Customer**: the fictional national Housing Assistance Agency. About **400,000 applications/year**, **60% on paper**; some handwritten; **seven form versions** from the last 15 years still in circulation. Typical packet: application form, ID, payslips, tenancy agreement, utility bills.
- **Pain**: backlog of **140,000** applications; average processing time **11 weeks**; **600 caseworkers** spend most of their time typing and checking document data. The minister publicly promised processing **within four weeks within a year**.
- **Mandate**: cut processing time **without changing who decides eligibility** — caseworkers decide, applicants keep their right to appeal; every decision traceable to evidence.
- **Constraints**: citizen data stays **in-country, including during AI processing**; **security accreditation** required before the system touches real applications (security accreditation officer approves before launch); legacy case-management system has limited integration.
- **Stakeholders**: Agency Director (sponsor, political pressure); caseworkers (decide eligibility); security accreditation officer; legal counsel and records management (decisions, appeals, records rules); Head of Caseworkers and union (job-cut concerns); external auditor and ombudsman (post-launch review); journalists and ombudsman scrutinize unfair outcomes.
- 行业背景：Accenture Federal Services 与 Google Public Sector 的 **Gemini Launchpads** 计划把 FDE 嵌入联邦机构，把 AI 从试点推向生产（只是背景，不是本案客户）。本章对应 **Cloud Consulting FDE** 方向：多模态输入、大规模处理、主权 (sovereignty) 约束。

"读申请" 内含多种工作：识别表单版本 → 读取内容（不静默替换看似合理的值）→ 识别支持文件类型 → 为审查准备信息（保持建议值与支持材料的连接）。一张干净表单的演示不能代表 7 个版本和手写 (handwriting)的全国负载。

**四个数字度量不同东西**：140,000（积压的工作）/ 11 周（平均耗时 elapsed time）/ 600 人（工作力，主动工作 active effort）/ 4 周一年内（公开目标）。减少主动工作只在它构成延迟或限制吞吐 (throughput)时才帮助缩短耗时。对 Director 的回应："The typing and checking workload gives us a concrete place to investigate. I need the time distribution across the process before estimating its contribution to the four-week target."

**授权方向：受理与辅助 (intake and caseworker assistance)**：转录 (transcription，提议文件内容)、可能遗漏标记 (possible-omission flagging)、案件准备 (case preparation)。都帮助人完成工作，都不授予批准或拒绝的独立权力。

**诱人错误**："High-confidence applications will be approved or rejected automatically. Caseworkers will handle exceptions, so humans remain accountable." —— **读文档的置信度 (confidence)不能委托资格决定权**；例外处理意味着部分结果仍是自动决定的。改变授权只能通过机构的政策与治理流程，FDE 不能靠选置信度阈值 (confidence threshold)或把拒绝改名成 intake status 来获得。

**标记何时变成拒绝**：面试官提议 "Transcribe, flag a utility bill that was not located, prepare the packet, and reject automatically if the flag remains."

| 子句 (Clause) | 角色 (Role) |
|---|---|
| 提议文档转录 | 证据主张：提议的文件内容（仍需与提交证据核对） |
| 报告检查后未找到水电账单 | 证据主张：基于检查的可能遗漏（需知道检查了什么、是否完成；页面不可读 → "inspection incomplete" 而非 "absent"） |
| 提示 caseworker 检查可能遗漏 | 辅助输出：引导审查注意 |
| 准备案件包 | 辅助输出：组织材料 |
| 标记仍在则自动拒绝 | **资格决定：超出授权的自动不利结果** |

转变发生在**标记成为拒绝的充分触发条件**时——不管组件叫不叫 eligibility engine；把申请永久挡在 caseworker 视野之外也是同样问题。**缺少证据 ≠ 不合格。**

<svg viewBox="0 0 760 210" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect width="760" height="210" fill="#fff"/>
  <text x="380" y="22" font-size="14" text-anchor="middle" font-weight="bold">Where a flag becomes a decision｜标记何时越界成为决定</text>
  <rect x="20" y="50" width="220" height="70" rx="8" fill="#e6f4ea" stroke="#34a853"/>
  <text x="130" y="74" font-size="12" text-anchor="middle">Evidence claim 证据主张</text>
  <text x="130" y="94" font-size="11" text-anchor="middle">"Utility bill not located in</text>
  <text x="130" y="109" font-size="11" text-anchor="middle">the inspected packet"</text>
  <rect x="270" y="50" width="220" height="70" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="380" y="74" font-size="12" text-anchor="middle">Assistive output 辅助输出</text>
  <text x="380" y="94" font-size="11" text-anchor="middle">"Caseworker should inspect</text>
  <text x="380" y="109" font-size="11" text-anchor="middle">the possible omission"</text>
  <rect x="520" y="50" width="220" height="70" rx="8" fill="#fce8e6" stroke="#ea4335"/>
  <text x="630" y="74" font-size="12" text-anchor="middle">Agency decision 机构决定</text>
  <text x="630" y="94" font-size="11" text-anchor="middle">"The application is rejected"</text>
  <text x="630" y="109" font-size="11" text-anchor="middle">caseworker only 仅限 caseworker</text>
  <line x1="240" y1="85" x2="268" y2="85" stroke="#555" stroke-width="1.5"/>
  <line x1="490" y1="85" x2="518" y2="85" stroke="#ea4335" stroke-width="2" stroke-dasharray="5,3"/>
  <text x="505" y="145" font-size="12" text-anchor="middle" fill="#ea4335">✘ automatic rule here = unauthorized</text>
  <text x="380" y="180" font-size="12" text-anchor="middle" fill="#555">Caseworkers retain eligibility authority; applicants retain appeal rights</text>
  <text x="380" y="198" font-size="12" text-anchor="middle" fill="#555">caseworker 保留资格决定权；申请人保留申诉权</text>
</svg>

修复后的提议："Prepare proposed transcriptions and a review packet. If a utility bill is not located after a completed inspection of the submitted material, flag the possible omission with its inspection basis. Keep the flag contestable and route it to caseworker consideration. The caseworker retains the eligibility decision, and the applicant retains appeal rights."

**实质性审查 (substantive caseworker review)** 四个条件（共同作用，缺一不可）：检查证据（能看支持材料）/ 识别建议（机器值与已确认事实可区分）/ 更正或质疑（能改值、质疑遗漏、记录理由）/ 保留决定（工作流允许 caseworker 按机构规则作出结果，而不只是背书预定结果）。"The system will recommend rejection, but a caseworker will click approve" —— 名义上的点击不够；加第二次点击也修复不了不能改变结果的流程。"approved by caseworker" 记录只证明有批准，没说明证据依据。

**真实数据之前**：主权和认证 (accreditation)约束对辅助型方案同样适用。"The files stay in-country, so a real-data demonstration is safe" —— 本地存储只回答仓库位置；AI 请求可能把内容发到别处，处理、生成工件、诊断处理需要各自的位置证据。先确定：认证状态、处理边界（每步数据去哪）、未决部署事实（国家、正式安全分级 (security classification)、批准服务、允许的集成机制）。遗留集成受限不能成为绕过审查或用未批准服务的理由。批准前用**合成数据包 (synthetic packets)** 演示。

**干系人职责**：caseworkers（决定资格）/ 安全认证官（提供必需批准；FDE 提供证据不宣布审查完成）/ 法务与档案（决定、申诉、记录规则）/ caseworker 负责人与工会 (union)（裁员担忧；FDE 不承诺人员结果）/ 外部审计与 ombudsman（上线后审查）。FDE 负责澄清边界、识别未决问题、产出工程证据，并升级运行效果超出声明范围的提议。

### 面试怎么说 / How to say it in the interview

**90 秒授权复述 (mandate readback)**：
> "The agency processes about 400,000 applications a year, 60% on paper, with handwriting and seven form versions in circulation. There's a 140,000 backlog, an 11-week average, and 600 caseworkers spending most of their time typing and checking. The minister's target is four weeks within a year, and feasibility is unproven. The mandate supports intake completeness and caseworker assistance: proposed transcriptions, possible-omission flags, and prepared packets that stay inspectable and contestable. Caseworkers keep eligibility decisions, applicants keep appeal rights, and every decision is traceable to evidence. Citizen data stays in-country during AI processing as well as storage, and no real applications before accreditation. Before estimating impact or choosing an architecture, I need to know where the eleven weeks go, how varied the packets are, and what processing boundary is permitted."

中文：数字→目标未证→辅助型授权→权限与申诉→主权与认证→调研问题。

| 问题 (Question) | English answer | 中文 |
|---|---|---|
| "Auto-approve or reject high-confidence applications, and let caseworkers handle exceptions?" | "Reading confidence can't delegate eligibility authority — the mandate keeps that with caseworkers, and an exceptions-only model still decides some outcomes automatically. Changing that would need an agency policy decision, not a threshold I pick. What I can do is make caseworkers faster with pre-filled, evidence-linked packets." | 置信度不能委托决定权；改授权需政策决定 |
| "Reject automatically if the utility-bill flag remains." | "That's the exact point it stops being assistance. 'Not located after a completed inspection' is an evidence claim and 'please check' is assistance, but turning the flag into a rejection makes an eligibility decision. Missing evidence isn't the same as ineligibility. I'd keep the flag contestable and route it to the caseworker." | 标记→拒绝即越界 |
| "The system recommends rejection and a caseworker clicks approve — isn't that human-in-the-loop?" | "Only if the review is substantive: the caseworker can see the supporting evidence, tell machine suggestions from established facts, correct or contest them with a reason, and actually reach a different outcome. A click on a predetermined result isn't accountable review." | 实质审查四条件 |
| "The files stay in-country, so can we demo on real data?" | "Storage location is only one question. The AI call itself could send document content elsewhere, and accreditation is required before real applications regardless. Until we have accreditation and processing-location evidence for every step, I'd demo on synthetic packets." | 存储≠处理；先认证，用合成数据 |

---

## 19. CS3 — Discovery and Scoping｜需求调研与范围界定

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/xlBNgwXzr0l

### 要点 / Key ideas

"Why start with faster extraction when applicants wait eleven weeks?" —— 打字负担说明 caseworker 精力花在哪，但调研要确定**是什么让申请一直开着**。

**追踪申请流程**：受理 (Receipt) → 完整性检查 (Completeness checking) → 证据请求 (Evidence request) → 申请人回应 (Applicant response) → 恢复审查 (Resumed review) → 决定 (Decision)。每阶段区分：**主动工作 (active work)**、**机构队列等待 (agency queue)**、**等待文件 (waiting for documents)**。caseworker 访谈说明人做什么，流程记录说明何时发生——单一来源不完整。

**六个调研问题**：能看真实申请而非空白表单吗？11 周去哪了？正式安全分级是什么？哪些字段错误造成伤害？审计轨迹必须包含什么？如何公开证明公平 (fairness)？→ 证据请求：提交的申请包、流程记录、caseworker 访谈、批准的要求（分级、有害错误定义、审计义务、公平主张依据）。调研审查了 **500 份真实申请**——这是需求证据，**不授权 AI 系统处理公民数据**。

**500 份申请的发现**：**23 种文件类型**、**18% 手写**、约 **10% 扫描差或手机照片**、约 **30% 不完整**；**11 周的大部分时间在等待缺失文件**；最大机会是**在受理时捕捉缺失或无效文件**。

目标从 "extract document data faster" 变为 "**identify missing or invalid documents early enough to address them at intake**"；预填 (pre-filling) 仍有价值但成为辅助工作。百分比**不能相加**（一个不完整包也可能手写且照片差）；样本代表性 (sample representativeness)未确定，不能外推 (extrapolate)全国精确数量。只对干净打印表单有效的受理检查会恰好漏掉最需要帮助的包。

**同一包，更早的证据请求**：后发现路径（受理 → 排队 → caseworker 发现遗漏 → 请求 → 申请人提供 → 重新审查 → 决定）vs 受理发现路径（受理时就发现 → 更早请求 → 申请人仍需提供 → 审查 → 决定）。第二条路径创造了**更早解决同一问题的机会**，可能避免准备好又立即重开的案件；但**不能保证**申请人更快拿到文件、消除其他队列或清空积压。**不假设节省时长**，四周目标仍待测量。

三个观察回答不同问题：caseworker 分钟数减少（主动工作下降？）/ 受理时识别更多真正不完整包（检测提前？）/ 可比的受理到决定时间缩短（服务改善？）。第一个不能替代后两个。

**约定的试点**：**一个申请类型、一个区域办公室**；AI 预填并标记问题；**caseworker 审查并作出每个决定**。不承诺全部 7 个版本、全国推广或自动拒绝。申请类型名、办公室、时长、量化阈值待约定，不要用方便的假设填充。

**收入 vs 姓名拼写**：

| 字段 (Field) | 错误后果 (Consequence) | 要求 (Requirement) |
|---|---|---|
| 收入 (Income) | 可能改变资格、错误拒绝住房支持 | **接近完美 (near-perfect)**；看似合理的提取值仍可能误读工资单，审查需对照批准证据 |
| 姓名小变体 (Name variation) | 可通过与 ID 记录匹配解决 | 可容忍；但**未解决的身份不匹配不是无害的** |

**关键字段 (critical field)** = 错误会实质影响案件或申请人结果的字段。正确的常规字段会主导汇总准确率 (pooled accuracy)，隐藏一个关键的收入错误。分开测量**原始提取**与 **caseworker 审查后的正确性**（审查能修复错误但消耗精力；自信的建议也可能错误地通过审查）。**模型置信度描述模型输出；批准的证据确立正确性。** "near-perfect" 没有数值定义，需约定。

**六个成功指标（操作化定义）**：

| 指标 (Measure) | 操作定义 (Operational definition) |
|---|---|
| 处理时间 vs 相似的未用系统办公室 | 约定受理到决定边界；可比申请队列；含等待文件时间；**报告仍未结案的申请**（防止只决定简单案件造成假象） |
| 每申请 caseworker 分钟数 | 计入检查、更正、审查、处理标记、剩余打字；省下的打字可能被更正或误报 (false positives)工作抵消 |
| 受理时捕捉的不完整申请 | 分母 = **独立审查确认的真正不完整申请**；率 = 受理时正确识别的真正不完整 / 全部真正不完整；单独检查对完整申请的误报（不必要的证据请求加重负担） |
| 审查后关键字段准确率 | 每个关键字段单独对照批准参考值；记录正确/错误/缺失/未解决；**不能静默删除未解决案例** |
| 任何群体准确率不下降 | 对手写、打印、语言群体用一致定义对比相关基线；保留字段级结果；显示样本量与不确定性，小群体报告 "insufficient observations" |
| 申诉不增加 | 约定申诉率定义、可比已决队列、**足够的跟进窗口**；没有成熟申诉观察的试点不能证明此项 |

六个指标**不能互相抵扣**：省力不能抵消关键字段更差、群体退化或申诉增加；缺失观察 = 未证明，不是通过。

**审核面试官说法**："The extractor reads forms faster and has high overall accuracy, so the pilot has met the minister's target." —— 速度与汇总准确率 ≠ 服务结果；只算完成的值排除未解决是偏差 (bias)；用最新快速演示定论而不等完整性与申诉观察也是偏差。

**对比办公室与群体**：可比性 (comparability)检查——申请类型、负载构成（复杂度、完整性、输入质量）、人员（容量或工作方式变化）、观察期。两个办公室都做前后基线会更强；**两个都改善时不能把试点办公室的全部改善归功于 AI**。群体报告回答"谁受益、谁更差"；汇总更好不能补偿手写或某语言群体的退化。

**分级结论**：数据为**敏感 (sensitive) 而非机密 (classified)** → 允许**有严格控制的国内云区域 (in-country cloud region)**，不需要完全断网。追加到记录作为之前问题的解答（保留原记录）。这缩小了部署要求，但不选定产品也不证明在未指定国家的服务可用性。剩余批准问题：标记证据（什么检查材料与完整性规则支持缺失/无效标记）、更正记录（按档案规则保留什么）、公开公平主张（群体定义、基线、观察、局限）、认证证据。

### 面试怎么说 / How to say it in the interview

**90 秒范围辩护**：
> "The review of 500 applications found 23 document types, 18% handwritten forms, about 10% poor scans or phone photos, and about 30% incomplete applications. Most of the elapsed time is waiting for missing documents, so the main objective becomes catching missing or invalid evidence at intake. Faster pre-filling is still useful, but it can't by itself take us from eleven weeks to four. The pilot is one application type in one regional office: AI pre-fills and flags problems, and caseworkers review and make every decision. Success is measured separately on processing time against a comparable office, caseworker minutes, intake detection of truly incomplete applications, critical-field accuracy after review, no group getting worse, and no rise in appeals. Sensitive classification allows an in-country cloud region with strict controls, but product fit, thresholds, and accreditation still need agreement."

中文：发现→目标转向受理完整性→试点边界→六指标→分级结论与待定项。

| 问题 (Question) | English answer | 中文 |
|---|---|---|
| "The extractor is faster with high overall accuracy — have we met the minister's target?" | "Not yet. Speed and pooled accuracy describe extraction, not receipt-to-decision time. Most delay is waiting for documents, and pooled accuracy can hide a wrong income value or worse handwriting performance. We need comparable processing-time data, critical-field results after review, group results, and mature appeal observations before claiming the target." | 提取指标≠服务结果 |
| "Why does income need near-perfect accuracy but names don't?" | "A wrong income figure can change eligibility and wrongly deny someone housing support. A small name spelling variation gets resolved against the ID record. That's why I track critical fields individually instead of one pooled accuracy number — though an unresolved identity mismatch still isn't harmless." | 收入影响资格；姓名可对照 ID |
| "How do you measure intake detection?" | "The denominator is applications independently confirmed as truly incomplete, and the rate is how many of those we flagged at intake. I'd track false flags on complete applications separately, because unnecessary evidence requests burden applicants and caseworkers." | 分母=真正不完整；误报单独看 |
| "Both offices improved — does the AI get credit?" | "Not all of it. If the comparison office also improved, something shared across the agency is at work. I'd use before-and-after baselines at both, check that workload mix and staffing were comparable, and attribute only the difference." | 只归因差值 |

---

## 20. CS3 — The System Design Round｜系统设计轮

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/7Dqz2n76QvA

### 要点 / Key ideas

**Problem (English)**: Design the one-application-type, one-regional-office pilot: document flow from arrival to caseworker; how workers know which fields to trust; sovereign deployment; and the evidence that explains an incomplete flag to an auditor. (Try it first: 20 minutes.) Interviewer adds **packet A17**: form, ID, payslips, tenancy agreement, and a utility-evidence photo that is **unreadable**. Declared income is **1,800**; the payslip visibly shows **1,800**, but extraction suggests **7,800 with confidence 0.99**. A clearer utility attachment arrives later.

```text
Input packet A17 (state 1):
  form (declared income = 1800), ID, payslip (visible total = 1800),
  tenancy agreement, utility photo (unreadable)
Extraction: payslip.income = 7800, confidence = 0.99
Expected system behavior:
  utility -> "possible omission; inspection incomplete (photo unreadable)"; re-upload requested
  income  -> mismatch 1800 vs 7800 highlighted; critical field requires caseworker confirm/correct
  caseworker corrects to 1800 (original 7800 suggestion preserved)
Packet A17 (state 2): clearer utility attachment -> rerun affected stages, keep earlier finding
```

**八阶段流水线 (eight-stage workflow)**：

<svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect width="800" height="400" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">CS3: Housing Document Pipeline｜住房申请文档处理架构</text>
  <rect x="20" y="40" width="760" height="230" rx="10" fill="#f8fbff" stroke="#4285f4" stroke-dasharray="6,4"/>
  <text x="400" y="57" font-size="12" text-anchor="middle" fill="#4285f4">In-country boundary｜国内边界：agency-held keys · network restrictions · in-country logs</text>
  <rect x="35" y="70" width="165" height="62" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="117" y="90" font-size="12" text-anchor="middle">1 Intake quality</text>
  <text x="117" y="107" font-size="11" text-anchor="middle">blur/orientation/pages</text>
  <text x="117" y="122" font-size="11" text-anchor="middle">受理质检 + 重传请求</text>
  <rect x="220" y="70" width="165" height="62" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="302" y="90" font-size="12" text-anchor="middle">2 Classify + split</text>
  <text x="302" y="107" font-size="11" text-anchor="middle">doc units → page map</text>
  <text x="302" y="122" font-size="11" text-anchor="middle">分类与拆分</text>
  <rect x="405" y="70" width="165" height="62" rx="8" fill="#fef7e0" stroke="#fbbc04"/>
  <text x="487" y="90" font-size="12" text-anchor="middle">3 Structured extract</text>
  <text x="487" y="107" font-size="11" text-anchor="middle">source anchor + conf</text>
  <text x="487" y="122" font-size="11" text-anchor="middle">Document AI first</text>
  <rect x="590" y="70" width="175" height="62" rx="8" fill="#fef7e0" stroke="#fbbc04"/>
  <text x="677" y="90" font-size="12" text-anchor="middle">4 Cross-doc validate</text>
  <text x="677" y="107" font-size="11" text-anchor="middle">name↔ID, income↔payslip</text>
  <text x="677" y="122" font-size="11" text-anchor="middle">跨文档校验</text>
  <rect x="590" y="160" width="175" height="62" rx="8" fill="#fce8e6" stroke="#ea4335"/>
  <text x="677" y="180" font-size="12" text-anchor="middle">5 Completeness + notify</text>
  <text x="677" y="197" font-size="11" text-anchor="middle">versioned rules</text>
  <text x="677" y="212" font-size="11" text-anchor="middle">omission / invalid / incomplete</text>
  <rect x="380" y="160" width="190" height="62" rx="8" fill="#e6f4ea" stroke="#34a853"/>
  <text x="475" y="180" font-size="12" text-anchor="middle">6 Caseworker review</text>
  <text x="475" y="197" font-size="11" text-anchor="middle">field → page crop link</text>
  <text x="475" y="212" font-size="11" text-anchor="middle">critical: confirm/correct</text>
  <rect x="190" y="160" width="170" height="62" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="275" y="180" font-size="12" text-anchor="middle">7 Legacy write</text>
  <text x="275" y="197" font-size="11" text-anchor="middle">reviewed state only</text>
  <text x="275" y="212" font-size="11" text-anchor="middle">export id + reconcile</text>
  <rect x="35" y="160" width="135" height="62" rx="8" fill="#ede7f6" stroke="#7e57c2"/>
  <text x="102" y="180" font-size="12" text-anchor="middle">Caseworker</text>
  <text x="102" y="197" font-size="11" text-anchor="middle">decides eligibility</text>
  <text x="102" y="212" font-size="11" text-anchor="middle">资格决定</text>
  <line x1="200" y1="101" x2="218" y2="101" stroke="#555" stroke-width="1.5"/>
  <line x1="385" y1="101" x2="403" y2="101" stroke="#555" stroke-width="1.5"/>
  <line x1="570" y1="101" x2="588" y2="101" stroke="#555" stroke-width="1.5"/>
  <line x1="677" y1="132" x2="677" y2="158" stroke="#555" stroke-width="1.5"/>
  <line x1="590" y1="191" x2="572" y2="191" stroke="#555" stroke-width="1.5"/>
  <line x1="380" y1="191" x2="362" y2="191" stroke="#555" stroke-width="1.5"/>
  <line x1="475" y1="222" x2="102" y2="224" stroke="#7e57c2" stroke-width="1.2" stroke-dasharray="4,3"/>
  <rect x="35" y="235" width="730" height="28" rx="6" fill="#ede7f6" stroke="#7e57c2"/>
  <text x="400" y="254" font-size="12" text-anchor="middle">8 Audit records persisted THROUGHOUT stages 1–7｜审计贯穿全流程（源位置、模型版本、置信度、编辑）</text>
  <rect x="20" y="290" width="370" height="95" rx="10" fill="#fff" stroke="#9aa0a6"/>
  <text x="205" y="310" font-size="12" text-anchor="middle" font-weight="bold">Service-location gate｜服务位置门</text>
  <text x="205" y="330" font-size="11" text-anchor="middle">Newest Custom Extractor: Preview, US+EU processing</text>
  <text x="205" y="348" font-size="11" text-anchor="middle">→ blocked unless in-country evidence</text>
  <text x="205" y="366" font-size="11" text-anchor="middle">alt: older in-country version / GDC / keep blocked</text>
  <rect x="410" y="290" width="370" height="95" rx="10" fill="#fff" stroke="#9aa0a6"/>
  <text x="595" y="310" font-size="12" text-anchor="middle" font-weight="bold">Evaluation｜评估</text>
  <text x="595" y="330" font-size="11" text-anchor="middle">raw vs post-review critical-field accuracy</text>
  <text x="595" y="348" font-size="11" text-anchor="middle">groups: doc type · handwriting · language · scan</text>
  <text x="595" y="366" font-size="11" text-anchor="middle">worst-group floor AND no-group-drop · calibration</text>
</svg>

| 阶段 (Stage) | 要点 (Key points) |
|---|---|
| 1 受理质检 (Intake quality checks) | 接受扫描、上传、手机照片；保存原件、受理时间、包 ID、页清单；检查模糊、方向、预期页；A17 不可读照片 → 通过批准流程**立即请求重传** |
| 2 分类与拆分 (Classification & splitting) | 把混合包拆成按类型标注的文档单元；保留到原文件、修订、页的映射；不确定分类送检查而不是随便指定 |
| 3 结构化提取 (Structured extraction) | 填入约定 schema；每个建议保留**源锚点 (source anchor，精确页面位置)**、源修订、提取版本、字段置信度 |
| 4 跨文档校验 (Cross-document validation) | 表单姓名 vs ID、申报收入 vs 工资单、日期 vs 机构批准的有效期规则；A17 产生收入不匹配 1,800 vs 7,800 |
| 5 完整性检查与通知 | 对已检查的包应用**版本化**、机构批准的证据要求；通过批准的申请人通知流程立即提示问题；重大证据请求权仍在 caseworker |
| 6 证据链接的 caseworker 审查 | 每个字段链接到精确源页位置；低置信与不匹配高亮；**每个关键字段必须确认或更正**；自信字段也保持可见 |
| 7 遗留系统写入 | 只导出审查后的案件状态（支持的 API 或批处理）；记录导出 ID 与回执 (receipt)；投递不确定时按该 ID 对账 (reconcile)再声称成功或重复 |
| 8 审计记录 | **贯穿 1–7 持续保存**，不能等最后一步成功才写 |

**三种观察要区分**：已知缺页（已建立的页预期未满足）/ 不可读页（材料到了但内容无法充分检查）/ 未知构成（无法确定包含哪些文件）。A17 的合理主张："utility evidence inspection incomplete"——**不是** "applicant supplied no utility evidence"。完整性结果分开：可支持的可能遗漏 / 无效证据 / 检查不完整。否则技术读取失败会变成关于申请人提交了什么的无依据主张。

更清晰的附件到达 → **创建新包状态 (packet state 2)**，重跑受影响的分类、提取、校验、完整性检查；**保留早先的结果和通知**——新证据改变评估，但不抹去之前干预的原因。

**关键字段审查的记录契约**（课程示例，Python 标准库；只演示记录结构，不调用提取服务）：

```python
from copy import deepcopy

suggestion = {
    "packet": "A17", "field": "income", "value": 7800,
    "source": {"document": "payslip", "revision": 1,
               "page": 1, "crop_id": "income-total"},
    "model_version": "candidate-version", "confidence": 0.99,
    "critical": True,
}
review = None


def ready(field, disposition):
    # Critical fields need a recorded confirmation or correction; confidence has no bypass.
    return not field["critical"] or (
        disposition is not None
        and disposition["action"] in {"confirmed", "corrected"}
    )


assert not ready(suggestion, review)          # 0.99 confidence still requires review
original = deepcopy(suggestion)
review = {"action": "corrected", "value": 1800,
          "reviewer": "caseworker-17", "reason": "Inspected payslip crop"}
assert suggestion == original                 # machine suggestion is preserved, not overwritten
assert ready(suggestion, review)
```

生产门还需证明：审查者权限、已检查源、绑定源版本、持久化——伪造的 review 字典也能通过这个小函数。

**审计员问 "Why was A17 flagged?" 需要的链**：原始输入（包状态 1、文件页、不可读照片）→ 检查结果（哪些页成功/失败）→ 结论（完整性规则版本、检查范围、可能遗漏、显式的检查不完整限制）→ 动作（通知内容、投递状态、caseworker 授权的证据请求）→ 修订（包状态 2 及其新处理结果，链接到早先结论）→ 处置（审查者、理由、检查附件后认定水电要求满足）。**缺失的文件没有源页链接**——遗漏结论需要检查范围与适用要求；不可读照片有真实源锚点解释为何检查不完整。保留原始建议（包括 7,800）、审查值与单独的人工资格决定，申诉审查能看到证据历史而不只是最终数据库行。

**捷径方案的失败**："store locally, send the mixed packet to the newest remote extractor, accept 7,800 at 0.99, call the photo missing, and export rejection with final values logged" —— 缺推理位置证据、缺源确认、合并了检查状态、取代了 caseworker 权限、缺更正历史。**提高置信度阈值一个都修不了。**

**当错误读数一致时**（多选测验）：两份提取都错成 7,800 → **收入比较会通过**；原始 1,800 vs 7,800 比较会标记不匹配但仍需源检查。0.99 不代表 99% 正确概率（需要对独立参考做**校准 (calibration)**）；跨文档校验对一致的错误无效。所以**强制的基于源的关键字段审查 + 独立确立的参考值**仍然必要。更正后：重跑依赖收入的检查，作废仍含 7,800 的待导出数据；审查绑定到检查过的源修订，替换文件不能静默继承过时的确认。A17 保留为回归用例。

**难输入评估**：原始提取与审查后正确性分开；每个关键字段保留正确/错误/缺失/未解决。群体结果（文件类型、手写、语言、扫描质量，报告数量与不确定性）；**最差群体下限 (worst-group floor)** 且**无群体下降 (no group drop)**——一个群体可以高于下限但相对基线退化，两条都要满足；置信度校准（置信区间 vs 实际正确率，显式报告像 A17 这样的高置信错误）；更正标签在档案控制下验证后才作为候选标签——**每次编辑都自动重训可能学到审查者的错误**。保留六个服务指标。

**定位 A17 的每个操作**：提议**机构持有密钥 (agency-held encryption keys)**、网络限制只到批准服务、国内日志。条件化位置清单：受理与原件（上传、扫描传输、原文件、元数据）/ 变换（分类、拆分、提取推理、页面裁剪、可选 Gemini 请求）/ 流程与审查（队列、派生字段记录、审查界面、通知、遗留导出）/ 运维与保留（日志、备份、评估导出、支持处理、依赖服务）。每项记录处理的公民数据、实际处理位置、选定服务与版本、控制、认证所需证据；未确定前标记未决。**存储区域设置或机构密钥本身不能证明推理位置或支持路径。** 真实数据边界未批准前用合成包。

**先评估 Document AI**："Why not use Document AI instead of prompting Gemini directly?" Document AI 含 OCR (optical character recognition)、Form Parser，以及基于 Gemini 的 **Layout Parser、Custom Extractor、Classifier、Splitter**；Custom Extractor 支持零样本 (zero-shot)、少样本 (few-shot)或微调 (fine-tuned) schema 学习并返回**每字段置信度**。它的分类、拆分、结构化提取、置信度、字段到页面链接契合审查契约 → 先评估（测试实际输出，不假设产品名保证锚点与质量）。直接 Gemini 只用于证明的缺口（跨文档推理、简短案件摘要），同样遵守源证据与位置要求；批准规则足够的地方用确定性比较。比较维度：质量（关键字段、难输入群体）、集成与可审计性（schema 映射、页锚点、版本记录、更正处理）、运维负担与成本、允许的执行位置。结论：**有条件的 Document AI 优先**。

**阻止不允许的提取器**：按 2026-10 设定，最新 Custom Extractor 使用 Gemini 3.5 Flash、处于 **Preview**、AI 处理在 **US 和 EU**。机构国家未指定，两个区域都需满足其国内边界 → 未满足就阻止。替代：在确认国内可用后评估旧版本；或评估 **Google Distributed Cloud** 适用性（不假设托管 Document AI 能在其上运行）；否则真实数据处理保持阻止。机密数据反事实：**GDC air-gapped**（Gemini 3.5 Flash 在其上 GA (generally available)）——成本更高、机构运维更多、模型选择更少；实际的敏感分级不需要断网。

**成本：480 万页**（课程给的 US Custom Extractor 示例：每申请约 12 页、$30 / 1,000 页，本地价格可能不同）：

| 量 (Quantity) | 计算 (Calculation) |
|---|---|
| 年页数 | 400,000 × 12 = **4,800,000 页/年** |
| 年提取费用 | 4,800,000 ÷ 1,000 × $30 = **$144,000/年**（全国量示例，不是报价或试点预算） |
| 总成本 | C_total = C_extraction + C_other_processing + C_storage + C_network + C_logging + C_security + C_integration + C_operations + C_human_review |
| 节省小时 | 若实测净节省分钟 s/申请：400,000 × s / 60 小时/年（净值含更正与误报工作） |

节省小时不等于现金节省或更短的受理到决定时间。

**容量与截止**：4.8M ÷ 365 ≈ **13,151 页/天**——年均值不能用来规划截止期峰值，全国量与试点负载也不同。需要峰值到达窗口与页数分布，然后设计：准入（下游排队时也持久确认受理）、处理（有界队列、提取吞吐、服务配额 (quota)、重试预算 (retry budget)）、恢复（峰值或中断后积压清空目标）、审查（caseworker 确认/更正/标记容量）。窗口 P 页 + 已积压 B 页 + 清空目标 T 小时 → 所需成功吞吐 ≥ **(P + B) / T 页/小时**；重试消耗额外容量；**更快的提取可能只是把队列移到 caseworker**。

**新表单版本**：检测或安全路由未知版面；版本化的 schema 映射与完整性规则；关键字段与受影响群体评估；门禁发布 (gated release)；旧映射不能静默重新解释新字段。**倾斜的工资单照片**：检查能否确立可读性，不能就请求更好的拍摄或送审查；几何校正只有在结果证据可读且可评估时才有用。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "Walk me through the pipeline." | "Eight stages inside an in-country boundary: intake quality checks that request a re-upload for unreadable pages; classification and splitting with a page map; structured extraction where every value keeps a source anchor, version, and confidence; cross-document validation like income against payslips; versioned completeness rules with early applicant notification; an evidence-linked caseworker screen where every critical field must be confirmed or corrected; a legacy write of reviewed state only, reconciled by export ID; and audit records written throughout, not at the end." | 八阶段；源锚点；关键字段强制审查；审计贯穿 |
| "How do you catch confidently wrong income — even if both readings agree on 7,800?" | "Cross-document validation catches the 1,800-versus-7,800 case, but if both readings are wrong it passes. That's why every critical field requires the caseworker to confirm or correct it against the linked payslip crop, regardless of confidence. A 0.99 score isn't a 99% probability without calibration, so I'd report high-confidence errors explicitly and keep A17 as a regression case." | 强制源审查；置信度需校准 |
| "Why was A17 flagged, and how was it resolved?" | "Packet state one had an unreadable utility photo, so the finding was 'possible omission, inspection incomplete' — linked to the completeness rule version and the unreadable page, not 'applicant supplied nothing.' We requested a re-upload. The clearer attachment created packet state two, we reran the affected checks, and the caseworker recorded that the requirement was met — with the earlier finding preserved." | 包状态链；检查不完整≠未提交 |
| "What proves every citizen-data operation stays in-country?" | "Not a storage setting. I'd build a location inventory for every component that touches A17 — intake, extraction inference, crops, queues, the review UI, notifications, logs, backups, support access — with the actual processing location, service version, and controls like agency-held keys and network restrictions. Anything unproven is marked unresolved, and real data waits for accreditation." | 逐组件位置清单；存储设置不够 |
| "Why evaluate Document AI before prompting Gemini directly?" | "Its classifier, splitter, Custom Extractor with per-field confidence, and field-to-page links match the review contract we need. I'd test its actual anchors and quality on our hard groups. But the newest Custom Extractor is in Preview and processes in the US and EU, so unless there's in-country evidence it's blocked — then I'd look at an older in-country version or Google Distributed Cloud, or keep real data blocked." | 契合审查契约；但位置不满足就阻止 |
| "How do you handle deadline spikes?" | "The annual average — about 13,000 pages a day — can't size a spike. I'd get the peak arrival window and page distribution, acknowledge receipt durably even while work queues, and size throughput as at least backlog plus window pages over the drain target. And I'd size caseworker review capacity too, since faster extraction can just move the queue to them." | 峰值≠均值；(P+B)/T；审查容量 |
| "What does a national rollout cost?" | "As an illustration at the US rate: 400,000 applications times about 12 pages is 4.8 million pages, which at 30 dollars per thousand is about 144,000 dollars a year for extraction alone. Total cost adds storage, network, logging, security, integration, operations, and human review. Hours saved is 400,000 times net minutes saved over 60 — net of correction and false-flag work." | 144K 仅提取；总成本公式 |

---

## 21. CS3 — The Googleyness Round｜Googleyness 轮（公共问责四个场景）

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/RMRqlBBEPyR

### 要点 / Key ideas

在压力下保持四个要素可听见：**有支持的事实 (supported fact)、你能控制的行动 (action within your control)、授权的决策者 (authorized decision owner)、剩余的不确定性 (remaining uncertainty)**。

**"minutes" 是什么意思**：Director 想宣布 "AI now processes applications in minutes"。"AI" 是主语、"processes applications" 听起来像完成了服务、"in minutes" 给出了耗时结果 → 公民会理解为几分钟拿到资格决定。分开**三个时钟**：

| 时钟 (Clock) | 含义 (Meaning) |
|---|---|
| 提取时间 (Extraction time) | 从文档生成机器建议的时间 |
| 准备时间 (Preparation time) | 组装、检查、更正案件以供决定的时间 |
| 受理到决定 (Receipt-to-decision) | 含队列、证据请求、申请人回应、审查、资格决定的总耗时 |

场景中**没有测量到的 "minutes" 结果**；11 周和 4 周都不是本系统已实现的改进。公众压力不扩大试点范围。

**手写错误（单独的场景分支）**：早期证据显示手写表单错误更多，大多来自老年申请人；记者问 AI 是否有偏见。没有提供数值差距、因果结论 (causal conclusion)或完成的修复。证据支持"观察到与手写相关的错误差距"和对不平等服务的担忧。未知：幅度（评估了多少包和字段、错误定义）、机制（手写、图像质量、表单版本、语言、交互因素？）、审查（caseworker 检查后还剩哪些错误）、申请人结果（是否造成额外请求、延迟、错误决定、申诉）。**年龄没有被确立为原因**。"总体准确率高所以没偏见" 会掩盖差距。也要问这个证据的来源——不能据此推断试点已获认证并处理了真实申请。

先**承认差距**再讲不确定性（先讲缺失统计听起来像回避）。不必等完整因果解释就要行动。

**立即改变**：公开报告差距，**手写表单走更完整的人工审查**直到修复。更完整审查需要：源访问（原页与字段锚点，包括看似自信的建议）、审查容量（工作分配给时间）、更正权限（能拒绝机器建议并更新依赖检查，保留证据历史）、负担检查（衡量额外审查是否造成更长等待或不必要的证据请求）。**保持每个包每个关键字段都确认/更正**——打印包不因此豁免。**按文档特征路由，不按年龄路由**（否则把观察到的关联变成关于人的无依据规则）。"review completed" 状态不能弥补不可访问的源页或没时间检查的队列。

**工会担忧裁员 (layoffs)**：避免 "No jobs will be lost" 和 "Automation inevitably means fewer caseworkers"——都不由工程范围推出。人员决定属于授权的机构领导。可以具体化工作变化：哪些打字任务改变、还剩哪些审查与更正工作、需要什么培训、建议错误时谁负责；确保效益估算包含审查与更正工作量。**减少打字可能把工作转移到检查、更正或证据请求**。会议邀请或未答复的转交是协调进展，不是解决。

**拒绝真实数据捷径**：较小数据集、本地存储、Director 支持或 "pilot" 一词都不能移除认证要求。替代：**完全合成的数据包**（凭空制造，而不是通过未批准路径从公民档案派生）、**尽早的安全审查**、**真正更小的首版范围**（现有范围已是一类申请一个办公室，再缩小需说明具体排除什么，仍需批准）。

**表面安抚的错误简报**："Overall accuracy is high, so there is no bias; human review guarantees nobody is harmed; AI handles applications in minutes; no caseworker jobs will be lost; we can use a few real files while approval catches up." —— 每句都改变了证据或超出权限。光改措辞修复不了：审查流程、人员问题归属、真实数据门必须改变或保持执行；但完全拒绝帮助也会放弃权限内的有用工作。

### 面试怎么说 / How to say it in the interview — 题库（每题 STAR 风格英文模型答案）

**Q1. Journalist: "Early data shows more errors on handwritten forms, mostly from older applicants. Is the agency's AI biased against older people?"**
> **Situation/Task:** "There's a real, observed gap, and my job is to make sure it's disclosed accurately and acted on, without overstating or understating it.
> **Action:** I'd give the agency's communication channel this account: the early evaluation shows more errors on handwritten forms, and many of those come from older applicants. That gap matters and should be reported openly. What we don't yet know is its size, whether age is actually the cause, or its effect on final decisions. Meanwhile I'd recommend fuller source-based human review for handwritten packets, working with caseworker leadership on evidence access, inspection time, and correction authority, while keeping critical-field review on every packet — and routing by document type, not by age. I'd also check whether the extra review creates delays for those applicants.
> **Result:** Caseworkers still decide eligibility and applicants keep appeal rights. I can't honestly say harm has been eliminated or the problem is solved — only that it's disclosed and being worked."

中文：承认差距→说明未知→立即加强手写审查→按文档特征路由→不说已解决。

**Q1 follow-up. "So can you assure older applicants that nobody has been harmed?"**
> "I can't give that assurance from these findings. I can commit to surfacing the gap and proposing the review and investigation work within my role. The agency needs verified reviewed-field and applicant-outcome evidence before making any claim about harm."

中文：不能保证；承诺暴露与调查；需要结果证据。

**Q2. Director: "I want to announce that 'AI now processes applications in minutes.' Can you help me make that announcement?"**
> **Situation/Task:** "The Director legitimately needs to show progress, but that sentence would be heard as 'you get a decision in minutes.'
> **Action:** I'd say yes, I'll help — with accurate wording. The system assists preparation and evidence checking; caseworkers still decide; and we don't have a measured 'minutes' result. I'd propose something like: 'The agency is piloting AI-assisted application preparation for one application type in one regional office. Caseworkers continue to make every eligibility decision. Real-data use remains subject to security accreditation and in-country processing.' The 11-week baseline and the four-week goal are described separately as starting point and target.
> **Result:** The Director gets a usable message now, and if we later measure preparation time, I'll help state the task, cohort, conditions, and result precisely."

中文：帮忙但改为准确措辞；说明范围与条件；基线与目标分开。

**Q2 follow-up. "If extraction is fast, why can't we just say 'minutes'?"**
> "A measured extraction time could support a narrowly worded extraction claim — with its start and end points, packet population, and conditions. But it still says nothing about review or receipt-to-decision time. And right now we don't even have that extraction measurement."

中文：提取时间≠决定时间；且尚无测量。

**Q3. Union: "Is this system the first step toward cutting caseworker jobs? Can you promise there will be no job cuts?"**
> **Situation/Task:** "The fear is legitimate, and the honest answer is that staffing isn't my decision.
> **Action:** I'd say: 'I can't promise there will be no job cuts — staffing belongs to authorized agency leadership. The agreed scope assists case preparation and checking, and caseworkers keep eligibility decisions, but that doesn't settle future staffing policy.' Then I'd offer something concrete: work with the Head of Caseworkers and the union to document which typing tasks change, what review and correction work remains, what training is needed, and who's responsible when suggestions are wrong — and make sure benefit estimates include that correction effort. I'd take the staffing question to the leaders who can answer it.
> **Result:** The union gets an inspectable account of the work change and a route to the real decision owner, rather than a reassurance I can't back."

中文：不承诺人员；具体化工作变化；转交授权决策者。

**Q3 follow-up. "If you won't promise jobs are safe, why should we support the pilot?"**
> "You should have an accurate account of the proposed work and an answer from the agency's staffing decision owners. I can document the task changes and open questions, and make sure the pilot measures the actual workload. I can't substitute an engineering reassurance for an agency commitment."

中文：给准确信息和真正决策者，不给虚假安抚。

**Q4. Colleague: "Accreditation is taking too long. Why don't we pilot on a few real applications now and finish approval afterward?"**
> **Situation/Task:** "Accreditation is a prerequisite for real data, not paperwork we can finish later, and that applies to a small test too.
> **Action:** I wouldn't process real applications before accreditation. We can still make real progress: run wholly synthetic packets through extraction, source-linked review, corrections, and a legacy-interface rehearsal; bring the processing-location inventory and security evidence to the accreditation officer early; and, if helpful, propose a genuinely smaller first scope with explicit exclusions — which would still need approval.
> **Result:** Real-data processing stays blocked, the service-version and in-country questions stay visible in the plan, and I help assemble the evidence — but I can't grant accreditation or promise a date."

中文：不在认证前用真实数据；合成数据+早期安全审查+更小范围。

**Q4 follow-up. "Why not just ten real applications stored locally?"**
> "Ten real applications are still citizen data, and local storage says nothing about where the AI processing happens. I'd keep that blocked and offer the synthetic rehearsal while the accreditation officer reviews the evidence."

中文：十份也是公民数据；存储≠处理。

---

## 22. CS3 — Debriefing the Case Study｜三案例横向复盘

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/m7Ro7XPNr93

### 要点 / Key ideas

**决策不变量 (decision invariant)** = 跨实现变化仍成立的义务。"确定谁能授权一个动作" 是不变量；"用路由器" 是实现选择。混淆两者会产出图一样但各自违背不同客户需求的系统。

**可复用的决策序列**：
1. 确定预期结果及其决策者 (intended outcome & decision owner)
2. 发现真实瓶颈或歧义 (actual bottleneck or ambiguity)
3. 识别权限、数据、处理边界 (authority, data, processing boundaries)
4. 评估最简单合适的托管基线 (simplest suitable managed baseline)
5. 定义失败处理与人工路径 (failure handling & human path)
6. 发布声明前要求任务证据与负责的验收 (task evidence & responsible acceptance)

**五个共同模式**：调研改变了问题；Google 托管产品是起点；权限在模型之外强制；准确性需要真实任务数据与清晰定义；人保留对重大决策的控制。

**三案例六属性对比**：

| 属性 (Attribute) | 零售 (Retail) | 电信 (Telecom) | 机构 (Agency) |
|---|---|---|---|
| 主要输入 (Main input) | 结构化 SQL 数据 → 在批准含义与权限下查询 | 对话 → 把请求绑定到已验证账户范围 | 文档与图片 → 保留源链接供检查 |
| 编排 (Orchestration) | 单 agent → 语义与执行控制在生成之外 | 路由 + 专家 → 隔离故障、保留操作状态 | 流水线 + 人工审查 → 每个关键字段确认或更正 |
| 最难约束 (Hardest constraint) | 指标定义与权限 → owner 批准的语义 + 强制范围 | 监管与账户安全 → 操作级权限与恢复 | 主权 (sovereignty)与问责 (accountability) → 可接受的处理 + 可审计审查 |
| 托管基线 (Managed baseline) | Conversational Analytics API | Customer Engagement Suite | Document AI |
| 调研变化 (Discovery change) | 冲突的批准含义 → 解决定义，而非只改进模型 | 操作风险层级 → 决定哪里允许生成与动作 | 不完整申请的等待 → 更早检测完整性问题 |
| 发布证据 (Release evidence) | 语义、结果、授权、扫描上限证据 | 解决、动作安全、恢复、人工可达、处理证据 | 源链接审查、关键字段、群体、服务结果、位置、认证证据 |

<svg viewBox="0 0 780 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect width="780" height="300" fill="#fff"/>
  <text x="390" y="22" font-size="14" text-anchor="middle" font-weight="bold">One decision sequence, three mechanisms｜同一决策序列，三种机制</text>
  <rect x="20" y="40" width="740" height="56" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="390" y="62" font-size="12" text-anchor="middle">Outcome+owner → real bottleneck → authority/data/processing bounds → managed baseline → failure+human path → evidence+acceptance</text>
  <text x="390" y="82" font-size="12" text-anchor="middle">结果与决策者 → 真实瓶颈 → 边界 → 托管基线 → 失败与人工路径 → 证据与验收</text>
  <line x1="140" y1="96" x2="140" y2="125" stroke="#555" stroke-width="1.5"/>
  <line x1="390" y1="96" x2="390" y2="125" stroke="#555" stroke-width="1.5"/>
  <line x1="640" y1="96" x2="640" y2="125" stroke="#555" stroke-width="1.5"/>
  <rect x="20" y="127" width="240" height="150" rx="10" fill="#e6f4ea" stroke="#34a853"/>
  <text x="140" y="150" font-size="13" text-anchor="middle" font-weight="bold">Retail｜零售</text>
  <text x="140" y="172" font-size="12" text-anchor="middle">Resolve MEANING</text>
  <text x="140" y="192" font-size="11" text-anchor="middle">owner-approved net_sales contract</text>
  <text x="140" y="210" font-size="11" text-anchor="middle">row policies + byte cap B</text>
  <text x="140" y="232" font-size="11" text-anchor="middle" fill="#ea4335">open: B unapproved,</text>
  <text x="140" y="250" font-size="11" text-anchor="middle" fill="#ea4335">300-Q eval not run</text>
  <rect x="270" y="127" width="240" height="150" rx="10" fill="#fef7e0" stroke="#fbbc04"/>
  <text x="390" y="150" font-size="13" text-anchor="middle" font-weight="bold">Telecom｜电信</text>
  <text x="390" y="172" font-size="12" text-anchor="middle">Reconcile a WRITE</text>
  <text x="390" y="192" font-size="11" text-anchor="middle">session-bound authority, Q17/O17</text>
  <text x="390" y="210" font-size="11" text-anchor="middle">OUTCOME_UNKNOWN → reconcile</text>
  <text x="390" y="232" font-size="11" text-anchor="middle" fill="#ea4335">open: US transcript</text>
  <text x="390" y="250" font-size="11" text-anchor="middle" fill="#ea4335">blocker unresolved</text>
  <rect x="520" y="127" width="240" height="150" rx="10" fill="#fce8e6" stroke="#ea4335"/>
  <text x="640" y="150" font-size="13" text-anchor="middle" font-weight="bold">Agency｜机构</text>
  <text x="640" y="172" font-size="12" text-anchor="middle">Complete INSPECTION</text>
  <text x="640" y="192" font-size="11" text-anchor="middle">source-linked review, A17 states</text>
  <text x="640" y="210" font-size="11" text-anchor="middle">critical fields always reviewed</text>
  <text x="640" y="232" font-size="11" text-anchor="middle" fill="#ea4335">open: service-version location,</text>
  <text x="640" y="250" font-size="11" text-anchor="middle" fill="#ea4335">accreditation</text>
</svg>

**三个未解决失败的安全下一步**（五问：结果、权限、证据缺口、安全动作、关闭证据）：

| 分支 (Branch) | 证据缺口 (Gap) | 安全动作 (Safe action) | 关闭证据 (Closure evidence) |
|---|---|---|---|
| 零售：含义 | 两个批准来源对 net sales 定义不同，无 owner 决定；更多 schema 上下文**不能授权**定义 | 呈现两种含义，取得授权指标 owner 的决定，再按批准契约测试 SQL（测验正确选项） | 批准的版本化定义（来源、粒度、日历、计算、比较规则）+ 契约下的查询与结果对比证据 |
| 电信：不确定写入 | O17 无权威结果；超时 = OUTCOME_UNKNOWN，不是失败也不是重写许可 | 保留 O17，通过权威记录对账，仅在下游契约下重放 (replay)；交接带提议、操作 ID、不确定性与禁止盲目重复 | 权威操作结果与确切商业效果 + 接收者理解未决事项的证据 |
| 机构：检查不完整 | 水电图片到了但无法充分检查 → 支持"检查不完整"而非"申请人遗漏" | 保留收到页清单、不可读项、检查范围、适用要求、结论；送 caseworker；新附件 → 新包状态，重跑受影响检查并保留早先结论 | 新源修订、完成的受影响检查、绑定到所检查证据的 caseworker 确认/更正 |

**托管优先需要什么**：用与自定义实现相同的验收契约测试基线。CA API（批准含义、用户权限、有界执行、结果检查）/ CES（授权操作、易达人工、处理边界、不确定效果的恢复）/ Document AI（源锚点 (source anchors)、审查集成、提取结果、确切服务版本的处理位置与认证适用性；字段置信度 (confidence)有用但不证明正确）。在决定性要求上失败就排除该配置，即使它让架构图更简单。

**人在哪里决定**：人的问责**不需要**对每个 SQL 答案或只读电信解释都点批准。人拥有批准的含义、策略、支持的动作边界、重大决策；应用与后端代码强制由此产生的权限。

**成功的定义**（复用评估结构：版本化任务、批准参考、保留的执行观察、显式分母、失败类别、发布决定）：零售 255/300，追问与拒答在原分母中单独可见，权限失败独立关注；电信 真正自助解决与围堵和转人工分开，账户安全与不确定写入恢复独立测试；机构 原始提取与审查后关键字段分开，加完整性检测、群体、工作量、受理到决定时间、申诉。

**机构六个错误修复**：

| 错误 (Mistake) | 修复 (Repair) | 关闭证据 (Closure) |
|---|---|---|
| 自动申请人决定 | 恢复辅助性结论与 caseworker 决定权 | 测试显示标记不能独立产生申请人结果，且保留决定证据 |
| 只优化提取 | 把支持的完整性结论前移 | 检测、适当证据请求、可比耗时的观察，而非推断的节省 |
| 单一准确率数字 | 报告字段、群体、原始、审查后结果 | 有定义分母与批准验收标准的独立评估结果 |
| 未检查区域可用性 | 完成组件与服务版本位置清单 | 处理、存储、诊断、保留工件的被接受证据 + 所需批准 |
| 绕过安全官 | 尽早接触安全官，真实数据准入保持阻止 | 针对实际拟议范围的认证决定 |
| 结果无证据 | 保留包修订、检查范围、字段锚点、模型版本、更正、审查者归属 | 能从记录重建 A17 的结论与后续解决 |

**修复"统一方案"**："Standardize all three customers on a router and specialist agents. Select the newest model everywhere, launch from one aggregate accuracy score, and ask humans to review only low-confidence exceptions." —— 路由不能批准 net sales 含义；不能授权电信账户访问或让新 ID 重试变安全；基于置信度的例外审查会让自信的机构错误绕过强制关键字段审查；最新提取器还面临未解决的处理位置门。**值得标准化的是**：权限契约（谁能决定，在生成之外强制）、证据记录（把声明和动作绑定到身份、源修订、操作状态、保留观察）、评估纪律（任务定义、分母、关键失败、未解决结果）、所有权实践（决策者、人工路径、维护责任、仍需的验收）。从这些契约出发选择编排与部署；共享的置信度阈值替代不了它们。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "What transfers across these deployments, and why does the architecture change?" | "I reuse a sequence: establish the outcome and who decides, discover the real problem, bound authority and processing, evaluate a managed baseline first, define failure handling and the human path, and demand task evidence before claiming readiness. Retail needed owner-approved metric definitions and bounded SQL; telecom needed risk-bounded actions and durable reconciliation of uncertain writes; the agency needed source-linked review inside an accredited in-country boundary. The architectures differ because the hardest constraint differs — meaning, persistent account effects, and inspectable document evidence." | 决策序列不变；最难约束不同→架构不同 |
| "Why not standardize on the newest model and review only low-confidence results?" | "Because each case's real failure isn't a confidence problem. A newer model can't approve which net-sales definition is correct, can't make a new-ID retry safe after an unknown write, and a confident wrong income — like 7,800 at 0.99 — would skip review entirely. And the newest extractor processes in the US and EU, which fails the agency's in-country boundary. What would change my mind is evidence: an approved semantic contract, a downstream idempotency guarantee, calibrated confidence on critical fields, and accepted in-country processing." | 失败不是置信度问题；列出推翻所需证据 |
| "Where do humans need to be in the loop?" | "Not on every read — people own the approved meanings, the policies, the supported action boundaries, and the consequential decisions, and code enforces the resulting permissions. So retail analysts don't approve each SQL answer, but an owner approves the metric; telecom cancellations go to a person; and agency caseworkers confirm every critical field and make every eligibility decision." | 人拥有含义/策略/重大决策；代码执行 |

---

## 23. Conclusion｜课程总结与 14 天准备

Source: https://www.educative.io/courses/google-forward-deployed-engineer-interview/mEXEzZV4Pw9

### 要点 / Key ideas

剩 14 天时，学完课程只引入概念；**练习结果**显示哪些技能仍需测试或改进。建 `readiness-plan.md`：目标岗位与方向、面试日期、每日可用时间、已确认轮次、未决条件。

决策两部分：**表现 (Performance)**（哪些必需能力有近期相关证据，哪些需修复或独立测试）/ **条件 (Conditions)**（recruiter 要澄清什么才能复现预期条件）。

**课程地图（按轮次找课）**：

| 轮次 (Stage) | 对应内容 (Lessons) | 准备产出 (Deliverable) |
|---|---|---|
| 岗位匹配 (Role fit) | Ch1 + 5.2 | 动机 + 两个项目（Agent/ML + 传统工程） |
| 编程 (Coding) | 5.3 | 实现、边界测试、讲思路、不变量、复杂度 |
| 模糊实现 | 5.4 + 4.7（Ch2–3 支撑） | 澄清、假设、可工作增量、适应变更、追踪失败 |
| Agent 设计 | Ch2–4 + 5.5，然后 Ch6–8 限时案例 | 授权边界、证据、失败恢复、评估、成本/延迟/可靠性 |
| 客户判断与行为 | Ch1 + 5.6 + 案例 | 客户调研 + 5–6 个事实例子 |
| HC 与团队匹配 | 5.7 | 关于剩余流程、团队职责、岗位范围的问题；不假设内部评审需单独面试 |

**案例设计不是个人生产成就**——排练推理和提议的保障不能当成自己的项目讲。

**排序关键缺口**：每次尝试记录日期、陌生任务、时限与用时、环境、参考、辅助、打断、观察、下次测试。辅助或不限时的练习只证明学习过。三类：近期已证明 / 需定向修复 / 尚未在相关条件下测试——**不要平均成及格分**。

示例候选人的排序（安全与可信度优先，编程早排以留修复周期）：
1. **不安全恢复**：不确定写入后提议新操作 ID → 可能隐藏已提交的写入导致重复效果；追踪派发、查询、交接；用"提交后确认丢失"的变体独立重测；要求原 ID、对账 (reconciliation)前状态未知、不盲目新写
2. **无依据声明**：把共享交付说成个人所有、引用未支持的收益 → 核对项目事实，区分个人与团队、测量与估算，接受"谁做了什么、如何测量"的挑战
3. **独立编程**：38 分钟拿到正确结果但用了提示且漏了边界 → 修复不变量与测试缺口，在确认条件下无提示做一道没见过的变体
4. **设计所有权**：50 分钟答辩覆盖身份、证据、评估、延迟、成本，但需提示才想到运维负责人 → 用改变的题目重测，要求主动想到检测、响应归属、升级、仍需验收

设计强项不能抵消恢复错误；客户调研没有尝试记录 = 未测试。

**后勤确认 (logistics check)**：日期、时区、时长、间隔、休息、平台、设置、提供的环境、无障碍 (accessibility)；**每轮分别确认**语言、文档、互联网、包、自动补全、AI 辅助——**未声明的 AI 权限不是权限**。每个未决问题有 owner 和跟进日期。

**14 天 × 60 分钟 = 840 分钟（810 分配 + 30 缓冲）**：

| 天 (Day) | 内容 (Activity) |
|---|---|
| 1 | 审计证据、建 recap、发后勤问题 |
| 2–3 | 修复编程不变量与边界缺口；独立重测没见过的变体 |
| 4–5 | 用状态追踪修复恢复问题；用"确认丢失"的变体工具独立重测 |
| 6–7 | 核实行为故事的所有权与收益；限时追问并记录矛盾 |
| 8 | 50 分钟变题设计答辩 + 10 分钟复盘（含主动想到运维归属） |
| 9 | 修复影响最大的剩余缺口 |
| 10 | 用变更需求与失败时机重测实现 |
| 11 | 在最佳确认条件下做新编程变体 |
| 12 | 排练客户调研、设计、被挑战的项目事实 |
| 13 | 重测剩余优先缺口并冻结 recap |
| 14 | 30 分钟后勤与轻量回忆；30 分钟不用 |

时间缩水时先砍泛读和打磨，保留关键重测。只能凭新观察改变类别；保留早期失败与辅助记录。不安全恢复复发 → 即使解释正确也保持未关闭，找原因（把超时当失败、丢失 ID、误解去重）。决定是有条件的：继续准备，独立重测与后勤答复后再评估；若关键错误持续或时间不够，问 recruiter 能否调整日程（不假设一定可以）。

**有界的更新**：每周 20 分钟看官方文档与 release notes，记录来源、日期、变化、受影响例子、行动。区分产品术语（**Gemini Enterprise Agent Platform、Agent Runtime、Agent Search**）与可能保留旧名的 SDK 标识符。区分 "Documentation reviewed"、"Change proposed"、"Compatibility check executed"。最后几天只调查影响计划声明、必需工具或决定性约束的变化。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "Why this FDE role?" | "Because the work I've done that I'm proudest of is the integration and delivery work that made systems usable for customers — like permission-aware retrieval and replay-safe integrations — and this role is centered on exactly that, in customer environments. I'd tie it to what I personally built and owned, not to product names." | 连接已确认方向与个人证据 |
| "Is this system ready?" | "I'd answer against acceptance conditions: here's what we agreed, here's what we've observed against it, here's who owns each decision, and here's what's still blocking. I'd say what would permit the next step and what stays blocked, and keep my proposed safeguards separate from tests we've actually run." | 验收条件→观察→负责人→阻断项 |
| "What changed your approach?" | "I trace the changed requirement or interface to the contract it affects, verify the change, compare options against the decisive constraints, and test the adaptation — keeping working interfaces until evidence justifies replacing them. For example, when revisions were added to the document utility, uniqueness and selection changed but the I/O shell didn't, so I only replaced those parts." | 变化→受影响契约→验证→比较→测试 |

---

# Section II — Google Module of "Forward Deployed Engineer for AI Systems"｜第二部分：主课程 Google 模块（只记新增/不同之处）

> 本部分与 Section I 大量重叠。以下只记录**新增或不同**的内容，其余请看对应的 Section I 课程。

## 24. The Google FDE Interview Loop｜Google FDE 面试流程（补充）

Source: https://www.educative.io/courses/forward-deployed-engineer/the-google-fde-interview-loop
重叠内容见 Section I §1 Interview Loop Overview、§7 Hiring Committee。

### 要点 / Key ideas（新增）

**角色定位**：Google FDE 拥有客户环境内 AI 系统的**技术交付 (technical delivery)**，覆盖完整生命周期：discovery → architecture → build → evaluation → handoff。产品工程师为很多用户改进一个产品；FDE 一次服务一个客户，衡量标准是**该客户的系统是否进入生产并交付价值**。跨客户重复出现的模式回流给 Google 产品团队作为 feature request。三种能力交叉：软件工程师的编码、解决方案架构师 (solutions architect)的系统思维、顾问的问题框定 (problem framing)。

**两个方向 (tracks)**：

| 方向 (Track) | 重点 (Focus) |
|---|---|
| FDE, GenAI, Google Cloud | 以 agent 为中心：agentic workflows、多 agent、MCP servers、检索、评估（Gemini + Agent Platform） |
| FDE, Google Cloud Consulting | 在 Google Cloud 专业服务组织内，更广的客户交付：数据、基础设施、AI |

职级如 FDE II、Senior FDE；部分有区域语言要求。**方向决定技术轮重点，职级决定设计与领导力答案的深度**（高级候选人要谈干系人对齐 (stakeholder alignment)和长期运维）。

**这门课给的具体轮次与时长（与 Section I 的"不确定"框架不同，这里给了典型值）**：

| 轮次 (Round) | 时长 (Duration) | 可见任务 (Visible task) | 底层信号 (Underlying signal) |
|---|---|---|---|
| Recruiter screen | 30–45 min 电话 | 背景、动机、对 Google Cloud 的熟悉 | 是否用部署语言讲经历：真实客户、约束、具体结果 |
| Coding round | 60 min | 实用工程：API、数据处理、限时调试；Python 构建组件 | 正确可读代码，**边写边说出失败模式**而不是等追问 |
| Vibe-coding session | 60 min 协作 | 与面试官一起按需求构建 | 澄清而非静默假设；方向变化时持续推进 |
| Agentic system design | 60 min | 为企业场景设计 AI 系统 | 回应给定约束；**把评估当核心需求而非最后一步** |
| Googleyness | 45–60 min | 讨论过往情境 | 个人主人翁、客户同理心、不确定时的判断 |

onsite 通常虚拟进行。HC 一起审所有评分卡 (scorecards) → **五轮一致表现比某一轮惊艳更重要**；强设计轮不能完全抵消弱行为轮。共同习惯：**clarify → scope a first version → build something that works → adapt**。

**常见准备错误**：只按标准 SWE 面试准备（算法不能帮协作构建与企业设计）；先写代码/画架构再提问；**只报产品名不讲权衡**（"偏好 Gemini Pro" 不是设计决策；"高并发分类步骤用 Gemini Flash，因为那里延迟和成本比深度推理重要" 才是）；行为故事只讲内部团队工作（要有客户/干系人、约束、个人决定、结果）。

**向 recruiter 确认（新增项）**：系统设计是 agentic/GenAI 还是通用云架构；是否有基于客户场景或角色扮演的轮次；是否有语言或区域要求；编程是传统题、实用构建还是两者兼有。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "Why Gemini Flash here instead of Pro?" | "This step is high-volume classification where latency and cost matter more than deep reasoning, so Flash fits. I'd reserve a Pro-tier model for steps that need multi-step reasoning, and confirm the split on the golden set rather than by preference." | 按任务特性选模型，用评估验证 |
| "What do you think this loop is testing?" | "Whether I can deliver a production AI system inside a customer's environment and use good judgment when things are ambiguous. In every round I try to do the same thing: clarify, scope a first version, build something that works, and adapt as I learn more." | 交付+判断；四步习惯 |

---

## 25. Vibe Coding and System Design｜氛围编程与系统设计（补充）

Source: https://www.educative.io/courses/forward-deployed-engineer/vibe-coding-and-system-design
重叠内容见 Section I §4 Vibe Coding Round、§5 Agentic System Design Round。

### 要点 / Key ideas（新增/不同）

**与 Section I 的不同**：这门课说 vibe-coding 轮中 **AI 辅助编码工具"常常被允许" (often permitted)**，因此信号从打字速度转向判断力（Section I 则强调"未声明一律视为不允许"——两者结合：先向 recruiter 确认，再在相同环境下练习）。

**60 分钟三阶段**：

| 阶段 (Phase) | 时间 (Time) | 目标 (Goal) |
|---|---|---|
| 澄清 (Clarify) | 5–10 min | 用户、输入、输出、成功标准；3–4 个精准问题 + 简短复述 |
| 交付可工作切片 (Ship a working slice) | 25–30 min | 最小端到端版本，产出真实结果 |
| 适应 (Adapt) | 剩余 | 纳入变更、加固、说明下一步 |

复述示例（工单分诊 (ticket triage)）："So the first version takes a support ticket, classifies it into one of five categories, and flags anything urgent for a human. Accuracy on the urgent flag matters more than the category. Is that right?"

**可工作切片 (working slice)**：从输入到输出的最薄版本，可能只处理一种情况、跳过错误处理，但产出真实结果；尽早暴露集成问题，给面试官具体可回应的东西。AI 生成的代码：读、解释、测试后再继续。

**Problem (English) — ticket triage slice**: Build the thinnest end-to-end function that sends one support ticket to Gemini and returns a typed result (category, is_urgent, reason) using structured output.

```text
Input:  "My account was charged twice this month and I need a refund ASAP."
Output: Category: billing | Urgent: True | Reason: duplicate charge, customer requests refund
```

```python
from google import genai
from google.genai import types
from pydantic import BaseModel


class TicketTriage(BaseModel):
    category: str
    is_urgent: bool
    reason: str


client = genai.Client(api_key="YOUR_API_KEY")
MODEL_ID = "gemini-3.6-flash"  # a Flash-tier model; exact names change over time


def triage_ticket(ticket_text: str) -> TicketTriage:
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=f"Classify this support ticket:\n\n{ticket_text}",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=TicketTriage,   # structured output -> easy to test and pass on
        ),
    )
    return response.parsed


if __name__ == "__main__":
    result = triage_ticket("My account was charged twice this month and I need a refund ASAP.")
    print("Category:", result.category)
    print("Urgent:", result.is_urgent)
    print("Reason:", result.reason)
```

SDK 与模型名会变；面试中**结构正确与推理清晰**比记住具体版本更重要。适应阶段的典型变更：路由到特定队列、处理其他语言 → 承认变更、说明对当前设计的影响、做最小更新；有时间就加输入校验 (input validation)、错误处理、几个样例测试；最后说明下一步（带标签的评估集、低置信结果的人工审查）。

**Agentic 系统设计六步框架 (six-step framework)**（与 Section I §5 的 40 分钟分配互补）：

| 步骤 (Step) | 内容 (Content) |
|---|---|
| 1 范围与成功 (Scope & success) | 收窄到一个工作流、一个用户群、一个清晰指标（如：首版帮助客服回答账单问题，成功 = 处理时长降低且准确率高于约定阈值） |
| 2 数据与工具 (Data & tools) | agent 需要知道什么（文档/数据库 → 检索或 Text-to-SQL）、需要做什么（工具，常通过 MCP）；记录数据质量与访问限制 |
| 3 Agent 模式 (Agent pattern) | 选满足范围的最简单模式；单 agent + 少量明确工具适合多数首版；**多 agent 只在需要分开所有权、不同模型或隔离权限时**才值得；解释为什么不选更复杂的同样有价值 |
| 4 权限与护栏 (Permissions & guardrails) | 在模型之外基于用户会话与身份强制权限；**低风险自动**（查订单）、**中风险人工审查**（起草客户回复）、**高风险显式批准 + 日志**（退款） |
| 5 评估与可观测 (Evaluation & observability) | 面试官特别关注：定义正确输出、如何测量、如何在到达客户前抓回归；真实例子的黄金集 (golden set)、每次发布前自动检查、生产中记录每一步的 tracing |
| 6 部署与成本 (Deployment & cost) | 托管 agent runtime、Cloud Run 或 GKE，取决于客户安全与运维约束；成本取决于模型选择、上下文大小、请求量；粗略的每请求成本估算 |

**时间管理**：约第 **40 分钟**讲到评估，给部署、成本、追问留时间；时间不够时对剩余每步说一句话也比跳过好——**缺少评估计划是最常被标记的缺口**。

**两轮共同错误**：跳过澄清；过度构建 (overbuilding)（单 agent 或简单函数就够时提多 agent 或复杂抽象）；把面试官当观察者而不是协作者（问面试官偏好是正面信号）；评估留到最后或缺失。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "Here's the brief — where do you start?" | "With three or four questions about who uses it, what comes in, what should come out, and how you'll judge success. Then I'll restate it back — for ticket triage, something like: 'the first version classifies a ticket into five categories and flags urgent ones for a human, and the urgent flag matters more than the category — right?' — before I write any code." | 先问 3–4 个问题并复述 |
| "Why ship such a thin slice first?" | "An end-to-end slice surfaces integration problems early and gives us something real to react to. Once one ticket goes in and a typed result comes out, I can harden it, add validation, and adapt to changes without guessing." | 端到端切片先暴露集成问题 |
| "Single agent or multi-agent?" | "I start with the simplest pattern that meets the scope — usually one agent with a few well-defined tools. I'd only split into multiple agents if parts of the work need separate ownership, different models, or isolated permissions." | 最简单模式；拆分有明确理由 |

---

## 26. Googleyness and Leadership｜Googleyness 与领导力（补充）

Source: https://www.educative.io/courses/forward-deployed-engineer/googleyness-and-leadership
重叠内容见 Section I §6 Googleyness Round（STAR、故事卡、Bracken 例子）。

### 要点 / Key ideas（新增/不同）

**四个维度**（Googleyness 是 Google 跨所有岗位的工作特质：适应模糊、重视反馈、用户第一、做正确的事、关心团队）：

| 维度 (Dimension) | FDE 中的表现 (What it looks like for an FDE) |
|---|---|
| 适应模糊 (Comfort with ambiguity) | 需求、数据或所有权不清时用合理计划推进 |
| 协作品格 (Collaborative character) | 与不向你汇报的客户团队、Google 产品团队、合作伙伴良好合作 |
| 客户同理心 (Customer empathy) | 理解客户真实问题与约束，包括他们不同意你时 |
| 个人主人翁 (Individual ownership) | 为决定及其结果负责，包括结果不好时 |

**领导力 = 无正式权力的领导**：FDE 很少管理所依赖的人，靠清晰度、可信度、跟进影响客户工程师、安全审查者、高管 (executives)。"在没有权力的情况下让客户数据团队对计划达成一致" 往往比"管理直接下属"的故事更强。

**面试官听什么**：区分团队成就与个人贡献——"we" 包办一切是弱信号。强回答说出**具体决定**、**在什么约束/不确定下**、**结果如何改变**，加**反思**。典型追问："What would have happened if you had not stepped in?"、"Who disagreed with that decision, and how did you handle it?" 两个常被标记的模式：把模糊描述为阻碍而非工作常态；把坏结果完全归咎于客户、其他团队或环境。

**改良版 STAR（新增 Constraint 与 Reflection）**：

| 部分 (Part) | 内容 (Content) | 长度 (Length) |
|---|---|---|
| Situation | 客户、项目、利害 | 2–3 句 |
| Constraint | 面临的模糊、冲突或限制 | 1–2 句 |
| Decision | 你的具体选择及原因（**大部分时间放这里**） | 3–4 句 |
| Outcome | 改变了什么，尽量带数字 | 1–2 句 |
| Reflection | 学到什么或会改变什么 | 1–2 句 |

整个故事约 2 分钟，留出追问空间。

**课程示例故事（零售政策助手）**：
> **Situation:** "A retail customer wanted a GenAI assistant to answer store staff questions about return policies, with a pilot planned for 40 stores in six weeks.
> **Constraint:** Two weeks in, it became clear the policy documents were inconsistent across regions, and the customer's policy team had no plan to reconcile them before the pilot.
> **Decision:** Instead of building retrieval over conflicting documents, I proposed narrowing the pilot to the one region with a single, current policy set. I brought the customer's project lead a short comparison of five conflicting answers to make the risk concrete. The lead pushed back because 40 stores had been promised to leadership, so I offered to present the trade-off to that leadership group together.
> **Outcome:** Leadership approved a 12-store pilot in one region. Answer accuracy in testing reached the agreed threshold, and the policy team used our comparison to start reconciling the other regions.
> **Reflection:** I learned to check source-data consistency during discovery, not during the build. I now include a document audit in the first week of every retrieval project."

中文：一个故事覆盖模糊、同理心、协作、主人翁。

**故事库 (story bank)**：**6–8 个**故事通常足够（Section I 说 5–6 张卡）。候选：需求大幅变化的项目、与客户/干系人的分歧、失败或表现不佳的部署、影响非下属团队、不完整数据下的决定、收到批评并改进。**覆盖矩阵 (coverage matrix)**：故事 × 四维度，**每个维度至少两个故事**，同一轮不重复使用同一故事。没有直接客户经验也可以用内部干系人（另一工程团队、PM、业务部门）扮演客户。

**常见问题模式（新增题，附模型答案）**：

**Q1. "Tell me about a time you moved a project forward without clear requirements."**
> "On the retail policy assistant, requirements assumed one consistent policy set, and two weeks in I found the regions disagreed. Rather than wait for the policy team or build retrieval over conflicting sources, I scoped the pilot to the one region with a single current policy set and showed the project lead five conflicting answers side by side. We launched a 12-store pilot that met the accuracy threshold, and I now audit source documents in week one."

中文：模糊是常态；用有界范围推进。

**Q2. "Tell me about a customer who rejected your technical recommendation."**
> "The project lead rejected narrowing the pilot because 40 stores had been promised to leadership. I didn't push harder on my own; I acknowledged that commitment and offered to present the trade-off to leadership with them, using the conflicting-answer comparison as evidence. Leadership chose the 12-store pilot, and the lead kept credibility because the decision was made with them, not around them."

中文：理解对方压力；一起向上呈现权衡。

**Q3. "Tell me about a deployment that produced an unexpected result."**
> "In a Veltra-style chat pilot, resolution rates were strong but satisfaction dropped for one customer group. Instead of reacting to the headline number, I pulled traces and feedback for that group, found the answers were technically correct but missing a step those customers needed, and adjusted the response design for that segment, then tracked their satisfaction separately in the next release."

中文：先用 trace 和反馈调查再行动；按群体调整。

**Q4. "Tell me about influencing a decision you didn't own."**
> "I had no authority over the customer's leadership or policy team. I made the risk concrete — five real questions with five conflicting answers — and offered a smaller, safe option plus a path to the full rollout. Leadership approved the narrower pilot, and the policy team used the same comparison to kick off reconciliation for the other regions."

中文：用具体证据 + 可行选项影响他人。

**常见错误（新增）**：没有真实冲突或约束的故事；用团队语言掩盖个人决定；只选一切顺利的故事（处理得好的失败更能体现主人翁与反思）；大部分时间讲背景；背诵脚本（追问时崩溃）。

---

## 27. The Telecom Case Brief (Veltra)｜Veltra 电信案例简报（与案例二不同的新案例）

Source: https://www.educative.io/courses/forward-deployed-engineer/the-telecom-case-brief
相关方法见 Section I §13 CS2 Case Study（电信，但客户、数字、约束不同）。

### 要点 / Key ideas

**Problem (English) — the customer brief**:
- **Customer**: Veltra Telecom (fictional), mobile and home broadband operator in **three EU countries**, **8 million subscribers**. From the Director of Customer Operations.
- About **1.2 million contacts/month** across phone, chat, and mobile app. Average handling time up **18%** over two years; CSAT falling. Leadership wants an AI agent that handles customer service **end to end** and **cuts contact-center costs 30% within six months**.
- Contacts mostly billing, plan changes, roaming, device issues, network problems. **During outages, volume can triple within an hour and waits exceed 40 minutes.**
- Billing system **on-premises** (IT-managed); customer records in CRM; BigQuery warehouse with usage and billing history; knowledge base of **~6,000 articles, many outdated**; network status from network operations' own monitoring tools.
- A **rules-based chatbot three years ago** — customers disliked it. **CISO must approve** anything touching customer data; GDPR + national telecom rules in each country.
- Wants a proposal and pilot plan **within four weeks**.

**读简报的六个问题**：

| 问题 (Question) | 揭示什么 (What it uncovers) |
|---|---|
| 表面诉求是什么？(Stated ask) | 客户已想象好的方案 |
| 底层问题是什么？(Underlying problem) | 真正重要的业务结果 |
| 有哪些明示或隐含约束？ | 数据、系统、时间、合规限制 |
| 什么未知或被假设？ | 界定范围前要填补的缺口 |
| 干系人是谁？ | 赞助、批准、运营或阻碍项目的人 |
| 风险是什么？ | 什么会阻止项目进入生产 |

**底层问题**："Veltra needs to resolve common customer contacts faster and absorb outage spikes without long waits, while maintaining or improving satisfaction." 这打开了多种方案：辅助人工客服、自动化特定联系类型、停电时主动告知——而不是一开始就承诺完全自动化。30% 可能是坚定承诺也可能是愿景——要问怎么算的、首版接受什么作为成功。

**约束**：

| 约束 (Constraint) | 来源 (From brief) | 影响 (Implication) |
|---|---|---|
| 本地账单系统 | "Runs on an on-premises platform" | 需要私有连接与 IT 参与 |
| 多数据源 | CRM、BigQuery、知识库、网络工具 | 各有 owner、访问流程、质量问题 |
| 过时知识库 | "Many are outdated" | 对现有内容检索可能给出错误答案 |
| 监管 | 三国 GDPR + 电信法规 | 数据驻留 (data residency)、同意 (consent)、日志、客户披露 |
| 安全审批 | "CISO will need to approve" | 安全设计必须早准备 |
| 时间线 | 四周提案、六个月结果 | 限制能真正构建与验证的量 |
| 多渠道 | 电话、chat、app | 语音增加延迟和集成要求 |

**首次会议问题（未知项）**：120 万联系按类型与渠道如何分布、哪些最频繁最贵？"end to end" 对领导意味着什么（完全自动化还是更快的人工解决也算）？30% 如何测量、基线是什么？账单系统能否通过 API 访问、谁负责集成？网络状态多新、能否程序化访问？领导愿意自动化哪些动作（换套餐、积分）？之前的 chatbot 为什么失败（除了客户不喜欢）？三国语言要求？

**干系人**：客服运营总监（赞助人 (sponsor)：处理时长、满意度、成本目标）/ 高管层（30% 与六个月可见结果）/ CISO（客户数据保护、合规、可审计 (auditability)）/ IT（账单平台稳定、有限集成风险）/ 网络运营（准确的停电信息、避免额外工作）/ **一线客服**（容易被忽略：不是决策者，但他们的采用决定 agent-assist 成败，他们对真实问题的了解对评估集至关重要）。

**最重要的风险**：过时知识库（自信的错误答案）、本地账单集成（依赖另一个团队的时间与批准）；其他：不现实的目标/时间线让成功的试点看起来失败、安全审批来得晚、客户因旧 chatbot 产生的怀疑。**面试中点出最可能阻止项目的一两个风险并解释原因，比平均列出所有风险更显判断力。**

### 面试怎么说 / How to say it in the interview

> "The stated ask is an end-to-end agent that cuts costs 30% in six months. The underlying problem is that common contacts take too long and outages create 40-minute waits, while satisfaction is falling. The two risks I'd worry about most are the outdated knowledge base, which would produce confident wrong answers, and the on-prem billing integration, which depends on IT's time and approval. Before designing, I'd want the contact mix by type and channel, how the 30% is measured, whether billing has an API, and why the old chatbot failed."

中文：区分诉求与问题；点出两大风险；列出首次会议关键问题。

---

## 28. Case Discovery and Scoping (Veltra)｜Veltra 调研与范围界定

Source: https://www.educative.io/courses/forward-deployed-engineer/case-discovery-and-scoping
方法同 Section I §14 CS2 Discovery and Scoping（风险层级、首版范围、托管对比）。

### 要点 / Key ideas（Veltra 特有发现）

**调研发现**：

| 领域 (Area) | 发现 (Finding) |
|---|---|
| 联系构成 | 账单 32%、网络与停电 20%、设备 15%、换套餐 14%、漫游 9%、其他 10% |
| 渠道 | 电话 60%、chat 30%、app 10% |
| 账单系统 | IT 中间件 (middleware)提供**只读 API**（余额、发票、费用）；任何写操作需要正式 IT 变更请求 (change request) |
| 网络状态 | 网络运营发布**内部停电 feed，每 5 分钟更新**，可按邮编查询 |
| 知识库 | 约 40% 文章两年未更新；**400 篇账单文章由账单团队维护，大多是最新的** |
| 成本目标 | 30% 是**整个项目的领导愿景**；赞助人会把**账单处理时长的可测降低**视为试点成功 |
| 旧 chatbot | 失败原因：死板菜单 + **无法把上下文交给人工**，客户要重复说明 |
| 语言 | 三国三种语言 |
| 安全 | CISO 要求 EU 数据驻留、**试点不允许自动金融操作**、完整审计轨迹 (audit trail) |

**价值 × 可行性优先级 (value vs feasibility)**：

| 用例 (Use case) | 价值 | 可行性 | 结论 |
|---|---|---|---|
| 账单解释（chat/app） | 高 | 高（API 就绪、文章最新） | **首版** |
| 停电状态（chat/app） | 高 | 高（feed 已存在） | **首版** |
| 人工账单客服的 agent assist | 中 | 高（帮助 60% 电话联系而不自动化语音） | **首版** |
| 设备排障 | 中 | 低（文章过时） | 后续（需清理文章） |
| 自动换套餐 | 高 | 被阻（写权限未批） | 后续（需 IT 批准） |
| 全语音 agent | 高 | 被阻（延迟、电话集成、范围大） | 后续 |

高价值低可行性的用例不放弃，移到后续阶段并写明依赖。

**Veltra 动作风险层级**：

| 动作 (Action) | 风险 (Risk) | 试点策略 (Pilot policy) |
|---|---|---|
| 解释账单、费用、余额 | 读 | 自动，限定于已认证客户 |
| 报告客户所在区域停电状态 | 读 | 自动 |
| 创建回电请求或工单 | 可逆写 | 自动，记录日志 |
| 带对话摘要转人工 | 可逆写 | 自动，记录日志 |
| 申请服务积分 (service credit) | 高风险 | 试点不自动化；agent 准备请求，人工批准 |
| 更改套餐 | 高风险 | 首版范围外 |
| 取消服务或携号转网 | 高风险 | **永不自动化** |

一张表同时满足：CISO 不自动金融操作的要求；修复旧 chatbot 最大的失败（带上下文交接成为核心能力）；给赞助人后续路径（IT 批准写权限且试点建立信任后再纳入换套餐）。

**Build vs buy（新名称）**：**Gemini Enterprise for CX**（原 Customer Engagement Suite with Google AI）提供预置联络中心能力（客户自助的 conversational agents、人工的 agent assist）vs **在 Gemini Enterprise Agent Platform 上用 ADK 构建自定义 agent**。

| 标准 (Criterion) | CES / Gemini Enterprise for CX | 自定义 ADK agent |
|---|---|---|
| 价值实现时间 (time to value) | 标准联络中心模式更快 | 更慢 |
| 与本地账单 API 集成 | 可通过连接器 (connectors)或工具 | 通过自定义 MCP server 完全控制 |
| 与现有联络中心平台契合 | 取决于兼容性，需确认 | 通过 API 集成 |
| 电话客服的 agent assist | 核心能力 | 需自建 |
| 自定义账单解释逻辑 | 产品限制内可配置 | 完全可定制 |
| 长期所有权 | 与产品共享 | Veltra 团队拥有 |

结论：**混合方案**——预置 agent assist 用于电话人工（若兼容）；自定义 ADK agent 用于账单解释与停电状态（依赖 Veltra 特定 API、feed、解释规则）。最终决定取决于**一个开放问题**：现有联络中心平台是否与 Google 预置能力集成——记为依赖而不是假设答案。"it depends on one specific fact, and here is how we would confirm it" 比自信但忽略现有系统的回答更强。

**首版范围声明**：目标（降低账单与停电联系的处理时长与等待）；渠道（chat + app + 人工账单客服 agent assist）；市场（一国一语言）；范围内（账单解释、停电状态、建工单、带摘要交接）；范围外（语音自助、换套餐、自动积分、设备排障）；成功指标 (success metrics)（无需人工解决的账单 chat 比例、辅助联系处理时长、CSAT ≥ 基线、约定黄金集上的准确率）；依赖（账单 API 与停电 feed 访问、联络中心平台兼容、CISO 批准）；时间（四周试点计划，三个月内有限生产发布）。不承诺首版 30%。

### 面试怎么说 / How to say it in the interview

| 问题 (Question) | English model answer | 中文要点 |
|---|---|---|
| "Which use cases go first, and why?" | "Billing explanations and outage status in chat and app — billing is the largest contact type with a read-only API and 400 maintained articles, and outages cause the worst waits with a feed that already exists. Plus agent assist for phone billing agents. Device troubleshooting waits on article cleanup, plan changes on IT write approval, and voice on latency and telephony work." | 价值×可行性；被阻用例写明依赖 |
| "Build or buy?" | "Probably hybrid: prebuilt agent assist for the phone agents if it's compatible with Veltra's contact-center platform, and a custom ADK agent for billing and outage because those depend on Veltra's own APIs and rules. The decision hinges on that one compatibility fact, so I'd confirm it with IT before committing." | 混合；取决于一个可确认的事实 |
| "Will the pilot hit 30%?" | "Not by itself, and I wouldn't promise that. The sponsor told us a measurable drop in billing handling time counts as pilot success, so that's the target. The pilot then gives us real numbers to model the path toward the full program goal." | 不承诺；以约定的试点成功为准 |

---

## 29. Agent System Design (Veltra)｜Veltra Agent 系统设计

Source: https://www.educative.io/courses/forward-deployed-engineer/agent-system-design
方法同 Section I §5（追踪请求、权限在模型外）与 §15 CS2 System Design（身份来自会话、风险层级）。以下为 Veltra 的具体设计。

### 要点 / Key ideas

**数据与工具**：

| 需求 (Need) | 来源 (Source) | 访问方式 (Access) |
|---|---|---|
| 客户账单、费用、余额 | 本地账单系统 | 自定义 MCP server 调用 IT 的只读中间件 API |
| 客户区域停电状态 | 网络运营停电 feed | 自定义 MCP server 按**客户账户上的邮编**查询 |
| 账单政策与解释 | 400 篇最新账单文章 | 托管企业搜索 (managed enterprise search) + 策展数据存储 |
| 建工单/回电 | CRM | MCP server 暴露窄的建工单工具 |
| 转人工 | 联络中心平台 | 交接工具传递结构化对话摘要 |

两个关键选择：(1) 检索数据存储**只含 400 篇维护的账单文章 + 为试点写的少量停电 FAQ**，过时文章被排除而不是"索引了再祈祷"；(2) 停电工具**从已认证客户账户取邮编**而不是接受对话中的邮编——绑定身份，防止被用来探测其他区域。

**Agent 模式**：**单个 ADK agent + 五个窄工具**。所有工具共享同一安全边界、同一交付团队拥有、服务一个面向客户的工作流——没有任何需要多 agent 的信号（分开所有权、分开权限、工具集太大）。人工的 agent assist 通过 Google 预置能力单独处理——不同用户、不同工具，是自然边界而非额外复杂度。

<svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect width="800" height="400" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">Veltra: Billing &amp; Outage Agent｜账单与停电 Agent 架构</text>
  <rect x="15" y="70" width="110" height="56" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="70" y="94" font-size="12" text-anchor="middle">Customer</text>
  <text x="70" y="111" font-size="11" text-anchor="middle">app / web chat</text>
  <rect x="145" y="70" width="90" height="56" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="190" y="94" font-size="12" text-anchor="middle">IdP</text>
  <text x="190" y="111" font-size="11" text-anchor="middle">token 令牌</text>
  <rect x="255" y="70" width="90" height="56" rx="8" fill="#e8f0fe" stroke="#4285f4"/>
  <text x="300" y="94" font-size="12" text-anchor="middle">Apigee</text>
  <text x="300" y="111" font-size="11" text-anchor="middle">API gateway</text>
  <rect x="365" y="45" width="220" height="130" rx="10" fill="#fef7e0" stroke="#fbbc04"/>
  <text x="475" y="66" font-size="12" text-anchor="middle" font-weight="bold">Agent Runtime (EU region)</text>
  <text x="475" y="86" font-size="12" text-anchor="middle">Single ADK agent 单 agent</text>
  <text x="475" y="104" font-size="11" text-anchor="middle">Flash-tier Gemini, 5 narrow tools</text>
  <rect x="380" y="115" width="190" height="48" rx="6" fill="#fce8e6" stroke="#ea4335"/>
  <text x="475" y="135" font-size="11" text-anchor="middle">Policy callback: risk tiers</text>
  <text x="475" y="151" font-size="11" text-anchor="middle">credits blocked in code 积分在代码中拦截</text>
  <line x1="125" y1="98" x2="143" y2="98" stroke="#555" stroke-width="1.5"/>
  <line x1="235" y1="98" x2="253" y2="98" stroke="#555" stroke-width="1.5"/>
  <line x1="345" y1="98" x2="363" y2="98" stroke="#555" stroke-width="1.5"/>
  <rect x="610" y="40" width="175" height="40" rx="6" fill="#e6f4ea" stroke="#34a853"/>
  <text x="697" y="64" font-size="11" text-anchor="middle">MCP: billing (read-only)</text>
  <rect x="610" y="88" width="175" height="40" rx="6" fill="#e6f4ea" stroke="#34a853"/>
  <text x="697" y="112" font-size="11" text-anchor="middle">MCP: outage (postcode from acct)</text>
  <rect x="610" y="136" width="175" height="40" rx="6" fill="#e6f4ea" stroke="#34a853"/>
  <text x="697" y="160" font-size="11" text-anchor="middle">MCP: CRM tickets</text>
  <rect x="610" y="184" width="175" height="40" rx="6" fill="#e6f4ea" stroke="#34a853"/>
  <text x="697" y="208" font-size="11" text-anchor="middle">Handoff + summary 转人工</text>
  <rect x="610" y="232" width="175" height="40" rx="6" fill="#ede7f6" stroke="#7e57c2"/>
  <text x="697" y="256" font-size="11" text-anchor="middle">Search: 400 billing articles</text>
  <line x1="585" y1="80" x2="608" y2="60" stroke="#555" stroke-width="1.2"/>
  <line x1="585" y1="100" x2="608" y2="108" stroke="#555" stroke-width="1.2"/>
  <line x1="585" y1="130" x2="608" y2="156" stroke="#555" stroke-width="1.2"/>
  <line x1="585" y1="155" x2="608" y2="204" stroke="#555" stroke-width="1.2"/>
  <line x1="585" y1="170" x2="608" y2="252" stroke="#555" stroke-width="1.2"/>
  <text x="697" y="290" font-size="11" text-anchor="middle" fill="#5f6368">MCP servers on Cloud Run</text>
  <text x="697" y="306" font-size="11" text-anchor="middle" fill="#5f6368">private link → on-prem billing</text>
  <rect x="365" y="200" width="220" height="70" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
  <text x="475" y="222" font-size="12" text-anchor="middle">Outage cache per postcode</text>
  <text x="475" y="240" font-size="11" text-anchor="middle">5-min TTL (= feed refresh)</text>
  <text x="475" y="258" font-size="11" text-anchor="middle">+ app outage banner 停电横幅</text>
  <rect x="15" y="200" width="330" height="70" rx="8" fill="#f8fbff" stroke="#4285f4" stroke-dasharray="5,4"/>
  <text x="180" y="222" font-size="12" text-anchor="middle">Guardrails 护栏</text>
  <text x="180" y="240" font-size="11" text-anchor="middle">Model Armor · VPC Service Controls</text>
  <text x="180" y="258" font-size="11" text-anchor="middle">Sensitive Data Protection masks logs</text>
  <rect x="15" y="295" width="570" height="90" rx="10" fill="#fff" stroke="#9aa0a6"/>
  <text x="300" y="316" font-size="12" text-anchor="middle" font-weight="bold">Evaluation + observability｜评估与可观测</text>
  <text x="300" y="336" font-size="11" text-anchor="middle">~300 real chats labeled by senior agents (outcome, tool calls, handoff)</text>
  <text x="300" y="354" font-size="11" text-anchor="middle">regression gate: task success · groundedness · tool accuracy</text>
  <text x="300" y="372" font-size="11" text-anchor="middle">end-to-end traces; weekly graded sample; failures → golden set</text>
  <rect x="610" y="325" width="175" height="60" rx="8" fill="#ede7f6" stroke="#7e57c2"/>
  <text x="697" y="347" font-size="11" text-anchor="middle">Agent assist (prebuilt)</text>
  <text x="697" y="365" font-size="11" text-anchor="middle">for human phone agents</text>
</svg>

**架构**：客户经 app/web chat 登录 → Apigee → 运行在 **EU 区域 Agent Runtime** 上的 agent（选它是因为 IT 缺乏大规模运维容器经验；它提供托管会话 (managed sessions)、记忆、评估与可观测集成）。自定义 MCP servers 跑在 **Cloud Run**（需要到本地系统的私有连接，IT 已部署少量 Cloud Run 服务）。

**权限与护栏**：客户访问令牌 (access token)从身份提供方 (identity provider)经 agent 流到每个 MCP server → 每次账单查询与工单都限定于登录客户；**模型从不生成或看到令牌**。策略层作为 **ADK callback** 按风险层级检查每次工具调用；读与建工单自动并记录；服务积分 agent 根本无法发放（建工单交人工审核）。**Model Armor** 筛查输入输出中的提示注入 (prompt injection)与敏感数据；**VPC Service Controls** 把数据留在批准边界内；日志经 **Sensitive Data Protection** 脱敏 (redaction)后存储。

**评估与可观测**：黄金集 (golden set)约 **300 条**来自试点国家的真实账单/停电 chat，由**资深客服**标注正确结果、预期工具调用、是否应转人工；含常见问题、困难争议、范围外请求、提示注入尝试。**回归门 (regression gate)**在每次发布前运行，任务成功率、groundedness、工具准确率低于与赞助人约定的阈值就阻止部署。生产中每个对话端到端 trace；仪表盘 (dashboard)跟踪解决率、转人工率、延迟、每对话成本、客户反馈；每周用同一评分器给抽样打分；**每个确认的失败加入黄金集**。

**部署、规模与成本**：停电峰值是主要扩展问题 → **按邮编缓存停电状态，TTL = feed 5 分钟刷新间隔**（同一区域上千客户不各自查询）；停电时 app 显示**横幅**，在对话开始前回答很多问题；Agent Runtime 与 Cloud Run 自动扩展 (autoscale)，**最大实例数限制保护账单中间件**（最慢的依赖）。

**粗略成本估算**：

| 步骤 (Step) | 计算 (Calculation) |
|---|---|
| chat + app 联系 | 1.2M × 40% ≈ 480K/月 |
| 账单 + 停电占比 | 32% + 20% = 52%，略过一半 → **约 250,000 合格对话/月**（三国） |
| 试点国家 | **约 80,000/月** |
| 每对话 | 约 6 轮，多数用 Flash 模型 → **约 1–2 美分/对话** |
| 试点模型成本 | **约 1,000–2,000 美元/月**（需按当前定价与实测流量确认） |

结论：模型成本相对联络中心人力成本很小。

### 面试怎么说 / How to say it in the interview — 追问题库（课程给了弱/强答案对比）

| 追问 (Follow-up) | 弱答案 (Weak) | 强答案 English (Strong) | 中文 |
|---|---|---|---|
| "Why not a multi-agent design?" | "Multi-agent systems are more scalable, so we could add one later." | "All five tools share one security boundary and one owning team, and the tool set is small. A single agent is cheaper, faster, and easier to evaluate. If plan changes arrive with separate IT ownership and write permissions, that would be a reason to add a separate agent." | 共享边界与 owner；何时才拆 |
| "Traffic triples during an outage. What happens?" | "The system autoscales." | "Outage status is cached per postcode for the feed's five-minute refresh window, and the app banner deflects many questions before chat starts. The runtime scales automatically, and instance limits protect the billing middleware, which is the slowest dependency." | 按邮编缓存+横幅分流+实例上限保护 |
| "A customer asks the agent to waive a late fee." | "The agent checks the policy and waives it if eligible." | "Credits are high-risk and not automated in the pilot. The agent explains the fee, checks eligibility against the policy articles, and creates a ticket with a summary. A human agent approves or declines it. The policy layer blocks any direct credit call regardless of what the model decides." | 高风险；建工单人工批；代码拦截 |
| "How do you know billing explanations are correct?" | "Gemini is very accurate, and we would test it." | "A golden set of 300 real conversations, labeled by senior agents, runs before every release. We measure groundedness against the billing articles and tool accuracy separately, so we can tell whether a failure comes from retrieval, the billing data, or the model's reasoning." | 黄金集；分开度量定位失败来源 |
| "Leadership wants voice next quarter. What changes?" | "We add speech-to-text and text-to-speech to the same agent." | "Voice adds strict latency requirements and telephony integration. We would evaluate prebuilt voice capabilities first, measure end-to-end latency on the billing API, and expand only after the chat pilot meets its targets. The tools, policy layer, and golden set carry over." | 先评估预置语音、测延迟、chat 达标后扩展 |
| "What does it cost?" (added) | "Not much, Flash is cheap." | "About 250,000 eligible chat and app conversations a month across three countries, roughly 80,000 in the pilot country. At about six turns, mostly on Flash, that's one to two cents per conversation — one to two thousand dollars a month for the pilot — to be confirmed with current pricing and measured traffic. It's small next to contact-center labor." | 给出估算链 |

强答案的共同模式：**把决策绑定到调研中的具体约束、说出执行机制、承认什么会改变决定**。被挑战时不要自动辩护——重述驱动该选择的约束，并说明什么变化会让另一个选择合理。

---

## 30. Case Debrief and Interview Follow-ups (Veltra)｜Veltra 复盘与追问

Source: https://www.educative.io/courses/forward-deployed-engineer/case-debrief-and-interview-follow-ups
相关内容见 Section I §16 CS2 Googleyness（场景化行为题）、§12/§22 复盘与可迁移原则。

### 要点 / Key ideas（新增）

设计讲完后面试官常留在同一案例上转向判断题——把技术与 Googleyness 信号结合。**回答场景化追问时，描述你在第一次对话中会做什么，而不只是最终结果**——信任在开启艰难对话时赢得或失去。

**Veltra Googleyness 场景**：

| 场景 (Scenario) | 考察维度 (Dimension) | 强回答要素 (Strong response) |
|---|---|---|
| 赞助人坚持试点必须达成完整 30% | 客户同理心、主人翁 | 理解目标背后的压力，展示试点实际能交付什么，提出试点结果如何通向完整目标 |
| CISO 团队在上线前两周提出日志保留问题 | 协作、模糊 | 视为合理关切，快速评估影响，给出带明确权衡的选项而不是坚持原日期 |
| 客服担心被取代 | 客户同理心、协作 | 让客服参与构建黄金集和审查交接；展示系统去除重复工作 |
| 试点解决率高但某客户群满意度下降 | 模糊、主人翁 | 先用 trace 与反馈调查再反应，找到原因，为该群体调整设计 |
| 缓存 bug 让 agent 把已恢复的停电报告为仍在进行 | 主人翁 | 直接承认错误、止损、修根因、加测试、与客户清晰沟通 |

**常见设计错误（Veltra 特有）**：照单全收简报（全渠道全类型端到端）；**索引全部 6,000 篇文章**（明知很多过时）；无理由提多 agent（账单、停电、工单分开 agent，而工具共享边界与 owner）；**让模型决定权限**（接受对话中的账号或邮编，靠 prompt 防止积分）；**忽略停电峰值**（平均负载下可用，流量三倍时压垮账单中间件）；评估留到最后；**忘记交接**（旧 chatbot 主要因客户要重复说明而失败）。

**可迁移原则（跨行业）**：

| 原则 (Principle) | Veltra 中 (In Veltra) | 其他行业 (Elsewhere) |
|---|---|---|
| 区分诉求与需求 | "端到端 agent" → 更快的账单与停电解决 | 银行要 "AI advisor" 可能只需更快回答费用问题 |
| 从窄而就绪的领域开始 | 账单文章最新且有 owner | 保险可从一个产品线的理赔问题开始 |
| 身份来自会话 | 客户令牌流到每个工具 | 医疗 agent 必须把记录限定于已认证患者 |
| 控制与风险匹配 | 积分走人工审查 | 零售可自动化某额度以下退款，更大额审查 |
| 用最简单 agent 模式 | 一个 agent 五个窄工具 | 多数行业首版 |
| 标准的买，特定的建 | 预置 agent assist，自定义账单逻辑 | 预置搜索 + 自定义业务规则 |
| 让客户专家定义正确性 | 资深客服标注黄金集 | 核保员 (underwriters)、临床医生、caseworker 标注测试用例 |
| 为最糟糕的一天设计 | 停电峰值决定缓存与扩展 | 零售旺季、报税截止、开放注册期 |

**新案例中按顺序问**：客户需要什么 → 哪些数据就绪 → agent 用谁的身份 → 哪些动作有风险 → 最简单设计是什么 → 什么能买 → 如何衡量正确性 → 系统最糟糕的一天是什么样。

### 面试怎么说 / How to say it in the interview — 场景题库（每题 STAR 风格英文模型答案）

**Q1. "Veltra's sponsor says leadership already committed to a 30% reduction this year and wants voice and plan changes in the pilot. How do you respond?"**
> **Situation/Task:** "The sponsor's credibility with leadership is on the line, so this is real pressure, not stubbornness — and my job is to protect both the pilot and the relationship.
> **Action:** In that first conversation, I'd start by acknowledging the commitment. Then I'd make the trade-off concrete: voice depends on telephony integration and plan changes depend on IT write approval, and neither can be ready in time, so adding them puts the whole pilot at risk. I'd offer a path: the pilot focuses on billing and outage contacts — over half of chat volume — and produces measured results within three months, and I'll model how those results scale across channels and contact types so leadership sees a credible plan toward 30%. And I'd offer to join the leadership conversation to explain the phases.
> **Result:** The sponsor goes to leadership with evidence and a plan rather than a promise, and the pilot stays deliverable."

中文：理解压力→说明具体权衡→提供路径与建模→陪同向上沟通；既不一味答应也不一味拒绝。

**Q2. "The CISO's team raises a log retention concern two weeks before launch."**
> **Situation/Task:** "The concern is valid — the CISO owns approval for anything touching customer data — and I need to turn it into a decision quickly rather than argue for the date.
> **Action:** I'd meet with their team the same day to understand exactly which logs and retention periods worry them, check what our pipeline actually stores after Sensitive Data Protection masking, and come back with options: shorten retention and adjust masking with no date change if that's enough, a short delay for a deeper fix, or a reduced launch that excludes the affected data path. Each option would state its risk and impact.
> **Result:** The CISO decides with clear trade-offs, and whatever we pick is documented and tested before launch."

中文：视为合理；快速评估；给带权衡的选项。

**Q3. "Contact-center agents worry the system will replace them."**
> **Situation/Task:** "Their adoption decides whether agent assist works, and they know the real customer problems better than anyone.
> **Action:** I'd involve senior agents in labeling the golden set and reviewing handoff summaries, so they shape what 'correct' means. I'd show concretely which repetitive lookups the system takes off their plate and how handoffs arrive with context so customers don't have to repeat themselves. Staffing decisions aren't mine to promise, and I'd say so.
> **Result:** Agents become co-owners of quality, and their feedback improves both the agent and the assist tool."

中文：让客服参与黄金集与交接审查；展示去除重复工作；不越权承诺人员。

**Q4. "Pilot resolution is strong, but satisfaction drops for one customer group."**
> **Situation/Task:** "A strong headline number can hide a group we're serving badly, and I own finding out why.
> **Action:** Before changing anything, I'd pull traces and feedback for that group to see where conversations go wrong — for example, correct answers that skip a step they need, a language nuance, or handoffs that happen too late. Once I'd found the cause, I'd adjust the design for that group and add their cases to the golden set.
> **Result:** We track that group's satisfaction separately in the next release, so the fix is verified rather than assumed."

中文：先调查再行动；按群体修复并单独跟踪。

**Q5. "A caching bug causes the agent to report a resolved outage as still active."**
> **Situation/Task:** "Customers are getting wrong information, and it's our bug.
> **Action:** I'd acknowledge it directly to the customer team, contain it immediately — invalidate the outage cache and, if needed, fall back to a direct feed lookup — then fix the root cause, such as a TTL or invalidation error, and add a regression test that a resolved outage clears within the refresh window. I'd tell Veltra clearly what happened, who was affected, and what we changed.
> **Result:** Correct status is restored, the failure is covered by a test, and the customer hears it from us first."

中文：直接承认→止损→修根因→加测试→清晰沟通。

---

## 速查 / Cheat sheet

1. **Confirmed vs reported vs unresolved｜已确认/报道/未决分开**：只把 recruiter 明确说的当事实；"vibe coding" 不授予 AI 工具权限，未声明的 AI 辅助一律视为不允许，每轮分别确认。
2. **One habit for every round｜每轮同一习惯**：clarify → scope a first version → build something that works → adapt；HC 看五轮一致性。
3. **Recruiter stories｜项目故事**：问题与范围 → 个人职责（"I" vs "we"）→ 约束与关键动作 → 结果与边界；分开验收测试、生产观察、估算收益（47/50 是预发布集，不是"94% 生产准确率"）。
4. **Coding｜编程**：45 分钟 = 澄清 5 / 方案 5 / 编码 20 / 测试 7 / 分析；按**正确性论证**选模式（负数 → 前缀和 + 哈希表，先查后插，`{0:1}` 初始化）。
5. **Vibe coding｜模糊实现**：短口头契约（输入、输出含义、失败行为）→ 最小端到端切片 + 测试 → 说出契约差异只改受影响部分 → 证据驱动调试（`'9' > '10'` 字符串比较 bug）。
6. **Agent design trace｜追踪一个请求**：身份 → 可信范围 → 授权读取 → 证据 → 模型起草 → 发布校验 → 记录 → 用户；**模型从不决定权限**，模型的工具调用只是提议。
7. **Timeouts｜超时**：超时 ≠ 空结果 ≠ 失败；写操作用稳定幂等键（O17），状态 OUTCOME_UNKNOWN → 对账 (reconciliation)；交接要携带不确定性，**绝不用新 ID 盲目重试**。
8. **Critical path & Little's law｜关键路径**：0.2 + max(0.6, 0.8) + 1.4 + 0.2 = 2.6 s；20 RPS × 2.6 s ≈ 52 并发；依赖变 3 s → 4.8 s 破约 → 谈判（放宽 / 异步 / 先给部分），不悄悄缓存。
9. **Managed-first｜托管优先**：零售 → Conversational Analytics API（LookML）；电信 → Customer Engagement Suite / Gemini Enterprise for CX（Flows + Playbooks + Agent Assist）；文档 → Document AI；用同一验收契约评估，自定义只补已证明的缺口。
10. **Semantics before tuning｜先语义后调优**：冲突的 net_sales 定义要 owner 批准；更强模型只会更流畅地解释未授权含义；评估比较**类型化结果**而不是 SQL 文本。
11. **Honest denominators｜诚实分母**：85% × 300 = 255；拒答不算匹配也不能移出分母（240/300 = 80%，不是 100%）；达标 ≠ 可发布，权限失败是独立阻断项。
12. **Data authority in the DB｜数据库层强制权限**：user-bound principal + 行级策略 + 授权视图 + dry run + `maximum_bytes_billed=B`；B 未批准 → 生产执行阻塞；负面测试直接执行越权 SQL。
13. **Risk tiers｜风险层级**：读 → 自动；可逆写 → 绑定具体提议的显式确认 + 确定性执行；重大决定（取消、信用、资格）→ 人工或固定规则；"yes" 不能修复缺失身份或权限。
14. **Resolution ≠ containment｜解决≠围堵**：放弃离开不算解决；成功转人工是好服务但不算自助；分开测量解决、7 天重复联系、满意度、交接质量、越权操作（目标为零）。
15. **Assistance, not decisions｜辅助不是决定**：缺失证据 ≠ 不合格；标记一旦成为拒绝的充分触发条件就越权；实质审查 = 看证据 + 区分建议 + 可更正 + 保留决定权；关键字段无论置信度都需确认。
16. **Sovereignty｜主权**：存储位置 ≠ 处理位置；逐组件位置清单（推理、裁剪、日志、备份、支持）；Preview 版本在 US+EU 处理 → 阻止；认证前只用合成数据。
17. **Googleyness formula｜行为题公式**：Situation → Constraint → **Decision（大部分时间）** → Outcome → Reflection；五要素 = 对方目标 + 实质风险 + 具体提议 + 权限边界 + 产生证据的下一步；6–8 个故事覆盖四维度各至少两次。
18. **Saying no well｜好好说不**：先公开纠正解读再私下调查；拒绝阻挠设计但给一个公平可拒绝的替代；不承诺人员、法律、认证结果；记录分歧并升级到决策者；诚实的未解决结果是可接受的。
19. **Incident order｜事故顺序**：止损（授权暂停/回滚 (rollback) + 保留记录）→ 核实范围 → 账户更正（权威记录验证）→ 公开沟通 → 回归测试 (regression tests)；补丁上线 ≠ 客户已修复。
20. **What transfers｜可迁移的**：决策序列（结果与决策者 → 真实瓶颈 → 边界 → 托管基线 → 失败与人工路径 → 证据与验收）不变；架构随最难约束变化（含义 / 持久账户效果 / 可检查的文档证据）。
