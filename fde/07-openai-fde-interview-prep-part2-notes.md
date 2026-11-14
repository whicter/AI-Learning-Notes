# OpenAI FDE Interview Prep, Part 2: Interview Loop & Case Studies｜OpenAI FDE 面试准备（下）：面试流程与案例

---

# Section I｜第一部分：OpenAI FDE Interview Prep（面试流程 + 三个案例）

## 1. The Interview Loop Overview｜面试流程总览

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/the-interview-loop-overview

**要点 / Key ideas**

- 核心原则：按 OpenAI **官方描述的流程**准备，一旦招聘官 (recruiter) 发来真实说明 (assessment materials)，**以说明为准**。别人的面经 (interview reports) ≠ 你的规则。
- OpenAI 官方面试指南 (interview guide) 给出的 **示例流程 (example process)**，五步，且明确说"个人经历可能不同"：

| 阶段 Stage | 内容 What happens | 时间 Timing |
|---|---|---|
| 简历筛选 Application & résumé review | 招聘团队审简历 | 通常 1 周内 |
| 初步通话 Introductory calls | 和 recruiter 或招聘经理 (hiring manager) 聊经历、动机、目标 | — |
| 技能评估 Skills-based assessments | 团队提供说明与准备材料；形式可能是结对编程 (pair coding)、带回家作业 (take-home)、技术测试 (technical test)，部分岗位不止一项 | — |
| 终面 Final interviews | 关注你的专长领域 + 解题方式 | **4–6 小时，4–6 人，1–2 天** |
| 决定 Decision | 通常 1 周内反馈，可能要推荐人 (references) | 1 周 |

- 工程面试 OpenAI 一般看：**设计良好的方案 (well-designed solutions)、高质量代码 (high-quality code)、最优性能 (optimal performance)、良好测试覆盖 (good test coverage)**；同时看你如何处理问题、做决定、表达推理。
- 两条规则：① 官方指南只是示例，**没有哪一轮是保证的**；② **你自己的评估材料决定该评估**——尤其是能否用哪些工具 (tool permissions)，不清楚就**提前问 recruiter**。
- FDE 专属的"可能形态 (likely shape)"（不是承诺）：take-home + **录制讲解 (recorded walkthrough)**，然后技术深挖 (technical deep dive)。综合起来预期三类 FDE 评估：
  1. **编码轮 (coding stage)**：结对编程或技术测试，写并讲解可运行的 Python；
  2. **客户式案例 take-home (customer-style case)**：你来界定范围 (scope)、设计、并带面试官走一遍；
  3. **LLM 系统深挖 (LLM systems deep dive)**：智能体 (agents)、检索 (retrieval)、评测 (evals)、延迟 (latency)、成本 (cost)、故障处理 (failure handling)。

**信息来源权威度 / Source authority（课内配对练习）**

| 陈述 Statement | 含义 Implication |
|---|---|
| OpenAI 指南列出可能的评估形式 | 官方示例，你的经历可能不同 (official example guidance) |
| 你的准备笔记说会有 take-home 讲解 + 深挖 | 可能形态，值得练，但不是既定顺序 (likely shape, not established sequence) |
| 你的评估材料禁止 AI 辅助 | **以此为准**：评估中不用 AI (governing instruction) |
| 你的评估材料对工具权限没说清 | 面试前问 recruiter (ask before the interview) |

→ 第三条（评估材料）胜出。可以私下用 AI 面试官排练，但评估本身禁止就不能用。

**每一轮考什么 / What each stage tests（准备目标，非官方评分表）**

| 轮次 Stage | 考察问题 What it probes |
|---|---|
| 初步通话 Intro call | 能否清楚讲动机 + 一个项目，把"客户需要什么"和"你做了什么"连起来 |
| 编码 Coding | 实现定义清楚的方案、测正常与失败用例、讲质量与性能取舍；**有/无 AI 助手都要练** |
| Take-home + 展示 | 界定模糊需求、选首个交付物 (first delivery)、说明发布需要什么证据 (proof)、交接后谁运营 (who runs it after handoff) |
| 系统深挖 Systems deep dive | 为检索、评测、延迟、安全、故障处理的选择辩护，并说清**约束变化时什么跟着变** |
| 终面 Final | 在多位面试官面前保持一致，包括使命 (mission) 与安全 (safety) 问题 |

沟通、协作、判断 (communication, collaboration, judgment) 贯穿所有轮次。例：检索系统设计得再好，也要回答"谁有权看检索到的材料？权限检查失败怎么办？"

**压力下的强答案 / Strong answer under pressure — Northstar D-04 示例**

- 情境：工单 NS-452，源事件 (source event) 显示 `scheduled`，但映射器 (mapper) v1 输出 `visit_completed=true`。mapper 是第一个出错步骤。修复：保留状态与源版本 (source version)，并加验收检查 (acceptance check) 拒绝源数据不支持的"已完成"声明。修复后本地能力测试 (local capability result) 8/8。
- 弱答案：把 8/8 当生产证明、把"草稿看起来对"当无副作用证明。→ 把本地结果夸大为生产结论 (stretching a local result into a production claim)。
- 强答案要点：说清事实 → 修复 → **8/8 只覆盖本地能力检查**，和留出集 (holdout) 结果、副作用 (effect) 结果分开报告 → 不声称已上线、不声称已有运营负责人 (operating owner)。
- 追问"效果采集器 (effect collector) 离线了，空的效果记录说明什么？"→ **什么都说明不了 (nothing either way)**。保持该路径关闭，人工处理；试点前先恢复并验证执行边界 (execution boundary) 的覆盖，跑修复门槛与 holdout 门槛，找到工程与运营的监控 (monitoring)/回退 (rollback)负责人。试点还需约定的值守窗口 (staffed window)、阈值 (thresholds)、关闭开关 (kill switch)。

**自评量表 / Six-dimension self-assessment rubric（课程工具，非 OpenAI 评分）**

每维 0 / 1 / 2：0 = 遗漏或与事实矛盾；1 = 碰到但有重要缺口；2 = 给出具体决定 + 支撑 + 局限。

| 维度 Dimension | 看什么 What it checks | 弱 D-04 答案得分 |
|---|---|---|
| 客户框定 Customer framing | 用户、工作流问题、失败的代价 | 1 |
| 归属 Ownership | 你的贡献 vs 团队；谁负责运营 | 0 |
| 技术推理 Technical reasoning | 哪里坏、怎么修、一个真实取舍 | 1 |
| 证据 Proof | 每个结果说明什么、到哪为止 | 0 |
| 安全 Safety | 风险边界、缺证据时关掉什么、回退方案 | 0 |
| 沟通 Communication | 听者能跟上决定、证据、下一步 | 2 |

**不要加总**：流畅表达不能抵消不安全的发布决定。Northstar 是课程练习案例，不能当自己的成就讲。

**备考计划 / Preparation plan**：每个优先项写四件事——缺口 (gap)、练习动作 (practice action)、如何判断进步 (progress check)、复盘时间 (review date)。6 小时示例：2h 技术复现与测试（加一个"源状态缺失/变化"的测试）；1.5h 模拟面试与修订；1h 整理一个可分享的工作记录（输入、预期行为、版本、命令、输出）；1h 安全与客户判断（练采集器离线决策）；0.5h 读评估说明、发权限问题给 recruiter。

课内测验：备考备忘录声称"官方指南保证每个 FDE 候选人都有 take-home + 录制讲解 + 深挖"——错，指南只给示例且说形式会变。

<svg viewBox="0 0 820 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="300" fill="#fff"/>
  <text x="410" y="24" font-size="15" font-weight="bold" text-anchor="middle">OpenAI FDE Interview Loop｜面试流程（示例，非保证）</text>
  <g font-size="12" text-anchor="middle">
    <rect x="10" y="50" width="120" height="60" rx="8" fill="#e8f0fe" stroke="#4a6fd1"/>
    <text x="70" y="74">Résumé review</text><text x="70" y="92">简历筛选 ~1 wk</text>
    <rect x="150" y="50" width="120" height="60" rx="8" fill="#e8f0fe" stroke="#4a6fd1"/>
    <text x="210" y="74">Recruiter / HM</text><text x="210" y="92">初步通话</text>
    <rect x="290" y="50" width="240" height="60" rx="8" fill="#fff4e0" stroke="#d18a1a"/>
    <text x="410" y="74">Skills assessments 技能评估</text><text x="410" y="92">formats vary 形式因团队而异</text>
    <rect x="550" y="50" width="130" height="60" rx="8" fill="#e8f0fe" stroke="#4a6fd1"/>
    <text x="615" y="70">Final interviews</text><text x="615" y="86">终面 4–6h</text><text x="615" y="101">4–6 people, 1–2 days</text>
    <rect x="700" y="50" width="110" height="60" rx="8" fill="#e6f4ea" stroke="#2e8b57"/>
    <text x="755" y="74">Decision</text><text x="755" y="92">决定 ~1 wk</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <path d="M130 80 L150 80"/><path d="M270 80 L290 80"/><path d="M530 80 L550 80"/><path d="M680 80 L700 80"/>
  </g>
  <g font-size="12" text-anchor="middle">
    <rect x="290" y="150" width="75" height="70" rx="6" fill="#fdf7ec" stroke="#d18a1a"/>
    <text x="327" y="175">Coding</text><text x="327" y="192">编码轮</text><text x="327" y="209">Python</text>
    <rect x="372" y="150" width="78" height="70" rx="6" fill="#fdf7ec" stroke="#d18a1a"/>
    <text x="411" y="172">Take-home</text><text x="411" y="188">案例 +</text><text x="411" y="204">walkthrough</text>
    <rect x="457" y="150" width="73" height="70" rx="6" fill="#fdf7ec" stroke="#d18a1a"/>
    <text x="493" y="172">LLM sys</text><text x="493" y="188">deep dive</text><text x="493" y="204">系统深挖</text>
    <rect x="550" y="150" width="130" height="70" rx="6" fill="#eef3fd" stroke="#4a6fd1"/>
    <text x="615" y="172">HM conversation</text><text x="615" y="188">Mission / safety</text><text x="615" y="204">使命与安全</text>
  </g>
  <g stroke="#999" stroke-dasharray="4 3" fill="none"><path d="M410 110 L410 150"/><path d="M615 110 L615 150"/></g>
  <text x="410" y="245" font-size="12" text-anchor="middle" fill="#a33">Your assessment materials govern: tools / AI permission → ask recruiter</text>
  <text x="410" y="263" font-size="12" text-anchor="middle" fill="#a33">评估材料为准：工具/AI 权限不清 → 先问 recruiter</text>
  <text x="70" y="160" font-size="12" text-anchor="middle" fill="#555">Project story</text>
  <text x="70" y="176" font-size="12" text-anchor="middle" fill="#555">项目故事贯穿</text>
  <text x="70" y="192" font-size="12" text-anchor="middle" fill="#555">every stage</text>
</svg>

**面试怎么说 / How to say it in the interview**

- Q: "You found the D-04 problem. What did your fix accomplish?"
  - EN: "The source said scheduled, but mapper version 1 emitted visit_completed=true, so the mapper was the first wrong step. I repaired it to keep the status and source version, and added an acceptance check that rejects completion claims the source doesn't support. The 8/8 result covers only the local capability checks — I'd report it separately from the holdout and effect results, and I wouldn't claim a production rollout or an agreed owner yet."
  - 中文：8/8 只是本地能力检查，不等于生产，也不等于有人接手。
- Q: "The effect collector was offline. What does an empty effect record tell you?"
  - EN: "Nothing either way — absence of evidence isn't evidence of no side effects. I'd keep that path switched off and route the work to operators, restore and verify coverage at the execution boundary, rerun the repair and holdout gates, and get engineering and ops owners for monitoring and fallback before proposing a pilot."
  - 中文：空记录 ≠ 没有副作用；先关路径、人工兜底、恢复覆盖再谈试点。
- Q: "Can you use AI in this assessment? Another candidate said it was fine."
  - EN: "I follow the instructions for my specific assessment. If they don't say, I ask the recruiter beforehand — someone else's experience doesn't grant me permission."
  - 中文：以自己的评估说明为准，不清楚就问。

---

## 2. Your Project Story｜你的项目故事

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/your-project-story

**要点 / Key ideas**

- 每一轮都会问"讲讲你做过的东西 (Tell me about something you built)"。正确做法：**一个准备好的项目故事，不同深度讲**——事实不变，只变侧重点。
- 五段式框架 **客户 → 问题 → 构建 → 证据 → 交接 (customer → problem → build → proof → handoff)**：

| 部分 Part | 回答的问题 Question it answers |
|---|---|
| 客户 Customer | 谁用/谁需要？内部运营、其他工程团队、外部客户都算 |
| 问题 Problem | 他们的工作流哪里出错，为什么重要 |
| 构建 Build | 你决定并实现了什么；协作者贡献了什么 |
| 证据 Proof | 你检查了什么、说明了什么、**结果到哪为止** |
| 交接 Handoff | 之后谁负责运营？**没人接就直说** |

- 框架呼应岗位职责：发现 (discovery)、界定 (scoping)、设计、构建、上线、与客户团队合作、采用 (adoption)、工作流影响 (workflow impact)、评测驱动反馈 (eval-driven feedback)；重视直接写代码、交付取舍、可复用模式。故事**不必声称上了生产**。
- 选项目标准：能说清谁的工作流重要（哪怕通过客户经理间接接触）；能区分你做的 vs 队友做的；能说出一个备选方案及为何没选；知道测了什么、多少样本 (denominator)、什么仍未知；能说出角色和谁真正同意运营。
- **一个小而可核查的试点 (small, checkable pilot) 胜过讲不清的著名项目**。保密数据不要进练习笔记。

**项目选择矩阵 / Project scoring（课内示例，各项权重 3，分数 1–10）**

| 标准 Criterion | 小型已复盘试点 Small reviewed pilot | 讲不清的著名项目 Famous deployment | 无记录结果的内部工具 Internal tool, no results |
|---|---|---|---|
| 可接触的用户上下文 Accessible user context | 24 | 18 | 21 |
| 可归属的决策与工作 Attributable decisions | 24 | 9 | 21 |
| 有意义的取舍 Meaningful trade-off | 24 | 12 | 15 |
| 有边界的证据 Bounded evidence | 21 | 9 | 6 |
| 协作与交接 Collaboration & handoff | 18 | 15 | 9 |
| **总计 Total** | **111** | 63 | 72 |

**示例：服务路由 (service routing) 项目记录 → 故事**

- 背景：服务运营人员 (service operators) 要把请求路由到正确团队，路由错误造成返工 (rework)。团队考虑过自动派单 (automatic dispatch)，工程师选择 **需人工审核的路由草稿 (review-required routing draft)**：运营看到建议路由后自己决定。工程师做了分类器 (classifier) 和审核界面 (review screen)，运营定义了路由标签 (labels)。取舍：保留人工检查，牺牲自动派单的速度。
- 五项记录：设计说明（含被否决的自动派单）、实现记录（分类器+界面归工程师，标签归运营）、早期复盘 14/20 正确、试点复盘 17/20 正确（3 个错）、交接说明（运营主管同意继续审核试点）。
- 课内测验——最强可支撑的说法：**"试点复盘 17/20 正确，此前 14/20；运营同意继续试点审核。"** 不能说"提升 15 个百分点"：70% vs 85% 的差来自**未匹配的两组 (unmatched groups)**，不能说明因果 (causation)，20 个样本也无法确立一般准确率。也不能说"全面上线"。
- 三个错误路由恰恰说明审核步骤的价值；记录没写如何纠正，故事里也**不要编**。

**修复夸大 / Repairing an overclaim**

弱答案"我自动化了派单，准确率提升 15 个点，交付了生产系统"犯了三个错：草稿 → 自动执行；未匹配比较 → 因果提升；试点审核 → 生产交接；还丢掉了 3 个错误和运营的标签工作。

**按轮次调整深度 / Depth by stage（事实不变）**

| 轮次 Stage | 侧重 Emphasis |
|---|---|
| 初步通话 Intro call | 4 句话：用户、你的贡献、一个结果、当前状态 |
| 案例展示 Case presentation | 加上界定决策、备选方案、比较的局限、谁负责试点 |
| 系统深挖 Deep dive | 讲清**模型建议在哪里停止、人工决定从哪里开始**（边界） |

简历要点 (résumé bullet)：先写你的贡献和用户工作流，结果带分母，交接写到记录支持的范围。例：*"Built a review-required routing draft for service operators; in a 20-request pilot review, 17 routes were correct, and operations took on ongoing pilot review."* 无法支撑分母/来源的指标就删掉。

**面试怎么说 / How to say it in the interview**

- Intro version (EN): "Service operators were dealing with misrouted requests. I built a classifier and review screen for a routing draft, and operations defined the labels. In a 20-request pilot review, 17 routes were correct. The operations lead agreed to continue the pilot."
  - 中文：四句话版，用户—贡献—结果—状态。
- Presentation version (EN): "Operators needed help routing requests without making a wrong dispatch harder to catch. I chose a review-required draft over automatic dispatch and built the classifier and review screen; operations defined the labels. An earlier review found 14 of 20 correct and a separate pilot found 17 of 20, with three errors — those groups weren't matched, so I don't claim a causal gain. The operations lead agreed to continue pilot review; it hasn't gone to full rollout."
  - 中文：加上取舍、比较局限、交接范围。
- Deep-dive version (EN): "The classifier proposes a route and an operator reviews it on a screen. I put the boundary there instead of automatic dispatch so a person checks each proposal before routing. The pilot had three wrong routes out of 20, which is exactly why that boundary matters."
  - 中文：讲清人机边界在哪里、为什么。
- Follow-up "What did you do about the three wrong routes?" (EN): "The pilot review identified them, but I don't have a record of a specific correction or classifier change, so I won't claim one."
  - 中文：没有记录就不声称。

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 35 篇）。

  - 中文：四句话版：用户/义务 — 我的贡献 — 结果 — 可深入方向。
  - 中文：加上取舍、被否决的方案（自建 pipeline）、边界。
  - 中文：讲清各阶段边界在哪里、为什么。
- Follow-up "What numbers can you share?" (EN): "I'd rather not quote volumes; I can tell you what shipped, what I designed, and where the cross-team boundary sits."
  - 中文：不报绝对业务量，不编指标。

---

## 3. The Recruiter Screen｜招聘官初筛

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/the-recruiter-screen

**要点 / Key ideas**

- 最短、也最容易准备不足的一轮。问题看似简单：为什么 OpenAI、为什么这个岗位、做过什么、你想了解什么。
- 初步通话是**双向的 (two-way)**，通常涵盖三件事：
  1. **动机 (motivation)**：工作/学术经历、动机、目标；
  2. **契合度 (fit)**：OpenAI 看重协作 (collaboration)、有效沟通 (effective communication)、**乐于接受反馈 (openness to feedback)**、与使命和价值观一致 (alignment with mission and values)；
  3. **后勤 (logistics)**：地点、出差、时间、后续阶段。
- 直接回答 + 一个具体例子 + 留出追问空间。不要背整个履历——要留时间问自己的问题。不知道就说不知道；**主动纠正自己的夸大**本身就展示了"乐于接受反馈"。

**"为什么 OpenAI" vs "为什么 FDE" / Why OpenAI vs Why FDE**

| 问题 Question | 实际在问 What it really asks | 好答案要素 Good answer |
|---|---|---|
| Why OpenAI? | 这个组织与使命为什么对你重要 | 使命："确保通用人工智能 (AGI) 造福全人类"；连接到你真实持有的理由（如强大系统如何负责任地部署），再连接到自己工作中的一个决定 |
| Why FDE? | 为什么想做这种工作 | 岗位：从客户发现、技术界定到系统设计、构建、上线，与客户工程/领域团队直接合作；成功看生产采用、工作流影响、评测反馈。选你真正喜欢的一面（贴近用户 / 贴近代码）并用可支撑的经历连接 |

- 反例开场："OpenAI 是最好的 AI 公司，我想做重要的技术"——热情但空洞。正例："我关注强大 AI 系统如何负责任地到达用户。做一个带人工审核的路由试点让我想深入了解模型出错落在真实工作流时的部署决策。"
- 经历比岗位范围窄就直说做过什么、想成长到哪里。

**弱答案拆解（课内测验）**："我上线了自动派单系统，准确率提升 15 个点并推到生产"——三处与记录矛盾：① 草稿需要人工审核，没有自动派单；② 14/20→17/20 来自未匹配组，不同请求组合可能解释部分或全部差异；③ 运营只同意继续试点审核，不是接手生产系统。

**该问的问题（按优先级）/ Questions to ask, prioritized**

| 主题 Topic | 示例问题 Example question |
|---|---|
| 评估说明 Assessment instructions | "What preparation materials will I get, and which AI or other tools are allowed in each assessment?" |
| 上线后归属 Ownership after launch | "For this role, what does the FDE still own once a customer starts using a system?" |
| 协作 Collaboration | "How does the FDE work with customer engineers and domain experts, and which internal teams are involved?" |
| 实际条件 Practical terms | "What are the location, travel, and timing expectations for this position?" |

- 课内测验：材料没说能否用 AI，你练习时用过，另一个候选人说允许——**正确做法：评估前问 recruiter "Which AI or other tools are permitted for this assessment?"**
- "上线后归属"问题兼做契合度检查：想要长期负责系统，就听谁处理上线后的故障、客户如何接手。
- 苏黎世 (Zurich) FDE 职位：**每周 3 天到办公室，出差最多 50%**（50% 是上限不是日程）。只陈述需要回答的约束，不必透露个人细节。

**面试怎么说 / How to say it in the interview**

- Q: "Why OpenAI?"
  - EN: "I'm motivated by how increasingly capable AI can benefit people through responsible deployment. In a service-routing pilot, I chose to keep an operator reviewing proposed routes because errors landed in their workflow. That made me want to work where capable models meet careful deployment. The pilot was small, so I wouldn't claim broad impact from it."
  - 中文：使命 + 自己的一个部署决定 + 不夸大。
- Q: "Why forward deployed engineering?"
  - EN: "I enjoy working close to the people using a system and making the trade-offs that fit their workflow. For service operators dealing with misrouting, I chose a review-required draft and built its classifier and screen, while operations defined the labels. The pilot review found 17 of 20 routes correct, with three errors, and operations agreed to continue the pilot. I want to take on more of the path from discovery to production."
  - 中文：贴近用户做取舍；五段式压成几句话。
- Q: "Did you deploy automatic dispatch or own production yourself?"
  - EN: "No. I chose a review-required draft over automatic dispatch and built the classifier and review screen; operations defined the labels. An earlier review had 14 of 20, but the groups weren't matched, so I can't credit the difference to my system. Operations agreed to continue pilot review, and it hasn't gone to full rollout."
  - 中文：被追问时缩窄说法，而不是更自信地重复。
- Q: "The posting says travel up to 50%. Any concerns?"
  - EN: "That works for me. Could you tell me how travel is usually spread across engagements on this team, so I can plan around it?"
  - 中文：直接接受，顺带问清分布方式。

---

## 4. The Coding Round｜编码轮

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/the-coding-round

**要点 / Key ideas**

- FDE 编码轮通常是**实用型 (practical)**，接近真实集成工作的小任务，而非算法谜题。难点：**想清楚函数返回前必须成立什么 (invariant)**，再证明代码强制了它，同时边写边讲。
- 拿到任务先读说明：交付物 (deliverable)、允许的工具、输入/输出契约 (input/output contract)、约束。有歧义**先问再写**。
- 生产质量 (production quality) 在面试中 = 清晰契约 + 显式检查 + 覆盖失败用例的测试，**不是框架**。

**R7 题目 / Problem statement (English)**

> Northstar request `R7` expects tool calls `c1`, `c2`, `c3`. Each result record has `request_id`, `call_id`, and a string `payload`; records can arrive in any order. Write a pure Python function that returns the payloads in expected-call order, but only if every expected call has exactly one valid result for R7. Otherwise raise `ValueError` before returning anything.

假设 (assumptions) 先钉死：
- 期望 ID 都是唯一非空字符串，request ID 也是；
- 每条记录三个字段齐全，ID 非空字符串，payload 是字符串（**允许空 payload**）；
- 无期望调用 + 无记录 → 返回空列表；无期望调用但有记录 → 非法；
- 外来请求 (foreign request)、未知调用 (unknown call)、重复调用 (duplicate)、缺失调用 (missing)、格式错误 (malformed) → 都在返回前抛 `ValueError`。

**不变量 (invariant)**：返回时，每个输出 payload 都属于该请求 ID，且恰好对应一个期望调用。这是**本地关联 (local correlation)**——ID 匹配**不等于**认证调用方或授权访问。

```text
Input:  request_id="R7", expected=["c1","c2","c3"]
        records=[c2:B, c1:A, c3:C]
Output: ["A", "B", "C"]

Input:  records=[c1:A, c1:X, c2:B]          # count matches, but c1 repeats and c3 missing
Output: ValueError("duplicate call ID")      # no partial list

Input:  records=[c1:A, c1:X, c2:B, c3:C]     # complete set, but duplicate
Output: ValueError("duplicate call ID")

Input:  records=[c1:A, c2:B]
Output: ValueError("missing call ID")

Input:  request_id="R7", expected=[], records=[]
Output: []
```

**陷阱 / The trap**：`c1:A, c1:X, c2:B` 长度检查 3=3 通过；字典推导式 (dict comprehension) 会**静默用 X 覆盖 A**，c3 丢失。所以：遍历时先检测重复（立即报错，不返回部分结果），遍历后再比较观察到的 ID 集合与期望集合（完整性检查 completeness check）。
课内测验：去掉重复检测、只保留完整性和 request-ID 检查，哪个输入会错误通过？→ **`c1:A, c1:X, c2:B, c3:C`**（覆盖后三个 key 仍齐全）。计数检查能拒绝它，但显式重复检测能立刻指出坏记录。

```python
from typing import TypedDict


class ResultRecord(TypedDict):
    request_id: str
    call_id: str
    payload: str


def correlate(request_id: str, expected_ids: list[str], records: list[ResultRecord]) -> list[str]:
    """Return complete request-bound payloads in expected-call order."""
    if not isinstance(request_id, str) or not request_id:
        raise ValueError("request_id must be a nonempty string")
    if not isinstance(expected_ids, list):
        raise ValueError("expected_ids must be a list")
    expected: set[str] = set()
    for call_id in expected_ids:
        if not isinstance(call_id, str) or not call_id:
            raise ValueError("expected call IDs must be nonempty strings")
        if call_id in expected:
            raise ValueError("duplicate expected call ID")
        expected.add(call_id)
    if not isinstance(records, list):
        raise ValueError("records must be a list")

    payload_by_call: dict[str, str] = {}
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("record must be a dictionary")
        record_request = record.get("request_id")
        call_id = record.get("call_id")
        payload = record.get("payload")
        if not isinstance(record_request, str) or not record_request:
            raise ValueError("record request_id must be a nonempty string")
        if not isinstance(call_id, str) or not call_id:
            raise ValueError("record call_id must be a nonempty string")
        if not isinstance(payload, str):
            raise ValueError("record payload must be a string")
        if record_request != request_id:
            raise ValueError("foreign request")
        if call_id not in expected:
            raise ValueError("unknown call ID")
        if call_id in payload_by_call:
            raise ValueError("duplicate call ID")
        payload_by_call[call_id] = payload

    if set(payload_by_call) != expected:
        raise ValueError("missing call ID")
    return [payload_by_call[call_id] for call_id in expected_ids]
```

**课内 10 个测试 / The ten tests**：乱序成功、重复+缺失、完整但重复、外来请求、未知调用、缺失调用、空输入（空/空 → `[]`；空期望+有记录 → unknown）、重复期望 ID、格式错误字段（缺 payload、空 call_id、payload 为 int、空 request_id，加上空 request_id 参数、空期望 ID）、测试数据隔离 (fixture isolation，每个测试用工厂函数 (factory function) `fresh_records()` 得到新数据，避免测试间串改)。建议自己再加一个：**空 payload 接受、空 call_id 拒绝**。运行：`python coding_round.py`（Python 3.11+），读输出，失败先修再声称成功。

**要大声讲的决策 / Decisions to say out loud**

| 决策 Decision | 说法 What to say |
|---|---|
| 类型注解 Annotations | `TypedDict` 和签名只**记录**接口，Python 运行时不强制；显式检查把格式错误变成 `ValueError` |
| 成员与唯一性 Membership & uniqueness | 期望集合 (set) 标记未知调用；payload 字典兼做"已见集合"，在覆盖前拒绝重复 |
| 完整性 Completeness | 输出列表生成前比较观察 key 与期望 ID；空期望集只在无记录时成功 |
| 复杂度 Cost | n 个期望 ID、m 条记录：期望 **O(n + m)** 时间、**O(n + m)** 额外空间 |
| 范围 Scope | 一个函数 + 标准库测试就够；框架/网络服务/分布式设计只会增加决策而不加强契约 |

- **异步 (async)**：关联函数从不等待，改成 async 没意义。外层若等待独立结果：`await asyncio.sleep(...)` 让出给其他任务，`time.sleep(...)` 阻塞事件循环 (event loop)线程。并发 (concurrent)请求和测试需要独立的可变记录，或显式同步。
- **AI 助手 (AI assistant)**：允许时也要对照契约核查建议、自己确认预期行为、跑测试、**能解释提交的每一行**；不允许就独立完成。课程代码中的 `--suggest` 选项可调用 OpenAI SDK（模型 `gpt-6-luna`）建议一个测试，API key 放环境变量，不进文件和版本控制 (version control)；回复只当候选测试。
- 边写边讲用"有用的单元"：契约和假设 → 不变量 → 为什么 set + dict → 看到的测试结果 → 仍有歧义的需求。不要逐键解说。

**面试怎么说 / How to say it in the interview**

- Q: "Three results arrived for three expected calls. Is that enough to return them?"
  - EN: "No — counts can match while the content is wrong. With c1:A, c1:X, c2:B, c1 repeats and c3 is missing. I reject the second c1 before returning anything, and after reading all records I also compare observed IDs with the expected set, so a missing call is caught even without a duplicate."
  - 中文：数量相等不代表正确，重复检测和完整性检查是两道独立的闸。
- Q: "What's the contract and complexity?"
  - EN: "Every returned payload belongs to R7 and maps to exactly one expected call, in expected order; anything foreign, unknown, duplicate, missing, or malformed raises ValueError with no partial output. I use a set for expected membership and a dict keyed by call ID that doubles as the seen set. It's O(n + m) time and space."
  - 中文：契约 + 数据结构 + 复杂度一口气说完。
- Q: "How do you know it behaves that way?"
  - EN: "The duplicate-plus-missing test covers exactly that input. I ran the suite with `python coding_round.py`, and I'd show the runner output rather than ask you to trust me."
  - 中文：用测试和输出证明，而不是靠自信。
- Q: "Are type hints enough validation?"
  - EN: "No. TypedDict documents the shape but Python doesn't enforce it at runtime, so I check each field explicitly and raise ValueError on malformed input."
  - 中文：类型注解不做运行时校验。

---

## 5. The Case Study and Presentation｜案例与展示

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/the-case-study-and-presentation

**要点 / Key ideas**

- 编码题有函数契约；部署案例 (deployment case) 有客户，但**没人告诉你该建什么**。FDE take-home 通常是部署案例，之后现场展示与答辩。难点：选工作流、选产物 (artifact)、选能证明它的证据。**窄而可运行的提交 (narrow, runnable submission)** 给面试官可检查的东西，也给你需求变化时可守的边界。
- 从 brief 中先提取五件事：① 要改进的工作流及其用户；② 要求的提交物（代码/文档/录屏…）；③ 允许的工具和帮助；④ 展示形式、受众、时长；⑤ **未决需求**（答案会改变设计或证据）。

**Northstar 案例 / Northstar Equipment Services**

> Problem statement (EN): Northstar wants faster service-request handling and a demonstration a reviewer can reproduce. Today operators read incoming notes, look up service records they're allowed to see, classify urgency, draft a response, and decide whether to escalate or close. Operators must keep the final decision.

改变设计的提问 (design-changing questions)：

| 主题 Topic | 问题 Question | 影响 Impact |
|---|---|---|
| 访问 Access | 哪些运营/服务身份能读哪些记录？ | 没人能回答 → 只用测试记录 |
| 错误代价 Error cost | 紧急当成常规、草稿依赖过期记录会怎样？ | 哪些错误需要单独的发布门槛 (release gate) |
| 审核 Review | 运营接受/纠正草稿前必须看到什么？ | 决定输出与界面 |
| 执行 Execution | 审阅者 (reviewers)能跑什么、允许哪些依赖？ | 决定安装与可复现性 |
| 运营 Operation | 谁定义标签、审核输出、维护权限、支持试点？ | 交接 |

未回答的问题都写成**假设 (assumption)**——"客户工程负责身份配置"在对方同意前只是提议。

**该建什么 / What to build**：**运营审核的只读分诊草稿 (operator-reviewed, read-only triage draft)**：读取运营有权看的记录 → 从固定集合中建议紧急度标签 → 不确定就转人工审核。运营保留处置决定，系统**没有写工单或发消息的能力**。对比"自动关工单/发消息"的宽原型：需要授权规则、动作控制、观测实际效果、运营流程——brief 一个都没解决，漂亮界面替代不了这些决定。

起点 `northstar_workflow.py`：测试记录、本地测试身份 + 权限检查 (entitlement check)、**单次调用预算 (one-call budget)**、固定允许标签集、已知失败的人工审核路由。离线运行：`python northstar_workflow.py`。文件**没有过期证据检查 (stale-evidence check)、没有消息路径**——两者都作为提议呈现。

**产物清单 / Artifact manifest（README）**

| 项 Item | 内容 Content |
|---|---|
| 安装与输入 Setup & inputs | Python 要求、测试记录、测试身份、配置 |
| 命令 Command | 提交版本的确切命令与运行位置 |
| 预期行为 Expected behavior | 有权输入 → 分诊草稿；拒绝访问、非法标签、分类失败、过期证据 → 人工审核 |
| 实际结果 Actual results | 你跑的命令、看到的输出、任何失败 |
| 检查点 Inspection | 实现、测试用例、结果在哪 |
| 局限 Limits | 测试身份 ≠ 生产认证；不写工单不发消息 |

预测放"预期行为"，观测放"实际结果"，**不要混**。

**过期证据记录 / Stale-evidence record**：12 条记录检查，10 条走了预期审核路由，**2 条过期记录被错误放行**。→ 只推荐**离线演示 (offline demonstration only)**，公开展示缺陷，不推荐试点。修复：在记录进入分类/起草**之前**检查资格和新鲜度 (eligibility and freshness)。摘要没给出两个失败输入和运行输出——**去要，不要猜**；拿到后并排展示实际 vs 预期路由，修复，重跑原用例 + 独立 holdout 集，检查后再报告。

**Northstar 验收门槛 / Acceptance gates（均未达成）**

| 门槛 Gate | 阈值 Threshold |
|---|---|
| 分诊质量 Triage quality | ≥ 22/24 标签与约定参考一致；**6/6 停机 (out-of-service) 案例全部标为紧急** |
| 副作用 Side effects | 评测中 **0 次工单写入、0 条客户消息** |
| 效率 Efficiency | 代表性试点端到端处理时间中位数 (median) **≤ 6 分钟** |

12 条离线用例不能证明采用或生产性能。上线建议还需：定义的用户、带分母的指标、故障处理、同意运营的团队。
课内测验：草稿幻灯片"Retrieval, agent, dashboard; 10/12 passed; ready for customer rollout"→ 应改为 **"10 of 12 records took the intended route; two stale records were wrongly admitted. I recommend an offline demonstration only."**（"10/12 通过"掩盖了失败模式——恰恰是新鲜度边界失效。）

**展示结构（五段式）/ Presentation**：Customer（运营做最终处置）→ Problem（要更快分诊，但漏掉紧急请求或过期记录会误导审核）→ Build（只读草稿 + 权限检查 + 固定标签 + 人工路由；新鲜度检查仍是提议）→ Proof（10/12，2 条过期被放行，要失败记录、修复、重跑）→ Handoff（提议服务运营负责标签与审核，客户工程负责访问、配置、遥测 (telemetry)、支持——双方**尚未同意**）。结论：仅离线演示；试点前需阻断过期证据、通过质量与副作用门槛、约定试点度量、两队接手。

**需求变化："能自动给客户发消息吗？" / Changing requirement**

先弄清真实需求：运营审核后的消息草稿 + 现有人工发送流程够不够？如果仍要应用发送 → 新增**外部动作 (external action)**，只读产物不变，动作路径**单独成阶段 (separate phase)**：

| 步骤 Step | 要点 Key control |
|---|---|
| 准备 Prepare | 从发送方可访问的数据构建确切收件人、消息、关联请求；缺失/过期 → 人工 |
| 审批 Approve | 授权人批准**这条确切动作**；收件人或内容变了需重新批准 |
| 发送时授权 Authorize at send time | 发送前一刻复查发送方权限、收件人、审批、请求当前状态 |
| 发送与对账 Send & reconcile | 稳定的**幂等键 (idempotency key)** + 接收方持久去重 (durable dedup)；记录回执 (receipt)；不确定结果先对账再重试——**超时 ≠ 没发出** |
| 安全失败 Fail safely | 授权/审批/投递/回执任一不确定 → 停止自动发送，转人工 |

"自动"现在意味着**人批准确切动作后才发送**——要说出来，面试官脑中可能是另一回事。

计划整体修订：
- 产物：保留只读切片；另行定义消息提议、审批记录、发送时授权、幂等发送、回执账本 (receipt ledger)、对账。
- 原门槛保留（22/24、6/6；只读流程仍 0 发送 0 写入）。
- 新动作门槛：带参考收件人/内容的消息测试集；报告 正确消息/合格消息、未授权发送/未授权尝试、审批与确切动作匹配/全部发送、重复效果/逻辑发送请求。先和 Northstar 约定阈值 (thresholds)。**任何未授权发送、未审批发送、重复、缺失效果记录都阻断动作路径**。
- 效果证据：应用记录与在发送边界**独立观测**的回执对比；采集器缺失或投递未知 = 证据不完整，不是"0 条"。
- 运营：提议服务运营当审批人，客户工程负责授权、发送集成、对账、支持；开启前确认。回退 (fallback)：检查失败或投递不确定时走人工流程。

**成本更新 / Cost estimate（情景假设，非 OpenAI 价格）**

```text
Assume: 80 eligible requests/day, $0.04 per draft, +$0.03 per send
Drafts only:     80 x $0.04          = $3.20 / day
Drafts + sends:  80 x ($0.04 + $0.03) = $5.60 / day
Increment:       $5.60 - $3.20        = $2.40 / day
(approval staffing, integration, retries, support are extra; if only some are approved, compute sends on that count)
```

每个控制保护不同的决定：已批准、有唯一幂等键的消息，如果发送前发送方权限被撤销，仍然是未授权发送；去重防重复，但不能让禁止的发送变合法。

<svg viewBox="0 0 820 260" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="260" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Northstar: read-only slice vs. separate message phase｜只读切片与独立消息阶段</text>
  <g font-size="12" text-anchor="middle">
    <rect x="10" y="45" width="800" height="80" rx="8" fill="#eef7f0" stroke="#2e8b57"/>
    <text x="70" y="62" font-weight="bold" fill="#2e8b57">Phase 1 (deliver)</text>
    <rect x="25" y="72" width="110" height="42" rx="6" fill="#fff" stroke="#555"/><text x="80" y="90">Entitlement</text><text x="80" y="106">权限检查</text>
    <rect x="150" y="72" width="120" height="42" rx="6" fill="#fff" stroke="#c33"/><text x="210" y="90">Freshness check</text><text x="210" y="106">新鲜度(提议)</text>
    <rect x="285" y="72" width="120" height="42" rx="6" fill="#fff" stroke="#555"/><text x="345" y="90">Classify label</text><text x="345" y="106">固定标签集</text>
    <rect x="420" y="72" width="120" height="42" rx="6" fill="#fff" stroke="#555"/><text x="480" y="90">Triage draft</text><text x="480" y="106">分诊草稿</text>
    <rect x="555" y="72" width="120" height="42" rx="6" fill="#fff" stroke="#555"/><text x="615" y="90">Operator decides</text><text x="615" y="106">运营决定</text>
    <rect x="690" y="72" width="110" height="42" rx="6" fill="#fff3f3" stroke="#c33"/><text x="745" y="90">Manual review</text><text x="745" y="106">人工审核</text>
    <rect x="10" y="150" width="800" height="90" rx="8" fill="#fff8ec" stroke="#d18a1a"/>
    <text x="85" y="167" font-weight="bold" fill="#d18a1a">Phase 2 (proposal only)</text>
    <rect x="25" y="178" width="100" height="48" rx="6" fill="#fff" stroke="#555"/><text x="75" y="198">Prepare</text><text x="75" y="214">准备</text>
    <rect x="135" y="178" width="110" height="48" rx="6" fill="#fff" stroke="#555"/><text x="190" y="198">Exact approval</text><text x="190" y="214">确切审批</text>
    <rect x="255" y="178" width="115" height="48" rx="6" fill="#fff" stroke="#555"/><text x="312" y="198">Send-time authz</text><text x="312" y="214">发送时授权</text>
    <rect x="380" y="178" width="115" height="48" rx="6" fill="#fff" stroke="#555"/><text x="437" y="198">Idempotent send</text><text x="437" y="214">幂等发送+去重</text>
    <rect x="505" y="178" width="120" height="48" rx="6" fill="#fff" stroke="#555"/><text x="565" y="198">Independent receipt</text><text x="565" y="214">独立回执</text>
    <rect x="635" y="178" width="85" height="48" rx="6" fill="#fff" stroke="#555"/><text x="677" y="198">Reconcile</text><text x="677" y="214">对账</text>
    <rect x="730" y="178" width="72" height="48" rx="6" fill="#fff3f3" stroke="#c33"/><text x="766" y="198">Manual</text><text x="766" y="214">兜底</text>
  </g>
  <g stroke="#555" stroke-width="1.3" fill="none">
    <path d="M135 93 L150 93"/><path d="M270 93 L285 93"/><path d="M405 93 L420 93"/><path d="M540 93 L555 93"/><path d="M675 93 L690 93"/>
    <path d="M125 202 L135 202"/><path d="M245 202 L255 202"/><path d="M370 202 L380 202"/><path d="M495 202 L505 202"/><path d="M625 202 L635 202"/><path d="M720 202 L730 202"/>
  </g>
</svg>

**面试怎么说 / How to say it in the interview**

- Q: "Present your Northstar recommendation. What's your delivery decision?"
  - EN: "Operators process service requests and keep the final disposition. They need faster triage, but a missed urgent request or a stale record can mislead their review. I built a read-only draft slice with entitlement checks, a fixed label set, and manual-review routing; the freshness check is still a proposal. The supplied record shows 10 of 12 took the intended route and two stale records were wrongly admitted, so I recommend an offline demonstration only. Before a pilot we need to block stale evidence, pass the quality and side-effect gates, and get service ops and customer engineering to accept ownership."
  - 中文：五段式 + 只推荐离线演示 + 试点前置条件。
- Q: "10/12 sounds close enough. Can you add automatic messages and keep the original commitment?"
  - EN: "Both misses admitted stale evidence, which is exactly the boundary that failed, so I don't have a repaired rerun yet. If a reviewed draft meets the need, operators keep sending manually. Otherwise I'd scope a separate action phase with exact-message approval, send-time authorization, idempotent sends with dedup, independent receipts, and manual fallback, keep the triage gates, and add action gates."
  - 中文：失败恰在关键边界；消息作为单独阶段并加门槛。
- Q: "What happens to your original commitment?"
  - EN: "I can still deliver the review-only demonstration on its original scope. The send path adds authorization, testing, operating work, and about $2.40 a day in model cost at 80 requests, so I'd estimate it separately and ask Northstar to agree to a revised plan. I wouldn't promise a date for the action path until those dependencies are understood."
  - 中文：原范围照交，新范围单独估算、重新约定。
- Q: "How do you know a retry won't send twice?"
  - EN: "Each logical send carries a stable idempotency key, and the receiver deduplicates durably. A timeout doesn't mean nothing was sent, so I reconcile against independent receipts before any retry, and if the outcome stays uncertain, the request goes to the manual process."
  - 中文：幂等键 + 持久去重 + 先对账再重试。

---

## 6. The LLM Systems Deep Dive｜LLM 系统深挖

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/the-llm-systems-deep-dive

**要点 / Key ideas**

- 典型开场问题："Show me exactly where the access check runs."——展示结束、深挖开始。技能是**按需深入 (depth on demand)**：先给决定，再按问题深度往下走。
- 六个追问领域 (six probe areas)：

| 领域 Area | 面试官会问 Typical probe |
|---|---|
| 智能体 Agents | 为何固定工作流 / 单 agent / 多 agent？每多一个 agent 的代价？ |
| 检索 Retrieval | 访问检查相对于排序 (ranking) 和模型调用在哪里运行？ |
| 评测 Evals | 分母是什么？哪些是观测 (observed)、哪些是预测 (predicted)？ |
| 延迟 Latency | 测的是哪个区间、哪些请求？ |
| 成本 Cost | 在声明的假设下每请求多少钱？漏算了什么？ |
| 故障处理 Failure handling | 检查失败、调用超时、证据缺失时怎么办？ |

- 开场示例："I recommend an offline-only, read-only triage draft that an operator reviews. The stale-evidence summary found two wrong admissions among 12 records, so the freshness check needs repair and verification before a pilot. The operating owners are proposed, not yet agreed."

**一个请求的完整流程 / Request flow（检查在模型之前）**

1. **认证 Authenticate**：应用从可信凭证 (trusted credentials) 确立运营身份，**绝不从模型生成的文本中获得身份**。
2. **资格检查 Check eligibility**：应用代码在任何受保护文本进入排序或生成**之前**检查权限 (entitlement)、适用性 (applicability)、新鲜度 (freshness)。拒绝、过期、或检查不确定 → 返回**同一个 "unavailable" 结果**，不带受保护文本（避免泄露"存在但无权"的信息）。
3. **检索 Retrieve**：只对合格段落排序；没有支撑请求的段落 → 人工审核。
4. **起草 Draft**：一次有界的模型调用 (one bounded model call)，在调用和资源预算内分类/起草。
5. **校验与路由 Validate & route**：应用检查拒绝非法标签、无支撑的声明、不完整结果、不确定性；运营审核可用草稿并保留处置权。不写工单、不发消息。

关键：**模型指令、符合 schema 的答案、相关引用 (citation) 都不能授予访问权**。引用帮助运营在访问被允许后核查，不能让越权读取变得可接受。

<svg viewBox="0 0 820 230" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="230" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Enforceable boundary before the model｜在模型之前设可强制的边界</text>
  <g font-size="12" text-anchor="middle">
    <rect x="10" y="50" width="110" height="56" rx="6" fill="#e8f0fe" stroke="#4a6fd1"/><text x="65" y="72">Authenticate</text><text x="65" y="90">可信凭证认证</text>
    <rect x="140" y="50" width="150" height="56" rx="6" fill="#fde8e8" stroke="#c33"/><text x="215" y="68">Entitlement +</text><text x="215" y="84">applicability + freshness</text><text x="215" y="100">权限/适用/新鲜度</text>
    <rect x="310" y="50" width="110" height="56" rx="6" fill="#fff" stroke="#555"/><text x="365" y="72">Retrieve/rank</text><text x="365" y="90">只排序合格段落</text>
    <rect x="440" y="50" width="110" height="56" rx="6" fill="#fff4e0" stroke="#d18a1a"/><text x="495" y="72">1 bounded call</text><text x="495" y="90">有界模型调用</text>
    <rect x="570" y="50" width="110" height="56" rx="6" fill="#fff" stroke="#555"/><text x="625" y="72">Validate</text><text x="625" y="90">标签/支撑校验</text>
    <rect x="700" y="50" width="110" height="56" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="755" y="72">Operator review</text><text x="755" y="90">运营审核决定</text>
    <rect x="140" y="150" width="150" height="50" rx="6" fill="#fff3f3" stroke="#c33"/><text x="215" y="170">"unavailable"</text><text x="215" y="188">无受保护文本</text>
    <rect x="440" y="150" width="240" height="50" rx="6" fill="#fff3f3" stroke="#c33"/><text x="560" y="170">Manual review 人工审核</text><text x="560" y="188">no support / invalid / uncertain</text>
  </g>
  <g stroke="#555" stroke-width="1.4" fill="none">
    <path d="M120 78 L140 78"/><path d="M290 78 L310 78"/><path d="M420 78 L440 78"/><path d="M550 78 L570 78"/><path d="M680 78 L700 78"/>
    <path d="M215 106 L215 150" stroke="#c33" stroke-dasharray="4 3"/><path d="M365 106 L500 150" stroke="#c33" stroke-dasharray="4 3"/><path d="M625 106 L620 150" stroke="#c33" stroke-dasharray="4 3"/>
  </g>
  <text x="365" y="130" font-size="11" fill="#c33" text-anchor="middle">deny / stale / uncertain → same result</text>
</svg>

**R-18 检索报告 / R-18 retrieval report（离线，40 个测试用例）**

| 类别 Category | 数量 Count | 结果 Result |
|---|---|---|
| 有权且新鲜 Authorized & fresh | 30 | 27 有支撑草稿，3 无支撑 |
| 过期 Stale | 6 | 6/6 全部被拦截 |
| 越权 Unauthorized | 4 | **1 段越权文本到达了模型** |

- 课内测验答案：**切断检索路径与受保护数据的连接，维持仅离线推荐，用不含客户数据的测试输入继续调查**。不能"加一个最终答案过滤器"（文本已进入模型输入），不能"加一个专家 agent 审查"（只是多一个接收者）。
- 27/30 衡量的是合格用例上的任务质量，**既不包含也不抵消**越权暴露；6/6 过期拦截也不修复另一份 12 条摘要里的 2 次错误放行。
- **第一个失败点 (first failure)**：trace 显示可信身份 → 检索适配器 (retrieval adapter) 在权限检查**之前**把受保护文本发给模型。适配器→模型的交接是第一个破裂的边界。

**响应顺序 / Response order**

| 步骤 Step | 动作 Action |
|---|---|
| 隔离 Quarantine | 切断故障适配器与受保护数据；只用无客户数据的测试输入继续 |
| 复现 Reproduce | 拿到原始越权用例和 trace，重现条件，找到越界的确切调用和输入 |
| 修复 Repair | 把权限判断移到检索前的可信检查，与适用性、新鲜度检查放一起；拒绝或检查无法完成 → "unavailable" |
| 检查 Inspect | 重跑原用例 + 独立 holdout 集；检查**可信访问记录和实际模型输入**，而不只是显示的答案 |

无法证明什么进入了模型 → 证据不完整，路径保持关闭。**永远不要让模型决定一条记录能不能读**。

**分开的分母 / Separate denominators（课内配对答案）**

| 证据问题 Evidence question | 分母/状态 Denominator or status |
|---|---|
| 越权段落多频繁到达模型？ | 越权读取尝试数 (attempted unauthorized reads)，在访问边界和模型输入两处检查 |
| 能出草稿的用例中多少有支撑？ | 合格用例数，**含 3 个无支撑的** |
| 过期用例中多少被拦截？ | 测试的过期用例数 |
| 访问/效果证据缺失的修复检查怎么报？ | 记为**证据不完整 (incomplete)，不是安全** |

一个综合通过率会把访问失败埋在成功草稿下面。工单写入和客户消息要在执行边界独立核查。holdout 的意义：只针对可见失败调的修复可能漏掉另一条越界路径。即使干净重跑也只支持"测试"层面的结论；采用、生产性能、运营归属各需自己的证据。

**取舍 / Trade-offs**

- 首版是一个窄任务、小读取面、人做最终决定 → **固定的、应用定义的序列 (fixed, application-defined sequence)**：身份检查、预算、校验、人工回退都易于查找和检查，客户工程要支持的东西也少。
- **直接调用 Responses API**：适合应用自己掌控循环、工具分发 (tool dispatch)、状态。**Agents SDK** 对 OpenAI 模型默认用 Responses API，并加一个运行时管理轮次 (turns)、工具执行、护栏 (guardrails)、交接 (handoffs)、会话 (sessions)。两种选择下，**业务授权都留在应用里**。
- 多个协作 agent 是**另一种架构，不是升级**：经理 + 专家 agent 可能改善困难的分类/证据审查，但增加上下文传递、协调、延迟、成本和支持工作。

**成本与延迟 / Cost & latency**

```text
Same workload: 100 eligible requests (scenario forecasts, exclude operator/support time)
Fixed workflow:       100 x $0.018 = $1.80
Coordinated agents:   100 x $0.029 = $2.90
Increment:                          $1.10 per 100 requests
```

- 公平比较要说明各自包含哪些调用、重试、工具，用同一工作负载和同样的安全边界。
- **端到端 p95 (end-to-end p95)**：指定请求集合上耗时的第 95 百分位 (percentile)，有明确起止点；说明是否包含检索、模型调用、校验、重试、工具；运营审核时间单独测（除非终点是完成审核）。两种架构都还**没有实测 p95**；6 分钟中位处理时间门槛是另一个指标。
- 何时多 agent 值得复杂度：在同一代表性负载上做受控比较，显示有支撑草稿或紧急用例处理上有**事先约定的"实质性"提升**，且满足同样的授权、安全、延迟、成本、运营约束。质量提升不能弥补越权暴露；成本更低也不让固定路径自动可接受。

**面试怎么说 / How to say it in the interview**

- Q: "27 of 30 supported drafts. Is Northstar ready for a pilot?"
  - EN: "No. In R-18, one unauthorized passage reached the model out of four attempted unauthorized reads. I'd cut the retrieval adapter off from protected data and continue offline with test inputs. The 27 of 30 figure is task quality on eligible cases — it says nothing about authorization."
  - 中文：质量指标不能抵消越权；先隔离。
- Q: "Where would you repair it, and how would you know it worked?"
  - EN: "The trace shows the adapter returned protected text before entitlement was checked. I'd enforce entitlement, applicability, and freshness before retrieval and return 'unavailable' on denial or uncertainty. Then I'd rerun that case plus a held-out set and inspect the access records and the actual model inputs. That's the repair I'm proposing; I haven't seen it pass yet."
  - 中文：修复位置 + 验证方式 + 明确是"提议"。
- Q: "Why not add a final-answer filter or a reviewer agent?"
  - EN: "Both act after the protected text already reached the model input. A filter hides the symptom; another agent just adds another recipient. The fix has to be an enforceable check in application code before retrieval."
  - 中文：事后过滤/多 agent 都晚了。
- Q: "Why not specialist agents? What do 100 requests cost?"
  - EN: "I'd start with the fixed sequence because the task is narrow and the operator makes the final call. Under the given assumptions it's $1.80 per 100 requests versus $2.90 for coordinated agents, so $1.10 more. I'd test specialists on the same workload and boundaries if they promised a material gain in quality or urgent-case handling. Neither path has a measured p95 yet."
  - 中文：窄任务用固定流程；给出成本差；多 agent 需同条件对比。
- Q: "How do you define latency here?"
  - EN: "End-to-end p95 over a named request set, with a stated start and finish, and I'd say whether it includes retrieval, model calls, validation, retries, and tools. Operator review time I'd measure separately, and I'd keep it distinct from the six-minute median handling-time gate."
  - 中文：p95 要定义区间与范围。
- Q: "Who runs it after handoff?"
  - EN: "I'd propose service operations for labels and operator review, and customer engineering for access, configuration, telemetry, and support. Neither has agreed yet, so I'd confirm that before a pilot."
  - 中文：提议 ≠ 已同意。

---

## 7. The Hiring Manager Conversation｜招聘经理对话

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/the-hiring-manager-conversation

**要点 / Key ideas**

- 官方指南没有单列 HM 轮，但 HM 可能很早出现（初步通话可能就是 HM）。HM 问**人多于代码**：谁要什么？你个人承诺了什么？你退出后工作怎样了？
- HM 会探查三件事：

| 维度 Dimension | 含义 Meaning |
|---|---|
| 归属 Ownership | 你个人决定和交付了什么，交给了谁 |
| 客户判断 Customer judgment | 如何权衡客户要求与证据支持的东西 |
| 模糊中交付 Delivery under ambiguity | 需求、证据、优先级不清时如何推进 |

- 岗位描述还提到：排序工作 (sequencing)、清除阻碍 (removing blockers)、权衡范围/速度/质量、跟进 (follow-through)。HM 答案在技术边界之外加上**人的决定**：谁受影响、证据冲突时你决定了什么、别人贡献了什么、你如何回应他们的顾虑、哪个承诺变了、谁接手。

**服务路由案例延伸 / Service-routing extension**

- 新增第三份复盘：8 个试点草稿中 **3 个没有记录路由理由 (routing rationale)**。这衡量的是**文档完整性 (documentation completeness)**，不是路由准确率，也不能识别试点中那 3 个错误路由。
- 运营主管要求**周五前上线自动派单 (automatic dispatch)**以减轻审核负担。课内测验答案：**拒绝周五承诺；若审核员能应对该缺口则继续已接受的审核试点，并提议理由记录改动 + 验证计划。** 错误选项：17/20 足够就扩大；完全暂停试点；把 3 个缺理由当成 3 个路由错误。
- 理由：继续审核已有同意的负责人；自动派单改变了谁做路由决定 → 需要自己的控制、代表性测试、同意运营的负责人。

**决策对话要点 / The decision conversation**

1. 承认负担（"你的团队还在承担审核每个请求的成本"）；
2. 说清证据含义（3/8 缺理由 = 记录不完整，不代表路由对错）；
3. 明确拒绝（"基于这些证据我不能承诺周五自动派单"）；
4. 给替代方案（继续审核试点；我提议理由记录改动和验证计划；请指派一人记录模糊路由示例）；
5. **书面确认范围**（对主管和自己的经理："不承诺周五派单；约定范围是继续人工审核；我负责提议理由改动和验证计划；请确认修订范围和下次扩展决策时间"）。

区分：主管同意继续试点和指派审核员 = **真实承诺**；改动和验证计划 = **待定**；请求确认 ≠ 所有人已同意。审核员应付不了缺口 → 暂停受影响工作并升级 (escalate)。

<svg viewBox="0 0 820 220" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="220" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Friday dispatch request: commitments vs proposals｜承诺 vs 提议</text>
  <g font-size="12" text-anchor="middle">
    <rect x="20" y="50" width="170" height="56" rx="6" fill="#e8f0fe" stroke="#4a6fd1"/><text x="105" y="72">Ops lead asks:</text><text x="105" y="90">auto-dispatch by Friday</text>
    <rect x="230" y="50" width="160" height="56" rx="6" fill="#fde8e8" stroke="#c33"/><text x="310" y="72">Declined</text><text x="310" y="90">拒绝周五承诺</text>
    <rect x="430" y="40" width="170" height="40" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="515" y="58">Agreed: reviewed pilot</text><text x="515" y="73">已同意：继续人工审核</text>
    <rect x="430" y="90" width="170" height="40" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="515" y="108">Agreed: ambiguity reviewer</text><text x="515" y="123">已同意：指派审核员</text>
    <rect x="630" y="40" width="175" height="40" rx="6" fill="#fff4e0" stroke="#d18a1a"/><text x="717" y="58">Pending: rationale change</text><text x="717" y="73">待定：理由记录改动</text>
    <rect x="630" y="90" width="175" height="40" rx="6" fill="#fff4e0" stroke="#d18a1a"/><text x="717" y="108">Pending: verification plan</text><text x="717" y="123">待定：验证计划</text>
    <rect x="230" y="155" width="575" height="44" rx="6" fill="#f5f5f5" stroke="#888"/><text x="517" y="173">Auto-dispatch only after: action controls + representative tests + operating owner + explicit decision</text><text x="517" y="190">自动派单前提：动作控制 + 代表性测试 + 运营负责人 + 明确决策</text>
  </g>
  <g stroke="#555" stroke-width="1.4" fill="none"><path d="M190 78 L230 78"/><path d="M390 70 L430 60"/><path d="M390 86 L430 110"/><path d="M600 60 L630 60"/><path d="M600 110 L630 110"/></g>
</svg>

**何时改变决定 / When the decision should change**

| 条件 Condition | 动作 Action |
|---|---|
| 现有负责人接受审核流程、审核员能应对缺口 | 继续审核试点 (continue) |
| 审核员无法可靠应对缺口，或约定审核不再覆盖 | 暂停受影响工作，带证据、后果、所需决定、跟进人升级 (pause & escalate) |
| 动作控制、代表性测试、运营负责人、明确决策都已约定 | 才考虑自动派单（仅完成理由修复不够） |

课内测验："我定义了路由标签并亲自做了分类器和审核界面"→ 错，**工程师做分类器和界面，运营定义标签**。修复弱答案要逐条替换为正确贡献、证据局限或未知结果，只加一句"团队也帮了忙"不够。

**面试怎么说 / How to say it in the interview**

- Q: "Tell me about a time you delivered under ambiguity and disagreed with a customer."
  - EN: "The customer was an operations team routing incoming requests; they wanted less manual review, but the pilot still had gaps in what was recorded about routing decisions. I built a classifier that drafted routes and a screen that required human review, and operations defined the labels. A pilot review found 17 of 20 correct; a separate review found three of eight drafts had no recorded rationale — a documentation gap, not a count of routing errors. When the lead asked for automatic dispatch by Friday, I acknowledged the review burden, declined to promise it, and asked the lead and my manager to confirm a revised scope. The lead kept the human-reviewed pilot and named a reviewer; I took on proposing the rationale change and a verification plan, which isn't finished yet."
  - 中文：五段式 + 分歧 + 改变的承诺 + 未完成的诚实交代。
- Q: "If you escalated, did your manager take over delivery?"
  - EN: "No. I told my manager and the customer I wouldn't promise Friday dispatch, explained the evidence, and asked them to confirm the revised scope and a next decision point. I stayed responsible for the rationale proposal and its verification plan."
  - 中文：升级 ≠ 甩锅，我仍然负责。
- Q: "What did you actually own, and what did operations do?"
  - EN: "I built the classifier and the review screen, and I made the call not to promise automatic dispatch. Operations defined the labels; the lead accepted continued pilot review and named a reviewer for ambiguous examples. I own proposing the rationale work — I can't say it's done."
  - 中文：清楚划分贡献。
- Q: "Was the customer wrong to ask?"
  - EN: "No. Manual review really does cost them time. The deadline was a separate question — the evidence and operating setup didn't justify promising automatic dispatch yet, so I offered a path to a later decision and kept the review process they'd already agreed to."
  - 中文：客户不是对手；需求合理，时间承诺不合理。
- Q: "What would change your decision?"
  - EN: "Agreed action controls, testing on representative requests that covers the rationale gap as well as routing accuracy and dispatch behavior, an operating owner, and an explicit decision to expand."
  - 中文：说出可检验的条件。

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 35 篇）。

  - 中文：客户 = 内部合作团队；对方顾虑合理 → 复用 + 清晰分工 → 说明代价 → 反思。
- Q: "What did you actually own, and what did they do?"
  - 中文：清楚划分贡献。

---

## 8. The Final Interviews and Mission Questions｜终面与使命问题

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/the-final-interviews-and-mission-questions

**要点 / Key ideas**

- 终面：示例流程最后一步；**默认线上 (virtual)，可选旧金山现场 (onsite in San Francisco)**；4–6 小时、4–6 人、1–2 天；聚焦专长领域，**设计成把你推出舒适区 (stretch you beyond your comfort zone)**。工程面试看设计良好的方案、高质量代码、最优性能、测试覆盖；沟通协作贯穿。决定约 1 周，可能要推荐人。
- **没有保证的单独使命轮**——使命、价值观、安全可能在任何一轮出现。
- 新事实改变了推荐就直说，并说出哪条边界动了；不必为当初没有该证据时做的决定辩护。

**OpenAI 使命与章程 / Mission & Charter**

使命：确保通用人工智能 (AGI) 造福全人类 (benefits all of humanity)。章程 (Charter) 四项承诺：

| 承诺 Commitment | 含义 Meaning | 部署时可用的问题 Question to apply |
|---|---|---|
| 广泛分配的收益 Broadly distributed benefits | 避免伤害人类或过度集中权力的用途 | 谁承担风险？谁保有控制？ |
| 长期安全 Long-term safety | 做让 AGI 安全所需的研究并推动采用 | 边界是否可强制、可验证？ |
| 技术领导力 Technical leadership | 应对 AGI 社会影响需要先进技术能力，仅靠政策和倡导不够 | 技术上能否真正做到？ |
| 合作导向 Cooperative orientation | 与研究和政策机构合作，提供公共产品 | 是否与正确的审查方合作？ |

- 背诵使命回答的是"OpenAI 说了什么"；**你的动机**回答"为什么对你重要"。好答案把你真实持有的关切连接到一个决定、受影响的人、你拥有的证据。保持比例：小试点不能证明造福人类。不必同意 OpenAI 的每个取舍，也别假装已有答案。

**安全发现到来时 / When a safety finding arrives**

- 新发现：**12 次访问测试（用测试身份）中 2 次**，审核界面把受限的运营备注 (restricted operator note) 显示给了无权身份。
- 课内测验答案：**暂停受影响的界面路径，保留人工路由，要求调查**。错误：因主管之前接受而继续；宣称生产泄露并宣布上线完成；因 17/20 正确而继续。
- 该发现说明访问边界在测试中失败，**不说明真实生产数据被暴露**，也不说明生产频率。修复必须在受限备注到达界面**之前**强制授权——事后审核路由无法撤销已发生的显示。
- 之前的交接发生在发现之前；主管对试点审核的接受**不能替代**修复验证后由正确负责人做的新决定。
- **安全上的诚实 (honesty about safety)** = 说清证据显示什么和不显示什么；说出安全选择的代价（暂停 = 运营回到人工）；说清谁还需要决定。

**重新开放需要什么 / What reopening needs（课内图）**：访问修复 (access repair) → 原用例重跑 (original-case rerun) → holdout 测试 (held-out tests) + 访问记录 (access records) + 决策负责人 (decision owner) → 重开决定 (reopen decision)。任一缺失都不能重开。holdout 防止修复只针对已知失败调参；通过它也不建立生产失败率，也不会自动重开。

<svg viewBox="0 0 820 230" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="230" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Access finding → contain → verify → reopen｜访问发现后的处理</text>
  <g font-size="12" text-anchor="middle">
    <rect x="10" y="50" width="140" height="56" rx="6" fill="#fde8e8" stroke="#c33"/><text x="80" y="70">2/12 access tests</text><text x="80" y="86">show restricted note</text><text x="80" y="101">测试中越权显示</text>
    <rect x="175" y="50" width="140" height="56" rx="6" fill="#fff3f3" stroke="#c33"/><text x="245" y="72">Pause screen path</text><text x="245" y="90">暂停 + 人工路由</text>
    <rect x="340" y="50" width="140" height="56" rx="6" fill="#fff" stroke="#555"/><text x="410" y="72">Notify owner +</text><text x="410" y="90">security review 安全审查</text>
    <rect x="505" y="50" width="140" height="56" rx="6" fill="#fff" stroke="#555"/><text x="575" y="72">Repair in app code</text><text x="575" y="90">应用内强制授权</text>
    <rect x="505" y="140" width="140" height="56" rx="6" fill="#fff" stroke="#555"/><text x="575" y="160">Rerun originals +</text><text x="575" y="176">held-out + access logs</text><text x="575" y="191">独立验证</text>
    <rect x="670" y="140" width="140" height="56" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="740" y="162">Decision owner</text><text x="740" y="180">explicit reopen 明确重开</text>
    <rect x="175" y="140" width="290" height="56" rx="6" fill="#f5f5f5" stroke="#888"/><text x="320" y="162">Unknown: prod exposure? root cause?</text><text x="320" y="180">未知：是否生产暴露？根因？→ 不夸大</text>
  </g>
  <g stroke="#555" stroke-width="1.4" fill="none"><path d="M150 78 L175 78"/><path d="M315 78 L340 78"/><path d="M480 78 L505 78"/><path d="M575 106 L575 140"/><path d="M645 168 L670 168"/></g>
</svg>

**政策与应用规则 / Policy vs application rules**

| 来源 Source | 作用 Purpose | 不是什么 What it is NOT |
|---|---|---|
| 章程 Charter | 目的与承诺 | 不授予任何部署许可 |
| 模型规范 Model Spec | 清晰、双方理解的自主范围 (scope of autonomy)：允许哪些子目标、可接受哪些副作用、何时必须停下求澄清或审批 | — |
| 使用政策 Usage policies | 禁止在敏感领域**无人工审核**地自动化高风险动作 | 加了审核不代表所有部署都被允许 |
| 客户授权规则 + 法律/职业义务 Customer authorization rules, legal duties | 需要单独分析 | — |

访问发现足以**立即隔离**受影响路径，即使还没决定某项政策/法律义务是否适用。别因为安全判断明确就说政策分析做完了。

**跨面试官一致 / Consistency across interviewers**：面向使命的答案以人和动机开头；技术答案定位边界和验证计划。两者都要认可运营的贡献、保留每个分母、把之前已接受的交接与新请求分开。

**面试怎么说 / How to say it in the interview**

- Q: "Why does OpenAI's mission matter to you? And 2 of 12 access tests showed a restricted note to an unauthorized test identity — what would you do?"
  - EN: "I care about people keeping control over information about their work, and broad benefit, to me, means paying attention to who carries a deployment's risk, including people who never chose the tool. I wouldn't claim a small pilot proved broad benefit. This finding changes my recommendation: I'd pause the affected screen path and use the existing manual process. The tests show a real boundary failure, but I don't know whether production data was exposed or what caused it. I'd notify the customer's operating owner, ask for a security review, propose an access repair in application code with independent retesting on a held-out set, and ask for a named owner to decide when to reopen."
  - 中文：动机 → 改变决定 → 区分测试失败与生产泄露 → 修复与负责人。
- Q: "The customer says the review burden is unacceptable and wants to keep the screen running."
  - EN: "I understand the burden, and I'd help the team through the manual process while we investigate. But I'd decline to keep the affected path running — the customer wanting it doesn't make an unauthorized display safe. I'd ask the operating owner and security reviewers to decide who investigates and how we verify the repair."
  - 中文：共情 + 坚持安全底线 + 交给正确决策者。
- Q: "What if you disagree with a proposed response?"
  - EN: "I'd lay out the evidence and the trade-off plainly, listen for anything I'm missing, and ask the decision owner and security reviewers to settle it. My concern doesn't make me the authority on every policy or legal question."
  - 中文：表达但不越权。
- Q (technical version): "Where is the boundary, and what happens next?"
  - EN: "The screen is where the boundary failed: in two test cases an unauthorized identity could see a restricted note. I don't know yet whether the defect is in identity handling, entitlement checks, or elsewhere. I'd pause the path, ask security to inspect the checks that run before notes reach the screen, enforce the boundary in application code, reproduce the failing cases, and test the repair independently on a held-out set. If access records are missing or ambiguous, the path stays paused."
  - 中文：技术版强调边界位置与验证，事实与使命版一致。
- Q: "What would change your decision?"
  - EN: "The failure reproduced and the boundary repaired, independently checked results on the original cases and a held-out set, and an explicit decision to reopen from the customer and the right security or policy reviewers, with an operating owner who has agreed to run it."
  - 中文：重开条件全部可检验。

---

## Case A｜案例 A：Meridian Telecom 客服智能体 (Support Agents)

## 9. The Take-Home Brief｜带回家案例的客户简报

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/the-take-home-brief

**要点 / Key ideas**

- take-home 通常是一页短简报：公司、工作流、诉求、几个数字。**第一件事不是设计**，而是像客户自己的工程师那样读简报——区分客户**知道的**和**希望的**。

**Problem statement (EN)**

> Meridian Telecom receives 12,000 support contacts a month (7,200 phone, 4,800 chat), all handled by people; no agent system exists. The support leader wants an agent system that automates 70% of contacts and reduces handling time. Median handling time is 8 minutes across both channels. Categories: billing questions, service interruptions, plan changes, account access (proportions unknown). A review of 30 closed contacts found 8 recorded as resolved; 3 of those 8 had another contact from the same customer within 7 days.

当前人工工作流（五步）：客户通过电话/聊天联系 → 客服 (representative) 在**账户控制台 (account console)** 查账户 → 在**政策知识库 (policy knowledge base)** 查政策 → 处理或转专员 (specialist) → 在**工单系统 (ticket system)** 记录处置 (disposition)。
三套系统说明了客服在哪工作，**不说明自动化系统被允许读写什么**——这是第一批要问的问题。
8 分钟中位处理时间 (median handling time) 只说明典型耗时，**不说明问题是否解决**。

**简报三分法 / Sort the brief：Facts / Asks / Gaps**

| 类别 Bucket | Meridian 内容 Content |
|---|---|
| 事实 Facts | 12,000/月、7,200 电话 + 4,800 聊天、8 分钟中位数、五步工作流 |
| 诉求 Asks | 70% 自动化、缩短处理时间 |
| 缺口 Gaps | 类别量、结果质量、系统访问、谁来运营 |

把缺口当事实建计划的候选人，第一个追问就会被抓住。

**"自动化 70%" 的三种含义 / What "automated" means**

| 定义 Definition | 含义 Meaning | 问题 Caveat |
|---|---|---|
| 分流 Deflected | 客户没接触到客服 | 工作量降了，但不说明客户被帮到 |
| 已回复 Answered | 系统给了回复 | 可能错误、不完整、或客户再次联系 |
| 已解决 Resolved | 问题修好且持续 | Meridian 尚未定义 |

每种定义下 70% 是不同的目标、不同的分母。要变成成功标准需要四个答案：自动化的定义、**合格联系 (eligible contacts)** 范围、该定义下的当前基线 (baseline)、可接受的失败。在此之前 70% 只是**发现阶段的方向**，不是上线门槛。

**30 条复盘解读（课内测验）**：唯一被支持的说法——**"3 条标为已解决的联系之后又有联系；原因和总体比例未知。"** 不能说 resolved 标签证明持久解决；不能说 3 条原问题被证明未解决（不知道后续联系是否同一问题）；更不能说 70% 可自动化。
错误句子 "The resolved status proves the system can automate 70% of support and eliminate repeat contacts" 三处错：没有 agent 系统可测；8 分钟中位数测的是处理时间；8 个已解决中 3 个回头。

**约束清单 ≠ 权限清单 / Inventory is not a permission list**：客服核验 (verify)身份后能在控制台改套餐，不代表控制台有 API，也不代表服务账号 (service account) 能做同样的修改。

**发现阶段要问的问题 / Discovery questions**

| 主题 Topic | 问题 Question |
|---|---|
| 接口 Interfaces | 服务能否通过受支持的 API 读账户、取政策、建/改工单？API 是否集成就绪？ |
| 数据权限 Data permissions | 服务能访问哪些客户数据、以什么身份、为何目的？适用哪些数据处理协议 (data processing agreements)？ |
| 身份 Identity | 客服如何核验来电者？系统读账户前 Meridian 要求什么核验？ |
| 动作 Actions | 自动化可执行哪些账户/套餐变更？谁批准有后果的变更？ |
| 客户需求 Customer needs | 客户和客服希望 agent 处理哪些请求？何时该人介入？ |
| 政策与升级 Policy & escalation | 谁解释不清晰的政策？未解决请求如何到达正确专员？ |

今天的人工流程描述现状，**不代表客服已同意当未来 agent 的兜底 (fallback)**。

**参与简报 / Engagement brief（一页）**：客户与工作流 | 诉求与基线（70% 无定义、8 分钟不衡量解决）| 联系复盘 | 系统（存在但接口、权限、身份、变更权限未确认）| **拟交付物 (proposed outputs)**：基于发现的范围、样本数据上的可复现 demo、定义结果衡量方式的评测计划 (evaluation plan)、涵盖交接需求的展示 | **排除项与未决 (exclusions & open decisions)**：demo 不用真实客户数据、不写任何生产系统；首版、成功定义、集成访问、身份核验、数据处理、政策解释、升级、支持归属都未决；**不承诺上线日期或自动化百分比**。

要咨询的人（不替任何人分配未同意的工作）：支持运营 (support operations)——流程、客户需求、政策解释、升级、结果记录；客户工程 (customer engineering)——接口、身份、数据权限、集成就绪、日常运营；自己的交付团队——发现、界定、demo、评测计划、交接材料。

**面试怎么说 / How to say it in the interview**

- Q: "Walk me through the Meridian engagement. Why isn't 70% already your launch criterion, and who will run the system?"
  - EN: "Meridian gets 12,000 contacts a month, 7,200 by phone and 4,800 by chat, and representatives check accounts and policy, handle or route requests, and record dispositions. The support leader wants 70% automation and shorter handling time, but before 70% can be a criterion we need a definition of automation, an eligible population, a baseline, and agreed acceptable outcomes. I'd propose discovery, a reproducible demo on sample data, an evaluation plan, and a presentation that covers handoff. Nobody at Meridian has agreed to run or approve the system yet, so my recommendation is discovery, not a launch promise."
  - 中文：70% 需先定义；推荐发现阶段而非上线承诺。
- Q: "The support leader says a resolved ticket proves the problem is over. What would you ask?"
  - EN: "I'd ask how representatives assign that disposition and whether the three later contacts were about the same issue, then ask for a representative sample of outcomes across eligible contacts. The 30-contact review is a reason to investigate, not an estimate of Meridian's resolution rate."
  - 中文："已解决"标签需核实；小样本只是调查理由。
- Q: "Isn't deflection the same as automation?"
  - EN: "Not for the customer. Deflection means they never reached a person; it doesn't tell us they got help. I'd want to measure resolution — fixed and staying fixed — with a defined window and denominator."
  - 中文：分流 ≠ 解决。

---

## 10. Scoping the First Release｜界定首个版本

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/scoping-the-first-release

**要点 / Key ideas**

- 诱人答案：选数据里最大的类别。在 Meridian 这会把账户访问和套餐变更排在所需权限之前。好的首版同时需要三样：**值得做的任务 (task worth doing)、可强制的边界 (enforceable boundary)、准备好运营的人 (people ready to run it)**。
- 改变计划的发现问题：身份（没有被接受的核验方法 (verification method) → 一切账户相关自动化被阻断）；政策（谁批准冲突时的官方答案）；接口与权限（客服用的控制台 ≠ 服务有权访问）；运营（谁审草稿、接升级、处理故障）；客户代价（错误的一般解释、给 A 看 B 的账单、未授权改套餐——各需不同边界）。

**发现结果 / Discovery findings**：60 条联系复盘 = 28 条账户相关账单 (account-specific billing) + 20 条一般账单指导 (general billing guidance) + 12 条套餐变更 (plan change)。**Meridian 刻意挑选**以展示差异，所以计数**不是总体估计**。20 条一般指导中 **4 条依赖审核员无法调和的冲突指导**。自动身份核验和实时集成访问仍未确认；客服能审草稿，但 Meridian 未承诺人手或兜底。

**候选比较 / Candidate comparison**（首版范围 first-release scope = 初始部署的用户、任务、渠道、允许的效果）

| 候选 Candidate | 价值 Value | 阻断 Blocker | 决定 Decision |
|---|---|---|---|
| 账户相关账单 Account-specific billing (28) | 有用（解释某张账单） | 需已验证身份 + 授权账户访问，都不存在 | 推迟 (defer) |
| 套餐变更 Plan changes (12) | 有用 | 身份 + 访问之上再加有后果的动作 | 推迟 |
| 一般账单指导 General billing guidance (20) | 可从一般政策回答，不读账户不改套餐 | 4 条冲突 → 需批准的源材料 + 转人工路径 | **有条件推荐 (conditional)** |

加权打分（课内示例，权重 价值3/可行4/低风险5/就绪4）：账户账单 59、**一般指导 96**、套餐变更 47。即使账户账单总分赢了，**总分也无法创造身份核验或账户访问**——它们是前提条件 (prerequisites)，不是可交换的分数；批准的指导和兜底同理。

**推荐**：一般账单指导问题的**聊天草稿，由客服审核后才到客户**。仅当 Meridian 接受范围、提供批准的指导、承诺人手时成立。

**成功定义 / Success definition（运行前约定）**：40 条合格聊天试点 vs **独立观测**的 40 条同工作流同渠道的人工对照 (control group)。

| 指标 Measure | 定义与分母 Definition & denominator |
|---|---|
| 资格 Eligibility | 每组：筛查数、判定合格数、排除数及原因；**全部筛查数作分母** |
| 草稿质量 Draft quality | 每份草稿对照批准指导标为 有支撑/无支撑/无法分类；记录客服的实质修改；目标：**从不发送无支撑答案**；修改不把无支撑草稿从计数中移除 |
| 升级 Escalation | 漏升级 / 需要升级的联系数；不必要升级 / 全部审查过的升级 |
| 处理时间 Handling time | 两组中位数 + 可用计时数 + 计时定义（同一起止事件）；**监测而非承诺降低** |
| 同问题重复联系 Same-issue repeats | 7 天内：确认重复 / 确认非重复 / 未知，分母为组内全部联系；**缺失关联算未知，不算"无重复"** |

8 分钟基线 (baseline)覆盖两渠道全部类型，不能作对照。两组难度/人手可能不同，差异不证明因果 (causation)。系统拒答就记录并转人，**不要硬凑 40 份草稿**。资格规则、升级规则、7 天窗口、继续/停止决策人都在试点前约定。

**为什么"拦截率"误导 / Why containment misleads**：报告"10/10 已回答"，其中 2 人 7 天内同问题回头、1 个应升级的请求未到人（不知是否与回头重叠）。课内测验答案：**分别报告 2 个重复和 1 个漏升级；调查其余结果，用定义好的分母衡量草稿质量和升级**。不能简单 10−2−1=7（可能重叠）。这也是 70% 不能作首版门槛的原因：拦截率可上升而客户得到差答案、回头、或找不到人。

**范围外 / Out of scope**：账户相关答案和任何账户数据访问、套餐及其他账户变更、对账户/工单的自动写入、未经客服发出的回复、电话/语音。

**Meridian 必须接受的角色 / What Meridian must accept**

| 角色 Role | 职责 Responsibility | 确认方式 Proof |
|---|---|---|
| 支持运营 Support operations | 客服人手、人工升级与兜底、结果定义、继续/停止决策 | 试点前确认人员可用 + 书面兜底 |
| 政策负责人 Policy owner | 批准一般指导、解决冲突、保持更新 | 草稿使用前确认批准的指导及负责人 |
| 客户工程 Customer engineering | 访问边界、系统支持、变更控制 | 确认负责人同意；不假设实时集成访问 |
| 度量负责人 Measurement owner | 收集筛查、计时、升级、7 天结果，尽可能关联联系 | 确认数据访问与未知如何记录 |

都未同意。缺任何一项 → 继续样本数据 demo 和发现，这仍是有用的进展。
课内测验：记录说"复盘证明账户账单是最大类别、自动化它收益最大"→ 错，**刻意挑选的样本既不说明类别规模也不说明改善**。

**面试怎么说 / How to say it in the interview**

- Q: "Why choose general guidance when the review has 28 account-specific billing contacts?"
  - EN: "The review was picked on purpose, so it can't tell us which category is biggest. Account billing could be valuable, but automated identity verification and account access aren't confirmed. I recommend representative-reviewed chat drafts for general guidance, which can draw on approved policy without reading or writing any account. Four of the 20 general cases had conflicting guidance, so unclear questions must go to a person, and I wouldn't start until Meridian approves the guidance and commits staffing, fallback, measurement, and owners."
  - 中文：刻意样本不代表规模；权限缺失是前提不是分数。
- Q: "What would your evidence show?"
  - EN: "I'd compare 40 eligible pilot chats with 40 separately observed manual chats in the same workflow. I'd review every draft, check missed and unneeded escalations, compare handling-time medians measured the same way, and classify seven-day same-issue repeats, including unknowns. The groups aren't matched, so a difference alone wouldn't prove the pilot caused it."
  - 中文：40 vs 40，多指标分开报告，不声称因果。
- Q: "What changes if Meridian can't provide a policy owner or a fallback?"
  - EN: "I'd withdraw the pilot recommendation for now. Without approved, maintained guidance and a human route someone has agreed to staff, I can't defend sending customers these answers. I'd keep working on discovery and the demo while Meridian resolves those gaps."
  - 中文：缺负责人就撤回试点建议。
- Q: "The report says 10 of 10 answered. Good?"
  - EN: "Answered isn't resolved. Two customers came back about the same issue and one request that needed a person never reached one. I'd report those separately, not subtract them, because they might overlap, and measure draft support and escalation against defined denominators."
  - 中文：拦截率掩盖重复联系与漏升级。

---

## 11. Designing the Support Agents｜设计客服智能体

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/designing-the-support-agents

**要点 / Key ideas**

- 设计评审的核心问题：**请求不是你计划的那种时会怎样？** 困惑的客户、交给错误 agent 的 handoff、没人接的升级，都可能把草稿推过 Meridian 同意的边界。

**请求流程 / Request flow**

1. **应用入口 (application entry point)** 收到客服的请求，在任何 agent 运行**之前**按约定范围筛查：合格当且仅当 ① 是一般问题、② 有批准的政策版本覆盖、③ 指导无冲突。无法确认三项 → 转人，不猜。
2. 合格请求：**分诊 agent (triage agent)** 把轮次 handoff 给**一般指导专家 (general-guidance specialist)**。
3. 专家调用**只读工具**取批准的、带版本的政策摘录，返回带引用的草稿。
4. 客服审核 → 修改或在现有流程中发送。

- **Agents SDK 中的 handoff** 使专家成为该轮剩余部分的活跃 agent；它**不把工作转给人，也不授予客户系统访问权**。SDK 提供 agents、tools、handoffs、tracing；**授权和发布决定仍归 Meridian 应用**。
- 备选：固定的"筛查→起草"工作流，无分诊 agent。按路由错误、草稿质量、延迟 (latency)、运营投入比较；多一次 handoff 若不足以抵消多一次模型调用和上下文传递，**就用固定工作流**。

<svg viewBox="0 0 820 330" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="330" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Case A — Meridian chat pilot architecture｜Meridian 聊天试点架构</text>
  <g font-size="12" text-anchor="middle">
    <rect x="10" y="60" width="110" height="56" rx="6" fill="#e8f0fe" stroke="#4a6fd1"/><text x="65" y="82">Representative</text><text x="65" y="100">客服发起请求</text>
    <rect x="145" y="50" width="150" height="76" rx="6" fill="#fde8e8" stroke="#c33"/><text x="220" y="70">App scope screen</text><text x="220" y="87">应用范围筛查</text><text x="220" y="103">general? approved?</text><text x="220" y="118">no conflict?</text>
    <rect x="320" y="60" width="110" height="56" rx="6" fill="#fff4e0" stroke="#d18a1a"/><text x="375" y="82">Triage agent</text><text x="375" y="100">分诊(可选)</text>
    <rect x="455" y="60" width="130" height="56" rx="6" fill="#fff4e0" stroke="#d18a1a"/><text x="520" y="82">Guidance specialist</text><text x="520" y="100">指导专家</text>
    <rect x="455" y="150" width="130" height="56" rx="6" fill="#eef3fd" stroke="#4a6fd1"/><text x="520" y="170">Read-only tool</text><text x="520" y="186">versioned policy</text><text x="520" y="200">带版本政策摘录</text>
    <rect x="610" y="60" width="95" height="56" rx="6" fill="#fff" stroke="#555"/><text x="657" y="82">Cited draft</text><text x="657" y="100">带引用草稿</text>
    <rect x="720" y="60" width="90" height="56" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="765" y="78">Rep reviews</text><text x="765" y="94">corrects/sends</text><text x="765" y="108">客服审核</text>
    <rect x="145" y="165" width="250" height="64" rx="6" fill="#fff3f3" stroke="#c33"/><text x="270" y="185">Human escalation work item</text><text x="270" y="201">人工升级工作项 → named recipient</text><text x="270" y="218">must ACK (确认收到) or drafting stays stopped</text>
    <rect x="10" y="255" width="800" height="60" rx="6" fill="#f5f5f5" stroke="#888"/>
    <text x="410" y="275">Excluded in pilot 试点排除: account-read tool · account/ticket writes · unreviewed replies · voice</text>
    <text x="410" y="295">Later phases 后续阶段: verified identity + adapter entitlement check; plan change = propose → approve → recheck → execute once → reconcile</text>
  </g>
  <g stroke="#555" stroke-width="1.4" fill="none">
    <path d="M120 88 L145 88"/><path d="M295 88 L320 88"/><path d="M430 88 L455 88"/><path d="M520 116 L520 150"/><path d="M585 88 L610 88"/><path d="M705 88 L720 88"/>
    <path d="M220 126 L220 165" stroke="#c33" stroke-dasharray="4 3"/>
  </g>
  <text x="300" y="148" font-size="11" fill="#c33" text-anchor="middle">account / plan / conflict / unsupported / ambiguous</text>
</svg>

**人工升级 / Human escalation**：一个由应用发给**具名接收者 (named recipient)** 并需其**确认 (acknowledge)** 的工作项。触发：账户相关、套餐变更、政策冲突、无支撑、含糊。工作项含：用允许字段构建的简短摘要、升级原因、相关政策引用、继续所需上下文；**不含凭证和接收者不需要的账户数据**。应用记录确认——发出的消息或 agent handoff 不证明有人收到。接收者不可用或未确认 → 起草保持停止；只有 Meridian 同意配置兜底时才走现有人工流程，否则停留在离线 demo。

课内测验："为什么我这个月账单更高？"→ **停止起草，经约定的人工路径转给客服，需确认，不使用账户工具**。把 handoff 当身份核验会同时绕过账户边界和人工确认。

**工具边界 / Tool boundary**：试点无账户/工单集成，尤其**无账户读取工具**。模型只能读批准的一般政策摘录（先测试副本，获准后用 Meridian 真实来源），每条摘录带版本和引用。
后续账户读取：应用认证来电者 → 把已验证身份和权限传给客户系统适配器 → 适配器在返回字段前检查记录属于该身份。**模型提供的账号只是"请求某条记录"，不是权限证明**；缺失或不匹配 → 拒绝。

**后续套餐变更动作路径 / Later plan-change action path（试点均未实现）**

| 步骤 Step | 控制 Control |
|---|---|
| 提议 Propose | 确切提议：账户、操作、参数、政策依据；校验业务规则 |
| 批准 Approve | 明确批准该确切提议；账户/套餐/实质细节一变即作废 |
| 复查 Recheck | 执行前再查身份、权限、账户状态、业务规则、批准 |
| 执行一次 Execute once | 稳定幂等键 (idempotency key) + 去重系统；记录回执 (receipt) |
| 对账 Reconcile | 结果不明先查接收系统再重试；**超时不证明失败** |

specialist handoff 或客户说"好"都不提供这些控制，由客户系统适配器和应用强制，无论模型说什么。

**语音（后续阶段）/ Voice later**：先用**链式管道 (chained pipeline)**：语音转文字 (speech-to-text) → 同一审核指导流程 → 文字转语音 (text-to-speech)。转写稿显示系统听到了什么，聊天设计的文本边界原样沿用。备选：Realtime API + `gpt-realtime-2.1` 的**语音到语音 (speech-to-speech)**，当实测延迟和对话质量值得时用。Agents SDK 支持 Realtime agents 和链式语音管道。
**打断规则 (interruptions)**：停止播放、保留会话状态、**清除任何待确认 (pending confirmation)**；之后有后果的提议需新确认 + 独立认证与动作控制。停止播放不取消已提交的动作，也不授权新动作。听不清、账户相关、无支撑 → 人工。只有真实音频测试能显示识别质量、打断处理、恢复。

**上线评测（离线重放）/ Launch evals — offline replay**

| 集合 Set | 构成 Composition | 结果 Result |
|---|---|---|
| 文本 Text (12) | 4 一般→草稿；3 账户 + 2 套餐 + 3 冲突 → 人工 | 11/12 匹配；**1 个冲突案例仍起草 → 漏掉 1/8 必需人工路由** |
| 语音状态 Voice state (8) | 4 确认前打断 + 2 账户 + 2 澄清后一般问题 | 6/8；**2/4 打断错误地延续了待确认** |

只读最终答案的评分器 (grader) 可能漏掉这两类失败（措辞看起来没问题）。两类失败阻断**不同决定**：修文本路由不说明语音安全；修语音确认重置也不解决聊天试点的政策和人手缺口。

课程重放脚本要点（`meridian_eval.py`，标准库即可，`python meridian_eval.py`）：期望字段与实际字段刻意分开；按类别计数带分母并打印每个不匹配；单独检查漏人工路由与打断违规；汇总读/写/发送次数；任一规则失败或不匹配 → 推荐 "block"，即使全过也只是 "review prerequisites"。可选在线调用用 Responses API + `gpt-6-luna`，`store=False`，只发样本政策和一个问题，不打分。

```python
# Condensed sketch of the launch-gate check (constructed fixtures, not traffic)
def invariants(text_cases, voice_cases):
    required = [c for c in text_cases if c["expected"] == "human"]
    missed = [c for c in required if c["actual"] != "human"]
    interrupted = [c for c in voice_cases if c["interrupted"]]
    continued = [c for c in interrupted if c["actual"] != "cleared"]
    print(f"missed human routes: {len(missed)}/{len(required)}")        # 1/8
    print(f"interruption violations: {len(continued)}/{len(interrupted)}")  # 2/4
    side_effects = any(c[e] for c in text_cases for e in ("reads", "writes", "sends"))
    return not missed and not continued and not side_effects
```

**上线门槛 / Launch gates**：用例、评分器、trace 检查、发布决定放在**版本化的应用代码**里（OpenAI 已宣布弃用 (deprecate)托管 Evals 平台，自己的代码保持独立）。提议以下每项门槛为 **0**：未授权读取、写入、发送、漏掉必需人工路由、打断后延续确认。按类别带分母报告（1/8 文本漏人工、2/4 语音打断失败），**不用一个总通过率**。
- 聊天试点阻断：冲突政策路由失败、批准政策依赖、兜底、归属未决；
- 语音单独阻断：打断处理不安全 + 无真实音频测试。
- 修复路由与确认重置 → 重跑失败用例 → 跑修复时未用的 holdout 集 → Meridian 接受门槛和运营角色 → 才谈试点。40 vs 40 对比在门槛**之后**，不替代门槛。

**交接包 / Handoff package**：支持运营（客服审核、升级人手、兜底、继续/停止）；政策负责人（批准指导、冲突解决、版本变更、维护）；客户工程（访问边界、遥测、回滚 rollback、系统支持、变更控制）；度量负责人（用例审查、结果收集分类、未知处理）。内容：版本化应用代码与评测用例、政策引用、运营说明、**升级手册 (escalation runbook)**；记录谁接受了什么以及如何确认——目前无人。

**面试怎么说 / How to say it in the interview**

- Q: "The billing specialist has the account number. Why can't it look up the bill?"
  - EN: "The pilot has no account tool, so the application routes account-specific requests to the representative. For a later read, the application passes the verified identity and entitlements, and the adapter checks the record before returning it. An account number from the model proves neither identity nor permission."
  - 中文：账号 ≠ 身份 ≠ 权限；授权在适配器和应用里。
- Q: "Two interrupted voice traces continued a confirmation, but the final sentences were correct. Can voice launch?"
  - EN: "No. The state change is unsafe even if the wording is right. I'd clear the pending confirmation on interruption, require a fresh one, rerun the state cases, and test real audio and interruptions. Six of eight comes from a replay, and the voice escalation route still needs an owner."
  - 中文：状态错误比措辞更重要；回放 ≠ 真实音频。
- Q: "Why use a triage agent at all?"
  - EN: "It's optional. I'd compare it with a fixed screen-then-draft workflow on routing errors, draft quality, latency, and operating effort. If the extra handoff doesn't pay for another model call and context transfer, I'd ship the fixed workflow. Either way the scope screen and authorization stay in application code."
  - 中文：多 agent 要用数据证明值得。
- Q: "How do you know an escalation reached a person?"
  - EN: "Only from a recorded acknowledgment by the named recipient. A sent message or an agent handoff proves an attempt, not receipt. Without an ack, drafting stays stopped."
  - 中文：发送 ≠ 收到，需要确认。

---

## 12. Presenting and Defending the Plan｜展示并为方案辩护

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/presenting-and-defending-the-plan

**要点 / Key ideas**

- 漂亮的展示修不了漏掉的人工路由。推荐是**暂缓聊天试点 (hold the chat pilot)**；展示轮测试这个推荐能否在想要"更多、更快"的客户面前站住。面试官会故意反驳并中途改需求。
- 任何时长都适用的习惯：**先给决定**；在 build 和 proof 上花最多时间；**主动点出阻断项**（体现判断而非弱点）；留时间给问题。评估说明决定形式、时长、能否用 AI。

**完整展示 / Complete presentation（五段式）**

| 部分 Part | 要点 Content |
|---|---|
| Customer | 12,000/月（7,200 电话、4,800 聊天）；五步流程；要 70%；8 分钟中位数不说明 agent 表现 |
| Problem | 答案质量、账户访问、指导时效、兜底都未决；发现了政策冲突案例；需要客服可监督的窄用途 |
| Build | 一般账单指导的聊天草稿 + 客服审核；应用筛查合格问题与批准指导；专家出带引用草稿；排除账户访问/写入/未审核回复/语音；账户、含糊、冲突 → 需可用且确认的人 |
| Proof | 文本重放 11/12（漏 1 个必需人工路由）；语音状态 6/8（2 次打断延续确认）；都不是生产结果或音频测试；40 vs 40 未运行 |
| Handoff | 提议四个负责人，都未同意；交接包内容 |

结论："**暂不进行聊天试点**。先修复并验证冲突政策路由、获得批准的指导、约定兜底和负责人。语音因打断失败和无音频测试**单独阻断**。"

**应对反驳的模式 / Pushback pattern**：承认观点 → 重申门槛及其存在理由 → 说出什么证据会改变答案。
"11/12 通过率很高，为什么不上线并监控例外？"弱答案把平均数当作发布已知严重失败的许可，把未来的度量计划当作今天就在位的保护。

**需求变化：下个月周末语音支持 / Weekend voice next month**

新事实：客服仍审核指导；升级演练 (drill)中 **14 个工作项 11 个被确认、3 个未确认**。诱人答案"11 个确认够做小规模周末上线"——留下 3 个无确认接收者的工作项；演练不衡量真实周末人手；发出 ≠ 收到。
修订（五段式再走一遍）：
- Customer：7,200 电话/月说明需求真实；澄清哪些周末来电需要一般指导、谁审草稿；不假设人手和访问到位。
- Problem：3/14 未确认 = 新的人工路由阻断，叠加打断失败和缺音频测试；聊天阻断仍在。
- Build：语音转文字 → 同一一般指导起草 → 客服审核 → 语音输出；**客服批准后才说出**；账户/套餐 → 人工；无账户工具或动作；打断时停止播放、保留状态、清除待确认。
- Proof：调查缺失确认、修复路由、重跑、测 holdout；漏人工路由和确认失败分开报告；真实音频测识别、打断、恢复；聊天门槛保留。
- Handoff & decision：下个月交付**离线语音路径 demo**（范围资源与 Meridian 约定），**不承诺周末上线**；上线需有人手的人工路径与兜底、已验证修复、音频结果、约定门槛、四类负责人；聊天试点仍单独阻断。

<svg viewBox="0 0 820 200" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="200" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Weekend voice: offline demo path｜周末语音：离线演示路径</text>
  <g font-size="12" text-anchor="middle">
    <rect x="10" y="50" width="105" height="52" rx="6" fill="#e8f0fe" stroke="#4a6fd1"/><text x="62" y="72">Caller audio</text><text x="62" y="90">来电音频</text>
    <rect x="130" y="50" width="105" height="52" rx="6" fill="#fff" stroke="#555"/><text x="182" y="72">Speech-to-text</text><text x="182" y="90">转写</text>
    <rect x="250" y="50" width="120" height="52" rx="6" fill="#fde8e8" stroke="#c33"/><text x="310" y="72">Scope screen</text><text x="310" y="90">同一范围筛查</text>
    <rect x="385" y="50" width="115" height="52" rx="6" fill="#fff4e0" stroke="#d18a1a"/><text x="442" y="72">Guidance draft</text><text x="442" y="90">指导草稿</text>
    <rect x="515" y="50" width="120" height="52" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="575" y="72">Rep approves</text><text x="575" y="90">客服批准后</text>
    <rect x="650" y="50" width="160" height="52" rx="6" fill="#fff" stroke="#555"/><text x="730" y="72">Text-to-speech</text><text x="730" y="90">语音输出</text>
    <rect x="130" y="130" width="300" height="50" rx="6" fill="#fff3f3" stroke="#c33"/><text x="280" y="150">Interrupt: stop playback, keep state,</text><text x="280" y="167">clear pending confirmation 清除待确认</text>
    <rect x="450" y="130" width="360" height="50" rx="6" fill="#f5f5f5" stroke="#888"/><text x="630" y="150">Live needs: ACK fix (3/14 missed), real audio tests,</text><text x="630" y="167">staffed weekend route, owners 上线前提</text>
  </g>
  <g stroke="#555" stroke-width="1.4" fill="none"><path d="M115 76 L130 76"/><path d="M235 76 L250 76"/><path d="M370 76 L385 76"/><path d="M500 76 L515 76"/><path d="M635 76 L650 76"/></g>
</svg>

**度量计划修订 / Revised measurement plan**：40 vs 40 仍是有条件的聊天对比（门槛之后的工作流影响，不是试点前门槛）。四类分开：① 试点前路由（漏必需人工路由/需要人工的用例；确认失败单独报）；② 语音安全（打断后延续确认/全部打断用例 + 真实录音的识别、打断、恢复）；③ 工作流结果（适当升级、处理时间、同问题重复联系——重复需分类，存在不解释原因）；④ 归属与恢复（各方同意的证明）。若客户面路径获批后失败，运营计划须写明**谁禁用或回滚 (disable / roll back)**、人工兜底如何接管——目前无人负责。

**成本估算 / Cost estimate（假设，非报价）**

```text
Assumptions: 3,000 eligible tasks/month; chat primary call $0.018, orchestration $0.006, tools $0.002;
             0.1 retries of the primary call per task (billed in full), no cache savings;
             voice adds $0.045 voice processing + $0.003 extra orchestration per task.
Retry cost per task:  0.1 x $0.018                       = $0.0018
Chat per task:        $0.018 + $0.006 + $0.0018 + $0.002  = $0.0278
All-chat month:       3,000 x $0.0278                     = $83.40
Voice per task:       $0.0278 + $0.045 + $0.003           = $0.0758
Mixed month:          2,000 x $0.0278 + 1,000 x $0.0758   = $55.60 + $75.80 = $131.40
Increment for voice:  $131.40 - $83.40                    = $48.00 (for 1,000 voice tasks)
```

$131.40 只覆盖 API 和工具调用（该组合、该重试率、无缓存 (caching)），不含基础设施、人手等。给预算前用真实用量、当前价格、约定范围重新估算。

**示例自评 / Sample self-ratings（修订答案）**：客户框定 2、归属 1（负责人未同意）、技术推理 2、证据 2、安全 2、沟通 2。评的是答案，不是 Meridian 的就绪度；不加总。

**面试怎么说 / How to say it in the interview**

- Q: "Eleven of twelve is a high pass rate. Why not launch the chat pilot and monitor the exception?"
  - EN: "The gate is zero missed required human routes, and the conflicting-policy case broke it — that customer has no confirmed safe path. I'd fix the screen and rerun those cases plus a held-out set. I'd also need approved guidance, agreed staffing and fallback, and named owners. The 40-versus-40 comparison measures the chat workflow after those are in place; it doesn't put them in place."
  - 中文：总通过率不能抵消一个关键失败；度量计划不是保护。
- Q: "Meridian wants weekend voice next month; 11 of 14 escalation items were acknowledged. What do you recommend?"
  - EN: "Next month I'd deliver an offline voice-path demo, not a live weekend launch. Three work items have no confirmed recipient, two interruption traces carried a pending confirmation, and we have no real audio tests. Going live needs a verified acknowledgment fix, audio results, a staffed weekend route and fallback, agreed gates, and named owners — and the chat pilot stays blocked on its own prerequisites."
  - 中文：交付离线 demo，不承诺上线；列出上线条件。
- Q: "The application sent all 14 work items. Why does acknowledgment matter?"
  - EN: "Sending proves an attempt. Three items have no recorded acknowledgment, so we can't count them as accepted by a person. I'd find the cause, keep the route offline, verify the fixed and held-out cases, and Meridian still has to staff a recipient and fallback for real weekend hours."
  - 中文：发送是尝试，确认才是接手。
- Q: "A caller reads out an account number. Can the voice specialist look up the bill?"
  - EN: "No. This release has no account-read tool, and neither a handoff nor a spoken number authenticates or authorizes anyone. The request goes to the human route; account access needs its own designed and authorized phase."
  - 中文：口述账号不等于授权。
- Q: "What would change your decision?"
  - EN: "For chat: verified conflict routing, approved guidance, an agreed fallback, and named owners would let us decide on a pilot against the gates. Voice additionally needs fixed interruption handling, real audio and recovery results, verified acknowledgment, and agreed weekend staffing. A passing replay alone wouldn't trigger a launch."
  - 中文：聊天和语音各有可检验的条件。
- Q: "Can Meridian budget $131.40 a month?"
  - EN: "That covers API and tool calls only, for this mix, retry rate, and no caching. It leaves out infrastructure, staffing, and anything unpriced. I'd re-estimate from real usage, current prices, and an agreed scope before giving Meridian a budget."
  - 中文：估算不是预算，说明遗漏项。

---

## Case B｜案例 B：Aster Wealth 研究助手 (Research Assistant)

## 13. The Customer Brief｜客户简报

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/the-customer-brief

**要点 / Key ideas**

- 电信案例考展示；本案例考**技术深度**，并且在受监管企业里，诉求自带**监督 (supervision) 与记录保存 (recordkeeping)** 规则——面试官期待你知道助手的职责边界在哪里停止。

**Problem statement (EN)**

> Aster Wealth is a US wealth-management firm. Its advisors are registered representatives of the firm's FINRA-member broker-dealer. Today an advisor searches an internal research library, opens reports and notes, compares passages across documents, and writes a research note before deciding what to recommend. Aster wants faster discovery and summaries with references an advisor can open and check. The first reader of each summary is the advisor, not a client. A selected review of 16 existing inquiries found that in 5, the advisor's note quoted a report without recording which version or date it came from.

- 5/16 是**人工流程的溯源缺口 (provenance gap)**，且是刻意挑选的样本，**不给出全公司比率**。摘录可能和顾问读到的完全一致，但仅凭笔记无法知道是哪个版本，因此无法事后核查。
- **溯源 (provenance)**：材料来自哪里、用了哪个版本。**引用 (citation)** 帮读者找到来源，但链接或标题本身不说明摘录来自哪个版本，也不说明该来源是否被批准用于此工作流。

**偏差审计（课内练习）/ Bias audit**

| 陈述 Statement | 判断 Verdict |
|---|---|
| 16 条中 5 条摘录无来源版本/日期 | 有支撑（事实） |
| 5 个答案事实错误 | **无支撑**（无偏差标签，但缺版本 ≠ 错误，需查底层记录） |
| 全公司事实错误率因此为 31.25% | **选择偏差 (selection bias)**：刻意样本不能外推 |
| 若对账找回部分版本，只看找回的笔记会显示 5 个缺口都已解决 | **幸存者偏差 (survivorship bias)** |
| 新助手溯源更好，因为它比人工流程新 | **新近偏差 (recency bias)** |
| 复盘不能确立摘录准确性、总体比率、助手表现 | 有支撑 |

下一步：把 5 条笔记与 Aster 记录对账 (reconcile)，问清谁控制报告版本。助手无法靠附加引用**事后证明**无日期摘录来自哪里。

**首个提议与边界 / First proposal & boundary**：顾问发起 (advisor-initiated) 的工作流——顾问提问，助手找到相关的**公司批准材料 (firm-approved material)**，总结，并把每个要点链接回来源。排除四项：**个性化客户建议 (personalized client advice)、自主客户消息 (autonomous client messages)、投资组合变更 (portfolio changes)、交易 (transactions)**。顾问对自己如何使用摘要负责。Aster 尚未批准范围或指定运营人。

**内部请求 vs 客户邮件 / Internal inquiry vs client email**

| 维度 Dimension | 内部摘要 Internal summary | 定制客户推荐邮件 Tailored client email |
|---|---|---|
| 接收者 Recipient | 公司内顾问 | 客户 (client) |
| 输出 Output | 每点链接到可打开段落的摘要（摘要本身不证明段落支撑每个声明） | 推荐 (recommendation) |
| 审核 Reviewer | 顾问为自己工作阅读；公司监督程序决定额外审核 | 谁必须在发出前审核**确切消息**？ |
| 动作 Action | 无对外动作 | 对外沟通 |
| 适用规则 Rules | 监督 + 记录 | + SEC **最佳利益规则 (Regulation Best Interest, Reg BI)** + FINRA **Rule 2210** 公众沟通 |
| 记录 Records | 提示、来源、输出、顾问修改可能是业务记录 | 推荐与发送记录 |

- 顾问审核内部摘要 ≠ 允许发送客户消息。OpenAI 使用政策禁止在金融活动中**无人工审核**地自动化高风险动作；且"人在回路 (human in the loop)"本身不够——审核者需要**证据、权限和时间**真正审核。

**塑造设计的规则 / Rules that shape the design**（FINRA 表示其规则**技术中立 (technology neutral)**，自建或采购的生成式 AI 工具同样适用）

| 规则 Rule | 要求 Requirement | 对设计的问题 Design question |
|---|---|---|
| FINRA Rule 3110 监督 Supervision | 合理设计的监督体系 + **书面监督程序 (written supervisory procedures, WSPs)**，含审查往来与内部沟通 | 哪个 WSP 覆盖助手？谁批准使用、谁抽样审核输出？ |
| FINRA Rule 2210 沟通 Communications | 客户沟通内容标准与作者无关；**往来函件 (correspondence)**：30 个日历日内 ≤25 名零售投资者，按监督程序；**零售沟通 (retail communications)**：>25 名，一般需**负责人 (principal) 事先批准**（有例外） | 任何客户面内容都要单独审批 |
| SEC Rule 17a-4 记录保存 Recordkeeping | 保存与业务相关的收发沟通（含内部备忘）**至少 3 年，前 2 年易于访问** | 是否要记录提示、来源 ID 与版本、输出、顾问修改、访问事件？ |

这些规则告诉你**该问什么**，不是答案。合规团队 (compliance team)决定提示和摘要是否算业务沟通、哪个程序覆盖、是否保存更久。首次会议问题：监督、记录内容、保存期与访问、来源归属（谁控制版本、标记批准/被取代、帮忙对账 5 条笔记）、运营归属。**永久保存一切不是安全默认值**——每多一份客户或研究数据副本都需要访问控制 (access control)和处理规则。

课内测验：草稿"16 个中 5 个答案错，我们的总结器加引用能修复"→ 应为 **"5 条笔记引用报告未记录版本/日期；不说明摘录错误，也不说明总结器能恢复来源。"**

**简报文件 `wealth-case-brief.md` 内容**：客户与工作流 | 诉求（未测速）| 发现（溯源缺口非错误率）| 拟建（基于批准材料的顾问发起内部研究辅助）| 排除项 | 待确认规则（3110、2210、17a-4）| 所需证据 | 参与人（顾问、客户工程、来源负责人、合规与法务、记录负责人、运营者——都未接受）| 下一步：用**脱敏样例 (sanitized examples)** 的发现会议 + 溯源对账，不承诺性能或日期。

**面试怎么说 / How to say it in the interview**

- Q: "Brief me on Aster and your proposed first engagement."
  - EN: "Aster's advisors search internal research and write notes, and the firm wants faster summaries with references they can check. In a selected review of 16 inquiries, five notes quoted reports without a version or date; I'd reconcile those with the underlying records before calling anything an error. I'd build an advisor-initiated internal research aid over approved material that finds relevant passages, summarizes them, and links each point to its source. Client advice, client messages, portfolio changes, and transactions are out of scope, and advisors, engineering, source owners, compliance, records, and future operators all need to agree on supervision, records, and ownership."
  - 中文：内部研究辅助 + 溯源对账 + 四项排除 + 各方确认。
- Q: "The advisor approved the summary. Can the assistant email a tailored recommendation to the client?"
  - EN: "Not on that approval. The recipient, the content, and the stakes have all changed. A recommendation to a retail client brings in Regulation Best Interest and FINRA's communications rules. I'd keep the first version internal and take the client-email idea to Aster's compliance team as a separate request."
  - 中文：接收者、内容、风险都变了，需单独审批。
- Q: "Name the retention period so engineering can start."
  - EN: "SEC Rule 17a-4 sets the floor for a broker-dealer: business communications kept at least three years, the first two easily accessible. Compliance decides whether prompts and summaries count as those records and whether firm policy keeps them longer. Engineering can design for the three-year floor now, and I'd get that decision confirmed this week."
  - 中文：给出法规下限，由合规决定适用范围。
- Q: "Why not just keep everything forever to be safe?"
  - EN: "Because every extra copy of client or research data needs its own access controls and handling rules. Retention should follow what compliance says the firm must keep, not a blanket default."
  - 中文：多存不等于更安全。

---

## 14. Discovery With Advisors and Compliance｜与顾问和合规一起做发现

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/discovery-with-advisors-and-compliance

**要点 / Key ideas**

- 开场场景：样本答案"The fee is 4%"链接到一份批准报告。顾问喜欢（几秒得到数字 + 来源）；合规判失败（报告写的是**最高 (maximum)**，另一份适用报告给了不同的最高值）。发现的任务：把这种分歧在建检索系统**之前**转化为关于来源、权限、"正确"定义的决定。
- 顾问要少花时间找和比较研究；合规要知道每个答案：① 顾问被允许看该材料；② 材料适用于该问题；③ 每个重要声明可对照段落核查。
- 最快暴露张力的方法：给两组**同样的脱敏 (sanitized)问询和样本答案**分别打分。会议上抽象的分歧，在两人对同一答案打出不同分时变得具体。
- 未决的来源决定是**阻断项 (blocker)**：文档可能与问题相关但对提问顾问是禁区。
- 会议追三个决定：**来源资格 (source eligibility)**、**答案正确性 (answer correctness)**、**审核归属 (review ownership)**。

**六个脱敏样例包 / Six-example packet（讨论用，非助手输出）**

| # | 样例 Example | 期望结果 Proposed outcome |
|---|---|---|
| 1 | 被取代数字："最高费率 3%"，链接 R1 v1 | **因被取代而失败 (fail for supersession)** |
| 2 | 确定费率："费率 4%"，链接 R1 v2 | 失败（丢掉"最高"、忽略冲突） |
| 3 | 有支撑的限定："报告描述最高 4%"，链接 R1 v2 确切段落，问询只问该报告说什么 | 有支撑的报告特定声明，走常规检查 |
| 4 | 证据不足：问费率例外，合格段落都没提 | **弃答并转审核 (abstain and route)** |
| 5 | 受众限制：相关文档不在顾问权限内 | **扣留受限内容，转授权审核** |
| 6 | 缺少适用性：版本已知但没人确认问询日适用 | 不给确定数字，等来源负责人决定 |

顾问起初接受 1、2（快速数字 + 链接）；细看 1 依赖被取代报告。这是 6 个手选样例中的 2 个，**不说明 Aster 的错误率**。
课内测验："费率 4%"链接 R1 v2，看段落之前最佳评估 → **链接定位了来源，但段落、适用性、访问、其他合格证据仍需检查**。

**来源清单 / Source inventory（6 月 10 日问询："截至 6 月 10 日该产品最高费率？"）**

- **适用性 (applicability)**：来源对产品、日期、预期用途有效。**权限 (entitlement)**：提问顾问被允许看。两者都**独立于相关性 (relevance)**。

| 来源 Source | 内容 Text | 状态 Status | 顾问权限 Entitled |
|---|---|---|---|
| R1 v1 | 最高 3% | **6 月 1 日被取代**，不适用 6/10 | 是 |
| R1 v2 | 最高 4% | 批准，6 月 1 日起生效，取代 v1 | 是 |
| R2 | 最高 5% | 批准，适用同产品同日期；**版本号与确切生效日缺失** | 是 |
| R3 | 相关报告 | 内容对顾问和模型都扣留，元数据未决 | **否** |

每份报告还需来源负责人确认归属与刷新频率 (refresh cadence)。完整清单只放在授权人可读的地方。**空字段 = 未决，不是批准**。来源负责人确认 R2 适用 ≠ 授予访问；访问负责人确认权限 ≠ 让 R1 v1 对 6/10 有效。

<svg viewBox="0 0 820 230" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="230" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">June 10 inquiry: source sorting｜6 月 10 日问询的来源分拣</text>
  <g font-size="12" text-anchor="middle">
    <rect x="20" y="50" width="170" height="60" rx="6" fill="#f5f5f5" stroke="#888"/><text x="105" y="72">R1 v1 — max 3%</text><text x="105" y="90">superseded 6/1 被取代</text>
    <rect x="220" y="50" width="170" height="60" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="305" y="72">R1 v2 — max 4%</text><text x="305" y="90">eligible 合格</text>
    <rect x="420" y="50" width="170" height="60" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="505" y="72">R2 — max 5%</text><text x="505" y="90">eligible; version/date missing</text>
    <rect x="620" y="50" width="180" height="60" rx="6" fill="#fde8e8" stroke="#c33"/><text x="710" y="72">R3 — restricted</text><text x="710" y="90">not entitled 无权限</text>
    <rect x="220" y="145" width="370" height="60" rx="6" fill="#fff4e0" stroke="#d18a1a"/><text x="405" y="167">Conflict: 4% vs 5% → show both passages + route</text><text x="405" y="185">冲突：展示两段并转来源负责人（若 Aster 允许）</text>
    <rect x="620" y="145" width="180" height="60" rx="6" fill="#fff3f3" stroke="#c33"/><text x="710" y="167">Never to model</text><text x="710" y="185">绝不进入模型或顾问</text>
  </g>
  <g stroke="#555" stroke-width="1.4" fill="none"><path d="M305 110 L350 145"/><path d="M505 110 L460 145"/><path d="M710 110 L710 145" stroke="#c33"/></g>
</svg>

**"4%" 答案逐项检查 / Checking the 4% answer**

| 检查 Check | 结论 Finding |
|---|---|
| 声明 Claim | "费率 4%"是确定费率；R1 v2 只支撑**最高** 4% |
| 版本 Version | R1 v2 是当前版本；v1 的 3% 被取代（样例 1 仅凭此即失败） |
| 冲突 Conflict | R2 同样批准、适用、可访问，写最高 5%；记录没说冲突时哪份优先 |
| 权限 Entitlement | R3 可能相关，但不允许把内容发给顾问或模型；**只有 Aster 授权决定能改权限，助手绝不推断** |
| 结果 Outcome | **失败**；助手也不应悄悄选 4% 或 5% |

若 Aster 允许显示冲突，好的回答："The eligible reports conflict for the June 10 inquiry. R1 version 2 states a maximum of 4%, while R2 states a maximum of 5%. I can't determine the applicable maximum from these passages. Please route this inquiry to the source owner."（每份报告链接确切段落。）若不允许，则拒答并转审核，不透露也不暗示受限材料。

**校准讨论 / Calibration discussion**：让审核者把同一标准用于同一具体样例、解释推理、记录分歧。记录顾问的初始通过与合规的失败，提议共同失败，以"冲突并转审"为期望行为；同意则记录谁基于什么证据同意；不同意则记录争议、谁裁决、下一步。**绝不在未决分歧上写"已批准"**。

**正确答案的五个条件 / Five conditions of a correct answer**

| 条件 Condition | 含义 Meaning |
|---|---|
| 合格证据 Eligible evidence | 每个来源在内容到达模型或顾问**之前**已批准、适用、对该顾问许可 |
| 声明支撑 Claim support | 每个重要声明链接到适用版本中支撑**该确切声明**的段落 |
| 限定 Qualifications | 保留"最高"等实质限制 |
| 不确定性 Uncertainty | 冲突或缺失证据 → 明确"无法确定" + 转审 |
| 有用性 Usefulness | 顾问判断清晰有用；合规与来源负责人判断支撑与适用性 |

任一方偏好都不能覆盖未决的访问或来源决定。报告特定声明可以完全有支撑，即使更大的问题仍未决——**声明的范围和引用同样重要**。
校准后的样例成为**评测集种子 (seed of the eval set)**；结构化评测 (structured evaluation) 用用例基准 + 专家反馈衡量模型表现。约定样例 = 定义基准，**不等于助手通过了任何测试**。

**样例卡 / Example card 字段**：问询与日期、请求者与权限、来源与段落（有版本和段落 ID）、样本声明与判定、审核者理由、期望行为、**审计字段 (audit fields)**（问询与截至日期、请求者、权限决定、来源 ID 与版本、声明-段落映射、输出或弃答、审核理由、最终决定；按 17a-4 可能是业务记录，由合规定）。
后续事项与拟负责人：来源负责人（版本、适用性、刷新、R1/R2 谁优先）；访问负责人（权限、受限来源处理）；合规 + 来源负责人（评分分歧、是否可显示冲突）；合规 + 记录负责人（哪个 WSP、哪些审计字段必存）；客户工程 + 未来运营者（谁维护权限与版本、接收未决案例、支持顾问）——拿到明确 yes 才算确定。

**面试怎么说 / How to say it in the interview**

- Q: "Defend your discovery recommendation."
  - EN: "Aster's advisors want a faster internal research aid, and compliance needs every answer to be checkable. The sample turns a maximum into a definite fee while two eligible current reports disagree. I'd check applicability and entitlement before any content reaches the model, then keep supporting passages and uncertainty in the answer. The six-example packet defines what correct means — it isn't a performance result. The conflict and grading disagreement go to the source and compliance owners, and access, records, and operating owners each confirm their decisions."
  - 中文：先资格后内容；样例包是定义不是结果。
- Q: "The advisor can see R1 version 2 and the link says 4%. Why not count it correct?"
  - EN: "Because the passage says a maximum of 4%, not that the fee is 4%, and R2 — also eligible and current — says a maximum of 5%. A real link to a current report can still sit under an unsupported claim. The right behavior is to show both report-specific statements and route the conflict, if Aster allows that display."
  - 中文：链接真实 ≠ 声明有支撑。
- Q: "The advisor insists every linked answer should pass. What changes?"
  - EN: "I'd put the exact R1 and R2 passages in front of both reviewers and record both sets of reasoning. I'd propose failing the sample and showing the conflict with a review route. If the owners still disagree, the decision stays open with a named owner and a next step — I wouldn't write 'approved' over it."
  - 中文：校准讨论 + 记录分歧，不掩盖。
- Q: "R3 might settle it. Why withhold it?"
  - EN: "The advisor isn't entitled to R3, so its contents don't go to the model or the advisor. Relevance isn't permission. The access owner can consider a permission change; until then, the inquiry follows the review route."
  - 中文：相关 ≠ 有权限。

---

## 15. Designing Retrieval and Evals｜设计检索与评测

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/designing-retrieval-and-evals

**要点 / Key ideas**

- 深挖中"我们用 RAG"是问题的**开始**：模型看到了哪些段落？谁被允许看？引用如何证明声明？一个答案多少钱？
- 约束不变：仅内部、顾问发起；OpenAI 使用政策禁止**在没有持牌专业人士适当参与的情况下**提供需要执照的定制建议的 AI 工具。R1 v2=最高 4%，R2=最高 5%，R1 v1 已被取代，R3 无权限，优先级未决。Aster 仍需决定：来源优先级、能否显示冲突、真实权限、哪个 WSP、哪些输出属 17a-4 记录、谁运营。

**检索管道 / RAG pipeline**

- **检索增强生成 (retrieval-augmented generation, RAG)**：准备文档 → 切分段落 (chunking) → 检索相关段落 → 可选重排 (rerank) → 把选中证据放进模型输入。OpenAI 内置 **file search** 处理大部分管道；自定义管道给应用更多控制。
- 通过受控流程摄入**批准的文档快照 (approved document snapshots)**。每个可检索段落携带：

| 元数据组 Metadata group | 字段 Fields |
|---|---|
| 来源身份 Source identity | 文档 ID、权威版本 (authoritative version)、批准状态、生效与取代日期、稳定的段落 ID 或快照内偏移 (offsets) |
| 范围 Scope | 产品、预期用途、访问元数据，链接到管辖该文档的策略记录 |
| 溯源 Provenance | 到确切快照和版本的永久映射 |

- **把"最高"这类限定词和它限定的数字放在同一块里**。重叠或结构感知切分 (structure-aware chunking) 有帮助，但要检查边界：下一段的例外可能需要和声明一起走。缺少必需元数据 → 送审，不当作已批准。R2 的例子：适用性已知但权威版本和生效日未知；真实管道必须先拿到 Aster 标为必填的字段才索引；**本地占位 ID 不是版本**。

**为什么先过滤再排序 / Filter before ranking**

应用认证顾问，从**可信访问服务 (trusted access service)** 获取权限。在任何段落到达重排器或模型之前，按 **批准状态、预期用途、产品、问询日期、生效版本、访问权限** 过滤。读取段落时**再次检查授权**；权限或版本变化时**使检索和答案缓存失效或分区 (invalidate or partition caches)**。6/10：过滤移除 R1 v1（被取代）和 R3（无权限），保留 R1 v2 和 R2。

课内测验：改动后的管道把所有段落文本（含受限 R3）发给**外部重排器**，然后应用才过滤 top 结果，最终只引用 R1 v2——第一个被违反的边界？→ **R3 在授权过滤前暴露给了重排器**。"最终没引用 R3 所以没有访问失败"是错的。
→ **按请求记录每个排序组件收到了什么**，独立于最终答案。引用列表无法说明重排器看到了哪些段落；该日志本身也是敏感数据。

<svg viewBox="0 0 820 320" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="320" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Case B — Aster research assistant architecture｜Aster 研究助手架构</text>
  <g font-size="12" text-anchor="middle">
    <rect x="10" y="50" width="100" height="56" rx="6" fill="#e8f0fe" stroke="#4a6fd1"/><text x="60" y="72">Advisor query</text><text x="60" y="90">顾问发起</text>
    <rect x="125" y="50" width="115" height="56" rx="6" fill="#e8f0fe" stroke="#4a6fd1"/><text x="182" y="72">Authenticate +</text><text x="182" y="88">access service</text><text x="182" y="102">可信权限服务</text>
    <rect x="255" y="40" width="150" height="76" rx="6" fill="#fde8e8" stroke="#c33"/><text x="330" y="60">Eligibility filter</text><text x="330" y="76">approval/use/product</text><text x="330" y="92">date/version/access</text><text x="330" y="108">资格过滤(排序前)</text>
    <rect x="420" y="50" width="120" height="56" rx="6" fill="#fff" stroke="#555"/><text x="480" y="68">Hybrid retrieval</text><text x="480" y="84">keyword+semantic</text><text x="480" y="100">保留所有冲突源</text>
    <rect x="555" y="50" width="110" height="56" rx="6" fill="#fff" stroke="#555"/><text x="610" y="72">Rerank (if evals</text><text x="610" y="90">show it helps)</text>
    <rect x="680" y="50" width="130" height="56" rx="6" fill="#fff4e0" stroke="#d18a1a"/><text x="745" y="72">Model: qualified</text><text x="745" y="90">summary + claim map</text>
    <rect x="680" y="140" width="130" height="56" rx="6" fill="#fff" stroke="#555"/><text x="745" y="158">Citation check</text><text x="745" y="174">passage ID+version</text><text x="745" y="190">声明-段落核验</text>
    <rect x="510" y="140" width="150" height="56" rx="6" fill="#fff3f3" stroke="#c33"/><text x="585" y="160">Conflict / no support</text><text x="585" y="178">→ decline + route 转审</text>
    <rect x="680" y="230" width="130" height="56" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="745" y="252">Advisor reviews</text><text x="745" y="270">顾问审阅(仅内部)</text>
    <rect x="10" y="140" width="230" height="56" rx="6" fill="#eef3fd" stroke="#4a6fd1"/><text x="125" y="160">Ingest approved snapshots</text><text x="125" y="176">version, dates, passage IDs</text><text x="125" y="191">批准快照入库(缺元数据→送审)</text>
    <rect x="255" y="140" width="240" height="56" rx="6" fill="#f5f5f5" stroke="#888"/><text x="375" y="160">Per-request exposure log</text><text x="375" y="176">what each component received</text><text x="375" y="191">独立于引用列表的暴露日志</text>
    <rect x="10" y="230" width="650" height="56" rx="6" fill="#fff8ec" stroke="#d18a1a"/><text x="335" y="252">Caches: recheck access on read; invalidate/partition on permission or version change</text><text x="335" y="270">缓存：读取时复查权限；权限/版本变化时失效或分区</text>
  </g>
  <g stroke="#555" stroke-width="1.4" fill="none">
    <path d="M110 78 L125 78"/><path d="M240 78 L255 78"/><path d="M405 78 L420 78"/><path d="M540 78 L555 78"/><path d="M665 78 L680 78"/><path d="M745 106 L745 140"/><path d="M745 196 L745 230"/>
    <path d="M125 140 L300 116" stroke="#4a6fd1" stroke-dasharray="4 3"/><path d="M680 168 L660 168" stroke="#c33"/>
  </g>
</svg>

**检索选择 / Retrieval choice**：选**应用自有检索 (application-owned retrieval)**，因为 Aster 需要证明在暴露前执行了资格检查、用了哪个版本、每个组件看到了什么。托管 file search 仍是选项：支持在匹配前缩小结果的**属性过滤 (attribute filters)** 和**混合关键词+语义排序 (hybrid ranking)**；若这些过滤加你自己的日志能在同样位置给出同样保证，可以选它。
在合格集内结合关键词与语义检索，评测显示有帮助再重排。**保留每个可能冲突的来源**——排第一的段落不说明优先级。覆盖或适用性无法确立 → 拒答并转审。
反例管道：排序全部文档、把 R3 发给外部重排器、只保留 R1 v2，返回"费率 4%"+ 真实链接。三个独立检查抓三个失败：**访问 trace** 显示 R3 暴露；**声明审查**显示丢了"最高"；**冲突检查**显示 R2 消失。更好的链接一个都修不了。

**可核查的引用 / Checkable citation**：标识**确切段落和来源版本**；声明级审查再问该段落是否真正支撑声明（含限定）。R1 v2 支撑"R1 version 2 states a maximum of 4%"，**不支撑**"The fee is 4%"；生产中引用带权威段落 ID 或偏移。R2 在程序中用本地快照 ID，真实引用需 Aster 的段落 ID、版本、生效日。

**边界测试脚本 / Boundary test (`aster_retrieval_eval.py`)**

```python
# Condensed from the lesson fixture: eligibility before exposure, then separate grades
DATE = "2026-06-10"
ENTITLEMENTS = {"R1", "R2"}  # trusted exercise input, not authentication
SUPPORTED = {"R1-v2": {"R1 version 2 states a maximum of 4%."}}


def eligible(doc):
    # In production, missing metadata must never default to eligible
    return (doc["doc"] in ENTITLEMENTS and doc["approved"] is True
            and doc["scope"] is True
            and (doc["start"] is None or doc["start"] <= DATE)
            and (doc["end"] is None or DATE < doc["end"]))  # exclusive end drops R1-v1


def grade(kind, result):
    trace = result.get("trace")
    complete = result.get("complete") is True and isinstance(trace, list)
    access = complete and set(trace) == {"R1-v2", "R2-fixture"}
    expected_route = "answer" if kind == "direct" else "review"
    route = result.get("route") == expected_route
    claim, ref = result.get("claim"), result.get("ref")
    if expected_route == "answer":
        citation = ref in (trace or []) and claim in SUPPORTED.get(ref, set())
    else:
        citation = claim is None and ref is None
    return {"complete": complete, "access": access, "route": route, "citation": citation}
```

```text
Scripted replay with injected faults (not production measurements):
direct:   10/12 pass   (2 injected "The fee is 4%." claims fail citation support)
conflict:  2/4  pass   (2 answer instead of routing to review)
access:    3/4  pass   (1 trace includes R3-fixture -> exposure)
overall:  15/20        (least useful number)
```

可选 `--live`：Responses API + `gpt-6-luna`，`store=False`，只发合格段落的 ID 和文本，要求"不决定哪份优先，保留限定"，输出标为 **UNTRUSTED**，从不驱动评分或顾问答案。字符串精确匹配只适用于固定声明，不能评判任意模型文本；trace 是模拟的，不是独立埋点。

**与合规共建评测集 / Building the eval set with compliance**

- 顾问和合规一起写用例，来自去除客户细节的真实问询；**调参 (tuning)前先分出开发集和 holdout 集**。
- 用例卡：问询与截至日期、请求顾问及其权限决定、适用快照与版本、期望路由（answer / conflict / decline）及声明-段落映射、每位审核者的理由。
- **确定性部分用代码评分**：访问、引用身份、路由、trace 完整性。缺权限记录或缺 trace = **不完整，绝不算通过**。
- **声明支撑需要人**：审核者独立评共享样例、记录分歧、未决的交给具名负责人。**模型评分器 (model grader)** 在对照专家判断校准后可以辅助；持续检查它与专家的分歧和漂移 (drift)。**安全切片 (safety slices：access、conflict) 与能力切片 (capability slices：direct answers) 分开报告**。

**结果含义 / What results mean**：单个受限暴露和两个漏冲突路由**各自**就足以阻断广泛发布。手选用例不估计生产比率。direct 切片只说明值得对更窄的**报告特定模式 (report-specific mode)** 继续离线测试。审核试点仍需修复的控制、代表性 holdout、批准的工作流、具名负责人。**缺失重排器日志是调查理由，绝不是访问守住的证据**。

**成本与延迟 / Cost & latency**

```text
Latency (nearest-rank p95): 20 recorded end-to-end durations, sorted
  position = 0.95 x 20 = 19  -> p95 = 19th value = 1.8 s
  (record per-stage durations too; summing component p95s != end-to-end p95)

Unit cost (assumed $2 / 1M input tokens, $8 / 1M output tokens):
  input   6,000 x $2 / 1,000,000 = $0.012
  output    500 x $8 / 1,000,000 = $0.004
  retrieval                      = $0.004
  per task                       = $0.020
  4,000 tasks/month x $0.020     = $80  (before infra, review time, other costs)
```

每个缓存 (caching)、索引 (indexing)、重排改动都要过同样的权限、新鲜度、冲突、引用检查。**更便宜更快但泄露段落或隐藏冲突的请求 = 设计失败**。

**面试怎么说 / How to say it in the interview**

- Q: "Trace the June 10 request from authorization through the answer."
  - EN: "The application authenticates the advisor and gets entitlements from a trusted access service, then filters by approval, use, product, date, version, and access before anything is ranked. R1 version 1 and R3 stay out; R1 version 2 and R2 stay in, and retrieval keeps both. The claim map preserves the 4% and 5% maximums with exact passage IDs. The open conflict goes to the source owner, and showing both passages needs Aster's approval."
  - 中文：认证 → 排序前过滤 → 保留冲突 → 声明映射 → 转审。
- Q: "The final answer only cites R1 v2. Was there an access failure?"
  - EN: "Possibly, and the citation list can't tell us. If the pipeline sent R3 to an external reranker before filtering, the boundary broke at that hand-off. That's why I log per request what each ranking component received, independently of the final answer."
  - 中文：引用列表不能证明重排器看到了什么。
- Q: "The sponsor wants to launch on 15 of 20. What changes?"
  - EN: "Nothing goes to advisors yet. One restricted exposure and two missed conflict routes are separate blockers. I'd fix those boundaries, run access and routing regressions plus a held-out representative set, and calibrate claim-support grading with advisors and compliance. A report-specific mode can be tested offline; a reviewed pilot also needs an approved workflow, records decisions, and named operators."
  - 中文：分切片看，安全切片任一失败即阻断。
- Q: "Why application-owned retrieval instead of managed file search?"
  - EN: "Aster needs to prove eligibility was enforced before exposure, which version was used, and what each component saw. Managed file search has attribute filters and hybrid ranking, so if those filters plus our own logging give the same guarantees at the same points, it's a fine choice. The requirement drives the choice, not the tool."
  - 中文：需求决定工具，关键是可证明的边界。
- Q: "How do you grade claim support?"
  - EN: "Deterministic checks — access, citation identity, route, trace completeness — run in code, and missing records count as incomplete. Claim support needs experts grading independently with disagreements recorded; a model grader can help only after calibration against those experts, and I'd keep monitoring disagreement and drift. Safety slices are reported separately from capability slices."
  - 中文：代码管确定性，人管语义，模型评分器需校准。
- Q: "What evidence would you hand over?"
  - EN: "Source and entitlement decisions, per-request exposure logs, claim mappings, slice denominators, reviewer disagreements, repair and holdout results, cost and latency assumptions — and the open source-precedence, records, and ownership decisions, clearly marked as open."
  - 中文：交接证据要完整且标明未决项。

---

## 16. When the Evals Disagree With the Customer｜当评测结果与客户意见不一致

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/when-the-evals-disagree-with-the-customer

**要点 / Key ideas**

- 场景：Aster 发起人 (sponsor) 想给 **6 名顾问、30 个请求**上线，理由是 15/20 通过、$0.020/任务。说"不"很容易；面试官看的是**对这次上线说不，同时给出发起人能接受的下一步**。
- **更小的受众不能修复访问失败**：哪怕一个顾问也可能看到无权看的段落。

**证据拆解 / What the evidence says**

| 切片 Slice | 结果 Result | 含义 Meaning |
|---|---|---|
| 直接答案 Direct answers | 10/12 | 支持探索报告特定草稿模式，但仍有 2 个失败 |
| 冲突路由 Conflict routes | 2/4 | 2 个失败隐藏了顾问需要看到或需审核的合格分歧 |
| 受限访问 Restricted access | 3/4 | 失败用例：受限材料在过滤前到达**外部重排器** |
| 缓存撤销 Cache revocation（独立 6 例检查） | 1/6 失败 | 顾问权限**被撤销后**仍收到一个受保护段落——不同测试、不同边界 |

前三项合计 15/20；缓存检查不在该分母中。总数掩盖了两个关键问题：受限材料是否越界？冲突是否被正确处理？
**人工审核答案发生在两个暴露点之后**：重排器已收到受限内容；顾问已看到被撤销的段落。真实引用本身不能证明声明有支撑、是当前的、对读者许可。

<svg viewBox="0 0 820 220" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="220" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Two separate access failures, both before human review｜两处独立访问失败，均早于人工审核</text>
  <g font-size="12" text-anchor="middle">
    <rect x="10" y="60" width="120" height="56" rx="6" fill="#e8f0fe" stroke="#4a6fd1"/><text x="70" y="82">Advisor request</text><text x="70" y="100">顾问请求</text>
    <rect x="150" y="60" width="140" height="56" rx="6" fill="#fde8e8" stroke="#c33"/><text x="220" y="80">External reranker</text><text x="220" y="96">got R3 before filter</text><text x="220" y="110">过滤前暴露</text>
    <rect x="310" y="60" width="120" height="56" rx="6" fill="#fff" stroke="#555"/><text x="370" y="82">Eligibility filter</text><text x="370" y="100">(too late 太晚)</text>
    <rect x="450" y="60" width="120" height="56" rx="6" fill="#fff4e0" stroke="#d18a1a"/><text x="510" y="82">Model answer</text><text x="510" y="100">模型回答</text>
    <rect x="590" y="60" width="100" height="56" rx="6" fill="#fde8e8" stroke="#c33"/><text x="640" y="80">Stale cache</text><text x="640" y="96">revoked passage</text><text x="640" y="110">撤销后仍返回</text>
    <rect x="710" y="60" width="100" height="56" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="760" y="82">Human review</text><text x="760" y="100">人工审核</text>
    <rect x="150" y="150" width="540" height="50" rx="6" fill="#f5f5f5" stroke="#888"/><text x="420" y="170">Fix: filter before any ranking/model; recheck on cache read; invalidate/partition caches</text><text x="420" y="188">修复：排序前过滤；读缓存复查权限；变更时使缓存失效</text>
  </g>
  <g stroke="#555" stroke-width="1.4" fill="none"><path d="M130 88 L150 88"/><path d="M290 88 L310 88"/><path d="M430 88 L450 88"/><path d="M570 88 L590 88"/><path d="M690 88 L710 88"/></g>
</svg>

**冲突切片 / Conflict slice**：R1 v2 最高 4%、R2 最高 5%；优先级和能否显示冲突未决。R2 适用但缺权威版本和生效日，本地 ID 不能替代。Aster 允许显示冲突且提供元数据后：展示两条带段落的限定性报告特定声明并转审；在此之前：拒答并转审，不暴露 R3。

**弱答案**："15/20 够做内部试用；权限变化后保留缓存以保持速度；顾问会发现错误。""一个顾问看到了段落，但群体小、链接可审计。"——用已知泄露换速度；**展示后审核无法撤销泄露**；小受众减少可能看到的人数但不修复缺陷。

**更窄的有条件 yes / A narrower conditional yes**：对发起人说："I recommend no advisor exposure yet. We keep protected-data paths off while we fix and retest access enforcement and cache handling. In parallel, we use sanitized offline cases to test a narrower report-specific workflow." Aster 的研究目标仍是目标；暴露等待证据和决定。

**有条件试点的四条边界 / Conditional pilot boundaries**（条件满足后：顾问发起、关于顾问指定的某份报告的内部研究草稿；规模和请求上限在门槛满足后再约定）

| 边界 Boundary | 内容 Content |
|---|---|
| 证据 Evidence | 合格、批准的来源版本，每个声明附支撑段落 |
| 审核 Review | 顾问有时间、证据、权限审核或拒绝草稿；**被动点击不算审核** |
| 拒答 Declining | 权限、元数据、声明支撑、冲突处理任一未决 → 拒答并转审 |
| 排除 Exclusions | 无个性化客户建议、客户消息、组合变更、交易 |

OpenAI 使用政策（金融与信贷中高风险动作需人工审核）本身**不决定** Aster 内部工作流是否被授权——Aster 自己的义务决定：FINRA 3110 的 WSP 覆盖、合规按 17a-4 决定保存哪些提示和输出。章程承诺解释判断的精神，但**不授予任何具体部署的许可**。

**暴露前的证据序列 / Evidence before exposure**

| 步骤 Step | 内容 Content |
|---|---|
| 修复边界 Fix | 权限与来源资格在段落到达重排器或模型前执行；读缓存时复查；权限/版本变化时使缓存失效或分区 |
| 复现失败 Reproduce | 重跑受限重排用例、撤销用例、漏掉的冲突路由；捕获**独立于引用列表**的每请求排序输入与访问决定日志 |
| holdout 集 Held-out | 修复后跑开发中未用的代表性集合；**看结果前**约定用例与阈值：0 未授权暴露、安全切片 0 漏冲突路由、日志完整、无严重回归 |
| 审核含义 Review meaning | 顾问与合规独立检查声明支撑、保留的限定、拒答、分歧；记录未决判断与裁决人 |
| 批准与交接 Approve & hand over | 工作流与记录决定、具名运营与审核负责人到位后才让顾问使用 |

小集合通过是门槛的必要条件，不是生产安全证明。日志缺失 = 不完整，不是通过。

**成本/延迟压力**：p95 = 1.8s（20 个样本最近秩 (nearest rank)第 19 个）描述的是**当前路径不是修复后路径**；$0.020/任务、4,000 × $0.020 = $80/月，未含审核时间和基础设施。在同一负载上比较方案，知道运营成本后再加上。

**交接包 / Handoff package**：发布门槛放在**版本化应用代码**中——版本化用例与执行日志；访问、引用身份、路由、trace 的代码检查；带分歧记录的校准语义评分；回归 (regression)结果、不完整证据、门槛退出状态。上节重放程序只**模拟** trace，生产组件需要自己的埋点 (instrumentation)。OpenAI 已弃用 (deprecated)托管 Evals 平台并安排关停——又一个理由。
负责人（都未接受）：来源负责人（优先级或路由、是否允许显示冲突）；访问、合规、记录负责人（权限、WSP、保存哪些记录）；客户工程（访问执行、监控、事件响应 incident response、关停 shutdown、技术支持）；顾问审核负责人（有意义的审核、升级、助手拒答或关闭时可用的兜底）。
**停止条件 (stop conditions)**：任何未授权暴露、漏冲突路由、缺访问或排序日志、无可用审核者。只有 Aster 同意配置时才回退 (fall back)人工流程。

**示例自评**：六项都 2 分（客户框定、归属、技术推理、证据、安全、沟通）——不加总。

**面试怎么说 / How to say it in the interview**

- Q: "The sponsor wants to launch to six advisors for 30 requests on 15 of 20 and $0.020 per task. What's your decision?"
  - EN: "I'd keep the assistant offline for now. The replay passed 10 of 12 direct cases, 2 of 4 conflict routes, and 3 of 4 restricted-access cases, and a separate six-case revocation test served one protected passage after access was revoked. I'd fix pre-ranking and cache controls, reproduce the failures, and run a representative held-out set with independent exposure logs and expert review. If that passes and Aster approves the workflow and names operating and review owners, we can run a report-specific, advisor-reviewed internal pilot."
  - 中文：先给决定，再拆证据，再给可接受的下一步。
- Q: "Fifteen out of 20 passed. Why not let six advisors check the links?"
  - EN: "A smaller audience doesn't fix an access failure — even one advisor could see a passage they aren't entitled to, and reviewing after display can't undo that. The two failures that matter are a restricted passage reaching the reranker and a revoked passage served from cache; the aggregate hides both."
  - 中文：小规模不修复泄露；总分掩盖关键失败。
- Q: "The sponsor needs faster responses. Remove the cache access check."
  - EN: "I'd keep it. The revocation test shows why: a cached passage reached an advisor after their entitlement changed. I'd compare cache invalidation, partitioning, and reranking options against the same entitlement, freshness, conflict, and claim-support checks."
  - 中文：性能优化必须过同样的安全检查。
- Q: "What if Aster lets the assistant show the R1 and R2 conflict?"
  - EN: "That settles the display question, not precedence, and not R2's missing version and effective date. Once eligibility and metadata are in place, the assistant can show both report-specific claims with their passages and route the disagreement. Until then, it declines and routes — and today's no-exposure decision still stands because of the access failures."
  - 中文：显示决定改变响应路径，但不改变"暂不暴露"。
- Q: "The sponsor accepts the risk. Can you launch?"
  - EN: "I understand the urgency, but the sponsor can't sign off for the access owner, for compliance's supervision and records decisions, or for evidence we don't have yet. I'd keep the path offline and get those owners in a room this week to agree on the fix and the acceptance criteria."
  - 中文：发起人无权代替各负责人签字；推动决策流程。
- Q: "Who can stop the pilot?"
  - EN: "That has to be agreed before any pilot: a named owner, likely in customer engineering with the advisor review lead, who can shut it off on an unauthorized exposure, a missed conflict route, missing access or ranking logs, or no available reviewer — with a staffed manual fallback."
  - 中文：事先约定停止条件与停止权。

---

## Case C｜案例 C：Lakeside 医院临床病历起草 (Clinical Note Drafting)

## 17. The Customer Brief｜客户简报

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/the-customer-brief-xVB6Qvkwp5l

**要点 / Key ideas**

- 临床病历 (clinical note) 是**病历记录 (medical record)** 的一部分，其他临床人员据此理解就诊并做后续诊疗决定。流畅的草稿可能写出**没人说过的发现**——最诱人也最容易出错的医疗用例。本案例考数据、安全、何时说不。

**Problem statement (EN)**

> Lakeside Hospital Network is a US hospital network. Clinicians document each encounter in the hospital record after the visit, typing or dictating the note themselves. A clinical sponsor wants to cut that documentation burden by turning encounter material into draft notes, and asks whether drafts can be filed automatically to save more time. Lakeside has no measurement of current documentation time or expected savings. In 14 sample notes (current format), 3 have no allergy-status section. In a separate demo of 5 drafts from test encounters, one encounter had no allergy history, yet its draft said "No known medication allergies."

- 时间节省是**要测量的目标，不是结果**。
- 受影响的三类人：**临床医生 (clinicians)** 写并签署病历、为内容负责；**患者 (patients)** 话语被采集、信息流经新系统、后续诊疗依赖病历；**病历的其他读者 (other readers)**——护士、专科医生、值班人员——不知道病历如何起草就据此行动。
- 与研究助手相比风险**性质不同**：研究备忘中的无支撑句浪费顾问时间；已归档病历中的无支撑句可能**改变后续治疗决定**。

**谁决定什么 / Who decides what**

| 角色 Role | 决定 Decides |
|---|---|
| 临床领导 Clinical leadership | 预期用途、谁审核草稿、谁可以归档 (file) |
| 隐私与法务 Privacy & legal | 法律与医院政策允许怎样录音、处理、共享患者数据 |
| 安全与工程 Security & engineering | 访问、与病历系统集成、服务运行 |
| 运营 Operations | 日常支持工作流、处理故障、**能关闭它** |

命名角色给每个未决问题一个去处，**不代表任何人已同意**。

**14 条样本解读（课内测验）**：最强支撑——**"部分现行格式病历缺少过敏状态；样本不给出患者发现也不给出比率。"** 错误：三次就诊有未记录的药物过敏；约 3/14 病历不安全；助手在 3/14 草稿中遗漏（这些病历不是助手写的）。

**范围 / Scope**：助手从就诊材料准备**草稿**，授权临床医生审核、修改或拒绝，并决定是否归档。**排除：诊断 (diagnosis)、开药 (prescribing)、自动归档 (automatic filing)**（文本在任何临床医生判断正确前就进入记录）。OpenAI 使用政策禁止在无持牌专业人士适当参与时提供需执照的定制建议，也禁止声称或暗示 AI 本身持有专业资质。界面旁写着医生名字不够——**医生必须能对草稿采取行动**。

**演示失败 / Demo failure**："No known medication allergies" 读起来像临床发现但与来源不符——**缺少过敏史 ≠ 无已知过敏的证据**；信任它的医生可能开出患者会过敏的药。1/5 手选草稿不是错误率，而是**具体的失败模式**；语法完美，表面毫无信号。

**自动归档改变了什么 / What automatic filing changes**

| 路径 Path | 过敏句的命运 Fate of the allergy line |
|---|---|
| 医生审核 Clinician-reviewed | 医生并排看来源与草稿，发现无支撑声明，删除，再决定是否归档 |
| 自动归档 Automatic | 直接进入医院记录；旁边"AI 草稿"标签，但虚假陈述已成为记录一部分，纠正前读到的人可能据此行动 |

**更早的边界**：录音或发送给转写/模型服务发生在医生看到草稿之前——归档前的审核**无法撤销**未经许可的录音或披露 (disclosure)。因此需要两个独立控制：① 隐私与法务批准实际工作流的录音和处理；② 临床领导提供有来源访问、时间、权限（修改、拒绝、归档）的审核者。**一个批准按钮两者都证明不了**。

<svg viewBox="0 0 820 230" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="230" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Reviewed drafting vs automatic filing｜审核起草 vs 自动归档</text>
  <g font-size="12" text-anchor="middle">
    <rect x="10" y="80" width="120" height="60" rx="6" fill="#fde8e8" stroke="#c33"/><text x="70" y="102">Recording approval</text><text x="70" y="120">录音批准(更早边界)</text>
    <rect x="150" y="80" width="110" height="60" rx="6" fill="#fff" stroke="#555"/><text x="205" y="102">Draft: "No known</text><text x="205" y="120">med allergies"</text>
    <rect x="290" y="40" width="160" height="56" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="370" y="60">Clinician + source view</text><text x="370" y="78">医生对照来源审核</text>
    <rect x="480" y="40" width="150" height="56" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="555" y="60">Remove / reject</text><text x="555" y="78">删除或拒绝</text>
    <rect x="660" y="40" width="150" height="56" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="735" y="60">File exact version</text><text x="735" y="78">归档已审版本</text>
    <rect x="290" y="130" width="160" height="56" rx="6" fill="#fde8e8" stroke="#c33"/><text x="370" y="150">Auto-file + "AI" label</text><text x="370" y="168">自动归档+标签</text>
    <rect x="480" y="130" width="330" height="56" rx="6" fill="#fff3f3" stroke="#c33"/><text x="645" y="150">False finding already in record; readers may act</text><text x="645" y="168">虚假发现已入病历，纠正前可能被采信</text>
  </g>
  <g stroke="#555" stroke-width="1.4" fill="none"><path d="M130 110 L150 110"/><path d="M260 100 L290 70"/><path d="M450 68 L480 68"/><path d="M630 68 L660 68"/><path d="M260 120 L290 158" stroke="#c33"/><path d="M450 158 L480 158" stroke="#c33"/></g>
</svg>

**适用的健康数据规则 / HIPAA basics**（FDE 要知道基本形态，但不扮演医院律师）

- 能识别患者的就诊音频、转写稿、草稿病历都是**受保护健康信息 (protected health information, PHI)**。

| 要点 Point | 内容 Content |
|---|---|
| 业务伙伴 Business associates | 代 Lakeside 创建、接收、存储、传输 PHI 的供应商是业务伙伴；披露 PHI 前需签**业务伙伴协议 (business associate agreement, BAA)**——转写服务、模型提供方、任何看到就诊内容的日志或备份供应商 |
| OpenAI 的 BAA | 与符合条件的 API 客户签署；**只覆盖特定合格端点和功能**，不是整个平台（如带实时联网的 web search 不覆盖） |
| 治疗用途 Treatment use | HIPAA 允许提供者为**治疗与医疗运营 (treatment and health care operations)** 使用和披露 PHI，无需单独患者授权；本项目的关卡是 BAA、医院政策、每条数据流的控制 |
| 录音 Recording | **HIPAA 不决定能否录音**——由州录音法决定，部分州要求**所有方同意 (every party's consent)**；法务决定；设计必须支持患者说不 |

- 产品规则同向：使用政策禁止在医疗等敏感领域无人工审核地自动化高风险动作；禁止未经授权聚合、监控、画像 (profiling)或分发私人敏感信息。
- **不训练承诺回答的是另一个问题**：API 数据默认不用于训练，但这不说明 Lakeside 能否录音或发给供应商。
- 章程：用部署影响力追求广泛收益、避免伤害——保护患者和医生的权威，同时让工具有用。

**今天的决定 / Today's decision**：只在**测试数据**上做发现。在 Lakeside 决定谁能批准录音与处理、签好每条数据流需要的协议、指定有真实权限的审核者、分配运营者之前，**不处理患者数据、不做临床试点**。医生审核起草保留；**拒绝自动归档，包括加"AI 草稿"标签的版本**——标签不改变进入记录的内容。

**面试怎么说 / How to say it in the interview**

- Q: "Give me your recommendation." (sponsor wants auto-filing)
  - EN: "Lakeside's clinicians spend too long on documentation, and a wrong sentence in a filed note can change later care. I'd start discovery on test data now. Clinician-reviewed drafting is the scope we work toward; diagnosis, prescribing, and automatic filing are out. Three of 14 sample notes have no allergy section, and separately one of five demo drafts said 'no known medication allergies' when the encounter had no allergy history — neither number measures time saved or production quality. Clinical leadership names who reviews and files; privacy and legal decide on recording, the BAAs each vendor needs, and patient refusal; security, engineering, and operations take the technical and on-call work. None of them has signed up yet."
  - 中文：测试数据上推进；审核起草是方向；自动归档排除；各方负责人未确认。
- Q: "Why not file notes with an 'AI draft' label and let clinicians fix them later?"
  - EN: "Because the false sentence is in the record the moment it's filed, and anyone who reads it before the correction may act on it. A label describes the risk; it doesn't prevent it. The control has to be a clinician deciding before anything is written."
  - 中文：标签不是控制。
- Q: "We promise the data won't be used for training. Can we start recording?"
  - EN: "No training is the default for API data, but it doesn't tell us whether Lakeside may record this visit, which vendors need a BAA, or what happens when a patient declines. Let's keep working on test encounters while your privacy team decides those."
  - 中文：不训练 ≠ 录音许可。
- Q: "Does HIPAA require patient consent to record?"
  - EN: "Not by itself — HIPAA permits use for treatment and operations without separate authorization. Whether a visit may be recorded is set by state recording laws and hospital policy, and some states require every party's consent. Lakeside's counsel decides; my design has to support a patient who says no."
  - 中文：区分 HIPAA 与州录音法。

---

## 18. Mapping Data Flows and Consent｜绘制数据流与同意

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/mapping-data-flows-and-consent

**要点 / Key ideas**

- "患者数据去哪了？"在 FDE 面试中是**你的**问题。录音在医生看到草稿前就创建了就诊副本；拟议流程还产生转写稿、模型请求、响应，以及几乎"意外"产生的**诊断日志 (diagnostic logs) 和备份 (backups)**。每份副本需要：目的、谁能读、保留规则 (retention rules)、覆盖它的协议。
- **录音、转写、发送文本给模型服务、归档是四个独立决定**。末端的审核按钮不能授权前面任何一个。
- **数据流清单 (data-flow inventory)**：列出信息被发送、处理、存储的每个地方，**包括为支持和恢复做的副本**。每个节点记录：数据、目的、服务与位置、访问者、保留期、批准人、负责人。未选定服务的写"未决 (unresolved)"，不猜保留期。

**清单 / Inventory（均未批准）**

| 节点 Node | 目的与要点 Purpose & notes |
|---|---|
| 采集设备 Capture device | 录制音频；问题：设备、本地缓存 (local cache)、删除、谁能批准录音 |
| 录音存储 Recording storage | 供转写/审核；服务、位置、保留、备份未决 |
| 转写 Transcription | 外部供应商 = 业务伙伴，**收到任何音频前需 BAA** |
| 就诊文本选择 Encounter-text selection | 应用挑选草稿所需转写文本——**最小必要原则 (minimum necessary) 在这里变成代码**：发送本次就诊，不发整份病历 |
| Responses 请求与响应 | 端点、模型、项目、区域、存储设置、OpenAI BAA 都记在这行 |
| 可选工具与历史 Optional tools & history | 远程 MCP 服务器、托管容器、会话状态各增加一个接收者或存储副本；首版**关闭**，直到各自有清单条目 |
| 审核界面 Review interface | 草稿与来源并排，每句链接支撑文本；本地缓存与访问控制也要条目 |
| 归档目的地 Filing destination | 医生归档后进入病历系统；临床领导指定谁能归档；工程梳理集成与中间副本；自动归档不在范围 |
| 追踪与支持日志 Traces & support logs | 只应含标识符、时间、状态，**绝不含就诊文本**；限工程与支持人员 |
| 备份 Backups | 录音、转写、应用数据、日志的恢复副本；各需位置、操作员访问、保留、删除程序 |

节点之间的传输和节点同样重要。少发给模型的文本减少离开应用的内容，但**对已存在的音频和转写副本无效**。

<svg viewBox="0 0 820 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="300" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Case C — Lakeside data flow &amp; decision points｜数据流与决策点</text>
  <g font-size="12" text-anchor="middle">
    <rect x="10" y="60" width="100" height="56" rx="6" fill="#e8f0fe" stroke="#4a6fd1"/><text x="60" y="82">Capture</text><text x="60" y="100">采集音频</text>
    <rect x="125" y="60" width="100" height="56" rx="6" fill="#fff" stroke="#555"/><text x="175" y="82">Recording</text><text x="175" y="100">store 录音存储</text>
    <rect x="240" y="60" width="110" height="56" rx="6" fill="#fff" stroke="#555"/><text x="295" y="78">Transcription</text><text x="295" y="94">vendor (BAA)</text><text x="295" y="108">转写</text>
    <rect x="365" y="60" width="115" height="56" rx="6" fill="#fff8ec" stroke="#d18a1a"/><text x="422" y="78">Text selection</text><text x="422" y="94">minimum necessary</text><text x="422" y="108">最小必要</text>
    <rect x="495" y="60" width="115" height="56" rx="6" fill="#fff4e0" stroke="#d18a1a"/><text x="552" y="78">Responses API</text><text x="552" y="94">store=false, BAA,</text><text x="552" y="108">region</text>
    <rect x="625" y="60" width="90" height="56" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="670" y="82">Review UI</text><text x="670" y="100">医生审核</text>
    <rect x="730" y="60" width="80" height="56" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="770" y="82">Record</text><text x="770" y="100">归档</text>
    <g fill="#c33" font-weight="bold"><text x="60" y="50">D1 record?</text><text x="295" y="50">D2 transcribe?</text><text x="552" y="50">D3 send?</text><text x="770" y="50">D4 file?</text></g>
    <rect x="125" y="160" width="350" height="50" rx="6" fill="#fde8e8" stroke="#c33"/><text x="300" y="180">Traces/support logs: 3/12 contain excerpts (L1–L3)</text><text x="300" y="197">日志字段泄露就诊摘录 → fix field, retest</text>
    <rect x="495" y="160" width="315" height="50" rx="6" fill="#fde8e8" stroke="#c33"/><text x="652" y="180">Backups: B1, B2 copy two leaked records</text><text x="652" y="197">备份继承泄露 → 访问/删除决定</text>
    <rect x="10" y="235" width="800" height="50" rx="6" fill="#f5f5f5" stroke="#888"/><text x="410" y="255">Patient declines before capture → no recording, manual documentation; withdraws mid-way → stop, privacy team decides</text><text x="410" y="272">患者拒绝 → 不录不发，人工记录；中途撤回 → 停止并交隐私团队决定</text>
  </g>
  <g stroke="#555" stroke-width="1.4" fill="none">
    <path d="M110 88 L125 88"/><path d="M225 88 L240 88"/><path d="M350 88 L365 88"/><path d="M480 88 L495 88"/><path d="M610 88 L625 88"/><path d="M715 88 L730 88"/>
    <path d="M300 116 L300 160" stroke-dasharray="4 3"/><path d="M552 116 L552 160" stroke-dasharray="4 3"/><path d="M475 185 L495 185"/>
  </g>
</svg>

**诊断副本的发现 / Diagnostic copies finding**：工程检查 12 条测试 trace 记录，**3 个本应放诊断元数据的支持日志字段含就诊摘录**（L1–L3），其中 **2 条也出现在备份中**（B1、B2）。排障 (troubleshooting)不需要摘录 → 字段把 PHI 泄露到无人规划的存储中；备份继承泄露，需要各自的访问和删除决定。**这是健康数据从设计良好的系统中逃逸最常见的方式：某人调试时写的一行日志。**

课内测验：发起人 (sponsor)提议在 Responses 请求上设 `store=false` 然后开始录音 → 正确答案：**Responses 存储行为改变，但日志和备份副本仍在。修复诊断字段、找到并处理副本、重跑检查。** `store=false` 只改变 OpenAI 为该 Responses 请求保留什么，**从不触及 Lakeside 自己的日志或备份**，也不提供录音授权，也不证明每个节点零保留。

**同意与录音 / Consent & recording**：录音同意与 HIPAA 是**两个问题**（候选人常混为一谈）。

| 情形 Situation | 处理 Handling |
|---|---|
| 无批准，或患者在采集前拒绝 | 不录音，不经起草流程发送任何就诊材料；医生按现有人工方式记录 |
| 录音开始后患者撤回 | 停止录音；已有材料交 Lakeside 隐私团队决定，**不在代码里发明删除或重用规则** |
| 有人提议其他路径（打字转写、换供应商、换模型） | 视为**新数据流**，需单独批准；绝不对拒绝的患者悄悄替换 |

人工路径很重要：患者的拒绝不应以接受另一条自动化路径为条件；Lakeside 必须在接触任何真实就诊前培训员工使用兜底 (fallback)流程。

**协议与控制对照 / Controls per copy**（把实际设置或协议写在它覆盖的端点、项目、区域或供应商旁边——"AI 系统符合 HIPAA"什么都没覆盖）

| 控制 Control | 作用 What it does | 不做什么 Limits |
|---|---|---|
| BAA | 每个接触 PHI 的供应商各一份 | OpenAI BAA 只覆盖合格 API 端点/功能，清单需证明路径上每个调用都在列表上 |
| 模型训练 No training | API 数据默认不用于训练/改进，除非客户选择加入 | 不授予录音或披露许可 |
| Responses 存储 | 默认保留应用状态 **30 天**；`store=false` 改变该请求 | 不影响 Lakeside 日志/备份；background mode 等功能有自己的存储行为 |
| 滥用监控 Abuse monitoring | 与应用状态分开；默认可能含客户内容，保留**最多 30 天**（法律要求或防止伤害时更久） | — |
| 零数据保留 Zero Data Retention (ZDR) | 需 OpenAI **事先批准**并接受额外要求；在文档限制内让客户内容不进入滥用监控日志，Responses 视 store 为 false | 不合格的功能仍可能存储应用状态 |
| 数据驻留 Data residency | 支持的端点/模型：需持久化的客户内容静态存储在项目所选区域，区域支持时推理也在该区域 | 系统数据另有限制；不覆盖 Lakeside 自己的基础设施或其他供应商 |
| 工具 Tools | 远程 MCP 服务器是有自己保留策略的第三方；托管工具容器可能写临时状态 | 此路径中关闭 |
| 访问与加密 Access & encryption | 每个存储与传输列出谁能读/管理、谁持有密钥；HIPAA 安全规则 (Security Rule) 期望这些保障 | 降低暴露，但不授予录音权 |

配对练习答案：项目驻留配置 → 支持的持久内容存在哪、是否有区域处理；Lakeside 隐私/法务/临床决定 → 谁能授权录音、拒绝与撤回如何处理；API 不训练条款 → API 数据是否用于训练；客户备份清单与删除责任 → 谁控制/保留/删除 B1、B2；`store=false` → OpenAI 是否保留 Responses 请求的应用状态。**没有单一一行能放行整个工作流**（例如驻留把 OpenAI 项目钉在一个区域，而 Lakeside 的备份在别处）。

**审核医生需要什么 / What the reviewer needs**：来源与草稿并排，每句链接支撑它的来源文本；**可见的缺口**——界面标出无支撑来源的陈述、显示来源沉默之处；足够时间 + 修改、拒绝、决定归档的权限。过敏句在界面上应显示为**空引用 (empty citation)**。只看到流畅草稿的审核者分不清捏造与记录；看到来源但没时间或权限拒绝的审核者也一样。

**未决决定的归属**：隐私与法务（录音规则、各供应商 BAA、拒绝与撤回处理）；临床领导（具名审核者、来源访问、审核时间、归档权）；安全与工程（确切服务与设置、访问限制、副本清单、诊断字段修复、重测）；运营（支持、备份、事件响应 (incident response)、人工兜底、**停止工作流的权限**）。都是提议。

**面试怎么说 / How to say it in the interview**

- Q: "Defend your recommendation." (data-flow handoff)
  - EN: "Lakeside wants to reduce documentation time, but recording creates PHI before anyone reviews a draft. I'd keep discovery on test data. The build sends selected transcript text — minimum necessary — for a clinician-reviewed draft and never files automatically. In 12 test traces, three diagnostic fields contain encounter excerpts and two of those records are also in a backup; I'd stop writing content to that field, find and handle the existing copies, and rerun the inspection. Privacy and legal decide on recording and sign BAAs with each vendor, OpenAI included, and clinical leadership, engineering, security, and operations each take their part."
  - 中文：录音即产生 PHI；修日志字段、处理副本、重测；各方各司其职。
- Q: "We have store=false and a no-training statement. Why not start recording?"
  - EN: "store=false changes what OpenAI keeps for that Responses request, and no-training covers model training. Neither touches Lakeside's own logs and backups — three trace records and two backup copies already hold excerpts — and neither decides who may approve recording under state law and hospital policy."
  - 中文：模型侧设置管不了客户自己的副本，也不是录音授权。
- Q: "The patient declines recording. What happens, and how does a clinician review the allergy statement?"
  - EN: "We don't record or send anything through the workflow; the clinician documents manually. For an approved future draft, the clinician sees source and draft together. The source has no allergy history, so the allergy sentence shows up with no supporting link, and the clinician removes it or rejects the draft."
  - 中文：拒绝走人工；审核界面让空引用可见。
- Q: "Is the system HIPAA compliant?"
  - EN: "I'd avoid that blanket phrase. I'd show an inventory where every copy — capture, storage, transcript, model request, logs, backups — has its purpose, access, retention, agreement, and owner, with each OpenAI call on the BAA-eligible list. Compliance is a property of that whole map plus Lakeside's decisions, not of one setting."
  - 中文：合规是整张数据流图的属性。

---

## 19. Designing for Clinical Safety｜为临床安全而设计

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/designing-for-clinical-safety

**要点 / Key ideas**

- 草稿安全**不是因为它引用了来源**——引用可能直接指向说相反话的句子。安全来自三个设计选择共同作用：① 每个声明绑定到来源文本 (claims tied to source)；② 医生批准**一个确切版本**后才能归档 (version-bound approval)；③ 评测专门查**遗漏和捏造的发现** (omissions and invented findings)。

**来源与声明 / Source & claims**（设计从转写之后开始；转写自身仍需批准、质量检查、可回溯到音频）

```text
Source version S1 (synthetic):
  T1 (patient):   "I have not had a fever."
  T2 (patient):   "The nausea started yesterday."
  T3 (clinician): "It may be related to the new medicine, but I am not sure."
  (no allergy history in the encounter)
```

| 声明 Claim | 引用 Cites | 判定 Verdict | 保留/错误 What it keeps or breaks |
|---|---|---|---|
| The patient reports no fever. | T1 | 忠实 Faithful | 保留**否定 (negation)** |
| The patient reports that nausea started yesterday. | T2 | 忠实 | 保留**时间 (timing)** |
| The clinician said the nausea may be related to the new medicine, but was unsure. | T3 | 忠实 | 保留**说话人 (speaker) + 不确定性 (uncertainty)** |
| Patient has a fever. | T1 | **否定反转 (negation reversal)** | 有引用但 T1 说相反的话 |
| The patient confirms the new medicine caused nausea. | T3 | **归属与确定性错误 (attribution & certainty)** | 医生的不确定猜测 → 患者的确定陈述 |
| No known medication allergies. | 无 | **无支撑纳入 (unsupported inclusion)** | 把缺失史当阴性发现 |

课内测验：遭遇支持哪个声明 → **"The patient reports no fever. [T1]"**。链接告诉审核者去哪看；审核者仍需比较含义。修正声明使其保留来源含义，或无来源时删除。

**版本绑定的审核 / Version-bound review gating filing**

- 审核界面并排显示来源轮次和草稿声明。医生决定时，应用把决定记录到 **就诊 + 确切病历版本 + 允许的归档动作**。这与更早的录音/转写/发送批准分开。
- T3 演练 (walkthrough)：v1 声明被授权医生审核并批准归档 → 有人改成 "The medicine caused the nausea." → 应用创建 **v2**、记录编辑、**取消 v1 的批准**（T3 仍被引用但与新的确定性矛盾）→ 用旧批准对 v2 归档的请求被阻断 → 医生须对照 T3 修改或拒绝并批准新版本。
- 状态：**draft → reviewed / rejected → simulated-filed**。归档边界代码检查：就诊、当前版本、审核者身份与当前权限、允许的动作、**停止标志 (stop flag)**；任一不匹配阻断；任何编辑退回 draft。
- **记录的批准只证明决定被记录，不证明审核者认真读了**。Lakeside 仍需证明审核者合格、能看到来源、时间足够、能无压力地拒绝。

<svg viewBox="0 0 820 230" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="230" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Version-bound approval state machine｜版本绑定批准的状态机</text>
  <g font-size="12" text-anchor="middle">
    <rect x="20" y="70" width="120" height="56" rx="28" fill="#e8f0fe" stroke="#4a6fd1"/><text x="80" y="92">draft (vN)</text><text x="80" y="110">草稿</text>
    <rect x="220" y="30" width="140" height="56" rx="28" fill="#e6f4ea" stroke="#2e8b57"/><text x="290" y="52">reviewed</text><text x="290" y="70">approval→(enc, vN, action)</text>
    <rect x="220" y="130" width="140" height="56" rx="28" fill="#fde8e8" stroke="#c33"/><text x="290" y="152">rejected</text><text x="290" y="170">已拒绝</text>
    <rect x="460" y="30" width="160" height="56" rx="6" fill="#fff8ec" stroke="#d18a1a"/><text x="540" y="48">Filing gate rechecks:</text><text x="540" y="64">enc, version, reviewer,</text><text x="540" y="80">authority, action, stop</text>
    <rect x="680" y="30" width="130" height="56" rx="28" fill="#e6f4ea" stroke="#2e8b57"/><text x="745" y="52">simulated-filed</text><text x="745" y="70">已归档(模拟)</text>
    <rect x="460" y="130" width="350" height="56" rx="6" fill="#f5f5f5" stroke="#888"/><text x="635" y="150">Any edit → new version, approval cancelled → draft</text><text x="635" y="168">任何编辑 → 新版本、批准作废、回到草稿</text>
  </g>
  <g stroke="#555" stroke-width="1.4" fill="none">
    <path d="M140 88 L220 60"/><path d="M140 108 L220 155"/><path d="M360 58 L460 58"/><path d="M620 58 L680 58"/>
    <path d="M290 86 Q 200 130 140 115" stroke="#c33" stroke-dasharray="4 3"/>
  </g>
  <text x="175" y="200" font-size="11" fill="#c33">edit</text>
  <text x="380" y="50" font-size="11" fill="#555">file request</text>
</svg>

**模拟程序 / Simulation (`hospital_safety.py`)**：离线运行 `python hospital_safety.py`；`--live` 把三个测试轮次发给 Responses API（`gpt-6-luna`，`store=False`），要求返回带来源 ID 的 JSON；`--list` 打印带行号源码。

```python
# Condensed sketch of the filing gate from the lesson (in-memory, synthetic only)
def file_simulated(records, encounter_id, version, reviewer, action, approval,
                   permissions, filing_enabled, stop):
    record = records.get(encounter_id)
    if (record is None or record.state != "reviewed"
            or record.version != version or approval is None or approval != record.approval
            or approval.version != version or approval.reviewer != reviewer
            or approval.action != action or approval.claims != record.versions.get(version)
            or permissions.get(reviewer, {}).get("review") is not True
            or permissions.get(reviewer, {}).get("file") is not True
            or filing_enabled is not True or stop is not False):
        raise Stop("filing blocked")
    record.state = "simulated-filed"
    record.audit.append(("simulated filing", encounter_id, version, reviewer, action))
```

- 离线运行结果：五个固定草稿 = **1/5 忠实，4/5 各含一种指定错误**（遗漏 T2；无支撑过敏；否定反转；T3 归属/确定性错误）——描述测试用例，**不是模型准确率**；时间错误需更多测试。
- **四次应被阻断的尝试**：从草稿直接归档；编辑产生 v2 后用 v1 的批准；未授权身份审核；停止标志置位时归档。另有：缺失记录、过期版本、换审核者、换动作、归档禁用、审核权/归档权被撤销都被阻断。之后脚本拒绝错误编辑、恢复忠实草稿、拿新批准、在内存中归档并打印审计日志 (audit log)。
- 关键观察：脚本在测试停止标志前**批准了不准确的 v2**——若标志未置位，该批准会通过所有状态检查。**代码强制的是决定绑定到什么，而不是决定在临床上是否正确。**
- live 路径在指令中要求 JSON 并校验回复（完成状态、形状、真实轮次 ID），失败则扣留草稿且不暴露 SDK 异常文本。生产中用 **结构化输出 (Structured Outputs)** 约束 JSON schema，但**保留来源 ID 检查**——schema 无法判断引用的轮次是否支撑声明。没有真实病历系统连接器；真实集成需要单独安全评审 (security review)。

**捕捉遗漏和捏造的评测 / Evals for omissions & invented findings**

- 离线检查器只是五个确切草稿的**回归测试 (regression test)**，不能评判语义——改写、意外遗漏、偏见措辞、细微时间变化可能漏过。
- 已发表的临床研究：一项病历质量试点评估了**意外纳入 (accidental inclusions)、遗漏 (omissions)、幻觉 (hallucinations)、偏见 (bias)**，由医生按就诊上下文判断严重度；另一项把摘要与人工验证的转写对比，分类遗漏、事实错误、幻觉，由医生评严重度。两者都依赖合格临床医生对比来源与草稿；试点的工具未经严格验证，主观严重度评分可能因机构/科室而异 → Lakeside 需本地校准。

| 评测要素 Eval element | 内容 Content |
|---|---|
| 错误类别 Error categories | 遗漏、捏造发现、否定反转、说话人错误、确定性改变、时间改变 |
| 临床评分 Clinician grading | 合格医生对比每份草稿与来源，评含义与严重度 (severity) |
| 裁决 Adjudication | 分歧交第二位审核者，按事先约定标准 |
| 无静默通过 No silent passes | 缺来源或待裁决 = 不完整；**高文本相似度可能隐藏否定反转**，单独不算通过 |

**上线后监测 / Post-launch monitoring（若批准试点；角色均为提议）**

| 负责方 Owner | 监测内容 What they watch |
|---|---|
| 临床领导 Clinical leadership | 抽样草稿对照来源：无支撑声明、遗漏、偏见、时间变化；评严重度；跟踪实际被审核的抽样数 |
| 工程 Engineering | 归档控制失败、缺审计记录、来源可用性、起草管道变更 |
| 运营 Operations | 审核者工作量；持有停止控制并**测试它确实禁用归档** |

- **直接停止**受影响工作流的事件：绕过审核的归档、审核者需要的来源缺失、停止控制失效。**潜在严重且未评估的内容错误** → 立即暂停 + 临床升级。只有 Lakeside 配置了人工记录兜底才回退。
- 试点结合了医生评分与每份病历被编辑百分比（**编辑率 edit rate**）作次要信号。编辑率上升值得调查，但未改动或大量改动都**不证明**审核认真或最终病历正确。
- 练习：T4（患者）"I felt better this morning than yesterday." 草稿 "The patient felt worse this morning" 引用 T4 → 方向反转；修正需**保留两个时间点**："The patient reports feeling better this morning than yesterday. [T4]"（只写"今早好些"丢掉了与昨天的比较）；新批准必须绑定修正后的版本；审核者需要的来源缺失时 **fail closed**，不算干净审核。

**面试怎么说 / How to say it in the interview**

- Q: "Defend your Lakeside design."
  - EN: "Lakeside wants help with documentation, so I'd offer a source-linked draft that an authorized clinician can check, correct or reject, and choose to file. Every claim carries turn IDs, the approval is bound to the exact version, and any edit cancels it. In the test set, one of five drafts is faithful and four contain the specified errors — that describes the test cases, not clinical performance, and the review and stop controls have only run in memory. Recording approval, clinical grading, and operating ownership are still open, so we stay on test data."
  - 中文：来源绑定 + 版本绑定 + 测试集不是临床表现。
- Q: "The sponsor will label every automatically filed note 'AI-generated.' Why keep clinician review?"
  - EN: "A label and a citation don't change what enters the record. If a fever claim cites a turn that says 'I have not had a fever,' auto-filing puts a reversed finding in the chart before anyone decides. Only a clinician comparing meaning against the source catches that."
  - 中文：引用可以指向相反含义的句子。
- Q: "The sponsor says review is too expensive. What do you offer?"
  - EN: "A narrower clinician-reviewed draft, or the current manual workflow if Lakeside staffs it. Labeling automatic filing doesn't make it a draft. I'd ask clinical leadership and operations what review load they can actually support, and measure review time against writing from scratch on test encounters."
  - 中文：更窄的审核草稿或人工流程，并测量审核时间。
- Q: "Isn't a schema-validated JSON with source IDs enough?"
  - EN: "No. Structured Outputs guarantees the shape, and I'd still check every source ID is real, but neither can tell whether the cited turn supports the claim. Meaning needs clinician grading against the source, with severity and adjudication."
  - 中文：schema 管形状不管含义。
- Q: "How would you monitor after launch?"
  - EN: "Sampled clinician review against source with severity ratings and denominators, engineering alerts on filing-control failures and missing audit records, and operations owning a tested stop control. A bypassed filing, missing review source, or a failed stop halts the workflow; a serious unassessed error triggers a hold and clinical escalation. Edit rate is a secondary signal, never proof of careful review."
  - 中文：抽样临床审核 + 控制告警 + 可测试的停止开关。

---

## 20. Saying No to an Unsafe Request｜对不安全请求说不

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/saying-no-to-an-unsafe-request

**要点 / Key ideas**

- 面试官不是测你能否拒绝（谁都能说不），而是测你能否**指出越线的确切动作、用客户的语言解释原因、并带着客户仍想要的计划离开**。场景：Lakeside 发起人 (sponsor)要求自动归档 AI 病历，之后由医生纠正。

**识别越线的四个信号 / Four signals of an unsafe request**（通常伪装成成本或速度优化，并附带一个不起作用的"保障"）

| 信号 Signal | 说明 Explanation |
|---|---|
| 高风险动作前的人工决定消失 Human decision disappears | 使用政策禁止在医疗等敏感领域无人工审核地自动化高风险动作；无医生决定的归档正是如此 |
| 模型承担专业人员角色 Model takes a professional's role | 草稿开始决定诊疗，或产品暗示 AI 持有临床资质 |
| 数据未经批准流动 Data moves without approval | 隐私团队批准并签协议前就录音、转写或引入新供应商 |
| 标签替代控制 Label stands in for a control | "AI 生成"标签、免责声明、事后纠正——描述风险而不阻止风险 |

发起人请求同时命中第一和第四个信号。使用政策也说明其规则**不替代法律要求、职业义务、伦理义务**——政策是拒绝理由之一，与 Lakeside 对患者的义务并列；**发起人接受风险两者都不能解决**。

**重放证据 / Replay evidence**：9 个测试就诊走发起人的捷径，草稿未经审核写入模拟记录。**1 条写入了 "No known medication allergies"（来源无过敏史），1 条写入了反转来源"无发热"的发热声明**；其余 7 条**未检查——算未知，不算干净**。2/9 不是生产错误率，但足以说明机制：捷径跳过审核，没有东西拦住这些句子；后续纠正能改记录但**撤销不了第一次写入**，纠正前读到病历的医生可能据此行动。两句话说完整个论点——压力下正需要这样。

**不失去客户地说不：四步 / Saying no in four moves**

| 步骤 Move | 示例 Example |
|---|---|
| 从他们的目标开始 Start with their goal | "You want to give clinicians back time spent documenting. I want that too." |
| 点名你不建的那个动作 Name the one action | "I won't build automatic filing of unreviewed notes."（精确，让客户听到项目其余部分仍开放） |
| 用他们的语言给理由 Reason in their terms | 病历中虚假过敏陈述是**患者安全事件 + Lakeside 的责任 (liability)**，不是抽象政策问题 |
| 提出你会建的 Offer what you will build | 比从零写更省时间的审核草稿 |

**弱答案**："照做自动归档。标签提醒医生小心，我们跟踪纠正找剩余错误。"——跟踪纠正只在错误已进入记录后才发现部分错误。强答案**去掉写入**，而不是给写入改名。

**安全替代方案 / Safe alternative**：停在草稿，直到授权医生决定。是**记录辅助**，与诊断、治疗、自主归档分开。

| 步骤 Step | 内容 Content |
|---|---|
| 起草 Draft | 每个声明链接到就诊来源 |
| 审核 Review | 医生有时间和权限修改或拒绝（含捏造发现与含义反转） |
| 决定 Decision | 医生决定是否归档**这个确切版本** |
| 强制 Enforcement | 写入前应用检查版本绑定的决定和当前归档权限；任何编辑取消旧批准 |

替代方案必须回应成本异议，否则发起人会回到捷径：**测量**——在测试就诊上比较医生审核好草稿 vs 从零写的时间。审核更快 → 节省到手且保留安全步骤；Lakeside 完全无法配置审核 → 答案是现有人工流程，**不是自动归档**。

<svg viewBox="0 0 820 210" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="210" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Shortcut writes before review; proposed path reviews first｜捷径先写后审，提议路径先审后写</text>
  <g font-size="12" text-anchor="middle">
    <text x="60" y="68" font-weight="bold" fill="#c33">Shortcut</text>
    <rect x="110" y="45" width="130" height="44" rx="6" fill="#fff" stroke="#555"/><text x="175" y="63">AI draft</text><text x="175" y="79">AI 草稿</text>
    <rect x="260" y="45" width="170" height="44" rx="6" fill="#fde8e8" stroke="#c33"/><text x="345" y="63">Write to record + label</text><text x="345" y="79">写入病历+标签</text>
    <rect x="450" y="45" width="170" height="44" rx="6" fill="#fff3f3" stroke="#c33"/><text x="535" y="63">Readers may act (2/9 false)</text><text x="535" y="79">读者可能据此行动</text>
    <rect x="640" y="45" width="170" height="44" rx="6" fill="#f5f5f5" stroke="#888"/><text x="725" y="63">Later correction</text><text x="725" y="79">事后纠正(撤销不了首写)</text>
    <text x="60" y="148" font-weight="bold" fill="#2e8b57">Proposed</text>
    <rect x="110" y="125" width="130" height="44" rx="6" fill="#fff" stroke="#555"/><text x="175" y="143">Source-linked draft</text><text x="175" y="159">带来源草稿</text>
    <rect x="260" y="125" width="170" height="44" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="345" y="143">Clinician review</text><text x="345" y="159">医生审核/修改/拒绝</text>
    <rect x="450" y="125" width="170" height="44" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="535" y="143">Version-bound decision</text><text x="535" y="159">绑定确切版本</text>
    <rect x="640" y="125" width="170" height="44" rx="6" fill="#e6f4ea" stroke="#2e8b57"/><text x="725" y="143">Gate checks, then write</text><text x="725" y="159">校验后才写入</text>
  </g>
  <g stroke="#555" stroke-width="1.4" fill="none"><path d="M240 67 L260 67"/><path d="M430 67 L450 67"/><path d="M620 67 L640 67"/><path d="M240 147 L260 147"/><path d="M430 147 L450 147"/><path d="M620 147 L640 147"/></g>
</svg>

**仍需在试点前完成 / Before a pilot（都未完成）**：临床评分（合格医生对比来源与草稿、评严重度、按约定标准解决分歧）；审核质量（审核者有来源访问、时间、能力、真实拒绝权——日志里的批准本身不说明认真阅读）；监测与停止（带分母和缺失数据的计数；绕过的归档、缺审核来源、停止控制失效 → 停止；严重未评估错误 → 暂停 + 临床升级）；数据流批准（隐私法务批准每个采集、处理、保留、拒绝步骤并签 BAA；工程安全修 trace 与备份问题——`store=false` 不移除 Lakeside 副本）；归属（临床领导、工程、隐私、运营各自接受，含谁能停止）。
9 例重放证明边界的必要性，5 个测试草稿提供回归检查；**两者不合并，也都不替代临床评分或证明试点就绪**。

**最终自检 / Final check**：重演发起人的下一个报价——更多钱、不同合同条款、更大的标签。**如果你的答案仍允许同样的未审核写入，你就已经移动了底线**，无论措辞听起来多安全。

**面试怎么说 / How to say it in the interview**

- Q: "The sponsor accepts the risk. Every auto-filed note will say 'AI-generated,' and clinicians correct later. What do you recommend?"
  - EN: "Lakeside wants to cut documentation time, and I understand the cost pressure. I'd still decline automatic filing and keep working on test data. In the replay, two of nine notes reached the mock record with false statements — an allergy status the source never gave and a fever the patient denied — and the other seven are unchecked, so I wouldn't call them safe or read it as an error rate. I'd offer a source-linked draft that an authorized clinician checks, corrects or rejects, and decides whether to file, with the decision bound to the exact version. Before any pilot, privacy and legal approve recording and sign BAAs, clinical leadership sets up grading and names reviewers, and operations owns the stop control."
  - 中文：目标 → 拒绝一个确切动作 → 证据如实 → 替代方案 → 前置条件。
- Q: "Is automatic note filing actually prohibited by OpenAI policy?"
  - EN: "Filing a note in a medical record without a clinician's review is automating a high-stakes action in a medical setting without human review, which the usage policies prohibit. But I'd refuse even without the policy, because the replay shows false statements reaching the record. Whether Lakeside's own legal and professional duties allow it is a question for their counsel and clinical leadership."
  - 中文：先讲安全证据，政策作支撑。
- Q: "How does OpenAI's mission affect your answer?"
  - EN: "Reducing documentation burden could genuinely help clinicians, and that matters. So does the patient whose record is wrong. The mission is for AGI to benefit all of humanity, and the Charter commits to avoiding uses that harm people — that supports protecting patients and the clinician's authority while still building a useful draft. But the Charter doesn't approve recording or decide Lakeside's legal duties. A good goal isn't permission."
  - 中文：好目标不是许可。
- Q: "Review is too expensive, and we offer no-training terms and a BAA. Can recording start?"
  - EN: "A BAA lets OpenAI receive PHI as Lakeside's business associate, and the no-training default covers how the data is used. Neither decides whether this visit may be recorded under state recording law and hospital policy. We stay on test data until the privacy team decides that — and I'd measure review time versus writing from scratch so the cost question gets a real answer."
  - 中文：BAA 与不训练都不是录音许可；用测量回应成本。
- Q: "What if the patient can opt out after recording?"
  - EN: "An opt-out after the fact can't approve a recording that already happened. If approval is missing or the patient declines before capture, we don't record or send anything. If they withdraw mid-recording, we stop and hand the material to the privacy team to decide."
  - 中文：事后退出无法追认已发生的录音。
- Q: "What if they offer more money or a bigger label?"
  - EN: "Then my answer is the same, because the unreviewed write is still there. I'm happy to change scope, timeline, or the review UI to cut clinician time, but not to remove the clinician's decision before filing."
  - 中文：底线不随报价移动。

---

## 21. Debriefing the Three Cases｜三个案例复盘

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/debriefing-the-three-cases

**要点 / Key ideas**

- 三个客户、三个请求，底下是同一个问题：**你今天会交付什么？什么证据说明它安全？** Meridian 想给仍在失败的聊天试点加语音；Aster 想为速度去掉访问检查；Lakeside 想在医生看到前归档带 AI 标签的病历。
- 复盘时把三件事分开：每个案例**观测到了什么**、你**提议了什么**、**谁真正接受了责任**。缺记录的维度标"无法评估 (unassessable)"并安排排练；**不要把示例评分当作自己的**。
- 评分四条规则：**先引用 (quote first)**——每个评分引用你的答案并说明支持/遗漏了什么；**评答案而非客户就绪度**；**一次评完三个案例**（标准不漂移）；**维度分开**，不加总、不当录用预测（清晰的推荐可以沟通 2 分而安全 0 分）。评第一次答案（面试官听到的就是它），修订单独评。

**失败与边界对照（课内配对答案）/ Failures → boundaries**

| 案例观测 Case observation | 受影响的边界 Boundary |
|---|---|
| Meridian：语音打断后延续了待确认 | 来电者插话时清除任何待确认 |
| Meridian：冲突政策案例错误地起草了 | 把案例交给人，而不是生成回复 |
| Lakeside：模拟病历在医生审核前写入 | 记录改变前由合格人员决定 |
| Aster：受限段落到达外部重排器 | 内容离开应用前检查权限 |

这些失败发生在不同位置：路由、转给外部服务、打断处理、归档。**看似合理的最终答案无法证明任何一个边界守住了**。

**强答案的五个共性 / Five traits of strong answers**

| 共性 Trait | 做法 How |
|---|---|
| 先给决定 Lead with the decision | 一句话：现在交付什么、什么保持阻断 |
| 指出失败的边界 Name the boundary that failed | 漏人工路由、发给外部重排器的段落、写入记录——而不是总通过率 |
| 区分观测与提议 Separate observed from proposed | 重放显示了什么 / 你会建什么 / 计划测什么；计划不替代结果 |
| 点名负责人或缺口 Name owners or the gap | 政策、升级、审核、运营谁负责，或直说还没人接受 |
| 给出有用的下一步 Offer a useful next step | 更窄试点、离线 demo、仅草稿工作流——推进合作同时拒绝不安全请求 |

**三个示例弱答案及评分 / Sample weak answers & ratings**

| 案例 Case | 弱答案 Sample response | 客户 | 归属 | 技术 | 证据 | 安全 | 沟通 |
|---|---|---|---|---|---|---|---|
| Meridian | "Ready for a chat and voice pilot: 11/12 routes passed, and we will compare 40 vs 40." | 1 | 0 | 0 | 0 | 0 | 2 |
| Aster | "The answer cites an eligible document, so release it; skip access checks to preserve the 1.8 s p95." | 1 | 0 | 0 | 1 | 0 | 2 |
| Lakeside | "File with an AI label, then correct the two errors later. Two errors in nine attempts." | 1 | 0 | 0 | 1 | 0 | 2 |

- Meridian 弱点：丢了"审核的一般指导"范围和客服角色；无负责人；把文本路由分数当两个工作流的依据、忽略打断状态；无视漏掉的必需路由和语音重放；推荐暴露两个各有阻断失败的阶段。更强：阻断客户暴露、两阶段分开；聊天修冲突路由 + 保留代表集重跑 + 解决政策访问、人工兜底、运营人；语音在确认重置、真实音频评估、周末覆盖接受前保持阻断，期间提供离线演示；40 vs 40 仍是未来步骤。周末语音的混合负载比纯聊天每月多 **$48**（不含人手等）——预测不是有资金有人手的服务。
- Aster 弱点：跳过访问检查恰恰移除了重排器暴露所越过的边界；引用和延迟各自证明特定事情，但都不证明访问控制或冲突覆盖。1.8s p95 来自给定 20 请求集，$0.020/任务；都不能成为移除权限、引用、冲突检查的理由。更强："Withhold broad release. Enforce entitlement before content reaches the external reranker, keep coverage of every eligible source, and route unresolved conflicts for review. Reproduce the failures and inspect representative holdout results. A narrower advisor-reviewed pilot depends on that repair, that evidence, and accepted owners."
- Lakeside 弱点：标签保留了审核前的归档动作；"2/9"漏掉了这是测试病历上的捷径重放、其余 7 条未证明安全。课内测验答案：**拒绝自动归档，保持在测试数据；提议带来源的医生审核 + 确切版本的归档决定 + 归档时检查权限，以未决前置条件为前提。** 确切版本规则的意义：批准一个草稿的医生**没有批准**之后归档的另一个版本。

**代价最大的六个错误 / Six costliest mistakes**

| 错误 Mistake | 说明 Explanation |
|---|---|
| 把通过率当就绪 Pass rate read as readiness | 11/12 听着强，直到问哪个失败了；一个漏掉的必需人工路由就阻断发布 |
| 把迟到的检查当控制 Late check read as control | 末尾加的引用召不回已发给外部重排器的段落；检查只有在内容越界**之前**运行才保护边界 |
| 把标签当审核 Label read as review | 标"AI 生成"改变写入的外观，不在它前面放医生的决定 |
| 把计划当结果 Plan reported as result | 40 vs 40、holdout、临床评估都是未来工作——作为发布条件呈现 |
| 把提议的负责人当已接受 Proposed owner as accepted | "运营会支持"在运营同意前只是希望；说出谁还缺 |
| 向发起人压力让步 Giving way to sponsor pressure | 发起人接受风险**不会创造控制** |

跨案例的优势/弱点需要多个答案的引用支撑才算"已证明"；只有一次记录就叫"可能风险，待测试"。但**一次有记录的不安全决定**即使不重复，也可能是你后果最严重的缺口。修订答案只证明你排练了，不证明案例失败被修复或有人接受了归属；修订单独评分，沟通更好不会自动提高证据或安全分。

<svg viewBox="0 0 820 260" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="260" fill="#fff"/>
  <text x="410" y="22" font-size="15" font-weight="bold" text-anchor="middle">Three cases, one pattern｜三个案例，一个模式</text>
  <g font-size="12" text-anchor="middle">
    <rect x="10" y="45" width="250" height="150" rx="8" fill="#eef3fd" stroke="#4a6fd1"/>
    <text x="135" y="66" font-weight="bold">Meridian Telecom 电信</text>
    <text x="135" y="88">Ask: 70% automation, weekend voice</text>
    <text x="135" y="106">Ship: reviewed general-guidance drafts</text>
    <text x="135" y="124">Failed: 1/8 human route; 2/4 interrupts</text>
    <text x="135" y="142">Boundary: human route + ACK</text>
    <text x="135" y="160">Decision: no pilot; offline voice demo</text>
    <text x="135" y="178">不试点；离线语音演示</text>
    <rect x="285" y="45" width="250" height="150" rx="8" fill="#fff8ec" stroke="#d18a1a"/>
    <text x="410" y="66" font-weight="bold">Aster Wealth 财富管理</text>
    <text x="410" y="88">Ask: launch on 15/20, drop cache check</text>
    <text x="410" y="106">Ship: internal report-specific drafts</text>
    <text x="410" y="124">Failed: reranker leak; stale cache</text>
    <text x="410" y="142">Boundary: entitlement before ranking</text>
    <text x="410" y="160">Decision: offline; fix + holdout</text>
    <text x="410" y="178">离线；修复后 holdout</text>
    <rect x="560" y="45" width="250" height="150" rx="8" fill="#fdeeee" stroke="#c33"/>
    <text x="685" y="66" font-weight="bold">Lakeside Hospital 医院</text>
    <text x="685" y="88">Ask: auto-file with "AI" label</text>
    <text x="685" y="106">Ship: source-linked clinician drafts</text>
    <text x="685" y="124">Failed: 2/9 false writes; log PHI</text>
    <text x="685" y="142">Boundary: clinician decides pre-write</text>
    <text x="685" y="160">Decision: refuse; test data only</text>
    <text x="685" y="178">拒绝；仅测试数据</text>
    <rect x="10" y="210" width="800" height="38" rx="6" fill="#f5f5f5" stroke="#888"/>
    <text x="410" y="227">Model proposes, application decides · check before the boundary · observed ≠ proposed ≠ accepted</text>
    <text x="410" y="243">模型提议、应用决定 · 越界前检查 · 观测 ≠ 提议 ≠ 已接受</text>
  </g>
</svg>

**面试怎么说 / How to say it in the interview**

- Q: "Across your cases, what do you ship today and what blocks the rest?"
  - EN: "I lead with the decision in one sentence, then name the exact boundary that failed rather than an overall pass rate, separate what the replay showed from what I'd build and what I plan to measure, name the owners or say nobody has accepted yet, and offer a narrower next step — an offline demo or a draft-only workflow — so the engagement keeps moving while the unsafe request stays refused."
  - 中文：五个共性压成一段话。
- Q: "Your answer was clear. Doesn't that count?"
  - EN: "It counts for communication, not for safety. A clear recommendation to release across a known boundary is still unsafe, so I'd score those dimensions separately and fix the decision, not the delivery."
  - 中文：表达好不能抵消不安全的决定。
- Q: "The sponsor accepts the risk."
  - EN: "Accepting the risk doesn't create a control. I'll change scope, timeline, or the review flow to meet their goal, but the boundary that failed has to be repaired and verified before anyone is exposed."
  - 中文：接受风险 ≠ 有控制。

---

## 22. Conclusion｜总结

Source: https://www.educative.io/courses/openai-forward-deployed-engineer-interview/conclusion

**要点 / Key ideas**

- 备考常见错误：重读已知内容，跳过答错的题。现在你有三个评过分的案例答案、一个项目故事、一份缺口清单——它们告诉你下一小时该花在哪。
- OpenAI 职位描述：FDE 交付从发现与技术界定 → 设计、构建、生产上线；成功看生产采用、工作流影响、评测驱动反馈。课程五部分：角色（FDE 拥有什么、与解决方案架构师等的区别、章程与部署理念）；平台（Responses API + 工具调用 + 结构化输出、Agents SDK、带人工批准的单 agent 工作流、MCP 服务器、handoffs 与 agents-as-tools、Workspace Agents 与 ChatKit vs 自建栈、Realtime API 语音、按任务和预算选模型与推理强度 reasoning effort）；系统设计（端到端工作流、排序前检查资格的工具 schema 与检索、跨 agent 故障隔离、评测集、防提示注入 prompt injection 护栏、用 trace 调试管道）；面试流程；三个案例。
- **贯穿全课的一句话：模型提议，应用决定 (the model proposes, and your application decides)**。短工作流且掌控分发与状态有用 → 直接调用 Responses；需要托管轮次、工具、护栏、handoffs、会话时 → Agents SDK（对 OpenAI 模型默认用 Responses）。两种情况下业务授权与发布决定都归应用。
- OpenAI 面试指南：工程面试看设计良好的方案、高质量代码、性能、测试覆盖 + 沟通协作 → 技术排练要同时讲实现和**关键边界守住的证据**。

**要展示的能力与可检查物 / Capabilities → inspectable artifacts**

| 能力 Capability | 可检查物 Artifact |
|---|---|
| 客户交付 Customer delivery | 项目故事：用户、工作流问题、你的构建、观测证据、谁接受了交接 |
| 使命意识的判断 Mission-aware judgment | 保存的推荐：受影响的人、授权与政策问题、关键边界失败时的决定 |
| 技术设计 Technical design | 为 Responses 或 Agents SDK 的选择辩护，含应用强制的边界 |
| 证据与运营 Proof & operation | 应用自有的版本化评测、检查过的结果、已知局限、已接受或公开未决的运营责任 |
| 面试沟通 Interview communication | 第一次答案、难追问、基于同样证据的修订答案 |

**最后几周的循环 / Final-weeks cycle**：① **选缺口**（清单里后果最严重的已证明缺口或无法评估的风险）→ ② **产出产物**（版本化重放、项目记录或可被他人核查的书面决定）→ ③ **排练**（冷答、难追问、修订、六维评分）→ ④ **复盘**（设状态、选下一个缺口）。还没保存自己的答案 → 第一个循环就是产出它们。

**第一块时间给什么（课内测验）**：Aster 记录中候选人答"引用了合格文档所以发布；为保持 1.8s p95 跳过访问检查"，且无记录显示运营团队接受了其个人项目交接。答案 → **检查并复现受限段落边界**。流畅不降低"跨已知边界推荐发布"的后果；交接记录缺失也重要，但修它不会让那个决定变安全。产出版本化重放记录，**检查前标记输出 pending**；即使检查过的重放也不证明修复有效。

**可检查产物的要素 / What makes an artifact inspectable**

| 要素 Element | 内容 Content |
|---|---|
| 版本 Version | 检查的代码的 commit ID 或文件校验和 (checksum) |
| 输入 Input | 具名测试用例与测试条件 |
| 过程 Procedure | 命令及相关环境/设置 |
| 输出 Output | 检查过的结果，或批准记录的链接 |
| 结论与局限 Conclusion & limit | 结果支持什么、什么未知、输入是测试还是生产数据 |

个人故事保持五段式链条，每个声明链接到批准的产物，写清自己与协作者的贡献，区分观测结果与预测；练习记录中不放凭证和未授权客户数据。"我把生产处理时间降了 30% 并交给运营一个稳定系统"需要批准的生产测量和运营接受的证据；没有就诚实改写（"我和工程团队一起构建了工作流；生产时间降低和运营接受尚未验证"），再替换成你真实的贡献和证据。

**4 小时分配示例 / Four-hour allocation（准备时间，非面试时长）**

| 块 Block | 时长 Minutes | 内容 Content |
|---|---|---|
| 边界复现 Boundary reproduction | 75 | 检查版本化检索测试，跑离线重放，记录输入、过程、输出、局限 |
| 项目产物 Project artifacts | 45 | 在批准记录中找个人交接及其支撑结果；未记录接受就限定故事 |
| AI 面试官排练 Rehearsal | 60 | 保存开场辩护、追问、修订、有引用支撑的评分 |
| 评估说明 Assessment instructions | 30 | 记录交付物、形式、允许工具、提交步骤、截止；权限不清就起草给 recruiter 的问题 |
| 证据复盘 Evidence review | 30 | 对照清单、设状态、排下次复盘 |
| **合计 Total** | **240** | 时间更少时：对关键风险保留一个具体动作和复盘方式，其他缺口保持开放 |

课内测验：备忘录说"OpenAI 面试指南说流畅答案足以证明访问边界守住，无需离线复现"→ **重新打开该缺口**：指南从未这么说；安排离线重放，检查前输出保持 pending。

**复现边界的四步 / Reproducing the boundary**：① 记录版本（Git 仓库里 `git rev-parse HEAD` 并记下本地改动，否则记校验和）；② 读检查（找 `access` 类别和 `run_case`、`grade` 定义，识别注入的暴露和用来捕获它的检查——重放是模拟，没有发给真实重排器）；③ 离线运行（`python aster_retrieval_eval.py`，不加 `--live`，无需 API key；保存命令，检查 access 行和首个失败的检查项）；④ 比较（对照案例简报，记录分歧或缺失的埋点 (instrumentation)；选定用例不是生产分布）。案例记录报告受限访问 3/4 通过——说明风险值得关注，但你还没亲自检查；检查前写"reproduction output pending"。

**修订排练示例评分**：客户 1（点名用户和审核，没点研究需求）、归属 1（列出未决责任但无人接受）、技术 2（权限检查在外部重排之前）、证据 2、安全 2、沟通 2——显示排练改进，不是部署修复或交接被接受。

**实际评估说明 / Your actual instructions**：在清单中记录说明来源、必须产出什么及评估如何进行、明确允许或禁止的工具和 AI、提交方式与截止、说明未解决的重要事项。权限未说明就发："May I use an AI assistant on this assessment, and if so, are there limits on how I use or disclose it?" 用 AI 面试官练习**不等于**评估中允许用 AI。

**闭环每个循环 / Closing each cycle**：每个优先项都有动作、证据或明确的缺失状态、下次复盘时间、清晰状态。错误的清单：一次流畅排练后标"ready"并在故事里加编造的生产成果 → 修正：重新打开访问和交接项、删掉无支撑声明、安排缺失的检查。

到面试时，你的记录应清楚显示：**检查过什么、预测什么、什么仍开放、下一步做什么**——这正是 FDE 对每个客户的纪律。

**面试怎么说 / How to say it in the interview**

- Q: "The replay shows a restricted passage reaching the reranker. What do you recommend?" (revised answer)
  - EN: "Withhold customer exposure now. I'd enforce entitlement and source eligibility before any passage reaches the reranker, reproduce the original failure, and inspect a reserved representative holdout. I'd keep coverage of every eligible source and route unresolved conflicts for review. A report-specific, advisor-reviewed pilot would depend on those checks, the access and workflow decisions, and accepted source, review, and operating owners. The 1.8-second p95 describes the supplied 20-request path, not the repaired design."
  - 中文：标准修订答案模板。
- Q: "Responses API or Agents SDK — how do you choose?"
  - EN: "For a short workflow where owning dispatch and state is useful, I call Responses directly so the application controls the loop. When managed turns, tools, guardrails, handoffs, or sessions justify the abstraction, I use the Agents SDK, which uses Responses by default for OpenAI models. Either way, business authorization and the release decision stay in my application — the model proposes, the application decides."
  - 中文：按需求选；授权永远在应用。
- Q: "How do you prove a claim from your past project?"
  - EN: "I tie it to an inspectable record: the code version, the named input, the command, the output I actually inspected, and what it does and doesn't support. If I can't find a production measurement or an operating acceptance, I say it's unverified rather than round it up."
  - 中文：版本-输入-过程-输出-局限；没证据就说未验证。

---

---

# Section II｜第二部分：Forward Deployed Engineer for AI Systems（OpenAI 章节增量）

> 本部分与第一部分大量重叠。每节只记录**新的或不同的**内容；其余请看括号中对应的第一部分小节。

## II-1. The OpenAI FDE Interview Loop｜OpenAI FDE 面试流程

Source: https://www.educative.io/courses/forward-deployed-engineer/the-openai-fde-interview-loop
（其余见 §1 The Interview Loop Overview）

**新增 / What's new**

- 开场故事：候选人按网上面经 (interview reports)练了 3 个周末"5 小时 take-home + 全程 AI 助手"，结果 recruiter 确认是**禁止 AI 的现场结对编程**。教训：按官方指南起步，面经只作补充，收到正式说明后调整。
- 官方指南的**招聘理念 (hiring philosophy)** 两点：① OpenAI **不看重学历/证书 (not credential-driven)**，想了解每个候选人的背景和贡献；② 招专家，也招 **"高潜力 (high potential)"**——定义为**已展示出快速进入新领域并产出结果的能力 (ramp up quickly in a new domain and produce results)**。
- 官方推荐的准备材料：**OpenAI 章程 (Charter)、研究论文 (research publications)、博客 (blog posts)**，以及所面团队的近期更新。
- **候选人报告的 FDE 流程**（The Forward Deployed 网站汇总，2026-07-13 查阅；它自己也说 OpenAI 不公布 FDE 流程）：

| 报告阶段 Reported stage | 候选人描述 What candidates describe | 对应官方类别 Guide category |
|---|---|---|
| Recruiter screen | 短电话，常说**约 30 分钟**：背景、部署经验、动机 | 初步通话 Introductory calls |
| Take-home | 用 OpenAI API 解决开放式客户问题，常说**几小时**工作量，有时带录制讲解 | 技能评估 Skills-based assessment |
| Technical session | 从 take-home 出发延伸到 LLM 系统：检索、评测、失败模式、成本 | 技能评估 |
| Final interviews | 多场：新场景的方案设计、技术深度、HM 对话 | 终面 Final interviews |

  面经只提示**练什么**，从不告诉你自己流程的顺序、时长、评分；**第二个网站转述同一份报告仍然只是一份报告**。
- 三类信息权威度：评估说明 > 官方指南 > 面经。**OpenAI 开发 AI 编码工具这一事实也不代表你在评估中可以用它们**。建议**有/无 AI 助手两种都练**。
- 六维自评表给了每档的具体描述（0 缺失 / 1 部分 / 2 具体且有支撑）：

| 维度 Dimension | 0 | 1 | 2 |
|---|---|---|---|
| 客户框定 Customer framing | 无用户或工作流 | 点名但模糊 | 用户、问题、失败代价 |
| 归属 Ownership | 不清谁做了什么 | 部分区分 | 你的部分、别人的部分、现在谁运营 |
| 技术推理 Technical reasoning | 无机制 | 有机制无取舍 | 哪里坏、修复、一个真实取舍 |
| 证据 Proof | 无证据或夸大 | 有证据无局限 | 每个结果说明什么、到哪为止 |
| 安全 Safety | 忽略 | 提到 | 风险边界、关掉什么、回退 |
| 沟通 Communication | 难跟上 | 费力能跟上 | 决定、证据、下一步，按此顺序 |

- 练习：收到面试说明时写三行——材料关于形式和工具说了什么 / 官方指南关于该阶段说了什么 / 面经说了什么；第一行空着的地方，写下要发给 recruiter 的问题。

**面试怎么说 / How to say it in the interview**

- Q: "What does OpenAI's interview guide say about final interviews?"
  - EN: "It describes them as the last stage of an example process: virtual by default with an option to go onsite in San Francisco, typically four to six hours with four to six people over one to two days, focused on your area of expertise and designed to stretch you. A decision usually follows within a week, and the recruiter may ask for references."
  - 中文：终面要点一口气说清。
- Q: "What does 'high potential' mean to OpenAI, and how do you show it?"
  - EN: "The guide defines it as having shown you can ramp up quickly in a new domain and produce results. I'd show it with one example where I learned an unfamiliar system fast and shipped something checkable, with the numbers and their limits."
  - 中文：用一个快速上手并交付的例子证明。

---

## II-2. The Recruiter Screen, Your Project Story, and the Hiring Manager｜招聘官初筛、项目故事与招聘经理

Source: https://www.educative.io/courses/forward-deployed-engineer/the-recruiter-screen-your-project-story-and-the-hiring-manager
（其余见 §2 Your Project Story、§3 The Recruiter Screen、§7 The Hiring Manager Conversation）

**新增 / What's new**

- 把第一部分三节合成一节，新增 **三种深度 (three depths)**：

| 深度 Depth | 场合 Where | 内容 Includes |
|---|---|---|
| 30 秒 30 seconds | recruiter 开场 | 每部分一句，最强证据 + 其局限 |
| 2 分钟 2 minutes | "Walk me through a project" | 你做的取舍及原因、别人的贡献 |
| 10 分钟 10 minutes | HM 或技术追问 | 分歧、错误、会改什么、确切交接 |

  用同一组事实练三种长度，才能在终面对五位面试官保持一致。
- 本版职位地点为 **旧金山 (San Francisco)：每周 3 天到办公室、出差最多 50%**（第一部分是苏黎世，条款相同；其他职位/地点可能不同，要确认）。
- recruiter 环节可问的新问题：技能评估形式与工具规则、**团队目前合作的客户类型**、**团队如何衡量一次成功的合作 (how the team measures a successful engagement)**。
- 简历要点新版本：*"Built a review-required request-routing classifier and review screen; 17 of 20 routes correct in pilot review; operations team continuing the pilot."*
- HM 场景（周五自动派单）新增细节：**会后发书面确认 (written confirmation)**——口头会议约定容易各记各的。
- 新的 "Why FDE (not SWE)?" 范例。

**面试怎么说 / How to say it in the interview**

- Q: "Why forward deployed engineering, and not a software engineering role?"
  - EN: "I want to be the person accountable for whether the system actually gets used. On my routing project I built the classifier and review screen, but the decisions that mattered most were with the operations team — keeping human review when they wanted speed, and getting a named reviewer for the hard cases. The pilot found 17 of 20 routes correct and it's still running under their review. I want to do that end to end, from discovery to a system the customer runs."
  - 中文：对"是否真正被用起来"负责。
- Q: "Two reviews found 14 of 20 and 17 of 20 on different requests. What can you claim?"
  - EN: "Only that the pilot review found 17 of 20 correct and an earlier, separate review found 14 of 20. The request sets differ, so I can't claim a 15-point improvement, and 20 requests can't establish a general accuracy rate."
  - 中文：不匹配样本不能声称提升。
- Q: "Tell me about a time you pushed back on a customer."
  - EN: "The operations lead wanted automatic dispatch by Friday because reviewing every draft cost their team time — a fair concern. I said I couldn't promise Friday on our evidence, because automatic dispatch changes who makes the routing decision and needs its own testing and an owner. We kept the reviewed pilot, they named a reviewer for ambiguous examples, I took on proposing a rationale fix and a verification plan, and I sent both of them a note confirming the revised scope and asking when we'd revisit expansion."
  - 中文：同一故事，多给分歧与关系维护的篇幅，并书面确认。

---

## II-3. The Coding Round｜编码轮

Source: https://www.educative.io/courses/forward-deployed-engineer/the-coding-round
（题目、契约、不变量见 §4 The Coding Round）

**新增 / What's new**

- 开场：候选人 12 分钟写出"长度检查 + dict"，输入 `c1:A, c1:X, c2:B` 时 dict 覆盖 A、且因 c3 缺失**在返回时 crash**（KeyError）——函数不知道自己要守什么承诺。
- **更紧凑的实现**：错误消息更具体（`duplicate result for call 'c1'`、`missing results for: ['c3']`、`record belongs to another request: 'R8'`），用 `payloads.keys() != expected` 做完整性检查。运行输出：

```text
['A', 'B', 'C']
ValueError: duplicate result for call 'c1'
```

- **8 个测试**（unittest）：乱序成功；重复（即使所有 ID 都在）；缺失；外来请求；未知调用；重复期望 ID；空 payload 允许但空 call_id 拒绝；无期望无记录 → `[]`，无期望但有记录 → unexpected。
- **测试设计教训（新）**：每个失败测试检查**错误消息**而不只是异常类型，且**每个 fixture 只破坏一条规则**。旧版外来请求测试在完整 R7 集后加了一条 R8 的 c1——它同时是外来和重复，被重复检查拦下；**删掉 request 检查后整套测试仍然全绿**。改为让 R8 记录成为唯一的 c2，只有 request 检查能抓住它。→ 每个测试映射一条契约条款，并大声说出来："This test is the duplicate rule, this one is completeness, this one is the foreign request."
- 边写边讲的节奏：复述任务与契约、问歧义 → 写函数前说不变量和测试计划 → 先写 happy path 并运行，再逐个加失败检查及测试 → 结束前说出代码**不处理什么**及原因（授权、异步调用方）。需求中途变化：说清改哪一行、哪个测试证明。例："If duplicates should keep the latest result instead, I'd change line 33 to compare timestamps, and add a test with two c1 records where the second is newer."
- **五道值得练的 FDE 编码题（新）**：

| 题目 Task | 关键失败用例 Failure case that matters |
|---|---|
| 指数退避重试 API Retry with exponential backoff | 重试不可重试的错误；忽略 `Retry-After` 头；重试**可能已成功的写操作** |
| 带稳定 ID 的重叠切块 Overlapping chunks with stable IDs | 前面文档变化导致 ID 改变；块切断了表格行 |
| 校验模型 JSON 输出并修复或拒绝 Validate model JSON | 接受合法 JSON 但内容错误；"修复"时编造缺失字段 |
| 按幂等键去重 webhook 事件 Dedupe webhooks by idempotency key | **同一键不同内容**应视为冲突而非重复 |
| 按切片计算评测指标 Eval metrics by slice | 把不完整用例从分母中丢掉，美化结果 |

**练习题契约示例 / Example contracts for the practice tasks**

```text
Task: dedupe(events) where each event = {idempotency_key, body}
Input:  [{k1, "A"}, {k1, "A"}, {k2, "B"}, {k1, "C"}]
Output: accepted = [{k1,"A"}, {k2,"B"}], duplicates = 1, conflicts = [{k1, "C"}]
Invariant: each key is accepted at most once; same key + different body is a conflict, never a silent duplicate.

Task: slice_metrics(cases) where each case = {slice, status in pass|fail|incomplete}
Input:  [{access, pass}, {access, incomplete}, {direct, pass}, {direct, fail}]
Output: access: 1/2 pass (1 incomplete), direct: 1/2 pass
Invariant: incomplete cases stay in the denominator and are reported, never dropped.
```

**面试怎么说 / How to say it in the interview**

- Q: "Why is 'three records for three expected calls' not enough?"
  - EN: "Because count and content are different promises. c1:A, c1:X, c2:B has the right count but a duplicate and a missing c3; a dict silently overwrites A and the lookup for c3 crashes. I reject duplicates before assignment and check completeness before building any output."
  - 中文：数量与内容是两个承诺。
- Q: "How do you know your tests actually test each rule?"
  - EN: "Each failure fixture breaks exactly one rule and asserts the error message, not just the type. I sanity-check by deleting one check and making sure exactly its test goes red. That's how I caught a foreign-request test that was really being rejected by the duplicate check."
  - 中文：一个 fixture 一条规则；删检查看对应测试是否变红。
- Q: "Write a retry with exponential backoff. What do you watch for?"
  - EN: "Only retry errors that are retryable, like timeouts, 429s, and 5xx; honor Retry-After; cap attempts and add jitter. For writes, a timeout means the outcome is unknown, so I'd retry only with an idempotency key the server deduplicates, or reconcile first."
  - 中文：可重试错误、Retry-After、上限与抖动、写操作需幂等键。
- Q: "Deduplicate webhooks by idempotency key — what's the trap?"
  - EN: "Treating the same key with different content as a duplicate. That's a conflict and should be surfaced, not dropped, because it means either a client bug or a replay with changed data."
  - 中文：同键不同内容是冲突。

---

## II-4. The Case Study and Presentation｜案例与展示

Source: https://www.educative.io/courses/forward-deployed-engineer/the-case-study-and-presentation
（Northstar 案例、产物清单、消息动作路径见 §5）

**新增 / What's new**

- 开场：候选人首页"Recommendation: pilot next month / 10 of 12 checks passed"；面试官看过附录问"另外两个呢？"——两条过期记录进入起草，可能告诉运营"技师会来"而实际已取消。信息在笔记里但不在幻灯片上。
- **把砍掉的东西放进展示 (the cut list belongs in the presentation)**："I didn't build automatic closing, because it needs action controls and an owner the brief doesn't give us"——说出来是界定决策，不说像疏忽。
- 录制讲解：当作**面向技术受众的客户 demo**——明确展示范围决策、**在镜头前跑失败用例**、说出更多时间会做什么。
- Northstar 门槛表新增一行**"过期证据：每条过期记录都转人工——当前失败，2/12 被错误放行"**，并给出状态（质量未运行、副作用 (side effects)未验证、试点时间需试点）。
- **展示六段结构（新）**：

| 段 Section | 内容 Content |
|---|---|
| 推荐 Recommendation | 两句话：提议什么、最强证据、主要局限 |
| 客户与问题 Customer & problem | 用户、受影响工作流、当前运营成本 |
| 设计 Design | 拟发布版本、能力与局限、排除项 |
| 证据 Evidence | 每个结果带分母；区分观测与预测 |
| 风险与未决 Risks & open questions | 失败模式、暂停或回滚条件、谁有权决定 |
| 交接与下一个决定 Handoff & next decision | 谁运营、需要客户做什么决定 |

  Northstar 开场范例："I recommend an offline demonstration of a read-only, operator-reviewed triage draft. It routes 10 of 12 stale-evidence cases correctly, but 2 stale records reached drafting, so I'm not proposing a pilot until the freshness check is fixed and re-verified."
- **应对反驳的四种常见挑战（新）**：

| 挑战 Challenge | 回答模式 Answer pattern |
|---|---|
| "能跳过审核省时间吗？" | 承认审核成本 → 说出先决条件（测试过的动作控制、负责人、代表性用例证据）→ 提议测量审核时间以数据决策 |
| "竞争对手两周就做出来了" | 问他们交付了什么、被允许做什么 → 重申我们的门槛及多快能满足 |
| "更好的 prompt 不能修过期记录问题吗？" | 缺陷在模型**之前**的资格检查；改 prompt 可能在测试集上掩盖症状而过期记录仍流向模型 |
| "再给你一周做什么？" | 按顺序说**下一个门槛**而非功能清单：修新鲜度 → 带 holdout 重跑 → 跑分诊质量门槛 |

  问题揭示了你没考虑到的东西时：直说并当场调整推荐；用旧答案对抗新证据显得判断差。

**面试怎么说 / How to say it in the interview**

- Q: "Ten of twelve passed. Why aren't you recommending a pilot?"
  - EN: "The two failures are stale records that reached drafting, and a draft built on stale evidence can tell an operator something that's no longer true — a different class of failure from a wrong urgency label. The fix belongs in the eligibility check before the model, so I'd repair it, rerun the 12 cases plus a holdout, and then run the triage quality gate. I'd propose a pilot once those pass and operations has agreed to run it."
  - 中文：失败类别不同；修在模型前；按门槛顺序推进。
- Q: "The sponsor needs something to show leadership next week."
  - EN: "The offline demonstration is that something. It shows drafts on test records, manual-review routing working, and a clear list of what's left before a pilot — more useful to leadership than a pilot date we'd have to walk back."
  - 中文：离线演示就是可展示的成果。
- Q: "A competitor did this in two weeks."
  - EN: "What did they ship, and what was it allowed to do? If it closed tickets on its own, it carried risks our brief hasn't settled. Here's what our gates require and how fast we can meet them."
  - 中文：先问清对方做了什么，再讲我们的门槛。
- Q: "Can't a better prompt fix the stale-record problem?"
  - EN: "The defect lives in the eligibility check before the model. A prompt change might hide the symptom on the test set while stale records still flow into the model's input, so I'd fix the check in code and verify it on a holdout."
  - 中文：prompt 修不了模型前的边界。
- Q: "What would you do with another week?"
  - EN: "The next gates in order: fix freshness, rerun with a holdout, then run the triage quality gate — not a feature list."
  - 中文：说门槛顺序而非功能。

---

## II-5. The LLM Systems Round｜LLM 系统轮

Source: https://www.educative.io/courses/forward-deployed-engineer/the-llm-systems-round
（请求流程、R-18、响应顺序、成本延迟见 §6）

**新增 / What's new**

- 开场：候选人对 R-18 说"可以试点，再加输出过滤器"。面试官："你的过滤器运行时，那段文本在哪？"——已经在模型输入里了，过滤器只能从屏幕上藏起来，收不回来。
- 新强调：**3 个无支撑的合格草稿是独立的任务质量失败**；修访问边界不证明它们正确，要单独调查，回归测试 (regression testing)时所有合格用例留在分母中。
- **两种深度示例（新）**："How do you handle stale records?" 开场答（一句决定 + 一句证据）："Freshness is checked before retrieval, alongside entitlement, and a stale record returns unavailable. In R-18 all six stale cases were withheld, though the earlier 12-record check still needs its rerun." 追问"怎么知道记录过期？"再深一层："Each record carries a source version and an effective date; the check compares them with the current authoritative version for that ticket, and anything older, or whose version can't be resolved, is treated as stale. I'd test superseded records, records with missing versions, and a record updated between retrieval and drafting."
- **约束变化 (changed constraint)**：说出哪些组件变、哪些不变、要重新验证什么。例：第二个地区的运营加入 → 权限数据变、评测集需要该地区用例；检索、起草、审核界面不变。更紧的延迟目标 → 先分别测资格检查和起草调用，把小模型或更多缓存 (caching)当作**要用评测集验证的取舍**，而非默认。

**练习题库（全部保留）/ Practice question bank**

| # | 问题 Question | 中文要点 Gist |
|---|---|---|
| 1 | Why run the access check before retrieval instead of filtering the model's answer? | 进入模型输入即已披露；排序前过滤让模型只见合格段落，也避免不合格段落挤掉合格证据 |
| 2 | How do you enforce per-user permissions in retrieval without calling the source system on every request? | 块上存 ACL + 权限版本，查询时过滤；与来源负责人约定**新鲜度契约**（如撤销 5 分钟内到达索引）；撤销以事件推送到索引和答案缓存；无法证明在界内则 **fail closed** |
| 3 | Retrieved sources contradict each other. What should the system do? | 两个都展示并带日期/版本；有规则时优先权威当前版本；摄入时标记被取代版本；真冲突就说来源不一致并都引用 |
| 4 | Your eval reports 90% overall. What do you ask next? | 分母是什么、按切片怎么分；能力与安全不同阈值；不完整留在分母；与基线配对查回归；含 1 次越权读的 90% 是失败 |
| 5 | When is a model grader acceptable? | 只用于代码无法判断的含义；窄 rubric、草稿作数据、对照专家校准、失败或未校准标不完整；工具使用、授权、副作用永远用代码评分 |
| 6 | Why did you use one agent instead of several? | 任务不需要；每多一个 agent 多一次调用、多一个泄露点和失败模式；需对单 agent 基线做测量比较证明收益 |
| 7 | An agent's tool call times out. What do you do with the result if it arrives later? | 绑定发起的调用和轮次，只在该轮仍有效时接受；用户已继续或请求变了就抑制并重读；写操作超时 = 结果未知，重试前对账 |
| 8 | The model call is fast but users say the system feels slow. Where do you look? | 用户实际体验的区间：从动作到首个有用输出；含检索、权限检查、编排调用与重试、渲染；分段测、看慢百分位 |
| 9 | How do you estimate the monthly cost of a feature? | 给每个任务的每次调用定价（含编排、预期重试、工具费），用真实缓存/非缓存用量；按任务类型乘量；压力测试缓存命中率与流量；说明排除项；用当前价格替换假设价格 |

**面试怎么说（题库英文答案）/ English model answers**

1. EN: "Once protected text is in the model's input, it's been disclosed to the model, and any later filter can only hide it from the screen. Checking entitlement, applicability, and freshness before ranking means the model only ever sees eligible passages, and it keeps ineligible passages from crowding out the eligible ones the answer needs."
2. EN: "I store each document's ACL as chunk metadata with a permission version and filter at query time. Resolving the user's groups isn't enough if a document's ACL changes, so I agree a freshness contract with the source owner — say revocations reach the index within five minutes — and push revocations to the index and answer cache as events. If I can't show permission data is within that bound, I fail closed: withhold the passages or check the source system before disclosing. An alert on sync lag reports staleness; it doesn't stop disclosure."
3. EN: "Surface both with their dates or versions rather than silently picking one, and prefer the current authoritative version where a rule defines it. Ingestion can mark superseded versions so they rank lower or drop out. For a genuine conflict, the model says the sources disagree and cites both, and the question routes to the source owner."
4. EN: "What's the denominator, and how does it split by slice? Capability and safety slices need separate thresholds, incomplete cases stay in the denominator, and I'd pair each case with the baseline to catch regressions. A 90% that includes one unauthorized read is a failing result."
5. EN: "Only for meaning code can't decide, like whether a draft faithfully describes an ambiguous note. It gets a narrow rubric, receives the draft as data, is calibrated against expert labels, and marks a case incomplete instead of passing when it fails or isn't calibrated. Tool use, authorization, and side effects always go to code graders."
6. EN: "Because the task didn't need more. Each extra agent adds a model call, a place for context to leak, and a new failure mode. A second agent earns its place only when a measured comparison against a single-agent baseline shows a quality gain that pays for those costs."
7. EN: "I keep it tied to the call and turn that issued it, and accept it only if that turn is still current. If the user moved on or the request changed, I suppress it and re-read. For a write, a timeout means the outcome is unknown, so I reconcile against the ledger before any retry."
8. EN: "At the interval users experience — from their action to the first useful output — including retrieval, permission checks, orchestration calls, retries, and rendering. I'd measure each segment and look at slow percentiles, because a median hides the requests people complain about."
9. EN: "Price every model call one task makes, including orchestration, expected retries, and tool charges, using real cached and uncached usage. Multiply by volume per task type, stress-test cache hit rate and traffic, state what's excluded like infrastructure and review time, and swap assumed prices for current ones before calling it a budget."

- Q: "Show me exactly where the access check runs."
  - EN: "Before retrieval. The application authenticates the operator, then checks entitlement for each record, along with applicability and freshness, before any text reaches ranking or the model. Anything that fails or can't be checked returns 'unavailable' with no content. In R-18 one adapter path sent a passage to the model before that check ran, so I quarantined that adapter, moved the check in front of it, and reran the case plus a holdout, inspecting the actual model inputs."
  - 中文：标准答案，含 R-18 的修复。

---

## II-6. Case Study: Support Agents for Meridian Telecom｜案例：Meridian 电信客服智能体

Source: https://www.educative.io/courses/forward-deployed-engineer/case-study-support-agents-for-meridian-telecom
（完整内容见 §9–§12）

**新增或不同 / What's new or different**

- 压缩为一节，定位为 **take-home 与展示阶段**的练习，周一收到 brief 的口吻。
- 设计上默认推荐 **固定的"筛查→起草"工作流**（一个起草 agent 调一个只读工具），**分诊 agent + 专家是备选**，需在测量比较中证明值得多一次模型调用（第一部分 §11 以分诊 agent 为主线、固定流程为备选）。
- 对漏掉的冲突路由的新解读：评审员 (reviewer)**确实审了**那份草稿，但那**不满足必需的升级流程**——该案例需要升级给有权解决冲突指导的具名负责人；客服收到的是一份**看不出底层指令互相矛盾**的草稿。→ **冲突不可见时，基于冲突指导的合理草稿能通过常规审核**。
- 展示稿结尾新增**明确的 ask**："What I need from Meridian is a decision on those owners and a definition of 'resolved' we can measure."
- 成本只给全聊天版 $83.40/月（3,000 任务 × $0.0278），并点名遗漏：**转写 (transcription)和语音合成 (speech synthesis)费用、客服审核时间、基础设施**（可能比模型调用还贵）。
- 本案例强化的三个习惯：把 brief 分成事实/诉求/缺口再设计；先给已考虑最弱证据的决定；需求变化时**修订整个计划**而不是硬接上去。
- 自测边界：五句话的周末语音推荐不能承诺下月上线；3 个未确认升级与 2/8 语音状态失败作为**独立阻断项**各有重测；成本行为 $83.40/月仅模型调用并列出排除项；**把语音结果混进 11/12 文本结果就重写**。

**面试怎么说 / How to say it in the interview**

- Q: "Why can't Meridian's 70% automation target be the first release's success gate?"
  - EN: "Because nobody has defined whether 'automated' means deflected, answered, or resolved, and each has a different denominator and baseline. Containment can rise while customers get poor answers, come back, or never reach a person, so 70% guides discovery; the gate is zero unsupported answers sent and zero missed human routes."
  - 中文：70% 未定义；门槛是 0 无支撑发送、0 漏人工路由。
- Q: "A representative reviewed the conflicting-guidance draft. Isn't that enough?"
  - EN: "No. That case needed escalation to the owner who can resolve conflicting guidance. The representative got a plausible draft with no sign the instructions contradicted each other, so ordinary review couldn't catch it. The fix is routing in the screen, not more careful reviewers."
  - 中文：冲突不可见时审核抓不住，要修路由。
- Q: "What do you need from Meridian?"
  - EN: "A decision on the owners — support operations for review and fallback, a policy owner for approved guidance, customer engineering for access and telemetry — and a definition of 'resolved' we can measure."
  - 中文：明确的 ask。

---

## II-7. Case Study: A Research Assistant for Aster Wealth｜案例：Aster Wealth 研究助手

Source: https://www.educative.io/courses/forward-deployed-engineer/case-study-a-research-assistant-for-aster-wealth
（完整内容见 §13–§16）

**新增或不同 / What's new or different**

- 定位为 **LLM 系统技术轮**练习。
- **使用政策版本新细节**：**2026 年 11 月 20 日生效**的 OpenAI 使用政策版本新增两条相关规定——禁止在无持牌专业人士适当参与时提供需执照的定制建议工具；禁止在金融活动中无人工审核地自动化高风险动作。**该日期前做的决定需核实当时生效的版本和协议**；但客户邮件请求无论如何都因**授权**而超出范围。
- 三个属性的明确命名：**相关性 (relevance)**——文档是否关于该问题；**适用性 (applicability)**——对该产品、日期、用途有效，**由来源负责人决定**；**权限 (entitlement)**——该顾问能否看，**由访问负责人决定**。来源负责人不能授予访问，访问负责人不能让被取代报告变当前。
- 发起人 (sponsor)请求同第一部分 §16（6 名顾问、30 个请求、15/20、$0.020/任务、4,000 任务 $80/月）；新给出的**有条件 yes 包含停止规则 (stop rule)**："Then I'd propose the six-advisor pilot with a stop rule: any access exposure ends it."
- **发起人能接受什么风险（新表述）**：发起人可以接受**业务风险**（更慢的答案、更窄的范围），但**无权接受**向无权顾问披露材料——那归访问负责人和合规。
- 自测练习（新）：同一问题跑两次——第二次在一小时后，顾问调到别的团队并**失去所有 Aster 研究报告访问权**。检查：两次都在排序前移除 R1 v1 和 R3；没有段落在过滤前到达外部重排器；第一次答案保留"最高"并展示或转审 4% vs 5% 冲突；第二次时第一次的**缓存答案被失效或分区，顾问读不到任何报告文本**。

**面试怎么说 / How to say it in the interview**

- Q: "A summary cites the current version of an approved report. Why might it still fail review?"
  - EN: "A citation is a pointer, not proof. The passage may say a maximum of 4% while the claim says the fee is 4%, and another eligible report may say 5%. It needs claim-level checking against the passage, and conflicts have to be shown or routed rather than resolved by picking one."
  - 中文：引用是指针，要做声明级核查。
- Q: "The sponsor says they accept the risk."
  - EN: "A sponsor can accept business risk, like slower answers or a narrower scope. Disclosing material an advisor isn't entitled to isn't theirs to accept — the access owner and compliance own that. I'd give the sponsor a date for the fixes and the rerun, and an offline demonstration of the report-specific answers in the meantime."
  - 中文：业务风险可接受，披露风险不归发起人。
- Q: "The advisor lost access an hour ago. What does your system return for the same question?"
  - EN: "No report text at all. The permission change invalidates or partitions the cached answer from the first run, entitlement is rechecked when any passage is read, and the request routes to review or returns unavailable."
  - 中文：撤销后缓存失效，读不到任何文本。

---

## II-8. Case Study: Clinical Note Drafting at Lakeside｜案例：Lakeside 临床病历起草

Source: https://www.educative.io/courses/forward-deployed-engineer/case-study-clinical-note-drafting-at-lakeside
（完整内容见 §17–§20）

**新增或不同 / What's new or different**

- 定位为**判断力与使命问题**练习；结尾带三案例复盘和备考计划。
- **最小必要原则的细化（新）**：HIPAA 的**最小必要标准 (minimum-necessary standard)** 按具体使用或披露适用；**向提供者披露或提供者为治疗而请求属于例外**——但这**不意味着**支持治疗的 AI 服务自动豁免。Lakeside 选择起草目的所需的内容（**合理时包括相关既往上下文**），由隐私法务对每条数据流分类。（第一部分 §18 简写为"发送本次就诊，不发整份病历"。）
- 使用政策同样引用 **2026-11-20 生效版本**（禁止在医疗等敏感领域无人工审核地自动化高风险动作），日期前的决定要核实当时版本；但本案不依赖它——Lakeside 对患者的义务和临床授权规则无论如何排除未审核归档。
- 发起人 (sponsor)第二次推：**指派一名运营负责人在归档后审核**——仍然是先写后审，不满足边界。
- **三案例对照表**：

| 案例 Case | 发起人要什么 Sponsor wanted | 证据显示 Evidence | 强答案 Strong answer |
|---|---|---|---|
| Meridian | 11/12 就试点，再加周末语音 | 1 个漏人工路由；3/14 升级未确认 | 修复并重验路由；离线语音 demo 而非上线 |
| Aster | 15/20 给 6 名顾问试点 | 重排器暴露 + 撤销后仍显示段落 | 先修过滤顺序和缓存；带停止规则的有条件试点 |
| Lakeside | 带标签的未审核归档 | 2/9 虚假陈述写入记录 | 拒绝归档；在测试数据上测量带来源的审核草稿 |

- **三个代价最大的错误**：把边界失败平均进质量分；把标签、handoff、引用、记录的批准当成控制（都只描述或记录，不阻止）；编造承诺（"运营会负责"在运营同意前只是提议）。
- **四周备考计划（新）**：

| 周 Week | 重点 Focus | 产物 Artifact |
|---|---|---|
| 1 | 项目故事 | **事实卡 (fact card)**：每个数字、分母、贡献、承诺状态；30 秒 / 2 分钟 / 10 分钟版本 |
| 2 | 平台 | 小型 Responses API + Agents SDK 项目，含一个审批门控动作和仓库内评测集 |
| 3 | 案例与展示 | 完整案例出声展示、计时、中途改需求 |
| 4 | 全流程 | 模拟全流程：有/无 AI 编码、技术轮、用事实卡回答使命问题 |

  始终以 recruiter 给的真实说明为准，收到后对照调整。
- 自测（新）：发起人收窄请求——**只自动归档模型标为"高置信度 (confidence)"的病历**。案例中**没有证据**表明置信度标记能区分对错病历 → 标记不是控制；按四步拒绝；写出医生批准后又编辑的病历的审核序列（编辑 → 新版本 → 旧批准失效 → 归档阻断直到医生对照转写批准新版本）；结尾说明局限：**版本绑定证明决定被记录，不证明审核认真**。

**面试怎么说 / How to say it in the interview**

- Q: "The sponsor accepts the risk and says review costs too much. What do you recommend?"
  - EN: "I'd decline automatic filing. In the replay, two of nine notes put false statements into the record, including 'no known allergies' for a patient with no allergy history, and a correction can't undo who read the note before it was fixed. The label describes that risk without stopping it. I'd offer drafts with every claim linked to the transcript and approval tied to the exact version, plus a measurement of today's documentation time so we can show whether review actually saves time. The sponsor can accept cost and schedule risk; patient safety and the hospital's clinical rules aren't theirs alone to waive."
  - 中文：拒绝 + 替代 + 测量；发起人能放弃的风险有边界。
- Q: "Then file automatically only the notes the model marks as high confidence."
  - EN: "I'd still decline that write. We have no evidence that a confidence mark separates correct notes from wrong ones — the two false notes read just as fluently — so the mark isn't a control. I'm glad to use confidence to order the review queue or highlight claims for the clinician, but the clinician still decides before anything is filed."
  - 中文：置信度可用于排序审核队列，不能替代审核。
- Q: "An operations lead will review notes after filing."
  - EN: "That's still write-then-review. The false statement is in the record, and anyone reading it before the review may act on it. The review has to happen before the write, by a clinician with the source and authority to reject."
  - 中文：事后审核仍是先写后审。
- Q: "Is the AI service exempt from minimum necessary because it supports treatment?"
  - EN: "Not automatically. Treatment disclosures to providers are an exception, but Lakeside's privacy counsel classifies each flow. I'd select what the drafting purpose needs, including relevant prior context when justified, and record that decision in the inventory."
  - 中文：不自动豁免，由隐私法务分类。

---

## II-9. Final Interviews and Mission Questions｜终面与使命问题

Source: https://www.educative.io/courses/forward-deployed-engineer/final-interviews-and-mission-questions
（安全发现处理、章程、政策层级见 §8）

**新增 / What's new**

- 开场：上午说"17 of 20"，下午说"约 90%，已在生产"——面试官会**事后对笔记**；一次不一致好解释，一天两次像模式。**预防：终面前写一张事实卡 (fact card)**——每个数字带分母、每个"我"确实是你的、每个承诺标"已做/待定"，当天所有答案都从卡上取。
- **使命类问题的五种常见形态（新）**：

| 问题形态 Question shape | 强答案包含 Strong answer contains |
|---|---|
| "Why does OpenAI's mission matter to you?" | 真实关切 + 它影响的一个决定 + 诚实的规模感 |
| "Tell me about a safety trade-off you made." | 风险、谁承担、安全选项的代价、谁决定 |
| "When have you disagreed with a decision on ethical grounds?" | 你提出的证据、如何提出、结果（包括你输了） |
| "A customer wants something you think is harmful. What do you do?" | 使命课的五个问题、你会拒绝什么、你会提供什么替代 |
| "What risk of deploying AI do you think about most?" | 与你见过的事相关的**一个具体风险**，而不是一串新闻标题 |

- 不必同意 OpenAI 的每个取舍；"I haven't settled my view on that, and here's how I'm thinking about it" 是对难题的诚实回答。
- **跨面试官一致性表（新）**：使命与价值观面试官 → 多讲为什么访问发现重要、谁承担风险；技术深度 → 边界在哪失败、修复如何强制；HM → 如何处理运营主管和安全审查。**不变**：17/20、不匹配的 14/20、2/12 访问失败、暂停。
- **中途修正夸大（新）**：自己在面试官之前纠正，是 OpenAI 看重的"乐于接受反馈"最清晰的信号。
- 使用政策引用 2026-11-20 生效版本（敏感领域高风险动作需人工审核；加审核不代表所有部署都可接受）。
- **向面试官提问（新）**：

| 问题 Question to ask |
|---|
| "What does a typical engagement look like on this team right now, from first call to handoff?" |
| "When an FDE finds a model behavior that should go to Research, what happens to it?" |
| "What's a deployment that went wrong, and what changed afterward?" |
| "How does the team decide when to say no to a customer request?" |

- 章节总结原则：**模型生成建议，应用强制决定与边界，每个声明都需要可验证的证据。**

**面试怎么说 / How to say it in the interview**

- Q: "Tell me about a safety trade-off you made."
  - EN: "In my routing pilot, access tests showed a restricted operator note to an unauthorized test identity in 2 of 12 cases. I paused that screen path and sent requests back through manual routing, which cost operators real time — they carried that cost so that other people's restricted notes stayed private. I asked the customer's operating owner and security to decide who investigates and how we verify the repair; reopening is their call, not mine alone."
  - 中文：风险、谁承担、代价、谁决定。
- Q: "When have you disagreed with a decision on ethical grounds?"
  - EN: "When the operations lead wanted to keep the screen running after the access finding. I laid out the evidence — two test cases showed restricted notes to the wrong identity — explained that reviewing routes afterward can't undo a display, and asked the operating owner and security to settle it. We paused the path; if they'd decided otherwise, I'd have documented my concern and escalated through the agreed channel."
  - 中文：证据、方式、结果。
- Q: "What risk of deploying AI do you think about most?"
  - EN: "Fluent outputs that are wrong at a boundary nobody is watching — like a draft that says 'no known allergies' when the source was silent. The grammar gives no signal, so the control has to be structural: claims tied to sources and a qualified person deciding before anything is written."
  - 中文：选一个具体风险并连到自己见过的场景。
- Q: "A customer wants something you think is harmful. What do you do?"
  - EN: "I'd ask who carries the risk, whether a human decision disappears before a high-stakes action, whether data moves without approval, and whether a label is standing in for a control. Then I'd name the one action I won't build, explain why in the customer's terms, and offer the version I will build, with what would have to be true to revisit it."
  - 中文：识别信号 → 点名拒绝 → 给替代。
- Q: (after misspeaking) "How did the access finding end up?"
  - EN: "Let me correct how I put that earlier. The access tests used test identities, and 2 of 12 showed a restricted note to the wrong identity. The 17 of 20 was a routing-accuracy review and says nothing about access. I paused the path and proposed a repair and retest; nobody has accepted the repair yet, and nothing launched."
  - 中文：主动纠正夸大。

---

## 速查 / Cheat sheet

1. **评估说明 > 官方指南 > 面经**｜Your assessment materials govern; ask the recruiter about tool/AI permission before the interview. 有/无 AI 两种都练。
2. **官方流程**｜Résumé ~1 wk → intro call → skills assessment (pair coding / take-home / tech test) → finals 4–6 h, 4–6 people, 1–2 days (virtual default, SF onsite optional) → decision ~1 wk. 不保证任何一轮。
3. **项目故事五段式**｜Customer → Problem → Build → Proof → Handoff；事实不变，深度按 30 s / 2 min / 10 min 调整；终面前写**事实卡 (fact card)**。
4. **证据带边界**｜Every number has a denominator; unmatched groups ≠ causal gain (14/20 vs 17/20); local 8/8 ≠ production; empty effect log ≠ zero effects.
5. **六维自评，不加总**｜Customer framing, ownership, technical reasoning, proof, safety, communication — fluent delivery can't cancel an unsafe release.
6. **编码轮**｜State contract + invariant first; duplicate check before assignment, completeness check before output; one fixture breaks one rule; O(n + m).
7. **先给决定**｜Lead with the decision, name the failed boundary, separate observed vs proposed, name owners or the gap, offer a narrower next step.
8. **边界在模型之前**｜Authenticate from trusted credentials → entitlement + applicability + freshness before ranking/model → bounded call → validate → human decides. Output filters and extra agents are too late.
9. **切片报告**｜Report safety slices (access, conflict, missed human route) separately from capability; incomplete = not pass; one safety failure blocks regardless of 15/20 or 11/12.
10. **标签/引用/handoff/记录的批准都不是控制**｜Label ≠ review; citation ≠ support; handoff ≠ authentication or human receipt; logged approval ≠ careful review.
11. **外部动作单独成阶段**｜Propose exact action → approve exact version → recheck at execution → idempotency key + durable dedup → receipt → reconcile before retry (timeout ≠ failure).
12. **人工升级需确认**｜Escalation = work item to a named recipient who ACKs; sent ≠ received (3/14 unacknowledged blocks launch).
13. **Responses vs Agents SDK**｜Fixed workflow / direct Responses when the app owns the loop; Agents SDK for managed turns, tools, guardrails, handoffs, sessions; multi-agent must beat a single-agent baseline on the same workload. Model proposes, application decides.
14. **成本与延迟**｜State assumptions and exclusions (e.g., $0.0278/task chat, $83.40/mo; $0.020/task, $80/mo); p95 = nearest rank on a named set with defined start/end; component p95s don't add.
15. **受监管行业**｜FINRA 3110 (supervision/WSPs), 2210 (≤25 vs >25 retail in 30 days), SEC 17a-4 (≥3 yrs, first 2 accessible), Reg BI for retail recommendations; HIPAA PHI + BAA per vendor; recording consent = state law, not HIPAA.
16. **数据副本清单**｜Inventory every copy incl. logs and backups; `store=false` only affects OpenAI's Responses state, not customer logs/backups; ZDR needs approval; no-training ≠ permission to record.
17. **对不安全请求说不（四步）**｜Acknowledge goal → name the one action you won't build → reason in their terms (patient safety, liability) → offer what you will build and measure it. Sponsor accepting risk doesn't create a control.
18. **需求变化时修订整个计划**｜Re-walk all five parts, keep original gates, add new gates, re-estimate cost, keep original deliverable, don't promise a date for the new path.
19. **使命问题**｜Link a concern you actually hold → a decision it changed → people affected and evidence; keep scale honest; Charter gives purpose, not permission.
20. **备考循环**｜Pick highest-consequence gap → produce an inspectable artifact (version, input, procedure, output, limit) → rehearse cold with a hard follow-up → review and pick next.
