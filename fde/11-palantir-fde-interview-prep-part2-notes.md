# Palantir FDE Interview Prep, Part 2: Decomposition, Learning, Re-Engineering, Design & Behavioral｜Palantir FDE 面试准备（下）：拆解、学习、重构调试、设计与行为面

> Section I: course "Palantir FDE Interview Prep" (`https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/`).
> Section II: Palantir module of "Forward Deployed Engineer for AI Systems" (`https://www.educative.io/courses/forward-deployed-engineer/`) — only what is new vs. Section I.
> Focus: experienced track（资深候选人路线）.

---

# Section I｜第一部分：Palantir FDE Interview Prep

## 1. What Decomposition Tests and How It's Scored｜拆解轮考什么、怎么评分

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/what-decomposition-tests-and-how-its-scored

### 要点 / Key ideas

- **拆解 (Decomposition)**：把一个模糊的实际问题 (ambiguous practical problem) 变成有范围、可落地的具体方案 (scoped, concrete approach)。Palantir 公开的开放题指南 (open-ended-question guidance) 强调：讲清备选方案与权衡 (alternatives and trade-offs)、得出务实方案 (pragmatic approach)、**先交付一个能跑的想法再扩展** (deliver a functioning idea before expanding it)。
- 第三方备考资料描述的是一场对话 (dialogue)：确定用户需求 (user needs)、范围 (scope)、数据 (data) 与接口 (interfaces)。这只是备考建议，**不是保证的面试合同**。FDSE（Forward Deployed Software Engineer）格式因 track 而异；有候选人报告"拆解 + coding 合并在一轮 screen"。所以不要假设固定时长、独立轮次或"不写代码"。
- 截至 2026-10-28 **没有官方拆解评分表 (no official rubric)**、分数刻度、权重或通过线。下面的五维清单是课程自创的教练工具 (course-authored coaching aid)。
- 开场例子：「帮设备借用柜台 (equipment-loan desk) 减少白跑的取件 (wasted pickup trips)」。回答 A："做一个可扩展的预测可用性 dashboard" → 只是辞藻；回答 B："谁来决定这趟值不值得跑？" → 得知前台员工需要告诉借用者"现在能不能来取" → 有用的澄清证据。**用"让用户下一步行动可构建"的可观察推理 (observable reasoning) 来评估拆解**。

**五个维度 / Five dimensions**

| 维度 Dimension | 正面证据 Positive evidence | 弱证据 Weak evidence |
|---|---|---|
| 澄清 Clarification | 识别用户与决策 (user & decision)，并**使用**有后果的答案——答案改变了工作流 | 一串没被用上的问题 |
| 优先级 Prioritization | 选出有价值、有边界的第一版 (bounded first version) + 明确排除项 (explicit exclusions)；一个用户操作 | 承诺解决所有利益相关方的问题 |
| 建模 Modeling | 实体 (entities)、标识 (identities)、关系 (relationships)、不确定数据具体化；可识别记录 + 有意义的状态 | "把数据放进数据库" |
| 执行 Execution | 模型连接到可实现的用户操作 + 可观察结果：输入、输出、具体检查 (concrete check) | 只报技术名词 |
| 迭代 Iteration | 收到反馈或检查后**真正改变一个决策**（如修改输出策略） | 承诺"以后会改进"但什么都没改 |

- 评分标签 (labels)：**demonstrated（已展示）/ partial（部分，有关键缺口）/ not evidenced（未见证据）**。每个判断都配**原话引用 + 后果** (exact quote + consequence)。**缺少证据 ≠ 没有能力** (missing evidence does not establish inability)。
- 动词很关键：asking / selecting / identifying / specifying / revising 留下不同证据；光说 "users / scope / iteration" 只是报了个类别名。

**设备借用案例对话 / Equipment-loan dialogue**

1. 面试官："Help us reduce wasted pickup trips." 候选人："Who uses the result, and what decision changes?"
2. 面试官：前台员工回答借用者"现在能取吗"；第一版两天内可行。
3. 候选人：一个柜台的员工查询 (staff lookup)；排除预约 (reservations)、需求预测 (demand prediction)、跨站点调拨 (multi-site transfers)。
4. 模型：`Item(item_id, label)`、`Loan(loan_id, item_id, checked_out_at, returned_at)`；假设 ID 稳定、loan 行有效；**未归还 loan = 该物品记录为借出**。
5. 例：I17 有 L8 且 returned_at 为空 → 借出；I18 有 L9 已归还 → 可用。`lookup(item_id)` 返回记录状态 + 数据源最后更新时间戳 (timestamp)。候选人说"这能回答现在是否可用"。
6. 面试官补充约束：**归还记录只在夜间批量到达 (nightly batch)**。候选人：撤回"现在可用"的保证；显示记录状态 + 源时间戳；陈旧 (stale)查询视为"未确认"，确认行程前要求员工实物核验 (physical verification)；并检查陈旧的 I18 不能显示为"已确认可用"。

| 维度 Dimension | 披露前 Before | 披露后 After |
|---|---|---|
| 澄清 Clarification | partial（用户与决策已知，新鲜度 freshness 未查） | demonstrated（新鲜度答案改变了员工流程） |
| 优先级 Prioritization | demonstrated | demonstrated |
| 建模 Modeling | demonstrated | demonstrated |
| 执行 Execution | demonstrated（具体操作 + 期望输出，未执行） | demonstrated（修订后的输出策略，仍需定义"陈旧"） |
| 迭代 Iteration | not evidenced | demonstrated（真正撤回了保证） |

- 核心教训：**记录状态 ≠ 当前可用性 (recorded status is not current availability)**。新鲜度策略缓解了无依据的确定性，但"陈旧"仍需操作化定义；检查未执行、影响未测量；试点 (pilot) 才能观察白跑是否减少。
- 同一回答可以同时有强项和弱项：建模强，但"now"的承诺超出了证据。**有边界的反馈 (bounded feedback)**："Your Item/Loan rule makes recorded state inspectable. Before promising current availability, establish how recently the source reflects the desk." 而不是"你缺乏用户同理心"。
- **辞藻陷阱 (polish earning execution credit)**："Segment users, calculate demand, deploy Kafka and Redis, and optimize utilization with AI." —— 没有员工决策、物品标识、新鲜度策略、查询行为、可测试的修订。追问应针对最关键的缺失证据："When the source is stale, what should the desk tell the borrower, and what data supports that?"
- 练习（取餐柜台 meal-pickup）：候选人建了 `Order(order_id, status ∈ {preparing, ready, collected})`、按 order_id 查询；面试官说"厨房数据可能晚 10 分钟"，候选人答"同一个查询就行" / "以后加缓存"。→ **缓存不会让延迟数据变新** (caching does not make delayed records current)。该问："How should staff verify a handover when the feed may be ten minutes late?" 澄清和迭代都是 partial / not evidenced。期望输出 ≠ 已观察的测试结果。

<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="200" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Five evidence dimensions｜五维证据</text>
<g fill="#eef4ff" stroke="#3b6fd8">
<rect x="10" y="50" width="130" height="70" rx="8"/><rect x="152" y="50" width="130" height="70" rx="8"/><rect x="294" y="50" width="130" height="70" rx="8"/><rect x="436" y="50" width="130" height="70" rx="8"/><rect x="578" y="50" width="130" height="70" rx="8"/>
</g>
<g text-anchor="middle">
<text x="75" y="78" font-weight="bold">Clarification</text><text x="75" y="98">澄清：用户+决策</text>
<text x="217" y="78" font-weight="bold">Prioritization</text><text x="217" y="98">优先：薄切片+排除</text>
<text x="359" y="78" font-weight="bold">Modeling</text><text x="359" y="98">建模：实体/ID/状态</text>
<text x="501" y="78" font-weight="bold">Execution</text><text x="501" y="98">执行：输入→输出→检查</text>
<text x="643" y="78" font-weight="bold">Iteration</text><text x="643" y="98">迭代：真的改决策</text>
</g>
<g stroke="#999" marker-end="url(#a)"><line x1="140" y1="85" x2="150" y2="85"/><line x1="282" y1="85" x2="292" y2="85"/><line x1="424" y1="85" x2="434" y2="85"/><line x1="566" y1="85" x2="576" y2="85"/></g>
<defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#999"/></marker></defs>
<text x="360" y="150" text-anchor="middle">Label each: demonstrated / partial / not evidenced — always with exact quote + consequence</text>
<text x="360" y="172" text-anchor="middle">每项标注：已展示 / 部分 / 未见证据 —— 必须配原话 + 后果</text>
</svg>

### 面试怎么说 / How to say it in the interview

- **When a new constraint undermines a promise**: "That changes my answer — I'll retract the 'available now' guarantee. The lookup will show the recorded status plus the source timestamp, and anything older than our freshness threshold is shown as unconfirmed, so staff verify physically before confirming a trip." ｜新约束推翻承诺时，明确撤回并改输出策略。
- **Opening move**: "Before I pick a design, who uses the result, and what decision changes for them?" ｜先问"谁用、改变什么决策"。
- **Avoid buzzword answers**: instead of naming Kafka/Redis, say "For the first version, one lookup: input item_id, output recorded state and last-update time. I'd check it on I17, which should show checked out, and I18, which should show available." ｜用输入/输出/具体检查代替技术名词。

---

## 2. A Repeatable Framework: Clarify, Scope, Model the Data, Design, Iterate｜可复用框架：澄清、定范围、数据建模、设计、迭代

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/a-repeatable-framework-clarify-scope-model-the-data-design

### 要点 / Key ideas

- 「减少错过的截止日期 (reduce missed deadlines)」是目标 (objective)；「为空闲打印机 P1 选下一个任务」是一个人能做的动作 (action)。框架把目标连到有边界的操作，并在关键假设失败时帮你修正。
- **clarify → scope → model the data → design → iterate** 是**内心的检查清单 (private checks)**，不是官方方法、也不是必须说出口的开场白。第三方建议有分歧（有的推荐结构化，有的警告别一开口就念框架）→ **结构放心里，嘴上讲具体问题**。可重复的是推理检查，路径随证据变化。

| 检查 Check | 产出 Inspectable output（P1 例子） |
|---|---|
| 澄清 Clarify | 用户 + 决策：班组长 (shift lead) 选 P1 的下一个任务；关键答案与显式假设 |
| 定范围 Scope | 推荐一个 P1 排队任务；排除自动开机、多打印机调度、截止保证 |
| 数据建模 Model the data | `Job(job_id, printer_id, due_at, status)`，每条记录一个任务，ID 可区分 |
| 设计 Design | `recommend(printer_id)`：过滤该打印机的 queued 任务 → 按 due_at、job_id 排序 → 返回第一个 + 理由，或 no candidate |
| 迭代 Iterate | 反馈或检查暴露问题时**改变**决策、规则或流程 |

- 依赖关系：用户决策里的打印机 → 决定过滤条件；临时调度策略 → 决定排序；班组长保留决定权 → 所以返回"推荐"而不是直接开机。每个检查没有固定时长。
- 何时澄清够了？用户、下一步动作、有边界的第一版都清楚后，**显式说出关键假设**："I'm assuming queued jobs have completed customer approval, due times are present, and earliest due is an acceptable first policy. Are any of those wrong?" 最早截止 (earliest due) 是**临时策略 (provisional policy)**——没有工时等约束，不能保证最优，但可理解、可检查。
- **薄切片 (thin slice)**：有边界、端到端、独立有用的能力。一张 Job 表本身不给班组长答案。
- 数据追踪 (trace)，09:00 P1 空闲：J41(P1, 10:00, queued)、J42(P1, 10:30, queued)、J43(P2, 09:30, queued) → 先排除 J43（属于 P2），返回 **J41** + 理由 "earliest due queued job for P1"。J43 虽更早也不能越过打印机边界。
- 新约束：queued 任务可能缺客户审批 (customer approval)；J41 缺失审批；**missing 或 unknown 审批都必须阻止推荐**。修订**向后**追溯到"可选资格 (eligibility)"的含义，再**向前**改结果：
  - 澄清改变：missing 和 unknown 都阻止。
  - 模型改变：加 `approval_state ∈ {approved, missing, unknown}`。
  - 规则改变：要求指定打印机 + `status = queued` + `approval_state = approved`，**先过滤资格再排序**。
  - 输出改变：返回 **J42**，理由 "earliest due approved queued job for P1"。J41 保留为可检查的 blocked + 原因，不删除、不默认视为已审批。
- 范围（一台打印机推荐）不变；模型、规则、输出因依赖被推翻的假设而改变。**结构靠修复依赖维持，而不是按顺序走完五步**。
- 反模式 (anti-pattern)："我会 clarify/scope/model/design/iterate。需要 ingestion、dashboard、全车间调度；审批以后迭代再说。" 若仍推荐 J41 → 输出不合格。说出未来功能 ≠ 改变了决策。

**区分资格与排序的走查用例 / Discriminating walkthroughs**

| 用例 Case | 期望 Expected | 抓住的 bug Catches |
|---|---|---|
| J41 missing, J42 approved | J42 | 基本资格过滤 |
| J41 改为 unknown | 仍 J42 | 只拒绝字面值 "missing" 的规则 |
| J41 改为 approved | J41（更早） | 排序是否仍正确 |
| J43 approved 且更早 | 不属于 P1 | 打印机边界 |
| 没有 queued+approved 的 P1 任务 | "no eligible job"，不回退到 blocked | 空队列时回退破坏资格限制 |

- 这些是**期望走查结果，不是已执行测试 (expected walkthrough results, not executed tests)**；截止改善未测量，之后试点才能观察。
- 不念稿的结构化：讲因果决策 ——"Since the shift lead chooses one P1 job, I'll start with that recommendation. Approval changes eligibility, so I'll filter before ranking." 自选检查点看：用户、切片、记录、操作、具体检查——推进最弱的关键部分。面试官已给出用户和范围就直接用，不要再走通用问卷。

<svg viewBox="0 0 720 210" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="210" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Revised path: filter eligibility before ranking｜先过滤资格再排序</text>
<defs><marker id="b" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<g fill="#f3f7ee" stroke="#5a8f29">
<rect x="10" y="60" width="120" height="56" rx="8"/><rect x="155" y="60" width="130" height="56" rx="8"/><rect x="310" y="60" width="150" height="56" rx="8"/><rect x="485" y="60" width="110" height="56" rx="8"/><rect x="615" y="60" width="95" height="56" rx="8"/>
</g>
<g text-anchor="middle">
<text x="70" y="84">recommend(P1)</text><text x="70" y="102">请求</text>
<text x="220" y="84">Job records</text><text x="220" y="102">任务记录</text>
<text x="385" y="80">printer=P1, queued,</text><text x="385" y="96">approval=approved</text><text x="385" y="111">资格过滤</text>
<text x="540" y="84">sort due_at, id</text><text x="540" y="102">排序</text>
<text x="662" y="84">J42 + reason</text><text x="662" y="102">推荐+理由</text>
</g>
<g stroke="#555" marker-end="url(#b)"><line x1="130" y1="88" x2="153" y2="88"/><line x1="285" y1="88" x2="308" y2="88"/><line x1="460" y1="88" x2="483" y2="88"/><line x1="595" y1="88" x2="613" y2="88"/></g>
<line x1="385" y1="116" x2="385" y2="150" stroke="#c0392b" marker-end="url(#b)"/>
<rect x="290" y="152" width="190" height="40" rx="8" fill="#fdecea" stroke="#c0392b"/>
<text x="385" y="170" text-anchor="middle">J41 blocked (missing approval)</text><text x="385" y="186" text-anchor="middle">保留可见，不删除</text>
<text x="662" y="150" text-anchor="middle">Shift lead decides</text><text x="662" y="166" text-anchor="middle">班组长决定是否开机</text>
</svg>

**练习：维修台 (repair desk) 参考答案**

- 题：调度员 (dispatcher) 需要技术员 (technician) T1 的下一个维修；两天内可行。R11(T1, 11:00, queued)、R12(T1, 12:00, queued)、R13(T2, 10:00, queued)。
- 第一版：`Repair(repair_id, technician_id, due_at, status)`；过滤 queued 的 T1 维修 → 按 due_at、repair_id 排序 → 返回第一个 + 理由；排除自动派单 (auto-dispatch)、多技术员调度、延误减少保证。期望 **R11**（R13 属于 T2）。
- 新约束：维修可能在零件到达前排队；R11 `parts_state = waiting`，R12/R13 ready；waiting 或 unknown 都阻止派单。→ 加 `parts_state ∈ {ready, waiting, unknown}`，要求 T1 + queued + ready → 期望 **R12**；R11 可见为 blocked。R11 改 unknown 仍 R12；无 ready 的 T1 维修 → "no eligible repair"，绝不回退。
- 心法：问自己"**哪个不确定的答案会改变选中的结果**？"——那就是值得花时间的澄清。

### 面试怎么说 / How to say it in the interview

- **Stating assumptions before tracing**: "I'll start with one next-job recommendation for P1 from the existing job records. I'm assuming queued jobs are already approved, due times are present, and earliest-due is acceptable as a first policy — is any of that wrong?" ｜先说出关键假设，请面试官纠正。
- **Repairing after a broken assumption**: "Since approval can be missing or unknown, eligibility changes: I'll add an approval_state field and filter to approved jobs before ranking. That moves the answer from J41 to J42, and J41 stays visible as blocked with its reason — I won't silently treat unknown as approved." ｜假设被推翻时，向后改资格、向前改输出。
- **Walkthrough checks**: "I'd walk through five cases: missing, unknown, approved-and-earlier, a job on another printer, and an empty eligible queue — that last one makes sure we return 'no eligible job' rather than falling back to a blocked one." ｜用区分性用例检查修订。

---

## 3. The Ideation Phase: Asking About Users, Data and Constraints｜构思阶段：问用户、数据与约束

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/the-ideation-phase-asking-about-users-data-and-constraints

### 要点 / Key ideas

- 「帮我们减少内涝 (reduce flooding)」：先问"用哪个云？"还是"**谁根据这些信息行动、他能改变什么？**"——后者决定整个方案边界。**澄清值得花时间的条件：答案会改变你本来要做的决策**。
- **私下测试 (private test)**：为一个问题想两个合理答案，说出你在两种情况下会做什么不同。若无差别，问题可以等。权限与安全问题即使不改变排序，也可能确立强制边界 (mandatory boundaries)。
- 有后果的澄清问题：其答案会改变 **用户、动作、范围、证据解读、运营行为或成功指标** (user, action, scope, evidence interpretation, operational behavior, success measure)。

**三个依赖链 / Three dependencies（诱人承诺 → 问答 → 修订边界 → 撤回承诺）**

| # | 诱人承诺 Tempting claim | 问与答 Question & answer | 修订边界 Revised boundary | 撤回 Withdrawn claim |
|---|---|---|---|---|
| 1 | 全市内涝优化 | 谁能行动？协调员 (coordinator) 每天下午看邮件报告，选**最多 6 个**次日巡检点 (inspection locations)；先一个区，3 天交付 | 支持一个区的次日巡检选择 | 该用户能执行应急响应或基建改造 |
| 2 | 用排水口标签数堵塞资产 | D12 标签验证过吗？没有，是员工猜的 | 带"未决身份 (unresolved identity)"审阅报告；O71、O72 分开显示为"可能相关 @P4" | 记录能证明"两个堵塞排水口"或"唯一的 D12" |
| 3 | 现场报告实时告警 (real-time alerts) | 数据何时到？离线工作，**18:00 UTC** 回站上传，可能已晚一天 | 晚间审阅、次日规划；**观测时间与上传时间分开显示** | 数据反映当前内涝或支持紧急实时干预 |

- 引导问题："Walk me through the last time someone chose an inspection location. What information did they have, and who made the final choice?"（让面试官讲上一次真实流程）。再问"哪些漏巡或无效巡检最重要？"防止"更好的可见性 (better visibility)"代替结果。
- 数据：O71（09:00, P4, 有照片, 暂定 D12）、O72（09:10, P4, 暂定 D12）、O73（11:00, P9, 描述格栅堵塞, 无照片无排水口 ID）。
- **观测 (observation)** = 记录的事件/报告；**识别 (identification)** = 关于它涉及哪个实体/类别的主张。
- **数据可用性 (data availability)** 包括：**来源 (provenance)、覆盖 (coverage)、新鲜度 (freshness)、权限 (permissions)、实际可访问 (practical access)**。"数据集可能存在"不能证明任何一项。问："Who recorded these? How were pins and asset labels assigned? When do records become visible, which areas are covered, and may the coordinator view the photos?" 答：允许查看的员工报告；资产标签是猜测；覆盖跟随员工路线；上传可能晚一天。
- 来源信息支持事后审查，但**不证明报告正确**。O73 缺 ID 仍是有用证据，删除就丢掉了巡检线索。**没有观测 ≠ 不存在 (missing observations are not evidence of absence)**。物种编目同理：两次目击 = 两条观测，不等于两个物种或两个个体；暂定物种标签可修订，原始观测与来源保留。
- 约束塑形：6 个/天的容量 (capacity)限制选择数；不变的员工路线限制采集能揭示什么。若真需紧急实时决策，此数据源不够 → **重新谈判承诺**，不要假设以后会有新传感器。
- 反面提案："全市装传感器、实时 dashboard、把 O71/O72/O73 计为三个堵塞排水口、优化路线减少 30% 内涝。" 问题：未授权的安装与采集；把上传报告当当前状态；虚构资产计数；无依据的 30%。错误会叠加——虚构计数放上 dashboard 也不会变可信；更快处理不会让延迟数据变实时。另一个安静的失败：**问了十个问题，提案却原封不动**。
- **成功指标 (success measure)** 需要：定义的总体 (population)、时间窗 (time window)、测量来源 (measurement source)。**护栏 (guardrail)**：追踪主指标可能掩盖的不可接受副作用。
- 首版协议："One coordinator reviews available reports after the depot upload, chooses up to six locations for tomorrow and records report dispositions with unresolved identity visible. One district, due in three days."
- **5 个工作日试点**：
  - 主指标：截止前可用报告中，在次日巡检名单定稿前获得审阅处置 (review disposition) 的比例 = 已审阅合格报告 / 截止前所有可用报告（用可用时间、审阅记录、名单定稿时间）。
  - 处置定义：选中 (selected)、带理由延后 (deferred with reason)、需澄清 (needs clarification)。
  - 护栏：因错误匹配导致的重复地点巡检；超过 1 个工作日未处理的报告。
  - 尚无基线 (baseline)，更快审阅 ≠ 内涝减少。

<svg viewBox="0 0 720 230" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="230" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Each answer reshapes scope｜每个答案都在收窄范围</text>
<defs><marker id="c" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<rect x="10" y="45" width="160" height="60" rx="8" fill="#fdecea" stroke="#c0392b"/>
<text x="90" y="70" text-anchor="middle">"Reduce flooding"</text><text x="90" y="90" text-anchor="middle">减少内涝（目标）</text>
<g fill="#eef4ff" stroke="#3b6fd8"><rect x="200" y="40" width="150" height="70" rx="8"/><rect x="370" y="40" width="150" height="70" rx="8"/><rect x="540" y="40" width="170" height="70" rx="8"/></g>
<g text-anchor="middle"><text x="275" y="62">Who acts?</text><text x="275" y="80">coordinator, 6 visits</text><text x="275" y="98">谁行动：协调员</text>
<text x="445" y="62">Labels verified?</text><text x="445" y="80">no → unresolved ID</text><text x="445" y="98">身份未决</text>
<text x="625" y="62">When does data land?</text><text x="625" y="80">18:00 UTC, ≤1 day late</text><text x="625" y="98">晚间批量上传</text></g>
<g stroke="#555" marker-end="url(#c)"><line x1="170" y1="75" x2="198" y2="75"/><line x1="350" y1="75" x2="368" y2="75"/><line x1="520" y1="75" x2="538" y2="75"/></g>
<line x1="625" y1="110" x2="625" y2="140" stroke="#555" marker-end="url(#c)"/>
<rect x="110" y="145" width="600" height="70" rx="8" fill="#f3f7ee" stroke="#5a8f29"/>
<text x="410" y="168" text-anchor="middle">First version: one district, evening review, pick ≤6 visits, unresolved identity visible</text>
<text x="410" y="188" text-anchor="middle">首版：一个区、晚间审阅、选≤6个点、身份未决可见</text>
<text x="410" y="206" text-anchor="middle">Measure: % reports dispositioned before list finalized; guardrails: duplicate visits, stale reports</text>
</svg>

**练习：改善城市交通 (Improve city traffic)**

- 背景：候选人报告中出现过"改善纽约交通"和政府方向新毕业生"收集某星球上生命数据"的题目。练习指南建议选**有可测结果、利益相关方 (stakeholders)利益冲突**的运营问题。
- 答案包：走廊运营主管 (corridor operations supervisor) 可批准**一次可逆的信号配时试验 (reversible signal-timing trial)**，两个路口，工作日 07:00–09:00 UTC；不能控制导航 App 或改道路；现有聚合车流量与行人等待观测**次日到达**；两周试点不能装新传感器；走廊更快可能增加行人等待或把排队推到邻近居民街。
- 参考答案（≤200 词）：主管批准并审阅一次两路口的可逆试验；次日数据只用于评估，不做实时控制；在选"平均车辆延误 (mean vehicle delay)"做主指标前，**先问现有观测能否估算它并支持可比基线**——不能就换一个有数据支撑的更窄指标或可行的人工抽样；开始前约定行人等待与邻街排队的观测计划、可接受上限与**回滚标准 (rollback criteria)**；若邻街影响无法观测，这个不确定性必须改变试验协议——没有报告不代表无伤害；排除全市优化、导航控制、道路改造、实时自适应控制；尚未测得任何改进。
- 被审计的错误说法：①"计数里包含车辆行程时间，所以平均延误不用检查可行性"（答案包没说）；②"缺失观测安全规则允许把未观测的邻街排队当 0"（编造的权威）；③"最短路径 (shortest path)推荐解决拥堵，试验已证明无行人伤害"（没有测量）。

### 面试怎么说 / How to say it in the interview

- **Opening for "Improve city traffic"**: "Before I propose anything, who would act on this — a signal-operations team, a planner, or a navigation provider? If it's signal operations, I'd scope a reversible timing trial on one corridor; if it's a planner, I'd focus on a study with longer horizons. And what data arrives, and how fast — live or next day?" ｜先问谁行动，并说明不同答案会导向不同方案。
- **Pushing back on live claims**: "Since field reports land at the 18:00 depot upload and can be a day old, I'd withdraw the live-alert idea and design an evening review for next-day planning, showing observation time and upload time separately." ｜数据延迟时撤回实时承诺。
- **Handling uncertain identity**: "O71 and O72 are both at P4 with a tentative D12 label, so I won't merge them or count two drains — I'll show them as possibly related pending review, and keep O73 even without an asset ID because it's still a lead." ｜身份不确定时不合并、不删除。
- **Defining success**: "For a five-day pilot, my primary measure is the share of reports available by the evening cutoff that get a recorded disposition before tomorrow's list is final. Guardrails are duplicate visits from bad matching and reports left unresolved for more than a working day. That measures better review — not less flooding, which we haven't shown." ｜指标要有总体、时间窗、来源，外加护栏。

---

## 4. The Execution Phase: Data Models, APIs and Where an Algorithm Fits｜执行阶段：数据模型、API 与算法放在哪

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/the-execution-phase-data-models-apis-and-where-an-algorithm

### 要点 / Key ideas

- 一张"UI, API, database"的框图不能告诉另一个工程师点"Assign"后发生什么。**可执行计划 (executable plan)** 必须说明：谁能操作、哪些事实一起变、重试后保留什么、调用方收到什么。
- 场景：一个仓库 (depot) 的设备维保队列；注册表 (registry) 每 15 分钟刷新；协调员控制分派 (assignment)；承包商 (contractor) 只看自己被分派的工作；排除预测性维护、回写注册表。
- 第三方指南：执行 = 涉及数据与 API 的高层设计，在可用输入支持时才放算法/模型。

**数据模型 / Data model（行粒度 row grain + 稳定键 stable keys）**

| 表 Table | 粒度 Grain | 键与关系 Keys & relationships |
|---|---|---|
| `Asset(asset_id, serial, location, active, registry_version)` | 一个规范设备资产 (canonical asset) | PK asset_id |
| `SourceLink(source_system, source_record_id, asset_id)` | 一个源记录 → 规范资产的映射 | (source_system, source_record_id) 唯一；FK asset_id |
| `ServiceTask(task_id, asset_id, due_at, state, assigned_team_id, task_version)` | 一个维保任务 | PK task_id；FK asset_id；一个资产多个任务 |

- 数据：R44 → A17（SN-88, Bay-2, active, registry v11）；R45 → 非活跃 A18。任务 T90(A18, 08:00)、T91(A17, 09:00)、T92(A17, 10:00)，都 open、未分派、task v3。**NULL assigned_team_id = 未分派，不是 team 0**。缺必填字段 → import issue。
- T91/T92 是 A17 上不同的工作，不是重复资产。新源记录带 SN-88 只是**匹配候选 (match candidate)**——源 ID 标识的是源记录，匹配到设备需要有依据、可审查的映射。

**API 契约 / API contract**：`POST /service-tasks/T91/assignment`，body `{team_id: K3, expected_task_version: 3, request_id: Q8}`；调用者必须是该 depot 的授权协调员。API 契约 = 允许的调用者、输入、校验、输出、错误、状态变化；**接口暴露行为，不是暴露表**。

一个事务 (one transaction) 内：
1. 校验 (validation)：设备 active、任务 open、团队被允许、版本匹配；与并发更新协调，保证校验的状态在提交时仍成立。
2. T91 分派给 K3，state = assigned，task_version = 4。
3. 持久化 Q8 的 payload 身份与提交结果，追加最小审计事件 (minimal audit event)。
4. 提交后返回已提交任务与版本。

| 情况 Case | 行为 Behavior |
|---|---|
| 未授权 Unauthorized | 拒绝，不泄露任务细节（**先鉴权 (authorization)再披露 (disclosure)**） |
| 相同 Q8 + 相同 payload 重试 | 返回存储的结果，不再修改、不再写审计 |
| Q8 复用但输入不同 | 拒绝 |
| 新请求但 expected version 过期 | 冲突 (conflict)，不修改 |
| 业务输入非法 | 校验错误 (validation error) |

- 重放键 (replay key) 按认证调用者 + 操作限定作用域，唯一性持久保证。**幂等 (idempotent)**：重复操作的效果等同于执行一次。重放检查、版本检查、状态变化必须协调；**"恰好一次投递 (exactly-once delivery)"的说法替代不了它们**。

**事实归属 / Fact ownership**

| 持久事实 Persistent fact | 负责者 Owner |
|---|---|
| Asset.serial / location / active / registry_version | 注册表权威导入 (registry-authoritative import) |
| ServiceTask.state / assigned_team_id / task_version | 服务应用 (service application) |
| 已审阅的 SourceLink 映射 | 应用管理的身份审查 (identity review) |
| 导入完成状态与被拒记录 issue | 导入器维护的运行状态 (importer run state) |
| Q8 payload 身份与提交结果 | 应用的事务性重放记录 (transactional replay record) |

- 关系型存储负责持久化，**不决定业务权威**。注册表与应用可以贡献同一屏但保持各自权威 → 决定哪个更新可以改哪些列。
- **同步 vs 异步 (synchronous vs asynchronous)**：分派与鉴权同步（协调员需要已提交的答案）；注册表轮询异步（每 15 分钟）。
- 首版只要：一个应用 + 关系型存储 + 定时导入器。导入运行有可见状态 pending/running/succeeded/failed；被拒记录单独记 issue；显示**最后一次成功刷新时间**（描述记录数据，不是物理现状）。重放记录保留声明的重试窗口（本设计 7 天），过期后旧 expected version 仍能阻止重复修改。**队列或独立服务在首版不增加必要行为**。
- **算法放哪 (where an algorithm fits)**：决策是"建议下一个任务"。确定性规则足够：过滤 open 且资产 active 的任务 → 按 due_at、task_id 升序 → 返回一个或 no eligible task。T90 最早但 A18 非活跃 → **T91**。一个 `ORDER BY` 就够；建议本身不做分派。没有行程时间输入或路线决策 → 加模型不会改善操作。

**防止注册表 v12 清掉 K3 / Field-level authority**

- 注册表拥有 serial/location/active；应用拥有任务 state 与分派。`registry_version` 排序资产的注册表变更，`task_version` 排序本地任务变更，**都不是导出时间戳 (export timestamp)或到达时间**。
- 完整走查（设计走查，非执行测试）：

| 步骤 Step | 结果 Result |
|---|---|
| 初始建议 | 返回 T91，不改行 |
| Q8 分派 | T91 → K3, task v4；A17 仍 Bay-2 v11；存储并返回 Q8 结果 |
| 相同 Q8 重试 | 返回原 v4 结果，无新行/审计 |
| 并发旧命令 (expected v3) | 冲突；T91 仍 K3 v4 |
| R44 v12（移到 Bay-4） | 原子更新 (atomic update) A17 location=Bay-4, registry v12；**保留 T91 的 K3 与 v4** |
| 重复 v12 / 旧 v11 | 相同 v12 no-op；v11 不能回滚 (roll back)；**同版本不同内容 → 隔离为可见冲突 (quarantine)** |

- 测验答案：最终 **T91 → K3, task v4；A17 Bay-4, registry v12；两次重试都不改变**。
- 其他分支规则：未知身份 → 挂起待映射审查，不按 serial 静默合并；v13 删除标记 → A17 置 inactive，保留关联任务，给协调员提 issue；schema 问题 → 隔离缺必填字段或不支持的 schema 版本，新增可选字段只在显式兼容规则下忽略；**每日对账 (daily reconciliation)** → 用完整源快照比对映射、版本、删除标记，**不能因无法解释的缺失就推断删除**。
- 诱人实现："按最新时间戳 upsert 整个对象" → 延迟导出可能带旧的"未分派"值但时间戳更新，清掉 K3；未保护的重试可能再发一条通知。修复：字段级权威 (field-level authority) + 持久重放处理；若加通知，把带唯一 ID 的通知意图 (notification intent) 与分派一起持久化并去重 (deduplicate)投递。

**输出威胁模型 / Output threat model**：识别接收者、可访问信息、可能的辅助知识 (auxiliary knowledge)、不希望的泄露。K3 只能看自己被分派的工作，不能看别队工作或内部故障备注。

```json
{
  "task_id": "T91",
  "location": "Bay-4",
  "due_at": "2026-10-29T09:00:00Z",
  "state": "assigned"
}
```

- 服务端从认证推导团队身份 → 过滤到 K3 的分派 → **序列化前投影允许字段 (project permitted fields before serialization)**。T92 未分派不出现；省略 serial、内部备注、无限制资产 ID、原始源 payload。
- 在所有读写处都鉴权，包括**导出与日志**。最小权限 (least privilege)：操作、记录、字段都限于任务需要；审计记录也要最小且访问受限。**在浏览器里隐藏备注是失败的——网络响应已经泄露了**。
- K3 可能认得 Bay-4 的设备 → 去掉 serial **不提供匿名保证 (anonymity guarantee)**；访问控制和审计也不能证明伦理或合规。若禁止基于位置的推断，输出契约必须改。
- 规范 ID 仍需有依据的匹配；队列仍允许重试与乱序；登录仍允许从披露字段推断 → **用有序走查证明正确性，不是组件名**。

<svg viewBox="0 0 720 250" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="250" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Sync assignment vs async import｜同步分派 vs 异步导入</text>
<defs><marker id="d" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<rect x="10" y="50" width="120" height="50" rx="8" fill="#eef4ff" stroke="#3b6fd8"/><text x="70" y="72" text-anchor="middle">Coordinator</text><text x="70" y="90" text-anchor="middle">协调员 POST</text>
<rect x="160" y="40" width="250" height="70" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
<text x="285" y="60" text-anchor="middle">Service app (1 transaction)</text><text x="285" y="78" text-anchor="middle">authz → replay? → version → write</text><text x="285" y="96" text-anchor="middle">鉴权→重放→版本→原子写</text>
<rect x="440" y="90" width="150" height="80" rx="8" fill="#f7f1e3" stroke="#a67c00"/>
<text x="515" y="115" text-anchor="middle">Relational store</text><text x="515" y="133" text-anchor="middle">assets, links, tasks,</text><text x="515" y="151" text-anchor="middle">replay, audit, runs</text>
<rect x="160" y="170" width="250" height="60" rx="8" fill="#f3f7ee" stroke="#5a8f29"/>
<text x="285" y="192" text-anchor="middle">Scheduled importer (15 min)</text><text x="285" y="212" text-anchor="middle">only registry-owned fields 只改注册表字段</text>
<rect x="610" y="170" width="100" height="60" rx="8" fill="#f3f7ee" stroke="#5a8f29"/><text x="660" y="195" text-anchor="middle">Registry</text><text x="660" y="213" text-anchor="middle">注册表</text>
<rect x="610" y="40" width="100" height="50" rx="8" fill="#fdecea" stroke="#c0392b"/><text x="660" y="62" text-anchor="middle">K3 view</text><text x="660" y="80" text-anchor="middle">服务端过滤</text>
<g stroke="#555" marker-end="url(#d)"><line x1="130" y1="75" x2="158" y2="75"/><line x1="410" y1="90" x2="440" y2="110"/><line x1="410" y1="195" x2="440" y2="160"/><line x1="610" y1="200" x2="412" y2="200"/><line x1="560" y1="90" x2="608" y2="65"/></g>
<text x="285" y="128" text-anchor="middle" font-size="12">returns only after commit 提交后才返回</text>
</svg>

**练习：校准计划 (Independent Calibration Plan) 参考答案**

- 题：仪器 I6 ↔ 注册表 L8（v4, Lab-A, active）；校准 C31 open、未分派、task v2、due 2026-10-30T12:00Z。注册表拥有 room 与 active；应用拥有校准状态与分派。协调员用请求 U5、expected v2 把 C31 分派给供应商 V2；随后注册表 v5 把 I6 移到 Lab-B；又来两次相同 v5；最后来 v4。V2 只能看到其分派的校准 ID、房间、到期时间、状态。唯一决策是手动分派。
- 记录：`Instrument(instrument_id, room, active, registry_version)`；`SourceLink((source_system, source_record_id) unique → instrument_id)`；`Calibration(calibration_id, instrument_id, due_at, state, assigned_vendor_id NULL=unassigned, task_version)`。
- 契约：`POST /calibrations/C31/assignment {vendor_id: V2, expected_task_version: 2, request_id: U5}` → 原子分派、state=assigned、v3、持久化 U5 结果与审计 → 返回已提交结果。未授权拒绝；非法输入拒绝；版本过期冲突；窗口内相同 U5 返回存储结果；U5 换输入拒绝。
- 走查：U5 → V2, v3；v5 原子移 Lab-B，只推进 registry version；两次相同 v5 no-op；迟到的 v4 不能回滚；C31 始终 V2 v3。
- V2 投影：`calibration_id: C31, room: Lab-B, due_at: 2026-10-30T12:00:00Z, state: assigned`；房间仍可能识别仪器 → 不作匿名承诺。
- 算法：**唯一决策是手动分派时不需要优化算法**；但校验、鉴权、重放规则仍必须有。

### 面试怎么说 / How to say it in the interview

- **Describing the assign endpoint**: "POST to the task's assignment resource with team_id, expected_task_version and a request_id. In one transaction I check authorization, look up the request_id for a replay, check the version, then write the assignment, the replay result and an audit event together. A retry with the same request_id gets the stored result; a stale version gets a 409 with no change." ｜讲清一个事务内的鉴权、重放、版本、原子写。
- **Field-level ownership**: "The registry owns location and active; the app owns assignment. So the importer only updates registry-owned columns, ordered by registry_version — not by export timestamp — which means a late export can never clear K3's assignment." ｜按字段划分权威，按版本号排序，不按时间戳。
- **When to skip the algorithm**: "The decision is 'suggest the next task', and the inputs are due time and asset status, so a filter plus ORDER BY due_at, task_id is enough. I'd only reach for optimization if we had travel times and a routing decision to make." ｜输入支持什么就用什么，简单规则优先。
- **Output security**: "The server derives the team from the auth token, filters to its assignments and projects only task_id, location, due_at and state before serializing. Hiding notes in the UI doesn't count — the network response would still leak them. And I wouldn't claim anonymity, because location can identify the equipment." ｜服务端过滤 + 字段投影，不承诺匿名。

---

## 5. Practice: Cataloging Species in an Unfamiliar Environment｜练习：在陌生环境中编目物种

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/practice-cataloging-species-in-an-unfamiliar-environment

### 要点 / Key ideas

- 背景：候选人报告过"构建收集某星球生命数据的系统"这类题（政府方向新毕业生）。练习建议 25 分钟时间盒 (timebox)。
- **English problem statement**: "Design a first-version species catalog that helps a research lead review field evidence and choose tomorrow's follow-up observations. It must stay useful when labels change, phones are offline and evidence is incomplete."
- 答案包 (answer packet)：

| 维度 Dimension | 给定条件 Given |
|---|---|
| 用户与决策 User & decision | 一位研究负责人 (research lead) 每晚审阅一个山谷的观测，选**最多 3 个**次日跟进地点 |
| 人员设备 People & equipment | 训练过的观察员 (observers)用现有手机、现有路线；5 个工作日出首版 |
| 连接 Connectivity | 野外离线 (offline)，**18:00 UTC** 回基地上传 |
| 证据 Evidence | 时间、位置（有时有）、备注、可选照片；标签是暂定的 (provisional)，照片不一定有 |
| 限制 Limits | 无新传感器、路线、实验室分析、外部物种库 |
| 访问 Access | 只有参与的野外团队与负责人 |

- → 选**晚间证据审阅目录 (evening evidence-review catalog)**；穷尽式生物多样性测量、自动发现、实时追踪都超出输入。
- 数据：

```text
O201: observer U1, device D1, 2026-10-27T09:00:00Z, location L4, photo P201, tentative "striped glider"
O202: observer U2, device D2, 2026-10-27T09:08:00Z, location L4, photo P202, tentative "striped glider"
O203: observer U1, device D1, 2026-10-27T11:00:00Z, location unknown, no photo,
      notes "three small winged forms", no identification
Event A: server accepts O201, response lost; D1 resends identical O201
Event B: 2026-10-28T08:00:00Z lead reviews P202 and changes O202 to "unresolved"
```

- O201 与 O202 可能是同一个体、同物种不同个体、或不同物种——数据包没有定论。

**诱人但错误的 schema / Tempting schema**：`Species(name PRIMARY KEY, location, photo, last_seen)` 按名字 upsert、把 dashboard 行数当发现的物种数。失败点：O201/O202 同标签互相覆盖；O201 重试使独立累加的计数虚高；O202 改成 "unresolved" 会抹掉原始主张或制造一个"新物种"；O203 没名字直接消失。

**正确模型：分离投递身份、观测身份、生物学识别 (delivery identity / observation identity / biological identification)**

| 记录 Record | 粒度与字段 Grain & fields |
|---|---|
| `Observation` | 每次目击一行：observation_id (PK, 设备生成), observer_id, device_id, observed_at, location_id (nullable), notes, photo_ref (nullable), source_record_ref, received_at |
| `IdentificationDecision` | 每个归属的主张或修订一行（**追加式 append-only**）：decision_id, observation_id, label (nullable), status, actor_id, decided_at, reason；观察员初始主张存为 provisional；O203 显式 unidentified |
| `ReviewDisposition` | 每个观测一个当前规划处置：follow-up selected / deferred with reason / needs clarification；历史保留，维护 review version |
| `UploadReceipt` | 每个被接受的观测身份一个持久回执 (durable receipt)：规范化 (normalized)提交内容 + 已提交结果；保留整个试点重试周期 |

**两个服务端操作 / Two server operations**

- `POST /observations`：设备生成的稳定 ID + 采集字段 + 可选初始识别主张。
  - 认证观察员，校验团队成员资格、设备关联、字段格式、证据引用访问权。
  - 允许缺少识别/照片/位置并可见标记；缺 observation ID 或观测时间 → 拒绝并要求修正。
  - **先原子持久化观测 + 初始主张 + 回执，再确认成功 (persist before acknowledge)**；首次接受时设 received_at。
  - 相同重试：返回已有回执（比较规范化内容，排除服务端生成字段）；同 ID 不同内容：可见冲突，不覆盖；事务性唯一约束 (unique constraint)防止并发重试 (concurrent retries)建两行。
- `POST /observations/{id}/review`：expected review version + 可选识别决策 + 带理由的处置。只有负责人可提交；先鉴权 (authorization)再返回细节；版本过期冲突不改动；原子追加识别决策与审阅历史、更新处置、推进版本。
- 本地状态 (local capture states)：saved → awaiting acknowledgement → acknowledged / failed-conflicted。未确认数据在断网与重启后持久保存。显示待传记录、未解决失败、最后成功上传信息——**服务端无法枚举滞留在离线手机上的记录**。
- 组件：一个带持久本地存储的应用 + 一个服务端存储；无需队列、识别模型或优化系统。没有标注训练集或可靠物种参考 → 人工审阅；置信度 (confidence)数字或图像模型不能证明物种真相。

**有序走查 / Ordered trace（期望设计结果，非执行测试）**

| 步骤 Step | 结果 Outcome |
|---|---|
| O201 首次投递 | 持久化 1 个观测 + U1 暂定主张 + 回执；响应丢失，D1 保留 pending |
| O201 相同重试 | 返回已有回执；D1 标记 acknowledged；观测数仍为 1，received_at 不变 |
| O202 投递 | 第二个观测 + U2 主张；相似标签/位置/时间**不足以合并** |
| O203 投递 | 第三个观测：位置未知、无照片、无识别；"three small winged forms" 作为备注保留，不推导物种或个体数 |
| 晚间审阅 | 选 L4（关联 O201 证据）；O202 deferred "L4 already selected"（避免重复规划但不合并）；O203 needs clarification |
| O202 修订 08:00 | **追加**负责人的 unresolved 决策（actor、时间、理由如"P202 区分特征不足"）；保留 U2 原始主张、P202、源引用、原始时间戳；推进 review version；O201 不变 |

- 结果：3 个观测；**既不证明 3 个物种，也不给出可靠物种/个体数**；未知仍未知；未访问区域不是"不存在"的证据。
- **试点指标**：18:15 UTC 前已确认、且在 19:00 定稿前有处置的观测 ÷ 18:15 前所有已确认观测；分母 (denominator)为 0 时报告 0 分母；护栏：最老的未处置观测、未解决的上传失败；离线设备上的观测排除在服务端分母外，单独报告已知本地待传。
- 权衡 (trade-off)：可行的每日证据流程 vs 延迟可见性；审阅完成率不等于生物多样性知识提高。

<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="220" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Observation vs identification (append-only)｜观测与识别分离（只追加）</text>
<defs><marker id="e" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<rect x="20" y="50" width="200" height="120" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
<text x="120" y="72" text-anchor="middle" font-weight="bold">Observation O202</text>
<text x="120" y="94" text-anchor="middle">U2, D2, 09:08Z, L4</text><text x="120" y="114" text-anchor="middle">photo P202, source ref</text><text x="120" y="134" text-anchor="middle">immutable 原始证据不变</text>
<rect x="280" y="45" width="200" height="50" rx="8" fill="#f3f7ee" stroke="#5a8f29"/>
<text x="380" y="66" text-anchor="middle">Decision #1 (U2, provisional)</text><text x="380" y="84" text-anchor="middle">"striped glider" 暂定</text>
<rect x="280" y="120" width="200" height="50" rx="8" fill="#fff4e0" stroke="#a67c00"/>
<text x="380" y="141" text-anchor="middle">Decision #2 (lead, 10-28 08:00)</text><text x="380" y="159" text-anchor="middle">"unresolved" + reason</text>
<g stroke="#555" marker-end="url(#e)"><line x1="220" y1="90" x2="278" y2="70"/><line x1="220" y1="120" x2="278" y2="145"/><line x1="380" y1="95" x2="380" y2="118"/></g>
<rect x="530" y="70" width="175" height="80" rx="8" fill="#fdecea" stroke="#c0392b"/>
<text x="617" y="94" text-anchor="middle">Current view</text><text x="617" y="114" text-anchor="middle">= latest decision</text><text x="617" y="134" text-anchor="middle">history kept 历史保留</text>
<line x1="480" y1="145" x2="528" y2="120" stroke="#555" marker-end="url(#e)"/>
<text x="360" y="200" text-anchor="middle">Relabeling never overwrites the sighting; O203 stays with label = null (unidentified)</text>
</svg>

### 面试怎么说 / How to say it in the interview — full walkthrough script

> **Clarify (1–2 min)**: "Before I design anything, who uses this catalog, and what do they decide with it? … OK — one research lead, each evening, picks at most three follow-up locations for tomorrow. And how does data get to us — are phones online in the field? … Offline, with an upload at base at 18:00 UTC. Are the species labels reliable? … Provisional. And is there an external species database or an image model I can lean on? … No. That tells me this is an evidence-review tool, not an automated species detector."
>
> **Scope**: "So the first version, in five days, is: offline capture on existing phones, an acknowledged upload at 18:00, an evening review screen, and a list of up to three follow-up locations. I'm explicitly excluding biodiversity counts, automated identification and live tracking — the inputs can't support them."
>
> **Model**: "The key modeling decision is to separate the sighting from the interpretation. An Observation row is one recorded sighting, keyed by a device-generated observation_id, with observer, device, observed_at, nullable location and photo, notes and a source reference. IdentificationDecision is an append-only table — each claim or revision is a new row with label, status, actor and reason. So the observer's first label is just a provisional decision, and O203 is valid with no label at all. Then a ReviewDisposition per observation — selected, deferred with reason, or needs clarification — with a review version, and an UploadReceipt per accepted observation ID."
>
> **API**: "Two operations. POST /observations persists the observation, the initial claim and the receipt in one transaction and only then acknowledges. An identical retry returns the existing receipt; the same ID with different content is a visible conflict, never an overwrite. POST /observations/{id}/review takes an expected review version, so a stale edit conflicts, and only the lead can call it."
>
> **Trace**: "If O201's response is lost, the phone keeps it as awaiting-ack and retries; the server returns the stored receipt, so we still have one observation. O202 at the same spot eight minutes later stays separate — similar label and place don't justify a merge. O203 is kept with unknown location as a needs-clarification lead. In review, the lead selects L4 and defers O202 because L4 is already selected — that avoids a duplicate visit without merging records. When the lead changes O202 to unresolved, I append a decision; U2's original claim and photo are untouched."
>
> **Measure & trade-off**: "For the pilot I'd measure the share of observations acknowledged by 18:15 that get a disposition before the list is finalized at 19:00, with guardrails on the oldest undisposed observation and unresolved upload failures. The trade-off is that daily uploads mean delayed visibility — this tells us review is happening, not that we know more about biodiversity, and three observations are not three species."

中文要点：先问用户与决策、连接与标签可靠性 → 定为晚间证据审阅 → 观测与识别分表（识别只追加）→ 先持久化后确认 + 幂等回执 → 走查重试/不合并/保留不完整 → 指标与护栏 → 承认延迟可见性。

---

## 6. Practice: Improving City Traffic｜练习：改善城市交通

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/practice-improving-city-traffic

### 要点 / Key ideas

- 候选人报告（2026-09-07）："Design a system to improve traffic in NYC." 练习用 25 分钟时间盒。
- **English problem statement**: "Improve traffic across the city. Produce one defensible traffic plan, then revise it when a favorable headline result conceals worse outcomes for other stakeholders."

| 维度 Dimension | 答案包 Answer packet |
|---|---|
| 权限 Authority | 交通运营主管 (traffic operations supervisor) 可批准一次可逆试验，用**已经工程批准的配时预设 (timing preset)**，走廊 C1（路口 I1、I2）；不能改道路、控制导航 App |
| 对比 Comparison | 试验 T1：两周工作日 07:00–09:00 UTC；第一周 Preset A（基线 (baseline)），第二周 Preset B |
| 证据 Evidence | 聚合车流量、走廊排队快照、行人等待观测、邻近居民街 R1 排队快照——**次日到达** |
| 时间表 Schedule | 每早 5 个观测时隙：07:00, 07:25, 07:50, 08:15, 08:40；I1/I2 测排队与行人等待，R1 测排队 |
| 资源 Resources | 无新传感器、无单车追踪、无新采集路线、无实时数据 |
| 流程 Workflow | 主管审阅延迟证据，记录 continue / revert / hold for clarification；**现有授权运营流程**执行预设切换并记录确认；应用**不操作信号灯** |

- → 有边界的证据审阅 + 试验决策流程。最短路径算法或吞吐优化器既没输入也没权限。

**验收条件 / Acceptance conditions（试点条件，不是通用交通安全标准）**

| 指标 Metric | 定义 Definition | 阈值 Threshold |
|---|---|---|
| 主指标 Primary | I1/I2 预定快照的平均观测排队车辆数 = 排队车辆总和 / 有效快照数 | 较基线降低 ≥ 15% |
| 行人护栏 Pedestrian guardrail | 平均行人等待 | ≤ 45 s |
| 居民街护栏 Residential guardrail | R1 平均排队 | ≤ 6 辆 |
| 覆盖 Coverage | 每周：50 个走廊排队快照（5 早 × 5 时隙 × 2 路口）、50 个行人等待、25 个 R1 快照；与均值分开报告 | 必须完整 |

- **缺失测量保持未知，绝不填 0**。保留观测窗口、观测时间、接收时间、源引用。车流量只是背景，单独不能证明行程时间、排队或拥堵减少。

**数据模型 / Data model**

| 记录 Record | 说明 Notes |
|---|---|
| `Site(site_id, site_kind, corridor_id)` | I1、I2 属于 C1；R1 是邻街站点 |
| `Preset(preset_id, approval_ref)` | A、B 都是已批准预设 |
| `Trial(trial_id, corridor_id, baseline_preset_id, candidate_preset_id, observation_windows, acceptance_conditions)` + version + review/application state | T1 引用 C1、A、B；存日期化 UTC 窗口与时隙 |
| `Observation(observation_id, site_id, metric_kind, observed_at, value nullable, unit, source_ref, received_at)` | 一个站点一个时间一个指标的一次源测量；稳定源观测 ID 防止重复投递虚增总数 |
| `TrialDecision(decision_id, trial_id, actor_id, evidence_refs, decision, reason, decided_at, expected_trial_version)` | 归属的决策，引用审阅过的证据 |
| `ApplicationConfirmation` | 关联决策 → 运营请求、目标预设、确认引用、确认生效时间 |

- 覆盖率 = 预定时隙 vs 已接受有效观测；**缺行或 null 值都算覆盖缺口**。observed_at 与 received_at 分开（今天收到的可能描述昨天）。冲突内容可见审查；未知站点映射保持未决，不猜。
- **读契约**：`GET /trials/T1/review` 先鉴权 (authorization)，返回证据摘要、有效分母、期望与已收覆盖、窗口、源引用、新鲜度 (freshness)、当前试验版本、待生效状态。
- **写契约**：`POST /trials/T1/decisions`（决策、理由、证据引用、expected trial version）→ 校验 (validate)决策值、证据关系、覆盖、验收条件；**无依据的 continue 校验失败；证据不完整支持 hold**；原子持久化并推进版本；过期版本冲突；未授权不返回细节；返回已提交决策与生效状态，**不声称信号已改变**。
- 导入异步 (asynchronous)；审阅读取与决策校验同步；预设切换在应用外由运营流程执行，确认后回写。

**为什么 25% 改善仍需回退 / Why a 25% improvement requires reverting**

| 指标 Metric | 基线 Baseline | 候选 Candidate | 结果 Result |
|---|---|---|---|
| 走廊排队 Corridor queue | 600/50 = 12 辆 | 450/50 = 9 辆 | (12−9)/12 = **−25%**，超过 15% 目标 ✔ |
| 行人等待 Pedestrian wait | 1750/50 = 35 s | 2600/50 = **52 s** | 超过 45 s 上限 ✘ |
| R1 排队 R1 queue | 100/25 = 4 辆 | 200/25 = **8 辆** | 超过 6 辆上限 ✘ |

- 主指标改善但**两个护栏在完整覆盖下都失败** → 试点违反利益相关方契约。主管记录 **revert**，关联证据，通过授权运营流程请求恢复 A。确认到达前显示 **"reversion requested"**，只有确认才是 **"restored to A"**。次日证据不能承诺即时发现或自动防止伤害。
- 反模式 (anti-pattern)：dashboard 显示"交通改善 25%，保留 B"（隐藏护栏失败）；记录 revert 后立即显示"A 已恢复"（越过人工生效边界）；把缺失的行人样本当 0（压低均值、掩盖覆盖缺口）。
- 期望检查：完整证据 → 护栏失败建议；缺一个行人观测 → 覆盖不完整，不能有依据地 continue；相同源投递 → 总数不变；过期决策 → 冲突；未确认的回退 → 保持 pending。
- 短期前后对比**不能证明因果 (causation)**：两周之间需求、事故等条件可能不同。

<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="200" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Decision ≠ request ≠ confirmed change｜决策≠请求≠已生效</text>
<defs><marker id="f" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<g fill="#eef4ff" stroke="#3b6fd8"><rect x="10" y="60" width="150" height="70" rx="8"/><rect x="190" y="60" width="150" height="70" rx="8"/><rect x="370" y="60" width="160" height="70" rx="8"/><rect x="560" y="60" width="150" height="70" rx="8"/></g>
<g text-anchor="middle">
<text x="85" y="85">Next-day evidence</text><text x="85" y="103">queue 9, ped 52s,</text><text x="85" y="120">R1 8 → guardrails fail</text>
<text x="265" y="85">TrialDecision</text><text x="265" y="103">"revert" + evidence</text><text x="265" y="120">记录决策</text>
<text x="450" y="85">Ops request</text><text x="450" y="103">"reversion requested"</text><text x="450" y="120">请求中（应用不控灯）</text>
<text x="635" y="85">Confirmation</text><text x="635" y="103">"restored to A"</text><text x="635" y="120">确认后才显示</text>
</g>
<g stroke="#555" marker-end="url(#f)"><line x1="160" y1="95" x2="188" y2="95"/><line x1="340" y1="95" x2="368" y2="95"/><line x1="530" y1="95" x2="558" y2="95"/></g>
<text x="360" y="170" text-anchor="middle">Missing samples = unknown, never 0｜缺失样本是未知，不是 0</text>
</svg>

### 面试怎么说 / How to say it in the interview — full walkthrough script

> **Clarify**: "'Improve traffic across the city' is an objective, so first: who can actually act, and what levers do they have? … A traffic ops supervisor who can approve one reversible trial with an already-approved timing preset on corridor C1 — no road redesign, no navigation apps. What data do we get, and when? … Aggregate counts, queue snapshots, pedestrian waits and queue snapshots on the residential street R1, all arriving the next day. And who applies a preset change? … An existing ops process. Then my system doesn't touch signals — it supports a review-and-decide workflow."
>
> **Scope**: "First version: a two-week A/B on C1, weekday mornings 07:00 to 09:00, preset A then preset B, with a review screen where the supervisor records continue, revert or hold. Out of scope: citywide optimization, routing algorithms, live adaptive control and road changes."
>
> **Metrics**: "Primary measure: mean observed corridor queue at I1 and I2 across the scheduled snapshots — total queued vehicles over valid snapshots — with a target of at least a 15% reduction. Two guardrails, because a faster corridor can hurt others: mean pedestrian wait at most 45 seconds and mean R1 queue at most six vehicles. And coverage reported separately: 50 corridor snapshots, 50 pedestrian observations and 25 R1 snapshots per week. A missing measurement stays unknown — I never fill in zero."
>
> **Model & API**: "Observation is one source measurement of one metric at one site and time, with observed_at and received_at kept apart and a stable source ID so duplicate deliveries don't inflate totals. TrialDecision records who decided what, against which evidence, with an expected trial version. A separate confirmation record tracks whether ops actually applied the change. GET /trials/T1/review returns the summaries, denominators, coverage and freshness; POST /trials/T1/decisions validates the decision against coverage and the acceptance conditions — so 'continue' fails validation if a guardrail fails or coverage is incomplete."
>
> **Revision with the feedback numbers**: "Baseline queue is 600 over 50, so 12; candidate 450 over 50, so 9 — a 25% reduction, which beats the target. But pedestrian wait goes from 35 to 52 seconds, over the 45 cap, and R1 goes from 4 to 8 vehicles, over the 6 cap. Both guardrails fail with complete coverage, so the recommendation is revert. The supervisor records revert with the evidence, the app shows 'reversion requested', and only when ops confirms does it show 'restored to A'."
>
> **Limits**: "Two things I can't promise: next-day data means we can't detect harm immediately, and a one-week-versus-one-week comparison doesn't prove causation — demand or incidents might differ between weeks."

中文要点：权限决定范围（一次可逆试验）→ 主指标 + 两个利益相关方护栏 + 覆盖率 → 缺失不填 0 → 决策/请求/确认三态分离 → 25% 改善但护栏失败 → 回退 → 承认延迟与因果局限。

---

## 7. Practice: Syncing Two Record Systems and Sharing Data Without Oversharing｜练习：同步两个记录系统，并在不过度共享的前提下共享数据

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/practice-syncing-two-record-systems-and-sharing-data-without

### 要点 / Key ideas

- 候选人报告汇编里出现过"同步两个员工记录系统"这类拆解题。
- **English problem statement**: "HR record H17 (department Operations, active true, HR revision 10) and Workplace record W62 (room R2, readiness pending, Workplace revision 7) are both linked by a reviewed mapping to employee E41. Make subsequent changes predictable across both systems, and give a room-preparation vendor only the information it needs for assigned work."

| 维度 Dimension | 答案包 Answer packet |
|---|---|
| 用户 User | 一个办公室的工位协调员 (workplace coordinator)，需要可靠的房间准备工作 |
| 权威 Authority | **HR 拥有** display name、department、active；**Workplace 拥有** room、readiness；双方各自存对方字段的镜像 (mirrors) |
| 身份 Identity | H17、W62 经审阅关联到 E41；**源记录身份 ≠ 员工身份**；同名不能成为新关联的依据 |
| 访问 Access | 被分派的准备供应商只看允许的 open 工作，不能浏览员工 |
| 资源 Resources | 5 分钟轮询 (polling) + 每日对账快照 (reconciliation snapshot)；无实时数据、无新源访问 |
| API 保证 | 导入 schema v1；目标 API 提供持久重放识别 + 带修订号检查的镜像写入 (revision-checked mirror writes) |

- 最小方案：为已审阅映射同步两组各自拥有的字段，暴露被分派的 open 准备工作。排除：模糊自动身份合并 (fuzzy automatic identity merging)、薪资、任意双向编辑、物理删除 (hard deletion)、瞬时传播。
- 一周试点指标：已接受的受支持变更在本地接受后 **10 分钟内**在目标端反映的比例；失败、未决映射、源覆盖陈旧 (stale)单独报告；该指标看不到轮询从未拿到的变更。
- **整行"最后到达者赢 (last-arrival-wins)"同步立即失败**：W62 r8 带旧镜像 Operations，会覆盖 Finance；回写会造成回声循环 (echo loop)；之后带 active=true 的 Workplace 行还会"复活"已离职员工。
- **每个所有者推进自己的事实；镜像只搬运，不成为新权威**。HR r11 和 Workplace r8 是独立序列，比较它们的数字或到达时间无法判断谁拥有 department。

**持久记录 / Persistent records**

| 记录 Record | 键 Key | 内容 Content |
|---|---|---|
| `Employee` | employee_id | 当前组合后的员工状态 |
| `SourceLink` | (source_system, source_record_id) | → 已审阅的 employee_id |
| `AcceptedState` | (employee, owning system) | 已接受的所有者修订号 + 规范化的自有字段内容（用于比较 payload 身份） |
| `PendingWrite` | (destination, durable propagation identity) | payload + pending/acknowledged |
| `SyncIssue` | — | 映射、schema、对账、内容冲突，待审 |
| `PreparationTask` | task_id | → employee；assigned vendor、room、state、task version |

- 组件：最小导入器 + 持久存储 + 传播 worker (propagation worker)。异步导入器校验认证来源、schema v1、映射与自有字段；一个事务内协调修订/内容比较、accepted state、员工/任务变更、待传播；**同一 owner state 的并发导入必须串行化 (serialized)**。
- 镜像写：`PUT /source-systems/{source_system}/employees/{source_record_id}/mirrors`，输入：owner origin、owner revision、owned-field projection、由 (employee, owner, revision, destination) 派生的稳定操作 ID。非法所有权拒绝；ID 复用但内容变 → 冲突；相同重试返回存储结果；旧镜像修订不能替换新的。
- **只有目标端已提交响应后才标记 acknowledged** → 目标端提交后响应丢失可安全重试。本地已接受状态、待传播、已确认目标状态分别可检查。允许暂时的镜像滞后 (mirror lag)，但保留权威；要求两系统同时提交会增加不必要依赖。

**基线投递账本 / Baseline delivery ledger**（假设期间无目标确认）

| # 投递 Delivery | 已接受 HR | 已接受 Workplace | 新增/累计 pending | Issue | V3 可见 |
|---|---|---|---|---|---|
| 0 初始 | r10 Operations, active | r7 R2, pending | — | — | P501 / R2 / pending |
| 1 HR r11 Finance | r11 Finance | r7 R2 | A / A | — | P501 / R2 / pending |
| 2 WP r8 R4（镜像 Operations） | r11 Finance | r8 R4 | B / A+B | 陈旧镜像被排除 | P501 / **R4** / pending |
| 3 相同 HR r11 | 不变 | 不变 | — / A+B | 无 | 同上 |
| 4 迟到 HR r10 | 不变 | 不变 | — / A+B | 记录：忽略陈旧投递 | 同上 |
| 5 HR r11 声称 Legal | 仍 Finance | 不变 | — / A+B | **同修订号内容冲突，可见** | 同上 |

- 镜像回声带原始 owner/revision → 识别为传播，不产生新的 owner 变更。

**续：离职与异常输入 / Inactivity & exceptional inputs**

| 投递 Delivery | HR/活跃 | Workplace | Pending | Issues | V3 输出 |
|---|---|---|---|---|---|
| HR r12 显式 inactive | r12 Finance / **false** | r8 R4 | +C+D | Legal 冲突仍待审 | `[]` |
| WP r9 room R5 | r12 / false | r9 R5 | +E | 同上 | `[]` |
| 未映射 W63（同名） | 不变 | 不变 | 不变 | **未决映射**（不按名字合并） | `[]` |
| 不支持的 schema 版本 | 不变 | 不变 | 不变 | 隔离 schema issue | `[]` |
| 每日快照缺 H17 | 不变 | 不变 | 不变 | **对账 issue**（不推断删除） | `[]` |
| 源轮询失败 | 不变 | 不变 | 不变 | 源失败；显示最后成功刷新 | `[]` |

- 内部结果 Finance / R5 / inactive。保留删除权威 (retained deletion authority) 防止旧行或非所有者行复活 E41。**显式 inactive 标记、快照中无法解释的缺失、物理删除请求三者处理方式不同**。保留映射与最小修订/删除状态，遵循批准的保留规则；物理删除需单独授权流程。
- **供应商读 / Vendor read**：`GET /vendor/preparation-tasks`（单条查询与导出同一策略）。序列化前：从认证推导 V3 并授权 → 检查当前已接受的员工活跃状态、任务 open、分派给 V3 → 只投影允许字段。
  - R4 之后：只返回 `task_id: P501, room: R4, preparation_state: pending`；省略员工/源 ID、姓名、部门、原始 payload。
  - HR r12 之后：P501 **本地取消**，task version 推进一次，即使取消的传播仍 pending，供应商读也不再返回。
  - 鉴权 (authorization)/资格检查与响应构造要协调——**陈旧缓存的员工行不能授权披露**。
- 拉整行员工数据再在浏览器隐藏姓名 → 响应和其他导出路径都泄露。最小审计事件记录 actor、operation、outcome、time，不复制受限 payload。供应商可能从 R4 + 辅助知识 (auxiliary knowledge)认出人 → 承诺的是"窄授权访问"，不是匿名。
- 授权撤回检查：P502 属于 V4，认证的 V3 通过 endpoint 和 export 请求 → 都不返回 P502 细节；拒绝审计不含受限内容。

<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="240" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Field ownership sync｜按字段所有权同步</text>
<defs><marker id="g" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<rect x="10" y="45" width="170" height="80" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
<text x="95" y="68" text-anchor="middle" font-weight="bold">HR (H17)</text><text x="95" y="88" text-anchor="middle">owns: name, dept, active</text><text x="95" y="108" text-anchor="middle">HR 拥有</text>
<rect x="10" y="145" width="170" height="80" rx="8" fill="#f3f7ee" stroke="#5a8f29"/>
<text x="95" y="168" text-anchor="middle" font-weight="bold">Workplace (W62)</text><text x="95" y="188" text-anchor="middle">owns: room, readiness</text><text x="95" y="208" text-anchor="middle">Workplace 拥有</text>
<rect x="250" y="80" width="200" height="110" rx="8" fill="#fff4e0" stroke="#a67c00"/>
<text x="350" y="104" text-anchor="middle" font-weight="bold">Importer + store</text><text x="350" y="124" text-anchor="middle">AcceptedState per owner</text><text x="350" y="144" text-anchor="middle">compare owner revision only</text><text x="350" y="164" text-anchor="middle">镜像字段不参与比较</text>
<rect x="520" y="45" width="190" height="60" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
<text x="615" y="70" text-anchor="middle">Worker → PUT mirrors</text><text x="615" y="88" text-anchor="middle">ack after dest commit</text>
<rect x="520" y="140" width="190" height="80" rx="8" fill="#fdecea" stroke="#c0392b"/>
<text x="615" y="163" text-anchor="middle">GET /vendor/prep-tasks</text><text x="615" y="183" text-anchor="middle">{task_id, room, state}</text><text x="615" y="203" text-anchor="middle">inactive → hidden 离职即隐藏</text>
<g stroke="#555" marker-end="url(#g)"><line x1="180" y1="90" x2="248" y2="115"/><line x1="180" y1="180" x2="248" y2="160"/><line x1="450" y1="115" x2="518" y2="80"/><line x1="450" y1="160" x2="518" y2="175"/></g>
</svg>

### 面试怎么说 / How to say it in the interview — full walkthrough script

> **Clarify**: "Who uses the synced data, and for what decision? … A workplace coordinator preparing rooms in one office. Which system is authoritative for which fields? … HR owns name, department and active; Workplace owns room and readiness, and each mirrors the other. How are records linked to a person? … Reviewed mappings — and a matching name isn't enough. And what does the vendor need? … Only its assigned open work."
>
> **Scope**: "So the first version syncs the two owned field groups for reviewed mappings and exposes assigned open prep tasks to vendors. I'm excluding fuzzy auto-merging, arbitrary two-way editing, payroll, physical erasure and instant propagation — we poll every five minutes, so I'll measure the share of accepted changes reflected at the destination within ten minutes."
>
> **The core design decision**: "Last-arrival-wins on whole rows breaks immediately: Workplace revision 8 carries a stale mirrored 'Operations' and would overwrite HR's 'Finance'. So I store accepted state per owner: HR's revision and its owned fields, Workplace's revision and its owned fields. An import from Workplace can only change Workplace-owned fields; its mirror of department is ignored. Revisions are compared within one owner's sequence — never across systems, never by arrival time."
>
> **Trace**: "HR 11 sets Finance and queues a mirror write. Workplace 8 sets R4; its mirrored Operations is excluded, so Finance survives. A duplicate HR 11 is a no-op, a late HR 10 is ignored, and a second HR 11 claiming Legal is a visible same-revision conflict — Finance stays. HR 12 marks E41 inactive: P501 is cancelled locally, and the vendor stops seeing it right away even though the cancellation hasn't propagated yet. Workplace 9 can still update the room to R5, but can't reactivate E41."
>
> **Propagation**: "A worker PUTs mirrors with owner, owner revision and a stable operation ID, and marks it acknowledged only after the destination commits — so a lost response is just a safe retry, and older mirror revisions can't overwrite newer ones."
>
> **Vendor output**: "The vendor endpoint derives V3 from auth, checks the employee is active, the task is open and assigned to V3, and returns only task_id, room and preparation state — filtered server-side, same policy for exports. And I'd be honest that a room number can still identify someone, so this is least-privilege access, not anonymity."
>
> **Exceptions**: "An unmapped record with a matching name goes to mapping review; an unsupported schema is quarantined; a record missing from the daily snapshot raises a reconciliation issue rather than being treated as a deletion; and a polling failure shows the last successful refresh so the coordinator knows agreement is unconfirmed."

中文要点：按字段定权威 → 每个 owner 独立修订序列 → 镜像不参与比较 → 重复/迟到/冲突各有处理 → 离职立即对供应商隐藏 → 目标提交后才确认 → 服务端投影最少字段 → 缺失 ≠ 删除。

---

## 8. How the Learning Round Works｜学习轮怎么进行

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/how-the-learning-round-works

### 要点 / Key ideas

- 开场可能是："这是一个你没用过的小库，第一个任务后我们会加需求。" 成功不取决于认识这个库，而是**弄清给定规则的含义、应用它们、让修订可见**。准备目标是**可观察的理解与适应 (observable understanding and adaptation)**，不是猜技术栈。
- Palantir 公开的早期人才 (early-talent) 时间线把**学习轮 (learning)** 列为 onsite 面试之一——但不代表所有 FDSE 候选人都是这个格式。
- 候选人报告：2025-12 政府 FDSE——拿到数据库 schema 和文档，按文档实现函数；2022-07 软件工程师——分阶段读应用代码、讨论局限、写修复（不同岗位）。汇编（2026-09-23）提醒政府/商业/实习/社招格式不同，**向 recruiter 确认**。
- 熟悉能省时间，但**导入熟悉工具的行为也会造成错误**。关键问题：你能否准确解释给定行为，以至于能预测接下来会发生什么？

**任务族 / Task family（不是脚本）**

| 活动 Activity | 留下的证据 Evidence |
|---|---|
| 接收概念/文档/现有代码 | — |
| 解释有边界的初始理解 | 复述 (restatement) 你要用的规则 |
| 应用到小任务 | 具体预测输出 (predicted output) |
| 回应纠正或新约束 | 能执行时对比预测与结果 |
| 用所学扩展方案 | 纠正后的新预测证明理解改变 |

**练习：`pick(records, predicate, limit)`**

- 契约 (contract)：从 index 0 按输入顺序**最多检查 (examine) limit 条记录**，返回其中满足 predicate 的，不修改输入；limit 为正整数。
- 记录：A(ready=false)、B(true)、C(true)、D(true)；limit=2 求 ready。
- 候选人错误预测 `[B,C]`（"前两个 ready 的"）→ 导入了**结果上限 (result limit)** 假设；契约是**扫描上限 (scan limit)**。正确：检查 A（拒绝）、B（返回），停在 C 前 → `[B]`。注意：选"只检查 B 返回 [B]"是**用错误模型得到正确输出**——说出被检查的记录才能暴露差异。
- 纠正后的说法："I treated it as a result limit. It is a scan limit: A consumes one slot and B consumes the second, so only B is returned; C is not examined." 再迁移到 limit=3 → `[B,C]`（检查 A、B、C，D 未检查）。
- 不要只说"懂了"（理解仍不确定）、不要反复道歉（浪费时间）、不要为熟悉语义辩护（忽视契约）。**推理预测 ≠ 执行测试**；能运行就对比实际行为并调查分歧。

**扩展契约：`pick(records, predicate, limit, start)`**

- `0 <= start <= len(records)`；检查 `start .. min(start+limit, len)-1`；`start == len` 时不检查；返回匹配项 + `next_start = min(start+limit, len)`；**`next_start == len` 时恰好耗尽 (exhausted)**；不改输入。
- start=0, limit=2 → `([B], 2)`，2≠4 未耗尽；续：start=2 → 检查 C、D → `([C,D], 4)`，**耗尽**。
- 两个不完整纠正的诱人实现：
  - **按匹配数推进 (advance by number of matches)**：返回 1 个匹配就从位置 1 续 → 再次返回 B。扫描已经消耗 2 个位置，与匹配数无关。
  - **短结果即停 (stop after a short result)**：匹配数 < limit 就停 → 漏掉 C、D。结果大小不说明是否还有未检查位置。

```python
def pick(records, predicate, limit, start=0):
    # Scan limit: count examined positions, not matches.
    if limit <= 0 or not (0 <= start <= len(records)):
        raise ValueError("invalid limit or start")
    end = min(start + limit, len(records))
    matches = [r for r in records[start:end] if predicate(r)]
    next_start = end                      # advance by positions examined
    exhausted = next_start == len(records)
    return matches, next_start, exhausted
```

- 新练习 W(false)、X(true)、Y(false)、Z(true)，limit=3：另一候选人预测 `[X,Z]`（"一直找到 3 个 ready 或到末尾"）→ 错。正确：检查 W、X、Y → `[X]`, next_start=3，未耗尽；续 start=3 → 检查 Z → `[Z]`, next_start=4，耗尽；输入不变。**Y 不贡献匹配但决定了从哪里续**——讲解跳过 Y 说明你还在偷偷数匹配。
- 被拒绝的假设：扫描可以持续直到填满匹配额度。
- 准备方法：诚实说明已知与未知，锚定给定规则，预测有边界的结果；纠正后**说出被拒绝的假设并在变化的用例上演示替代规则**。提问与被纠正既不自动等于失败，也不保证通过。

### 面试怎么说 / How to say it in the interview

- **Naming your prior**: "I've used a different API where limit caps the number of results. Here the docs say it caps examined records, so I'll count positions, not matches." ｜说出你带入的熟悉假设，再改用文档规则。
- **After a correction**: "Got it — I was treating it as a result limit. Under a scan limit, A uses one slot and B the second, so the result is [B] and C isn't examined. With limit 3 it'd be [B, C], and D still isn't examined." ｜纠正后说出被拒绝的假设并迁移到新用例。
- **Continuation**: "next_start is start plus limit, capped at the length — it advances by positions examined, not by matches. So the next call starts at 2, returns [C, D], next_start 4, and that equals the length, so we're exhausted. A short page doesn't mean we're done." ｜续页按检查位置推进，短结果不代表结束。
- **Prediction vs. run**: "That's my predicted trace; if I can run it, I'll check it against the actual output before calling it done." ｜区分推理预测与实际运行。

---

## 9. Reading Docs Fast and Asking the Right Questions｜快速读文档、问对问题

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/reading-docs-fast-and-asking-the-right-questions

### 要点 / Key ideas

- 任务："从前三条输入记录里选 ready 的任务，并发评估，发布一份完整有序报告——否则保留旧报告。" 文档目录：Overview、Query operators、Missing fields、Execution、Examples。快速找规则 = **把每个需求路由到管它的契约 (route each requirement to the governing contract)**。

| 任务需求 Requirement | 先看哪节 First section |
|---|---|
| 从前三条输入记录选 (first three) | Query operators + **Overview**（要先确定输入顺序） |
| 缺失 ready 算不算 (absent ready) | Missing fields |
| 报告保持选中顺序 (preserve order) | Execution: report ordering |
| 只发布完整成功的报告 (publish only complete) | Execution: completion, success, publication |

**任务驱动阅读循环 / Task-directed reading loop**

1. 确定需要的行为 (identify required behavior)
2. 找到相关契约和例子 (locate contract & examples)
3. 用自己的话复述语义 (restate semantics)
4. 探测能区分不同解释的边界 (probe a discriminating edge)
5. 能运行就做最小使用 (run a minimal use)
6. 根据证据修正模型 (revise model)

- 速度来自缩小契约搜索范围 + 测试最关键的假设。**例子只在其假设下演示行为，不提供未写明的顺序、缺失值、修改、完成或失败保证**。
- 候选人报告：文档驱动的 schema + 函数任务；2022-10 一份汇编描述"自定义包安装器 (custom package installer)，多仓库 + 多线程 + Python 并发工具"。

**文档包 / Packet**：O1 每条记录一个 job（唯一 job_id），输入有序；Q1 阶段从左到右执行，`take(n)` 保留当前序列前 n 条；M1 `keep_ready` 只保留 ready **显式为 true** 的，丢弃 false 和缺失；Q2 两个操作都保持顺序、返回 job 记录、不改输入。
- 输入 J1(ready 缺失)、J2/J3/J4(true)。`take(3)` → [J1,J2,J3]，`keep_ready` 去掉 J1 → **[J2,J3]**。先过滤再 take 会得到 [J2,J3,J4]——错误地包含 J4（改变了 take 接收的序列）。**SQL 语义不会自动迁移**；缺失不自动等于 false/0/空串。

**哪个问题值得问 / Which question deserves clarification**

- ✘ "缺失 ready 会保留吗？"——M1 已写明。复述 M1 并用 J1 做区分探测。
- ✔ "如果上游给的是无序记录，哪个顺序定义前三条？"——不同答案改变选择（但 O1 已解决）。
- ✔ "一个评估失败时，成功的行是否替换旧报告的一部分？"——若发布语义未定义就该问。
- **有用的澄清：指出一个未决规则，并说明不同答案如何改变实现或期望输出**；文档矛盾或确实不清也值得问。
- 执行契约：E1 worker 返回评估值，完成顺序不受约束，报告顺序跟随选中输入顺序；E2 每个选中任务都成功后才发布，任何失败都保留旧报告、不部分替换；E3 **单一协调者 (single coordinator) 拥有发布权**，worker 不改报告状态；失败后仍观察每个任务的结果用于诊断。
- 契约到检查记录 (contract-to-check record)：规则与位置（Q1）→ 预测 → 最小探测（J1）→ 未决问题。

**并发：futures 与共享状态 / Futures & shared state**

- **共享状态 (shared state)**：多任务可访问的可变状态。**不变量 (invariant)**：可见报告要么是旧的完整报告，要么是新的完整成功报告，**绝不是进行中的混合**。
- **Future**：异步 (asynchronous)任务的最终结果。`submit` 只是调度并返回 future，不代表完成；J3 可能比先提交的 J2 先完成。
- Python 3.12 `concurrent.futures`：`Future.result()` 必要时等待，返回值或**抛出任务的异常**；`wait(futures)` 默认 `ALL_COMPLETED`，等到终态 (terminal state)（包括失败），但**自己不重新抛出 worker 异常** → "wait 返回了"不能作为发布依据。
- 所有权：worker 返回值不改报告；协调者按选中顺序保存 futures、取回每个结果、构建本地候选 `[(J2,20),(J3,30)]`；全部成功才发布完整快照；有异常 → 观察其余结果用于诊断、丢弃候选、保留 `[(J0,9)]`。（这是进程内有界报告，不是分布式事务 (distributed transaction)。）
- **同步 (synchronization)**：若 worker 分别写结果和追加完成 ID，读者可能只看到其一——即使每个操作都线程安全 (thread-safe)。**锁 (lock)必须覆盖整个保持不变量的操作，读者也要遵守同一协议**；锁住单次赋值边界就错了。

**不用 sleep 验证 / Event-based verification without sleeps**

1. J2 发 start 事件，然后阻塞在 release 事件上。
2. J3 返回 30。
3. 测试等待 J2 start 和 J3 future 完成。
4. J2 仍阻塞时，可见报告必须仍是 `[(J0,9)]`。
5. 释放 J2，协调完成后期望 `[(J2,20),(J3,30)]`（尽管完成顺序相反）。
6. 再跑一遍 J3 抛错：两个都终态后 wait 正常返回，但取 J3 结果会抛 → 旧报告必须仍可见。

```python
from concurrent.futures import ThreadPoolExecutor, wait
from threading import Event, Lock


class ReportStore:
    """Whole-snapshot store: readers and publishers share one lock."""

    def __init__(self):
        self._lock = Lock()
        self._report = [("J0", 9)]

    def read(self):
        with self._lock:
            return list(self._report)

    def publish(self, report):
        with self._lock:
            self._report = list(report)


def refresh(selected_ids, evaluate, store, on_submitted):
    candidate = []
    diagnostics = []
    with ThreadPoolExecutor(max_workers=2) as workers:
        pairs = [(job_id, workers.submit(evaluate, job_id)) for job_id in selected_ids]
        on_submitted(dict(pairs))
        wait([future for _, future in pairs])   # terminal outcomes, NOT success
        for job_id, future in pairs:            # selected order, not completion order
            try:
                value = future.result()         # re-raises the worker exception
            except Exception as error:
                diagnostics.append((job_id, error))
            else:
                candidate.append((job_id, value))
    if not diagnostics:
        store.publish(candidate)                # all-or-nothing publication
    return diagnostics
```

- 测试要点：held 时报告 = `[("J0", 9)]`；成功后 = `[("J2", 20), ("J3", 30)]`；失败时报告不变、diagnostics 恰有 J3 的 ValueError；**在 finally 里释放被阻塞的 worker**；有界等待 (bounded wait)防止测试挂死，但超时 (timeout)时长不证明顺序；**sleep 既不证明完成也不证明调度**。没执行就叫"预测"。
- K-job 审计练习的错误点：把 Q2 当成定义了完成顺序（实际是 E1）；引用不存在的 "Examples rule X1" 说超额 take 返回全部（包里没有）；把散文式调度说成"已执行证据"。真正未决问题是**超额 take（n > 长度）该拒绝还是截断 (truncate)**——只在扩展会触及时才问，否则记录并推迟。正确预测：take(4) → [K1,K2,K3,K4] → keep_ready → [K2,K4]；全成功发布 `[(K2,12),(K4,14)]`；K4 失败保留 `[(K0,5)]`。

<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="200" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">All-or-nothing publication｜全有或全无发布</text>
<defs><marker id="h" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<rect x="10" y="50" width="120" height="40" rx="6" fill="#eef4ff" stroke="#3b6fd8"/><text x="70" y="75" text-anchor="middle">worker J2 → 20</text>
<rect x="10" y="110" width="120" height="40" rx="6" fill="#eef4ff" stroke="#3b6fd8"/><text x="70" y="135" text-anchor="middle">worker J3 → 30</text>
<rect x="180" y="60" width="200" height="80" rx="8" fill="#fff4e0" stroke="#a67c00"/>
<text x="280" y="84" text-anchor="middle">Coordinator 协调者</text><text x="280" y="104" text-anchor="middle">wait → result() each</text><text x="280" y="124" text-anchor="middle">local candidate 本地候选</text>
<rect x="440" y="40" width="270" height="45" rx="8" fill="#f3f7ee" stroke="#5a8f29"/><text x="575" y="67" text-anchor="middle">all ok → publish [(J2,20),(J3,30)]</text>
<rect x="440" y="115" width="270" height="45" rx="8" fill="#fdecea" stroke="#c0392b"/><text x="575" y="142" text-anchor="middle">any error → keep [(J0,9)] + diagnostics</text>
<g stroke="#555" marker-end="url(#h)"><line x1="130" y1="70" x2="178" y2="90"/><line x1="130" y1="130" x2="178" y2="115"/><line x1="380" y1="90" x2="438" y2="65"/><line x1="380" y1="115" x2="438" y2="135"/></g>
<text x="360" y="185" text-anchor="middle">Workers never touch the report; readers see old OR new snapshot, never a mix</text>
</svg>

### 面试怎么说 / How to say it in the interview

- **Routing the docs**: "'First three' depends on input order, so I'll check Overview before Query operators; 'ready' is a missing-field question; 'complete ordered report' is in Execution. Let me read those contracts and their smallest examples first." ｜按需求路由到对应章节。
- **Asking a question that matters**: "The docs don't say what happens to the old report if one evaluation fails. Should a partial set of successful rows replace any of it? That changes whether I publish incrementally or all-or-nothing." ｜问会改变实现的问题，并说明为什么。
- **Concurrency invariant**: "The invariant is that readers see either the old complete report or the new complete one. So workers only return values; one coordinator collects every future in selected order, and publishes once — only if none raised. Note wait() returning doesn't mean success; result() is what surfaces the exception." ｜单一协调者 + 全有或全无 + wait 不抛异常。
- **Testing without sleeps**: "I'd force the schedule with events: hold J2 on a release event, let J3 finish, assert the old report is still visible, then release J2 in a finally block and assert the final order is J2, J3." ｜用事件强制调度，而不是 sleep。

---

## 10. Practice: Extend an Unfamiliar System and Learn a New Query Language｜练习：扩展陌生系统并学习新查询语言

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/practice-extend-an-unfamiliar-system-and-learn-a-new-query

### 要点 / Key ideas

- 背景：2025-12 政府 FDSE 候选人报告"拿到数据库 schema 和文档，按文档实现函数"。本练习的语言与应用是课程自创，**运行时已完整提供，不需要写解析器 (parser)或查询引擎 (query engine)**。
- **English problem statement**: "`device_queue.py` already exposes `open_history(tables)`, and the repository includes a complete tuple-query runtime `run(tables, stages)`. Add `current_open_queue(tables, unassigned_only=False)` that returns the devices whose *current* update is open — including devices missing from the registry — without changing the existing function or engine."

**文档包 / Contract packet**

| 规则 Rule | 内容 Content |
|---|---|
| D1 数据 Data | updates 每行一次设备状态更新（唯一 update_id），**有序序列**；设备当前状态 = 序列中**最后一次出现**（不是最大 ID 或时间戳 (timestamp)）。devices 每行一个注册设备（唯一 device_id）；更新可引用未注册设备；**显示名不定义身份** |
| Q1 阶段 Stages | 从左到右；`('read', table)` 必须第一；`('tail_by', key)` 每个 key 保留最后一次出现，**按获胜出现的位置排序**；`('eq', path, literal)`；`('attach', table, left_key, right_key, alias)`；`('emit', paths)` 必须最后，返回有序 tuple 列表 |
| L1 关联 Linking | attach **保留所有左行及顺序**（类似 left join）；无匹配的 alias 为 None |
| V1 值 Values | 点路径遍历嵌套 dict；路径缺失或经过 None → None；`eq` 与 None 比较时**缺失和显式 None 都保留**，没有 SQL UNKNOWN；空串 ≠ None |
| A1 应用 Application | 默认队列：当前更新为 open 的每个设备一行 `(device_id, update_id, owner_id)`，按获胜更新位置排序；含未注册设备，排除无更新的注册设备；`open_history` 行为不变（粒度是历史 open 更新，同一设备可多行） |

**Input/Output example**

```text
updates (ordered):
  U1 D1 open | U2 D2 open | U3 D1 closed | U4 D3 open
  U5 D4 open | U6 D2 open | U7 D6 open
devices:
  D1 owner O1 | D2 owner null, name Pump | D3 (no owner field), name Pump
  D5 owner O5 | D6 owner O8          (D4 is unregistered; D5 has no update)

open_history(tables)
  -> [('U1',), ('U2',), ('U4',), ('U5',), ('U6',), ('U7',)]
current_open_queue(tables)
  -> [('D3','U4',None), ('D4','U5',None), ('D2','U6',None), ('D6','U7','O8')]
current_open_queue(tables, unassigned_only=True)
  -> [('D3','U4',None), ('D4','U5',None), ('D2','U6',None)]
```

**解答 / Solution**

```python
from tuple_query import run


def open_history(tables):
    # Unchanged: grain is a historical open update.
    return run(tables, [
        ('read', 'updates'),
        ('eq', 'state', 'open'),
        ('emit', ('update_id',)),
    ])


def current_open_queue(tables, unassigned_only=False):
    stages = [
        ('read', 'updates'),
        ('tail_by', 'device_id'),      # select current state FIRST (D1)
        ('eq', 'state', 'open'),       # then filter on the current state
        ('attach', 'devices', 'device_id', 'device_id', 'device'),  # keeps unmatched rows (L1)
    ]
    if unassigned_only:
        # Absent owner, path through None, and explicit None all match (V1); '' does not.
        stages.append(('eq', 'device.owner_id', None))
    stages.append(('emit', ('device_id', 'update_id', 'device.owner_id')))
    return run(tables, stages)
```

**逐阶段走查 / Stage trace**

| 阶段 Stage | 剩余 update IDs | 说明 Why |
|---|---|---|
| read | U1..U7 | — |
| tail_by device_id | U3, U4, U5, U6, U7 | U3 取代 U1（D1），U6 取代 U2（D2）；**按获胜位置排序，不是首次出现顺序** |
| eq state open | U4, U5, U6, U7 | U3 closed 被去掉 → D1 不在队列 |
| attach devices | U4, U5, U6, U7 | D4/U5 无注册仍保留 (L1)；D3 无 owner 字段 → None (V1)；D2 显式 None；D6 → O8 |
| (flag) eq owner None | U4, U5, U6 | D6 的 O8 不符合 |

- D2 与 D3 都叫 Pump 但身份不同（device_id）。D5 无更新，read 不会引入它。
- **故意的变异 (deliberate mutation)：先过滤再选当前 (filter-before-selection)** → `eq` 先去掉 U3，D1 的获胜者变成更早的 open U1 → 输出多一行 `('D1','U1','O1')`，**错误地把当前已关闭的设备放进队列**。用固定的期望去跑它应失败——**绝不要改期望去迎合变异**。
- 其他错误：inner-join 式 attach 会丢 D4/U5（违反 L1）；首次出现排序会把 D2 排到 D3、D4 前面（违反 Q1）；SQL UNKNOWN 语义会错误丢掉合格行。
- 测试：比较**完整有序 tuple**（集合会隐藏顺序错误，计数会隐藏替换错误）；空 updates → 三个函数都返回 []；**deep-copy 前后比较**检查不改输入；空串边界：把 D6 owner 设为 '' → 默认队列含 `('D6','U7','')`，unassigned 视图仍是三行（'' 不算未分派）。
- 记录预测与执行证据分开；通过测试只证明被检查的行为，不证明所有输入。

### 面试怎么说 / How to say it in the interview

- **Choosing stage order from the contract**: "D1 says current state is the last occurrence, so I need tail_by on device_id before I filter on state. If I filtered first, U3's close would disappear and D1's earlier open U1 would win — a closed device would show up as open." ｜先选当前状态再过滤，并说出反例。
- **Missing values**: "attach preserves unmatched left rows, so unregistered D4 stays with device = None, and V1 says a path through None resolves to None — so D4's owner emits None rather than being dropped." ｜按文档处理缺失与未匹配。
- **Extension**: "For the unassigned view I append eq on device.owner_id against None after attach — it has to come after attach because it reads an attached field, and after tail_by because it's about current devices. An empty string isn't None, so I'd add a boundary test for that." ｜扩展条件放在 attach 之后，并加空串边界测试。
- **Tests**: "I'd assert complete ordered tuples, not sets or counts, plus an empty-input case and a deep-copy check that the input wasn't mutated." ｜完整有序断言 + 空输入 + 不可变检查。

---

## 11. Practice: Extending a Multithreaded System With an Unfamiliar Library｜练习：用陌生库扩展多线程系统

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/practice-extending-a-multithreaded-system-with-an-unfamiliar

### 要点 / Key ideas

- **English problem statement**: "Implement `refresh_catalog(requests, load_entry, store, pool)`. A catalog reader must keep seeing `[('legacy', 3)]` while replacement entries load concurrently; the whole new catalog appears only after every load succeeds, in request order. On failure, return ordered diagnostics and leave the old catalog unchanged."
- 这是**整快照不变量 (whole-snapshot invariant)**。库与场景是课程自创。

**契约 / Contracts**

| 编号 | 内容 Content |
|---|---|
| P1 提交与结果 | `Pool.submit(fn, arg)` 开始工作并返回 ticket；提交 ≠ 完成；完成顺序未指定。`wait_all(tickets)` 等所有 ticket 到终态 (terminal state)（含失败），**不抛 worker 异常、不取结果**。`ticket.result()` 返回值或抛异常 |
| S1 快照存储 | `CatalogStore.read()` 返回副本；`publish(entries)` 复制并**整体替换**；同一把锁 |
| A1 所有权 | worker 返回条目、不改已发布目录；一个协调者收集每个结果，按请求顺序构建私有候选，全部成功才发布；保证：同时只有一个刷新协调者、请求 ID 唯一、loader 输出有效、提交成功、失败派生自 Exception |
| A2 必需行为 | 每个请求**恰好提交一次**，**先全部提交再收集**；观察每个结果（包括早先失败之后的）；诊断 (diagnostics)按请求顺序 `(request_id, exception_type_name, message)`；成功返回 `[]`；任何失败保留旧目录；**空请求成功发布 `[]` 且不调用 loader**；重试、取消、网络、并发刷新仲裁超出范围 |

**Input/Output example**

```text
requests = ['atlas', 'beacon', 'cedar']; old catalog = [('legacy', 3)]
success: atlas->('atlas',12), beacon->('beacon',7), cedar->('cedar',9)
  while atlas is held (beacon, cedar terminal): reader sees [('legacy', 3)]
  after release: catalog = [('atlas',12), ('beacon',7), ('cedar',9)]; returns []
failure: beacon raises ValueError('unavailable')
  returns [('beacon', 'ValueError', 'unavailable')]; catalog stays [('legacy', 3)]
multiple failures: atlas RuntimeError('atlas failed'), cedar ValueError('cedar failed')
  returns [('atlas','RuntimeError','atlas failed'), ('cedar','ValueError','cedar failed')]
empty requests: returns []; catalog = []; loader never called
```

**解答 / Solution**

```python
from work_pool import wait_all


def load_preview(requests, load_entry):
    # Existing sequential helper: keep unchanged.
    return [load_entry(request_id) for request_id in requests]


def refresh_catalog(requests, load_entry, store, pool):
    # Submit ALL work before retrieving any outcome (A2).
    pending = [(request_id, pool.submit(load_entry, request_id)) for request_id in requests]
    wait_all([ticket for _, ticket in pending])   # terminal, not necessarily successful
    candidate = []
    diagnostics = []
    for request_id, ticket in pending:            # request order, not completion order
        try:
            candidate.append(ticket.result())
        except Exception as error:                # per-ticket handler: keep observing the rest
            diagnostics.append((request_id, type(error).__name__, str(error)))
    if not diagnostics:
        store.publish(candidate)                  # single whole-snapshot publication
    return diagnostics
```

- **诱人的错误实现**：worker 直接 append 到已发布目录 → atlas 被阻塞时读者看到 `[('beacon',7),('cedar',9)]`；给每次 append 加锁只防止同时修改，仍暴露不完整目录且顺序依赖调度。
- **另一个错误**：在 beacon 的异常处理中直接 return → 旧目录保留（可见性对），但 **cedar 的结果没被观察**，违反 A2——retrieval log 会抓住。**可见性正确 ≠ 扩展完整**。
- 测试 harness：≥3 个 worker 线程 + 单独协调者线程（防止 atlas 饿死 (starving)其他加载）；atlas 阻塞在 event 上，beacon、cedar 真正到达终态（完成信号挂在 future 回调上，而不是 worker 返回前手动 set）；检查 atlas 与协调者都未完成、读者仍见旧快照；**cleanup 里释放 atlas**；之后检查发布/保留、诊断、每个结果被观察（submit 全在 result 之前，各恰好一次）。
- 需要补的测试：多重失败（完整有序诊断、旧目录保留、三个结果都取回、只提交一次）；空请求（`[]`、发布空目录、0 次 loader 调用、0 个 ticket）；快照复制隔离（改 read() 返回的列表 / 发布后改输入列表都不影响存储）；顺序回归 (regression)（load_preview 保持请求顺序）。
- **预测与执行是不同证据**；通过这些检查只证明指定行为，不证明所有并发调度下都正确。

### 面试怎么说 / How to say it in the interview

- **Explaining the design**: "Workers only return entries; they never touch the store. The coordinator submits everything first, waits for all tickets to be terminal, then calls result() on each one in request order with its own try/except, so one failure doesn't stop me from observing the rest. I publish once, only if diagnostics is empty." ｜worker 不碰存储，协调者逐个取结果，全成功才发布一次。
- **Why per-append locking isn't enough**: "Locking each append prevents a torn list, but readers can still see two of three entries, in scheduler order. The invariant is about the whole snapshot, so the lock boundary has to be the publish of the complete list." ｜锁的边界要覆盖整个不变量。
- **Edge cases I'd call out**: "Empty requests should publish an empty catalog without calling the loader, and on multiple failures I return diagnostics for each in request order, with the exception type name and message." ｜主动说出空输入与多重失败的行为。

---

## 12. A Systematic Debugging Method for Unfamiliar Code｜陌生代码的系统化调试方法

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/a-systematic-debugging-method-for-unfamiliar-code

### 要点 / Key ideas

- 重构/调试轮 (re-engineering round) 的核心技能。Palantir 把"在现有系统、代码库、基础设施中工作"列为工程能力，公开指南强调调试、修改、扩展现有代码；第三方建议：追踪陌生代码、找到缺陷、**先解释修复再改**。
- 现象：同一进程里先渲染英文问候后，法文问候返回英文。**可见错误是字符串，原因是跨调用共享的状态**。

**六步方法 / Six-step method**

| 步骤 Step | 做什么 What |
|---|---|
| 1. 确立契约 Establish contract | locale 每次调用都选模板，名字之后再替换；早先调用不能改变语言选择 |
| 2. 复现 Reproduce | 记录输入、相关初始状态、执行序列、期望与实际；**在报告的序列内保留状态，在独立场景之间重置** |
| 3. 读调用路径 Follow call path | 从失败断言 → `render` → `load_template`；3 分钟定位时间盒 (orientation timebox)，结束时总结路径与剩余不确定性 |
| 4. 找最早分歧点 Earliest divergence | 逐步追踪预测值，找到**最早违反契约的地方**——可见错误的位置不一定是错误值产生的位置 |
| 5. 可证伪假设 Falsifiable hypothesis | 命名机制 + 预测一个可能反驳它的观测；用对照场景在改代码前检验 |
| 6. 最小根因修复 + 回归测试 Minimal root-cause repair + regression tests | 在因果缺陷处恢复契约，保留无关行为；加测试证明修了什么 |

**Buggy code**

```python
# template_catalog.py
TEMPLATES = {
    ('welcome', 'en'): 'Hello, {name}!',
    ('welcome', 'fr'): 'Bonjour, {name}!',
}


def load_template(template_id, locale, cache):
    key = template_id                  # BUG: cache identity ignores locale
    if key not in cache:
        cache[key] = TEMPLATES[(template_id, locale)]
    return cache[key]


# greeting_service.py
from template_catalog import load_template


def render(template_id, locale, name, cache):
    template = load_template(template_id, locale, cache)
    return template.format(name=name)
```

```text
Input:  cache = {}
        render('welcome', 'en', 'Ari', cache)  -> 'Hello, Ari!'      (expected 'Hello, Ari!')
        render('welcome', 'fr', 'Bo',  cache)  -> 'Hello, Bo!'       (expected 'Bonjour, Bo!')
```

- **复现陷阱**：只跑法文 `render('welcome','fr','Bo',{})` 会通过——测试的是不同历史，**不能反驳报告**；给每次调用单独的空 dict 也改变了复现。正确：从 `cache = {}` 开始，两次调用共享同一 dict。
- 追踪：英文查找 key 'welcome' miss → 存英文模板；法文查找 key 'welcome' **hit** → 法文条目从未被读取 → 格式化器**正确地**把 Bo 替换进英文模板。最早分歧 = **缓存 (cache)把两个 locale 的模板当成同一身份**。
- 错误修复：在 render 里对法文把 'Hello' 替换成 'Bonjour' → 掩盖输出但身份冲突仍在。
- 假设："The loader caches by template_id alone, so the first locale loaded supplies later calls for that template ID." 改代码前的对照预测：
  - 新鲜缓存只跑法文 → `'Bonjour, Bo!'`
  - 反向预热（同一缓存先法文 Bo 后英文 Ari）→ `'Bonjour, Bo!'`、**`'Bonjour, Ari!'`**
  - 若结果相反则机制不成立。只打印"loader 被调用了"无法区分缓存身份与格式化。

**The fix**

```python
def load_template(template_id, locale, cache):
    key = (template_id, locale)        # FIX: composite identity includes locale
    if key not in cache:
        cache[key] = TEMPLATES[(template_id, locale)]
    return cache[key]
```

- 成员检查、插入、返回都用 key → 一处修改全局一致。修复后缓存含 `('welcome','en')` 与 `('welcome','fr')` 两项。**名字不属于 key**（缓存的是未格式化模板）；禁用缓存是丢弃设计；硬编码法文绕过身份规则。**最小 (minimal) 指修复范围，不是字符数**。

```python
import unittest
from greeting_service import render


class GreetingTests(unittest.TestCase):
    def test_english_then_french(self):          # original reproduction, unchanged
        cache = {}
        self.assertEqual(render('welcome', 'en', 'Ari', cache), 'Hello, Ari!')
        self.assertEqual(render('welcome', 'fr', 'Bo', cache), 'Bonjour, Bo!')

    def test_fresh_french(self):
        self.assertEqual(render('welcome', 'fr', 'Bo', {}), 'Bonjour, Bo!')

    def test_french_then_english(self):          # reversed warm-up regression
        cache = {}
        self.assertEqual(render('welcome', 'fr', 'Bo', cache), 'Bonjour, Bo!')
        self.assertEqual(render('welcome', 'en', 'Ari', cache), 'Hello, Ari!')

    def test_same_locale_different_names(self):  # name substituted per call
        cache = {}
        self.assertEqual(render('welcome', 'en', 'Ari', cache), 'Hello, Ari!')
        self.assertEqual(render('welcome', 'en', 'Bo', cache), 'Hello, Bo!')
```

- 证据分三类：**预测结果、已执行检查（命令 + 实际结果）、未执行检查**。通过只支持被测序列，不证明所有 locale 或缓存行为。
- 练习（收据 receipt）：同一缺陷，"法文 Noor 后英文 Lee 返回两次法文"——同法修复。

<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="200" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Debugging loop｜调试循环</text>
<defs><marker id="i" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<g fill="#eef4ff" stroke="#3b6fd8">
<rect x="10" y="50" width="105" height="60" rx="8"/><rect x="128" y="50" width="105" height="60" rx="8"/><rect x="246" y="50" width="105" height="60" rx="8"/><rect x="364" y="50" width="105" height="60" rx="8"/><rect x="482" y="50" width="105" height="60" rx="8"/><rect x="600" y="50" width="110" height="60" rx="8"/>
</g>
<g text-anchor="middle">
<text x="62" y="75">Contract</text><text x="62" y="93">确立契约</text>
<text x="180" y="75">Reproduce</text><text x="180" y="93">保留共享状态</text>
<text x="298" y="75">Call path</text><text x="298" y="93">读调用路径</text>
<text x="416" y="75">Earliest diverge</text><text x="416" y="93">最早分歧点</text>
<text x="534" y="75">Hypothesis</text><text x="534" y="93">可证伪预测</text>
<text x="655" y="75">Fix + tests</text><text x="655" y="93">根因修复+回归</text>
</g>
<g stroke="#555" marker-end="url(#i)"><line x1="115" y1="80" x2="126" y2="80"/><line x1="233" y1="80" x2="244" y2="80"/><line x1="351" y1="80" x2="362" y2="80"/><line x1="469" y1="80" x2="480" y2="80"/><line x1="587" y1="80" x2="598" y2="80"/></g>
<path d="M534,110 C534,160 298,160 298,112" fill="none" stroke="#c0392b" stroke-dasharray="4,3" marker-end="url(#i)"/>
<text x="416" y="168" text-anchor="middle" fill="#c0392b">prediction fails → revisit 预测失败则回到路径</text>
</svg>

### 面试怎么说 / How to say it in the interview

- **Reproduce faithfully**: "The bug only shows after an English render, so I'll keep one shared cache across both calls, starting empty. Running French alone would pass, but that's a different history — it doesn't refute the report." ｜复现时保留触发 bug 的共享状态。
- **Locate the earliest divergence**: "The formatter is actually fine — it correctly puts Bo into the template it was given. The earliest wrong value is the cache hit: the key is just template_id, so French gets the English entry." ｜区分错误出现的位置与产生的位置。
- **Falsifiable hypothesis**: "If the first locale loaded wins, then a fresh French call should work, and French-then-English should give 'Bonjour, Ari!'. If I see the opposite, my theory is wrong." ｜先给可证伪预测再改代码。
- **Minimal fix**: "I'll change the key to (template_id, locale). Every cache operation already uses key, so that one line fixes it consistently. I won't patch the output in render, and the name doesn't belong in the key because we cache the unformatted template." ｜根因修复，不掩盖输出。

---

## 13. Red Herrings and Verifying Your Fix｜识别误导线索并验证修复

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/red-herrings-and-verifying-your-fix

### 要点 / Key ideas

- **误导线索 (red herring)**：分散注意力的可疑细节。注释、低效、无关 helper **只有当其行为参与了违反契约的序列时**才是因果证据。
- **有依据的修复 (justified repair)**：改变已证明的失败机制，同时保留独立推导的期望。**把期望改成迎合错误输出会使检查失效**。

**Buggy code（tally）**

```python
def tally(categories):
    # Categories arrive alphabetically.      <- stale comment: red herring (never executes)
    counts = {}
    for category in sorted(set(categories)):  # BUG: set() discards multiplicity
        counts[category] = counts.get(category, 0) + 1
    return counts
```

```text
Contract: each occurrence adds exactly 1 to its category; returns dict; input unchanged.
Input:  ['red', 'blue', 'red']
Actual: {'blue': 1, 'red': 1}
Expected: {'red': 2, 'blue': 1}
```

**观察分类 / Classifying observations**

| 观察 Observation | 因果意义 Causal significance |
|---|---|
| 给 ['red','blue'] 加第二个 red，`set(categories)` 不变 | **多重性 (multiplicity)丢失的直接证据** |
| `sorted` 改变 blue/red 处理顺序 | 在此契约下无害的排序 |
| 过时注释说按字母顺序到达 | 不执行的干扰 |
| 累加器对每个收到的值加一 | 下游行为正确（只是输入可迭代对象有缺陷） |

- **对照对比 (controlled contrast)**：['red','blue'] 与 ['red','blue','red'] 期望不同，但变成相同的 set 和排序序列 → 预测相同输出 → 定位到累加之前的丢失。去掉排序仍然每个类别只喂一次；改注释喂的值完全相同。

**The fix（保留排序以隔离因果变化）**

```python
def tally(categories):
    # Categories arrive alphabetically.
    counts = {}
    for category in sorted(categories):        # FIX: keep every occurrence
        counts[category] = counts.get(category, 0) + 1
    return counts
```

- 修复序列 ['blue','red','red'] → {'blue':1} → {'blue':1,'red':1} → {'blue':1,'red':2}。保留排序只是隔离"保留信息"这个变化，**不代表认可其开销**：排序 O(n log n)，直接迭代期望 O(n)。去掉排序、修注释作为**单独验证的清理 (cleanup)**。

**区分性检查 / Discriminating checks**（拒绝"强制 red=2"之类的 workaround）

```python
import unittest
from tally_verification import tally


class TallyTests(unittest.TestCase):
    def test_contract_cases(self):
        cases = [
            (['red', 'blue', 'red'], {'red': 2, 'blue': 1}),   # original reproduction
            ([], {}),                                          # rejects unconditional inserts
            (['blue'], {'blue': 1}),                           # singleton
            (['red', 'red', 'red'], {'red': 3}),               # rejects distinct-only / fixed 2
            (['blue', 'red', 'blue', 'green', 'red', 'blue'],
             {'blue': 3, 'red': 2, 'green': 1}),               # unequal counts
        ]
        for categories, expected in cases:
            with self.subTest(categories=categories):
                before = categories.copy()
                actual = tally(categories)
                self.assertIsInstance(actual, dict)
                self.assertEqual(actual, expected)                    # exact allocation
                self.assertEqual(sum(actual.values()), len(before))   # conservation invariant
                self.assertEqual(categories, before)                  # rejects in-place sort
```

- **总数不变量 (total invariant)** `sum(counts.values()) == len(input)`：对原输入 {'red': 3} 满足总数却丢了 blue → **精确映射检查分配，总数检查守恒，二者互补**。
- 审计的错误说法：①"强制 red 为 2 后原例通过，所以修好了"；②"输出 {'red':3} 总数为 3，应更新原期望"；③"测试矩阵有'输出匹配例外'允许用候选输出替换期望"（编造）。

**图可达性验证 / Graph reachability**

- 契约：结果含起点和所有可达顶点**各恰好一次**，排除不可达顶点，**有环有限图 (finite cyclic graph)上终止**；顺序不指定；邻接表 (adjacency list)不变。

```python
def reachable(adjacency, start):
    stack = [start]
    seen = set()
    output = []
    while stack:
        vertex = stack.pop()
        if vertex in seen:             # expansion control: expand each vertex once
            continue
        seen.add(vertex)
        output.append(vertex)
        stack.extend(adjacency[vertex])
    return output
```

- 菱形图 (diamond graph) A:[B,C], B:[D], C:[D], D:[] → 成员 {A,B,C,D}，长度 4。只检查 `set(result)` 会隐藏重复输出如 ['A','B','D','C','D'] → **同时要求成员与唯一性 (uniqueness) `len(result) == len(set(result))`**。
- 环 A:[B], B:[A] 和自环 (self-loop) A:[A]：没有扩展控制会无限 A,B,A,B…；**对最终列表去重 (deduplication)救不了——遍历根本到不了 return**。参考实现每个顶点只在首次 pop 时扩展 → 有限图有限次 push → 终止。入队时标记 (mark on enqueue) 也是一致可行的策略。
- 练习夹具 (fixtures)：tally ['oak','pine','oak','oak','pine'] → {'oak':3,'pine':2}；空 → {}；['pine'] → {'pine':1}。图 S:[T,U], T:[V], U:[V], V:[S], X:[]：从 S → 成员 {S,T,U,V}，长度 4，不含 X；从 X → 恰好 ['X']；深拷贝比较嵌套邻接不变。
- 可辩护的报告：保留原复现不变；把因果修改与清理分开；每个附加检查对应一个合理缺陷；**列出被测用例而不是宣称"全面回归安全"**。

### 面试怎么说 / How to say it in the interview

- **Dismissing a red herring with evidence**: "The comment is stale, but it doesn't execute, and removing the sort would still feed each category once. The contrast that matters is that ['red','blue'] and ['red','blue','red'] collapse to the same set — that's where the second red is lost." ｜用对照证据排除误导线索。
- **Keeping the fix minimal**: "I'll change only sorted(set(categories)) to sorted(categories) to prove the cause, then remove the sort and fix the comment as a separate cleanup, because the sort is O(n log n) for no reason." ｜先最小因果修复，再单独清理。
- **Tests that reject workarounds**: "A hard-coded red=2 would pass the original case, so I add ['red','red','red'] expecting 3, an empty list, and a mixed case — plus a conservation check that the counts sum to the input length and that the input isn't mutated." ｜加能拒绝投机修复的区分性测试。
- **Graph verification**: "Membership alone hides duplicates, so I assert both the set and that the length equals the set size. And dedup at the end can't fix a cycle — the seen check has to control expansion, or we never return." ｜成员 + 唯一性；去重不能替代扩展控制。

---

## 14. Practice: Fixing a Tally Bug and a Graph Traversal Bug｜练习：修复计数 bug 与图遍历 bug

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/practice-fixing-a-tally-bug-and-a-graph-traversal-bug

### 要点 / Key ideas

- 交付：两个有限的实现补丁（无关清理分开）、保留两个报告夹具 (fixtures) + 独立推导的邻近用例的测试、一份调查报告（每个模块：复现、聚焦追踪、改前假设 + 可能反驳的预测、因果修改、验证证据）。
- 课程建议 35 分钟预算：5 分钟契约与复现，15 分钟调查与修改，10 分钟回归检查，5 分钟报告。

### Bug 1: Tally loses repeated occurrences｜计数丢失重复项

- **English problem statement**: "`tally_categories(categories)` must count every input occurrence, return the exact category-to-count dict, and leave the input unchanged. The reported input `['amber', 'teal', 'amber', 'amber', 'teal']` should give `{'amber': 3, 'teal': 2}`."

```python
# category_tally.py (buggy)
def tally_categories(categories):
    # Categories arrive alphabetically.
    counts = {}
    for category in sorted(categories):
        counts[category] = 0          # BUG: resets the accumulator on every occurrence
        counts[category] += 1
    return counts
```

```text
Input:    ['amber', 'teal', 'amber', 'amber', 'teal']
Actual:   {'amber': 1, 'teal': 1}
Expected: {'amber': 3, 'teal': 2}
```

- 追踪：排序后 ['amber','amber','amber','teal','teal']；第一个 amber 置 0 加到 1；第二个 amber **把已有计数重置为 0** 再加 1；第三个同样 → amber=1，teal=1。
- 区分性预测：单个类别 → 正确 1；三个相同 → 仍为 1 → 支持"重置"假设：**初始化应每个不同类别一次，而不是每次出现一次**。

```python
# category_tally.py (fixed)
def tally_categories(categories):
    # Categories arrive alphabetically.
    counts = {}
    for category in sorted(categories):
        if category not in counts:    # FIX: initialize once per distinct category
            counts[category] = 0
        counts[category] += 1
    return counts
```

- 验证期间保留排序与过时注释（隔离因果修改）。硬编码报告的计数会在 4 个 amber 与 violet 夹具上失败。
- 测试：混合夹具 + `[]` + `['teal']` + 4 个 amber + `['violet','teal','violet']`；断言 dict 类型、精确映射、总数守恒、输入不变（`finally` 中检查）。

### Bug 2: Dependency order emits jobs too early｜依赖排序过早输出任务

- **English problem statement**: "`execution_order(vertices, edges)` returns an order where, for every edge `(prerequisite, dependent)`, the prerequisite comes first; every vertex (including isolated ones) appears exactly once; a directed cycle raises `ValueError('dependency cycle')`; inputs are not mutated."

```python
# dependency_execution.py (buggy)
from collections import deque


def execution_order(vertices, edges):
    adjacency = {vertex: [] for vertex in vertices}
    indegree = {vertex: 0 for vertex in vertices}
    for prerequisite, dependent in edges:
        adjacency[prerequisite].append(dependent)
        indegree[dependent] += 1

    frontier = deque(vertex for vertex in vertices if indegree[vertex] == 0)
    queued = set(frontier)
    output = []
    while frontier:
        vertex = frontier.popleft()
        output.append(vertex)
        for dependent in adjacency[vertex]:
            indegree[dependent] -= 1
            if dependent not in queued:      # BUG: confuses "discovered" with "ready"
                frontier.append(dependent)
                queued.add(dependent)

    if len(output) != len(vertices):
        raise ValueError('dependency cycle')
    return output
```

```text
Input:    vertices = ['A', 'B', 'C', 'D'], edges = [('A','D'), ('B','C'), ('C','D')]
Actual:   ['A', 'B', 'D', 'C']      # membership and uniqueness pass, C -> D violated
Expected: any order with A before D, B before C, C before D, e.g. ['A', 'B', 'C', 'D']
```

- 追踪：初始 frontier [A,B]，indegree A:0, B:0, C:1, D:2。pop A → D 减到 1，因未入队就入队 → [B,D]；pop B → C 减到 0 入队 → [D,C]；pop D（**D 还有一个未满足前置**）、pop C → D 减到 0 但已输出。
- **全部 4 个顶点都在、各一次，顺序仍然错**——只检查成员与唯一性会漏掉。

```python
            if indegree[dependent] == 0:     # FIX: enqueue only when every prerequisite is done
                frontier.append(dependent)
                queued.add(dependent)        # now redundant; remove later as separate cleanup
```

- 修复后：pop A → frontier [B]（D 还差一个）；pop B → [C]；pop C → 释放 D → `['A','B','C','D']`。每个顶点只在 indegree 归零时入队一次 → 有限图终止；**有向环 (directed cycle)使顶点无法输出 → 原有长度检查才有效**。
- 诱人补丁：对返回列表排序——恰好适配报告夹具，但链 `['Z','A'], [('Z','A')]` 失败（字母序把依赖方放前面）；去重 (deduplication)不能建立前置顺序。
- **根喂环 (root-fed cycle)** A→B→C→B：原实现输出 A、发现并输出 B、再 C → 返回全部三个（尽管 C→B），长度检查通过！修复后只输出 A，B 仍有一个入边，C 被阻塞 → 长度检查抛 `ValueError('dependency cycle')`。
- 测试：报告图、空图、单个孤立点、菱形、含孤立点的不连通图 (disconnected graph)、逆字母链（无环：检查全部顶点各一次 + 每条边 `position[u] < position[v]`，**接受任何合法拓扑序 (topological order)**）；自环、两节点环、根喂环（要求 ValueError 且消息匹配，**即使抛异常也用深拷贝比较输入**）。

<svg viewBox="0 0 720 210" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="210" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Discovery vs readiness (Kahn's algorithm)｜发现 ≠ 就绪</text>
<defs><marker id="j" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<g fill="#eef4ff" stroke="#3b6fd8"><circle cx="60" cy="70" r="20"/><circle cx="60" cy="150" r="20"/><circle cx="170" cy="150" r="20"/><circle cx="280" cy="110" r="20"/></g>
<g text-anchor="middle"><text x="60" y="75">A</text><text x="60" y="155">B</text><text x="170" y="155">C</text><text x="280" y="115">D</text></g>
<g stroke="#555" marker-end="url(#j)"><line x1="80" y1="75" x2="260" y2="105"/><line x1="80" y1="150" x2="148" y2="150"/><line x1="190" y1="145" x2="260" y2="118"/></g>
<rect x="330" y="45" width="380" height="60" rx="8" fill="#fdecea" stroke="#c0392b"/>
<text x="520" y="68" text-anchor="middle">Buggy: enqueue when first discovered</text><text x="520" y="90" text-anchor="middle">A, B, D, C — D runs before C 依赖未满足</text>
<rect x="330" y="125" width="380" height="60" rx="8" fill="#f3f7ee" stroke="#5a8f29"/>
<text x="520" y="148" text-anchor="middle">Fixed: enqueue when indegree == 0</text><text x="520" y="170" text-anchor="middle">A, B, C, D — cycles leave vertices unemitted → raise</text>
</svg>

### 面试怎么说 / How to say it in the interview

- **Tally**: "Single categories count correctly but three ambers still give one, so the accumulator is being reset per occurrence — initialization has to happen once per distinct category. I'll guard the assignment with 'if category not in counts' and leave the sort and comment alone until the fix is verified." ｜用单个 vs 三个相同的对照定位重置。
- **Dependency order**: "Every vertex appears exactly once, but C→D is violated. The enqueue condition checks whether D was discovered, not whether it's ready. In Kahn's algorithm a vertex is ready only when its remaining indegree hits zero — and that change also makes the final length check catch cycles like A→B→C→B." ｜发现 ≠ 就绪；修复后长度检查才能抓环。
- **Tests**: "For acyclic graphs I don't assert one specific order — I check every vertex once and that each edge's prerequisite comes first. For cycles I expect ValueError and still check the inputs weren't mutated." ｜接受任意合法拓扑序，环要抛错。

---

## 15. Practice: Debugging a Several-Hundred-Line Codebase｜练习：调试数百行的代码库

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/practice-debugging-a-several-hundred-line-codebase

### 要点 / Key ideas

- 第三方备考资料描述过"追踪和调试较大的陌生代码文件"；不保证格式、代码长度或评分。
- **English problem statement**: "The event report for start H overcounts inspections and repairs. The app spans ~300–340 meaningful lines across five modules with one integrated defect. Derive the expected report independently, reproduce the public failure, and follow only the call path that can explain the difference."

```text
adjacency:            events:
  H: [J, K]             H: [inspection]
  J: [L]                J: [repair, repair]
  K: [L]                K: [inspection]
  L: [H]                L: [repair, inspection]
  Z: []                 Z: [repair]

build_event_report('H', adjacency, events)
Expected: reachable_sites = {H, J, K, L} (each once), category_counts = {'inspection': 3, 'repair': 3}
Actual:   reachable_sites = [H, J, K, L, L, H],       category_counts = {'inspection': 5, 'repair': 4}
```

- 契约：结果含起点与所有可达顶点**各一次**，排除不可达，**有限有环图 (finite cyclic graph)终止**，深度保留两个输入；顺序不指定。**相同记录是独立出现**：J 的两个 repair 都要算。
- 40 分钟预算：5 分钟推导期望与复现；15 分钟聚焦调查 + 可证伪假设；5 分钟有限因果修复；10 分钟对保存的补丁跑回归；5 分钟证据报告——**保留最后 15 分钟做检查与报告**。
- 模块：`event_report.py`（公开组装）、`site_routes.py`（可达性）、`event_counts.py`（收集、选择、计数）、`event_display.py`（展示）、`event_inputs.py`（校验与夹具）。

**聚焦路径 / Focused call path（不读全部文件）**

`build_event_report` → `reachable_sites`（site_routes）→ `collect_events` / `count_categories`（event_counts）→ `structured_report`（event_display）。过滤 helper 与可选渲染可以等（默认路径不调用）。直接检查计数器 `['repair','repair']` → `{'repair': 2}` 正确 → 若上游给了太多出现，正确计数也会产生错误报告。

**Buggy code**

```python
# site_routes.py (buggy excerpt)
from collections import deque


def reachable_sites(start, adjacency):
    queue = deque([start])
    seen = set()
    output = []
    while queue:
        site = queue.popleft()
        output.append(site)            # BUG: emitted BEFORE the seen check
        if site in seen:
            continue
        seen.add(site)
        queue.extend(adjacency[site])  # only first visits expand neighbors
    return output
```

- 追踪（发射 (emit)与扩展 (expand)分开看）：pop H 发射+扩展 [J,K] → pop J 发射+扩展 [K,L] → pop K 发射+扩展 [L,L] → pop L 发射+扩展 [L,H] → **pop 第二个 L 先发射再跳过** → **pop H 先发射再跳过**。返回 H,J,K,L,L,H：集合 4 个正确，6 个条目违反唯一性 (uniqueness)。
- 多出的 L 贡献 1 repair + 1 inspection，多出的 H 贡献 1 inspection → 预测 {'inspection': 5, 'repair': 4}，共 9 个而不是 6 个——**每个多余事件都能解释**。
- **终止 (termination)不能证明遍历正确**：扩展控制让遍历结束了，但发射仍重复。可达顶点的重复处理是错误；正确处理的顶点上的重复事件是合法的。
- 区分性预测：无环菱形在同一缺陷下也会重复共享后代；简单链不会重复 → 区分"重复入队 (duplicate enqueue)"与"只怪环"的解释。

**The fix（移动一条语句）**

```python
        site = queue.popleft()
        if site in seen:               # skip already-processed sites first
            continue
        seen.add(site)                 # mark the first visit
        output.append(site)            # FIX: emit only first visits
        queue.extend(adjacency[site])
```

- 保持 FIFO 调度、计数、排序、格式化不变；过时注释不执行，排序展示不会制造额外出现。
- 较弱的补丁：①把每个站点的事件列表变成 set → 抹掉 J 的一个合法 repair；②只在格式化时去重 → `reachable_sites` 仍违反唯一性契约，直接遍历测试会暴露。

**回归测试 / Regression suite**（同时测直接遍历 API 与公开报告 API，每次调用前后深拷贝快照）

| 夹具 Fixture | 期望成员 Expected sites | 期望计数 Expected counts | 总数 |
|---|---|---|---|
| 事故 H | {H,J,K,L} | inspection 3, repair 3 | 6 |
| 无环菱形 A:[B,C],B:[D],C:[D] | {A,B,C,D} | inspection 3, repair 3 | 6 |
| 链 A→B→C | {A,B,C} | inspection 2, repair 2 | 4 |
| 自环 A:[A] | {A} | repair 2 | 2 |
| 两点环 A↔B | {A,B} | inspection 1, repair 2 | 3 |
| 孤立 Z | {Z} | repair 1 | 1 |
| 空事件 | {A,B,C,D} | {} | 0 |
| 单点重复 A:[repair×3] | {A} | repair 3 | 3 |
| 计数器直测 ['repair','repair'] | — | repair 2 | 2 |

- 每个夹具检查：成员、长度、唯一性、排除不可达、精确计数、**独立总数**、**出现守恒 (occurrence conservation)（用指定的可达集合与调用前事件，不用可能有缺陷的返回站点）**、深度输入保留。
- 调查笔记四类证据：独立推导的期望、预测追踪、执行的命令与实际结果、未执行检查（含执行限制）。最终声明列出检查过的夹具，支持有界的结论，而不是"全面回归安全"。

### 面试怎么说 / How to say it in the interview

- **Scoping the read**: "I won't read all five modules. The incident uses the default report path, so I'll follow build_event_report into reachable_sites, then collection and counting. First I'll check the counter directly — two repairs give two, so the counter is fine and the extra occurrences must come from upstream." ｜只读能解释差异的路径，先排除下游。
- **Accounting for the excess**: "The traversal returns H, J, K, L, L, H — the set is right but L and H are duplicated, because output.append runs before the seen check. The extra L adds one repair and one inspection, the extra H adds one inspection, which explains exactly 5 and 4." ｜用多余元素精确解释多出的计数。
- **Rejecting workarounds**: "Turning each site's events into a set would drop J's legitimate second repair, and deduping only in the formatter leaves reachable_sites violating its own contract. The real fix is moving the append below the seen guard." ｜拒绝掩盖症状的补丁。
- **Time management**: "I'm budgeting the last fifteen minutes for running the regression suite and writing up what I actually executed versus what I only predicted." ｜留时间验证与报告。

---

## 16. The Coding Round With End-User Framing｜带终端用户视角的编码轮

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/the-coding-round-with-end-user-framing

### 要点 / Key ideas

- 场景：工具台操作员 (tool-desk operator) 收到借电钻请求，需要搜索目录、找到可用工具、把 ID 传给**单独的**借出操作。"让工具搜索好用"留下关键问题：哪些词匹配、哪些记录合格、什么排前面、非法请求怎么办。
- 依据：美国政府 FDSE 职位描述看重"理解技术决策对用户的影响、强编码、与用户迭代"（职位证据，非评分表）；第三方指南：编码轮先澄清不明确的题目，解决核心挑战，并从对整个系统和用户的影响解释实现选择。
- 用户视角约束接口、算法与失败行为：**身份 (identity)** —— 稳定 ID 区分同名工具；**可用性 (availability)** —— 不推荐不可用工具；**只读范围 (read-only scope)** —— 搜索不预留、也不保证借出时仍可用。模糊建议、缓存、自动借出都超出约定。

**函数契约 / Function contract：`search_tools(tools, query, limit=5)`**

| 方面 Aspect | 规则 Rule |
|---|---|
| 目录 Catalog | ≤2,000 条可信记录；唯一非空 tool_id、非空 name/category、非负整数 available_units；schema 校验是前置条件 (precondition) |
| 查询 Query | 至少一个非空白字符；按空白切分，每个 token `casefold()` |
| 匹配 Matching | **每个 token** 都是 casefold 后 name **或** category 的子串（不同 token 可匹配不同字段）；只有 available_units > 0 合格 |
| 排序 Ordering | 对**所有**合格匹配按 `(name.casefold(), tool_id)` 排序，**再**取 limit |
| 输出 Output | 新字典列表，恰好含 tool_id、name、available_units；保留目录顺序与内容 |
| 失败 Failures | 非字符串 query 或非整数 limit（含 bool）→ TypeError；空白 query 或非正 limit → ValueError；**空目录也先校验参数**；合法但无匹配 → `[]` |

- 测验：`search_tools([], ' ')` → ValueError；`search_tools([], 'lathe')` → `[]`；`search_tools([], 'drill', True)` → TypeError。**先校验才能区分"没有匹配"与"请修正请求"**。

**Input/Output example**

```text
Catalog (input order):
  T4 Drill Press     | Workshop Tools | 1
  T3 Cordless Drill  | Power Tools    | 0
  T6 Cordless Drill  | Power Tools    | 1
  T2 Drill Bit Set   | Power Tools    | 3
  T5 Safety Goggles  | Safety         | 4
  T1 Cordless Drill  | Power Tools    | 2

search_tools(catalog, ' DRILL tools ', 3) ->
  [{"tool_id": "T1", "name": "Cordless Drill", "available_units": 2},
   {"tool_id": "T6", "name": "Cordless Drill", "available_units": 1},
   {"tool_id": "T2", "name": "Drill Bit Set", "available_units": 3}]
search_tools(catalog, 'drill workshop') -> [T4 only]
search_tools(catalog, 'lathe')          -> []
search_tools(catalog, '   ')            -> ValueError
```

**Solution**

```python
def search_tools(tools, query, limit=5):
    # Validate arguments before touching the catalog (even if it is empty).
    if not isinstance(query, str):
        raise TypeError("query must be a string")
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer, not bool")
    tokens = query.casefold().split()
    if not tokens:
        raise ValueError("query must contain a non-whitespace character")
    if limit <= 0:
        raise ValueError("limit must be positive")

    matches = []
    for tool in tools:
        if tool["available_units"] <= 0:
            continue
        name = tool["name"].casefold()
        category = tool["category"].casefold()
        if all(token in name or token in category for token in tokens):
            matches.append(tool)

    # Sort ALL matches first, then limit; tool_id breaks name ties.
    matches.sort(key=lambda tool: (tool["name"].casefold(), tool["tool_id"]))
    return [
        {
            "tool_id": tool["tool_id"],
            "name": tool["name"],
            "available_units": tool["available_units"],
        }
        for tool in matches[:limit]
    ]
```

- 追踪：tokens = drill, tools；T3 不可用，T5 不匹配 → 保留 T4, T6, T2, T1 → 全局排序 T1, T6, T2, T4 → 取 3。
- **诱人捷径：先取前三个合格记录再排序** → T4, T6, T2 → 排序 T6, T2, T4，**错误地漏掉 T1**——数据源行顺序改变了操作员看到的子集。修复：先全部排序再切片；不要为了能提前停止而改排序规则。
- 复杂度 (complexity)：n 记录、t token、L 最大字段长、m 匹配数。匹配保守上界 O(n·L·Σtoken_len)；排序 O(m log m)；辅助空间 (auxiliary space) O(m)。2,000 条内存目录 → 选**可读的全扫描 + 排序基线**。复杂度推理不等于实测响应时间。更大目录/请求率才考虑索引 (index)或有界 top-k；缓存 (caching)会引入新鲜度 (freshness)问题（陈旧可用性误导操作员）。
- 测试：精确投影 (exact projection)（只查数量会接受错误子集）；大小写与空白归一化 (normalization)；跨字段 token；排除不可用；同名按 ID 排序；合法无匹配；空目录；**空目录上的非法参数**；**反转输入顺序结果相同**（直接检查行顺序不影响子集）；嵌套 metadata 不泄露、返回字典是新对象、修改结果不影响源（`tearDown` 中深拷贝比较）。
- 练习：S8 Socket Set(0)、S4 Torque Wrench(2)、S2 Socket Wrench(1)、S1 Socket Wrench(3)、S9 Workbench(1)；`' WRENCH hand '` limit 2 → S1, S2；limit 3 → S1, S2, S4（可用数 3, 1, 2）。

### 面试怎么说 / How to say it in the interview

- **Framing around the user**: "The operator's next step is checkout, so each result needs a stable tool_id — two tools can share a name — and I'll only return tools with units available. Search stays read-only; it doesn't reserve anything." ｜从用户下一步推出接口：ID、可用性、只读。
- **Clarifying questions**: "Should every word match, or any word? Can 'drill' match the name and 'tools' match the category? How should ties be ordered? And for a blank query, do you want an error or an empty list?" ｜问匹配、跨字段、排序、非法输入。
- **Avoiding the early-limit bug**: "I'll collect all matches, sort them globally, and only then slice. If I stopped after the first three matches, the answer would depend on catalog order — T1 sits last in the input and would be lost." ｜先排序后切片。
- **Complexity and baseline**: "For 2,000 in-memory records a full scan plus sort is plenty — O(n times string work) for matching and O(m log m) for sorting. I'd only look at an index or a top-k heap if the catalog or QPS grew a lot, and I'd be careful with caching because stale availability would mislead the operator." ｜规模小选简单基线，说明何时才优化。

---

## 17. Implement, Refactor, Extend: Handling Changing Requirements｜实现、重构、扩展：应对需求变更

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/implement-refactor-extend-handling-changing-requirements

### 要点 / Key ideas

- 面试中途变更："保持排序，但加一个可选的**每站点上限 (per-site cap)**，免得一个站点占满操作员队列。" 挑战：保留已工作的行为，只改选择规则。
- 先问两个关键问题："站点上限是**硬上限**吗（即使留下空位）？" "不传或传 None 是否保持原行为？" —— 都是 yes。
- **需求增量 (requirement delta)**：区分新增/改变的行为与仍然有效的承诺；改前先记录；面试官替换假设时**更新契约，而不是为假设辩护**。
- Palantir 把"在现有系统中工作（修改、扩展现有代码）"列为工程能力；但不保证有固定的 implement-refactor-extend 面试顺序。
- **把保持行为的重构 (refactor)与有意的行为变更分开，各自在自己的检查点验证**。

**基线契约 / Baseline contract：`select_alerts(alerts, limit=3)`**：可信记录（唯一 alert_id、site_id、bool active、severity 1–3）；limit 正整数（bool/非整数 → TypeError，非正 → ValueError，空输入也校验）；保留 active，按 `(-severity, alert_id)` 全局排序，最多 limit 条；输出恰好 alert_id/site_id/severity 的新字典；保留输入。
- 扩展：keyword-only `per_site_limit=None`，同样的正整数校验；原承诺都保留；硬上限可能返回少于 limit 条。

**三步 / Three steps**

```python
# Step 1 - baseline (alert_selection_baseline.py)
def select_alerts(alerts, limit=3):
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer, not bool")
    if limit <= 0:
        raise ValueError("limit must be positive")
    active = [alert for alert in alerts if alert["active"]]
    ranked = sorted(active, key=lambda alert: (-alert["severity"], alert["alert_id"]))
    return [
        {"alert_id": alert["alert_id"], "site_id": alert["site_id"], "severity": alert["severity"]}
        for alert in ranked[:limit]
    ]
```

```python
# Step 2 - refactor only: extract ranking so selection can see ALL ranked candidates.
def _ranked_active_alerts(alerts):
    return sorted(
        (alert for alert in alerts if alert["active"]),
        key=lambda alert: (-alert["severity"], alert["alert_id"]),
    )
# select_alerts now calls _ranked_active_alerts(alerts); behavior is unchanged.
# Run the UNCHANGED regression suite here and snapshot/commit this version.
```

```python
# Step 3 - extend: per-site hard cap with a full scan past the old prefix.
def select_alerts(alerts, limit=3, *, per_site_limit=None):
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer, not bool")
    if limit <= 0:
        raise ValueError("limit must be positive")
    if per_site_limit is not None:
        if isinstance(per_site_limit, bool) or not isinstance(per_site_limit, int):
            raise TypeError("per_site_limit must be an integer, not bool")
        if per_site_limit <= 0:
            raise ValueError("per_site_limit must be positive")

    selected = []
    site_counts = {}
    for alert in _ranked_active_alerts(alerts):
        site = alert["site_id"]
        count = site_counts.get(site, 0)
        if per_site_limit is not None and count >= per_site_limit:
            continue                      # site is full; keep scanning
        selected.append(alert)
        site_counts[site] = count + 1
        if len(selected) == limit:        # stop only on the GLOBAL limit
            break
    return [
        {"alert_id": alert["alert_id"], "site_id": alert["site_id"], "severity": alert["severity"]}
        for alert in selected
    ]
```

- 只抽取过滤与排序：当前变更需要在**同一排序上换选择步骤**，helper 就是足够的接缝 (seam)。策略框架、类层次、无关清理只会增加需要诊断的变更。
- **相同的回归 (regression)期望让重构检查点具有诊断性**：此时失败不能归咎于上限（还没引入）。重构检查点失败 → 先修复或回退 (revert)，再叠加扩展。

**Input/Output example**

```text
Input order: A4(Y,2,active) A2(X,3,active) A5(Z,1,active) A1(X,3,active) A3(Y,3,active) A6(X,3,inactive)
Ranked active: A1, A2, A3, A4, A5

select_alerts(alerts, 3)                    -> A1/X/3, A2/X/3, A3/Y/3
select_alerts(alerts, 3, per_site_limit=1)  -> A1/X/3, A3/Y/3, A5/Z/1
select_alerts(alerts, 3, per_site_limit=2)  -> A1, A2, A3
select_alerts(alerts, per_site_limit=None)  -> A1, A2, A3   (original behavior)
select_alerts(alerts, 4, per_site_limit=1)  -> A1, A3, A5   (hard cap underfills)
select_alerts(alerts, 3, 1)                 -> TypeError     (cap is keyword-only)
```

- **诱人的错误补丁：保留 `ranked[:limit]` 再在前缀内执行上限** → 只返回 A1, A3（丢掉 A5）。两种补丁都满足"每站不超上限"，**只有精确的完整期望投影能发现丢失的合格结果**。
- 正确扫描：选 A1（X=1）→ 跳 A2（X 满）→ 选 A3（Y=1）→ 跳 A4（Y 满）→ 选 A5（Z=1）→ 达到 3 条。这是**硬上限，不是公平轮转 (round-robin)**，也不保证每个站点都出现。
- 扩展测试：cap 1/limit 3 → A1,A3,A5（severity 3,3,1）；cap 2 → A1,A2,A3；显式 None → 原输出；cap > limit → 原输出；资格不足 → 合法的不满结果；空输入上的非法 cap；keyword-only 强制。**期望只在约定需求改变该行为时才改，不能因为改后代码给出不同答案就改**。
- **时间不够时的进度陈述**："The default path must remain unchanged. The new cap changes selection; ranking and projection stay fixed. The refactor checkpoint is [executed result or unexecuted]. The capped-selection checks are [executed result or unexecuted]." 保留最后通过的版本，说明未完成行为与未执行检查，不要重来。
- 复杂度 (complexity)：全排序 O(n log n)；候选引用 O(n) 空间；计数与输出 O(s + k)。上限不需要新架构。
- 练习（B 告警，limit 4）：默认/None → B1,B2,B4,B3；cap 1 → B1,B4,B6（硬上限留一个空位）；cap 2 → B1,B2,B4,B5（超出原四个候选前缀）。

<svg viewBox="0 0 720 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="190" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Implement → Refactor → Extend, each with a checkpoint｜每步都有检查点</text>
<defs><marker id="k" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<g fill="#eef4ff" stroke="#3b6fd8"><rect x="20" y="50" width="190" height="70" rx="8"/><rect x="265" y="50" width="190" height="70" rx="8"/><rect x="510" y="50" width="190" height="70" rx="8"/></g>
<g text-anchor="middle">
<text x="115" y="75">1. Baseline 基线</text><text x="115" y="95">filter → sort → slice</text>
<text x="360" y="75">2. Refactor 重构</text><text x="360" y="95">extract _ranked_active_alerts</text>
<text x="605" y="75">3. Extend 扩展</text><text x="605" y="95">scan with site counts</text>
</g>
<g stroke="#555" marker-end="url(#k)"><line x1="210" y1="85" x2="263" y2="85"/><line x1="455" y1="85" x2="508" y2="85"/></g>
<g fill="#f3f7ee" stroke="#5a8f29"><rect x="20" y="135" width="190" height="40" rx="6"/><rect x="265" y="135" width="190" height="40" rx="6"/><rect x="510" y="135" width="190" height="40" rx="6"/></g>
<g text-anchor="middle" font-size="12"><text x="115" y="160">regression suite ✔</text><text x="360" y="160">SAME suite, unchanged ✔</text><text x="605" y="160">suite + exact cap tests ✔</text></g>
</svg>

### 面试怎么说 / How to say it in the interview

- **Confirming the delta**: "Before I change anything: is the per-site maximum a hard cap even if it leaves empty slots, and does passing None keep today's behavior exactly? … Great. So ranking and the output shape stay the same; only the selection step changes." ｜先确认需求增量，说明哪些不变。
- **Refactor first**: "I'll first extract filtering and ranking into a helper without changing behavior and rerun the same tests. If that fails, I know it's the refactor, not the new feature." ｜先重构并用原测试验证，再扩展。
- **The key bug to avoid**: "I can't slice to the limit and then apply the cap — with cap 1 that returns only A1 and A3. I need to scan the full ranked list, skip full sites, and stop only when I hit the global limit, which gives A1, A3, A5." ｜不能先切片再限流，要全扫描。
- **Running short on time**: "Here's where I am: the refactor checkpoint passes the original suite; the cap logic is written and the cap-1 and None cases pass; I haven't yet run the invalid-cap tests. I'd keep this version rather than restart." ｜诚实汇报进度：已执行 vs 未执行。

---

## 18. System Design Basics for New Grads｜新毕业生的系统设计基础

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/system-design-basics-for-new-grads

> 资深候选人也要掌握：这是 FDE 设计题的"最小可辩护基线"思路——先讲一个请求怎么走，再谈基础设施。

### 要点 / Key ideas

- **系统设计 (System Design)**：组件、接口、存储数据如何协作服务用户。对比两个校园包裹柜台 (parcel desk) 提案："加缓存、队列和几个服务" vs "授权员工确认取件，应用提交包裹新状态并返回已存储结果"——后者给了**可跟踪的请求和可检验的主张**。
- 系统描述要说明：谁调用、请求如何到达、哪个组件能改事实、重启后什么保留、调用方何时可信任响应。**光有技术名词留下这些连接未解决**。
- 第三方指南强调需求收集、架构清晰、权衡辩护、终端用户导向；报告过 60 分钟 CodePair 轮（确认自己的安排）。

**需求 / Requirements**

| 类型 Type | 内容 Content |
|---|---|
| 功能需求 Functional | 认证员工在一个组织内登记包裹、查询、确认取件 |
| 负载 Workload | 每 10 小时营业日 20,000 新包裹；40 个员工客户端每 20 秒刷新 |
| 峰值 Peaks | 登记与刷新都假设 10 倍 |
| 响应 Response | 普通请求 2 秒内 |
| 保留 Retention | 365 天 |
| 导出 Export | ≤100,000 行，假设生成 30 秒 |
| 排除 Exclusions | 收件人自助、承运商集成、支付、通知、附件；无多区域/持续可用要求 |

**组件与所有权 / Components & ownership**

- 浏览器：发操作、显示结果，**显示的副本不是权威 (source of truth)**。
- 应用：拥有登记与取件变更，执行校验与员工授权。
- 数据库：持久存 `parcel(parcel_id unique, recipient_reference, shelf_location, status, version, collected_at, collected_by)`；登记设 status=awaiting_collection, version=1。
- 导出职责：任务元数据存 DB，后台生成文件；初期可共享应用代码库与数据库。**逻辑组件边界 ≠ 部署单元 (deployment unit)**。
- 认证是给定边界：应用收到已验证的员工身份；**客户端提供的名字不是身份证据**。

**API**：`POST /parcels`（校验、创建、返回初始状态）；`GET /parcels/{id}`；有界查询（recipient 过滤 + 分页 (pagination) limit + continuation）；`POST /parcels/{id}/collect {expected_version}`（服务端提供取件人身份与时间）。**接口暴露受控动作，不是无限制的表编辑**。

**取件 P410 / Conditional transactional update**

- 诱人实现：读行 → 检查状态 → 无条件更新 (unconditional update) → 两个请求都读到 v3、都报成功、互相覆盖取件归属。
- 正确路径：
  1. `POST /parcels/P410/collect {expected_version: 3}`
  2. 检查已验证员工身份并授权；**忽略调用方提供的 collected_by**。
  3. 事务内条件更新：`WHERE parcel_id='P410' AND status='awaiting_collection' AND version=3`
  4. 同时设 status='collected', version=4, collected_by=认证身份, collected_at=服务器 UTC 时间。
  5. 改了 1 行 → 提交 → 返回已提交包裹；**提交失败不能返回成功**。
- 竞争的 v3 请求改 0 行 → conflict；改 0 行时在事务内区分"不存在"（not found）与"陈旧/已取件"（conflict）。
- **不变量 (invariant)**：一个包裹只有一次 awaiting → collected 的成功转换。提交后响应丢失 → 浏览器读当前状态；重复 v3 命令不会再取一次。

```sql
UPDATE parcel
SET status = 'collected',
    version = 4,
    collected_by = :authenticated_staff_id,
    collected_at = :server_utc_now
WHERE parcel_id = 'P410'
  AND status = 'awaiting_collection'
  AND version = 3;
-- 1 row changed  -> COMMIT, return committed row
-- 0 rows changed -> check existence: 404 if missing, 409 if stale/already collected
```

**异步导出 / Async export**：30 秒导出超过 2 秒目标 →
1. `POST /exports` 校验选择并创建持久 `ExportJob(export_id, requester, selection, status, result_ref nullable)`；
2. 事务提交后返回 export ID + pending（如 HTTP 202 Accepted）；
3. 后台 worker 认领 pending 任务，记 running，生成文件到文件/对象存储；
4. 文件可用后持久化 ready + result_ref；失败记 failed；
5. `GET /exports/{id}` 暴露 pending/running/ready/failed，ready 时才有 result_ref。
- **DB 支撑的任务列表就够了，后台执行不必须用消息代理 (message broker)；受理 ≠ 完成**。

**估算 / Back-of-envelope estimation**

| 项 Item | 计算 Calculation | 结果 Result |
|---|---|---|
| 营业日秒数 | 10 × 3,600 | 36,000 s |
| 登记平均/峰值 | 20,000 / 36,000；×10 | ≈0.56 rps；≈5.6 rps |
| 刷新平均/峰值 | 40 / 20；×10 | 2 rps；20 rps |
| 合计建模峰值 | 5.6 + 20 | ≈25.6 rps（仅这两类） |
| 原始存储 | 20,000 × 365 × 2 KB | 14.6 GB（不含索引、备份、副本、任务元数据、导出文件） |

- 测验要点（估算不证明容量 (capacity)）：14.6 GB 只是原始数据；25.6 rps 只含登记 + 刷新，**要问取件次数与聚集程度**，并计入导出提交、轮询、处理；单应用是**提议基线，不是已证明的容量**——要在合适负载下测量，包括导出干扰。分母用营业时间 36,000 s 而不是 86,400 s。
- 权衡：直接读 DB（无缓存失效 (cache invalidation)问题；缓存在未证明读瓶颈前引入陈旧显示）；单应用（无内部网络契约与部署协调，代价是不能独立扩展、共享故障边界 (failure boundary)）；后台导出（保持交互预算，但增加任务状态、worker、结果获取，仍可能争 DB 资源）。**14.6 GB 或更大峰值倍数都不自动要求分片 (sharding)或分布式数据库 (distributed database)**。

<svg viewBox="0 0 720 230" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="230" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Parcel desk baseline｜包裹柜台基线</text>
<defs><marker id="l" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<rect x="10" y="70" width="120" height="60" rx="8" fill="#eef4ff" stroke="#3b6fd8"/><text x="70" y="95" text-anchor="middle">Staff browser</text><text x="70" y="113" text-anchor="middle">员工浏览器</text>
<rect x="180" y="50" width="200" height="100" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
<text x="280" y="74" text-anchor="middle" font-weight="bold">Application 应用</text><text x="280" y="94" text-anchor="middle">authz + validation</text><text x="280" y="112" text-anchor="middle">conditional collect</text><text x="280" y="130" text-anchor="middle">POST /exports → 202</text>
<rect x="440" y="50" width="130" height="100" rx="8" fill="#fff4e0" stroke="#a67c00"/>
<text x="505" y="80" text-anchor="middle">Relational DB</text><text x="505" y="100" text-anchor="middle">parcel, version</text><text x="505" y="120" text-anchor="middle">ExportJob</text>
<rect x="440" y="170" width="130" height="50" rx="8" fill="#f3f7ee" stroke="#5a8f29"/><text x="505" y="192" text-anchor="middle">Export worker</text><text x="505" y="210" text-anchor="middle">后台导出</text>
<rect x="610" y="170" width="100" height="50" rx="8" fill="#f3f7ee" stroke="#5a8f29"/><text x="660" y="192" text-anchor="middle">File store</text><text x="660" y="210" text-anchor="middle">文件存储</text>
<g stroke="#555" marker-end="url(#l)"><line x1="130" y1="100" x2="178" y2="100"/><line x1="380" y1="100" x2="438" y2="100"/><line x1="505" y1="150" x2="505" y2="168"/><line x1="570" y1="195" x2="608" y2="195"/></g>
<text x="280" y="180" text-anchor="middle" font-size="12">No cache / queue / microservices</text><text x="280" y="198" text-anchor="middle" font-size="12">until measurements justify them</text>
</svg>

**练习：巡检请求系统 (inspection requests) — 自写参考答案**

- 需求：每 8 小时日 800 新请求 + 800 完成尝试；12 台平板每 15 秒刷新；全部 5 倍峰值；每请求 1 KB 保留 90 天；普通响应 1 秒；报告生成 12 秒。
- 估算：28,800 s/日；新建 800/28,800 ≈ 0.028 rps → 峰值 ≈ 0.14 rps；完成同为 ≈ 0.14 rps；刷新 12/15 = 0.8 rps → 峰值 4 rps；合计峰值 ≈ **4.3 rps**。存储 800 × 90 × 1 KB = **72 MB** 原始数据。
- 设计：平板 → 单应用（授权、校验、`POST /inspections`、`GET /inspections?status=open&limit=…`、`POST /inspections/{id}/complete {expected_version}` 条件更新）→ 关系型 DB；12 秒报告走 `POST /reports` → 202 + 持久 ReportJob + 后台 worker。无缓存、无队列、无分片。

### 面试怎么说 / How to say it in the interview

- **Lead with a request path, not boxes**: "Let me trace one collection: the browser posts collect with expected_version 3; the app authorizes the staff identity from the token, then runs a conditional update on id, status and version in one transaction. One row changed means commit and return the stored parcel; zero rows means I check whether it's missing or already collected and return 404 or 409." ｜先讲一个请求的完整路径。
- **Async for long work**: "The 30-second export can't sit inside a two-second request, so POST /exports creates a durable job and returns 202 with an ID; a worker moves it to running and ready. A database-backed job table is enough — I don't need a broker for this." ｜长任务异步 + 持久任务表。
- **Estimation with caveats**: "Peak is about 5.6 registrations plus 20 refreshes per second, roughly 26 rps, and about 15 GB raw over a year. That's a test workload, not proof — I still need collection volume, and I'd measure latency with exports running." ｜估算后说明它不证明容量。
- **Defending simplicity**: "One app and one relational database fit this load. I'd add a cache only if reads become a measured bottleneck, because it brings stale state and invalidation; sharding isn't justified by 15 GB." ｜为简单基线辩护，说明什么证据会改变决定。

---

## 19. FDE System Design: Data Pipelines, Integration and Reliability｜FDE 系统设计：数据管道、集成与可靠性

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/fde-system-design-data-pipelines-integration-and-reliability

### 要点 / Key ideas

- "worker 活着，但数据是 6 分钟前的。调度员能信任异常列表吗？"——快速的 dashboard 响应回答不了。可靠管道必须把**已接受的源变更、持久进度、展示给决策者的新鲜度**连起来。
- 场景：调度员 (dispatcher) 审阅所属仓库的延迟货件，决定联系谁；应用**从不自动改道**。约定承运商数据新鲜度上限 **5 分钟**；超过则：保留旧列表 + 原覆盖时间戳 + 醒目的陈旧状态；禁用依赖承运商的联系建议，直到刷新或批准的人工检查。
- **用户可见的新鲜度必须跟随已提交的源覆盖 (committed source coverage)**；存活的 worker 或快速 HTTP 响应都不能证明源完整或物理现实。
- 依据：FDSE 职位描述提到面向客户的架构设计、业务关键数据、定制应用、端到端执行；第三方指南强调以用户为中心的管道、摄取、存储、可靠性与权衡。

**所有权 / Ownership**

| 来源 Owner | 事实 Facts |
|---|---|
| 承运商 Carrier | 货件状态、源修订号、事件时间、受限的收件人联系方式 |
| 运营应用 Operations app | 仓库分配（S71 属于 D4）、内部备注——摄取不能覆盖 |

- 承运商 API 承诺：稳定货件 ID、**每货件单调递增 (monotonically increasing)修订号**、显式删除标记、可恢复的变更分页 (resumable change pages)；完成有界追赶 (bounded catch-up) 返回 continuation cursor + **源确认的 complete-through 时间戳**（含空响应时）。**完整性保证来自 API 契约；没有就要弱化新鲜度声明并用周期性权威快照——时间戳字段造不出完整性**。

**持久记录 / Persistent records**

| 记录 Record | 内容 Content |
|---|---|
| CarrierState | 货件 ID、已接受修订号、规范化自有字段内容（状态、事件时间、受限联系方式）；到达时间单独存 |
| LocalShipment | 货件 ID、仓库分配、内部备注 |
| FeedProgress | 已提交 cursor + complete-through 时间戳 |
| Run | run ID、起始 cursor、状态、issue 引用、**claim generation、lease 到期、心跳 (heartbeat)时间** |
| Issue | 失败类别、受限的可重放输入引用、负责人、解决审计 |

- 调度员投影：货件 ID、状态、事件时间、管道覆盖。

**重复、迟到、冲突 / Duplicates, late, conflicts**（至少一次投递 at-least-once）

- 相同已接受修订 → no-op；更低修订不能替换；**同修订不同内容 → 可见冲突**。测验：S71 r9 已接受 → 相同 r9 重放 no-op；r8（更晚到达）不能替换；同 r9 不同内容 → 记 issue 并阻止该候选发布。**到达顺序规则混淆了传输行为与权威**。
- 每个有界追赶私下暂存 (staged)；校验后**原子提交 (atomic commit)：已接受变更 + 源 cursor + 覆盖时间戳 + run 成功**；从已提交版本发布投影；**提交后才确认 (acknowledgment follows commit)**。

**S71 状态走查 / Predicted state trace**（2026-10-29 UTC）

| # 时间 | 输入 | 承运商状态 | 本地 | 已提交进度 | Run/Issue |
|---|---|---|---|---|---|
| 1 · 10:02 | 完整有效追赶，gen 7 | r8 → r9 arrived_depot | D4 不变 | C0→C1，覆盖→10:02 | succeeded；确认丢失 |
| 2 · 重放 | 相同 r9 | 不变 | 不变 | 不变 | 可记成功与心跳 |
| 3 · 10:03 | r8 到达 | 拒绝旧修订 | 不变 | 不变 | 追赶无法完成，不提交进度 |
| 4 · 10:04 | 从 C1 追赶，r10 schema 不支持，gen 8 | 私有候选被扣留，保持 r9 | 不变 | 不变（10:02） | run held；E1 打开 |
| 5–6 · 崩溃边界 | 提交前 / 提交后确认前 | 前：旧状态 / 后：新状态持久 | 不变 | 前：旧检查点 (checkpoint) / 后：新检查点 | 前：可能仍 running / 后：succeeded |
| 7 · 10:08 | 近期 worker 心跳 | 不变 | 不变 | 不变 | 只推进心跳 |
| 8 · 接管 | gen 8 租约 (lease)过期，新 claim gen 9 | **旧 gen 8 提交被拒** | 不变 | 不变 | E1 仍开 |
| 9 · 10:09 | 批准映射后从 C1 重放，gen 9 | r9 → r10 | D4 保留 | C1→C2，覆盖→10:09 | succeeded；E1 带审计关闭；发布后确认 |

- 提交前崩溃留旧状态与检查点；提交后确认前崩溃 → 重放靠身份检查。这些协调保证防止**重复的逻辑摄取效果**，不是任意外部系统的 exactly-once。
- **事件时间 (event time)** vs **到达时间 (arrival time)**：都不证明所有源变更已到；更高修订可能带更早事件时间，仍按修订契约处理。
- Schema：显式批准的新增可选字段可忽略；必填字段删除或含义变化需审查过的映射。
- **每小时对账 (reconciliation)** 对比带截止时间 (cutoff)的权威快照：快照显示 S88 r6、已接受 r5 → 取回并走正常校验重放；S89 缺失 → 调查，**无法解释的缺失不授权删除**；删除只认显式删除标记。

**10:08 的信号与行动 / Signals → owners → actions**：覆盖 10:02，10:08 时已 6 分钟 > 5 分钟 → 告警 (alert)集成负责人 + 应用陈旧视图限制，**即使有近期心跳**。

| 度量 Measure | 含义 Meaning |
|---|---|
| 覆盖年龄 Coverage age | 源确认的已提交截止落后于现在多久 |
| 成功处理时间 Successful processing time | 上次 run 成功提交的时间 |
| 最老待处理年龄 Oldest pending age | 已知工作等了多久 |
| 事件年龄 Event age | 源描述的事件有多旧 |
| 心跳 Heartbeat | **只证明 worker 活动** |

| 故障 Failure | 信号 Signal | 负责人 Owner | 有界行动 Bounded action |
|---|---|---|---|
| 覆盖 > 5 分钟 | 陈旧视图，覆盖告警 | 集成负责人 | 调查阻塞；保留列表与原时间戳；禁用联系建议 |
| 瞬时拉取失败 | 失败次数、连续失败、最老待处理 | 集成运维 | **最多 3 次尝试，递增退避 + 抖动 (backoff + jitter)，45 秒 run 预算内**；遵守限流 (rate limiting)指示；之后持久记失败，等下一次轮询 |
| Schema 不支持 | 立即 issue + 受限输入引用 | 映射负责人 | 扣留候选等批准映射，再走校验重放 |
| 同修订不同内容 | 冲突 issue | 源/集成负责人 | 调查源不一致，不静默覆盖 |
| 授权失败/凭据 (credentials)撤销 | 授权告警 | 凭据负责人 | 停止轮询直到恢复 |
| worker 租约过期 | 过期 claim 指标 | worker 控制器 | 60 秒租约过期后回收，**递增 claim generation，隔离 (fence) 旧提交** |
| 快照缺失/不一致 | 对账 issue | 集成负责人 | 有效差异重放；缺失调查，不隐式删除 |

- **Worker 租约 (lease) + 隔离令牌 (fencing)**：租约 60 秒；回收时递增 generation；**每个发布事务同时检查当前 generation 与未过期租约**，拒绝过时 worker 的提交。**仅靠租约过期无法阻止暂停的 worker 恢复后写入**。
- 被审计的错误修复："HTTP 200 就设 last_refreshed_at；立即确认分页"；"按到达顺序 upsert"；"不支持的 schema 一直重试直到通过；回收过期租约，旧 worker 可正常完成"；"继续返回缓存的 D4 列表，因为原请求已授权"。→ 重复拉无效 schema 修不了含义；之后的成功 HTTP 也不应关闭 issue——**解决取决于经校验的恢复提交，不是恢复连通性**。
- 10:09 修复：runbook 识别阻塞 run 与起始 cursor → 查看受限 issue → 获得批准映射 → 在当前 claim 下从最后提交检查点重放 → 完整校验候选后提交并发布。若还有记录校验失败，保留旧发布与陈旧状态。
- 权衡：保留可重放输入有存储与访问控制成本；扣留整个有界追赶 = **真实的完整性 (completeness)优先于可用性 (availability)**；按独立分区 (partition)发布是替代方案，但需分区级新鲜度与用户可见的完整性。

**访问控制 / Access control**

- 承运商读取服务身份只限摄取；应用身份只限批准的派生数据；都无无关管理权限。Dashboard 检查已认证调度员的**当前**仓库范围再投影字段，包括保留的陈旧视图。
- 收件人电话与内部备注不进共享异常投影、指标标签、普通日志；审计访问受限，记录最小的 actor、action、scope、run/记录引用、结果、时间。技术控制不证明匿名或合规。
- **导出 worker 评估请求者当前范围；获取时再次授权** → 撤销 D4 访问也会阻止之前的 D4 导出。初期无响应缓存；若测量证明需要，按授权范围/策略版本 + 数据版本做 key 与失效，强制新鲜度，返回前复查权限。**隐藏 dashboard 控件不是边界**。
- 练习检查：14:04 时 I22 仍为 r5/fail、审核人 R6、F2；覆盖仍是 14:01，已 3 分钟 > 2 分钟上限；新修订即使事件时间更早也胜出；14:05 撤销 F2 权限后即使之前授权生成也无法获取导出。

<svg viewBox="0 0 720 260" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="260" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Carrier pipeline: atomic progress + fencing｜原子进度 + 隔离</text>
<defs><marker id="m" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<rect x="10" y="60" width="110" height="60" rx="8" fill="#eef4ff" stroke="#3b6fd8"/><text x="65" y="85" text-anchor="middle">Carrier API</text><text x="65" y="103" text-anchor="middle">poll 1/min</text>
<rect x="160" y="50" width="170" height="80" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
<text x="245" y="72" text-anchor="middle">Worker (gen N, lease 60s)</text><text x="245" y="92" text-anchor="middle">stage + validate</text><text x="245" y="112" text-anchor="middle">私下暂存 + 校验</text>
<rect x="370" y="40" width="200" height="110" rx="8" fill="#fff4e0" stroke="#a67c00"/>
<text x="470" y="62" text-anchor="middle" font-weight="bold">One transaction 单事务</text><text x="470" y="82" text-anchor="middle">check gen + lease</text><text x="470" y="100" text-anchor="middle">CarrierState (by revision)</text><text x="470" y="118" text-anchor="middle">cursor + complete-through</text><text x="470" y="136" text-anchor="middle">run = succeeded</text>
<rect x="610" y="50" width="100" height="80" rx="8" fill="#f3f7ee" stroke="#5a8f29"/><text x="660" y="75" text-anchor="middle">Projection</text><text x="660" y="93" text-anchor="middle">+ coverage</text><text x="660" y="111" text-anchor="middle">then ack</text>
<g stroke="#555" marker-end="url(#m)"><line x1="120" y1="90" x2="158" y2="90"/><line x1="330" y1="90" x2="368" y2="90"/><line x1="570" y1="90" x2="608" y2="90"/></g>
<rect x="160" y="170" width="170" height="60" rx="8" fill="#fdecea" stroke="#c0392b"/><text x="245" y="195" text-anchor="middle">Issue (schema/conflict)</text><text x="245" y="213" text-anchor="middle">hold candidate 扣留</text>
<line x1="245" y1="130" x2="245" y2="168" stroke="#c0392b" marker-end="url(#m)"/>
<rect x="370" y="170" width="340" height="60" rx="8" fill="#fdecea" stroke="#c0392b"/>
<text x="540" y="193" text-anchor="middle">Dispatcher view: coverage age &gt; 5 min → stale banner,</text><text x="540" y="213" text-anchor="middle">contact recommendations disabled 陈旧即禁用建议</text>
</svg>

### 面试怎么说 / How to say it in the interview

- **Freshness is coverage, not liveness**: "The dashboard's 'as of' time comes from the source-confirmed complete-through timestamp that we committed, not from the last HTTP 200 or a worker heartbeat. At 10:08 with coverage at 10:02, we're six minutes stale, so the list stays visible with its original timestamp and contact recommendations are disabled." ｜新鲜度来自已提交的源覆盖，不是心跳。
- **Ordering and duplicates**: "I order by the source's per-shipment revision, not arrival time. Same revision and same content is a no-op, a lower revision is ignored, and the same revision with different content is a visible conflict that blocks publication." ｜按源修订排序，三种情况分别处理。
- **Atomic progress**: "Accepted changes, the cursor, the coverage timestamp and the run status commit in one transaction, and we only acknowledge after commit. A crash before commit replays from the old checkpoint; a crash after commit replays harmlessly because of the revision checks." ｜进度与数据同事务提交，提交后才确认。
- **Fencing stale workers**: "Leases alone don't stop a paused worker from waking up and writing. So every publish transaction checks the claim generation and that the lease is unexpired; reclaiming bumps the generation, which fences the old worker." ｜租约 + generation 隔离。
- **Access on exports**: "Exports are authorized at generation and again at download against the user's current depot scope, so revoking D4 blocks an old D4 file too." ｜导出生成和下载时都按当前权限校验。

---

## 20. Practice: Designing an Operational System With Access Control｜练习：设计带访问控制的运营系统

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/practice-designing-an-operational-system-with-access-control

### 要点 / Key ideas

- **English problem statement**: "Give a supervisor a usable failed-inspection review list across five facilities without exposing another facility's records or inspector contacts — even when the inspection feed stops advancing. The hard boundary is the moment a review selection becomes durable: permission, source freshness and both versions must agree there."

| 方面 Aspect | 题目包 Packet |
|---|---|
| 流程 Workflow | 主管决定哪些不合格设备巡检需要跟进审阅；首版 5 个设施；记录选择**不**派技术员、不改设备控制、不认证安全 |
| 源拥有 Source-owned | 巡检 ID、设备引用、结果、修订号、事件时间、**受限的巡检员联系方式** |
| 本地拥有 Local-owned | 设施归属、审阅人分配、审阅处置、本地版本——摄取必须保留 |
| 权限 Permissions | 主管只能在**当前**授权设施内查看与操作；联系方式不进主管视图与导出；后台工作只拿职责所需权限 |
| 源保证 Source guarantees | 每巡检单调修订、规范内容比较、可重放变更页、显式删除标记、每次完成有界追赶后源确认的 complete-through |
| 新鲜度 Freshness | 每分钟轮询 (polling)；覆盖 > **3 分钟** → 列表陈旧 (stale)，**服务端阻止依赖源的审阅选择**；已提交记录在当前权限内仍可见，保留原截止 |
| 导出 Exports | 受理只是记录请求；生成与获取都执行当前权限；就绪文件不能绕过撤销 |
| 负载 Workload | 每 10 小时日 12,000 巡检更新；24 客户端每 15 秒刷新；两者 5 倍峰值；180 天 × 1 KB；普通请求 1 秒；导出 15 秒 |

- **三个关键澄清问题**：主管能派工吗？（不能，权限止于审阅选择）源能证明完整性吗？（能；否则弱化新鲜度声明）谁能收导出？（认证请求者通过应用获取；更多接收者需显式授权）
- **试点指标**：5 个工作日，约定每日审阅截止与会议时间；合格总体 (population) = 5 个设施中截止前已提交、审阅开始时仍待处置的不同不合格巡检；指标 = 会议前获得处置记录的比例（用已提交审阅与审计记录）；护栏 (guardrail) = 未处理项年龄、重复审阅选择。

**持久记录 / Persistent records**：InspectionState（ID、已接受修订、规范源字段、删除状态、单独的到达时间；联系方式对主管投影不可访问）、LocalReview（ID、设施、审阅人、处置、本地版本）、FeedProgress（cursor + complete-through）、Run（起始 cursor、状态、claim generation、租约 (lease)到期、诊断）、Issue（类别、受限重放输入引用、负责人、解决审计）、ExportJob（请求者、选择、状态、nullable result_ref）。

**API**

- `GET /review-items`：服务端检查当前设施范围，返回有界投影 (projection)（巡检 ID、设备引用、结果、审阅处置、已提交覆盖），**从不返回联系方式**；陈旧保留视图也走同样权限检查。
- `POST /review-items/{id}/select {expected_revision, expected_local_version, reviewer}`：actor 来自认证边界。记录前检查：
  1. 对本地拥有的设施有当前权限，审阅人在该设施合格；
  2. 已提交覆盖不落后服务器时间超过 3 分钟；
  3. 巡检修订匹配、当前未删除且结果为 fail、本地版本匹配；
  4. 本地转换 unreviewed → selected_for_review 被允许。
- **检查与本地写必须共享协调的事务边界 (transaction boundary)**：按一致顺序锁定授权策略状态、FeedProgress、InspectionState、LocalReview；权限变更、摄取发布、本地变更遵守同一协调协议；**提交前立即重新检查基于时间的新鲜度**并限制事务时长。外部权限服务需要同样明确的撤销一致性 (revocation consistency)契约。**很早之前做的权限检查不够**。
- 同事务记录处置、审阅人、本地版本递增、最小审计；提交后才返回成功；过期版本或竞争选择 → conflict；陈旧 → 阻止；未授权不泄露细节。
- **成功分支（事故前）**：新鲜覆盖 + 当前 F3 权限，用 r4/local v2 选择 → selected_for_review、R2、local v3，修订仍 4；竞争的 local v2 命令 → conflict。

**I64 事故走查 / Incident trace**（2026-10-29 UTC）

| 时间 | 已接受源状态 | 本地 | 覆盖/检查点 | 用户结果 |
|---|---|---|---|---|
| 08:00 | r4 / fail | F3/R2/unreviewed/v2 | 08:00; C0 | 可列出 |
| 08:01 | r5 / fail（事件 07:58） | 不变 | 08:01; C1; 成功但确认丢失 | U7 的 E7 被受理（≠ 就绪） |
| 08:02 | 相同重放，保持 r5 | 不变 | 保持 08:01; C1 | 无重复效果；E7 生成时授权后就绪 |
| 08:03 | r3 不能回退 r5；必填字段 schema 变更阻止候选 | 不变 | 保持 08:01; 记失败 run | 无部分发布；记 issue 与受限重放引用 |
| 08:05 | 保持 r5 / fail | 不变 | 08:01，**覆盖年龄 4 分钟** | 主管可看保留列表（原截止 + 陈旧状态），**选择被阻止**；告警 (alert)集成负责人；U7 失去 F3 → **E7 获取被拒且不泄露 F3 细节** |
| 08:06 | r6 / **pass**（事件 08:04） | 不变（源不拥有） | 08:06; C2; issue 带审计关闭 | 批准映射 + 校验重放在当前租约/generation 下提交；**期望 r5 的请求冲突；pass 结果也不再合格** |

- 决策边界解释了两次被拒的选择：08:05 是**陈旧**；08:06 新鲜度恢复但**修订不匹配**且结果已为 pass。
- 重放控制：同 Lesson 19（原子提交 + 提交后确认；修订比较；最多 3 次尝试 45 秒预算；必填 schema 变更需批准映射；60 秒租约 + generation 隔离；覆盖 > 3 分钟告警；每小时对账 (reconciliation)，缺失不是删除）。

**E7 的三个授权边界 / Three export boundaries**：受理（记录 U7 与选择，返回 pending）→ 生成（检查 U7 当前范围，只投影允许字段）→ 获取（**重新授权**请求者与文件所需范围）。不发可复用的公开下载链接；多设施文件含新近未授权记录 → 拒绝或重新生成允许的投影。最小权限 (least privilege)：摄取凭据 (credentials)只读源；面向主管的 worker 只拿派生数据；联系方式不进输出、导出、普通日志、指标标签。

- **表面完整的错误设计**：只在浏览器过滤设施（直接请求可达受保护记录）；每次 fetch 成功就设新鲜（阻塞的覆盖被标为新鲜，放行无依据的选择）；可复用导出链接（撤销后仍可用）。**图上一个"访问控制"框本身不建立任何执行点**。

**估算 / Estimates**

| 项 | 计算 | 结果 |
|---|---|---|
| 更新 | 12,000 / 36,000；×5 | ≈0.33/s；峰值 ≈1.67/s |
| 刷新 | 24 / 15；×5 | 1.6 rps；峰值 8 rps |
| 原始存储 | 12,000 × 180 × 1 KB | 2.16 GB |

- 更新与客户端请求是不同工作类型，**相加不得出 HTTP 请求估算**；源页数、批大小、处理成本未知；存储不含索引、备份、重放输入、本地状态、导出。

**三个可辩护的权衡 / Trade-offs（需求 → 替代 → 成本 → 重新考虑触发器）**

| 选择 Choice | 替代 Alternative | 代价 Cost | 何时重新考虑 Reconsider when |
|---|---|---|---|
| 关系型基线 + 直接授权读 | 缓存或独立部署服务 | 失效 (invalidation)或协调成本 | 测得延迟、饱和 (saturation)或部署隔离需求 |
| 异步导出 | 同步生成（更简单） | 持久任务 + DB 争用 (contention) | 测量导出运行时普通请求延迟受显著干扰 → 限并发或隔离资源 |
| 整个有界追赶一起发布 | 分区发布（未受影响设施继续推进） | 需分区级检查点与新鲜度 | 测得阻塞成本高且源支持独立覆盖 |

<svg viewBox="0 0 720 270" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="270" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Decision boundary for "select for review"｜审阅选择的决策边界</text>
<defs><marker id="n" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<rect x="10" y="100" width="120" height="60" rx="8" fill="#eef4ff" stroke="#3b6fd8"/><text x="70" y="125" text-anchor="middle">Supervisor</text><text x="70" y="143" text-anchor="middle">POST select</text>
<rect x="170" y="40" width="330" height="180" rx="10" fill="#fff4e0" stroke="#a67c00"/>
<text x="335" y="62" text-anchor="middle" font-weight="bold">One coordinated transaction 单一协调事务</text>
<text x="335" y="90" text-anchor="middle">1. current facility permission + reviewer eligible</text>
<text x="335" y="115" text-anchor="middle">2. coverage age ≤ 3 min (rechecked before commit)</text>
<text x="335" y="140" text-anchor="middle">3. revision matches, not deleted, result = fail</text>
<text x="335" y="165" text-anchor="middle">4. local version matches; unreviewed → selected</text>
<text x="335" y="195" text-anchor="middle">write disposition + version++ + audit</text>
<rect x="540" y="50" width="170" height="45" rx="8" fill="#f3f7ee" stroke="#5a8f29"/><text x="625" y="77" text-anchor="middle">200 after commit</text>
<rect x="540" y="110" width="170" height="45" rx="8" fill="#fdecea" stroke="#c0392b"/><text x="625" y="137" text-anchor="middle">409 stale version</text>
<rect x="540" y="170" width="170" height="45" rx="8" fill="#fdecea" stroke="#c0392b"/><text x="625" y="190" text-anchor="middle">blocked: stale feed /</text><text x="625" y="206" text-anchor="middle">403 no detail</text>
<g stroke="#555" marker-end="url(#n)"><line x1="130" y1="130" x2="168" y2="130"/><line x1="500" y1="90" x2="538" y2="72"/><line x1="500" y1="130" x2="538" y2="132"/><line x1="500" y1="175" x2="538" y2="190"/></g>
<text x="360" y="255" text-anchor="middle">Ingestion publish and permission changes use the SAME lock order 同一锁顺序</text>
</svg>

### 面试怎么说 / How to say it in the interview — full walkthrough script

> **Clarify & scope**: "Three questions change the design. Can the supervisor dispatch work, or only select for review? … Only select. Does the source tell us how complete our data is? … Yes, a complete-through timestamp per catch-up. And who receives exports? … Only the requester, through the app. So version one is: list failed inspections in my facilities, and record 'selected for review' with an eligible reviewer — no dispatch, no equipment control, no safety certification."
>
> **Data & ownership**: "The source owns inspection identity, result, revision, event time and inspector contacts; we own facility placement, reviewer, disposition and a local version. I keep those in separate tables — InspectionState and LocalReview — plus FeedProgress for the cursor and complete-through timestamp, Run and Issue for the pipeline, and ExportJob. Ingestion can only touch source-owned columns."
>
> **Read path**: "GET /review-items checks the caller's current facility scope on the server and projects only ID, equipment, result, disposition and the committed coverage time. Contacts are never in the projection, the export, logs or metric labels."
>
> **The decision boundary**: "POST select carries the expected inspection revision and expected local version. Inside one transaction I check current permission and reviewer eligibility, that coverage is no more than three minutes old — rechecked right before commit — that the revision matches and the result is still fail, and that the local version matches. Then I write the disposition, bump the version and add an audit row, and only return success after commit. Permission changes and ingestion publishing take the same locks in the same order, so nothing slips in between the check and the write."
>
> **Incident walkthrough**: "At 08:01 we commit revision 5 with coverage 08:01 but lose the ack; the 08:02 replay is a no-op. At 08:03 a revision 3 can't regress us and a required-field schema change blocks the whole catch-up, so coverage stays at 08:01 and we open an issue. At 08:05 coverage is four minutes old: the supervisor still sees the list, marked stale with its original cutoff, but selection is blocked server-side and the integration owner is paged. At 08:06 an approved mapping replays and commits revision 6, pass. A select expecting revision 5 now conflicts — and the item isn't eligible anyway because it passed."
>
> **Exports**: "E7 has three checks: acceptance, generation and retrieval. U7 lost F3 at 08:05, so the ready file is denied without revealing anything — no reusable public links."
>
> **Numbers & trade-offs**: "About 1.7 updates per second and 8 refreshes per second at peak, 2.2 GB raw over 180 days — I don't add those together because they're different kinds of work. I'd keep one relational app with direct authorized reads and reconsider a cache only on measured latency; exports are async and I'd measure interference; and I publish whole catch-ups for truthful completeness, switching to per-facility partitions only if blockage costs justify it."
>
> **Success measure**: "For a five-day pilot: share of eligible failed inspections that get a recorded disposition before the daily review meeting, with guardrails on unresolved-item age and duplicate selections. Nothing here proves a safety outcome."

中文要点：三个澄清 → 源/本地字段分表 → 服务端范围过滤 + 投影 → 选择时在单事务内检查权限、新鲜度（提交前复查）、修订、本地版本 → 事故走查（陈旧阻止 vs 修订冲突）→ 导出三次授权 → 估算不相加 → 三个带触发器的权衡 → 试点指标。

---

## 21. Embedded Behavioral Questions: Answering Well in 15–20 Minutes｜技术轮中嵌入的行为问题：15–20 分钟答好

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/embedded-behavioral-questions-answering-well-in-15-20-minutes

### 要点 / Key ideas

- 场景："Tell me about a mistake you made and what changed afterward." 而你的 `totals_by_team(entries)` 写到一半：累加循环已实现、一个普通检查通过、空输入未检查。
- 先说 "Sure — may I take a few seconds to note where I am?" **协调暂停、保存位置、回答时停止写代码**。

**中断检查点 / Interruption checkpoint（四字段）**

| 字段 Field | 内容 Content |
|---|---|
| 契约 Contract | 按团队累加整数分钟；空输入返回 `{}`；负分钟抛 ValueError |
| 实现 Implementation | 累加循环已实现；**边界行为仍需验证** |
| 已执行检查 Executed checks | `[('A',3),('A',2),('B',4)]` → `{'A':5,'B':4}`；空输入与负值**未检查** |
| 下一步 Next action | 检查空输入，期望 `{}` |

- 测验陷阱：写"边界已验证/全部通过"或"计划中的检查返回了 {}"都是把预测当执行。
- **时长依据**：Palantir 公开指南（经汇总）描述 onsite 会问执行力、挑战自己、激励他人、判断与失败；面试数量与格式**按候选人技能与岗位个性化**——向 recruiter 确认。第三方 SWE 指南说技术轮内有 15–20 分钟行为问题（不足以作为 FDSE 普遍规则）；2022-10 有候选人描述一小时学习轮约一半是行为讨论（历史个例）。→ 把 15–20 分钟当**排练分配**，开场回答约 **2 分钟**，过渡由面试官控制。

**压缩故事时保留什么 / What survives compression**

1. 问题与你的责任 (problem & responsibility)
2. 你的决定、为什么失败、你做了什么 (decision, why it failed, what you did)
3. 观察到的结果及其局限 (observed result & limits)
4. 你行为上的具体改变 (concrete change in behavior)

- **先砍时间线和附带细节**，不要砍个人决定、因果推理、合作者、证据局限、行为改变。可靠数字有用；没有数字时，直接观察到的行为也可以作为结果。

**示例：CSV 导入器错误（练习素材，不是你的经历）— 压缩后的英文回答**

> "In a three-person project, I implemented a CSV importer and made a wrong identity assumption. I used display names as record keys without checking whether names could repeat, which meant two distinct records could collapse into one entry.
> A teammate discovered it using two different record IDs with the same display name. I had chosen examples with distinct names, so my checks never challenged my assumption. I reproduced the collision and checked the input contract with the team, which confirmed the supplied record ID was the intended identity.
> I changed the importer to key by that ID and added same-name, different-ID regression cases; my teammate reviewed it. Against the final twelve-fixture suite, six failed on the old implementation and all twelve passed on the new one.
> That result is limited to local checks — the importer wasn't deployed, so I can't claim user or production impact.
> What changed in my practice: I now write identity assumptions into my implementation checklist, and before the next import change I added a collision case up front."

| 段落 Paragraph | 保留的证据 Evidence kept |
|---|---|
| 责任与原因 | 你实现了导入器，选错了 key |
| 发现与推理 | 队友发现；你的例子都是不同名字所以漏了 |
| 修复与验证 | 改为 ID key + 回归用例 + 队友审阅 |
| 结果边界 | 旧实现 6/12 失败，新实现 12/12 通过，本地、未部署 |
| 反思 | 下一次先加碰撞用例——**展示行为改变，而不只是说"我学到了"** |

**追问 / Follow-ups**：先精确回答问题、给必要证据、然后停。

- "Why did you not catch it sooner?" → "I assumed display names were unique and selected only distinct-name examples, so my checks reflected the assumption instead of testing it. I should have confirmed identity and included a collision case earlier."（承认自己的决定，不怪发现问题的队友）
- "Did this improve the users' workflow?" → "I don't have evidence of user improvement. The evidence is the local regression results and the reviewed change; the importer wasn't deployed."

**两种更弱的回答 / Weaker answers**

- 过短："We fixed the importer and made it reliable. I learned to communicate." → 去掉了你的错误、修复机制、队友贡献、验证边界、改变的实践。
- 过长："First we divided up the project, then discussed… all twelve fixtures passed, proving it was production-ready." → 时间线多了但因果证据没回来；12 个本地夹具不能证明生产就绪。把 "production-ready" 改成 "passed the twelve local fixtures" 是**改变主张本身**，不只是语气。

**回到技术题 / Returning**："The accumulation loop is implemented. The ordinary run returned {'A': 5, 'B': 4}. Empty input and negative-value rejection remain unchecked. My next action is to check empty input, expecting {}." 没有运行环境就说 "That is my proposed check and expected result." **不要跳去优化**——会跳过你明确保存的未完成验证；需求在讨论中变了就先更新契约。

```python
def totals_by_team(entries):
    """Sum minutes by team; reject negative minutes.

    Preconditions: entries contains (team, minutes) pairs,
    where team is a nonempty string and minutes is an integer.
    """
    totals = {}
    for team, minutes in entries:
        if minutes < 0:
            raise ValueError("minutes must not be negative")
        totals[team] = totals.get(team, 0) + minutes
    return totals

# Next action: run totals_by_team([]) and compare with {} before recording a result.
# Negative-value rejection stays unchecked until it is explicitly tested.
```

- 用自己真实经历排练：先写空检查点，伙伴可以提前喊回；分别评估故事质量与技术恢复；保留第一次尝试，找一个关键遗漏，再来一次。没有合适经历就记录证据缺口——练习素材只能演示结构。

### 面试怎么说 / How to say it in the interview

- **Pausing cleanly**: "Sure — give me ten seconds to jot down where I am so I can pick it back up." ｜请求几秒保存检查点。
- **Resuming honestly**: "Picking back up: the loop is done and the mixed-team case passed. Empty input and negative minutes are still unchecked, so next I'll run the empty case and expect an empty dict." ｜回来时准确复述已执行 vs 未执行。
- **Bounding impact in a story**: "Those were local checks on a project that wasn't deployed, so I can't claim user impact — what I can show is six of twelve fixtures failing before and all twelve passing after." ｜主动说明结果边界。

---

## 22. The Behavioral Question Bank: Pushback, Failure, Ownership and Ambiguity｜行为题库：反对意见、失败、负责到底与模糊性

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/the-behavioral-question-bank-pushback-failure-ownership-and

### 要点 / Key ideas

- 一个亮眼的上线故事可能只回答四类请求之一。**故事库 (story bank)** = 真实事件 + 每个事件包含的证据的索引——按证据选事件，再换重点但**不换事实**。
- 依据：Palantir 公开招聘页（经汇总）提到执行力 (execution)、挑战自己 (challenging yourself)、激励他人 (motivating others)、判断 (judgments)、失败 (failures)。第三方报告题："Tell me about a time you pushed back on a customer request." 其他候选人报告主题：模糊的端到端负责、失败的项目及结论、选第一版并砍范围。四主题库是课程自创的准备工具，不是官方评分表。

**故事卡字段 / Story card fields**

| 字段 Field | 要写什么 What to record |
|---|---|
| 事件与利害 Event & stakes | 发生了什么、谁需要什么、什么会出错 |
| 责任与权限 Responsibility & authority | 你负责什么、你能决定什么 |
| 合作者 Collaborators | 还有谁贡献、他们的目标与约束 |
| 信息 Information | 当时知道什么、什么未知 |
| 决策 Decision | 考虑过哪些方案、接受了什么权衡 |
| 行动与结局 Actions & resolution | 你做了什么、**谁决定了结果** |
| 观察结果与局限 Observed result & limits | 什么支持结果、什么未测量 |
| 改变的行为 Changed behavior | 之后具体做了什么不同的事 |
| 索引 Index | 主主题、次主题、可能的追问 |

- "良好的利益相关方 (stakeholder)沟通"不是决策证据——要写对方告诉了你什么、改变了哪个选择。可用经授权的项目/实习/研究/志愿/工作经历；**只讲你被允许披露的**（去掉公司名不等于获得许可）。

**示例：240 工单导出（课程练习素材）**

- 运营负责人要一个每晚包含全部 240 张 open 工单的表格。候选人起初提议改成显示 50 张的界面；问用途后得知两位审阅者**离线工作需要完整集合** → 承认提议不合适。剩下更窄的担忧：文件含联系方式且会发给调度团队以外的人 → 与数据所有者核对字段权限 → 提议完整导出但只含 ticket ID、status、queue，联系方式留在受限应用。运营负责人接受流程、数据所有者批准字段、候选人实现投影、队友审阅。
- 证据对应：240 个 ID 各恰好一次 → **完整覆盖**；无联系字段 → **字段排除**；两位审阅者确认能离线审阅 → **利益相关方流程接受**；候选人实现、队友审阅 → **有边界的贡献归属**；下次导出设计前先记录接收者与离线需求 → **展示出的行为改变**。**都不证明节省时间或更广泛采用**。
- 主题适配：主 = pushback；次 = ambiguity（未知的离线需求改变了提案）；有有边界的实现负责，但**没有持续运营跟进的证据**；**不是失败项目**（不合适的提议在实现前就被修正了）→ 失败题要换一个真实事件。
- 夸大的反面复述："客户要不安全的表格，我反对，说服所有人用我的安全 dashboard，省了几小时。我的失败是太在乎质量。" → 改了结局、忽略离线需求、抢了别人的审批权、编造节省、用讨好的特质冒充失败。
- 其他三个练习条目：**失败**（错过 demo：负责集成排期却拖到最后一天，组件对不上，错过承诺的演示；承认排期决定；下一里程碑提前做集成检查发现不匹配）；**负责到底**（维护交接：接手 importer，加回归测试、写发布与回滚 (rollback)说明；维护者批准、授权运维执行；交接时继任者按 runbook 独立完成；后来参加事故复盘 (postmortem)并更新恢复说明——不暗示独自完成或拥有发布权）；**模糊性**（"更好的告警"：考虑每日摘要 vs 即时通知，观察用户在下一班前决定哪些需要处理 → 首版改为班次优先审阅列表）。

**选择问题 / Selection questions**

| 主题 Theme | 自问 Ask yourself |
|---|---|
| 反对 Pushback | 理解对方后我重新考虑了什么？ |
| 失败 Failure | 到底哪里出错了，我的决定如何促成？ |
| 负责 Ownership | 我把什么责任扛到底了，包括交接或之后的问题？ |
| 模糊 Ambiguity | 哪个关键不确定性改变了我的决定？ |

### 题库与 STAR 英文模型回答 / Question bank with STAR model answers

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 38 篇）。

**Q1. Tell me about a time you pushed back on a customer request.｜讲一次你对客户请求提出异议**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 38 篇）。

**Q2. Tell me about a project that failed. What did you conclude?｜讲一个失败的项目，你得出什么结论**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 38 篇）。

**Q3. Tell me about a time you owned something end to end when the scope was ambiguous.｜讲一次在范围模糊时端到端负责**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 38 篇）。

**Q4. Tell me about a decision you made with incomplete requirements.｜讲一次需求不完整时做的决定**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 38 篇）。

**Q5. Tell me about a time you chose a first version and cut scope.｜讲一次你选第一版并砍掉范围**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 38 篇）。

**Q6. Tell me about a time you executed under pressure.｜讲一次在压力下的执行（execution）**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 38 篇）。

**Q7. Tell me about a time you challenged yourself / learned something new quickly.｜讲一次挑战自己、快速学习**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 38 篇）。

**Q8. Tell me about a time you motivated others or helped a team move.｜讲一次激励他人**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 38 篇）。

**Q9. Tell me about a difficult judgment call.｜讲一次困难的判断**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 38 篇）。

**Q10. Tell me about a disagreement with a teammate.｜讲一次与同事的分歧（pushback 变体）**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 38 篇）。

**常见追问 / Common follow-up probes**（答案要能回答，且**不改事实**）

| 追问 Probe | 英文回答要点 Answer sketch |
|---|---|
| What did you rule out? (Q2) | "A second rule engine for rollback, and restoring a stale 'passed' snapshot — both would have hidden the seller's current facts." |
| How do you know the result? | "The capabilities shipped. Where I only have targets or forecasts, I say targets or forecasts." |
| How much did this improve efficiency? | "I don't have a measured before-and-after for that, so I won't give a number." |
| What changed afterward? | "I involve the owner of any system I depend on during requirement breakdown, and treat operating capacity as a design constraint." |
| How did your decision contribute to the failure? (Q2) | "I accepted a coordinated, non-atomic recovery to avoid a second rule engine; that's why per-action idempotency should have come first." |
| Why not a DB lock? (Q9) | "A row lock protects a transaction; this was a multi-step transition across processing paths." |

### 面试怎么说 / How to say it in the interview

- **Bounding results**: "I want to be precise: the capability shipped, but the review-volume number is a design target, not a measured result." ｜主动说明结果边界。

---

## 23. The Hiring Manager Final: What It Re-tests and How to Prepare｜招聘经理终面：重测什么、怎么准备

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/the-hiring-manager-final-what-it-re-tests-and-how-to-prepare

### 要点 / Key ideas

- 场景：邀请确认 60 分钟招聘经理对话，没说技术形式；recruiter 说"准备一个项目深入讲，解释用户需求如何影响你的决策"；你自己的笔记：拆解回答从没说清一个具体的写操作。**保持三类来源分开**：

| 类别 Category | 内容 Content |
|---|---|
| 已确认安排 Confirmed logistics | 60 分钟 HM 对话；技术形式未知 |
| 给定准备建议 Supplied guidance | 准备一个项目，讲用户驱动的决策 |
| 自我观察 Self-observation | 之前的操作太抽象 |
| 准备假设 Preparation hypothesis | 练习具体写操作能弥补该缺口（**不预测终面内容**） |

- 依据：Palantir 早期人才时间线（经汇总）提到 HM 面试**根据 onsite 反馈定制**——只适用于早期人才招聘；第三方指南说会重测 onsite 较弱的领域（不保证你最弱的轮会重复）；2025-07 候选人报告一小时在行为与拆解式问题间交替；社区指南说包括简历决策、动机、对 Palantir 的兴趣 + 技术内容，约 30/30 分（报告，不是通用时间表）。
- 被审计的错误推断："recruiter 说拆解是我最弱的轮，所以终面会重复，我只准备旧题"（改变了证据来源与含义）；"让最后读到的面经决定准备"（近因偏差 recency bias）；"只看拿到 offer 的候选人报告的格式"（幸存者偏差 survivorship bias）。

**三条准备线 / Three preparation lanes**

1. **项目深度与动机 (project depth & motivation)**：选一个真实、获授权的项目，准备好被追问开场故事之下的决策。
2. **定向修补 (targeted repair)**：把模糊的写操作变成输入、检查、状态变化、失败行为、验证。
3. **不同任务的就绪 (different-task readiness)**：编码、拆解、学习、重构调试、系统设计的短期检索练习（准备池，不是承诺的五个组件）。

- 问 recruiter："Will there be a technical exercise? What tools and logistics apply? Is there any preparation focus you can share?" 没答的保持未知。

**项目深度示例：工作坊报名 (workshop registration)**

- W8 容量 (capacity) 12、已确认 11；每人每工作坊只能报名一次；重复请求不能占额外座位。候选人实现了报名与 8 个本地顺序夹具；队友做界面；**无部署、无并发测试、无出勤收益证据**。
- 初始排练："Check the count and save." → 项目深度图暴露未解决的部分：

| 维度 Dimension | 内容 Content |
|---|---|
| 身份 Identity | workshop_id；(workshop_id, participant_id) 标识一个报名 |
| 规则 Rule | 新确认报名必须保持确认数 ≤ 容量；已存在的报名不占额外座位 |
| 贡献 Contribution | 报名函数与本地夹具是候选人的；界面是队友的 |
| 替代方案 Alternative | 只在界面检查（可被其他调用者绕过）vs 在写边界执行规则——除非有历史证据，否则说成"比较"而不是"我当时否决了" |
| 失败行为 Failure behavior | 满员/重复时实际返回什么（记不清就看代码） |
| 验证与局限 Validation & limits | 说出实际夹具输入与断言；"8 个通过"本身说明不了检查了什么 |

- 动机连接："I liked translating the capacity and duplicate rules into working behavior. That makes customer-facing implementation appealing to me. My evidence here is a local prototype; customer deployment is experience I want to develop." FDSE 职位描述：客户协作、架构与实现、定制应用、利益相关方参与、端到端执行。

**并发追问：P14 和 P15 同时抢第 12 个座位**

- 现有应用侧检查：P14 读到 11；P15 在 P14 插入前也读到 11；都通过；都插入 → **13 个确认**。顺序夹具 (sequential fixtures)从未制造这种交错 (interleaving)——**承认这个局限是诚实辩护项目的一部分**。
- 提示 "What must be serialized?" 后的方案：

```sql
BEGIN;
SELECT * FROM workshop WHERE workshop_id = 'W8' FOR UPDATE;      -- exclusive row lock
SELECT 1 FROM registration
 WHERE workshop_id = 'W8' AND participant_id = :pid;             -- duplicate? return existing, no new seat
SELECT COUNT(*) FROM registration
 WHERE workshop_id = 'W8' AND status = 'confirmed';             -- fresh count under the lock
INSERT INTO registration (workshop_id, participant_id, status)
VALUES ('W8', :pid, 'confirmed');                                -- only if count < capacity, else return "full"
COMMIT;                                                          -- report success only after commit; ROLLBACK on failure
-- Plus: UNIQUE (workshop_id, participant_id) enforces identity independently.
```

- **所有报名写入者都必须获取同一个工作坊锁**；唯一约束 (unique constraint)单独防重复；容量固定（未来改容量的操作也需协调）。效果：第一个看到 11 并提交第 12 个；第二个拿到锁后看到 12 → full。这是**推理的提议扩展，原型未实现也未验证**。
- 取消竞争：P03 取消与 P16 报名都拿同一把锁。取消先提交 → P16 看到 11 可以报名；报名先拿锁 → P16 看到 12 被拒，之后取消留下 11——**拒绝不会悄悄变成自动报名**。
- 工作坊锁串行化合作的写者；唯一约束保护参与者身份；**二者互不替代**；绕过协议的写者会破坏容量论证。

**排练校准 / Rehearsal calibration（七个维度，课程自创）**

问题框定与范围 · 技术执行 · 数据与运营判断 · 学习与适应 · 验证与证据局限 · 协作与负责 · 动机与反思。每个相关维度记录：确切问题、观察到的行动、后果、标签（demonstrated / partial / not evidenced）、下一个追问。**无官方等级、权重或通过线**；短尝试未引出的维度标 not evidenced，不代表没能力；被提示后的适应要和独立表现区分。

- 工作坊示例：数据判断（身份）= demonstrated；技术执行初始 = partial（"check the count and save"）；验证局限 = demonstrated（准确限定为本地顺序行为）；学习适应 = 提示后 demonstrated；协作 = demonstrated（区分自己与队友的工作）。
- 选两类排练：观察到的弱项 + 一个对比类。本例：**拆解 + 编码**。**同一清单适用于两个级别**：新毕业生讲项目决策、可工作的实现与可见的学习；**资深候选人还要加上真实的生产约束、客户决策与持续负责**（在经历支持的范围内），同时仍要追到实现细节。缺的经验记为缺口。
- 一页准备单：已确认/未知安排、带来源的反馈、一个项目深度图、有边界的动机提纲、选定的排练组合、两个改进行动（每个写：缺口 → 行为改变 → 新的检查）。例："并发写没解释 → 用提议的事务追踪两个请求 → 新检查：取消与报名竞争，并指出仍未测试的部分"；"'8 个夹具'掩盖了验证细节 → 找回实际输入、期望与断言 → 新检查：为新需求实现并执行一个检查，结果单独记录"。
- 24 分钟校准排练：8 分钟项目与动机追问 + 10 分钟所选类型任务 + 6 分钟证据评审；保留第一次，改一个关键缺口，再用陌生的需求变更追问不看笔记回答一次。**背诵式重放可能隐藏同样的推理缺口**。

<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="200" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Lost update without serialization｜无串行化时的丢失更新</text>
<defs><marker id="o" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<line x1="80" y1="45" x2="80" y2="180" stroke="#3b6fd8" stroke-width="2"/><text x="80" y="40" text-anchor="middle">P14</text>
<line x1="260" y1="45" x2="260" y2="180" stroke="#a67c00" stroke-width="2"/><text x="260" y="40" text-anchor="middle">P15</text>
<g font-size="12"><text x="90" y="70">read count = 11</text><text x="270" y="90">read count = 11</text><text x="90" y="115">insert → 12</text><text x="270" y="135">insert → 13 ✘</text></g>
<rect x="400" y="50" width="310" height="120" rx="8" fill="#f3f7ee" stroke="#5a8f29"/>
<text x="555" y="74" text-anchor="middle" font-weight="bold">Fix 修复</text>
<text x="555" y="96" text-anchor="middle">lock workshop row (FOR UPDATE)</text>
<text x="555" y="116" text-anchor="middle">re-count under lock → insert or "full"</text>
<text x="555" y="136" text-anchor="middle">UNIQUE(workshop, participant)</text>
<text x="555" y="156" text-anchor="middle">all writers + cancels use same lock</text>
</svg>

### 面试怎么说 / How to say it in the interview

- **Defending the project honestly**: "My eight fixtures were sequential, so they never tested two people taking the last seat. With the current check-then-insert, both could read 11 and we'd end up at 13." ｜主动承认测试局限并指出竞态。
- **Proposing the fix**: "I'd serialize on the workshop: lock the workshop row in a transaction, check for an existing registration, re-count under the lock, and insert only if there's a seat — committing before reporting success. A unique constraint on workshop and participant handles duplicates separately, and cancellations take the same lock. To be clear, that's a proposal; I haven't implemented or tested it." ｜给方案并标明是提议、未验证。
- **Motivation tied to evidence**: "What I enjoyed was turning capacity and duplicate rules into working behavior with real users in mind — that's why customer-facing implementation appeals to me." ｜动机连接到具体做过的事。
- **Asking the recruiter**: "Will the final include a technical exercise, and is there any area you'd suggest I focus on?" ｜向 recruiter 确认形式。

---

## 24. Team Matching, the Offer and Negotiation｜团队匹配、offer 与谈判

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/team-matching-the-offer-and-negotiation

### 要点 / Key ideas

- **硬性要求 (hard requirement)** = 会因此拒绝 offer 的条件；**偏好 (preference)** = 在满足硬性要求的 offer 中排序。**先过硬性要求，再比总包 (total compensation)**。
- 示例（练习包，非真实 Palantir offer）：要求 base ≥ $160k、出差 ≤ 20%、不搬家。Offer A：base $155k + sign-on $20k = 首年 $175k，设备维护流程实现 + 生产支持，本市；Offer B：base $160k + sign-on $5k = 首年 $165k，数据集成，本市。A 首年现金高，但**经常性 (recurring) base 差 $5k**，出差未确认。
- 第三方指南报告匹配通常在 onsite 之后；确认你的申请顺序以及接受前什么是最终的。FDSE 职位描述写"出差最多 25%，可根据个人偏好灵活"、办公室/混合/特殊远程的区分——**要核实具体团队的安排**。

**团队证据账本 / Team-evidence ledger**

| 条件 Condition | 当前证据 Evidence | 来源 Source | 决策影响 Consequence |
|---|---|---|---|
| A 职责 | 面向客户实现 + 生产支持 | 经理口述 | 偏好未定：问负责边界、支持期望、客户与使命背景 |
| A 地点 | 本市，到办公室天数未确认 | 比较包 | 要求已满足；问办公天数 |
| A 出差 | 职位写最多 25%，团队实际未确认 | 职位描述 | **接受阻塞项**：与 20% 上限的兼容性未确认 |
| B 职责与地点 | 书面：数据集成，本市 | 书面团队摘要 | 要求满足；工作与办公细节未定 |
| B 出差 | 书面：最多 10% | 书面团队摘要 | 满足 |
| B 支持 | 书面：无排班 on-call；偶发事故支持期望未定 | 书面团队摘要 | 影响未定 |
| 双方团队与分配 | 经理、导师、分配稳定性、匹配何时最终 | 比较包；指南 | 区分偏好与会拒绝的条件 |

- 问未来经理：**工作与目的**（实际工程职责、客户与使命背景、实现负责、生产支持）；**工作关系**（经理、导师、办公出勤、支持升级）；**分配条件**（出差频率与时长、分配稳定性、匹配何时最终）。美国政府职位申请会问其他面试阶段、决策时间线、安全许可 (clearance)、出差、搬迁 (relocation)、薪酬范围 (salary range)、国际出差。
- 该 FDSE 职位估计薪资 $135k–$200k/年，可能含 RSU、sign-on、其他激励（职位特定，非保证）。

**拆解薪酬 / Compensation components**

| 组件 Component | Offer A | Offer B |
|---|---|---|
| 经常性年 base | $155,000 | $160,000 |
| 一次性 sign-on | $20,000 | $5,000 |
| 条件/酌情奖金 (discretionary bonus) | 10% 酌情目标（=$15,500，**不算可靠现金**） | 无 |
| RSU 与计划 | 1,000 RSU；每年 250 × 4 | 600 RSU；每年 150 × 4 |
| 福利 | 未知 | 未知 |
| 首年 base + sign-on | $175,000 | $165,000 |
| 条件 | sign-on 入职后支付，**12 个月内主动离职全额返还** | 同 |
| 书面接受截止 | 2026-11-06T17:00Z | 2026-11-12T17:00Z |

- 第二年起 base：A $155k vs B $160k。**再加 $10k sign-on → A 首年 $185k，但经常性 base 仍 $155k，出差仍未定 → 两个阻塞项都在**。更大的一次性付款可以改善偏好，但不能满足要求。
- **RSU（限制性股票单位 restricted stock unit）**：在指定条件下与公司股票挂钩的奖励；**归属 (vesting)**：按条件与计划获得权利。A 每期 250 股，B 每期 150 股。情景价值：$80/股 → A $20,000、B $12,000；$120/股 → A $30,000、B $18,000——**算术情景，不是预测、保证收益或到手金额**；查看授予文件的实际授予、归属、结算、出售条件；不要假设每年有 refresh。A 的更大授予**不能满足经常性 base 要求**。
- 对 A 有用的请求：base 提到 $160k + 确认兼容的出差安排 + 截止从 11-06 延到 11-10。**修订后的条件是书面确认清单，不是 A 已同意的证据**；解除阻塞只让 offer 进入考虑范围，不证明最适合。

**谈判信 / Negotiation message**

- ✘ 错误版："你的包只有 $155k，我另一个 offer 保证 $190k/年。sign-on 加 $10k 我今天就签；出差会自己解决的。"（抹掉组件；编造的 $190k；只加 sign-on 不解决 base；在硬性要求未解决时承诺立即接受）
- ✔ 修复版（英文原意）：

> "Thank you for the offer. I'm particularly interested in the maintenance-workflow implementation responsibilities. My requirements are at least USD 160,000 annual base, no relocation, and travel of no more than 20%. Could you raise the base to USD 160,000 and confirm a team arrangement compatible with that travel limit? Another written offer has a USD 160,000 base. Could you also extend the acceptance deadline from November 6 to November 10 so I can review the clarified terms? I remain interested and would appreciate written confirmation of any changes."

- 没有竞争 offer 也可以提同样基于优先级的请求。清晰的请求给雇主一个具体可考虑的东西，但不保证灵活。
- 按实际给出的条件回应：只加 $10k sign-on → 说明经常性 base 要求仍未满足；出差无法确认在上限内 → 暂停或拒绝（薪酬解决不了该约束）；延期被拒 → 按原截止用已确认条件 + 明确的不确定性决定。**进行中的面试 ≠ 书面 offer；延期请求在确认前不改变截止日**。
- 新练习（只有一个书面 offer：base $150k、sign-on $30k 可返还、无保证奖金、800 RSU 四年；要求 base ≥ $155k、不搬家、出差 ≤ 20%；经理估计出差 20–30%；另一家只是约了面试）：错误说法——把 sign-on 当经常性薪资；声称另一家"书面 offer"提供筹码；沿用旧包的截止日。正确：首年 $180k、之后 $150k；每期 200 股 → $60 时 $12,000、$100 时 $20,000；只加 sign-on → 仍不满足 base。

### 面试怎么说 / How to say it in the interview

- **Asking the prospective manager**: "Could you walk me through what a typical month looks like — how much is on-site with the customer, how long trips usually are, and who I'd work with day to day? And when does the team assignment become final?" ｜问工作内容、出差频率与时长、团队与匹配最终时间。
- **Negotiating on the real gap**: "The sign-on is generous, but my priority is recurring base — could you get the base to 160? A bigger sign-on doesn't change that for me." ｜针对经常性 base 而不是一次性奖金谈。
- **Deadline**: "Could we extend the deadline to the 10th so I can review the clarified terms? I'll treat the current deadline as binding until I hear back." ｜请求延期但在确认前按原截止对待。

---

## 25. Full Mock Loop: New Grad｜完整模拟面试：新毕业生版

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/full-mock-loop-new-grad

> 资深候选人只需看与 Lesson 26 的差异；这里给结构与各题要点。

### 要点 / Key ideas

- **210 分钟**七站（课程自创，不是邀请预测；Palantir 说面试数量与格式按候选人与岗位个性化）：

| 站 Station | 分钟 | 内容 |
|---|---:|---|
| 动机与项目 Motivation/project | 15 | Why Palantir / why FDSE；一个真实的学术/个人/研究/实习项目 |
| 技术 Technical | 60 | 30 依赖排序 + 15 SQL + 15 分页 API |
| 拆解 Decomposition | 40 | 海岸线协调员选 3 个次日巡检点 |
| 学习与修复 Learning/repair | 40 | 25 RowPath 扩展 + 15 计数修复 |
| 入门系统设计 Intro design | 25 | 食品库库存查询与预留 |
| 新追问 Fresh follow-up | 10 | 选一张卡 |
| 证据评审 Evidence review | 20 | 七维 + 两个目标 |

- 权限：除非 recruiter 明确允许，**练习时不用候选人侧 AI**（保守假设，不是已证实的公司规则）；雇主 AI 记录员同意与否不影响候选资格，但不等于候选人可用 AI。
- 技术题要点：
  - `plan_steps`：A,B,C,D,E；A→C、B→C、C→D、重复 A→C；**去重 (deduplication)要同时作用于邻接 (adjacency)插入与入度 (indegree)递增**（错误：`neighbors[a].add(b); indegree[b] += 1` 总是递增 → C 入度 3，误报环）；分钟 23 加 D→B → 必须 ValueError，不返回部分列表；O(V+E)。
  - SQL：10 月创建的请求（半开区间 (half-open interval)）、对**全部**结果历史按 `outcome_at DESC, outcome_id DESC` 取 rn=1；从 regions LEFT JOIN；`COUNT(request_id)` 排除占位行；`NULLIF(count,0)` + numeric 除法。期望 N 2/2/0/1；S 0/0/0/NULL；W 1/0/1/0。
  - API：从 `'start'` 开始，None 终止且**永不作为请求 cursor**；快照稳定、重复 cursor 拒绝；只重试 RetryableError，同 cursor 最多 3 次；记录校验（UTC 时间戳 (timestamp)、amount 为 int 非 bool）；**全局去重先于 10 月过滤**；冲突即失败；不返回部分结果。期望 N count 2 total 3；S count 1 total 7。
- 拆解：数据卡（observation_id、observed_at、uploaded_at、location 是巡检区域不是精确坐标、tentative_asset_id、reporter、source_reference；无 severity）；O1/O2 可能是同一资产；Z3 覆盖 L4 但无观测。分钟 25 变更：**报告量会让选择偏向报告多的地点**（偏差 bias）；精确报告者位置与身份受限 → 修订覆盖护栏 (guardrail)、授权输出与有界指标；报告数不能证明环境改善。
- 学习：RowPath `latest(key, time, tie)` 每 key 保留一行、排除缺失时间、平局取更大 tie；`keep(field, value)` 排除缺失字段；当前 open 预览只含 R2（先 latest 再 keep）。计数修复：`[('A',2),('B',4),('A',3)]` 应得 `{'A':5,'B':4}`（原实现覆盖而非累加）。
- 设计：两个 feed 各拥有不相交的源范围与数量；10,000 更新/10 小时、20 客户端每 30 秒、5 倍峰值、2 秒目标；**快照完整性 (snapshot completeness)与源版本语义未给出——要问或声明假设**；10 分钟 feed 中断时陈旧数量不能成为当前库存承诺。
- 追问卡：断开的图环；无请求的 SQL 区域（E: 0/0/0/NULL）；c1 永久 RetryableError（3 次后报错、无总数、不请求 None）；新历史行关闭 R2（无 current-open 行）；**预留响应在提交后丢失**（重试用同一操作 ID 返回已提交的预留，不再预留——身份、持久化、原子性 (atomicity)、授权、并发重试）。
- **冻结 (freeze) 第一次尝试后才看参考**；评审写 "Expected result understood; execution unrecorded"，而不是 "Test passed"。

### 面试怎么说 / How to say it in the interview

- **Dedup in Kahn's algorithm**: "I deduplicate pairs before touching both adjacency and indegree — otherwise the duplicate A→C leaves C waiting for a release that never comes and a valid graph looks cyclic." ｜去重同时作用于邻接与入度。
- **Lost reservation response**: "The client sends an operation ID with the reservation. The server stores that ID with the committed reservation in the same transaction, under a unique constraint, so a retry — even a concurrent one — returns the same reservation instead of reserving again." ｜用操作 ID + 唯一约束实现幂等重试。

---

## 26. Full Mock Loop: Experienced｜完整模拟面试：资深版（重点）

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/full-mock-loop-experienced

### 要点 / Key ideas

- 核心命题：**再漂亮的生产架构也修不了一个没执行的函数，也证明不了客户影响**。资深模拟要在同一证据记录里同时保留：可工作的实现细节、客户决策、持续负责。
- Palantir 把 FDSE 描述为面向客户的架构、实现、端到端执行，包括与技术利益相关方 (stakeholders)和高管打交道 → 资深练习需要实现细节 + 客户与运营推理。

| 站 Station | 分钟 | 内容 |
|---|---:|---|
| 动机与负责 Motivation & ownership | 20 | 连接 Palantir 能力 → 客户决策 → 你真实做过的事 → why FDSE；追踪一个例子的完整生命周期 |
| 技术筛选 Technical screen | 60 | 30 部署顺序 + 15 SQL + 15 事故分页 API |
| 拆解 Decomposition | 40 | 三个公交路口的交通改善 |
| 学习与修复 Learning & repair | 45 | 25 并发 depot 刷新 + 20 图报告调试（226 行包） |
| 系统设计 System design | 40 | 双源设备对账 + 中断/撤权 + 离线运维部署 |
| 新追问 Fresh follow-up | 15 | 选一张卡 |
| 证据评审 Evidence review | 20 | 七维 + 两个目标 |
| **合计** | **240** | |

- 开始前：记录运行时、工具权限、无障碍安排 (accommodations)（是背景不是缺陷）；Python 3.12、PostgreSQL 16、ISO 8601 UTC；允许本地文档；**未获 recruiter 明确许可前不用候选人侧 AI**。

### Station 1 — Motivation & ownership（20 分钟）

- 追踪一个获准讲的例子：初始决策 → 亲自实现 → 发布约束 → 事故或需求变更 → 交接或持续运营。区分你的行动、合作者、观察到的测量、证据局限；不属于你的阶段说出负责人。
- 追问（直接回答）：What did you personally implement? Who disagreed with a consequential choice? What customer control constrained the work? What measurement supports the outcome? What changed afterward, and who owned recovery or handover? What can you not substantiate?
- **资深 = 持续的决策 + 生产后果；不等于可以编造范围或影响**。

**English model answer structure（填你自己的真实项目）**

> "One capability I studied is how an ontology lets operational users act on integrated data rather than just view it — and that's the part of my own work I've enjoyed most. On my last major project, I personally designed and implemented [component] for [user group]. The consequential choice was [decision]; [person/role] disagreed because [reason], and we settled it by [evidence]. The customer's [change-control window / security control] meant we could only deploy through [process], so I built [rollback/feature flag]. After launch, [incident or changed requirement] happened; I [action], and [owner] handled [phase I didn't own]. The measurement I can stand behind is [metric with source]; what I can't substantiate is [limit]. When I handed it over, [successor] ran [procedure] without me. That arc — from a customer decision to running software someone else can operate — is why FDSE fits me."

### Station 2 — Technical screen（60 分钟）

**(a) `deployment_order(service_ids, dependencies)`（30 分钟）**

- **English problem statement**: "Return any complete topological order of services. Pairs point prerequisite → dependent; duplicate pairs count once; isolated services are included; inputs are not mutated; any cycle (including disconnected and self cycles) raises ValueError — never a partial plan."

```text
service_ids  = ['ingest', 'normalize', 'publish', 'audit', 'archive']
dependencies = [('ingest','normalize'), ('normalize','publish'), ('ingest','audit'), ('ingest','normalize')]
Output: e.g. ['ingest', 'archive', 'normalize', 'audit', 'publish']
Minute 23 change: add ('publish','ingest') -> ValueError('dependency cycle')
Also: disconnected X<->Y cycle -> ValueError; self-cycle a->a -> ValueError
```

```python
from collections import deque


def deployment_order(service_ids, dependencies):
    adjacency = {service: [] for service in service_ids}
    indegree = {service: 0 for service in service_ids}
    seen_pairs = set()
    for prerequisite, dependent in dependencies:
        if (prerequisite, dependent) in seen_pairs:   # duplicate pair counts once
            continue
        seen_pairs.add((prerequisite, dependent))
        adjacency[prerequisite].append(dependent)
        indegree[dependent] += 1

    ready = deque(service for service in service_ids if indegree[service] == 0)
    order = []
    while ready:
        service = ready.popleft()
        order.append(service)
        for dependent in adjacency[service]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                ready.append(dependent)

    if len(order) != len(service_ids):                # any cycle -> no partial plan
        raise ValueError('dependency cycle')
    return order
```

- 追踪：初始入度 (indegree) ingest 0、normalize 1（重复只算一次）、publish 1、audit 1、archive 0 → 队列 ingest, archive → 输出 ingest 释放 normalize、audit → normalize 释放 publish。分钟 23 加 publish→ingest：ingest 入度 1，只输出 archive，5 个中 1 个 → ValueError。
- 常见错误：对重复 ingest→normalize 也递增入度 → normalize 永远等不到第二次释放 → 合法图被误拒。
- 复杂度 (complexity)：V 服务、E 对；期望 O(V + E) 时间与空间（哈希 (hash)），结果 O(V)。
- **分钟 12 中断**：保存四字段检查点 (checkpoint)（契约 / 实现状态 / 已执行检查 / 下一步），回答一个真实的 pushback 或 failure 问题，然后恢复。

**(b) SQL 区域延迟报告（15 分钟）**

- **English problem statement**: "For orders created in [2026-10-01, 2026-11-01) UTC, select one complete latest delivery-history row per order from ALL history (greater update_id wins event_at ties). Late = selected outcome late; missing history or selected 'unknown' = unknown. Report every region, including empty ones; late_share = late_count / order_count as a non-integer ratio, NULL for zero orders."

```text
Expected (region order):
region | order_count | late_count | unknown_count | late_loss_cents | late_share
East   | 2           | 1          | 0             | 100             | 0.5
North  | 0           | 0          | 0             | 0               | NULL
West   | 1           | 0          | 1             | 0               | 0
```

```sql
WITH latest AS (
    SELECT order_id, outcome,
           ROW_NUMBER() OVER (PARTITION BY order_id
                              ORDER BY event_at DESC, update_id DESC) AS rn
    FROM delivery_history                 -- rank ALL history, not only October
),
october_orders AS (
    SELECT order_id, region, loss_cents
    FROM orders
    WHERE created_at >= TIMESTAMPTZ '2026-10-01T00:00:00Z'
      AND created_at <  TIMESTAMPTZ '2026-11-01T00:00:00Z'
)
SELECT r.region,
       COUNT(o.order_id) AS order_count,
       COUNT(o.order_id) FILTER (WHERE l.outcome = 'late') AS late_count,
       COUNT(o.order_id) FILTER (WHERE l.order_id IS NULL OR l.outcome = 'unknown') AS unknown_count,
       COALESCE(SUM(o.loss_cents) FILTER (WHERE l.outcome = 'late'), 0) AS late_loss_cents,
       (COUNT(o.order_id) FILTER (WHERE l.outcome = 'late'))::numeric
           / NULLIF(COUNT(o.order_id), 0) AS late_share
FROM regions r
LEFT JOIN october_orders o ON o.region = r.region
LEFT JOIN latest l ON l.order_id = o.order_id AND l.rn = 1
GROUP BY r.region
ORDER BY r.region;
```

- 要点：E1 的 update 11 与 12 时间相同，12（late）胜出 → 100 cents；E2 最新行是 11-02 的 update 22（on_time），**从全部历史排名**，即使在 10 月之后；W1 无历史 → unknown；边界外订单排除。**先把历史归约成每单一行再聚合 (aggregate)**——先 join 原始历史会放大；`SUM(DISTINCT loss_cents)` 会合并两个合法的 100 cents。

**(c) 事故快照分页 `incident_totals(fetch_page)`（15 分钟）**

- **English problem statement**: "First call `fetch_page(None, None)`. Capture the page's non-empty snapshot and forward it unchanged with the exact opaque next_cursor. Validate every page and record; normalize timestamps to UTC; compare canonical duplicates globally BEFORE October filtering (conflicts fail even outside the window); repeated cursor or changed snapshot fails; retry only RetryableError, at most three total attempts per cursor; any failure raises with no partial aggregate. Return {region: {'count', 'minutes'}} for October."

```text
snapshot-v7, 3 pages:
  page 1: I1 East 4 @ 2026-10-01T00:00:00Z
  page 2 (c1, fails retryably once): I1 again @ 2026-10-01T01:00:00+01:00 (same instant), I2 West 6 @ Oct 20
  page 3 (c2): I3 East 3 @ Oct 31, I4 West 8 @ 2026-11-01T00:00:00Z (excluded: upper bound)
Calls: (None, None), ('c1','snapshot-v7') x2, ('c2','snapshot-v7')
Output: {'East': {'count': 2, 'minutes': 7}, 'West': {'count': 1, 'minutes': 6}}
```

```python
from datetime import datetime, timezone

OCT_START = datetime(2026, 10, 1, tzinfo=timezone.utc)
NOV_START = datetime(2026, 11, 1, tzinfo=timezone.utc)
MAX_ATTEMPTS = 3


class RetryableError(Exception):
    pass


def _fetch_with_retry(fetch_page, cursor, snapshot):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            return fetch_page(cursor, snapshot)
        except RetryableError:
            if attempt == MAX_ATTEMPTS:
                raise                      # exhaustion re-raises; no partial totals
        # any other exception propagates immediately


def _canonical(record):
    for key in ('id', 'region'):
        if not isinstance(record.get(key), str) or not record[key]:
            raise ValueError('invalid ' + key)
    minutes = record.get('minutes')
    if isinstance(minutes, bool) or not isinstance(minutes, int) or minutes < 0:
        raise ValueError('invalid minutes')
    instant = datetime.fromisoformat(record['occurred_at'])
    if instant.tzinfo is None:
        raise ValueError('naive timestamp')
    return record['id'], (record['region'], minutes, instant.astimezone(timezone.utc))


def incident_totals(fetch_page):
    seen = {}                              # id -> canonical payload, global
    requested = set()
    cursor, snapshot = None, None
    while True:
        page = _fetch_with_retry(fetch_page, cursor, snapshot)
        if not isinstance(page, dict) or not isinstance(page.get('records'), list):
            raise ValueError('malformed page')
        page_snapshot = page.get('snapshot')
        if not isinstance(page_snapshot, str) or not page_snapshot:
            raise ValueError('invalid snapshot')
        if snapshot is None:
            snapshot = page_snapshot
        elif page_snapshot != snapshot:
            raise ValueError('snapshot changed')
        for record in page['records']:
            incident_id, payload = _canonical(record)
            if incident_id in seen and seen[incident_id] != payload:
                raise ValueError('conflicting duplicate ' + incident_id)
            seen[incident_id] = payload    # dedup BEFORE window filtering
        next_cursor = page.get('next_cursor')
        if next_cursor is None:
            break
        if not isinstance(next_cursor, str) or not next_cursor or next_cursor in requested:
            raise ValueError('invalid or repeated cursor')
        requested.add(next_cursor)
        cursor = next_cursor

    totals = {}
    for region, minutes, instant in seen.values():
        if OCT_START <= instant < NOV_START:
            bucket = totals.setdefault(region, {'count': 0, 'minutes': 0})
            bucket['count'] += 1
            bucket['minutes'] += minutes
    return totals
```

### Station 3 — Decomposition（40 分钟）：三个公交路口

- **English problem statement**: "Improve traffic around three bus intersections." 答案卡：交通运营负责人 (transit operations lead) **下周可以选一个地点做有人监督的信号配时试点 (signal-timing pilot)**；记录有公交通过时间、信号周期、偶尔的行人计数；**没有**紧急车辆覆盖与完整行人覆盖。分钟 25 披露：降低公交延误可能增加行人等待；**原始车辆标识不能导出**。

### 面试怎么说 / How to say it in the interview — Station 3 full walkthrough script

> **Clarify**: "Who decides, and what can they actually do next week? … The transit operations lead can pick one intersection for a supervised signal-timing pilot. What does 'delay' mean to them — bus schedule adherence, or travel time through the intersection? Which records can we join — bus passages, signal cycles, pedestrian counts? Who authorizes a timing change, and how would we monitor pedestrian and emergency effects? And which outputs are allowed to leave the system?"
>
> **Thin slice**: "So the first version is one supervised timing pilot at one intersection the lead selects, with a comparison report — not citywide optimization."
>
> **Model & grain**: "I'd key on intersection_id, approach_id and signal_cycle_id, with one row per bus passage event and one row per signal phase interval per cycle and approach, keeping provenance and clock-quality flags. Pedestrian counts are separate sampled observations with explicit coverage intervals — missing coverage is unknown, never zero."
>
> **Write contract**: "Authorized ingestion accepts source and event ID, intersection, approach, UTC event time, source revision and payload; it validates schema and references and returns accepted, duplicate or quarantined. Same identity and revision with different content goes to review. Raw identifiers stay only in the restricted local store."
>
> **Read contract**: "An authorized pilot-comparison request names an intersection and matched observation windows; the response has aggregate passage counts, median and p95 bus delay, sample coverage, pedestrian waiting observations, freshness and methodology — no raw vehicle identifiers."
>
> **Baseline & measure**: "Compare matched route, direction and time-of-day periods against a documented baseline with sample sizes and confounders. Before activation, agree with the lead on a numeric bus-delay improvement threshold and a pedestrian-wait guardrail — I won't invent those numbers."
>
> **Revision at minute 25**: "Since cutting bus delay can raise pedestrian waits and raw IDs can't be exported, I change the proposal: add supervised pedestrian monitoring where coverage is missing, a pedestrian guardrail with a stop rule, and aggregate-only outputs to authorized recipients. Stop and revert on a guardrail breach, unsafe observations, insufficient monitoring, invalid clocks or operator concern. Emergency coverage is unavailable, so I'd get the required operational sign-off rather than claim no emergency impact. All of this is proposed — no traffic improvement has been measured."

中文要点：谁决定、下周能做什么 → 一个路口的监督试点 → 粒度与键、缺失覆盖为未知 → 写/读契约（不导出原始 ID）→ 匹配基线 + 事先约定阈值与护栏 → 分钟 25 加行人监测与停止条件 → 承认紧急车辆数据缺失。

### Station 4 — Learning & repair（45 分钟）

**(a) Depot 刷新（25 分钟）**：契约——`wait_all` 等待但不抛 worker 错误；`ticket.result()` 抛对应错误；完成顺序未指定；`commit` 原子替换 (atomically replaces)目录。要求：私下暂存 (staging)、**即使失败也检查每个 ticket**、保留第一个观察到的异常直到全部检查完、**拒绝跨 depot 重复的 item 身份（即使数量相同）**、仅完全成功后提交**一次**；出错不提交；不承诺上游同时快照。

```python
def refresh(depot_ids, pool, store):
    tickets = [(depot_id, pool.submit(depot_id)) for depot_id in depot_ids]
    pool.wait_all([ticket for _, ticket in tickets])
    first_error = None
    payloads = []
    for depot_id, ticket in tickets:               # inspect EVERY ticket
        try:
            payloads.append((depot_id, ticket.result()))
        except Exception as error:
            if first_error is None:
                first_error = error                # keep the first observed failure
    if first_error is not None:
        raise first_error                          # zero commits on any failure
    staged = {}
    for depot_id, payload in payloads:
        for item, quantity in payload.items():
            if item in staged:                     # cross-depot identity, even if quantities match
                raise ValueError('item supplied by two depots: ' + item)
            staged[item] = quantity
    store.commit(staged)                           # exactly one atomic replacement
```

```text
Start: store = {'old': 9}
D1 -> {'pump': 2}, D2 raises DepotUnavailable  -> store stays {'old': 9}, commits = 0 (both completion orders)
D1 -> {'pump': 2}, D2 -> {'valve': 4}            -> one commit: {'pump': 2, 'valve': 4}
Unsafe: committing D1 as soon as it finishes leaves {'pump': 2} after D2 fails
```

**(b) 图报告调试（20 分钟，226 行包：validation / traversal / aggregation / rendering / report / fixtures / tests）**

- **Bug**：`traversal.py` 记录每个出队站点、调度邻居，**扩展之后才标记**。菱形 (diamond) H→J, H→K, J→M, K→M（每站一个 1 分钟事件）：J 与 K 都看到 M 未扩展 → M 入队两次 → 总数 **5**（应为 4）。格式化与排序是误导线索 (red herring)——第一个错误值是遍历输出里重复的 M。

```python
# graph_work_report/traversal.py (buggy shape)
from collections import deque


def reachable_sites(start, adjacency):
    queue = deque([start])
    expanded = set()
    output = []
    while queue:
        site = queue.popleft()
        output.append(site)                  # BUG: duplicates enter output
        for neighbor in adjacency[site]:
            if neighbor not in expanded:
                queue.append(neighbor)       # M is queued by both J and K
        expanded.add(site)                   # marked only after expansion
    return output
```

```python
# fixed: mark on DISCOVERY so every site is queued once
def reachable_sites(start, adjacency):
    queue = deque([start])
    discovered = {start}
    output = []
    while queue:
        site = queue.popleft()
        output.append(site)
        for neighbor in adjacency[site]:
            if neighbor not in discovered:
                discovered.add(neighbor)     # mark when first discovered
                queue.append(neighbor)
    return output
```

- 验证：H,J,K,M 各一次，总数 4；加 M→H → 终止（H 已被发现）；M 再加一个**不同的** 1 分钟事件 → 修复后总数 **5**（M: event_count 2, minutes 2）——合法数据。保留原文件与修复文件。

### Station 5 — System design（40 分钟）：双源设备对账

- **English problem statement**: "Design equipment reconciliation: 120,000 updates per ten-hour day, tenfold ingestion peak, 80 coordinators refreshing every 20 seconds, two-second ordinary-response target. Source A owns location and retirement; source B owns inspection state. A supplied mapping relates their IDs; missing mappings go to review, never name matching. At minute 20 add a 15-minute outage and a user's site-access removal; at minute 30 require deployment through the customer's approved operator with no outbound network access."

| 估算 Estimate | 计算 | 结果 |
|---|---|---|
| 更新平均/峰值 | 120,000 / 36,000；×10 | ≈3.33/s；≈33.33/s |
| 刷新平均 | 80 / 20 | 4 rps（同步刷新可能突发，单独测试） |
| 15 分钟中断积压 (backlog) | 3.33 × 900；33.33 × 900 | ≈3,000（平均）/ ≈30,000（峰值持续） |
| 2 秒目标 | — | 需约定百分位 (percentile)与测量边界 |

<svg viewBox="0 0 720 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="300" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Two-source equipment reconciliation｜双源设备对账</text>
<defs><marker id="p" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<rect x="10" y="45" width="140" height="55" rx="8" fill="#eef4ff" stroke="#3b6fd8"/><text x="80" y="68" text-anchor="middle">Source A</text><text x="80" y="86" text-anchor="middle">location, retirement</text>
<rect x="10" y="120" width="140" height="55" rx="8" fill="#eef4ff" stroke="#3b6fd8"/><text x="80" y="143" text-anchor="middle">Source B</text><text x="80" y="161" text-anchor="middle">inspection state</text>
<rect x="190" y="70" width="170" height="85" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
<text x="275" y="92" text-anchor="middle">POST /source-updates</text><text x="275" y="110" text-anchor="middle">authz + schema → 202</text><text x="275" y="128" text-anchor="middle">durable inbox</text><text x="275" y="146" text-anchor="middle">持久收件箱</text>
<rect x="400" y="50" width="180" height="130" rx="8" fill="#fff4e0" stroke="#a67c00"/>
<text x="490" y="72" text-anchor="middle" font-weight="bold">Local store 本地存储</text><text x="490" y="92" text-anchor="middle">mapping A↔B → canonical id</text><text x="490" y="110" text-anchor="middle">per-source revision HWM</text><text x="490" y="128" text-anchor="middle">tombstones (retired r8)</text><text x="490" y="146" text-anchor="middle">derived equipment state</text><text x="490" y="164" text-anchor="middle">checkpoint (same txn)</text>
<rect x="610" y="60" width="100" height="100" rx="8" fill="#f3f7ee" stroke="#5a8f29"/><text x="660" y="88" text-anchor="middle">GET</text><text x="660" y="106" text-anchor="middle">/equipment</text><text x="660" y="124" text-anchor="middle">authz +</text><text x="660" y="142" text-anchor="middle">freshness</text>
<g stroke="#555" marker-end="url(#p)"><line x1="150" y1="72" x2="188" y2="100"/><line x1="150" y1="147" x2="188" y2="125"/><line x1="360" y1="112" x2="398" y2="112"/><line x1="580" y1="110" x2="608" y2="110"/></g>
<rect x="190" y="200" width="170" height="70" rx="8" fill="#fdecea" stroke="#c0392b"/><text x="275" y="222" text-anchor="middle">Quarantine / review</text><text x="275" y="240" text-anchor="middle">schema, conflicts,</text><text x="275" y="258" text-anchor="middle">missing mapping (A-103)</text>
<rect x="400" y="200" width="310" height="70" rx="8" fill="#f3f7ee" stroke="#5a8f29"/><text x="555" y="222" text-anchor="middle">Async jobs: derive, reconcile, retry, export</text><text x="555" y="240" text-anchor="middle">offline release via customer operator</text><text x="555" y="258" text-anchor="middle">离线发布：签名制品 + 回滚包 + runbook</text>
<g stroke="#c0392b" marker-end="url(#p)"><line x1="275" y1="155" x2="275" y2="198"/></g>
</svg>

**参考设计要点 / Reference design points**

- 映射：A-101→B-701、A-102→B-702 → 规范设备 ID；A-103 进入有负责人的审查队列；**绝不启发式按名字 join**。
- **每源**身份/修订高水位 (high-water mark) + 规范 payload 哈希；**源修订号不可跨源比较**。旧修订忽略并留审计；相同修订/内容 = 重放；相同修订/不同内容 = 隔离。
- 事务性持久化：已接受源状态、修订、来源、派生设备状态 + 收件箱 (inbox)/检查点 (checkpoint)。**A r8 retired 墓碑 (tombstone) 重启后仍在；重放 A r7 (active) 不能复活**；B r3 passed 可更新检查状态但不改退役 (retirement)。压缩 (compaction)时不丢墓碑/高水位，除非有显式重放保留契约。物理删除需显式上游墓碑或对账策略；不完整扫描中的缺失不证明删除。
- 写 API：`POST /source-updates`（认证的源身份、源本地 ID、整数修订、schema 版本、自有字段）→ 先校验授权与 schema → 持久记录后返回 **202 + tracking ID**；schema 变更与畸形 (malformed) payload 进受限隔离 (quarantine)（脱敏 (redacted)诊断 + 指定审查人）；拒绝写别的源的字段；映射变更需授权、版本化 (versioned)、可审计。
- 读 API：`GET /equipment?site=...&cursor=...` 只返回当前授权的记录（位置/检查/退役、每源新鲜度、stale/unknown 状态、来源引用）；**常规读绝不同步扇出 (fan-out)到上游**；本地索引状态做授权与读取；摄取、派生、对账、重试、导出都异步幂等 (idempotent)；新鲜度或权限无法确认时**返回 unavailable/unknown，而不是空数据**。
- 对账：对照完整、版本化的源快照/检查点比较计数、修订、自有字段；差异与缺失映射进审查；不要用到达顺序合并覆盖权威退役状态。保留可重放收件箱、死信 (dead-letter)/隔离队列、备份与恢复流程；监控队列年龄、源新鲜度、冲突数、未授权请求、延迟；指定源负责人、映射审查人、服务 on-call、客户运维（真实人员要约定）。
- **分钟 20（中断 + 撤权）**：只显示带新鲜度/陈旧与来源的最后良好状态；无法支持的源字段标 unknown；与客户约定最大可容忍陈旧度；从持久检查点恢复、按每源修订、有界并发排空 (drain)、**对账后才宣布健康**；测试"接受后派生前重启"与"退役状态重放"。在服务、任务、派生记录、日志、导出中执行当前站点访问；缓存按 principal/site + 权限版本做作用域 (scope)，撤权即失效；任务在读/写/发布前复查授权；导出在创建与获取时复查；**无法确认新鲜授权时 fail closed**；已下载的离线导出无法收回——要写明。
- **分钟 30（离线运维部署）**：只有批准的客户运维部署；通过批准的本地传输路径交付**签名/校验和 (checksum)的发布制品 (release artifacts)、依赖清单、离线依赖、配置模板、迁移脚本、冒烟测试 (smoke tests)、回滚包 (rollback package)、runbook**；运行时不下载包、不发外部遥测 (telemetry)；密钥 (secrets)与端点配置在客户批准的本地存储。分阶段：本地夹具 + 备份/恢复检查 + schema 兼容检查 → **影子对账不发布 (shadow reconciliation)** → 有限站点发布（约定新鲜度/错误/授权阈值，运维记录每个关口 (gate)）。回滚应用/配置到兼容版本，保留持久源修订与墓碑，**避免会复活退役设备的破坏性 schema 回滚**；无法安全兼容时暂停摄取/发布、恢复已测试备份并对账。交接：运维演练、升级负责人、恢复演练、制品清单、撤权流程、接受未解决局限。**描述一个无法访问的前雇主平台解决不了本地实现与操作流程**。

### 面试怎么说 / How to say it in the interview — Station 5 condensed script

> "Source A owns location and retirement, B owns inspection, and a supplied mapping links their IDs — anything unmapped like A-103 goes to a review queue, never name matching. I keep a per-source revision high-water mark and payload hash, because revisions aren't comparable across sources. Ingestion is POST /source-updates: authorize the source, validate the schema, durably record, return 202. Accepted state, derived equipment state and the checkpoint commit together, so a retired tombstone at A revision 8 survives a restart and a replayed revision 7 can't resurrect it.
> Reads come from the local store only — never a synchronous fan-out to upstream — and every record shows per-source freshness and stale or unknown status. At peak that's about 33 updates and 4 refreshes a second; a 15-minute outage is roughly 3,000 to 30,000 updates to drain, which I'd drain with bounded concurrency and reconcile before declaring healthy.
> When a user loses site access, every path re-checks current permission: services, jobs, caches keyed by permission version, logs and exports at creation and download — and if we can't confirm permission, we fail closed.
> For deployment with no outbound network, I hand the customer's operator signed artifacts with offline dependencies, migrations, smoke tests, a rollback package and a runbook; we shadow-reconcile without publishing, then roll out to a limited set of sites with agreed thresholds. Rollback never includes a destructive schema change that could bring retired equipment back. All of this is a proposed design — not a measured two-second service."

### Station 6–7 — Follow-up & evidence review

| 追问卡 Follow-up card | 期望 Expected |
|---|---|
| 断开的依赖环 | 整个调用 ValueError；输入不变；无部分结果 |
| 等值延迟订单 + 多条历史 | 加 update 23（late，11-03）→ E2 最新为 late → East 2/2/0/200/1，其他不变 |
| 终页 API 失败 | 调用 None, c1, c1, c2；c2 的异常原样传播，不重试、无总数 |
| 一个 worker 成功后另一个失败 | store 仍为 {'old': 9}，0 次提交，两个 ticket 都检查，抛出 DepotUnavailable |
| 恢复后重放退役设备更新 | 重放 A r7 (active) 不能撤销 r8 (retired)；B r3 不受影响 |

- **冻结 (freeze)**整个第一次尝试（只读副本/归档 + 时间戳 + 文件清单），之后才看参考；参考运行另记时间戳。
- 七维评审：问题框定与范围；技术执行；数据与运营判断；学习与适应；验证与证据局限；协作与负责；动机与反思。每项：制品/时间戳、观察、后果、标签（Demonstrated / partial / not evidenced）。**无官方权重、通过线或录用概率**。
- 两个目标格式：**观察 → 后果 → 最小纠正练习 → 新的验证**。例："Publishing D1 before D2 failed exposed a mixed catalog → practice private staging → force a new failure-order permutation and check that the prior snapshot remains exactly unchanged."

---

## 27. 4-Week Prep Plans for Both Levels｜两个级别的四周准备计划

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/4-week-prep-plans-for-both-levels

### 要点 / Key ideas

- 从日历和模拟记录里的两个纠正目标开始；**证据改变优先级时，从别的活动挪出具名的时间块，而不是增加看不见的小时**。
- 记录每周可用时间、可用的单次时长、面试日期、工具权限、无障碍安排 (accommodations)、未决问题；每个已确认轮次保留来源与确认日期。Palantir 说面试数量与格式个性化；工程能力：可工作代码、效率分析、开放推理、技术解题、在现有系统中工作。
- 示例：周一/周三 19:00–20:00 + 周六/周日 09:00–12:00 = **8 小时 = 16 个 30 分钟块**；留 2 块应急 (contingency)，14 块分配给具名工作。四周是计划周期，不是招聘时长估计。

**纠正目标 / Corrective target** = 观察 → 后果 → 最小有用练习 → 新的验证任务。缺失观察需要诊断，不证明不会。

| 路线 Route | 目标 1 | 目标 2 |
|---|---|---|
| 新毕业生 | **关系粒度 (relational grain)**：先聚合历史再选最新行 → 用新数据（后来关闭的状态 + 时间戳平局）验证 | **契约阅读迁移**：把扫描上限当匹配数 → 先追踪检查位置与续页；用不同 API 契约验证 |
| **资深 Experienced** | **可执行基线 (executable baseline)**：计时实现停在伪代码 → 先完成最小函数再优化；用新的计时实现 + 已执行检查验证 | **完整结果检查 (complete outcome inspection)**：把完成的 future 当成功 → 私下暂存 + 取回每个结果；用另一个失败 worker 验证旧快照不变 |

- 证据状态：看完参考后复现 = 修复练习（不是迁移证据）；独立解出并检查变化的 latest-row 夹具 = 新的关系粒度证据；跑一个变化的 worker 失败用例并检查每个结果与旧快照 = 新的结果检查证据；某类别未被观察 = 需要诊断。**修复与验证分开排期——修好的方案不关闭目标**。

**六类时间块与四周账本 / Six categories, four weekly ledgers**（目标练习 / 广度练习 / 经历证据 / 计时模拟 / 评审反馈 / 应急）

| 周 Week | 分配 Ledger | 目的 Purpose |
|---|---|---|
| 1 | 4 / 4 / 2 / 2 / 2 / 2 = 16 | 诊断与修复 |
| 2 | 6 / 2 / 2 / 2 / 2 / 2 = 16 | 检查迁移 |
| 3 | 4 / 2 / 2 / 4 / 2 / 2 = 16 | 在中断或需求变更下组合技能 |
| 4 | 4 / 2 / 2 / 4 / 2 / 2 = 16 | 验证剩余目标，排练已确认的格式；看完第三周证据再定目标组合 |

- 第三方建议的日历（第一周编码与沟通、第二周设计、第三周拆解、第四周经历与学习）只是建议，**不能成为推迟关键弱项的理由**。
- 第一周具体安排：周一/周三各 1 目标块 + 1 评审块；周六 2 目标 + 2 经历证据 + 2 块诊断模拟（60 分钟选定轮次模拟）；周日编码/SQL 维护、修复、拆解、设计各 1 块 + 2 应急块不分配。后面 4 块模拟 = 120 分钟集成子集，不是重复 4 小时全模拟。
- **资深路线的经历证据产物**：一个真实决策，追踪实现 → 发布约束 → 需求变更 → 跟进，**客户影响以测量为界**。两条路线都需要可工作代码、技术清晰与适应；都不允许编造经历。
- **资深周一的一小时**：19:00–19:30 写一个可运行的有序请求处理器（拒绝库存不足、保留调用方输入、每个请求返回一个状态）；保存已执行检查、复杂度推理与未完成工作。19:30–20:00 检查第一个行为不匹配并指定新的实现检查。（每小时 = 30 分钟目标尝试 + 15 分钟比较与因果分析 + 15 分钟指定新验证。）
- 没有同伴反馈 → 记录讲解并按课程标准评审，**标记为自评 (self-review)**。

**第二周检查点规则 / Week-two checkpoint rule**

- **同一关键失败在两次新尝试中出现 → 改变方法与分配**；两次新检查成功 → 可转为维护（只支持被检查的行为）。
- 新毕业生：latest-row 两次成功、API 契约又失败两次 → 第三周从可选集成模拟砍 2 块给契约阅读 → **6 / 2 / 2 / 2 / 2 / 2**（5 块契约 + 迁移，1 块 latest-row 维护；用"大声说出契约 + 预测区分性用例 + 检查"代替重读例子）。
- **资深：代码与结果检查两次成功，但两次负责叙述仍把同事的 dashboard 说成自己的** → 2 块模拟挪到经历证据 → **4 / 2 / 4 / 2 / 2 / 2**：从项目记录重建作者归属、明确致谢 dashboard 作者、排练关于个人决策的新追问。**成功的代码无法提供负责叙述的证据**。
- 评审、广度、应急保持受保护；总数仍 16。

**可用时间减少或面试提前 / When availability falls or dates move**

- 常见失败日历：16 块全给新内容、评审事后再加、学习推到第四周 → 评审一开始就超容量、无应急、忽视重复的契约错误。
- 修复：把评审计入；把弱的已确认技能提前并说出捐出的块；先从已展示的熟悉练习或可选长模拟取时间，保留有界模拟、证据工作与评审；没有捐出者就缩减或推迟范围；已确认轮次提前 → 提前独立尝试与反馈（不要推断未提到的格式被取消）；记录推迟的可能性与能改变其优先级的 recruiter 问题。
- 审计练习：6 小时/周（12 块），11-08 面试已确认 live coding + learning；检查点后降到 5 小时（10 块）→ 一个可行修订 **4 / 0 / 1 / 2 / 2 / 1 = 10**（相关维护放进模拟、明确推迟未确认的设计）。错误说法：从工程能力指南推断"系统设计已排在 11-08"；"完成所有预订的练习块即证明就绪，计划中的检查可列为成功"；"检查点后仍按原 12 块"。资深包注意：区分"实现了重试与分阶段发布"与"未测量的客户节省时间"。

### 面试怎么说 / How to say it in the interview

- （本课为准备方法，无直接面试问答。）对 recruiter 的确认问题："Could you confirm which rounds are in my loop and their dates, whether I can use any tools or AI assistance, and how accommodations are arranged?" ｜向 recruiter 确认轮次、日期、工具与安排。

---

## 28. Conclusion｜结语

Source: https://www.educative.io/courses/palantir-forward-deployed-engineer-interview/conclusion

### 要点 / Key ideas

| 阶段 Stage | 内容 Content |
|---|---|
| 1. 角色、流程与你的故事 | Foundry、Gotham、AIP、Ontology 如何配合（AI 建议本身不验证也不执行决策）；逐行读 FDSE JD；FDSE 变体与相邻岗位；招聘流程（轮次池、时间线、**no-AI 规则**）、不同经验级别的评判差异；简历/内推/Build to Apply；Why Palantir、项目、使命与伦理 |
| 2. 技术筛选 | HackerRank 与 CodePair/Karat 的时间策略；实现与算法题；SQL；分页 (paginated) REST API 聚合；一小时内编码 + 澄清 + 行为题 |
| 3. 运营解题轮 | 拆解框架（用户、数据、约束 → 数据模型、API、算法放哪）；物种编目、城市交通、记录系统同步；快速学文档、扩展陌生系统/查询语言/多线程库；系统化调试、避开误导线索、验证修复；把模糊提示变成精确函数契约；重构后扩展 + 回归测试；带数据管道、集成、可靠性、访问控制的运营系统设计 |
| 4. 行为证据与排练 | 嵌入式行为题；pushback/failure/ownership/ambiguity 题库；HM 终面重测什么；团队匹配、offer 与谈判；新毕业生与资深完整模拟；围绕已展示弱项的四周计划 |

- 下一步：向 recruiter 确认你的流程与轮次池 → 开始四周计划 → 计时重复练习题 → 用模拟找最弱轮次 → 保持项目与经历故事最新且真实 → 面试前查看最新官方材料（格式与产品会变）。

---

# Section II｜第二部分：Forward Deployed Engineer for AI Systems — Palantir module（只记新增/不同之处）

## II-1. Decomposition: What It Tests and a Repeatable Framework｜拆解：考什么与可复用框架

Source: https://www.educative.io/courses/forward-deployed-engineer/decomposition-what-it-tests-and-a-repeatable-framework

> 与 Section I 第 1–3 课重叠（五维证据、clarify/scope/model/design/iterate、有后果的澄清问题）。下面只记**新内容**。

### 要点 / Key ideas（新增）

- 公开报告描述拆解轮为**开放式对话，通常很少或不写代码**（Section I 第 1 课则提醒有的 track 把拆解与 coding 合并——两者都要准备）。四个考察点：问会改变工作的问题；区分已知与假设；**注意到数据看起来完整但支撑不了决策**；以一个可执行的有范围陈述收尾。
- **五遍框架 (five-pass framework)**，每遍产出一两句能说出口的话：

| 遍 Pass | 产出 Output |
|---|---|
| 1. 用户与决策 User & decision | 谁在什么时间前决定什么 |
| 2. 目标与约束 Goal & constraints | 想要的运营改变 + 约束 |
| 3. 证据发现 Evidence discovery | 有哪些记录、含义、局限 |
| 4. 关键未知 Consequential unknowns | 答案可能改变工作的、排序后的短假设列表 |
| 5. 有界重述 Bounded restatement | 带范围与剩余不确定性的问题陈述 |

- **虚线回环**：某个未知的答案推翻早先假设时，回到第一遍修订用户与决策（例：记录晚一天到 → 实时监控目标变成计划目标）。"一个修订后的决策句是真进展；20 个什么都不改变的问题不是"。
- 面试官不回答时，提出**可逆假设 (reversible assumption)**："I'll assume the immediate user allocates fieldwork, so coverage planning comes first. I'd revisit that if identification turns out to be the real decision."

**物种编目的五遍示例（不同于 Section I 第 5 课的数据）**

- 用户与决策："The field coordinator must choose tomorrow's two survey zones before 16:00, within route permissions and team capacity." 角色：协调员（授权分派）、野外队（在批准路线采集）、专家审阅人（确认不确定识别）、数据所有者（控制日志使用，待确认）。推荐一个区域≠获准进入；分派队伍≠确认物种。
- 目标与约束：减少可用观测目录中的空白；只走批准路线、不确定标签需专家审阅、敏感位置受限访问；认证所有物种超出范围。
- 证据发现：每次目击一个观测 ID + 重复上传规则；**努力量 (effort)** = 每区每次调查的调查小时（不是每次目击）；标签是暂定还是已审阅；日志次日 14:00 上传，审阅需 3 天。**事件时间 vs 可用时间 (availability time)**：16:00 时能用的是昨天的日志，多数标签仍暂定。

| 区 Zone | 观测 | 调查小时 | 每小时率 |
|---|---:|---:|---:|
| A | 18 | 6 | 3 |
| B | 8 | 2 | 4 |
| C | 0 | 0 | 未定义 |
| D | 4 | 4 | 1 |

- **零不等于不存在 (zero isn't absence)**：C 没有调查努力 → "C 没有物种"无依据，只能说"C 缺调查证据"；**率不衡量生物多样性**（方法与路线可能不同）。诱人答案"用实时数据按生物多样性排名、跳过 C、完成目录"每一部分都越界。
- 关键未知：三个问题（C 可达吗？某次目击最终标签？用什么存储引擎？）中先问 **C 是否可达**——只有它改变可行分派。确认 C 可达、每队 4 小时。

| 答案 Answer | 打破的假设 Broken assumption | 修订边界 Revised boundary |
|---|---|---|
| C 努力为 0 | 零目击 = 无物种 | C 是覆盖缺口 |
| 日志次日到 | 16:00 能看到今天的数据 | 按昨天的上传规划 |
| 审阅要 3 天 | 所有标签已确认 | 暂定与已审阅标签分开 |
| C 可达 | 有缺口就可调查 | C 是可行的调查 |

- 有界重述："Help the field coordinator plan two four-hour surveys before 16:00 using available, permitted records, prioritizing coverage gaps and keeping provisional and reviewed labels separate." 代理指标 (proxy)：有记录调查努力的区域数；基线 (baseline) 3/4（75%）；调查 C 可达 100%，但**只有回传的努力记录能证明**；全覆盖改善代理指标，不证明所有物种都已编目。**一旦答案不再能改变决策就停止提问**。
- 同法用于"改善城市交通"：区分分钟级操作信号的操作员 vs 选下个月研究走廊的规划者；若传感器计数晚一天、无人确认改信号权限 → 框定为规划："Help the transport planner choose a corridor for next month's study, using permitted historical data and noting the coverage gaps."

**报告过的拆解题 / Reported decomposition prompts**

| 题 Prompt | 思路 Approach |
|---|---|
| Catalog species in an unfamiliar environment | 先分用户：鉴定标本的研究员 vs 规划调查的协调员；问访问、审阅能力、调查努力 |
| Improve traffic in a city | 区分实时控制与规划；问数据新鲜度、权限、谁能改信号；安全是约束 |
| **Help a hospital reduce emergency-room wait times**（新题） | 问谁决定（这一小时的值班护士长 charge nurse vs 下个月的管理者）、有哪些时间戳；隐私 (privacy)与临床权限约束方案 |

### 面试怎么说 / How to say it in the interview

- **Opening fork**: "If the goal is tomorrow's field allocation, I need survey effort and coverage. If it's species identification, I need evidence and expert confirmation. Which decision should I support?" ｜开场把两种解读摆出来让面试官选。
- **ER wait times (new prompt) — full walkthrough script**:
  > "First, whose decision is this — a charge nurse deciding who's seen next this hour, or an administrator planning staffing next month? Those need very different data. … Say it's the administrator planning next month's staffing. What timestamps exist — arrival, triage, bed assignment, provider seen, discharge? Are they recorded consistently, and how quickly are they available? Privacy and clinical authority bind everything: I won't touch triage decisions, and outputs should be aggregates the administrator is authorized to see.
  > Thin slice: a weekly view of median and 90th-percentile arrival-to-provider time by hour of day and day of week, with coverage — how many visits had complete timestamps — shown next to every number, because missing timestamps aren't zero waits.
  > Model: one Visit row per ED visit keyed by visit_id, with nullable stage timestamps and a source and quality flag; staffing shifts as a separate table keyed by shift_id. Read contract: GET wait-time summaries by week and hour for an authorized administrator, returning aggregates only, never patient identifiers. Baseline: the last eight weeks. Success measure: the administrator uses it to change one staffing block, and we compare the next four weeks' wait percentiles for that block — knowing seasonality and volume can confound it.
  > The biggest unknown I'd resolve first is whether provider-seen times are reliably recorded, because without them the whole wait metric falls apart."
  ｜先分清决策者与时间尺度 → 时间戳与隐私 → 带覆盖率的周视图 → 模型/读契约/基线/指标 → 先解决最关键的未知。

---

## II-2. From Ideation to Execution: Users, Data Models, and APIs｜从构思到执行：用户、数据模型与 API

Source: https://www.educative.io/courses/forward-deployed-engineer/from-ideation-to-execution-users-data-models-and-apis

> 与 Section I 第 4 课（执行阶段：行粒度 (row grain)、契约、幂等 (idempotency)、算法放哪）重叠；这里是同一物种场景的**简化执行版**，新增点如下。

### 要点 / Key ideas（新增）

- 先把协调员的一天写成步骤再选技术：看每区的记录努力、观测、访问状态 → 选两个可行区域并分派 → 调查后看回传努力与观测 → 专家确认或修正暂定标签。**不服务任何步骤的组件暂不做**。预览不能"预留世界"——提交时命令必须**重新校验 (revalidate)**记录与权限。

| 实体 Entity | 键 Key | 字段 Fields | 存在原因 Why |
|---|---|---|---|
| Zone | zone_id | name, access status | 分派与覆盖按区 |
| Assignment | assignment_id | zone_id, team, date, planned hours | 记录协调员决策 |
| Survey effort | effort_id | assignment_id, zone_id, actual hours, returned_at | **证明调查发生了** |
| Observation | observation_id | zone_id, effort_id, event time, upload time, provisional label | 一次目击，关联产生它的努力 |
| Review | review_id | observation_id, reviewer, reviewed label, status | 已确认标签与暂定标签分开 |

- 三个关键选择：**努力量单独成实体**（覆盖从努力计算，"零目击"与"从未调查"可区分）；**分派与努力分开**（计划的≠完成的，只有回传努力计入覆盖）；**审阅不覆盖观测**（暂定标签保留，审阅加一个确认标签在旁边）。

| 步骤 Step | 操作 Operation | 校验 Validates | 改变 Changes |
|---|---|---|---|
| 看覆盖 | `GET /zones/coverage?date=` | 用户可查看 | 无（只读） |
| 分派 | `POST /assignments` | 协调员角色、区域访问已批准、队伍容量 | 创建分派 |
| 回传调查 | `POST /effort` | 分派存在、hours ≥ 0 | 记录实际努力 |
| 上传目击 | `POST /observations` | 努力存在；重复 observation_id 忽略 | 添加观测 |
| 审阅标签 | `POST /reviews` | 审阅人角色 | 添加审阅标签 |

- 两个习惯：**在变更发生处校验权限与可行性**（不管 dashboard 显示什么，`POST /assignments` 拒绝未批准访问的区域）；**重试写安全**（相同 observation_id 只存一次）。
- 选区规则（4 区 2 队）：只留批准访问的区 → 零努力的排前 → 再按最低努力排序 → 作为推荐展示，协调员最终决定。

| 情境 Situation | 方法 Approach |
|---|---|
| 4 区、2 队、一个截止 | 简单排序规则，协调员决定 |
| 200 区、10 队、区间行程时间 | 分配问题 (assignment problem)：先贪心 (greedy)，贪心明显更差再考虑优化器 (optimizer) |
| 数千张照片需标注 | 分类器 (classifier)建议标签并排审阅优先级，专家仍确认 |
| 标签需法律认证 | 算法替代不了专家，软件只路由工作 |

- 经验法则：**约束或规模让简单规则失败时才用算法，并说出什么会让你升级**。
- 验证决策确实发生：Assigned（C 明天有分派）→ Completed（C 回传努力 > 0）→ Improved（覆盖 3/4 → 4/4，从努力记录计算）——每个检查读不同实体，这就是模型分开的原因。

**常见追问 / Common follow-ups**

| 追问 | 英文回答 Answer |
|---|---|
| How would this scale to hundreds of zones? | "The data model and APIs stay the same. Zone choice may become an assignment problem with travel times — start greedy, and add an optimizer only if greedy plans are measurably worse." |
| What if an upload arrives twice? | "Observations are keyed by observation_id, so the second copy is ignored. A different payload under the same ID is flagged for a person, not silently merged." |
| What if the expert disagrees with the provisional label? | "The review is stored beside the observation. Reports can show reviewed, provisional or both — nothing is overwritten." |
| Where would you use machine learning? | "To suggest labels and prioritize which photos experts review first, if volume makes manual review the bottleneck — never as the final confirmation where experts are required." |
| How do you know it worked? | "Coverage computed from returned effort records goes from 3 of 4 zones to 4 of 4 — that proves the survey happened, not that every species is cataloged." |

<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="200" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Separate entities make each check readable｜实体分开，检查才可读</text>
<defs><marker id="q" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<g fill="#eef4ff" stroke="#3b6fd8"><rect x="10" y="60" width="110" height="50" rx="8"/><rect x="150" y="60" width="120" height="50" rx="8"/><rect x="300" y="60" width="120" height="50" rx="8"/><rect x="450" y="60" width="120" height="50" rx="8"/><rect x="600" y="60" width="110" height="50" rx="8"/></g>
<g text-anchor="middle"><text x="65" y="82">Zone</text><text x="65" y="100">区域</text><text x="210" y="82">Assignment</text><text x="210" y="100">计划 planned</text><text x="360" y="82">Survey effort</text><text x="360" y="100">完成 completed</text><text x="510" y="82">Observation</text><text x="510" y="100">provisional</text><text x="655" y="82">Review</text><text x="655" y="100">confirmed</text></g>
<g stroke="#555" marker-end="url(#q)"><line x1="120" y1="85" x2="148" y2="85"/><line x1="270" y1="85" x2="298" y2="85"/><line x1="420" y1="85" x2="448" y2="85"/><line x1="570" y1="85" x2="598" y2="85"/></g>
<text x="210" y="140" text-anchor="middle" font-size="12">"Assigned?"</text><text x="360" y="140" text-anchor="middle" font-size="12">"Completed? coverage"</text><text x="655" y="140" text-anchor="middle" font-size="12">"Confirmed?"</text>
<text x="360" y="180" text-anchor="middle">Coverage comes from effort, not observation counts｜覆盖来自努力量而非观测数</text>
</svg>

### 面试怎么说 / How to say it in the interview

- "I'd model survey effort separately from observations, because a zone with zero sightings could be unsurveyed or surveyed-with-nothing-found — only effort records tell them apart." ｜努力量单独建模。
- "I'd start with the ranking rule. If we grow to hundreds of zones with travel costs, I'd treat it as an assignment problem." ｜说出升级到算法的触发条件。

---

## II-3. The Learning Round: Reading Docs and Extending Systems｜学习轮：读文档与扩展系统

Source: https://www.educative.io/courses/forward-deployed-engineer/the-learning-round-reading-docs-and-extending-systems

> 与 Section I 第 8–11 课（pick 扫描上限、文档路由、futures、全有或全无 (all-or-nothing)发布、RowPath 查询）重叠。新增点如下。

### 要点 / Key ideas（新增）

- **契约边界**："Successful results are returned in input order; execution and completion order are unspecified." → 只能预测**返回列表的顺序**，不能预测开始顺序、外部调用顺序或完成顺序。
- **学习循环（六步）**：复述要求的改变与必须不变的行为 → 追踪一个现有调用穿过入口 → 只读这条路径上的签名、示例、并发说明、失败规则 → 写下改动依赖的契约 → 用小实验测最危险的未决解释 → 做最小扩展并验证新旧行为。
- 三列工作笔记：

| 已文档化契约 Documented | 未决问题 Unresolved | 最小探测 Probe |
|---|---|---|
| 结果按输入顺序返回 | 服务能并发读吗？ | 问，或找服务契约 |
| 等所有任务完成才返回 | 失败批次会回滚 (roll back)吗？ | 文档说不回滚 → 假设没有 |
| 执行顺序未指定 | 本改动无 | 测试中强制一个不寻常的完成顺序 |

- **一次成功的并发运行不能证明线程安全 (thread safety)**。不要一开始读完所有页面——读够下一步安全行动即可，有具体问题再回文档。
- 证据：公开报告有"给 schema + 文档、面试中实现函数"、现场学 SQL 或陌生系统；**没找到有来源的多线程库任务报告**（练习示例是虚构的）。Recruiter 的说明决定真实格式、语言、允许资源。
- 模糊规则探测（新查询语言）："KEEP value > 5 保留谓词 (predicate)为真的行；与缺失值比较得 unknown，unknown 行被丢弃。" 求每设备最新读数且最新值 > 5：先 latest 再过滤 → C（最新值缺失）被排除；先过滤再 latest → 旧读数 8 错误存活。好的探测：**最新值缺失、较旧值 > 5 的设备**；只有一条干净读数的设备区分不了。**熟悉的 PostgreSQL 行为不是新语言的证据**。

**扩展批处理库 / Extending the batch library**

- **English problem statement**: "The existing `enrich` returns enriched records in input order. Add totals by region without changing that list. `parallel_map(fn, items, workers=3)` runs fn once per input in worker threads, no retries; execution/completion order unspecified; results in input order; waits for every task or raises BatchError if any worker fails; no rollback. A failed batch must not return a partial summary."
- **诱人扩展**：每个 worker 往共享 totals 字典加金额 → read-add-write 三步，合法交错 (interleaving)丢更新 (lost update)：J1 读 north=0、J3 读 north=0、J1 写 7、J3 写 11 → 结果 11 而不是 18。**Python GIL 不是对这个序列的文档化保证**；只锁最后赋值仍保留陈旧读——**锁必须覆盖整个 read-add-write**。
- **更简单的扩展**：worker 返回不可变记录，调用方在 `parallel_map` 返回后构建 totals——**库文档化的"等待所有任务"边界就是同步 (synchronization)**，没有共享可变状态 (shared mutable state)可竞争。

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Enriched:
    job_id: str
    region: str
    amount: int


def enrich(jobs, read_amount):
    # Unchanged original: workers return immutable records.
    def worker(job):
        return Enriched(job.job_id, job.region, read_amount(job.job_id))
    return parallel_map(worker, jobs, workers=3)


def enrich_with_totals(jobs, read_amount):
    records = enrich(jobs, read_amount)          # raises BatchError -> no partial summary
    totals = {}                                  # single owner: the caller's thread
    for record in records:
        totals[record.region] = totals.get(record.region, 0) + record.amount
    return records, totals
```

```text
JOBS: J1 north 7, J2 south 5, J3 north 11, J4 south 3 (test forces J3 to finish before J1)
records order: J1, J2, J3, J4   totals: {'north': 18, 'south': 8}
empty batch -> ([], {})
J2 raises -> BatchError, no summary returned
J1 submitted twice -> north = 14 (separate inputs contribute separately)
```

- 该改动**不声称**：失败后已完成的只读调用保持完成（此处可接受）；写服务需要自己的失败与恢复契约；不要声称文档没给的重试、去重 (deduplication)、回滚。
- 练习 `summarize` → `{region: (count, total)}`：K1/east 4、K2/east 6、K3/west 2 → east (2, 10)、west (1, 2)；K1 提交两次 → east (2, 8)。

```python
def summarize(jobs):
    records = enrich(jobs)                       # (job_id, region, amount) in input order
    summary = {}
    for _, region, amount in records:            # caller's thread; every record counts once
        count, total = summary.get(region, (0, 0))
        summary[region] = (count + 1, total + amount)
    return summary
```

- **60 秒讲解**：一个文档化规则（输入顺序返回 + 等待所有任务）；一个探测解决的不确定性（完成顺序是强制的，不是假设的）；测试不证明的东西（超出澄清范围的服务线程安全、写服务的行为）；单一所有者的位置（totals 在调用方线程，库返回 = "所有 worker 完成"边界）。

**报告过的学习轮问题 / Reported learning-round questions**

| 问题 Question | 英文回答 Answer |
|---|---|
| You're given a schema and documentation. Implement a function. | "I find the function's inputs and outputs in the docs first and read only the relationships it needs. I settle ties and missing values from the docs before writing code, and test them with a small example." |
| The documentation doesn't say what happens in this case. What do you do? | "I say what the docs do guarantee, name the open question, and run a small probe or ask. If I must proceed, I state the assumption aloud and keep the code easy to change." |
| Why didn't you just add a lock? | "A lock only helps if it covers the whole read-add-write and the holder can't block on slow calls. Returning immutable results and aggregating on the caller thread removes the shared state entirely." |
| How do you know your change didn't break existing behavior? | "I keep the original function untouched, compare its output before and after, and add one check per documented guarantee, such as input order and failure behavior." |
| What would you do if the library had no concurrency notes? | "Treat thread safety as unknown: keep shared mutable state out of workers, and ask or read the source before relying on anything stronger." |

### 面试怎么说 / How to say it in the interview

- "The doc guarantees result order, not completion order — so I'll aggregate after parallel_map returns, on the caller's thread. The library's wait-for-all boundary is my synchronization; there's no shared dictionary for workers to race on." ｜用库的完成边界代替锁。

---

## II-4. The Re-Engineering Round: Debugging and Verifying Fixes｜重构调试轮：调试与验证修复

Source: https://www.educative.io/courses/forward-deployed-engineer/the-re-engineering-round-debugging-and-verifying-fixes

> 与 Section I 第 12–15 课（调试六步、可证伪假设、误导线索、tally 与图遍历修复）重叠。新增两个 bug：**跨请求保留的去重 (deduplication)状态**与**路径枚举的 visited 生命周期**。

### 要点 / Key ideas（新增）

- 第一个探测 (probe)：**同一请求在全新服务实例上是否成功？**——把请求历史变成可测变量。新实例成功 ≠ 复用时正常：说明失败输入本身没问题，问题是**跨调用存活的状态**。
- 多出的一步："列出竞争解释 (list competing explanations)"，再跑能区分它们的探测。证据：Palantir 指南（经汇总）把"在现有系统中工作"列为能力；有个人报告描述"读代码、讨论局限、写修复"的短阶段；报告的代码库大小差异很大，不能预测你的面试。

### Bug A: request-scoped dedup state stored on the instance｜请求级去重状态存在实例上

- **English problem statement**: "Each distinct event ID contributes once within a request; repeated deliveries of one ID share a category; separate requests are independent. Request 1 returns red=2, blue=1 correctly; request 2 on the same service returns only blue=1 instead of red=1, blue=1."

```python
import json


class TallyService:
    def __init__(self):
        self.seen = set()                  # BUG: outlives a single request

    def tally(self, events):
        counts = {}                        # request-scoped, but seen is not
        for event_id, category in events:
            if event_id in self.seen:
                continue
            self.seen.add(event_id)
            counts[category] = counts.get(category, 0) + 1
        return counts


def handle_request(events, service):
    counts = service.tally(events)
    return json.dumps({"counts": dict(sorted(counts.items()))}, separators=(",", ":"))
```

```text
REQ1 = [("E1","red"), ("E2","blue"), ("E1","red"), ("E3","red")] -> {"blue":1,"red":2}  (correct)
REQ2 = [("E1","red"), ("E4","blue")] on the SAME service           -> {"blue":1}         (expected {"blue":1,"red":1})
REQ2 on a FRESH service                                             -> {"blue":1,"red":1}
```

| 假设 Hypothesis | 若为真会看到 If true | 探测 Probe |
|---|---|---|
| 格式化器丢 red | 原始计数有 red，输出没有 | 比较原始计数与格式化输出 |
| 解析器丢 E1 | tally 之前 E1 就不在 | 打印解析后的事件 |
| 去重被禁用 | 请求 1 返回 red=3 | 单独检查请求 1 |
| **排除状态被保留** | 请求 2 单独成功，在请求 1 之后失败 | 在新服务上跑请求 2 |

- 每个探测用**全新、相同初始化**的实例（同一实例调两次会改变你正在调查的状态）。只有最后一个假设预测"新的成功、复用的失败"。格式化器是误导线索（只排序标签，原始 tally 已缺 red）。
- 追踪请求 2（复用）：E1/red 时 seen = {E1,E2,E3} → **跳过（第一个错误排除）**；E4/blue 接受 → {blue: 1}。**不变量 (invariant)**：每处理一个前缀后，seen 恰好包含本请求已接受的 ID；契约要求每个请求开始时 seen 为空。
- 诱人修复：删除重复检查（请求 1 变 red=3）；给 red 加 1（修例子不修原因）；在 tally 开头重置 `self.seen`（单线程可用，但请求数据仍存为共享实例状态，**重叠调用会互相干扰**）。

```python
class TallyService:
    def tally(self, events):
        seen = set()                       # FIX: same lifetime as counts (one request)
        counts = {}
        for event_id, category in events:
            if event_id in seen:           # duplicate within a request still counts once
                continue
            seen.add(event_id)
            counts[category] = counts.get(category, 0) + 1
        return counts
```

- 按 ID 去重而不是 payload：E7/red 和 E8/red 是两个事件，都计数。

### Bug B: traversal-wide visited set used for path enumeration｜路径枚举误用全局 visited

| 问题 Question | 排除状态 Exclusion state | 示例结果 |
|---|---|---|
| 哪些顶点可达？ | **整个遍历一个 visited 集合** | {S, A, B, T} |
| 最短距离（等权边）？ | 每顶点首次发现距离，BFS | T 距离 2 |
| 所有简单路径（无重复顶点）？ | **只记当前路径上的顶点** | S–A–T 与 S–B–A–T |

- 对所有简单路径，全局 visited 是 bug：探索 S–A–T 后 A 仍被标记，后来的 S–B–A 发现 A 被排除 → 丢失合法路径。修复 = **回溯 (backtracking)**：进入时加，离开时移除（包括到达目标后）。环 A→S 仍被阻止（S 在当前路径上）。反过来：路径枚举可能产生指数级 (exponential)结果，不是 O(V+E) 的可达性任务。

```python
GRAPH = {"P": ["Q", "R"], "Q": ["U"], "R": ["Q"], "U": ["P", "V"], "V": [], "Z": []}


def simple_paths_buggy(graph, source, target):
    paths = []
    path = []
    visited = set()                        # BUG: never cleared when DFS backs out

    def visit(node):
        visited.add(node)
        path.append(node)
        if node == target:
            paths.append(path.copy())
        else:
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visit(neighbor)
        path.pop()                         # path is undone, visited is not

    visit(source)
    return paths


def simple_paths(graph, source, target):
    paths = []
    path = []
    on_path = set()                        # FIX: only vertices on the current path

    def visit(node):
        path.append(node)
        on_path.add(node)
        if node == target:
            paths.append(path.copy())      # snapshot; later backtracking cannot mutate it
        else:
            for neighbor in graph.get(node, []):
                if neighbor not in on_path:    # blocks cycle U->P, allows R->Q later
                    visit(neighbor)
        path.pop()
        on_path.remove(node)               # undo on EVERY exit, including after target

    visit(source)
    return paths
```

```text
simple_paths_buggy(GRAPH, 'P', 'V') -> [['P','Q','U','V']]                       (lost P,R,Q,U,V)
simple_paths(GRAPH, 'P', 'V')       -> [['P','Q','U','V'], ['P','R','Q','U','V']]
simple_paths_buggy(GRAPH, 'P', 'Q') -> [['P','Q']]
simple_paths(GRAPH, 'P', 'Q')       -> [['P','Q'], ['P','R','Q']]
simple_paths(GRAPH, 'V', 'V')       -> [['V']]                                     (zero-edge path)
```

- 被错误排除的顶点是 **Q**（分支 P→R→Q 上），因为第一个分支把它留在了 visited 里。

**报告过的重构调试问题 / Reported re-engineering questions**

| 问题 Question | 英文回答 Answer |
|---|---|
| Here is a codebase. Find a limitation against this requirement. | "I find the entry point and read only the path the requirement touches. I state the requirement as a test, reproduce the failure, then say what I expect to see in the code before I open it." |
| Your first guess was wrong. What now? | "I say which probe ruled it out, update the hypothesis list, and run the next probe that separates the remaining ones. Silent switching looks like guessing." |
| Why not just rewrite it? | "A rewrite throws away behavior that currently works and makes it hard to prove what changed. A focused repair keeps the diff small, so the verification is small too." |
| How do you know your fix didn't break something? | "I keep checks for behavior that must stay the same — duplicates within a request, the output format — and run them with the failing case." |
| How would you debug this in a real service you can't run locally? | "Reversible, isolated probes: logging at the suspected boundary, a copy of the service with outbound effects stubbed, and no edits until the cause is confirmed." |

### 面试怎么说 / How to say it in the interview

- "Before reading the code, I'd run request two on a fresh instance. If it passes there and fails after request one, the bug is state that outlives a request — and here `seen` lives on the instance while `counts` lives in the call." ｜先用新实例区分历史依赖与输入依赖。
- "For reachability one visited set is right; for all simple paths the exclusion has to be path-local, added on entry and removed on exit, or later branches lose valid paths." ｜按问题选 visited 的生命周期。

---

## II-5. The Coding Round: User Needs and Changing Requirements｜编码轮：用户需求与需求变更

Source: https://www.educative.io/courses/forward-deployed-engineer/the-coding-round-user-needs-and-changing-requirements

> 与 Section I 第 16–17 课（用户视角契约、先排序后切片、implement-refactor-extend）思路相同；这里是**全新的题目：兴趣匹配 + 三次需求变更 + 倒排索引 (inverted index)**。

### 要点 / Key ideas

- 二手汇编提到一个 FDSE 题："连接相似兴趣的人的 App"（只有这个前提来自报告，记录与追问是练习）。交付物是**内存匹配函数**，UI 或社交网络架构不回答编码请求。
- 应对需求变更的方法：说出对用户有用的结果 → 只解决会改变实现的不确定性 → 构建并验证可工作的基线 → 每次追问：说出改变了什么、保留其余承诺、选最小的可行适配。**为可能永远不来的追问预先建缓存 (cache)和抽象 (abstraction)，通常会推迟第一个有用结果**。

**基线契约 / Baseline contract**

| 方面 | 规则 |
|---|---|
| 身份 Identity | 每个 profile 唯一字符串 ID；名字不标识人 |
| 归一化 Normalization | `strip()` 再 `casefold()`，丢空白标签，每个标签只算一次 |
| 重复 Duplicates | 构造时重复 ID → ValueError（不让输入顺序决定哪个版本存活；后来加 upsert 也保留此规则） |
| 输出 Output | `matches(user_id)` 返回共享至少一个兴趣的其他 ID，升序，排除请求者 |
| 边界 Boundaries | 无兴趣的已知 profile → `[]`；未知 ID → KeyError |
| 不变 Mutation | 不改调用方输入 |

**Input/Output example**

```text
A: [' Art ', 'HIKING', 'art']   -> {art, hiking}
B: ['chess', 'hiking']
C: ['art']
D: ['chess']
matches('A') -> ['B', 'C']
Change 1: upsert('B', ['chess'])            -> matches('A') == ['C']
Change 2 (ranked): C := ['art', 'hiking']   -> matches('A') == ['C', 'B']   (C scores 2, B scores 1)
Duplicate rows ('A', ['art']), ('A', ['hiking']) at construction -> ValueError
```

**Baseline + changes 1–2**

```python
def normalize(labels):
    return {tag for label in labels if (tag := label.strip().casefold())}


class RankedScan:
    def __init__(self, rows):
        self.profiles = {}
        for user_id, labels in rows:
            if user_id in self.profiles:
                raise ValueError(f"duplicate user ID: {user_id}")
            self.profiles[user_id] = normalize(labels)

    def upsert(self, user_id, labels):
        # Change 1: create or FULLY replace; never append a second row or merge old interests.
        self.profiles[user_id] = normalize(labels)

    def matches(self, user_id):
        interests = self.profiles[user_id]                 # unknown ID -> KeyError
        scores = {other: len(interests & tags)             # Change 2: distinct shared interests
                  for other, tags in self.profiles.items() if other != user_id}
        return sorted((other for other, score in scores.items() if score > 0),
                      key=lambda other: (-scores[other], other))
```

- 变更 1 错误版本：追加第二个 B 行（破坏"每 ID 一个当前 profile"）；把 {chess} 合并进旧集合（保留 hiking，A 仍看到 B）。
- 变更 2：**只退役一个旧检查**（"结果按 ID 升序"，且只针对排序版本）；身份、归一化、排除自己、未知 ID 行为、输入不变都保留。陷阱：数原始标签（A 的输入有两个 art，归一化后只算一次）。

**变更 3：更快的重复搜索 → 倒排索引 (inverted index)**

- 优化前先问：多少 profile、每人多少兴趣、查询与更新频率、响应时间要求。**很多重复查询 + 很少变更的 profile** → 倒排索引（兴趣 → 持有它的 ID）；**小或频繁更新的集合 → 保留扫描**。
- 复杂度 (complexity)：扫描 ≈ O(N + M log M) + 集合交集 (set intersection)工作；索引查询 ≈ O(U + P + C log C)（U 查询兴趣数、P 访问的 posting 数、C 不同候选数）。**某兴趣几乎人人都有时 P → N，索引不比扫描快；不要声称常数时间**。
- **索引不变量**：对每个 ID v 与兴趣 t，`v ∈ by_interest[t]` 当且仅当 `t ∈ profiles[v]`。

| Posting | 更新前 | 正确更新后 | 只加不删更新后 |
|---|---|---|---|
| art | {A, C} | {A, C} | {A, C} |
| hiking | {A, B} | {A} | {A, B} ← **陈旧** |
| chess | {B, D} | {B, D} | {B, D} |

- 陈旧 hiking 条目 → 索引查询 A 错误返回 `['B','C']`，扫描正确返回 `['C']`。只在这个结果里过滤掉 B 是掩盖症状。
- **正确更新**：先归一化 → 删除 old − new → 添加 new − old → 删除空 posting 列表 → 存新 profile。**重复同一更新不改变任何东西（幂等 (idempotent)）**。

```python
from collections import Counter


class IndexedMatches(RankedScan):
    def __init__(self, rows):
        super().__init__(rows)
        self.by_interest = {}
        for user_id, interests in self.profiles.items():
            for tag in interests:
                self.by_interest.setdefault(tag, set()).add(user_id)

    def upsert(self, user_id, labels):
        new = normalize(labels)                       # normalize before changing anything
        old = self.profiles.get(user_id, set())       # a new ID has no old interests
        for tag in old - new:
            postings = self.by_interest[tag]
            postings.discard(user_id)
            if not postings:
                del self.by_interest[tag]             # drop empty posting lists
        for tag in new - old:
            self.by_interest.setdefault(tag, set()).add(user_id)
        self.profiles[user_id] = new                  # store the replacement profile

    def matches(self, user_id):
        scores = Counter()
        for tag in self.profiles[user_id]:
            for candidate in self.by_interest[tag]:
                if candidate != user_id:
                    scores[candidate] += 1
        return sorted(scores, key=lambda other: (-scores[other], other))

    def is_consistent(self):
        expected = {}
        for user_id, interests in self.profiles.items():
            for tag in interests:
                expected.setdefault(tag, set()).add(user_id)
        return self.by_interest == expected
```

```text
Rows: Q [maps, cycling], R [maps, maps], S [cycling, maps], T [music]
matches('Q') = ['S', 'R']
upsert S [cycling]  -> matches('Q') = ['R', 'S'], consistent
upsert R []         -> ['S']
upsert T ['Maps ']  -> ['S', 'T']
upsert T ['Maps ']  -> ['S', 'T']   (repeat is harmless)
```

- 这些检查覆盖列出的用例，不证明所有序列正确或真实延迟；代码是单线程的，假设调用方用方法而不是直接改字典。

<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="200" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Scan vs inverted index｜扫描 vs 倒排索引</text>
<defs><marker id="r" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<rect x="10" y="50" width="330" height="120" rx="8" fill="#eef4ff" stroke="#3b6fd8"/>
<text x="175" y="74" text-anchor="middle" font-weight="bold">Scan 扫描</text>
<text x="175" y="98" text-anchor="middle">visit every profile, intersect sets</text>
<text x="175" y="120" text-anchor="middle">O(N + M log M); no second copy</text>
<text x="175" y="142" text-anchor="middle">best for small / frequently updated</text>
<rect x="380" y="50" width="330" height="120" rx="8" fill="#f3f7ee" stroke="#5a8f29"/>
<text x="545" y="74" text-anchor="middle" font-weight="bold">Inverted index 倒排索引</text>
<text x="545" y="98" text-anchor="middle">interest → {ids}; visit own postings</text>
<text x="545" y="120" text-anchor="middle">O(U + P + C log C); P→N if tag is common</text>
<text x="545" y="142" text-anchor="middle">invariant: remove old−new, add new−old</text>
<text x="360" y="190" text-anchor="middle">Verify the index against a rebuild + the scan oracle after every update</text>
</svg>

**常见追问 / Common follow-ups**

| 追问 | 英文回答 |
|---|---|
| Why didn't you build the index from the start? | "The baseline answered the user's need with less state to keep correct. An index pays off only with many repeated reads and relatively few updates; I'd ask about scale and query frequency before adding one." |
| Is the indexed search constant time? | "No. It visits every posting for the requester's interests. If an interest is very common, that's close to a full scan." |
| What changed when ranking was added, and what didn't? | "The output order changed, so the ascending-ID check was retired for the ranked version. Identity, normalization, self-exclusion and error behavior stayed, and their checks still run." |
| How do you know the index is correct after updates? | "Compare it with an index rebuilt from the profiles after every update, and compare query results against the simple scan." |
| What if two people update at the same time? | "This code is single-threaded. For concurrent writers I'd make the profile replacement and its posting changes one critical section — a lock around upsert, or a single writer — so readers never see the profile and index disagree." |

### 面试怎么说 / How to say it in the interview

- "Ranking changes only the output order, so I'm retiring exactly one check — ascending IDs — and keeping identity, normalization and self-exclusion tests running." ｜需求变更时说清楚退役哪个检查、保留哪些。
- "The index is a second copy of the facts, so upsert has to remove old-minus-new and add new-minus-old; an add-only update leaves B in hiking and A wrongly matches B." ｜索引是事实的第二份拷贝，必须维护不变量。

---

## II-6. FDE System Design: Pipelines, Reliability, and Access Control｜FDE 系统设计：管道、可靠性与访问控制

Source: https://www.educative.io/courses/forward-deployed-engineer/fde-system-design-pipelines-reliability-and-access-control

> 与 Section I 第 18–19 课（条件更新、修订排序、隔离、原子进度、租约隔离、导出授权）重叠。新增：**承诺优先的设计步骤、摄取方式选择、5 分钟新鲜度预算、外部写的幂等键 (idempotency key)恢复 (K42)、Foundry 事务提示**。

### 要点 / Key ideas（新增）

- 一个正确的函数提供不了这些保证。**可辩护的设计把每个用户可见的承诺连到三样东西：在哪里执行、存了什么证据、失败时发生什么**。
- **先写验收测试 (acceptance test)**：东部仓库协调员看到足够新的可用性，请求一个被允许的变更，得到确认的结果或显式的"未解决"状态；合作方只收到批准的信息。
- 五步：澄清（actor、允许的变更、权威输入、所需新鲜度、失败容忍、披露边界）→ 追踪读所需数据与写发出的命令 → 分配每个职责、它拥有的状态与输入输出 → 规定失败、恢复、安全行为 → **用具体场景挑战每个保证**。
- **延迟 (latency) ≠ 新鲜度 (freshness)**：查询 100 ms 返回也可能显示昨天的库存。问记录量、变化率、并发用户、读写比、源 API 能力（能否列变更、给版本与删除标记、从 cursor 恢复）；把给定值与假设分开记；没给规模就**不要编造百万记录或提分片 (sharding)**。

| 职责 Responsibility | 拥有 Owns | 返回 Returns |
|---|---|---|
| 摄取与校验 Ingestion & validation | 源记录、版本、cursor、隔离 | 接受的记录，或带原因的拒绝 |
| 调用方授权 Caller authorization | 谁能读/命令什么 | 允许的视图，或显式拒绝 |
| 权限执行与操作存储 Operation store | 接受的请求及结果 | pending / unknown / confirmed |
| 目标适配器 Target adapter | 翻译成 Dispatch 的写契约 | 结果的目标端证据 |
| 披露控制 Disclosure control | 批准的合作方字段与接收者 | 白名单化 (allowlisted)的发布 |

- 场景：Stock 拥有物品可用性，Dispatch 拥有配送状态；批准的映射 Stock:S31 ↔ Dispatch:D88；东部协调员可以把可用性从一边复制到另一边。框是逻辑职责，可以先在一个应用 + 后台 worker 里。**命名一个队列什么也保证不了——重要的是消息内容、谁拥有、失败时怎样**。

**5 分钟新鲜度预算 / Five-minute freshness budget**：源发布 1 + 等轮询 1 + 拉取与校验 2 + 发布与服务 1 = 5 分钟（假设，需测量）。

| 摄取方式 Ingestion style | 适用 Fits when | 代价 Cost |
|---|---|---|
| 全量批量重载 Full batch reload | 源小到能在预算内重载 | 简单但重复工作 |
| **变更记录轮询 Changed-record polling** | 源能列出变更并从 cursor 恢复 | 需持久 cursor 与重放规则 |
| 流式 Streaming | 需要秒级新鲜度且源发事件 | 运维部件最多 |

- 每条落地记录保留：来源、版本、事件时间、拉取时间、批次 ID。校验必填字段、类型、批准的身份、允许值后才发布；**cursor 只与已存储输入一起推进**（崩溃不会跳过变更）。
- 保持数据诚实的规则：按源版本而非到达时间排序（S31/v11 已接受后，迟到的 v10 不能替换）；**隔离 (quarantine)无法解释的变化**（可用性字符串突然变成数字码 → 扣留直到含义约定，否则 1 可能变成自信但错误的答案）；显示最后良好数据及其年龄（被拒的更新不能让旧值标为当前），阻止需要无法重新校验数据的命令；**部分轮询证明不了删除**，只有 Stock 的显式删除标记才停用映射。
- **Foundry 提示**：数据集事务 SNAPSHOT（替换）与 APPEND（只追加）影响增量管道 (incremental pipeline)；**声明的 schema 不保证文件符合**，领域校验仍需显式检查；已提交的数据集事务**不覆盖**对 Dispatch 的外部写——把那份证据分开。

**安全写：K42 操作 / Safe write**

- 当前：Stock:S31/v11 = Available；Dispatch:D88/v6 = Unavailable，配送状态 Loaded。协调员请求 K42，存储的请求固定：映射、源版本 11、期望 Available、期望目标版本 6。发送前**重新校验 (revalidate)**调用方权限、映射、源状态；适配器只发可用性字段，**从不碰配送状态**。
- 守卫 (guard)成功：Dispatch 检查 v6，设可用性，保留 Loaded，变 v7。并发编辑先赢：Dispatch 已过 v6 → 写失败不覆盖；刷新并获取新的确认，**不要削弱守卫**。Dispatch 回显复制的可用性不是新的 Stock 权威——追踪值的来源以免同步循环。
- **响应丢失**：诱人设计"发送更新后设本地 processed = true"——Dispatch 提交后应用崩溃 → 效果发生了但记录说没发生；用新 key K43 重试可能重复。
- 假设并**明确说出** Dispatch 提供更强的契约：K42 的效果与结果原子存储在一起；K42 复用但 payload 不同 → 拒绝；重复 K42 **在版本检查之前**返回存储的结果；结果保留约定的重试窗口。

| 步骤 Step | 本地 Local | Dispatch |
|---|---|---|
| 1. 存请求，然后发送 | K42 accepted | v6 |
| 2. Dispatch 提交 | K42 accepted | v7，K42 → success |
| 3. 响应丢失 | K42 **unknown** | v7，K42 → success |
| 4. 重试相同 K42 | K42 confirmed，v7 | 不变，返回存储结果 |

- 把期望版本改成 7、改 payload、或建 K43 都是**新尝试**，不是恢复旧尝试。

```python
def recover(ops, dispatch, key):
    op = ops[key]
    if op["state"] != "unknown":
        return op
    # Resend the SAME key with the SAME stored payload; never edit it or mint a new key.
    status, detail = dispatch.apply(key, op["payload"])
    if status == "success":
        op["state"] = "confirmed"
        op["target_version"] = detail
    else:
        op["state"] = "needs review"          # conflict or rejection: reconcile, don't guess
    return op
```

```text
Before: K42 unknown, Dispatch v7 with stored result ('success', 7), effects = 1
recover(ops, dispatch, 'K42') -> K42 confirmed, target_version 7, effects still 1 (applied exactly once)
```

- **没有该契约时**：本地去重表 (dedup table)关不上"目标提交与进程崩溃之间"的缺口；版本守卫可能阻止第二次写，但冲突不证明是谁改的 → 从目标历史或运维审查对账，证据缺失就保持 unknown，**绝不承诺 exactly-once 效果**；任何可能产生新变更的重试前重新检查权限；重试窗口过期后重试失去保证。

| 信号 Signal | 遏制 Containment | 何时恢复 Recover when |
|---|---|---|
| 覆盖年龄 > 5 分钟 | 标陈旧，阻止需要当前数据的命令 | 覆盖与有效性恢复 |
| 操作超期仍 pending | 保持 pending/unknown，重发前先查目标 | 结果已对账 |
| 隔离率高于基线 | 隔离受影响记录，不发布猜测 | 数据契约已约定 |
| 管道失败或时长异常 | 带阶段与范围转给管道负责人 | 调度与输出健康 |

<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="220" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Idempotency key recovers a lost response｜幂等键恢复丢失的响应</text>
<defs><marker id="s" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>
<line x1="120" y1="45" x2="120" y2="205" stroke="#3b6fd8" stroke-width="2"/><text x="120" y="40" text-anchor="middle">App (operation store)</text>
<line x1="560" y1="45" x2="560" y2="205" stroke="#5a8f29" stroke-width="2"/><text x="560" y="40" text-anchor="middle">Dispatch (effect + key result, atomic)</text>
<g stroke="#555" marker-end="url(#s)"><line x1="120" y1="70" x2="558" y2="70"/><line x1="120" y1="150" x2="558" y2="150"/><line x1="560" y1="175" x2="122" y2="175"/></g>
<text x="340" y="64" text-anchor="middle">K42 {expected v6, Available}</text>
<text x="570" y="95">v6 → v7, store K42 → success</text>
<line x1="560" y1="110" x2="340" y2="110" stroke="#c0392b" stroke-dasharray="5,4"/><text x="330" y="114" text-anchor="end" fill="#c0392b">response lost ✘ → K42 unknown</text>
<text x="340" y="144" text-anchor="middle">retry SAME K42, SAME payload</text>
<text x="340" y="195" text-anchor="middle">stored ('success', 7) returned before version check → confirmed, 1 effect</text>
</svg>

**常见系统设计追问 / Common follow-ups**

| 追问 | 英文回答 |
|---|---|
| Why not use streaming? | "The requirement is five minutes and the source supports change polling. Streaming adds moving parts the freshness target doesn't need; I'd move to it if the target dropped to seconds and the source emitted events." |
| What happens if the target system is down for an hour? | "New commands stay pending, users see that state, and nothing is reported as done. When the target recovers, pending operations retry with their original keys and outcomes are reconciled before being shown as confirmed." |
| Can you guarantee exactly-once updates? | "Only if the target stores the effect and the key's result together. Without that, I can prevent many duplicates, but some outcomes must stay 'unknown' until reconciled." |
| How would you scale this? | "First measure where time goes — full reloads, slow joins or hot keys — then fix that bottleneck. Sharding isn't justified until a measured workload needs it." |
| How do you stop sensitive fields from leaking? | "Partner output is built from a server-side allowlist, permissions are rechecked at release, and markings propagate to derived data. I don't rely on the UI hiding a field." |

### 面试怎么说 / How to say it in the interview

- "I start from the promise — 'the coordinator sees availability no older than five minutes and gets a confirmed or explicitly unresolved outcome' — and for each promise I say where it's enforced, what evidence we store, and what happens on failure." ｜从承诺出发，每个承诺对应执行点、证据、失败行为。
- "If Dispatch's response is lost, the operation is 'unknown', not failed. I retry with the same key and payload, and that only works because Dispatch stores the key's result atomically with the effect — without that contract I'd reconcile from target history instead of promising exactly-once." ｜丢失响应 = unknown，同 key 重试，依赖目标端契约。

---

## II-7. Case Study: Designing an Operational System With Trade-offs｜案例：带权衡的运营系统设计

Source: https://www.educative.io/courses/forward-deployed-engineer/case-study-designing-an-operational-system-with-trade-offs

> 与 Section I 第 20 课（I64 审阅选择）同类；新案例的关键差异：**目标系统 Routing 不存每操作结果、也没有变更历史 → 丢失的响应只能标"结果未知"并人工对账 (reconciliation)**（对比 II-6 的 Dispatch 有幂等契约）。

### 要点 / Key ideas

- **English problem statement**: "A north-depot coordinator needs to copy maintenance priority into the matching routing job, without changing routing status. OP81 has a durable local request, but Routing never returned a response — should the operator resend it?"

| 项 Item | 详情 Detail |
|---|---|
| 维护记录 | M61/v14，priority Urgent，受限技术员备注；Maintenance 拥有 priority |
| 路由记录 | R24/v8，priority Normal，status Scheduled；Routing 拥有 status |
| 映射 | MAP7 revision 3；**共享资产标签本身不证明任何东西** |
| 权限 | 协调员只能改本仓库的 priority；viewer 不能改 |
| 合作方发布 | 只含北仓库 job 引用与 priority；从不含技术员备注或 status |
| 新鲜度 | 命令需要源覆盖不超过 10 分钟 |
| Maintenance 接口 | 可恢复变更页、每记录版本、删除标记、覆盖水位 (watermark) |
| Routing 接口 | **原子的期望版本字段 patch + 当前状态读；无每操作存储结果、无谁改了什么的历史** |

- **成功指标**：人工基线 24 次可比对账的中位数 (median) **14 分钟**；试点目标中位数 **< 6 分钟**；同时报告**未解决数量与年龄**、授权或错字段违规——否则更快的中位数可能只是难的案例没做完。量与并发未给 → 设计最小有用试点并列出扩展前要测什么。
- Palantir 开放题建议（候选人转述）：摆出备选与权衡，承诺一个具体方案，先得到可工作的想法再扩展。

**五个澄清问题 / Five clarifying questions**："Priority only, or status too?"（只 priority）· "Are mappings already approved?"（是，含 MAP7 r3；缺失需审查）· "What does stale data allow?"（带警告可读；命令需覆盖 < 10 分钟）· "Which fields can the partner receive?"（北仓库 job 引用 + priority）· **"Can Routing report the result of an earlier operation?"（不能，只有条件 patch 与当前状态读）**。

- 范围：已批准北仓库对的单向 priority 复制。排除：自动记录匹配、双向同步、创建 job、路线优化。缺映射 → `review_needed`；Maintenance 删除标记 → 停用映射、阻止新命令，**从不删除 Routing job**。
- 职责（一个应用 + 后台 worker）：Connector（原始页、持久 cursor、覆盖水位）、Validation（已接受版本、拒绝、删除状态）、Workflow（映射、预览、授权检查、命令受理）、**Operation store（不可变的请求、尝试、响应、未解决结果）**、Routing adapter（只改 priority 的期望版本 patch）、Partner release & audit。**直接映射查找 + 字段比较就够了**——图搜索、ML 模型、路线优化器都不需要。
- OP81 请求在发送前存储且**永不编辑**：调用方身份与北仓库范围；源 M61/v14、期望 Urgent；MAP7 r3、目标 R24；期望目标版本 8，patch 只含 priority；受理时间 + 所用覆盖与授权证据的引用。执行前复查权限、映射、源；前提变了就阻止执行，**不悄悄编辑请求**；OP81 复用不同 payload → 拒绝。
- 摄取预算：发布 2 + 等轮询 2 + 拉取校验 3 + 发布服务 1 = 8 分钟，留 2 分钟余量。迟到 v13 不能替换已接受 v14（记录被忽略的版本）；未知 priority 码隔离（若属于更新版本，旧值显示为最后良好 + 标注有未决的新输入）；**覆盖年龄 ≠ 事件年龄**（未变的记录事件时间旧但被近期水位覆盖时仍是当前的）。

**每个场景都有确定结果 / Every scenario has a defined outcome**

| 场景 Scenario | 用户看到 User sees | Routing 效果 | 保留证据 Evidence | 下一步 Next action |
|---|---|---|---|---|
| 正常成功 | Confirmed | v8 → v9，Urgent，保留 Scheduled | 响应与结果版本 | 无 |
| viewer 尝试更新 | Denied | 无 | 受限策略决定 | 找授权协调员 |
| 未映射记录 | review_needed | 无 | 缺映射决定 | 映射审查 |
| 覆盖 12 分钟 | 陈旧，命令被阻止 | 无 | 水位与失败检查 | 恢复覆盖后重新预览 |
| v14 之后迟到 v13 | 无变化 | 无 | 被忽略版本记录 | 无 |
| 已完成 OP81 重复投递 | 存储的结果 | 无 | 原结果 | 无；按操作 ID 串行化 (serialize)处理器 |
| 别人把 R24 推过 v8 | Conflict | OP81 无效果 | 冲突记录 | 刷新、确认、新建请求 |
| Routing 中断、未发送 | Pending | 无 | 持久意图与尝试 | 退避重试 |
| **提交后响应丢失** | **Outcome unknown** | v9，Urgent（来自 OP81） | 当前状态快照，单独保存 | **对账，不自动重发** |

**丢失响应的追踪 / Lost response traced**

| 步骤 | 本地 | Routing |
|---|---|---|
| 1. 存 OP81 后发送 | Accepted，记录尝试 | v8，Normal，Scheduled |
| 2. Routing 提交 | Accepted | v9，Urgent，Scheduled |
| 3. 响应丢失 | Outcome unknown | v9 |
| 4. 授权读 | Unknown + 存 v9 Urgent 快照 | v9 |
| 5. 可选的相同重试（期望 v8） | Unknown | **Conflict，无变化** |

- 实际上 OP81 导致了提交，但应用**证明不了**：观察到的状态（v9 Urgent）可能是别人做的同样改动；Routing 无每操作结果与历史；版本守卫阻止对 v8 的第二次写，但冲突不说明谁改的。
- 告诉用户："OP81's outcome is unknown. Routing currently shows Urgent and Scheduled at version 9. We can't confirm which operation made that change." —— 存为**分开的事实**。
- **诱人的恢复**："没有成功标志，就读 R24；若是 Urgent 就标 OP81 confirmed，再安全起见对当前版本发 OP82。" → ① 匹配的状态当证明——不是；② 自动发 OP82 是**新变更**，可能触发下游工作。若真需要后续业务变更：刷新输入、获取当前授权与确认、记录一个独立请求。**没有本地标志或存储意图能关上"Routing 提交与响应丢失之间"的缺口——只有目标端契约可以，而 Routing 不提供**。
- **中断**：意图持久；从未发送 → pending，可能已到达 → outcome_unknown；瞬时失败用有上限 + 抖动 (jitter)的退避 (backoff)重试；与流程负责人约定响应截止（未给出）。
- **权限撤销**：队列中未发送的请求 → 阻止并记录拒绝；已模糊的 OP81 → 用单独授权的读对账；撤销不说明之前的写是否发生。
- **恢复顺序**：从持久 cursor 恢复摄取 → 重新校验覆盖与版本 → 对账模糊操作 → **之后才重新启用命令**。
- **合作方发布**：在发布边界用白名单 (allowlist)构建（含导出与派生输出）；UI 隐藏列阻止不了含技术员备注的导出。审计：actor、操作 ID、映射修订、版本、决定、结果；技术员备注不进广泛可读的日志。

| 选择 Choice | 替代 Alternative | 理由 Why |
|---|---|---|
| 变更轮询 | 全量重载、流式 | 用源的变更接口且在预算内；测得合适时重载也行；流式需要理由 |
| 一个应用 + worker | 独立服务 | 逻辑所有权才重要；只有真实隔离或负载需要时才拆 |
| 陈旧显示、阻止命令 | 允许陈旧操作 | 用户保留可见性，不安全写被遏制 |
| 人工对账未知结果 | 承诺 exactly-once | Routing 没有能让 exactly-once 成立的契约 |

- **面试官找的弱点**：问题框定前就选技术；编造规模；缺身份或所有权规则；用时间戳解决所有冲突；把 processed 标志当作与远程写原子；**把匹配值当作操作证明**；无限制导出；监控没有负责人或遏制动作。

<svg viewBox="0 0 720 230" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<rect width="720" height="230" fill="#fff"/>
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="bold">Target contract decides recoverability｜目标端契约决定能否自动恢复</text>
<rect x="20" y="45" width="320" height="160" rx="10" fill="#f3f7ee" stroke="#5a8f29"/>
<text x="180" y="70" text-anchor="middle" font-weight="bold">Dispatch (II-6): key result stored</text>
<text x="180" y="95" text-anchor="middle">effect + K42 result atomic</text>
<text x="180" y="118" text-anchor="middle">retry same key → stored result</text>
<text x="180" y="141" text-anchor="middle">→ confirmed, one effect</text>
<text x="180" y="170" text-anchor="middle">自动恢复 = 查找</text>
<rect x="380" y="45" width="320" height="160" rx="10" fill="#fdecea" stroke="#c0392b"/>
<text x="540" y="70" text-anchor="middle" font-weight="bold">Routing (II-7): no key result, no history</text>
<text x="540" y="95" text-anchor="middle">retry vs v8 → conflict, tells nothing</text>
<text x="540" y="118" text-anchor="middle">v9 Urgent ≠ proof OP81 did it</text>
<text x="540" y="141" text-anchor="middle">→ outcome_unknown + snapshot</text>
<text x="540" y="170" text-anchor="middle">人工对账 = 判断，不自动发 OP82</text>
</svg>

**常见追问 / Common follow-ups**

| 追问 | 英文回答 |
|---|---|
| Just resend OP81. What's the harm? | "An identical resend against version 8 is blocked by the version guard, so it's harmless but tells us nothing. A new request against version 9 could make a second change and trigger downstream work, so I wouldn't do that automatically." |
| What would make this recoverable automatically? | "A Routing contract that stores each operation's result under its key, or a history of which operation changed what. With either, recovery becomes a lookup instead of a judgment." |
| Why not build two-way sync now? | "Each system owns different fields, and two-way sync adds conflict rules and loop risks. One-way priority copying proves value first; I'd expand once the pilot meets its target." |
| How would you know the pilot worked? | "Median time for comparable completed work below 6 minutes against the 14-minute baseline, with the unresolved count and age reported, and zero unauthorized or wrong-field updates." |
| What would you measure before scaling? | "Record volume, change rate, poll duration, validation backlog, Routing rate limits, and how often operations end up unknown." |

### 面试怎么说 / How to say it in the interview — condensed walkthrough

> "I'd clarify five things first: priority only or status too; whether mappings are approved; what stale data allows; which fields the partner gets; and — most important — whether Routing can tell me the result of an earlier operation. It can't, which shapes recovery.
> Scope is one-way priority copy for approved north-depot pairs. OP81 is stored immutably before dispatch with the caller, source version 14, mapping revision 3 and expected target version 8, and I recheck permission, mapping and coverage right before sending. The adapter patches only priority with an expected-version guard.
> If the response is lost, OP81 is 'outcome unknown'. An authorized read showing version 9 Urgent is stored as a separate observation — it doesn't prove OP81 did it, and I won't auto-send a new request against version 9. A human reconciles. Success is a median under 6 minutes versus the 14-minute baseline, reported together with the unresolved count and age and zero wrong-field updates, so we can't win by leaving hard cases undone."

---

## II-8. Behavioral Questions: Pushback, Failure, Ownership and Ambiguity｜行为题：反对、失败、负责与模糊

Source: https://www.educative.io/courses/forward-deployed-engineer/behavioral-questions-pushback-failure-ownership-and-ambiguity

> 与 Section I 第 21–22 课（压缩故事、故事卡、240 工单导出）重叠。新增：**四要素 + 五段结构、30 个调度任务的示例（pushback 与 failure 在同一事件中）、重叠计数陷阱、使命与伦理题、新增问题（与利益相关方分歧、政府/国防工作）**。

### 要点 / Key ideas（新增）

- 选故事前先找到**一个你做的真实决定 + 一个它的后果**；找不到就说明故事没准备好。**可辩护的回答在面试官换问法时保持相同事实**。
- 四要素：**个人决定、当时掌握的信息、受影响的人、观察到的后果**。模糊："We delivered under pressure."；具体："I assumed an empty field meant standard service. Review found four incorrect classifications."
- 美国政府 FDSE 职位看重：与技术和非技术人员协作、随目标变化与用户迭代、持续学习、在最少监督下做决定（职位期望，非评分表）。**职责清楚的小项目胜过讲不清决策的大项目**。
- **五段结构（STAR (Situation, Task, Action, Result) 的增强版）**：情境与利害 → 个人责任（区分你和队友的工作，说出不确定或分歧）→ 决定（证据、备选、你的建议、**谁有决定权**）→ 观察到的后果（测量、观察、未知分开）→ 反思（失败要有之后行为改变的证据；没有就直说并说明打算怎么改）。准备**事实笔记而非背诵段落**；开场 60–90 秒，被问再展开。

**示例：周五试点的 30 个调度任务（虚构演示）**

| 人 Person | 拥有 Owns |
|---|---|
| 你 | 解析、校验、异常队列 |
| 队友 | 调度接口、排期集成 |
| 运营负责人 | 分类策略、试点批准 |

| 选项 Option | 收益 Benefit | 代价 Cost |
|---|---|---|
| 全部派发 | 保持完整范围与日期 | 把未解决的目的地送进运营 |
| 阻止整个试点 | 无风险暴露 | 停掉可以审阅并使用的工作 |
| **带异常队列的监督试点** | 有用的试点，不完整任务待审 | 需要有人审异常 |

- 开场回答（英文）：
> "An operations lead wanted 30 imported delivery jobs sent straight to dispatch for a Friday pilot. I owned parsing, validation, and exception handling. Six jobs had incomplete destinations, so I recommended a supervised pilot with those jobs held for review. I compared that with dispatching everything and with delaying all the work. The lead owned the pilot scope and approved the reviewed approach.
> The review also exposed my own mistake: I had treated empty service codes as standard without confirming the policy. Four jobs needed reclassification, and the pilot started a day late. I removed the default, got approved classifications, and checked the rerun against all 30. On a later import, I used an explicit code dictionary and approved examples before implementation, which caught two undocumented codes before release. I learned to confirm operational meanings before encoding them."
- 负责人的截止日期是合理的；**目的地确实完整的证据会改变建议——好的 pushback 对这种证据保持开放**。
- **失败**是未确认的服务码假设（之前对目的地的 pushback 不能为它开脱）。"What did you personally get wrong?" → "I treated an empty service code as standard without confirming it with the operations lead. That was my parser decision. Four jobs needed reclassification, and the pilot began a day late. I should have raised the unknown policy before implementing."
- **修复 (repair) vs 行为改变 (changed behavior)**：修复 = 去掉默认、未分类任务转审、验证重跑；行为改变 = 之后 20 任务的导入用代码字典 + 批准样例在发布前抓到两个未文档化代码。"I fixed the parser" 是恢复，之后的导入才是改变做法的证据。不要怪脏数据——源里有个未知，是你选择赋予它一个没人确认过的含义。
- **负责**："I owned the parser, validation and exception handling. Teammates owned the dispatch interface and scheduling. The lead owned classification policy and pilot approval. I brought the alternatives and implemented the agreed behavior. I didn't have authority to define service policy or approve dispatch."
- **模糊性：讲每个选择的可逆性 (reversibility)**——发布前（代码映射可改、可重跑）vs 派发后（指令可能已影响人和工作，很难撤销）；刻意排除路线优化与自动异常处理（首版要先建立可靠导入与审阅；优化解决不了目的地完整性或分类策略）。
- **重叠计数陷阱**：4 个错误分类 + 6 个不完整目的地，**重叠未知** → 不同受影响任务数在 **6 到 10** 之间，不能说 10。重跑匹配全部 30 个批准分类；**无处理时间基线 → 不能声称更快**。

| 质疑 Challenge | 可辩护回答 Defensible reply |
|---|---|
| "Was it your decision?" | "The empty-code default was mine. The reviewed-pilot scope was my recommendation, approved by the lead. Classification policy was the lead's." |
| "Why not delay everything?" | "The known destination issue didn't justify discarding all progress. The lead could still delay if supervision wasn't available. It ultimately started a day late." |
| "How do you know it improved?" | "The rerun matched approved classifications for all 30 reviewed jobs. With no baseline, I can't claim it was faster." |
| "What did you do differently next time?" | "On a later 20-job import, a code dictionary and approved examples caught two undocumented codes before release. That supports a change in practice, not a claim that every future error was prevented." |
| "What would the stakeholder say?" | "I can't speak for them. They could fairly point to the missed Friday start and the extra review my assumption caused. I'd ask whether the exception process met their needs." |

- **Why Palantir / Why FDSE**（不需要平台经验、不需要说 Palantir 独一无二、不堆产品名）：
> "I found I wanted to stay involved through user review and operational verification, not stop when the parser produced output. The FDSE posting describes working with technical and non-technical people and iterating with users as objectives change. That's a reason I'm looking at FDSE work at Palantir. I'd want to understand how this team balances hands-on building with user iteration."
- **使命与伦理（不表演认同）**：负责人要求给所有承包商**无限期**访问可识别的配送历史用于排障 (troubleshooting) →
> "I support giving contractors what they need to resolve their assigned delivery problems. First I'd establish which records and fields they need, whose information is in those histories, what authorization applies and how long access is needed. A restricted view of current jobs might meet the need with far less exposure. I wouldn't implement blanket indefinite access while purpose, authorization and retention are unresolved. I'd escalate those questions to the people who own them."
- 政府、国防、隐私、公民自由 (civil liberties)类问题同法：**说出真实观点、你看到的权衡、什么信息会改变你的决定**；不编造保障措施或部署事实。（有二手指南里候选人把 HM 面后被拒归因于"使命契合"——那是发帖人的解读。）
- 诱人回答修复：✘ "The client wanted a bad approach, so I convinced them to use mine. We launched successfully, saved 50% of the time, and I learned to communicate."（贬低对方、冒领权限、无证据的成功与 50%、空洞教训）→ ✔ "The lead needed a Friday pilot. Six jobs lacked complete destinations, so I recommended supervised review, and the lead approved the scope. My unconfirmed empty-code default caused four wrong classifications, and the pilot began a day late. I removed the default and verified the rerun against all 30. I have no speed baseline. On a later import, a code dictionary caught two undocumented codes before release." —— **不说任何东西"糟糕"或"成功"，让事实替听者判断**。

**报告过的行为问题（新增的两题给出 STAR 模型回答；其余见 Section I 第 22 课）**

| 问题 Question | 回答要点 Guidance |
|---|---|
| Why Palantir, and why this team? | 连接一个真实经历与你对岗位的研究；说你想做什么，而不只是公司有名；坦白没用过的东西 |
| Tell me about a time you pushed back on a customer. | 说出客户的合理目标、让你担心的证据、备选、你的建议、谁决定；别说对方的想法糟糕 |
| Tell me about a failure. | 你的具体决定导致的具体后果；修复与之后的行为改变分开；不怪数据或队友 |
| Describe owning an ambiguous problem end to end. | 说出未知、先解决哪些及原因、刻意排除了什么、如何验证结果 |
| **Tell me about a disagreement with a stakeholder.** | 展示你理解他们的约束、什么证据会改变你的想法、最终如何决定 |
| **How do you feel about government or defense work?** | 说真实观点、权衡、什么会改变你的想法；不表演认同、不编造部署事实 |

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 38 篇）。

**Q: How do you feel about government or defense work? — model answer structure**

> "I think software that helps public institutions make better operational decisions can do real good, and I'm comfortable working in that space. The trade-off I take seriously is that the same data capabilities raise privacy and civil-liberties risks, so I care about purpose limits, authorization and auditability being built in rather than bolted on. What would change my view on a specific project is if I couldn't get a clear answer on what the system is for, who can access what, and how misuse would be detected. I'd want to understand how teams here raise those concerns."

### 面试怎么说 / How to say it in the interview

- "Four jobs had wrong classifications and six had incomplete destinations, but I don't know the overlap, so the distinct count is somewhere from six to ten — and with no baseline, I can't claim it got faster." ｜重叠未知不相加；无基线不声称改进。

---

## II-9. The Hiring Manager Final, Team Matching, and the Offer｜招聘经理终面、团队匹配与 offer

Source: https://www.educative.io/courses/forward-deployed-engineer/the-hiring-manager-final-team-matching-and-the-offer

> 与 Section I 第 23–24 课重叠（来源分开、项目深度图、硬性要求、证据账本、谈判信）。新增：**"你想改之前哪一轮"的回答法、三类陈述分离、项目证据图（库存导入示例）、日期三分类、offer 清单与 recruiter 信**。

### 要点 / Key ideas（新增）

- "Which part of your earlier interview would you change?" → **先澄清**："Would you like me to reflect on my approach, work through a corrected solution, or focus on a particular technical decision?" 保持实际发生的事不变，同时展示你现在的理解。公开报告（2025-07-01）：一小时 HM 面混合行为与拆解式问题；二手指南说经理会重访未解决的话题与动机——**它们不说明任何面试官对你表现的看法**。
- 示例：面试后意识到 API 方案只处理了第一页。✔ "I processed one page but did not establish that all records had been retrieved. I can explain how I would follow continuation tokens to the documented stopping condition." ✘ "我事后修好了"（后来的设计不改变面试中运行的东西）；✘ "面试官显然认为那轮很弱"（不知道他们的判断）；✘ 空泛道歉然后转移话题。

**项目证据图 / Project evidence map（库存导入示例）**：你做了库存导入流程的校验与预览；运营负责人拥有库存策略与导入批准；导出 40 行：35 行有不同可用 item ID，5 行无 ID；**预览静默丢掉了这 5 行**；审阅在批准前发现，没有导入发生。

| 要点 Point | 笔记 Note |
|---|---|
| 用户与决策 | 负责人决定导出是否可以导入 |
| 你的工作 | 只有校验与预览 |
| 数据路径 | 导出 → 校验 → 预览 → 批准 → 导入 |
| 权衡 | 无 ID 行待审，而不是猜 |
| 失败 | 预览隐藏 5 行，且没有异常计数 |
| 验证 | 审阅在批准前发现这 40 行导出的缺口 |
| 局限 | 没有导入发生，速度未测量 |

- "Why not infer the missing IDs?" → "A guessed ID could attach stock to the wrong item. I'd hold those rows and ask the lead how to resolve them. Holding a row doesn't declare the stock invalid. Inventory policy belongs to the lead."

**三类陈述分开 / Keep three statements separate**

| 陈述 Statement | 库存导入 |
|---|---|
| 当时发生了什么 What happened then | 预览漏掉 5 行且不显示计数；我的决定；审阅发现，未导入 |
| 我现在理解什么 What I understand now | **每个输入行都需要一个可见结果** |
| 之后检查了什么 What has been checked since | **还没有**——只有提议的修复与测试计划，没有证据 |

- "What would you change?" → "Add a review list and a row-accounting check: 35 accepted plus 5 held must equal 40 inputs. Also check duplicate IDs, an empty file, and an attempted import without approval. Those are proposals. I haven't implemented or run them." 行计数检查抓行消失，但总数 40 揭示不了错误 ID 或重复替换缺失行——所以还需其他检查。
- "Which test proves the fix works?" → **"None yet."**（比暗示性的声称更有力）。把问题叫"沟通问题"会掩盖真实失败：**软件对批准人隐藏了需要的信息**。
- **Why Palantir / why this team** 的三个输入：一个解释你想做的工作的真实经历 + 一个已核实的岗位方面 + 过程中学到的东西 + 一个决定是否契合的剩余问题：
> "The stock-import project showed me I value staying involved until a user can make a reliable decision. Producing a preview wasn't enough when it hid unresolved rows. That connects with the user collaboration in the FDSE role description, and your description of staying involved through operational review makes it more concrete. I'd still like to understand who owns discovery, implementation, deployment and post-release checks on the team I'm being considered for."
- 简短追问：所有权（"I owned validation and preview, including the omission. The lead owned policy and approval."）；"负责人要全部 40 行导入怎么办？"（解释未解决 ID、建议扣留 5 行，策略决定权在负责人，不编造标识）；"为排障广泛访问员工活动？"（先问排障需要什么、谁有权看哪些记录）。

**团队匹配、出差、资格 / Team matching, travel, eligibility**

- 二手说法冲突：一个说匹配在 HM 电话时，另一个说通常在 offer 之后；**无官方统一顺序 → 问 recruiter**：还剩哪些决定、匹配何时预期？我被考虑的 track 与团队范围、汇报给谁？首个分配如何选、构建 vs 面向客户的比例？
- "Travel as needed" 没给可用上限 → 问拟议分配的频率、行程时长、目的地、提前通知、近期模式；另问家庭所在地、搬迁 (relocation)、国际出差。部分 FDSE 申请会问出差、搬迁、安全许可 (security clearance)、其他流程、薪酬范围——对那些职位相关，不是通用要求。把你的要求写在答案旁边；**不要把安慰当成约定**。

**日期分类 / Keep dates in their categories**

| 日期 | 是什么 | 不是什么 |
|---|---|---|
| 11-06 | recruiter 的估计 | 承诺，或有 offer 的信号 |
| 11-09 | 另一流程的决定截止 | Palantir 的截止 |

> "I have another decision due November 9. You mentioned hoping for an update November 6. Is that an estimate, what's still outstanding, and when should I check back if there's no update?"

- 诱人总结："之前那轮很差，但我全修好了。这个团队完全合适，匹配在 offer 之后，出差应该没问题。" → 两个普通追问就打破："Which test ran?"、"What travel have you agreed to?" 修复版："I noticed an omission and have a proposed fix, untested. The assignment isn't settled yet, and I still need concrete travel expectations."

**Offer 清单（通用，非 Palantir 标准条款，非法律/财务建议）**

| 方面 Area | 检查 Check |
|---|---|
| 现金 Cash | base 金额与币种、奖金或 sign-on 条款及条件 |
| 股权 Equity | 类型、数量、管辖文件、归属 (vesting)；示例不是保证价值 |
| 雇佣 Employment | 雇佣实体、职位、地点、开始日期、分配状态、出差 |
| 决定条款 Decision terms | 声明的条件与接受截止 |

| 项 Item | 类别 Category | 下一步 Next step |
|---|---|---|
| base、地点 | 书面条款 | 与之前对话比较 |
| 11-09 接受截止 | 书面条款 | 规划审阅时间 |
| 股权计划 | **被引用但缺失** | 索要 |
| 团队分配 | 开放问题 | 问状态与负责人 |
| "as needed" 出差 | 未定义 | 问频率、时长、通知 |
| 11-06 更新 | 估计 | 确认是否仍有效 |
| 你的出差通知需求 | 个人要求 | 说出来并问能否满足 |

> **Recruiter message**: "Thank you for the offer. I have the base compensation, location and November 9 deadline. Could you send the referenced equity schedule and clarify any conditions? Please also confirm the assignment status, and connect me with whoever can explain expected travel frequency, duration and notice. Another process needs my decision November 9. If the missing information arrives close to the deadline, could we discuss review time? Please confirm any agreed changes in writing."

- 发信本身不解决任何事；**延期在约定前不存在**。
- 练习检查点：优先问题——①具体出差频率/时长/通知（"regular" 无法规划）②分配范围与状态（团队未定）③岗位特定的安全许可或资格条件（可能决定能否接受）；信中区分三个日期（11-10 估计、11-11 另一流程约束、11-12 书面截止），请求审阅时间但不假设延期。

**终面可能问到的问题 / Final-round questions**

| 问题 | 英文回答要点 |
|---|---|
| Which part of your earlier interview would you change? | "Can I check what you'd like — reflection, a corrected solution, or one decision? … The gap was that I processed one page without establishing complete retrieval. Now I'd follow continuation tokens to the documented end, with checks for multiple pages, failures and repeated tokens — I've designed that but haven't run the checks." |
| Walk me through a project in depth. | 用证据图：用户与决策、你的部分、数据路径、权衡、失败、验证、局限；不冒领队友的工作 |
| Why this team? | 一个真实经历 + 一个已核实的岗位方面 + 一个关于契合的开放问题；具体来自你学到的事实，而不是更强的形容词 |
| How do you feel about travel? | "I'm open to customer travel; what I need is some advance notice. Could you tell me the typical frequency, trip length and notice for this assignment?" ——给出真实要求，不对 "as needed" 先同意 |
| Do you have other processes? | "Yes — I have another decision due on [date]. I'm not trying to pressure the timeline; I just want to make sure I can give this a proper decision." ——如实分享时间，不虚张 offer、不承诺做不到的可用性 |

---

## II-10. Full Mock Loop and a 2-Week Prep Plan｜完整模拟与两周准备计划

Source: https://www.educative.io/courses/forward-deployed-engineer/full-mock-loop-and-a-2-week-prep-plan

> 与 Section I 第 25–27 课（模拟、冻结 (freeze)、七维评审、四周计划）重叠。新增：**八站 350 分钟模拟（新题目）、六维证据账本、14 天计划、"17 是中间小计"**。

### 要点 / Key ideas（新增）

- 开场："The total is 17" 但端点还在返回 continuation token → **算术对，但检索未完成、停止条件 (stopping condition)未检查**——这是正确的中间小计，不是完成的答案。算术与验证分开记，才知道下一步练什么。
- 二手指南的准备池：拆解、学习、重构调试、编码、系统设计 + recruiter、筛选、HM 对话。各站独立练，可按真实日程重排。

| 日 Day | 站 Station | 分钟 |
|---|---|---:|
| 1 | Recruiter | 15 |
| 1 | 技术筛选 Technical screen（约 25 实现 + 30 SQL + 35 API） | 90 |
| 1 | 拆解 Decomposition | 40 |
| 1 | 学习 Learning | 40 |
| 2 | 重构调试 Re-engineering | 40 |
| 2 | 编码 Coding | 40 |
| 2 | 系统设计 System design | 40 |
| 2 | 行为与 HM | 45 |
| | **合计**（185 + 165） | **350** |

- 规则：材料分开（候选人拿任务与允许文档；观察者拿澄清单、期望答案、失败变体）；计时中不教学（实质提示记录措辞与时间）；**截止时冻结**，未完成标未完成；除提供的文档外不借助任何东西（真实工具权限问 recruiter）；独自练习时先全部尝试再看评审。**保存的代码是强证据，事后对自己沟通表现的记忆是弱证据**。

### Station 2 — Technical screen solutions｜技术筛选题解

**(a) Implementation: signed warehouse movements**

- **English problem statement**: "Sum signed movements by the full (warehouse, SKU) key, drop only final zeros, sort by warehouse then SKU, and don't modify the input. A negative movement is a contribution, not a row to discard."

```text
Input:  [('W1','A',+7), ('W1','A',-2), ('W2','A',+4), ('W2','A',-4), ('W1','B',-1)]
Output: [('W1','A',5), ('W1','B',-1)]      # W2/A nets to 0 and is dropped; W1/B stays negative
Empty input -> []
```

```python
def net_movements(movements):
    totals = {}
    for warehouse, sku, quantity in movements:          # read-only pass; input untouched
        key = (warehouse, sku)                          # full composite key
        totals[key] = totals.get(key, 0) + quantity     # negatives are contributions
    return sorted(
        (warehouse, sku, total)
        for (warehouse, sku), total in totals.items()
        if total != 0                                   # drop only FINAL zeros
    )
```

**(b) SQL: active devices per region**

- **English problem statement**: "Return one row per region in `devices`, including regions with zero active devices. A device is active only if its latest event (by event_time, then event_id) is active; a device with no events is not active."

```text
devices: D1 north, D2 north, D3 south
events:  1 D1 09:00 active | 2 D1 10:00 inactive | 3 D2 09:00 active
Output:  north 1, south 0
Wrong (filter active first, then pick latest): north 2
```

```sql
WITH latest AS (
    SELECT device_id, status,
           ROW_NUMBER() OVER (PARTITION BY device_id
                              ORDER BY event_time DESC, event_id DESC) AS rn
    FROM events                                -- choose latest across ALL statuses first
)
SELECT d.region,
       COUNT(*) FILTER (WHERE l.status = 'active') AS active_devices
FROM devices d
LEFT JOIN latest l ON l.device_id = d.device_id AND l.rn = 1
GROUP BY d.region
ORDER BY d.region;
```

**(c) API: paginated sum with dedup and 429 retry**

- **English problem statement**: "Sum amounts across pages. First request has no token. Identical duplicate IDs count once; a conflicting amount for the same ID fails. Never return a total from incomplete retrieval. Guard against repeated tokens and too many pages. Variant: the first request for T returns 429 with Retry-After: 2 and the retry succeeds — at most three attempts per page, using a fake clock."

```text
Page (no token): R1=8, R2=9, next=T
Page T:          R2=9, R3=4, next=None
Output: 21   (8 + 9 + 4, R2 counted once; 17 after page 1 is only a subtotal)
Variant: T -> 429 Retry-After 2, then 200 -> still 21, fake clock advanced by 2
```

```python
MAX_ATTEMPTS = 3
MAX_PAGES = 1000


class RateLimited(Exception):
    def __init__(self, retry_after):
        super().__init__("429")
        self.retry_after = retry_after


def total_amount(fetch, sleep):
    amounts = {}
    seen_tokens = set()
    token = None
    for _ in range(MAX_PAGES):
        page = None
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                page = fetch(token)
                break
            except RateLimited as error:
                if attempt == MAX_ATTEMPTS:
                    raise                          # exhaustion: no partial total
                sleep(error.retry_after)           # injected fake clock in tests
        for record_id, amount in page["records"]:
            if record_id in amounts and amounts[record_id] != amount:
                raise ValueError("conflicting amount for " + record_id)
            amounts[record_id] = amount            # identical duplicate counts once
        token = page.get("next")
        if token is None:
            return sum(amounts.values())           # only after the terminal page
        if token in seen_tokens:
            raise ValueError("repeated token " + token)
        seen_tokens.add(token)
    raise RuntimeError("page limit exceeded")      # never a partial total
```

### Station 3 — Decomposition: missed community-clinic appointments｜拆解：减少社区诊所爽约

- **English problem statement**: "How would you reduce missed community-clinic appointments?" 评审要点：用户是诊所协调员 (clinic coordinator)、两周试点、有预约登记表、**临床优先级排序不在范围内**、联系需要同意 (consent)；看是否有尊重同意的首个工作流以及出勤与联系结果的测量。

### 面试怎么说 / How to say it in the interview — Station 3 full walkthrough script

> **Clarify**: "Before proposing anything: who would act on this — a front-desk coordinator calling patients this week, or a manager redesigning scheduling policy? … A clinic coordinator, with a two-week pilot. What data exists — is there an appointment register with booking time, appointment time, status and contact preference? … Yes. Do we have consent to contact patients, and through which channels? And is prioritizing patients clinically in scope? … Contact needs consent, and clinical prioritization is out of scope. That tells me this is a reminder-and-follow-up workflow, not a risk model that ranks patients by medical need."
>
> **Scope**: "First version: each morning, the coordinator sees tomorrow's appointments for patients who consented to contact, sends or makes a reminder, and records the outcome — confirmed, rescheduled, cancelled, no answer. I'm excluding no-show prediction, automated clinical triage and any contact without consent."
>
> **Model**: "Appointment keyed by appointment_id with patient reference, clinic, scheduled time and final status — attended, missed, cancelled, rescheduled. A separate ContactAttempt keyed by attempt_id: appointment_id, channel, time, coordinator and outcome. Consent is its own record with channel and recorded date, so we never infer it from a phone number existing. Missing outcomes stay unknown, not 'attended'."
>
> **Write and read**: "POST /contact-attempts requires an authorized coordinator for that clinic, checks consent for that channel at write time, and appends — attempts are never overwritten. GET /reminder-list?date= returns only consented, scheduled appointments for the caller's clinic, with minimal fields: time, preferred channel, contact status. No clinical notes."
>
> **Measure**: "Baseline is the missed-appointment rate for the same clinic and weekdays over the previous four weeks. The pilot measure is the missed rate among consented appointments over two weeks, reported with the share of appointments we actually reached, and guardrails: complaints or opt-outs, and contacts attempted without valid consent — which must be zero. Two weeks is short and seasonality or staffing can confound it, so I'd frame it as a signal, not proof."
>
> **Unknown I'd resolve first**: "Whether final attendance status is reliably recorded the same day — without that, I can't measure the outcome at all."

中文要点：协调员 + 两周试点 → 只联系已同意的患者 → 预约/联系尝试/同意分表 → 写入时校验同意 → 最少字段读接口 → 基线对比 + 护栏（投诉、无同意联系为 0）→ 先确认出勤状态是否可靠记录。

### Station 4 — Learning: order-preserving enrichment

- **English problem statement**: "A hypothetical batch reader returns one result per requested key, in request order; duplicates are allowed, missing keys return None, and a transport failure raises without returning partial results. Write an order-preserving enrichment for [B, A, B, C] where B=2, A=5 and C is missing."

```python
def enrich(keys, batch_read):
    values = batch_read(keys)              # one result per key, request order; raises on transport failure
    return list(zip(keys, values))         # duplicates preserved; missing -> None

# enrich(['B', 'A', 'B', 'C'], reader) -> [('B', 2), ('A', 5), ('B', 2), ('C', None)]
# transport failure -> the exception propagates; no partial list is returned
```

### Station 5 — Re-engineering: falsy cache values

- **English problem statement**: "A Totals class uses a caller-supplied cache and reader. Both 0 and None are valid cached values. The reader returns 0 for A, None for B, 7 for P, and counts its calls. Diagnose repeated reads and repair."

```python
class Totals:
    def __init__(self, cache, reader):
        self.cache = cache
        self.reader = reader

    def get_buggy(self, key):
        if not self.cache.get(key):        # BUG: 0 and None look "missing", so they are re-read
            self.cache[key] = self.reader(key)
        return self.cache[key]

    def get(self, key):
        if key not in self.cache:          # FIX: test membership, not truthiness
            self.cache[key] = self.reader(key)
        return self.cache[key]

# Two requests each for A (0) and B (None): buggy -> 4 reader calls; fixed -> 2.
# Also check: P=7 positive case, and a separate instance with its own cache reads again.
```

### Station 6 — Coding: reservations with booking IDs

- **English problem statement**: "An in-memory reservation object with 5 seats. A reservation takes a quantity, rejects negatives, allows zero, succeeds only if enough seats remain, and changes nothing on failure. Change: reservations take a booking ID and can be cancelled by ID. Only successful reservations create bookings; a used ID can't be reused even after cancellation; a failed request doesn't use up its ID; a repeated cancellation can't restore seats twice; an unknown cancellation returns False."

```text
reserve(3) -> True, reserve(3) -> False, reserve(2) -> True   (0 seats left)
With IDs: reserve('b1', 3) -> True; cancel('b1') -> True (seats +3); cancel('b1') -> False
          reserve('b1', 1) -> ValueError (ID used); reserve('b9', 99) -> False, then 'b9' still usable
Invariant: 0 <= seats_left <= 5
```

```python
class Reservations:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.seats_left = capacity
        self.active = {}                   # booking_id -> quantity
        self.used_ids = set()              # IDs consumed by SUCCESSFUL reservations

    def reserve(self, booking_id, quantity):
        if quantity < 0:
            raise ValueError("quantity must be non-negative")
        if booking_id in self.used_ids:
            raise ValueError("booking ID already used")
        if quantity > self.seats_left:
            return False                   # failure changes nothing, ID stays unused
        self.seats_left -= quantity
        self.active[booking_id] = quantity
        self.used_ids.add(booking_id)
        return True

    def cancel(self, booking_id):
        quantity = self.active.pop(booking_id, None)
        if quantity is None:
            return False                   # unknown or already cancelled
        self.seats_left += quantity        # restores exactly once
        return True
```

- 保留的基线承诺：负数拒绝、零允许、只在座位足够时成功、失败不改变任何东西、座位在 0–5 之间。

### Station 7 — System design brief

- **English problem statement**: "Design an authorized staff workflow that updates repair urgency from an inspection source. The source owns urgency; local staff own scheduling notes, which must be preserved. A write response can be lost. Cover caller scope, identity mapping, freshness, stale-state behavior, durable intent, and how to tell success from an unknown outcome."
- 评审要点：目标支持**版本条件的、只改字段的更新**，但**没有每操作存储结果** → 之后看到的匹配 urgency **不证明**是这次操作造成的（同 II-7 的 OP81：结果未知 + 快照 + 人工对账 (reconciliation)；只 patch urgency，保留调度备注；陈旧覆盖阻止命令；持久意图 (durable intent)先存再发）。

### Station 8 — Behavioral & HM

- "Tell me about a time you pushed back on a customer request" 与 "Why Palantir, and why this team?"（二手指南列为报告题，无日期、无保证），然后追问失败、使命与伦理、项目局限、团队契合、未决条款——见 Section I 第 22 课与 II-8、II-9 的模型回答。

**六维证据账本 / Six-dimension evidence ledger**（每站每维：independent / prompted / not demonstrated / n/a + 简短观察；**不相加成分数**）

| 维度 Dimension | 问题 Question |
|---|---|
| 澄清 Clarification | 是否解决了关键的模糊点？ |
| 推理 Reasoning | 解释是否把契约连到选择？ |
| 正确性 Correctness | 结果是否满足约定契约？（设计题 = 与约定契约一致，不是像某张偏好的图） |
| 验证 Verification | 实际运行了哪些检查、结果如何？ |
| 沟通 Communication | 观察者能否跟上决定、变化与局限？ |
| 判断 Judgment | 是否尊重权限、不确定性与真实声明？ |

- 写 "Described an empty-input test but didn't run it"，不写 "Good testing"；写 "Filtered to active events before choosing the latest"，不写 "Weak SQL"。
- **诊断"SQL 弱"前先分离语法与顺序逻辑**：不写 SQL 问 "With an active event at 09:00 and an inactive one at 10:00, which row decides the device's state, and when should the active filter apply?" → 仍先过滤 = 契约与顺序推理问题；答对但写错查询 = 查询构建问题。
- 按后果、跨站复发频率、与下一个已确认轮次的相关性排序缺口；**严重的授权或诚实错误即使只见一次也优先**。"多刷算法"不针对观察到的行为。

| 优先级 Priority | 证据 Evidence | 练习 Drill | 改善条件 Improvement condition | 后备 Fallback |
|---|---|---|---|---|
| 契约与顺序推理 | SQL 提升了旧行；API 没有明确计数规则 | 编码前用一句话说出贡献规则；先不用 SQL 解两行 latest-status 例子再翻译 | 独立选择全部状态中的最新事件再过滤，保留零区域 | 推理对但 SQL 错 → 换查询构建练习 |
| 完成与验证 | API 提前停止；调试修复无回归检查；编码检查不完整 | 每个练习留时间做普通、边界、失败三类区分性用例 | 独立运行这些检查并说出仍未测试的部分 | 重测失败 → 用一次新尝试替换一个维护块 |

- **重读参考答案只是为下一次尝试做准备，不是改善的证据**。

**14 天计划 / Fourteen-day plan**（第 3–11 天每天 75 分钟：约 15 评审证据 + 45 实做 + 15 检查与排期）

| 日 Day | 重点 Focus | 分钟 |
|---|---|---:|
| 1 | 基线：recruiter、筛选、拆解、学习 | 185 |
| 2 | 基线：调试、编码、设计、行为与 HM | 165 |
| 3 | 无 SQL 的顺序探测 → 最新记录计数 + 零区域 | 75 |
| 4 | API 完成：token 耗尽 (exhaustion)、去重 (deduplication)、429 恢复、有界失败 | 75 |
| 5 | 新的带符号聚合 + 一个按证据选的算法模式 | 75 |
| 6 | 有界拆解 + 小型需求变更编码题 | 75 |
| 7 | 未见过的 SQL 与 API 重测 + 缓存回归探测 | 75 |
| 8 | 陌生文档与调试，要求失败路径检查 | 75 |
| 9 | 运营设计：所有权、授权、陈旧状态、丢失响应 | 75 |
| 10 | 行为：动机、失败、pushback、伦理、项目追问 | 75 |
| 11 | 修复第 7 天最弱的行为 + recruiter 与 HM 问题 | 75 |
| 12 | 换题的第 1 天类别新模拟 | 185 |
| 13 | 换题的第 2 天类别新模拟 | 165 |
| 14 | 比较证据、写就绪陈述、确认安排 | 60 |
| | **合计** 350 + 9×75 + 350 + 60 | **1,435** |

- 日历变化：每天的真实面试标 confirmed（有证据）/ reported / unresolved；**练习时段不是面试确认**；学习面试确认在第 6 天 → 把文档练习与新的学习重测提前（不说明 SQL 会不会出现）；每天只有 45 分钟 → 14 × 45 = 630，放不下 → 拆分长站、尽量保持每题时间预算、记录失去的覆盖；第 7 天后某优先项仍失败 → 用低价值块换一次针对性尝试 + 新重测。
- 新模拟示例：API 页 1 Q1=6、Q2=10、token U；页 U 重复 Q2、加 Q3=5 → 独立到达终点，Q2 计一次，返回 21，并跑冲突与重试耗尽检查。SQL：E1 同一时间有 active 与 inactive（event 11 inactive）→ 平局选 11 并排除 E1；E2 计入；E3 区域保持 0。

> **Bounded readiness statement (English)**: "I independently demonstrated complete token retrieval, latest-before-status selection and cache regression checks on fresh tasks. My decomposition scope was clear, but I didn't test its outcome assumptions. I explained authorization checks but didn't fully challenge them. My next action is a stale-scope design probe before my confirmed design conversation."

- 三个站不住的声称：把参考例子当自己的证据；把练习时段当已确认面试；重测发生前就填入重测结果。

---

## 速查 / Cheat sheet

| # | 要点（中文） | Takeaway (English) |
|---|---|---|
| 1 | 拆解先问"谁根据结果行动、他能改变什么"；有后果的问题 = 不同答案会导向不同设计 | Open with "Who acts on this, and what can they change?" — a good question has answers that change the design. |
| 2 | 框架放心里（clarify → scope → model → design → iterate / 五遍），嘴上讲具体因果决定 | Keep the framework private; narrate causal decisions out loud. |
| 3 | 薄切片 = 有边界、端到端、独立有用；说出排除项；最早截止等是临时策略 | A thin slice is bounded, end-to-end and useful alone; state exclusions and call simple policies provisional. |
| 4 | 假设被推翻时：向后改资格/模型，向前改输出；被阻止的记录保留可见，不默认通过 | When an assumption breaks, repair eligibility and output; keep blocked records visible, never default them to approved. |
| 5 | 观测 ≠ 识别；零 ≠ 不存在；缺失 ≠ 0；记录状态 ≠ 当前现实 | Observation ≠ identification; zero isn't absence; missing isn't zero; recorded status isn't current reality. |
| 6 | 新鲜度 = 已提交的源覆盖（complete-through），不是心跳或 HTTP 200；延迟 ≠ 新鲜度 | Freshness is committed source coverage, not a heartbeat or a 200; latency is not freshness. |
| 7 | 按字段划分权威；按每源修订号排序（不按到达时间/时间戳）；同修订不同内容 → 隔离 | Field-level ownership; order by per-source revision, never arrival time; same revision with different content is quarantined. |
| 8 | 写操作：鉴权 → 重放键 → 期望版本 → 原子写 + 审计 → 提交后才返回 | Writes: authorize → replay key → expected version → atomic write + audit → respond after commit. |
| 9 | 进度（cursor + 覆盖）与数据同事务提交，提交后才确认；租约 + generation 隔离旧 worker | Commit cursor and coverage with the data, ack after commit; fence stale workers with lease + claim generation. |
| 10 | 丢失响应 = unknown；同 key 重试只在目标端原子存结果时有效；否则保存快照、人工对账，不承诺 exactly-once | A lost response is "unknown"; same-key retry works only if the target stores the key's result atomically — otherwise snapshot and reconcile. |
| 11 | 输出安全：服务端按当前权限过滤 + 字段投影；导出在生成与获取时都重新授权；不承诺匿名 | Server-side scope filter + field projection; re-authorize exports at generation and download; never promise anonymity. |
| 12 | 学习轮：把需求路由到管它的契约；说出带入的熟悉假设；纠正后在变化用例上演示新规则 | Learning round: route each requirement to its contract, name your imported assumption, re-apply the corrected rule to a changed case. |
| 13 | 扫描上限按检查位置推进；短页 ≠ 结束；先选当前状态再过滤 | Scan limits advance by positions examined; a short page isn't the end; select current state before filtering. |
| 14 | 并发：worker 只返回值，单一协调者取每个结果，全成功才整体发布；wait 不抛异常，result() 才抛；用事件不用 sleep 测 | Workers return values; one coordinator inspects every result and publishes all-or-nothing; wait() doesn't raise, result() does; test with events, not sleeps. |
| 15 | 调试：契约 → 保留共享状态复现 → 调用路径 → 最早分歧点 → 可证伪预测 → 根因最小修复 + 回归测试 | Debug: contract → faithful repro with shared state → call path → earliest divergence → falsifiable prediction → minimal root-cause fix + regression tests. |
| 16 | 常见 bug：缓存 key 漏维度、每次重置累加器、发现≠就绪（Kahn 用入度归零）、扩展后才标记 visited、状态生命周期过长、真值判断代替成员判断 | Classic bugs: missing cache-key dimension, accumulator reset, discovery ≠ readiness, marking after expansion, state outliving its scope, truthiness instead of membership. |
| 17 | 编码：先校验参数再扫描；先全局排序再切片；返回新字典投影；完整有序断言 + 空输入 + 深拷贝不变 | Validate before scanning; sort globally before slicing; return fresh projections; assert full ordered output, empty input and no mutation. |
| 18 | 需求变更：确认增量 → 先只重构并跑原测试 → 再扩展；只退役被改变的那条检查；时间不够就诚实汇报已执行/未执行 | Changing requirements: confirm the delta, refactor-only checkpoint on the old suite, then extend; retire only the check the change invalidates. |
| 19 | 系统设计：先讲一个请求的完整路径与不变量；估算只定义测试负载，不证明容量；简单基线 + 说出重新考虑的触发器 | Trace one request and its invariant first; estimates define a test workload, not capacity; defend a simple baseline with explicit reconsider triggers. |
| 20 | 行为题：个人决定 + 当时信息 + 受影响的人 + 观察后果；修复 ≠ 行为改变；结果有边界（重叠未知不相加、无基线不说更快）；谁有决定权说清楚 | Behavioral: your decision, what you knew, who was affected, the observed consequence; repair ≠ changed behavior; bound results; name who had authority. |
| 21 | HM 终面 / offer：先澄清问题意图；"当时发生 / 现在理解 / 之后检查"分开；硬性要求先于总包；sign-on 修不了 base；日期分清估计与截止 | HM final & offer: clarify intent first; separate then / now / checked since; hard requirements before totals; sign-on doesn't fix base; separate estimates from deadlines. |
