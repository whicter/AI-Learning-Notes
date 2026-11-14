# FDE Interview Fundamentals & Integration Patterns｜FDE 面试基础与系统集成模式

> Course: Forward Deployed Engineer for AI Systems (Educative) — Lessons 15–25

---

## 15. How FDE Interviews Work｜FDE 面试如何运作

Source: https://www.educative.io/courses/forward-deployed-engineer/how-fde-interviews-work

### 要点 / Key ideas

- 技术准备是基础：**编码轮 (coding round)** 考实用 AI 系统技能；**技术深挖 (technical deep dive)** 考架构决策、评估方法、可观测性 (observability) 策略。
- 多数 AI 工程师没练过的是技术范围之外的两轮：**拆解轮 (decomposition round)** —— 唯一输入是模糊的企业问题，"第一个问的问题比第一个提出的系统更重要"；**客户模拟轮 (customer simulation round)** —— 面试官扮演企业买家，候选人主持调研会。

**FDE 面试考的三个维度 (three evaluation dimensions)**：

| 维度 Dimension | 含义 Meaning | 出现在 Surfaces in | 关键点 What interviewers watch |
|---|---|---|---|
| 技术深度 Technical depth | 设计和部署生产 AI 系统的能力，基线要求 | 编码轮、技术深挖 | 在 **部署情境 (deployment context)** 下回答：RAG 题是问"为这个客户环境怎么做检索、哪种分块 (chunking)/嵌入 (embedding) 适合他们数据、怎么评估够不够上生产"；agent 题是问怎么埋点、护栏 (guardrails) 边界、客户能运营的可观测性。抽象回答 = 没抓住 FDE 框架 |
| 部署思维 Deployment thinking | 处理没有清晰规格的问题 | 拆解轮、方案设计轮 | 是否先停下来问澄清问题再设计；区分"客户说了什么"与"客户真正需要什么" |
| 面向客户的沟通 Client-facing communication | 主持调研、挖出真实问题、用非技术干系人 (stakeholders) 能行动的语言解释权衡 | 客户模拟轮（SWE/AI 工程师面试都没有） | 不看是否知道正确方案，而看问题能否暴露真实约束、是否避免过早设计、能否以客户认可的问题陈述收尾 |

- **部署思维反例**：物流公司想减少发货延误 → 立刻讲多 agent 架构。跳过了最重要的问题：发货数据能否访问？谁有权批准自动化决策？当前手工流程是什么样？错误自动决策的代价是什么？

**SWE vs AI 工程师 vs FDE 面试对比**：

| 维度 Dimension | 软件工程师 SWE | AI 工程师 AI Engineer | FDE |
|---|---|---|---|
| 问题类型 Problem type | 定义清晰、一个正确答案 | 期望技术精确 | 模糊企业场景，**推理过程即信号** |
| 编码重点 Coding focus | 算法：数组、图、动态规划 (dynamic programming) | 应用：RAG 流水线、agent 流程、评估 | 应用且场景化：数据处理、API 集成、SQL |
| 系统设计 System design | 规模与基础设施 | AI 系统架构 | **企业集成**：合规 (compliance)、访问控制 (access control)、遗留系统 (legacy systems) |
| 独有轮次 Unique rounds | 无 | 无 | 拆解轮、客户模拟轮 |
| 行为重点 Behavioral focus | 团队协作、技术决策 | 同 SWE | 客户所有权 (client ownership)、生产问责、处理模糊 |
| 沟通考察 Communication testing | 极少 | 极少 | 专门的客户模拟轮 |

- 从 SWE/AI 工程师背景来的最大结构差异是 **问题类型**：FDE 拆解和方案设计轮 **故意给模糊提示**，评估是否问必要问题、拆成连贯子问题、在定方向前阐明权衡 —— 正是现场调研的核心行为。

**面试前研究四个方面 (what to research)** —— 在招聘电话前花 2–3 小时：

| 领域 Area | 研究什么 What to learn | 如何用 How it helps |
|---|---|---|
| 公司部署模式 Deployment model | FDE 如何嵌入客户、公开案例中的行业/客户类型、完整项目长什么样 | 系统设计答案反映这些具体环境 |
| AI 产品与 FDE 定位 AI product &amp; FDE's position | FDE 端到端拥有什么、离产品/研究团队多近、现场观察如何反哺路线图 | 按公司实际产品和工具设计，不设计公司不支持的架构 |
| 公开技术内容 Published technical content | 工程博客、案例、演讲 | 常写评估 → 技术轮重评估；常写企业安全 → 系统设计带合规约束 |
| 职位描述 Job postings | 技术栈、客户类型、成功 FDE 交付什么的措辞 | 预判部署面、系统设计场景、公司看重什么 |

### 面试怎么说 / How to say it in the interview

**Q: Why FDE rather than a pure SWE or AI engineering role? / 为什么选 FDE？**
> "I've spent my career building production systems, and the part I'm best at is the messy middle — taking an ambiguous problem, figuring out what the customer actually needs, and shipping something that holds up in their environment. FDE is the role where that's the job, not a side skill. I like that success is measured by whether the customer relies on the system, not whether a ticket closed."
>
> 中文：擅长从模糊问题到可落地系统；FDE 以客户是否依赖系统为成功标准。

**Q (opening any vague design prompt): "A logistics company wants to reduce shipment delays."**
> "Before I propose anything, I'd like to understand a few things. Is the shipment and carrier data accessible to us, and in what form? What does the team do today when a delay is detected? Who has authority to approve an automated rerouting decision? And what does a wrong automated decision cost — a missed delivery window, a penalty, a lost customer?"
>
> 中文：先问数据可访问性、当前手工流程、决策授权、错误决策代价。

---

## 16. The Four Interview Rounds｜四种面试轮次

Source: https://www.educative.io/courses/forward-deployed-engineer/the-four-interview-rounds

### 要点 / Key ideas

- FDE 面试一般 **4–6 轮、3–5 周**；有的公司合并。四种核心轮次：拆解轮、客户模拟轮、技术轮、行为轮。

<svg viewBox="0 0 780 230" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="780" height="230" fill="#fff"/>
  <text x="390" y="22" font-size="15" text-anchor="middle" font-weight="bold">Four Core FDE Rounds｜四种核心轮次</text>
  <g font-size="12" text-anchor="middle">
    <rect x="15" y="45" width="180" height="150" rx="10" fill="#e8f0fe" stroke="#3367d6"/>
    <text x="105" y="70" font-weight="bold">Decomposition</text><text x="105" y="88">拆解轮 · 60 min</text>
    <text x="105" y="118" font-size="11">vague problem →</text><text x="105" y="134" font-size="11">clear problem statement</text>
    <text x="105" y="164" font-size="11" fill="#c5221f">fail: jumps to model</text>
    <rect x="207" y="45" width="180" height="150" rx="10" fill="#fef7e0" stroke="#e37400"/>
    <text x="297" y="70" font-weight="bold">Customer simulation</text><text x="297" y="88">客户模拟 · 45–60 min</text>
    <text x="297" y="118" font-size="11">live discovery with</text><text x="297" y="134" font-size="11">"VP Eng / Head of Ops"</text>
    <text x="297" y="164" font-size="11" fill="#c5221f">fail: proposes in 5 min</text>
    <rect x="399" y="45" width="180" height="150" rx="10" fill="#e6f4ea" stroke="#137333"/>
    <text x="489" y="70" font-weight="bold">Technical</text><text x="489" y="88">技术轮 · 3–5 h</text>
    <text x="489" y="118" font-size="11">coding + deep dive</text><text x="489" y="134" font-size="11">编码 + 系统深挖</text>
    <text x="489" y="164" font-size="11" fill="#c5221f">fail: eval as footnote</text>
    <rect x="591" y="45" width="175" height="150" rx="10" fill="#fce8e6" stroke="#c5221f"/>
    <text x="678" y="70" font-weight="bold">Behavioral</text><text x="678" y="88">行为轮 · STAR</text>
    <text x="678" y="118" font-size="11">customer-facing</text><text x="678" y="134" font-size="11">judgment 客户判断</text>
    <text x="678" y="164" font-size="11" fill="#c5221f">fail: customer as backdrop</text>
  </g>
  <text x="390" y="218" font-size="12" text-anchor="middle" fill="#444">Same orientation from four angles: keep the customer's problem at the center｜四个角度，同一核心：客户问题居中</text>
</svg>

### 16.1 拆解轮 (Decomposition round)

- 给一个无定义范围、无唯一正确答案的模糊企业问题，**60 分钟**。例：医疗网络如何减少医生每天 2 小时临床文档时间；金融公司如何自动化每份 3–4 天的贷款审核；零售公司如何处理团队已处理不了的每日 10,000 张工单。
- 评估：提方案前是否问澄清问题、拆解是否干净、是否区分 **根因与症状 (root causes vs symptoms)**、是否以清晰问题陈述收尾。

| 阶段 Phase | 时长 Duration | 重点 Focus |
|---|---|---|
| 澄清问题 Clarifying questions | 10 min | 用户、数据可用性、决策权限、成功指标 |
| 问题拆解 Problem decomposition | 15 min | 拆成具体子问题 |
| 约束与优先级 Constraints &amp; prioritization | 15 min | 什么塑造架构、先建什么 |
| 权衡讨论 Tradeoff discussion | 10 min | 列出备选方案及各自代价 |
| 呈现总结 Present back | 10 min | 清晰问题陈述 + 建议方向 |

- **澄清阶段权重最大**：在提任何模型/架构前确定用户是谁、有什么数据什么格式、当前手工流程、生产可接受的准确率/延迟阈值。
- **当前变体**：拆解后延伸到 agentic 系统设计 —— 命名工具、定义编排模式、描述生产中如何评估。
- **拒绝信号 (rejection signals)**：问题没理解就跳到模型/架构；把问题描述当成完全定义；结尾的问题陈述不比开头的描述更具体。

**示例题 (sample prompt) — English statement**: *A financial services company wants to automate loan application review, which currently takes underwriters 3–4 days per file. Decompose the problem.*

示范拆解（按 60 分钟结构）：
1. **澄清**："Which part of the 3–4 days is active work versus waiting on documents? What document types arrive — pay stubs, bank statements, tax returns? Is there labeled history of approved/declined files? Who must sign off on a decision, and are there fair-lending rules on explainability?"
2. **子问题**：文档收集与完整性检查 → 字段抽取（收入、负债）→ 规则/政策核对 → 风险判断 → 审批人复核与记录。
3. **约束与优先级**：监管要求决策可解释 (explainable)、人必须最终决定 → 先做 **抽取 + 完整性检查**（最大耗时、风险最低），不做自动批准。
4. **权衡**：结构化 LLM 抽取 vs 微调 (fine-tuning) 抽取模型（有标注数据时）；全自动 vs 人在回路 (human-in-the-loop)（合规 (compliance) 要求后者）。
5. **呈现**："The real bottleneck is underwriters manually extracting and cross-checking figures across six document types; a system that extracts and reconciles those fields with citations, leaving the decision to the underwriter, targets roughly X of the 3–4 days."

### 16.2 客户模拟轮 (Customer simulation round)

- 面试官扮演企业客户（常为 **工程副总裁 VP of Engineering** 或 **运营负责人 Head of Operations**），候选人主持 **45–60 分钟** 调研会。场景：AI 能否改善慢的内部流程；大量重复工作是否值得自动化；如何从已有数据中获得更多价值。
- 评估：提方案前的 **克制 (restraint)**、调研问题能否暴露真实约束、能否以客户认可的问题陈述收尾。**是 FDE 招聘中权重最高的轮次之一**，最直接复现第一天的工作。
- 结构：不带任何提案开场，先请客户描述当前流程（什么触发问题、谁处理、哪里实际崩）。覆盖四个领域：

| 领域 Area | 关键问题 Key question |
|---|---|
| 流程与痛点 Workflow &amp; pain | 当前流程是什么、哪里失败最明显？ |
| 数据与系统 Data &amp; systems | 有什么数据、在哪、谁控制访问？ |
| 约束与权限 Constraints &amp; authority | 合规/安全要求？谁批准系统做什么？ |
| 成功定义 Success definition | 六个月后成功的结果是什么样？ |

然后进入 **综合 (synthesis)**：总结所听到的，给出提炼后的问题陈述，会话在此结束。
- **拒绝信号**：前五分钟就提架构；附和客户而不质疑约束；没有以清晰综合的问题陈述收尾。

### 16.3 技术轮 (Technical round)

- 通常 **3–5 小时**，两种形式：编码评估 + 技术深挖（同场或分开）。
- **编码评估** 典型任务：清洗数据集准备模型摄取；调用 LLM API 并处理 **流式响应 (streaming responses)** 与错误；构建分块 (chunking) + 嵌入 (embedding) 的检索组件；实现衡量输出质量的评估脚本；在定义范围内端到端构建小 AI 功能。
- 有的公司用 **take-home + 录制讲解 (recorded walkthrough)**：讲解与代码同等权重 —— 建了什么、为什么、失败模式是什么。

```python
# Typical coding task: call an LLM with streaming, retries, and error handling (illustrative)
import time

class TransientError(Exception):
    pass

def stream_completion(client, prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            chunks = []
            for event in client.stream(prompt=prompt, timeout=30):
                if event.type == "text_delta":
                    chunks.append(event.text)
            return "".join(chunks)
        except TransientError:
            time.sleep(2 ** attempt)  # exponential backoff
    raise RuntimeError("LLM call failed after retries")
```

- **技术深挖** 通用方法（四步）：
  1. **从问题开始**：命名模型/框架前，先确定系统要做什么、有什么数据、成功阈值。
  2. **架构匹配问题**（见下表）。
  3. **考虑企业约束**：**数据驻留 (data residency)**、合规标准、访问控制、遗留系统 (legacy systems) 集成。忽略这些 = 没抓住 FDE 框架。
  4. **部署前定义评估**：好输出是什么、怎么测、生产可接受阈值。评估是设计决策，不是事后补充。

| 问题 Problem | 架构 Architectural approach |
|---|---|
| 大型内部文档库问答 | RAG（检索层 + 生成层） |
| 有标注数据的领域文档结构化抽取 | 在标注样本上微调的模型 |
| 需要工具和条件路由的多步流程 | 单 agent 或多 agent 编排 |
| 大批量分类/路由 | 约束输出格式的结构化 LLM 调用 |
| 检索 + agentic 工具使用结合 | 混合 RAG + agentic 架构 (hybrid) |

- 架构只是起点；面试官同样评估选择背后的推理。
- **拒绝信号**：未确定需求就命名架构；设计不考虑企业约束；把评估当脚注。

### 16.4 行为轮 (Behavioral round)

- 结构化过往经历面试，**STAR**（Situation 情境、Task 任务、Action 行动、Result 结果）。不同于普通工程行为轮（技术判断、团队协作），FDE 行为轮考 **面向客户的判断**：部署失败、客户反对、范围扩张 (scope creep)、AI 在干系人 (stakeholders) 面前出错时你怎么做。
- STAR 每个元素都以 **客户和约束** 为中心：Situation 说清客户、项目背景、难在哪；Task 说要解决的约束；Action 讲 **判断**（为什么选这个而非其他）而不只是执行；**Result 权重最大** —— 必须说明客户那边具体改变了什么，而不只是技术里程碑。
- 有的公司加价值观/文化维度：看是否真正面对权衡，而非背准备好的答案。
- **拒绝信号**：客户只是背景板；结果只讲技术里程碑；只讲发生了什么、不讲做了什么决定和为什么。

### 面试怎么说 / How to say it in the interview

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 33 篇）。

**Q: Tell us about a time you stopped a project and communicated that decision to a customer. / 讲一次你叫停项目并告知客户的经历**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 33 篇）。

**Q: Describe a deployment that went wrong. What happened and what did you do? / 讲一次上线出问题**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 33 篇）。

**Q: Tell us about a time you pushed back on scope creep from a stakeholder. / 讲一次你顶住范围扩张**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 33 篇）。

**Q: Describe a time you explained an AI failure to a non-technical executive. / 讲一次向非技术高管解释 AI 出错**

> 🔒 这里原本是本人真实经历的回答，已隐去。完整版本只保留在本地（project_deep_dive 第 33 篇）。

**Q: How do you approach an AI system design question in a technical deep dive?**
> "I go in four steps. First the problem — what the system must do, what data exists, and the success threshold. Then I match architecture to the problem signal — RAG for a large corpus, a constrained LLM call for classification, an agent only if there's real multi-step tool use. Then enterprise constraints: data residency, compliance, access control, legacy integration. And I define evaluation before deployment, because that's a design decision, not a footnote."
>
> 中文：问题 → 匹配架构 → 企业约束 → 部署前定义评估。

---

## 17. How FDE System Design Rounds Work｜FDE 系统设计轮如何运作

Source: https://www.educative.io/courses/forward-deployed-engineer/how-fde-system-design-rounds-work

### 要点 / Key ideas

- FDE 与客户一起理解重要工作流、连接相关系统和信息、把方案带进生产并产生 **可衡量业务结果 (measurable business outcomes)**。FDE 系统设计 = 把这项工作变成扎根于客户工具、数据、运营约束的技术提案；面试中通常是技术深挖的 **集成密集版 (integration-heavy version)**。
- **难点很少是选模型或框架**，而是在别人定的规则下连接客户已有系统，并清楚解释推理。AI 只是一种应用；很多集成问题 **根本不需要 AI**，设计轮同样对待。
- FDE 工作链：做关键工作的人（派修、对账、回答客户）→ 现有系统各持部分信息但连接不完整 → 与客户一起调查 → 建连接方案 → 投入使用 → 验证结果是否改善。**权限 (permissions)** 决定可用信息和动作；**部署边界 (deployment boundaries)** 决定软件能跑在哪、能访问哪些系统。解决模糊性本身就是工程工作。

**示例：维修派单 (maintenance dispatch)**
- 请求："Help dispatchers assign urgent repair jobs faster." 已有 **工单跟踪器 (job tracker)** 和 **技师名册 (technician roster)**。
- 有用的开场问题是 **答案可能改变方案** 的问题：
  - "What causes the delay today?" → 可能发现派单员找不到合适技师。
  - "What access is available?" → 可能发现集成无法更新工单。
- 面试官给出的事实：
  - 当前紧急工单出现到派单的 **中位时间 30 分钟**，目标 **10 分钟**。
  - 工单跟踪器访问 **只读 (read-only)**。
  - 技师可用性是 **每小时导出 (hourly export)**。
  - **派单员必须批准分配 (dispatchers must approve assignments)**。
- 解读："更快" 有了可衡量含义（派单时间，不是维修完成时间）；读权限支持查看但不代表能修改；每小时名册是 **最近快照 (recent snapshot)**，不是当前可用性的证明；必需审批保留派单员决策角色。
- 课程审计练习要点（memo 里的错误说法）：① "客户命名了两个系统，所以自动分配服务可行" —— 错，命名系统 ≠ 集成可行；② "某指南建议先选组件再问流程" —— 错，引用不实；③ "强制标准要求开场问题必须提数据库或消息队列 (message queue)" —— 虚构权威。正确结论：好的开场问题是 **其答案能改变提案** 的问题。

**传统系统设计 vs FDE 系统设计**：

| 维度 Dimension | 传统 Traditional System Design | FDE System Design |
|---|---|---|
| 起点 Starting point | 要构建的产品（短链、聊天服务） | 一个客户需要改进的工作流 |
| 主要约束 Main constraint | 规模、延迟、可用性 | 现有系统、访问规则、数据质量、截止日期 (deadline) |
| 数据 Data | 从零设计 | 已存在于客户系统和格式中 |
| 典型难点 Typical hard part | 分片、缓存、复制 (sharding, caching, replication) | 认证 (authentication) 不匹配、**限流 (rate limits)**、脏数据 (dirty data) 或迟到数据 |
| 成功衡量 Success measure | 系统扛住目标负载 | 工作流可衡量地改善 |
| 期望的第一个回答 Expected first answer | 高层架构 | **澄清问题，然后有范围的第一版** |

- 经典关注点不消失（规模、存储、可靠性仍重要），只是不再是起点。
- 候选人报告的 FDE 设计题 **五种类型**：① 连接从未设计为协同的系统；② 加载脏/遗留数据 (legacy data)；③ 严格 API 限制下设计；④ 开放式运营问题；⑤ 为业务流程构建 AI agent。
- 知道某机制（如 **流式 streaming**）≠ 知道客户接口与新鲜度需求是否值得用它 —— 这种判断才是被考的。
- **开放问题 vs 命名系统**："Design a repair-job tracking service"（命名系统）vs "Help dispatchers assign urgent jobs faster using their current tools"（问题定义部分开放；也许需要的是跨现有工具的更好视图而非替代跟踪服务）。"decomposition / customer scenario / case study / architecture" 等标签会重叠，标签本身不说明期望。

**有边界的开场 (bounded opening) — 范例**：
> "The goal is to reduce median urgent-job assignment time from 30 minutes to 10. I would first explore showing urgent jobs alongside the latest available technician roster for dispatcher review, while leaving approval with dispatchers. With read-only job access and hourly availability exports, I would not claim live availability or automatic writes. Is read access sufficient for a first useful version in which dispatchers continue assigning jobs through their current workflow?"

面试官能观察到的推理动作：

| 动作 Action | 体现 What it shows |
|---|---|
| 定义收益 Define the benefit | 问"更快"是什么 → 得到派单时间目标 |
| 测试可行性 Test feasibility | 问访问权限 → 检查连接能否支持预期动作 |
| 暴露不确定性 Expose uncertainty | 称名册为"最新可用" → 承认新鲜度局限 |
| 尊重工作流 Respect the workflow | 保留派单员审批 → 不悄悄改变运营政策 |
| 区分事实与假设 Separate facts from assumptions | 问只读第一版是否有用 → 把判断留给客户 |

- 这些（相关问题、显式假设、可构建拆解、有用初始范围、关注障碍）是 **实用准备标准**，不是雇主公布的统一评分标准。
- **拒绝信号**：问需求/现有系统允许什么之前就提组件；把命名系统当集成可行的证明；声称事实不支持的实时数据、写权限或结果；忽视已确立约束（如必需的人工审批）。

**为什么"先上炫架构"不行**：
- 反例："I'll stream technician locations into an automatic assignment engine and write the selected technician back to each urgent job. That should get assignment time down to 10 minutes."
- 测验正确答案 (B)：它假设了事实不支持的 **实时数据流和写权限**，**绕过了必需的派单员审批**，并把 10 分钟目标当成已证明结果。（A 错：不是存储容量问题；C 错：流式并非永远不适合，取决于接口与权限。）
- 三个问题需不同回应：实时数据和写权限是 **未验证能力 (unverified capabilities)**；派单员审批是 **已确立约束 (established constraint)**；10 分钟是 **待验证假设 (hypothesis)**，不是架构能保证的结果。
- 更好的回应先撤回不受支持的说法："I assumed live data and write access that we have not established. Given the hourly roster and required approval, I would start with dispatcher review of urgent jobs and the latest roster. I still need to confirm whether that view addresses the actual delay and whether it can fit into the existing assignment workflow." —— 组件更少，但能力与收益的连接更清晰。

**向招聘方确认轮次形式 (confirm the round format with the recruiter)**：

| 类别 Category | 问法 Question to ask |
|---|---|
| 形式 Format | "Does the round begin with an open business problem or a specified system? How collaborative is it?" |
| 时长 Timing | "How long does it last, and does that include a presentation?" |
| 产物与工具 Artifacts &amp; tools | "Should I produce a diagram, verbal proposal, written plan, code, or a combination? Which tools are permitted?" |
| 评估指导 Evaluation guidance | "Which competencies should I demonstrate, and are there preparation materials you can share?" |

**练习：仓库拣货 (warehouse practice)**
- English prompt: *A warehouse wants pickers to spend less time walking. Inventory data is split across two tools, both provide daily exports, pickers use an existing handheld application, and replacing that application is out of scope.*
- 两个澄清问题："Which parts of a picking trip cause the most unnecessary walking, and what reduction would count as success?" / "Can the handheld application receive recommendations from another system?"
- 一个未验证假设：手持应用能接收外部生成的推荐。
- 两句话解释："We do not yet know which workflow change would reduce walking or whether the existing handheld application can support it. Daily exports do not establish live inventory access, so choosing streaming infrastructure now would assume an interface we have not confirmed."
- memo 中的错误说法：把维修例子的派单员审批套到仓库（无依据）；虚构"手持集成标准保证可接收推荐"；"每日导出足以立即选实时库存流" —— 均不成立。

<svg viewBox="0 0 760 220" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="760" height="220" fill="#fff"/>
  <text x="380" y="22" font-size="15" text-anchor="middle" font-weight="bold">Facts decide the design｜事实决定设计（维修派单）</text>
  <g font-size="12" text-anchor="middle">
    <rect x="20" y="45" width="220" height="150" rx="8" fill="#f1f3f4" stroke="#5f6368"/>
    <text x="130" y="68" font-weight="bold">Supplied facts 已知事实</text>
    <text x="130" y="92" font-size="11">median 30 → target 10 min</text>
    <text x="130" y="112" font-size="11">job tracker: read-only</text>
    <text x="130" y="132" font-size="11">roster: hourly export</text>
    <text x="130" y="152" font-size="11">dispatcher must approve</text>
    <rect x="270" y="45" width="220" height="70" rx="8" fill="#fce8e6" stroke="#c5221f"/>
    <text x="380" y="68" font-weight="bold">Rejected 否决</text>
    <text x="380" y="88" font-size="11">stream locations + auto-assign</text>
    <text x="380" y="104" font-size="11">+ write back (no evidence)</text>
    <rect x="270" y="125" width="220" height="70" rx="8" fill="#e6f4ea" stroke="#137333"/>
    <text x="380" y="148" font-weight="bold">First version 第一版</text>
    <text x="380" y="168" font-size="11">urgent jobs + latest roster view</text>
    <text x="380" y="184" font-size="11">dispatcher approves in current tool</text>
    <rect x="520" y="85" width="220" height="70" rx="8" fill="#fef7e0" stroke="#e37400"/>
    <text x="630" y="108" font-weight="bold">Open question 待确认</text>
    <text x="630" y="128" font-size="11">does this view fix the actual</text>
    <text x="630" y="144" font-size="11">delay? 是否解决真实延迟</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="240" y1="90" x2="268" y2="80"/><line x1="240" y1="150" x2="268" y2="160"/>
    <line x1="490" y1="160" x2="518" y2="130"/>
  </g>
</svg>

### 面试怎么说 / How to say it in the interview

**Q: How is an FDE system design round different from a classic one? / 与传统系统设计有何不同？**
> "A classic round starts with a product to build at scale, so the hard parts are sharding and caching. An FDE round starts with one customer's workflow and the systems they already run, so the hard parts are auth mismatches, rate limits, and messy or late data. My first answer isn't an architecture — it's the questions whose answers could change the design, then a scoped first version their current systems can actually support."
>
> 中文：传统从产品与规模出发；FDE 从客户工作流与现有系统出发；第一回答是能改变设计的问题 + 有范围的第一版。

**Q (prompt): "Help dispatchers assign urgent repair jobs faster."**
> "Before choosing anything, two questions: what causes the delay today, and what access do we have to the job tracker and roster? … Given the 30-minute median, read-only job access, an hourly roster, and required dispatcher approval, I'd start with a view of urgent jobs next to the latest roster snapshot — clearly timestamped — and keep approval in their current tool. I wouldn't claim live availability or automatic assignment. The 10-minute target is a hypothesis we'd measure in a pilot."
>
> 中文：先问延迟原因和访问权限；按事实给出只读视图 + 保留审批；10 分钟是待验证假设。

**Q: The interviewer pushes back on your streaming design. How do you recover?**
> "I'd say: 'You're right — I assumed live data and write access that we haven't established.' Then I'd rescope to what the facts support and name what I'd still need to confirm. Withdrawing an unsupported claim cleanly is a stronger signal than defending more infrastructure."
>
> 中文：坦然撤回未经证实的假设，按事实重定范围。

**Q: What do you ask the recruiter about the design round?**
> "Whether it starts from an open business problem or a named system, how long it is and whether there's a presentation, what artifact they expect — diagram, written plan, or code — and which competencies they'd like me to demonstrate."
>
> 中文：问形式、时长、产物、评估重点。

---

## 18. The CLIENT Approach for FDE System Design｜FDE 系统设计的 CLIENT 方法（核心框架）

Source: https://www.educative.io/courses/forward-deployed-engineer/the-client-approach-for-fde-system-design

### 要点 / Key ideas

- **CLIENT** = **C**ontext（情境）、**L**andscape（系统全景）、**I**ntegration points（集成点）、**E**nd-to-end design（端到端设计）、**N**on-happy paths（非正常路径）、**T**rade-offs（权衡）。
- 它建立在技术深挖四步法上（从问题开始 → 架构匹配问题 → 企业约束 → 部署前定义评估），并 **补上集成密集轮次最常追问的三块：集成点、失败路径、权衡**。Context 和 Landscape 使用与客户模拟轮相同的四个问题领域（流程与痛点、数据与系统、约束与权限、成功定义）。CLIENT 是本课程的组织清单，**不是雇主官方评分标准**。
- **关键：各步骤输出相互约束 (decisions constrain one another)**。接口检查失败可以把设计打回 scope；填满六个标题不等于可行。

### ⭐ CLIENT 框架总表 / CLIENT framework at a glance

| 步骤 Step | 中文 | 产出 Output | 关键问题 Key questions | 常见错误 Common mistake |
|---|---|---|---|---|
| **C — Context** | 情境 | 工作流、干系人 (stakeholders)、**结果陈述 (outcome statement)**（任务 + 基线 + 目标 + 安全条件）、范围、**非目标 (non-goals)** | Who does the work? What's the obstacle? What does "better" mean, measured how? What must not happen? | 把"更快"留作模糊词；把目标当承诺而非试点假设 |
| **L — Landscape** | 系统全景 | 系统清单：负责人 (owner)、**权威字段 (authoritative fields)**、标识符 (identifiers)、接口、凭证 (credentials)、网络可达性、限制 | Which system owns which fact? What IDs link records? What's read-only? What can't change? | 字段名相同就当含义相同；按名称/邮箱匹配实体 |
| **I — Integration points** | 集成点 | 基于 **接口 + 凭证 + 网络路径** 的连接决策；未知项显式记录 | Is there an API, export, or event feed? What auth? Reachable from where? Rate limit? | 假设存在客户没提供的端点、权限或网络路径（自定义代码补不出来） |
| **E — End-to-end design** | 端到端设计 | 从源信息到 **用户下一步动作** 的连通流程 | What does the user see, and what do they do next, in which tool? | 画了箭头但没落到用户动作；悄悄改变审批/写入流程 |
| **N — Non-happy paths** | 非正常路径 | 对 **缺失、陈旧、冲突、不可用** 信息的系统与用户响应 | What if the ID doesn't map? Data is stale? API is down or rate-limited? | 把缺失/陈旧证据推断成"放行"；缓存 (cache) 冒充当前数据 |
| **T — Trade-offs** | 权衡 | 推荐方案、其代价、备选方案为何在此落选 | Why this over automation/streaming? What do we pay? What would change the answer? | 只列优点；不说什么条件下会改选 |

<svg viewBox="0 0 820 360" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="820" height="360" fill="#fff"/>
  <text x="410" y="24" font-size="16" text-anchor="middle" font-weight="bold">The CLIENT Approach｜CLIENT 方法</text>
  <g font-size="12" text-anchor="middle">
    <rect x="15" y="50" width="120" height="110" rx="10" fill="#e8f0fe" stroke="#3367d6" stroke-width="2"/>
    <text x="75" y="80" font-size="22" font-weight="bold" fill="#3367d6">C</text>
    <text x="75" y="102" font-weight="bold">Context</text><text x="75" y="118">情境</text>
    <text x="75" y="140" font-size="10">outcome · scope</text>
    <rect x="148" y="50" width="120" height="110" rx="10" fill="#e8f0fe" stroke="#3367d6" stroke-width="2"/>
    <text x="208" y="80" font-size="22" font-weight="bold" fill="#3367d6">L</text>
    <text x="208" y="102" font-weight="bold">Landscape</text><text x="208" y="118">系统全景</text>
    <text x="208" y="140" font-size="10">owners · IDs</text>
    <rect x="281" y="50" width="120" height="110" rx="10" fill="#fef7e0" stroke="#e37400" stroke-width="2"/>
    <text x="341" y="80" font-size="22" font-weight="bold" fill="#e37400">I</text>
    <text x="341" y="102" font-weight="bold">Integration</text><text x="341" y="118">集成点</text>
    <text x="341" y="140" font-size="10">interface·auth·network</text>
    <rect x="414" y="50" width="120" height="110" rx="10" fill="#fef7e0" stroke="#e37400" stroke-width="2"/>
    <text x="474" y="80" font-size="22" font-weight="bold" fill="#e37400">E</text>
    <text x="474" y="102" font-weight="bold">End-to-end</text><text x="474" y="118">端到端设计</text>
    <text x="474" y="140" font-size="10">source → user action</text>
    <rect x="547" y="50" width="120" height="110" rx="10" fill="#fce8e6" stroke="#c5221f" stroke-width="2"/>
    <text x="607" y="80" font-size="22" font-weight="bold" fill="#c5221f">N</text>
    <text x="607" y="102" font-weight="bold">Non-happy</text><text x="607" y="118">非正常路径</text>
    <text x="607" y="140" font-size="10">missing·stale·down</text>
    <rect x="680" y="50" width="125" height="110" rx="10" fill="#e6f4ea" stroke="#137333" stroke-width="2"/>
    <text x="742" y="80" font-size="22" font-weight="bold" fill="#137333">T</text>
    <text x="742" y="102" font-weight="bold">Trade-offs</text><text x="742" y="118">权衡</text>
    <text x="742" y="140" font-size="10">pick · cost · why not</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="135" y1="105" x2="146" y2="105"/><line x1="268" y1="105" x2="279" y2="105"/>
    <line x1="401" y1="105" x2="412" y2="105"/><line x1="534" y1="105" x2="545" y2="105"/>
    <line x1="667" y1="105" x2="678" y2="105"/>
    <path d="M341 162 C341 215, 75 215, 75 162" stroke="#c5221f" stroke-dasharray="5,4"/>
    <path d="M742 162 C742 240, 208 240, 208 162" stroke="#c5221f" stroke-dasharray="5,4"/>
  </g>
  <text x="208" y="208" font-size="11" fill="#c5221f" text-anchor="middle">failed interface check → rescope｜接口不通 → 回到范围</text>
  <text x="560" y="236" font-size="11" fill="#c5221f" text-anchor="middle">trade-off reveals ownership gap → revisit landscape｜权衡暴露归属问题 → 回看全景</text>
  <g font-size="11" fill="#444">
    <rect x="15" y="262" width="790" height="86" rx="8" fill="#f8f9fa" stroke="#dadce0"/>
    <text x="30" y="284" font-weight="bold">Maps to case-study lessons｜对应案例课</text>
    <text x="30" y="304">Decomposing the Problem → C + L　｜　System Design → I + E　｜　FDE Interview Questions → N + T</text>
    <text x="30" y="324">Builds on: problem → match architecture → enterprise constraints → eval before deploy（技术深挖四步）</text>
    <text x="30" y="342">C + L reuse the 4 discovery areas: workflow/pain · data/systems · constraints/authority · success</text>
  </g>
</svg>

### 示例：Cedar Rentals 设备就绪屏 (equipment-readiness screen)

**English prompt**: *Cedar Rentals asks for "one equipment-readiness screen so desk staff can prepare handovers faster."*

**C — Context**
- 现状流程：前台找预订 → 在维修导出中查分配资产 → 解决标识符不匹配 → 在现有预订工具中完成 **出租交接 (checkout)**。
- 竞争需求：前台 = 更短交接、更少重复查找；维修 = **未解除的安全扣留 (safety holds)** 必须可见；预订系统负责人 = 集成 **不得写预订**。
- **结果陈述 (outcome statement)**："During a one-branch pilot, reduce median time from starting reservation review to recording checkout from 12 minutes to 5 minutes, without checking out an asset with an unresolved safety hold." —— 包含任务、基线、目标、安全条件；架构提出帮助方式，试点测量确定是否达标。
- 范围：一个门店、为已分配资产展示就绪证据。**排除**：重新分配、自动 checkout、替换任一源应用。

**L — Landscape**

| 系统 System | 负责人 Owner | 权威字段 Authoritative for | 接口 / 凭证 / 网络 Interface · auth · network | 限制 Limits |
|---|---|---|---|---|
| 预订 Reservations | 租赁运营系统团队 rental ops systems | `reservation_id`、`assigned_asset_id`、checkout 状态 | 只读 REST API + 服务 API key；从门店批准的内部应用主机可达 | 60 req/min；无事件、无写入 |
| 维修 Maintenance | 维修团队 | 安全扣留、检查状态 `inspection_status` | 每小时 CSV，内部 SFTP + SSH 服务密钥；同一主机可达 | 无实时查询接口 |
| 资产登记 Asset registry | 车队运营 fleet ops | `asset_id` ↔ `maintenance_tag` 的 **批准对照表 (approved crosswalk)** | 交付方式、刷新频率、纠错流程 → **记为待确认问题** | — |
| 变更限制 Change restrictions | — | — | 两个源应用必须保持不变 | — |

- 还要确定：谁能用此屏、新鲜度如何呈现、各任务需要多新的信息。**每小时导出支持快照 (snapshot) 证据，不能提供实时安全证据。**
- 接口、凭证、网络路径 **三者都要** 支持连接；自定义代码补不出客户没提供的端点、权限或网络路径。

**"ready" vs "HOLD" 冲突 —— 实体身份 vs 字段归属**
- R17 分配 `A0042`，状态 `ready`；登记表 `A0042 → M883`；维修导出 `M883` 的 `inspection_status = HOLD`；另有 `A0043 → M884`。
- 测验正确答案 (C)：**保留两个源值，确认含义与字段级归属，用批准的 A0042→M883 对照表**。（A "取最新时间戳" 错；B "维修对所有字段权威" 错。）
- 即使连接正确，一个合并状态也会把"预订准备"和"设备检查"压成误导性答案。分清两个问题：

| 问题 Question | 含义 Meaning | Cedar 答案 |
|---|---|---|
| 实体身份 Entity identity | 一条记录代表哪个业务对象？ | 稳定标识符 + 批准对照表建立关系 |
| 字段归属 Field ownership | 哪个系统对某属性权威？ | 预订管分配和预订状态；维修管检查和安全状态；车队运营管标识符对应 |

- 展示 **"Booking: Ready"** 与 **"Maintenance inspection: HOLD"** 并列，各带源时间戳，互不覆盖。**单一事实来源 (single source of truth) 可以按事实 (per fact) 适用**，无需让一个应用对资产所有属性权威。
- 设备名称、邮箱会变；字段名相同 ≠ 业务含义相同。系统对同一事实冲突时，定义归属或 **冲突策略 (conflict policy)**；让双方都能覆盖只会保留冲突 —— 跨系统归属争议是公认的集成失败模式。

**I — Integration points + E — End-to-end design**
- 推荐：**内部只读就绪视图 (internal, read-only readiness view)**。实现前确认对照表的交付与刷新细节、如何获取源快照时间。
- 流程：
  1. **导入器 (importer)** 通过 SFTP 读每小时维修 CSV，连同源时间戳载入本地 **读存储 (read store)**；通过确认的机制导入批准对照表。
  2. 前台打开预订时，应用用服务 API key 通过允许的 REST API 取预订。
  3. 通过对照表把 `asset_id` 解析为对应维修证据。
  4. 屏幕分开展示预订状态与维修证据，含时间戳及任何身份/新鲜度警告。
  5. 员工执行必需的实物检查，并在 **现有预订工具** 中记录 checkout。
- 面试官确认：带时间戳的快照对准备有用，但不能单独授权 checkout。这把只读设计和有用工作连起来（减少重复查找，保留 checkout 控制）。如果准备需要实时放行，已确认接口会迫使改范围或要求客户提供额外能力。

<svg viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="800" height="300" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">Cedar Readiness View — End-to-End｜Cedar 就绪视图端到端</text>
  <g font-size="11" text-anchor="middle">
    <rect x="15" y="45" width="160" height="56" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="95" y="66" font-weight="bold">Maintenance</text><text x="95" y="82">hourly CSV · SFTP/SSH</text><text x="95" y="96">无实时接口</text>
    <rect x="15" y="120" width="160" height="56" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="95" y="141" font-weight="bold">Asset registry</text><text x="95" y="157">crosswalk A↔M</text><text x="95" y="171">delivery TBC 待确认</text>
    <rect x="15" y="195" width="160" height="56" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="95" y="216" font-weight="bold">Reservations</text><text x="95" y="232">read-only REST · API key</text><text x="95" y="246">60 req/min · no writes</text>
    <rect x="215" y="75" width="130" height="70" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="280" y="100" font-weight="bold">Importer</text><text x="280" y="116">导入器</text><text x="280" y="132">+ source timestamp</text>
    <rect x="385" y="75" width="130" height="70" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="450" y="100" font-weight="bold">Local read store</text><text x="450" y="116">本地读存储</text>
    <rect x="385" y="185" width="130" height="70" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="450" y="210" font-weight="bold">Readiness app</text><text x="450" y="226">就绪应用</text><text x="450" y="242">join via crosswalk</text>
    <rect x="555" y="150" width="225" height="110" rx="8" fill="#e6f4ea" stroke="#137333"/>
    <text x="667" y="172" font-weight="bold">Screen 屏幕</text>
    <text x="667" y="192">Booking: Ready (ts)</text>
    <text x="667" y="210" fill="#c5221f">Maintenance inspection: HOLD (ts)</text>
    <text x="667" y="228">warnings: identity / stale</text>
    <text x="667" y="248">→ physical check → checkout in existing tool</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="175" y1="73" x2="213" y2="100"/><line x1="175" y1="148" x2="213" y2="120"/>
    <line x1="345" y1="110" x2="383" y2="110"/><line x1="450" y1="145" x2="450" y2="183"/>
    <line x1="175" y1="223" x2="383" y2="220"/><line x1="515" y1="220" x2="553" y2="205"/>
  </g>
  <text x="280" y="215" font-size="10" fill="#444" text-anchor="middle">on open: GET reservation</text>
  <text x="400" y="285" font-size="11" fill="#137333" text-anchor="middle">neither value overwrites the other; checkout stays in the source tool｜互不覆盖，checkout 留在原工具</text>
</svg>

**N — Non-happy paths**

| 失败情况 Failure | 系统行为 System behavior | 用户/流程 User / process |
|---|---|---|
| A0042 无唯一对照 No unique crosswalk | 显示 **"Identity unresolved"** | 差异转给车队运营；**不按设备名猜** |
| 维修证据超过 90 分钟 Evidence older than 90 min | 标记 **stale** | 走现有人工核验 (manual verification) 路径；阈值管显示行为，较新证据也不等于安全放行 |
| 预订 API 不可用或限流 Reservation API down / quota-limited | 显示 **"Reservation could not be refreshed"** | 保留现有源工具流程；缓存的预订状态 **不得显示为当前** |

- 维修 HOLD **无论预订是否 ready 都保持可见**。缺失身份或陈旧证据 **绝不能变成推断出的放行 (inferred clearance)**。
- "拥有数据" ≠ "拥有可用证据"：屏幕可以可用，同时某个决策所需信息仍未解决。
- 课程失败模拟器思想：逐个拿掉支撑条件（可刷新的预订 API、唯一批准对照表、90 分钟内的维修证据、现有 checkout 控制），预测影响范围 —— 爆炸半径 (blast radius) 越大越接近单点故障 (single point of failure)。

**T — Trade-offs**
- 选只读视图：已验证接口支持它，能减少查找工作而不改变源权威。**代价**：重复的读存储、依赖对照表、仍需人工核验。
- 否决自动 checkout 和实时事件流（第一版）：预订写入和事件源都不可用。只有客户提供必要能力和运营许可后它们才成为候选。
- **反例（填满所有 CLIENT 标题但每个决定都错）**："Join on equipment name, copy the newest ready value into a shared status, subscribe to maintenance updates, and write automatic checkout back to reservations." —— 名称不建立身份；R17 的 ready 可能掩盖 M883 的 HOLD；维修没有事件接口；预订写入被禁止。修复：对照表建立身份、保留分开的含义、用提供的导出、checkout 留在现有工具。**加更多组件不会修复这些错误。**
- 最终提案可追溯：业务目标定义测量、归属保护含义、对照表建立身份、接口约束连接、失败响应保持证据诚实。

### 练习：培训报名准备视图 (training enrollment practice)

**English prompt**: *Coordinators take a median of 20 minutes from opening a training-enrollment request to recording a decision; the target is 8 minutes. Training operations requires prerequisite checks and human-approved decisions.*

已知全景：
- 报名应用 Enrollment app：学习运营 owns `request_id`、`employee_id`、`requested_course`、决策状态；只读 REST + API key，30 req/min。
- HR：owns 雇佣状态；每晚 CSV over SFTP + SSH key。
- 学习系统 Learning system：owns 已完成课程记录；每日 CSV over 同一 SFTP。
- 身份：两个文件都含稳定 `employee_id`；邮箱可能变。全部接口从批准内部主机可达。
- 范围：不替换应用、不加写权限、不自动决策。面试官确认：带时间戳的准备视图有用，但不确定的资格必须走现有人工核验。

memo 审计中的 **错误说法**：① 把雇佣状态归给学习系统、把完成课程记录归给 HR（归属颠倒）；② 声称存在"先修规则 REST 端点"（虚构接口）；③ "导入并 join 成功后自动标记批准并记录决策"（违反人工审批 + 无写权限）。

正确的六项输出：

| 步骤 | 输出 Output |
|---|---|
| C | 中位"打开请求→记录决策"从 20 分钟降到 8 分钟，同时保留先修检查与人工审批；8 分钟是试点目标非承诺；范围 = 准备视图；排除替换应用、新写入、自动决策 |
| L | 学习运营 owns 报名字段与决策状态；HR owns 雇佣状态；学习系统 owns 完成课程；用稳定 `employee_id`，不用可变邮箱 |
| I | 从批准主机：报名只读 REST（API key、30 req/min）；SFTP + SSH 导入 HR 每晚 CSV 和学习系统每日 CSV；**确认新鲜度阈值与先修要求的获取方式**，不假设存在其他接口 |
| E | 导入带时间戳快照 → 取报名请求 → 按 `employee_id` join → 分开展示源事实；协调员 (coordinator) 核验不确定资格、批准并在现有流程中记录 |
| N | 缺 `employee_id` → 身份未解决，不用邮箱猜，走人工核验；完成导出逾期 → 标 stale，人工核验，不推断资格（场景未给数值阈值，需约定） |
| T | 选只读准备视图（现有接口支持、不改审批控制）；接受重复读存储、快照延迟、持续人工核验；不假设不可用的写入或实时更新 |

### 🎤 CLIENT 完整英文走查脚本 / Full English walkthrough script (Cedar Rentals)

> 用法：面试中按此节奏讲，每一步结束时用一句话"锁定输出"，再进入下一步。中括号内是对面试官的提问点。

**C — Context (≈5 min)**
> "Before I draw anything, I want to make sure I understand the workflow. Today, desk staff find the reservation, look up the assigned asset in a maintenance export, resolve ID mismatches by hand, and then record checkout in the reservation tool — is that right? [confirm] Who else cares about this? I'm hearing three groups: desk staff want shorter handovers, maintenance needs unresolved safety holds to stay visible, and the reservation system owner doesn't want any writes from us.
> So let me state the outcome: during a one-branch pilot, reduce the median time from starting reservation review to recording checkout from 12 minutes to 5, without ever checking out an asset that has an unresolved safety hold. The 5 minutes is a pilot target we'll measure, not a promise.
> Scope for version one: show readiness evidence for assigned assets at one branch. Out of scope: reassignment, automated checkout, and replacing either source application."

**L — Landscape (≈5 min)**
> "Next I want an inventory before I draw arrows. Reservations is owned by the rental ops systems team and is authoritative for reservation ID, assigned asset ID, and checkout status — read-only REST with a service API key, 60 requests per minute, no events, no writes. Maintenance is owned by the maintenance team and is authoritative for safety holds and inspection status — hourly CSV over internal SFTP with an SSH key, no live query. Fleet operations owns the approved crosswalk between asset ID and maintenance tag. [ask] How is that crosswalk delivered, how often is it refreshed, and how are corrections made? I'll keep those as open questions until confirmed.
> One thing I want to flag now: the hourly export gives us snapshot evidence, not live safety evidence. And I'll join on stable IDs through the crosswalk, never on equipment names or emails."

**I — Integration points (≈5 min)**
> "For each connection I check three things: an interface, a credential, and a network path. Reservations: REST plus API key, reachable from the approved internal host — confirmed. Maintenance: SFTP plus SSH key, same host — confirmed. Crosswalk: delivery mechanism unknown, so that's an explicit dependency. I'm not going to assume an event feed or a write endpoint, because nothing we've been given provides one, and custom code can't create a permission the client hasn't granted. I'll also design reservation calls to stay well under 60 per minute — fetch on open, not polling."

**E — End-to-end design (≈8 min)**
> "Here's the flow. An importer pulls each hourly maintenance CSV over SFTP and loads it into a small local read store with its source timestamp, and imports the crosswalk the same way once we confirm how it's delivered. When a desk agent opens a reservation, the app calls the reservation API, resolves the assigned asset ID through the crosswalk, and looks up the matching maintenance evidence.
> The screen shows two separate facts: 'Booking: Ready' from reservations and 'Maintenance inspection: HOLD' from maintenance, each with its timestamp. Neither overwrites the other — reservations owns booking state, maintenance owns safety state. Then staff do the physical checks and record checkout in the existing reservation tool, exactly as today. [ask] Is a timestamped snapshot useful for preparation even though it can't authorize checkout on its own?"

**N — Non-happy paths (≈5 min)**
> "Now the failure cases, because this is where the screen can mislead people. If there's no unique crosswalk entry for an asset, we show 'Identity unresolved' and route it to fleet ops — we never guess from the name. If maintenance evidence is older than the agreed threshold — say 90 minutes — we mark it stale and send staff to the existing manual verification. If the reservation API is down or we hit the rate limit, we show 'Reservation could not be refreshed' and staff fall back to the source tool; cached booking state never looks current.
> And two invariants: a HOLD is always visible regardless of booking status, and missing or stale evidence never turns into an inferred clearance."

**T — Trade-offs (≈4 min)**
> "My recommendation is the read-only readiness view. It wins because the interfaces we've verified support it, and it removes repeated lookups without changing who owns what. The costs are a duplicate read store, a dependency on the crosswalk, and continued manual verification.
> I'm rejecting automatic checkout and live event streaming for version one — not because they're bad ideas, but because reservation writes and maintenance events don't exist here. If the client later provides a write API with operating approval, or a maintenance event feed, those become candidates for phase two. What would change my answer today is learning that preparation actually needs live safety clearance — then we'd have to rescope or ask the client for new capabilities."

**Close (≈1 min)**
> "To summarize: one-branch pilot, 12 to 5 minutes median, zero checkouts with unresolved holds; a read-only view that keeps booking and inspection facts separate with timestamps; explicit handling for unresolved identity, stale evidence, and API outages; and open questions on crosswalk delivery and the freshness threshold that I'd confirm before building."

中文要点：每步一句话锁定输出；C 给出含基线/目标/安全条件的结果陈述；L 先列归属与标识符再画箭头；I 检查接口+凭证+网络三件套；E 落到用户在现有工具里的下一步；N 列缺失/陈旧/不可用三类并给出两条不变量；T 说清选什么、付出什么、为什么不选别的、什么条件下会改选。

### 面试怎么说 / How to say it in the interview

**Q: What framework do you use for integration-heavy design questions?**
> "I walk through CLIENT: Context, Landscape, Integration points, End-to-end design, Non-happy paths, and Trade-offs. Each step produces a concrete output — an outcome statement, a system inventory with owners and IDs, verified connections, a flow that ends in the user's next action, behavior for missing, stale or unavailable data, and a recommendation with its costs. The steps constrain each other, so if an interface check fails I go back and rescope rather than just filling in the next heading."
>
> 中文：CLIENT 六步，每步有具体产出，且相互约束。

**Q: Two systems disagree — one says "ready," the other says "HOLD." What do you do?**
> "I separate entity identity from field ownership. First, confirm the records are the same asset through an approved crosswalk, not by name. Then ask which system owns which fact — reservations owns booking state, maintenance owns inspection state. I'd show both values side by side with timestamps rather than merging them into one status, because 'newest wins' could hide a safety hold."
>
> 中文：区分实体身份与字段归属；并列展示两值与时间戳，不合并。

**Q: Why not automate checkout?**
> "Because the facts don't support it: there's no reservation write access, and the owner explicitly said no writes. Automation would also bypass the physical check. It's a phase-two candidate if they grant a write API and operating approval, but adding components wouldn't fix the missing permission."
>
> 中文：无写权限且业主明确禁止；属二期候选，加组件补不了权限。

---

## 19. Running an FDE Design Round｜主持一场 FDE 设计面试

Source: https://www.educative.io/courses/forward-deployed-engineer/running-an-fde-design-round

### 要点 / Key ideas

- 典型失败：12 分钟过去还在提问，桌上一堆约束但面试官没有可检查的设计。**补救**：总结关键点 → 声明能推进的假设 → 把一个有用工作流追踪到足以测试可行性。
- 调研应确定：约定范围、可实现组件、**最小可行方案 (smallest viable solution)**。记录工作假设、标出需验证项，而不是等完整规格。

**45 分钟练习节奏 (45-minute practice schedule)**（按面试形式与面试官重点调整）：

| 时间 Time | 内容 Focus | CLIENT 对应 |
|---|---|---|
| 0–8 min | 期望结果、约束、初始范围 | C |
| 8–13 min | 初始工作流、分配职责 (responsibilities) | L / I |
| 13–27 min | **追踪一个端到端操作**，按关键约束计算可行性 | I / E |
| 27–38 min | 失败场景 + 回应面试官追问 | N |
| 38–45 min | 关键权衡 + 最终推荐 | T |

- 这套节奏、CLIENT、自评量表都是课程练习工具，**不是官方雇主要求或评分标准**。
- 笔记保持三类：**已确认事实 (confirmed facts)**、**声明的假设 (declared assumptions)**、**未解决问题 (unresolved questions)**。
- 第 12 分钟的过渡话术："The outcome and approval boundary are clear. I'll scope one product line, assume the documented Repair interface supports duplicate-safe creation, and flag that for verification. May I trace that workflow, then test capacity?" —— 给面试官一个可挑战的具体假设，同时保住设计时间。

### 示例：Alder Appliances 保修理赔 → 维修工单 (warranty claim to repair ticket)

**English prompt**: *Coordinators spend a median of 25 minutes from warranty-claim approval to a repair ticket becoming visible. Pilot target: 10 minutes for one product line, with an agreed maximum normal-operation data age of 15 minutes.* —— 中位工作流目标与最大数据年龄要求衡量的是不同的东西。

- 归属：Claims 拥有审批和客户信息；Repair 拥有工单状态。
- **薄切片 (thin slice)**：一个可独立产生价值的工作流 —— 每个已批准理赔创建并链接一个维修工单，并向协调员暴露未解决的交接。排除：理赔审批、排期、替换任一应用。连接器 (connector) 演示成功本身 **不证明** 用户价值、采用或生产所有权。
- 访问事实：Claims 只读 API + 服务 API key；Repair 允许通过 **受限服务账号 (restricted service account)** 写入；批准的内部主机可访问两者；有批准的连接器 —— 声称复用前需验证其认证访问与分页 (pagination)。
- 可复用组件减少自定义实现，但 **字段映射 (field mapping)、业务规则、归属冲突、异常处理** 仍需解决。自定义职责：审批资格判断、理赔→工单映射、操作跟踪、测试、异常。

| 负责方 Owner | 职责 Responsibility |
|---|---|
| 集成团队 Integration team | 运行时、告警 (alerting)、连接器维护 |
| 保修运营 Warranty operations | 异常处理、批准资格规则 |
| Repair 应用负责人 Repair application owner | API 权限与工单契约 (ticket contract) |
| 保修运营 + Repair 负责人共同 | 批准未来业务映射；集成团队实现与测试 |

- 安全：客户数据走批准路径、协调员只访问被授权的理赔、保护服务凭证 (credentials)、诊断日志不含客户信息；部署前确认保留与访问要求。

**三种身份 (three identities)**：

| 身份 Identity | 含义 Meaning | 例 Example |
|---|---|---|
| 实体身份 Entity identity | 记录描述哪个业务对象 | `claim_id C204` |
| 操作身份 Operation identity | 正在执行哪个业务操作 | `repair-handoff:C204:v1` |
| 尝试身份 Attempt identity | 哪次执行在运行；**重试保留操作身份** | `A1`，重试为 `A2` |

**追踪 C204（边说边画）**：
1. "Claims reports C204 as approved. I validate eligibility and map its permitted customer and claim fields into Repair's ticket contract."
2. "I persist a pending handoff with `repair-handoff:C204:v1`. Only after that durable write do I treat the integration as responsible for tracking the handoff through completion or an explicit exception."
3. "Worker attempt A1 sends a create request with the stable operation key. Repair returns accepted job J88. This acknowledges request acceptance; it does not yet identify a created ticket."
4. "For this design, I assume Repair's documented contract makes accepted jobs durable, supports operation-key deduplication, and exposes terminal status by job ID. These are interface assumptions to verify."
5. "A status lookup for J88 returns ticket T901. I persist that link and mark the handoff completed. The coordinator now sees 'Repair ticket created: T901.' Before confirmation, the display remains pending."

- **四个不同边界**：请求被接受 (request acceptance)、持久责任 (durable responsibility)、业务完成 (business completion)、用户可见成功 (user-visible success)。HTTP 成功码不结合接口契约，无法证明协调员的工作已完成。

| 观察 Observation | 建立的承诺 Promise established |
|---|---|
| Claims 报告 C204 已批准 | 交接的源授权证据 |
| 集成持久化 C204 的 pending 交接 | 集成承担跟踪至完成或显式异常的持久责任 |
| Repair 向 A1 返回 accepted job J88 | 请求被接受；按假设契约 Repair 拥有一个持久 job |
| J88 状态确认 T901，集成持久化链接并标记完成 | 业务完成已记录；可显示 "Repair ticket created: T901" |

<svg viewBox="0 0 800 260" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="800" height="260" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">Claim C204 Handoff — Acknowledgment Boundaries｜确认边界</text>
  <g font-size="11" text-anchor="middle">
    <rect x="10" y="50" width="140" height="60" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="80" y="72" font-weight="bold">Claims: approved</text><text x="80" y="88">source authorization</text><text x="80" y="102">源授权证据</text>
    <rect x="170" y="50" width="140" height="60" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="240" y="72" font-weight="bold">Persist pending</text><text x="240" y="88">op key …C204:v1</text><text x="240" y="102">集成承担责任</text>
    <rect x="330" y="50" width="140" height="60" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="400" y="72" font-weight="bold">A1 → accepted J88</text><text x="400" y="88">request accepted</text><text x="400" y="102">Repair 持有 job</text>
    <rect x="490" y="50" width="140" height="60" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="560" y="72" font-weight="bold">Lookup → T901</text><text x="560" y="88">business complete</text><text x="560" y="102">业务完成</text>
    <rect x="650" y="50" width="140" height="60" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="720" y="72" font-weight="bold">UI: ticket T901</text><text x="720" y="88">user-visible success</text><text x="720" y="102">用户可见成功</text>
  </g>
  <g stroke="#555" stroke-width="1.5"><line x1="150" y1="80" x2="168" y2="80"/><line x1="310" y1="80" x2="328" y2="80"/><line x1="470" y1="80" x2="488" y2="80"/><line x1="630" y1="80" x2="648" y2="80"/></g>
  <rect x="170" y="140" width="460" height="40" rx="6" fill="#fff" stroke="#e37400" stroke-dasharray="5,4"/>
  <text x="400" y="165" font-size="11" text-anchor="middle">UI shows "pending" from persist until confirmation｜确认前一直显示 pending</text>
  <text x="400" y="210" font-size="11" text-anchor="middle" fill="#444">retry A2 reuses operation key repair-handoff:C204:v1 → no second ticket｜重试复用操作键，不产生第二张工单</text>
  <text x="400" y="235" font-size="11" text-anchor="middle" fill="#444">timeout = outcome unknown, not failure｜超时 = 结果未知，不等于失败</text>
</svg>

**容量计算 (capacity arithmetic)** —— 声明输入：每天 1,200 个已批准理赔、**持续规划峰值 12/min**、平均记录 2 KB、源分页 100 条、源配额 (quota) 30 req/min；积压 (backlog) 240。

```text
Source side
  pages      = ceil(240 / 100)     = 3 pages
  payload    = 240 x 2 KB          = 480 KB (excluding protocol overhead)
  -> fits the 30 req/min source quota

Destination side (the real bottleneck)
  Repair quota          = 60 calls/min, 20 reserved for others
  available budget      = 60 - 20  = 40 calls/min
  calls per handoff     = 2 (create + status lookup)
  capacity              = 40 / 2   = 20 handoffs/min
  net backlog reduction = 20 - 12  = 8 /min
  recovery time         = 240 / 8  = 30 min
```

- 20/min 是 **乐观值**：额外查询、重试、其他瓶颈会降低它。**日均量不能替代持续峰值计算。**
- **新鲜度 (freshness)** = 源发布延迟 + 发现延迟 + 等待 + 处理。源发布延迟可忽略时，每 5 分钟轮询 + 等待与处理 &lt; 2 分钟 ≈ **7 分钟** 正常数据年龄 —— 是估算不是保证。30 分钟积压恢复已排除"无条件 15 分钟新鲜度"承诺；**恢复需要单独的承诺**。

**面试官改约束：Repair 配额减半 (quota halved)** —— 总配额 30/min，保留 10。

```text
available = 30 - 10  = 20 calls/min
capacity  = 20 / 2   = 10 handoffs/min
backlog   = 12 - 10  = +2 /min  -> backlog GROWS; no recovery time exists
```

- 测验正确答案 (B)：**收回新鲜度承诺**，寻求更多配额、已验证的更少调用流程、或约定更窄范围 + 排除部分人工处理；同时保留审批权限、每个已批准理赔一个交接、稳定操作身份。
  - A 错：队列 (queue) 只存储等待工作，不增加完成能力。
  - C 错：重试换新操作身份会造成重复工单。
  - D 错：加 worker 扩大不了 API 预算。
- 话术："I retract the original freshness commitment for this workload. Can we change peak duration, secure more quota, verify a supported lower-call workflow, or narrow the pilot? I recommend delaying that commitment until one option is validated."
- 收窄试点需业务同意，并对排除的理赔保留人工处理。追问应 **修订受影响的决策和承诺**；推荐要说明被否方案、剩余风险、会改变选择的条件。

**失败回答剖析**："The connector already handles the integration. I will add a queue and more workers, mark the claim successful when Repair accepts it, and keep the 15-minute promise after the quota reduction."

| 失败 Failure | 修复 Fix |
|---|---|
| 传输复用掩盖未解决的映射与归属决策 | 列出自定义职责与负责人 |
| 把已接受工作显示为已完成工单 | 工单确认前显示 pending |
| 把 worker 数当 API 容量 | 计算瓶颈 |
| 新鲜度承诺与 10 完成 vs 12 到达矛盾 | 重新协商具体约束 |

**一分钟收尾 (closing in ~1 minute) — 范例**：
> "For one product line, I recommend a connector-assisted approved-claim handoff, targeting a median reduction from 25 to 10 minutes without moving approval authority. It creates and links repair tickets and exposes exceptions; approval, scheduling, and application replacement stay outside scope. The supplied credentials and internal route support the connections; connector behavior, duplicate-safe creation, and durable asynchronous acceptance still need verification. Each claim keeps a stable handoff operation key, and pending becomes completed only after ticket confirmation. The reduced quota supports 10 handoffs per minute against 12 arrivals, so I cannot promise the original freshness target. Subject to agreement, the integration team owns runtime and alerts, warranty operations owns exceptions, and warranty operations and the Repair application owner jointly approve mapping extensions. I reject an all-product rollout until quota and ownership are established. Next, validate the two-call estimate and acceptance contract, then agree on quota or narrower scope. Outage recovery needs its own freshness commitment."

收尾必须与追踪和计算一致；自信地捍卫没改的图会掩盖最重要的发现。

**八维自评量表 (eight review dimensions)** —— 每项 0 = 缺失、1 = 断言但无支撑、2 = 与题目绑定的明确证据；每项引用答案中的句子或计算作证据；弱项写一条改进；**没有及格总分**。

| # | 维度 Dimension |
|---|---|
| 1 | 调研与范围 Discovery &amp; scope |
| 2 | 定量可行性 Quantitative feasibility |
| 3 | 业务语义 Business semantics |
| 4 | 实体与操作身份 Entity &amp; operation identity |
| 5 | 认证与可达接口 Authentication &amp; reachable interfaces |
| 6 | 失败与确认边界 Failures &amp; acknowledgment boundaries |
| 7 | 安全与访问边界 Security &amp; access boundaries |
| 8 | 推荐、权衡与归属 Recommendation, trade-offs &amp; ownership |

**三个迷你轮练习 (three mini-rounds) — 参考解**：

| 题 Prompt | 基线容量与恢复 Baseline | 改约束 Follow-up | 正确回应 Correct response | memo 中的错误 Memo error |
|---|---|---|---|---|
| 发票 Invoice（30→10 min；峰值 8/min；2 调用；配额 30 留 10；积压 100） | (30−10)/2 = **10/min**；恢复 100/(10−8) = **50 min** | 总配额降为 20，仍留 10 → (20−10)/2 = **5/min**，积压每分钟 +3 | 收回中位目标承诺；争取配额/更少调用/更窄范围 | "队列 + 更多 worker 仍能保住 10 分钟目标" —— 错 |
| 退货 Return（40→15 min；峰值 4/min；预算 12/min；积压 40） | 12/2 = **6/min**；恢复 40/(6−4) = **20 min** | Intake 写权限被撤回 | 停止自动创建；改为只读准备视图 + 人工在 Intake 中创建，或重新争取写权限 | "继续用原来允许的受限服务账号自动创建" —— 错，权限已撤 |
| 访问开通 Access（20→5 min；峰值 3/min；预算 10/min；积压 20） | 10/2 = **5/min**；恢复 20/(5−3) = **10 min** | 安全团队禁止请求数据离开客户网络 | 部署在客户网络内（客户托管运行时），外部连接器不可用 | "加密例外允许外部连接器" —— 虚构的例外 |

- 跨题的正确要点：持久化 pending 交接后才承担责任；区分源实体 ID、稳定操作键、单次尝试 ID（重试保留操作键）；接受响应只代表契约记载的承诺；确认前显示 pending；提出运行时负责人、业务异常负责人、目标系统权限/契约负责人供确认。

### 面试怎么说 / How to say it in the interview

**Q: You're 12 minutes in and still asking questions. How do you move on? / 12 分钟还在提问怎么办？**
> "I'd summarize: 'The outcome and the approval boundary are clear. I'll scope one product line, assume the destination API supports duplicate-safe creation, and flag that for verification. Can I trace one workflow and then check capacity?' That gives the interviewer something concrete to challenge and keeps time for design."
>
> 中文：总结 → 声明假设并标注待验证 → 追踪一个流程 → 算容量。

**Q: The API returned 202 Accepted. Can you mark the ticket created?**
> "No. Accepted means the destination took a durable job under its documented contract — if that's what the contract says. Business completion means I've confirmed the ticket ID through a status lookup and persisted the link. Until then the user sees pending. And if a retry is needed, it reuses the same operation key so we don't create a second ticket."
>
> 中文：接受 ≠ 完成；查到工单 ID 并持久化后才显示成功；重试复用操作键。

**Q: The interviewer halves your API quota. What do you say?**
> "I'd redo the math out loud: 20 available calls at 2 per handoff is 10 per minute against 12 arrivals, so the backlog grows — there's no recovery time. Adding workers or a bigger queue doesn't help, because the API budget is the bottleneck. So I retract the freshness commitment and offer options: more quota, a verified one-call workflow, or a narrower pilot with manual handling for the rest."
>
> 中文：重算 → 积压增长 → 加 worker/队列无用 → 收回承诺并给选项。

---

## 20. Choosing How Data Moves Between Systems｜选择系统间数据流动方式

Source: https://www.educative.io/courses/forward-deployed-engineer/choosing-how-data-moves-between-systems

### 要点 / Key ideas

**场景 Morrow Supply（English prompt）**: *Morrow offers three inventory interfaces: a nightly CSV, a read API with snapshot pagination and an incremental change endpoint, and best-effort webhook hints. Inventory changes must become visible within five minutes during normal operation; approved database replication access is unavailable.*
- 选型 = 决定变化多快到达 + 崩溃后谁能恢复。
- **推荐：API 回填 (backfill) + 增量轮询 (incremental polling)；可选用 webhook 更早发现变化**。仅夜间文件达不到新鲜度；直接数据库 **CDC（变更数据捕获 change data capture）** 需要未批准的访问。

**数据移动模式对比 (data movement patterns)**：

| 模式 Pattern | 说明 Description | 关键依赖/风险 Key dependency |
|---|---|---|
| 文件 Files | 定时批量传输（快照与增量） | 交付完成需显式协议（manifest / 原子重命名） |
| 同步 API Synchronous APIs | 即时查询或有界命令 | **时间耦合 (temporal coupling)**：调用方依赖远端在截止时间 (deadline) 内响应 |
| 轮询 Polling | 通过支持的增量接口反复读取 | 恢复依赖 **续接契约 (continuation contract)** |
| Webhook | 提供方主动通知，减少发现延迟 | 完整性依赖投递与恢复机制 |
| 异步消息 Asynchronous messaging | **队列 (queues)** 分发工作；**保留型流 (retained streams)** 支持独立消费与 **重放 (replay)** | 解耦收发可用性，但增加持久发布、消费、恢复责任 |
| CDC | 通过批准的源/复制访问捕获数据库变更 | 快照与日志恢复契约 |
| 虚拟化/联邦读 Virtualized / federated reads | 查询外部数据而不维护本地完整副本 | 源可用性、查询延迟、权限、网络、配额都在读路径上 |

- 模式可组合：API 轮询器本地捕获变化后再发布给消费者。加 **消息代理 (broker)** 前问：谁运维？保留成本多少？现有持久存储是否够用？
- Morrow 新鲜度：1 分钟扫描 + 源发布 &lt; 1 分钟 + 等待处理 &lt; 2 分钟 → 正常数据年龄 &lt; **4 分钟**（以验证过的容量为前提）。停机 (outage) 恢复需要单独预算。

**导入操作 I17 的契约 (accepted import I17)** —— 同步库存查询在响应契约内返回可用值；初始导入则返回一个需要随时间跟踪的 **操作 (operation)**：
- 返回 accepted I17 之前持久化操作身份 (operation identity) `import:warehouse:v1` 及状态。
- 按 I17 提供状态查询：pending / running / completed / failed（含终态细节）。
- 通过 I17 关联请求、进度、结果；每次抓取执行有独立尝试身份 (attempt identity)，重试保留操作身份。
- 设置请求和抓取 **超时 (timeouts)**。**超时 = 结果未知，不证明已取消**；用相同操作身份重试会找到已有导入。
- 接受 = 建立持久跟踪责任；业务完成 = 快照 + 后续变更应用到约定的 **追平边界 (catch-up boundary)**。此前显示 pending/running。

**快照 S800 与变更流无缝衔接 (snapshot-to-feed handoff)**：
- **快照 (snapshot)** 表示某边界时的源状态；**游标 (cursor)** 是续接令牌 (continuation token)，其保证来自提供方。**分页本身不产生一致快照，也不产生可恢复的变更历史。**
- Morrow API：快照令牌 S800 = 截至源变更位置 800 的 250 条记录；三页 100/100/50；有序变更流保留 24 小时（含删除）。
- 步骤：
  1. 持久化回填阶段和 S800；第 1 页存入 **暂存区 (staging)**，然后持久保存其下一页游标；第 2、3 页同理。
  2. 在显式边界 **发布 (publish)** 完整暂存快照；发布前 **暂缓较新变更**，避免后面的快照页覆盖更新的库存状态。
  3. 消费 **严格大于 800** 的变更；捕获当前源头部位置（如 845），导入持续运行直到 845 之前的变更都已应用。
  4. 标记 I17 completed through 845，继续持续同步。
- 成立前提：源把 S800 绑定到位置 800（普通 REST 端点未必提供这种流）。必须在保留期内完成捕获，否则调用受支持的 **重新同步 (resynchronization)** 路径。

**时间戳水位线陷阱 (timestamp watermark pitfall)**：
- `updated_at > last_timestamp` 会 **跳过与边界时间戳相同的记录**。
- 对策：文档化的有界窗口、支持时用稳定分页、处理并列 (tie handling)、**包含式重叠 (inclusive overlap)**、按 **记录版本去重 (record-version deduplication)**。延迟可见、并发更新、不稳定分页、删除仍需源保证；无上界的可见延迟需 **对账 (reconciliation)** 或对完整性声明加限定。

**检查点 803 该在何时保存 (checkpoint placement)**：
- **捕获检查点 (capture checkpoint)**：记录集成已持久承担多远的源变更责任。
- 错误实现：先存位置 803 → 确认 webhook H9 → 再存变更 801–803。存储前崩溃 → 下次从 803 后轮询、提供方认为 H9 已送达 → **视图静默丢更新**。
- 正确：**收件箱 (inbox) 持久写入与检查点推进在同一本地事务 (transaction) 中**：
  1. 开启集成数据库事务；
  2. 插入 801、802、803 的 inbox 条目，键为 `(source, change_position)`，含负载 (payload) 与 pending 应用状态（唯一键识别重放）；
  3. 检查点从 800 更新为 803；
  4. 提交。
- 测验正确答案 (D)：**提交前崩溃** → 条目和检查点都不保留，检查点仍为 800，下次重抓三条；**提交后崩溃** → 检查点 803 与三条 pending 条目都持久，worker 从 inbox 恢复应用。（B 错：检查点 803 只证明 **捕获**，不证明已应用到读模型 (read model)；C 错：重放不需要新操作身份。）
- 源不必参与事务：可重放的源读取让集成能在本地原子化 inbox 存储与捕获进度。
- 若记录与检查点无法同事务：**先持久化记录，后存检查点**；中间崩溃导致重放，由 **重复安全应用 (duplicate-safe application)** 处理。**先推进检查点会产生丢失窗口。**
- 通用原则：恢复可以重复已持久的工作，但重复必须保持原意图操作，不能产生新的业务动作。

```sql
-- Atomic capture: inbox rows and checkpoint advance commit together
BEGIN;
INSERT INTO inbox (source, change_position, payload, state)
VALUES ('morrow', 801, :p801, 'pending'),
       ('morrow', 802, :p802, 'pending'),
       ('morrow', 803, :p803, 'pending')
ON CONFLICT (source, change_position) DO NOTHING;
UPDATE capture_checkpoint SET position = 803 WHERE source = 'morrow';
COMMIT;
```

**Webhook H9 不能替代轮询器**：H9 只说 "W1 仓库 P42 变了"，是 **提示 (hint)** 而非完整记录。入口处理：
1. 用提供方支持的签名、基于文档规定的请求字节 **验签 (verify signature)**；应用支持的时间戳或事件 ID **防重放 (replay controls)**。
2. 持久写入入口存储，识别重复事件 ID。
3. **持久捕获后** 才返回提供方期望的确认。
4. 异步获取受支持的源表示并处理；重复 H9 不得产生另一个业务操作；同一源版本的不同提示也要安全收敛。
- 入口存储不可用时 **不要确认**（否则等于承诺了持久接受）。保留周期性权威变更扫描以恢复漏掉的提示；可用时使用提供方的查询或重放。
- 监控 **权威捕获延迟 (authoritative capture lag)**，而不只是 webhook 确认成功数。扫描必须在 24 小时保留期过期前捕获漏掉的变化 —— 持久入口无法恢复已过期的源历史。

**预测是否共享库存队列 (should forecasting share the queue?)**：
- **工作队列 (work queue)**：每个任务分给若干 **竞争消费者 (competing consumers)** 之一 —— 一个库存更新任务只需一个 worker 时用。
- 库存读模型和预测 **都需要每个变化** → 各自独立的 **持久订阅 (durable subscription)** 和检查点。放在同一竞争消费者组会把变化分给两方。持久订阅与保留的流位置只在文档化的持久与保留范围内可恢复。
- **排序范围 (ordering scope)**：`(warehouse_id, item_id)`，如 W1/P42。按该键分区 (partition)/路由，说明 broker 的排序契约，防止并发 worker 先应用较新版本；不同键可并发推进。
- Worker 可能提交数据库更新后、确认消费前崩溃 → 重投递 (redelivery) 以新尝试身份重复同一操作。需要 **重复安全的数据库应用** 或目标系统支持的操作键；**broker 投递保证本身不能保证业务效果无重复**。

**仅文件 vs CDC (file-only vs CDC)**：
- 文件：每小时快照仍达不到 5 分钟 → 换接口或重新协商新鲜度。文件契约要明确：
  - **完成 (completion)**：上传后由生产方发布 **清单 (manifest)**（如 `inventory-20261026T1000.csv` 的快照时间、文件身份、预期行数、**校验和 (checksum)**）；文件出现不代表上传完成；支持时也可用 **原子重命名 (atomic rename)**。
  - **发布 (publication)**：区分全量快照与增量，暂存并校验，识别重复文件身份，在显式边界发布。
  - **重启 (restart)**：若失败运行已发出外部写入，部分效果可能残留 → 从记录的行或操作边界重启。
  - **原子性 (atomicity)**：批次原子性只属于某个具体事务（如 Palantir Foundry 记载批量同步的输出数据集为单一事务），**不覆盖任意下游 API 调用**。
- CDC：需要批准的访问和源定义的 **快照到日志衔接 (snapshot S at log position L)**，回填期间从正确边界保留变更；捕获插入、更新与 **删除墓碑 (delete tombstones)**；持久捕获后保存位置。停机超过保留期 → **检测缺口并重新快照** 或用受支持的修复，绝不默默从最新 offset 恢复。

<svg viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="800" height="300" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">Morrow: Backfill + Poll + Webhook Hints｜回填 + 轮询 + webhook 提示</text>
  <g font-size="11" text-anchor="middle">
    <rect x="15" y="45" width="150" height="50" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="90" y="66" font-weight="bold">Snapshot S800</text><text x="90" y="82">3 pages, as of pos 800</text>
    <rect x="15" y="115" width="150" height="50" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="90" y="136" font-weight="bold">Change feed</text><text x="90" y="152">ordered, 24h retention</text>
    <rect x="15" y="185" width="150" height="50" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="90" y="206" font-weight="bold">Webhook hint H9</text><text x="90" y="222">best-effort 尽力而为</text>
    <rect x="205" y="45" width="140" height="50" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="275" y="66">Staging + page cursors</text><text x="275" y="82">暂存 + 游标持久化</text>
    <rect x="205" y="115" width="140" height="50" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="275" y="136">Poller (1-min sweep)</text><text x="275" y="152">changes &gt; 800</text>
    <rect x="205" y="185" width="140" height="50" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="275" y="206">Verify → durable ingress</text><text x="275" y="222">→ then ACK</text>
    <rect x="385" y="100" width="170" height="80" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="470" y="125" font-weight="bold">One local transaction</text><text x="470" y="143">inbox rows (source, pos)</text><text x="470" y="159">+ checkpoint advance</text><text x="470" y="174">同一事务</text>
    <rect x="595" y="65" width="190" height="50" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="690" y="86">Worker: inventory model</text><text x="690" y="102">key (warehouse, item)</text>
    <rect x="595" y="165" width="190" height="50" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="690" y="186">Forecasting subscription</text><text x="690" y="202">own checkpoint 独立订阅</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="165" y1="70" x2="203" y2="70"/><line x1="165" y1="140" x2="203" y2="140"/><line x1="165" y1="210" x2="203" y2="210"/>
    <line x1="345" y1="70" x2="383" y2="120"/><line x1="345" y1="140" x2="383" y2="140"/><line x1="345" y1="210" x2="383" y2="160"/>
    <line x1="555" y1="130" x2="593" y2="90"/><line x1="555" y1="150" x2="593" y2="190"/>
  </g>
  <text x="400" y="270" font-size="11" text-anchor="middle" fill="#444">hint triggers early fetch; periodic sweep is the authority｜提示加速发现，周期扫描才是权威</text>
  <text x="400" y="288" font-size="11" text-anchor="middle" fill="#444">checkpoint = captured, not applied｜检查点 = 已捕获，不等于已应用</text>
</svg>

### 练习：Pine Print 移动与恢复契约 (practice)

**English prompt**: *Dispatch staff need job-status changes within ten minutes during normal operation. Source: ≤1 min from change to source timestamp, then ≤2 min visibility delay. Five-minute polling; extraction+application ≤1 min at validated load. `updated_since` API with bounded windows and stable snapshot pagination within each poll. Stable `job_id` and `record_version`; inclusive five-minute overlap covers visibility delay. No events, no DB access. A nightly full snapshot whose absent job IDs identify deletes. Follow-up: deletes must also appear within ten minutes.*

参考解：
- **新鲜度预算**：1 + 2 + 5 + 1 = **9 分钟** ≤ 10。仅夜间传输不达标；webhook 和 CDC 不受支持。
- **窗口规则**：每次轮询从"上次已完成的上界水位 − 5 分钟"包含式查询到固定的当前上界；所有分页保持同一窗口；按 `(job_id, record_version)` 去重。
- **水位推进**：**只有在该有界窗口的所有页都持久捕获后** 才推进完成水位到上界（memo 中"第一页持久后就推进"是错的）。
- **检查点含义**：捕获水位 = 持久责任，不是应用完成；应用进度单独跟踪。
- **记录已提交但检查点失败**：从较旧的持久水位恢复，重复包含式重叠窗口，识别重复的 job/version 对，不产生新操作 —— 重复捕获工作而不冒跳页风险。
- **删除策略**：只有 **验证完整** 的夜间快照才可把缺失 job ID 视为删除；不完整快照不得触发基于缺失的删除。
- **新需求（删除也要 10 分钟内可见）**：夜间缺失对账 **无法** 满足。需要墓碑、删除流、其他受支持接口，或明确放宽需求。（memo 声称 API 含删除墓碑 —— 题目未提供，属虚构。）
- memo 其他错误："9 分钟预算由夜间全量快照契约支撑" —— 错，支撑的是轮询链路。

### 面试怎么说 / How to say it in the interview

**Q: How do you choose how data moves between two systems? / 如何选择数据移动方式？**
> "I start from what the source actually supports and the freshness target, then think about who can recover after a crash. For Morrow, nightly files miss the five-minute target and CDC needs database access they haven't approved, so I'd do an API backfill from a snapshot plus incremental polling of the change feed, and use webhooks only as hints to fetch sooner. Before adding a broker, I ask who will operate it and whether our existing durable store is enough."
>
> 中文：按源能力 + 新鲜度 + 恢复责任选；Morrow 选回填 + 增量轮询 + webhook 提示。

**Q: How do you avoid gaps between a backfill and the change stream?**
> "I need a snapshot that's tied to a change position — say S800 at position 800. I stage all snapshot pages, persisting the cursor after each page, publish at an explicit boundary while holding newer changes, then apply changes strictly after 800 until I catch up to the head I captured. That only works within the feed's retention; otherwise I resync."
>
> 中文：快照绑定变更位置；分页暂存并持久化游标；显式发布；从 800 之后追平；保留期内完成。

**Q: Where do you save the checkpoint?**
> "In the same local transaction as the durable inbox rows for those changes. If I crash before commit, the checkpoint is still at the old position and I refetch; after commit, both are durable and workers recover from the inbox. If I can't share a transaction, records first, checkpoint second — replay is safe with dedup on source and position, but advancing the checkpoint first creates a loss window."
>
> 中文：与 inbox 同事务；否则先记录后检查点；先推检查点会丢数据。

**Q: Can webhooks replace polling?**
> "No — webhooks are best-effort hints. I verify the signature, durably store the event before acknowledging, fetch the authoritative record asynchronously, and dedupe by event ID and source version. I keep a periodic authoritative sweep to catch missed hints, and I monitor capture lag against the feed's retention window, not just webhook success counts."
>
> 中文：webhook 是提示；验签、持久化后再确认、异步取权威记录；保留周期扫描并监控捕获延迟。

**Q: Why not use `updated_at > last_seen` for incremental sync?**
> "Because records sharing the boundary timestamp get skipped, and late-visible records slip through. I use bounded windows with an inclusive overlap that covers the documented visibility delay, stable pagination within the window, and dedup on record ID plus version. Deletes need their own mechanism — tombstones or reconciliation against a verified full snapshot."
>
> 中文：严格大于会漏同时间戳记录；用有界窗口 + 包含式重叠 + 版本去重；删除另行处理。

---

## 21. Bridging Authentication Across Systems｜跨系统认证桥接

Source: https://www.educative.io/courses/forward-deployed-engineer/bridging-authentication-across-systems

### 要点 / Key ideas

- 场景：Rill Parts 员工成功登录门户、打开工单，却收到 API **拒绝访问 (access denied)**。登录建立的是 **门户身份 (portal identity)**；工单 API 仍需要 **已授权的调用方** 和 **它接受的凭证**。认证桥接 = 为每个连接规定访问契约，并在适配器 (adapter) 和复制数据中保持用户权限不被放大。
- Rill 环境：门户用 **SAML 单点登录 (SSO)** + **SCIM 用户配置 (provisioning)**；工单 API 支持委托与应用 OAuth；保修 API 要求 **OAuth 1.0a**；供应商 API 要求 **API key + 客户端证书 (client certificate)**。

**四个概念必须区分**：

| 概念 Concept | 回答的问题 Question answered | 典型协议 Typical protocol |
|---|---|---|
| 认证 Authentication | 谁登录了？Who signed in? | OIDC、SAML |
| 联邦 Federation | 门户接受谁的身份证据？Whose identity evidence is trusted? | SAML、OIDC |
| 配置 Provisioning | 账号是否存在且仍有效？组成员关系？ | SCIM |
| 授权 Authorization | 这个调用方能否读这个工单？May this caller read this case? | OAuth 2.0（访问受保护资源）+ 业务策略 |

- SAML 常用于联邦登录；**OIDC 在 OAuth 2.0 上加身份层**；OAuth 管理对受保护资源的访问；SCIM 管配置。**任何一个单独都不保证下游业务权限。**
- Rill 的 SAML 登录产生 **门户会话 (portal session)**，不是工单 API 的 **访问令牌 (access token)**。SCIM 组成员是策略输入；API 仍执行自己的授权模型。每个下游边界都要识别 **人类调用方** 和 **集成身份 (integration identity)**。

**委托访问 vs 工作负载访问 (delegated vs workload access)**：
- **委托访问 (delegated access)**：带着用户的授权行事。**工作负载访问 (workload access)**：以应用/服务身份行事。**服务账号 (service account) 是一种身份，不是通用凭证格式，也不是 OAuth 授权类型 (grant)。**

**Rill 连接清单 (connection inventory)**：

| 连接 Connection | 身份与凭证 Identity &amp; credential arrangement |
|---|---|
| 门户登录 Portal login | 员工身份：SAML 联邦登录；SCIM 配置门户账号与组 |
| 用户级工单查看 Case viewer | 用户委托：**授权码 + PKCE (authorization code with PKCE)**；请求 `cases.read`，应用提供方的用户级限制 |
| 夜间导入 Nightly importer | 专用应用身份：**客户端凭证 (client credentials)**，工单 API 应用权限 `cases.read`；可摄取租户 (tenant) 工单但不能写 |
| 保修适配器 Warranty adapter | 租户专属只读集成身份：OAuth 1.0a **请求签名 (request signing)** 凭证集 |
| 供应商连接器 Supplier connector | 自有只读集成身份：API key + **mTLS 客户端证书**（证明持有对应私钥 (private key)） |

- 证书认证仍需业务授权。OAuth 1.0a 签名、API key、证书认证是不同机制，各自独立适配器。
- 交互式委托默认 **授权码 + PKCE**。**公共客户端 (public client)**（如浏览器代码）无法安全保存共享客户端密钥 (client secret)；**机密客户端 (confidential client)** 能在其执行环境中保护凭证 → Rill 把委托令牌处理放在机密的门户后端。
- SAML IdP 可在工单提供方授权流程中认证用户，但工单提供方仍须签发它支持的 API 授权。若无应用权限：选提供方支持、管理员批准的委托（并承担其生命周期义务），或重新协商无人值守流程。**借用浏览器会话既不是受支持的工作负载身份，也没有可靠的授权生命周期。**
- 清单也确定了独立的 **撤销目标 (revocation targets)**：禁用门户账号和撤销连接器下游凭证是不同操作。

**令牌何时可用、如何续期 (token usability &amp; renewal)** —— 工单 API 期望 **受众 (audience)** `case-api`：
- Viewer：`cases.read` 访问令牌 15 分钟；只有在要求的 **离线访问同意 (offline-access consent)** 与策略批准后才签发 **刷新令牌 (refresh token)**。
- Importer：应用访问令牌 15 分钟；不签发刷新令牌，用工作负载凭证重新获取。
- **ID 令牌 (ID token)** 只为其目标客户端证明身份，**不能替代 API 访问令牌**。按接收方验证契约匹配：**签发者 (issuer)**、受众、租户、主体或应用身份、过期时间、权限。用提供方库或受支持的 **令牌内省 (introspection)**；令牌不一定是 JWT，**仅解码 JWT 不等于验证**。
- **令牌缓存隔离**：按租户、客户端、身份、资源、权限集隔离。刷新令牌和工作负载凭证存于受保护后端，跟踪过期，通过受支持的授权类型续期。
- 因委托同意被撤销而续期失败 → 标记连接 **reconnect-required**，转给 Rill 的客户身份管理员。**绝不用导入器更宽的令牌顶替让 viewer 继续工作。**

**OAuth 安全控制 vs 攻击 (RFC 9700, OAuth 2.0 Security BCP, Jan 2025)**：

| 威胁 Threat | 控制 Control |
|---|---|
| 重定向替换 Redirect substitution | 授权服务器 **精确字符串匹配 (exact string matching)** 重定向 URI；唯一例外是原生应用 localhost 重定向的端口号 |
| 授权码截获/注入 Code interception / injection | 公共客户端 **必须** 用 PKCE，机密客户端 **应该** 用；授权服务器必须支持 PKCE（截获者没有 **code verifier** 无法换令牌） |
| 浏览器事务攻击 CSRF | 客户端必须防 CSRF；仅当确认授权服务器支持 PKCE 时 PKCE 才提供此保护，否则用一次性 `state` 值 |
| 已签发令牌被盗重放 Stolen token replay | PKCE 不保护已签发令牌 → 推荐 **发送方约束令牌 (sender-constrained tokens)**：mTLS 或 **DPoP**，加受众与权限限制 |

- RFC 9700 还规定：**禁止** 使用 **资源所有者密码凭证授权 (ROPC)**；**不应** 使用 **隐式授权 (implicit grant)** 或从授权端点直接签发访问令牌的响应类型；签发给公共客户端的刷新令牌必须发送方约束或 **轮换 (rotated)**。
- 原生应用：**RFC 8252** 要求通过外部用户代理授权，公共原生应用必须实现 PKCE —— 不要推广到所有 OAuth 客户端。

**混淆代理问题 (confused deputy) 与正确路由**：
- 错误 broker 设计：接受任何登录用户、信任请求参数 `tenant_id`、选择该租户连接器、返回完整下游对象 → 调用方可替换成 T2 或请求无关保修，broker 用特权 (privileged) 凭证替他执行。**特权组件替缺乏相应权限的调用方行使其权限 = 混淆代理失败。**
- 正确路由（u17 在租户 T1，可读被分配的工单 C42，C42 引用保修 W42）：
  1. 后端验证门户会话，从 **可信身份上下文** 推导 u17 和 T1；请求参数不能选择 T2 的权限。
  2. 检查当前策略：u17 与 C42 的关系、请求的读动作、C42 与 W42 的已验证关联；任意保修 ID 不够。
  3. 把可信 T1 映射到 T1 批准的保修连接器，请求 **有界操作** "read W42"；调用方不能选择任意目标 URL 或操作。
  4. 只有适配器从受保护存储取 T1 的 OAuth 1.0a 凭证，用受支持库签名。
  5. 后端只返回 u17 可接收的字段；签名密钥和通用特权令牌永不进入响应。
- 受控 **凭证代理 (credential broker)**：认证并授权调用方、选择批准的下游身份、调解有界操作，或执行显式支持的 **令牌交换 (token exchange)**。它 **不能** 把 SAML 断言普遍转换成任意 API key、OAuth 令牌或遗留凭证。

<svg viewBox="0 0 800 270" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="800" height="270" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">Avoiding the Confused Deputy｜避免混淆代理</text>
  <g font-size="11" text-anchor="middle">
    <rect x="10" y="70" width="120" height="60" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="70" y="94" font-weight="bold">u17 browser</text><text x="70" y="110">portal session</text><text x="70" y="124">门户会话</text>
    <rect x="160" y="45" width="190" height="110" rx="8" fill="#e8f0fe" stroke="#3367d6"/>
    <text x="255" y="66" font-weight="bold">Backend (confidential)</text>
    <text x="255" y="86">1 derive u17, T1 from session</text>
    <text x="255" y="102">2 policy: u17 → C42 → W42</text>
    <text x="255" y="118">3 bounded op "read W42"</text>
    <text x="255" y="134">5 project permitted fields</text>
    <rect x="380" y="70" width="150" height="60" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="455" y="92" font-weight="bold">T1 warranty adapter</text><text x="455" y="108">4 sign with OAuth 1.0a</text><text x="455" y="122">secret stays here</text>
    <rect x="560" y="45" width="110" height="40" rx="6" fill="#fff" stroke="#5f6368"/><text x="615" y="70">Secret store</text>
    <rect x="560" y="105" width="110" height="40" rx="6" fill="#e6f4ea" stroke="#137333"/><text x="615" y="130">Warranty API</text>
    <rect x="690" y="70" width="100" height="60" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="740" y="92" font-weight="bold">Policy svc</text><text x="740" y="108">down → deny</text><text x="740" y="122">失败即拒绝</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="130" y1="100" x2="158" y2="100"/><line x1="350" y1="100" x2="378" y2="100"/>
    <line x1="530" y1="90" x2="558" y2="65"/><line x1="530" y1="110" x2="558" y2="125"/>
    <path d="M350 60 C500 20, 700 20, 740 68" stroke-dasharray="4,3"/>
  </g>
  <g font-size="11" fill="#c5221f">
    <text x="20" y="190">✗ tenant_id from request param → can pick T2 authority｜请求参数选租户 = 漏洞</text>
    <text x="20" y="210">✗ arbitrary warranty ID / destination URL｜任意 ID 或目标 URL</text>
    <text x="20" y="230">✗ signing secret or broad token returned to caller｜把密钥/宽令牌返回调用方</text>
  </g>
  <text x="20" y="255" font-size="11" fill="#137333">✓ authority derived from trusted identity, bounded operation, field projection｜权限来自可信身份 + 有界操作 + 字段投影</text>
</svg>

**导入器能读 C99，u17 为何不能 (connector access ≠ user permission)**：
- 导入器复制 T1 的 C42 与 C99，含 `internal_cost`。当前策略：u17 只能读 C42、排除 `internal_cost`、无写权限。
- **连接器的宽权限绝不能变成应用用户的有效权限。** 每条复制记录保留租户和源标识，保留或可解析执行所需的策略信息。
- 缓存读 C42 的检查顺序：
  1. 从可信会话推导 T1，检索限制在 T1；返回前检查 **对象与行级授权 (object &amp; row authorization)** —— C99 即使在 T1 内也失败。
  2. **每次读都查询当前策略服务 (policy service)** —— Rill 的 **权限新鲜度契约 (permission-freshness contract)**：策略服务故障 → **拒绝 (fail closed)**；重新分配在下次读取生效。
  3. 只 **投影 (project)** 允许的字段，从 C42 去掉 `internal_cost`；同样适用于缓存响应、搜索结果、**AI 功能使用的检索**。
  4. 每次下游工具调用前 **重新检查请求的动作**；读 C42 的权限不授予写权限。
- 连接器认证成功与用户请求被拒绝可以共存。测试实际响应边界，包括分配变更后会怎样。
- 课程 9 题允许/拒绝测试的规律：可信 T1 会话 + 被分配 C42 + 策略可用 + 只请求允许字段 → **允许**；请求 C99、请求 `internal_cost`、篡改 `tenant_id` 为 T2、分配已移除、策略服务不可用、请求写操作 → **拒绝**。**缓存的业务数据不能授权自身的披露 (disclosure)**；只在摄取时过滤会失败，因为共享副本本就包含不同权限调用方的记录和字段。

**轮换与撤销 (rotation &amp; revocation)**：
- 按客户和环境隔离的 **最小权限 (least privilege) 集成身份**；保护密钥与私钥，限制只有相关适配器能取。两个负责人：**客户身份管理员** 负责同意与重新授权；**集成运维** 负责连接器发布。
- 计划内供应商轮换：
  1. 在提供方支持的 **重叠期 (overlap)** 内注册替换 key 与证书为 v2；
  2. 安全存储 v2，用它测试一次授权读；
  3. 连接器实例切到 v2，验证没有实例仍在用 v1；
  4. 重叠期结束前退役 v1；提前监控证书过期。
- 无重叠期 → 安排显式切换 + 计划内暂停，**不承诺零停机 (zero downtime)**。旧 OAuth 客户端凭证签发的访问令牌要单独跟踪：替换存储的密钥不一定使已签发令牌失效。
- **泄露 (compromise)**：立即撤销（不保留计划重叠）、清空本地凭证和令牌缓存、按支持的令牌撤销与事件流程处理。委托同意被撤销 → reconnect-required，转指定管理员。

### 练习：Vale Service 访问契约 (practice)

**English prompt**: *Staff use OIDC login and SCIM. The report API supports only delegated authorization code with PKCE (audience `reports-api`, scope `reports.read`, 10-minute tokens); refresh tokens require approved offline access; no application permissions. The archive must run after staff sign out. A legacy attachment API accepts a tenant-specific service API key and supports two active keys during rotation. u8 (tenant V1) may read assigned report G9 excluding `margin`, no write. Consent is later revoked.*

memo 中的错误说法：
1. "提供方支持仅归档用的应用权限 + 客户端凭证" —— 虚构，题目明确无应用权限。
2. "OIDC 登录 + SCIM 建立下游报告权限，viewer 可把 ID token 发给 reports-api" —— 错，ID token 不是访问令牌。
3. "登出后复用员工浏览器会话做归档" —— 错，借用会话不是受支持的工作负载身份。
4. "信任用户提供的 `tenant_id` 选附件 key，返回含 `margin` 的完整归档" —— 混淆代理 + 字段泄露。
5. "无限重试已撤销的同意" —— 应标记 reconnect-required 转管理员。
6. "轮换时先退役旧 key 再发布新 key" —— 顺序反了，应先上 v2 验证再退役 v1。

正确结论：**登出后归档只有在管理员批准离线访问委托后才可行**；否则是部署约束，需重新协商（不能假设能力）。memo 中正确的部分（受保护存储、缓存隔离、10 分钟过期跟踪、保留租户/源 ID、每次读查策略、策略失败即拒绝、字段投影、下游调用前复查动作）保留。可观测测试：u8 只拿到 G9 允许字段（实时与归档）；其他 V1 报告、其他租户、`margin`、写操作被拒；测试 tenant 参数篡改、无关附件、分配移除、策略服务故障、错误受众令牌、ID token 替换；测试批准后登出归档、过期续期、撤销恢复、旧 key 仍有效时的新 key 发布。

### 面试怎么说 / How to say it in the interview

**Q: The user is logged in but the API returns 403. Why? / 已登录却 403？**
> "Login only established a portal identity — SAML gave us a session, not an access token for the case API. The API needs a caller it authorizes and a credential it accepts, with the right audience and scope. So I'd check which identity is actually calling the API — the user via delegated OAuth, or a service identity — and whether that identity has the permission for that specific case."
>
> 中文：登录 ≠ API 授权；检查实际调用身份、受众、范围和对象权限。

**Q: Your integration's service account can read everything. How do you stop it from leaking data to users?**
> "Connector access must never become the user's effective permission. I keep tenant and source IDs on every copied record, derive the tenant from the trusted session — never a request parameter — check row-level authorization against the live policy service on every read, fail closed if policy is unavailable, and project only permitted fields. That applies to caches, search, and anything an AI feature retrieves. And I recheck the action before every downstream tool call."
>
> 中文：连接器权限 ≠ 用户权限；可信租户、行级授权、策略失败即拒绝、字段投影、复查动作。

**Q: Which OAuth flow for an interactive web app, and which for a nightly job?**
> "Interactive: authorization code with PKCE, with tokens handled in a confidential backend. Nightly job: client credentials with an application permission, if the provider supports it. If it doesn't, I don't borrow a browser session — I either get admin-approved offline delegation with its lifecycle obligations, or renegotiate the unattended requirement. Per RFC 9700, no password grant, no implicit flow, exact redirect matching, and sender-constrained tokens where replay matters."
>
> 中文：交互用授权码 + PKCE；后台任务用客户端凭证；不支持就走批准的离线委托或重新协商。

**Q: How do you rotate a credential without downtime?**
> "If the provider supports overlap: register v2, store and test it, move all instances, verify nothing still uses v1, then retire v1 before the overlap ends. If there's no overlap, I schedule an explicit cutover with a planned pause instead of promising zero downtime. For a compromise, I revoke immediately and flush caches — no overlap."
>
> 中文：有重叠期按 v2 注册 → 测试 → 切换 → 验证 → 退役 v1；无重叠则计划停机；泄露立即撤销。

---

## 22. Handling Failures, Rate Limits, and Silent Errors｜处理失败、限流与静默错误

Source: https://www.educative.io/courses/forward-deployed-engineer/handling-failures-rate-limits-and-silent-errors

### 要点 / Key ideas

**场景 Tern Dispatch（English prompt）**: *Workers are healthy, yet shipment S204 is still pending after a courier request timed out. Recovery must establish what happened remotely and finish the shipment without booking it twice.*

| 观察 Observation | 证明了什么 Establishes | 仍未知 Unknown |
|---|---|---|
| 所有 worker 健康 | 进程可用 | 业务进度 |
| 快递创建超时 | 调用方停止等待 | 是否已下单 (booking effect) |
| 派送屏显示 pending | 无可见就绪 | 远端面单与持久派送引用 |
| 三者合起来 | 未证明完成 | 哪些业务步骤未完成 |

- 契约：**只有快递报告可用面单 (usable label) 且派送系统持久保存其引用**，货件才算 ready。
- **四个确认边界**（与第 19 课一致）：请求接受 → **持久责任**（集成已提交意图并可崩溃恢复，此后才可回复 "accepted for processing"）→ 业务完成 → 用户可见成功。
- 快递返回 **202** 只证明远端接受；**超时只限制调用方等待时长，远端副作用可能已发生**。
- 测验要点：意图未提交时，入口 **只能确认收到 (acknowledge receipt only)**，等持久意图后再说 "accepted for processing"。把收到当持久责任 → 可能丢失已接受工作；把远端接受当完成 → 掩盖未完成工作。

**哪些失败值得重试 (retry policy)** —— 由 worker 拥有远端重试：

| 参数 Parameter | 值 Value |
|---|---|
| 每次执行总尝试次数 Total attempts | 3 |
| 单次超时 Per-call timeout | 3 s |
| 执行截止时间 Execution deadline | 15 s（含调用、准入等待、延迟） |
| 退避 Backoff | 第 i 次重试前（i 从 0 起）等待 **全抖动 (full jitter)**：在 0 与 min(2 s, 0.5 s × 2^i) 之间均匀随机 |
| 准入 Admission | 只有延迟 + 超时能放进剩余截止时间才发起下一次调用 |

| 失败类型 Failure type | 处理 Handling |
|---|---|
| 文档化的瞬时故障、限流 Transient / throttling | 操作安全时重试 |
| 无效请求 Invalid request | 需要修复，不重试 |
| 授权被撤销 Revoked authorization | 转访问负责人 |
| 写操作超时 Timed-out write | 归类为 **结果未知 (outcome-unknown)**，先查清效果再继续 |

- 遵守提供方 **`Retry-After`** 头：30 秒延迟 = **持久地调度到本次执行之外**，不提前重试、不无限占用 worker。预算耗尽 → 持久化 deferred/exception 状态，含累计尝试历史与 **有限恢复期限 (finite recovery horizon)**；超过期限需运维审核。
- **重试放大 (retry amplification)**：SDK、适配器、worker 各 3 次 → 3 × 3 × 3 = **27** 次下游调用。关闭下层重试，或显式计入 worker 预算。

**共享配额预算 (shared quota budget)** —— 快递允许所有 Tern 连接器实例共 **120 calls/min**；正常每单 1 次创建 + 1 次状态查询，20 单/分钟 → 40 calls/min。

| 用途 Use | 上限 Ceiling (calls/min) | 配额降到 60 时 When quota falls to 60 |
|---|---|---|
| 实时工作 Live work | 40 | 40 |
| 重试与结果未知恢复 Retries &amp; recovery | 20 | 10 |
| 定期对账 Scheduled reconciliation | 10 | 10 |
| 回填 Backfill | ≤ 50 | 暂停 paused |
| 合计 Total | 120 | 60 |

- 额外的 pending 状态轮询消耗显式预算；2 次是正常基线，不是每单保证成本。
- **共享准入限流器 (shared admission limiter)** 覆盖所有调用方与提供方文档化的配额窗口和突发 (burst) 规则；另把在途快递调用 **并发上限 (concurrency limit) 设为 4**。**速率控制单位时间调用数；并发控制同时资源使用** —— 4 个并发不保证达到配额上限的吞吐。
- 限制 pending 队列大小，满了停止接收回填。容量耗尽时，在确认持久责任 **之前** 拒绝新的实时请求。

**安全地用 A2 跟进超时的 A1 (idempotent retry)**：
- 首次下单操作身份 `T1:S204:book:1`；尝试 A1、A2 身份不同但保留同一操作身份。**仅货件身份不够**：有意的替换下单需要新操作身份。
- 设计依赖的提供方能力：**幂等键 (idempotency key)** 原子绑定 **请求指纹 (request fingerprint)** 与下单；相同并发提交返回已有结果或进行中状态；**载荷变化则冲突 (conflict)**；支持按键查询；绑定持续 **7 天**。
- 本地：唯一操作行、载荷指纹、持久状态、**原子处理认领 (atomic processing claim)**。
- 崩溃追踪：
  1. Tern 提交 `T1:S204:book:1` 的意图，A1 认领；
  2. 快递在该键下原子创建 B77；
  3. 响应丢失，A1 超时并在本地记录 B77 前崩溃；
  4. 认领过期后 A2 发现未完成的本地意图，**保留同一键** 并查询；
  5. 查询返回 B77；A2 记录并继续监控面单就绪。
- 反模式：调用前就标记完成 → 发送前崩溃则丢失 S204；用新键盲目重发 → 可能产生 B78；本地认领或完成标志无法原子覆盖独立的快递事务；upsert 货件行不能对下单动作去重。
- **本地认领协调 worker；快递的键绑定保护远端效果；二者不可互相替代。**
- 无提供方幂等与可靠查询 → 此崩溃留下需人工调查的未解决结果。**超过 7 天**：阻止自动重建，先核实结果再授权下单。**本地记录不能延长提供方的保留保证。**

```python
# Idempotent booking with outcome-unknown recovery (illustrative)
def book_shipment(op, courier, store):
    # op.key is stable across attempts, e.g. "T1:S204:book:1"
    if not store.claim(op.key, worker_id=op.attempt_id):
        return "claimed_by_other_worker"
    existing = courier.lookup_by_key(op.key)          # resolve unknown outcome first
    if existing is not None:
        store.record_booking(op.key, existing.booking_id)
        return "recovered"
    try:
        result = courier.create(payload=op.payload, idempotency_key=op.key, timeout=3)
        store.record_booking(op.key, result.booking_id)
        return "accepted"
    except TimeoutError:
        store.mark_state(op.key, "outcome_unknown")     # never resend with a new key
        return "outcome_unknown"
```

**B77 如何在派送更新失败后存活 (explicit workflow states)**：

| 状态 State | 允许进入的证据 Evidence | 恢复/下一步 Recovery / next step |
|---|---|---|
| queued | 持久意图已提交 | 认领操作，开始远端工作 |
| remote-pending | 快递已接受，面单未就绪 | 在共享预算内监控就绪 |
| outcome-unknown | 超时后写效果不明 | 按已有操作键查询 |
| label-ready | B77 与可用面单已验证 | 持久化就绪，更新派送 |
| dispatch-update-pending | 就绪 B77 已保存，持久派送更新未完成 | **只恢复派送更新** |
| completed | 就绪面单与持久派送引用均已验证 | 允许屏幕显示成功 |

- A2 拿到 B77 并验证面单就绪后派送系统不可用 → **保留 B77，只恢复未完成的派送更新**；再建一个下单会重复已完成的效果。
- **条件式派送转换 (conditional transition)**：检查预期货件版本与下单代数 (booking generation)，防止旧下单覆盖新状态。派送持久存储 B77 引用后才标记完成。
- **对账 (reconciliation)**：定期比较持久意图、快递结果、派送引用 → 发现搁浅操作、恢复可恢复的缺失更新、标记分歧 —— **即使所有 worker 都报告健康**。
- 提供方支持的 **取消 (cancellation)** 是一个新业务动作，有自己的身份和可能失败；只在业务规则允许时使用；不能假设承运交接可逆。

**S205 谁修复、谁授权重放 (dead-letter ownership)**：
- 快递停机 → 有界重试与恢复。S205 **永久性无效目的地拒绝** → **死信异常 (dead-letter exception)**：等待诊断和受控处理的持久记录。
- 本地异常保留 **30 天**，含操作身份、源引用、拒绝原因、尝试历史、时间戳；未解决的必须在过期前升级并保存，不能静默删除。

| 角色/规则 Role / rule | 内容 Content |
|---|---|
| 修复负责人 Repair owner | Tern 派送 **数据管理员 (data steward)** 修复权威输入；被拒载荷保留在审计轨迹 (audit trail) |
| 重放审批人 Replay approver | **集成运维 (integration operator)** 确认不存在远端效果后授权恢复 |
| 指纹规则 Fingerprint rule | 业务意图不变 → 保留操作身份；修正后的载荷只有在提供方确认拒绝未绑定该键时才可沿用身份；否则在核实原结果后创建显式授权、关联的 **替换操作代 (replacement operation generation)**，绝不静默绕过冲突 |
| 重放检查 Replay checks | 限流重放、检查当前货件状态与代数、保护顺序、验证下游效果；S205 第 1 代绝不能覆盖已完成的第 2 代 |

- 没有诊断、负责人、重放权限、效果验证的死信队列 (dead-letter queue) 只是 **存放未完成的责任**。

**发现 HTTP 200 但面单 pending (silent errors)**：
- 记录：操作与尝试身份、源货件与版本、快递下单引用、状态转换、时间戳 → **源到目标血缘 (lineage)**，区分重复尝试与另一业务操作。
- 监控 **业务进度** 而非仅基础设施错误与限流：

| 指标 Metric | 说明 |
|---|---|
| 最老未完成操作年龄 Oldest unfinished-operation age | 核心告警 |
| 就绪面单新鲜度、队列滞后 Ready-label freshness, queue lag | 发现卡顿 |
| 死信年龄、dispatch-update-pending 数量 | 发现搁浅 |
| 对账不一致及其解决历史 Reconciliation mismatches | 发现分歧 |

- 告警 (alerting)：任何已接受货件 **5 分钟** 未完成 → 通知集成运维；无效数据异常 → 数据管理员，**30 分钟** 无人认领则升级 (escalate)。**状态 API 返回 HTTP 200 但 body 为 pending 不能计入完成数。**
- **运行手册 (runbook)**：识别受影响操作 → 任何重发前先查快递状态 → 指明授权恢复动作 → 事后验证派送引用。所有修复与重放决定都要审计。

<svg viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="800" height="250" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">S204 Workflow States｜S204 工作流状态</text>
  <g font-size="11" text-anchor="middle">
    <rect x="10" y="60" width="100" height="44" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="60" y="80">queued</text><text x="60" y="95">意图已持久</text>
    <rect x="135" y="60" width="115" height="44" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="192" y="80">remote-pending</text><text x="192" y="95">已接受，面单未好</text>
    <rect x="135" y="150" width="115" height="44" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="192" y="170">outcome-unknown</text><text x="192" y="185">超时 → 按键查询</text>
    <rect x="275" y="60" width="110" height="44" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="330" y="80">label-ready</text><text x="330" y="95">B77 + 面单已验证</text>
    <rect x="410" y="60" width="160" height="44" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="490" y="80">dispatch-update-pending</text><text x="490" y="95">只重试派送更新</text>
    <rect x="595" y="60" width="100" height="44" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="645" y="80">completed</text><text x="645" y="95">屏幕可显示成功</text>
    <rect x="595" y="150" width="190" height="44" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="690" y="170">dead-letter (S205)</text><text x="690" y="185">steward repairs · operator replays</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="110" y1="82" x2="133" y2="82"/><line x1="250" y1="82" x2="273" y2="82"/>
    <line x1="385" y1="82" x2="408" y2="82"/><line x1="570" y1="82" x2="593" y2="82"/>
    <line x1="60" y1="104" x2="135" y2="160"/><line x1="250" y1="160" x2="275" y2="104"/>
  </g>
  <text x="400" y="225" font-size="11" text-anchor="middle" fill="#444">reconciliation sweeps all states even when workers look healthy｜对账覆盖所有状态，即使 worker 都健康</text>
</svg>

### 练习：Nacre Facilities 徽章打印 (practice)

**English prompt**: *Provider permits 60 shared calls/min. Normally 15 new jobs/min, each 1 submission + 1 status lookup. Identical keyed submissions return one job; changed payloads conflict. Key lookup and dedup last 24 hours. Local exceptions last 7 days. J18 is durably accepted locally, creates remote print P9, times out, and crashes before recording P9. P9 later reports printed, but the facilities update fails. J19 has an invalid template. An operator proposes replaying an unresolved three-day-old job.*

参考解：
- **配额**：15 × 2 = 30 实时；剩余 30 分给恢复、对账、回填（含额外轮询），例如 恢复 15 + 对账 5 + 回填 ≤10。
- **重试策略**：worker 拥有；如 3 次、单次 3 s、执行截止 15 s、全抖动封顶指数退避 (capped exponential backoff with full jitter)；`Retry-After` 持久延期；SDK 重试关闭或计入预算；累计恢复期限必须 **&lt; 24 小时**（提供方去重窗口 (deduplication window)）。
- **J18 追踪**：操作键 `J18:print:1`，尝试 A1 超时崩溃 → A2 认领过期后用同一键查询 → 得到 P9 → 记录 → 监控至 printed → 设施更新失败 → 进入 facilities-update-pending，只重试设施更新 → 持久更新后才 completed 并显示成功。（memo 声称"恢复到 P9 提交接受后即可关闭 J18" —— 错。）
- **J19**：客户数据管理员修复权威模板；集成运维核实无远端效果后审批重放；变更后的指纹需新的关联操作代（或提供方确认键未绑定）；检查当前状态与代数、限流重放、验证下游。（memo 中"Nacre 自动模板重放授权"是虚构权威。）
- **三天前的旧任务**：已超过 **24 小时** 提供方去重窗口，原键不再保护 → **禁止自动重提交**；先核实远端是否已打印，再由审批人授权。本地异常保留 7 天只保存证据，不代表 7 天内重提交安全。
- **告警**：未完成任务年龄超过阈值（如 5 分钟）→ 集成运维；修复与重放决定写审计轨迹。

### 面试怎么说 / How to say it in the interview

**Q: A write call timed out. Do you retry? / 写请求超时要重试吗？**
> "A timeout only means I stopped waiting — the remote side may have done the work. So I classify it as outcome-unknown and resolve that first: if the provider supports idempotency keys and lookup, I look up by the same operation key, and either record the existing booking or retry with that same key. I never resend with a fresh key, because that's how you book a shipment twice."
>
> 中文：超时 = 结果未知；按同一操作键查询或重试；绝不用新键重发。

**Q: How do you design retries so they don't make an outage worse?**
> "One layer owns retries — usually the worker — with a small attempt count, per-call timeouts, an overall deadline, and capped exponential backoff with full jitter. I disable SDK and adapter retries or count them, because three layers of three is 27 calls. I honor Retry-After by durably scheduling the work later, and all callers share one admission limiter with explicit budgets for live, recovery, reconciliation, and backfill — backfill is the first thing to pause when quota drops."
>
> 中文：单层拥有重试、全抖动退避、关闭下层重试、遵守 Retry-After、共享限流与分项预算。

**Q: How do you catch silent failures?**
> "I monitor business progress, not just HTTP errors: the age of the oldest unfinished operation, dead-letter age, stuck intermediate states, and reconciliation mismatches between our intents, the provider, and the target system. A 200 with a 'pending' body never counts as completion. Alerts go to a named owner with a runbook that checks remote state before any resend."
>
> 中文：监控业务进度与对账不一致；200 + pending 不算完成；告警有负责人和运行手册。

**Q: What makes a dead-letter queue actually useful?**
> "Ownership and replay rules. A data steward repairs the authoritative input, an integration operator verifies there's no remote effect and approves replay, and the replay checks current state and generation so an old version can't overwrite a newer one. Records are retained long enough to escalate — otherwise a DLQ just stores unfinished responsibility."
>
> 中文：明确修复人、审批人、重放检查与保留期；否则 DLQ 只是存放未完成责任。

---

## 23. Data Contracts, Validation, and Schema Changes｜数据契约、校验与 Schema 变更

Source: https://www.educative.io/courses/forward-deployed-engineer/data-contracts-validation-and-schema-changes

### 要点 / Key ideas

**核心例子 Bracken Services（English prompt）**: *Two records both say `duration: 120`. Do they represent the same amount of work?*

```json
{"system":"Time","schema_version":"v1","duration":120,"status":"APPROVED"}
{"system":"Payroll staging","duration":120,"status":"PAID"}
```

- Time 记录 = **120 分钟**、可导出；Payroll 记录 = **120 小时**、已付款。按同名字段复制 → 工时 ×60，并虚假断言已付款。安全映射通过 **显式、版本化的解释 (explicit, versioned interpretation)** 保留业务含义。Bracken 集成只 **暂存已批准工时**，不执行付款。

**映射契约 (mapping contract)** 规定：源与目标含义、**字段级权威 (field-level authority)**、单位、**枚举 (enumerations)**、引用映射、冲突策略。

| 契约元素 Element | Bracken 内容 |
|---|---|
| 工人对照 Worker crosswalk | `(B1, Time, W17)` → `(B1, Payroll, P804)` |
| 条目身份 Entry identity | `(B1, Time, E41)` |
| 项目对照 Project crosswalk | 源项目 P9 → Payroll 项目 J22 |
| Time 权威 | 工作时长、项目、审批、条目修订版本 (revision) |
| Payroll 权威 | 付款状态与付款引用 —— 对本集成 **只读** |

- 标识符按 **租户 (tenant) + 源系统** 限定作用域 (scope)；邮箱和显示名可变，不能建立身份。对照未解决或归属冲突 → **异常**，而非猜测匹配或覆盖。
- 实体、操作、尝试身份保持区分；重试保留操作身份。
- **规范契约 (canonical contract) c1**：租户、条目身份、工人身份、源修订、`duration_hours`、项目引用、成本中心、资格 (eligibility)。规范表示是 **刻意选择的集成模型**：降低翻译复杂度，同时保留工作流所需的区分；同时保存 **原始源数据与来源 (provenance)**。
- Time `APPROVED` → 资格 `READY`；Payroll 的 `PAID` 仍归 Payroll 控制。

**E41 更新何时可接受 (validation rules)**：

| 校验类型 Validation type | 检查内容 Checks |
|---|---|
| 结构校验 Structural | 形状、必填字段、类型：`tenant`、`entry_id`、`employee_id`、`revision`、`schema_version`、事件类型；批准的 upsert 还需数值型 duration 和项目引用 |
| 语义校验 Semantic | 业务含义：支持的审批状态、声明的单位、正数时长、已批准的工人/项目对照、允许的状态转换、**修订顺序 (revision ordering)** —— 结构合法的数字仍可能不安全 |

**部分更新规则 (partial update rules)**：
- 缺少 `cost_center` → **保留** 现有值。
- 显式 `cost_center: null` → **清空**（该目标允许清空）。
- `VOID` → 使资格失效，并请求 Payroll 支持的作废转换；**绝不物理删除 (hard delete) 工资历史**。
- 批准的 upsert：把部分更新与已知状态合并后校验 **有效记录 (effective record)**；无法确定必需业务值 → 隔离。全量快照需要不同的缺省策略。
- 格式错误的标识符 → 格式规则失败；格式正确但未知的工人/项目 → **引用解析 (reference resolution)** 失败。都不能用显示名匹配、猜项目、强转负时长、丢弃不支持的状态。

**匹配练习答案**：

| 情况 Case | 契约结果 Contract result |
|---|---|
| `VOID` 事件 | 受支持的资格失效，不删除历史 |
| 缺少 `revision` | 结构拒绝（缺少必需元数据） |
| 部分更新 `cost_center: null` | 按目标契约清空成本中心 |
| 批准 upsert，duration = -120 | 语义范围拒绝 |
| 格式正确但未知项目 PX | 语义引用异常，需权威方解决 |
| 部分更新缺 `cost_center` | 保留现有成本中心 |

- 按拒绝类别路由修复：未解决引用 → **数据管理员 (data steward)**，而非让适配器规则发明匹配；待决期间记录保持阻塞。

**被拒修订 7 的去向 (quarantine &amp; repair)**：
- E41 revision 7：v1、W17、APPROVED、120、项目 PX；结构通过，语义失败（PX 无批准对照）。
- 目标提交前 **隔离 (quarantine)**，拒绝码 `UNKNOWN_PROJECT`；保存原始载荷、操作身份、源修订、源 schema、映射版本、引用数据版本、时间戳。
- 职责：时间数据管理员诊断 PX 并修复权威 Time 记录为 P9 → revision 8（仍为 v1）；批准的项目对照提供 P9→J22；集成运维确认无目标效果，按既定操作键与指纹规则批准受控重放；运维核验结果小时数、引用、资格、付款字段未变。
- **保持被拒的 revision 7 原样**，把 revision 8、修复决定、批准关联到它。编辑隔离载荷会毁掉解释失败原因的证据。

**Time v2 到来 (schema version dispatch)** —— v2 以小时表示时长、支持小数。**按载荷声明的源版本选择映射**：

| 源版本 Source version | 映射器 Mapper | 结果 |
|---|---|---|
| v1 | `time-v1-to-c1@1`：120 分钟 → 120/60 = 2 小时 | c1 |
| v2 | `time-v2-to-c1@1`：保留 2 小时，不换算 | c1 |

- 保留 v1 映射用于历史数据；不支持的源版本载荷 → 暂缓或隔离。
- 兼容性要在 **实际的生产方、消费方、校验器、存储** 上评估：新增可选 `note` 字段可能被容忍未知字段的适配器接受，却在拒绝额外字段的下游 schema 校验或摄取中失败。新状态 `APPROVED_PENDING_REVIEW` 要显式映射，未确认业务含义等价前不得当作 `APPROVED`。
- **漂移检测 (schema &amp; semantic drift)**：校验声明版本、监控字段结构与类型、标记未知枚举值和引用、用 **契约测试夹具 (contract test fixtures)** 跑语义检查。**数值类型不变时，结构校验检测不到单位变化。**

**重放该用哪种解释 (replay interpretation)** —— 先声明 **重放目的**，再选权威输入与解释：

| 目的 Purpose | 输入 Input | 结果 Result |
|---|---|---|
| 历史重建 Historical reconstruction | 保存的 revision 7 + v1 映射器 + 当时的引用上下文 | 2 小时，但 PX 仍未解决 → 预期得到原异常，无外部写 |
| 业务修复 Business repair | 批准的权威 revision 8（v1）+ 含 P9→J22 的批准引用版本 | 2 小时 + 已解决项目 |
| 当前状态守卫 Current-state guard | 应用 revision 8 前检查 E41 当前状态，应用时做 **条件修订检查** | 若 revision 9 已作废 E41 → 阻止 revision 8，即使映射正确 |

revision 8 的预期规范输出：

```json
{"tenant":"B1","entry_id":"E41","worker_id":"P804","source_revision":8,"duration_hours":2,"project_ref":"J22","eligibility":"READY"}
```

（缺 `cost_center` 则保留；绝不写 Payroll 付款状态。）

- **解释来源元组 (interpretation-provenance tuple)**：源与实体标识、源修订、事件与摄取时间；源 schema/API 版本、映射版本、引用数据版本、规范版本；结果目标引用或异常。修复时保留原始与重放两个元组，加目的、批准、当前状态证据、已验证目标结果。
- 重放仍遵守既定控制：新尝试身份；只在验证无效果和提供方指纹规则下复用操作身份；修正载荷遇到已绑定的冲突键 → 走授权替换流程；保证顺序、限流、下游效果验证；本地历史不能延长提供方去重/查询保证。

**诱人捷径的三个失败**：

| 捷径 Shortcut | 后果 Consequence | 防护 Prevention |
|---|---|---|
| 把保存的 v1 `120` 送进最新 v2 映射器 | 得到 120 小时而非 2 小时 | 版本分派 (version dispatch) |
| 用默认项目替代 | 工时记到错项目 | 权威修复 + 来源记录 |
| 在 revision 9 之后重放 | 作废后又恢复资格 | 当前修订守卫 |

再多重试也解决不了这些错误。

**让映射变更安全的证据 (contract test fixtures)**：

| 夹具 Fixture | 输入 Input | 预期结果 Expected outcome |
|---|---|---|
| 时长换算 | v1 `120`（分钟）/ v2 `2`（小时） | 都映射为 `duration_hours = 2` |
| 成本中心更新 | 缺省 / 显式 null | 保留 / 清空 |
| 未知项目 | 项目 PX | 隔离，报告未解决项目引用 |
| VOID 状态 | VOID | 受支持失效转换，不删记录 |
| 不支持的 schema 版本 | v3 | 阻塞直到有兼容映射 |
| 乱序修订 | revision 9 已是当前时来 revision 8 | 拒绝 revision 8 |
| Time 审批 | APPROVED | 映射为 READY，不写/不改 PAID |

- 测验要点：新增可选 `note` 字段，经过容忍未知字段的适配器后进入 **严格追加存储 (strict append storage)** → 需要 **包括严格存储在内的端到端测试** 才能称为兼容（适配器接受 ≠ 管道兼容；可选字段并非对所有消费者都兼容）。
- **映射修正影响已处理记录 = 数据迁移 (data migration)**：对代表性历史样本 **dry-run**（不写外部系统）→ 比较规范输出与异常数 → 调查意外变化 → 批准预期差异 → 识别受影响记录并迁移持久表示 → 核验目标小时、工人/项目关联、资格，且无重复效果。
- **连接器存储语义**：Palantir Data Connection 文档讨论增量 APPEND 事务中的 schema 不匹配及连接器特定恢复流程（暂停同步、版本化数据集、在支持协助下回滚 (roll back) 事务）—— 依赖具体连接器，**不保证原地 schema 演进**。批准迁移前按当前提供方文档核实客户 API 版本、自定义 schema、弃用 (deprecation) 通知、兼容要求、连接器恢复能力，并在代表性环境验证。

<svg viewBox="0 0 800 270" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="800" height="270" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">Boundary Validation &amp; Versioned Mapping｜边界校验与版本化映射</text>
  <g font-size="11" text-anchor="middle">
    <rect x="10" y="80" width="110" height="60" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="65" y="104" font-weight="bold">Source payload</text><text x="65" y="120">schema_version</text><text x="65" y="134">源载荷</text>
    <rect x="145" y="80" width="110" height="60" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="200" y="104" font-weight="bold">Structural</text><text x="200" y="120">shape · types</text><text x="200" y="134">结构校验</text>
    <rect x="280" y="80" width="110" height="60" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="335" y="104" font-weight="bold">Semantic</text><text x="335" y="120">units · refs · order</text><text x="335" y="134">语义校验</text>
    <polygon points="465,70 515,110 465,150 415,110" fill="#fef7e0" stroke="#e37400"/><text x="465" y="106">version</text><text x="465" y="120">dispatch</text>
    <rect x="545" y="45" width="120" height="40" rx="6" fill="#fff" stroke="#3367d6"/><text x="605" y="62">v1 mapper</text><text x="605" y="77">min ÷ 60</text>
    <rect x="545" y="135" width="120" height="40" rx="6" fill="#fff" stroke="#3367d6"/><text x="605" y="152">v2 mapper</text><text x="605" y="167">hours as-is</text>
    <rect x="690" y="85" width="100" height="50" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="740" y="106" font-weight="bold">Canonical c1</text><text x="740" y="122">+ provenance</text>
    <rect x="230" y="190" width="220" height="50" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="340" y="210" font-weight="bold">Quarantine 隔离</text><text x="340" y="226">raw + reason + versions; steward repairs</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="120" y1="110" x2="143" y2="110"/><line x1="255" y1="110" x2="278" y2="110"/><line x1="390" y1="110" x2="413" y2="110"/>
    <line x1="510" y1="100" x2="543" y2="68"/><line x1="510" y1="120" x2="543" y2="152"/>
    <line x1="665" y1="65" x2="688" y2="100"/><line x1="665" y1="155" x2="688" y2="122"/>
    <line x1="200" y1="140" x2="280" y2="188" stroke="#c5221f"/><line x1="335" y1="140" x2="340" y2="188" stroke="#c5221f"/>
  </g>
</svg>

### 练习：Fen Water 映射契约 (practice)

**English prompt**: *Tenant F1 has one approved meter crosswalk `(F1, source, M12) → (F1, Billing, A90)`. Source owns readings and revisions; Billing owns invoice and payment status. Partial updates: missing optional `quality_note` preserves it; explicit null is **forbidden**. v1 `reading_value` = cumulative liters; v2 = cumulative cubic meters; canonical = cumulative cubic meters. VALID means eligible for billing review, not INVOICED. RETRACT invalidates via supported transition, never deletes invoices. R6 revision 3 (v1, 2500, meter M99, VALID) was quarantined (no crosswalk); steward corrects to revision 4 with M12 (still v1); operator approves replay; provider confirms no effect and no bound key. Follow-up: revision 5 has already retracted R6.*

memo 中的错误：
1. "显式 null 可以清空 `quality_note`" —— 错，Fen Water 禁止显式 null（应拒绝），不能照搬 Bracken。
2. "v2 可用后取代 v1 解释，revision 4 的 2500 原样作为立方米" —— 错，按声明版本 v1 分派：2500 升 ÷ 1000 = **2.5 m³**。
3. "强制标准要求源修订变化就必须新业务操作身份" —— 虚构权威；提供方已确认无效果且键未绑定，可沿用操作身份 + 新尝试身份。

正确部分：作用域身份 `(F1, source, R6)`、M12→A90 批准对照、不用地址匹配；分类规则；VALID 只映射为账单审核资格；修复选 revision 4 + 显式 v1 映射器；应用前当前状态检查 + 条件修订守卫；**revision 5 已撤回 → 阻止过期的 revision 4**，不恢复资格、不删除发票。

四个测试（示例）：

```text
1. v1 reading_value 2500 (liters)      -> canonical 2.5 m3
2. v2 reading_value 2.5 (cubic meters) -> canonical 2.5 m3, no conversion
3. partial update with quality_note: null -> structural/semantic rejection (null forbidden)
4. revision 4 arrives after revision 5 RETRACT -> blocked by revision guard; no invoice deleted
```

### 面试怎么说 / How to say it in the interview

**Q: Two systems both have a `duration` field. Can you just map it? / 两个系统都有 duration，能直接映射吗？**
> "Not without a contract. Matching names don't mean matching meaning — in one system it's minutes approved for export, in the other it's hours already paid. I'd write a versioned mapping that converts units explicitly, records which system owns each field, and maps status values by business meaning. Payroll's PAID stays read-only to the integration."
>
> 中文：同名不等于同义；版本化映射、显式单位换算、字段归属、按业务含义映射状态。

**Q: The source releases v2 and changes units but not types. How do you handle it?**
> "Structural validation won't catch it — it's still a number. I dispatch on the declared schema version: v1 goes through the minutes-to-hours mapper, v2 through the hours mapper, both into the same canonical model, and I keep the v1 mapper for history. Unsupported versions get held. And I have contract fixtures — v1 120 and v2 2 must both produce 2 hours — that run on every mapping change."
>
> 中文：按声明版本分派映射器；保留旧映射；契约夹具覆盖关键例子。

**Q: A record fails validation because of an unknown reference. What happens?**
> "It's quarantined before any destination write, with the raw payload, rejection code, operation ID, and all version info. The data steward fixes the authoritative source, which produces a new revision; I don't edit the quarantined record or let an adapter guess a match. The operator approves replay, and before applying I check current state — if a newer revision already voided the entry, the replay is blocked."
>
> 中文：写前隔离并保留证据；数据管理员修复源；运维审批重放；应用前检查当前修订。

**Q: How do you know a schema change is safe?**
> "End-to-end evidence, not adapter acceptance. An optional field can pass a tolerant adapter and still break strict append storage downstream. I run the contract fixtures end to end, and if the change affects already-processed records, I treat it as a migration: dry-run on a historical sample, diff the canonical outputs and exception counts, get approval for intended differences, then migrate and verify there are no duplicate effects."
>
> 中文：端到端证据；影响历史数据视为迁移：dry-run、对比、批准、迁移、核验。

---

## 24. Designing for Client Security and Deployment Environments｜面向客户安全与部署环境的设计

Source: https://www.educative.io/courses/forward-deployed-engineer/designing-for-client-security-and-deployment-environments

### 要点 / Key ideas

**场景 Moss Manufacturing（English prompt）**: *Production approval is withheld even though the connector authenticates successfully in its sandbox: a support export leaves the approved region, and nobody has tested the production token-refresh route. Moss wants approved maintenance requests to become work orders in an externally hosted service.*
- 每个 **信任边界 (trust boundary)** 声明都需要：完整依赖清单、负责人、边界有效的证据。
- 请求含：请求人姓名、工作邮箱、站点、自由文本事件描述、可选照片。源系统拥有批准请求内容；目标服务拥有工单 ID 与执行状态。
- 第一版 **排除附件**：照片留在源端，连接器不抓取不转发；只把必要、批准的工单字段送到目标 —— **数据最小化 (data minimization)**。
- 信任边界 = 分隔受不同访问、网络或运营控制管理的组件。上线前需知道：每个组件和副本在哪、谁能访问、哪些路由可用、谁授权使用。"私有 VPC 里的加密数据库"只回答一部分。

**M52 的去向与停留 (data lifecycle inventory)** —— 追踪：私有源 API → 客户云连接器 → 加密持久意图存储 → 原始摄取 → 映射 → 目标提交 → 异常处理；同一清单还要包括 **遥测 (telemetry)、导出、备份 (backup)、删除流程、支持访问**。
- Moss 批准的保留期 (retention period)（**客户假设，非法律默认值**）：原始载荷 7 天、隔离载荷 30 天、审计元数据 180 天、备份 35 天。活跃意图与映射数据需要显式批准的完成与删除计划，不能悄悄沿用审计期。

| 位置/边界 Location | 内容 Contents | 保护/访问 Protection / access | 保留/删除 Retention | 负责人 Owner | 测试/证据 Evidence |
|---|---|---|---|---|---|
| 私有源 API | 姓名、邮箱、站点、描述；照片留源端 | 认证加密私有读；窄源读权限；禁用附件抓取 | 源方控制 | 源方；集成运维 | 验证私有路由与批准字段；确认照片未抓取/转发 |
| R1 VPC 持久意图 | 操作身份、批准最小字段、处理状态 | Moss 自有密钥加密；窄 worker 访问 | **未决**：需客户批准完成与删除计划 | 客户平台；集成运维 | 接受前已提交意图；重试保留操作身份；测试删除计划 |
| R1 VPC 原始摄取 | 抓取的请求内容（不含照片） | Moss 密钥加密；受限诊断访问 | **已批准**：7 天 | 客户平台；集成运维 | 验证过期与未授权读被拒；检查无照片 |
| R1 映射 → 批准的 R1 目标 | 只有必要批准的工单字段；目标引用与结果 | 经批准出站代理 (outbound proxy) 的认证 TLS；目标创建权限 + 单独批准的恢复读权限 | **未决**：映射副本删除计划；目标条款需隐私 (privacy)/法务 (legal) 确认 | 集成运维；目标服务负责人；隐私/法务 | 对比批准字段；核验 R1 处理方条款、权限、恢复查询 |
| R1 隔离/死信 | 被拒载荷；拒绝与解释来源 | Moss 密钥加密；管理员可查看；普通支持被拒 | **已批准**：30 天 | 数据管理员；集成运维；客户平台 | 缺站点夹具进入隔离且无写；验证访问与过期 |
| R1 本地遥测 / 独立审计 | 遥测：有界标识、转换、时间戳、耗时、错误类别；审计：操作者、动作、记录引用、原因 | 受限访问；审计单独保护；遥测不含敏感载荷、照片、凭证、令牌、请求体 | 遥测需客户批准；审计 **180 天** | 客户平台 | 扫描遥测敏感字段；验证审计访问与过期 |
| R1 批准导出 / 支持工具 | 批准的支持会话记录与合格派生导出 | **无常驻支持载荷访问**；限时批准访问；可审计会话 | 按批准删除指令删除派生导出；保全/冲突需客户决定 | 客户平台；集成运维；批准的服务支持负责人 | 普通支持被拒；限时访问记录操作者/记录/原因 |
| R1 备份 / 受限恢复 | 保留的连接器数据备份 | 按记录的密钥安排加密；受限恢复访问 | **已批准**：35 天；恢复后访问前重新应用删除指令 | 客户平台；集成运维 | 恢复测试备份并确认先重新应用删除指令 |

- 保留源修订、schema、映射版本、引用版本、时间戳、目标引用或异常（在批准保留期内）。原始数据支持诊断与重放，但无限期保留会违背策略。
- 认证加密传输 + 静态加密 (encryption at rest) + 显式 **密钥归属 (key ownership)**：Moss 拥有连接器密钥；批准服务的密钥安排单独记录。**加密无法防止有权解密的身份滥用。**

**需要审批决定的约束 (constraint register)**：Moss 合同只允许批准的工单字段在 **区域 R1** 由批准的处理方处理；新的存储、遥测、备份、支持路径都要满足。

| 约束 Constraint | 做法 Approach | 证据/审批 Evidence / approver |
|---|---|---|
| R1 处理 R1 processing | 连接器副本和批准的支持处理都放在 R1 | 存储、备份、处理方、支持配置；隐私/法务确认处理方条款与允许位置 |
| 受限访问 Restricted access | 工作负载权限、管理员角色、限时支持审批 | 安全团队依据权限与访问测试结果批准 |
| 保留与删除 Retention &amp; deletion | 记录活跃副本删除、备份过期、法律/合同保全、恢复行为 | 隐私/法务与数据所有者解决义务与保全 |
| 生产流程 Production workflow | 业务验收字段正确性与可见结果 | **变更审批方 (change authority)** 依据就绪证据批准切换 |

- 合规调研还要确定：数据分类 (data classification)、适用义务、司法辖区 (jurisdiction)、允许的处理方、所需证据、客户审批权限。**云区域选择器或供应商证书本身回答不了备份、支持、流程问题。**
- 仅有健康相关字段不足以判定 **HIPAA** 适用（HIPAA Security Rule 针对电子受保护健康信息 ePHI，分行政、物理、技术保障措施），需客户专家判定。
- 次要渠道会改变范围：**PCI SSC** 指出通过终端用户消息收发 **主账号 (PAN)** 会把该渠道及相关系统纳入 **PCI DSS** 范围 → 支持对话也属于调研范围。

**部署位置对比 (deployment placement)**：

| 部署 Deployment | 要求 Requirements |
|---|---|
| SaaS | 可接受的数据暴露、私有源连通、批准处理方、约定运营条款 |
| 客户云/VPC Client cloud / VPC | 客户管理的边界，仍需显式路由与运营归属 |
| 本地 On-premises | 运行时、密钥、补丁、支持都在客户设施与网络内 |
| 气隙 Air-gapped | 依赖全部本地化，批准的离线传输与更新；**外部令牌端点、托管模型、回调、包仓库、远程支持都不能成为依赖** |

- **受限出站 ≠ 气隙 (restricted outbound is not air-gapped)**。Moss 允许批准的出站连接 → 选 **R1 中客户管理的 VPC**：请求 API 私有可达、禁止公网入站。
- 连接器通过 **受控出站 TLS 代理 (controlled outbound TLS proxy)** 访问两个不同的批准外部目标：**工单 API** 和 **其 OAuth 令牌端点**。还要验证内部 DNS、私有源路由、客户密钥管理与 KMS (key management service)、**内部包镜像 (internal package mirror)**、本地遥测、R1 备份、批准的支持路径。无需托管模型。
- 图上画一条 private link 不够：提供方必须为该具体服务支持私有连通；这里用批准的出站代理。客户平台运维拥有运行时、代理、密钥、更新、遥测、备份；集成运维拥有处理与恢复。

<svg viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="800" height="300" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">Moss Deployment: Client VPC in R1｜客户 VPC（区域 R1）</text>
  <rect x="15" y="40" width="560" height="240" rx="12" fill="#f8f9fa" stroke="#3367d6" stroke-dasharray="6,4"/>
  <text x="30" y="58" font-size="11" fill="#3367d6">Client-managed VPC, region R1 — no public inbound｜禁止公网入站</text>
  <g font-size="11" text-anchor="middle">
    <rect x="30" y="75" width="120" height="50" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="90" y="96" font-weight="bold">Request API</text><text x="90" y="112">private · no photos</text>
    <rect x="185" y="75" width="140" height="50" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="255" y="96" font-weight="bold">Connector</text><text x="255" y="112">intent → map → submit</text>
    <rect x="360" y="75" width="110" height="50" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="415" y="96" font-weight="bold">Egress proxy</text><text x="415" y="112">allowlist 2 hosts</text>
    <rect x="30" y="150" width="120" height="40" rx="6" fill="#fff" stroke="#5f6368"/><text x="90" y="174">Secrets / KMS</text>
    <rect x="165" y="150" width="120" height="40" rx="6" fill="#fff" stroke="#5f6368"/><text x="225" y="166">Intent / raw (7d)</text><text x="225" y="181">Moss keys</text>
    <rect x="300" y="150" width="120" height="40" rx="6" fill="#fff" stroke="#c5221f"/><text x="360" y="166">Quarantine (30d)</text><text x="360" y="181">steward only</text>
    <rect x="435" y="150" width="125" height="40" rx="6" fill="#fff" stroke="#5f6368"/><text x="497" y="166">Telemetry (redacted)</text><text x="497" y="181">audit 180d</text>
    <rect x="30" y="210" width="120" height="40" rx="6" fill="#fff" stroke="#5f6368"/><text x="90" y="234">Package mirror</text>
    <rect x="165" y="210" width="120" height="40" rx="6" fill="#fff" stroke="#5f6368"/><text x="225" y="226">Backups (35d)</text><text x="225" y="241">re-apply deletions</text>
    <rect x="300" y="210" width="260" height="40" rx="6" fill="#fff" stroke="#5f6368"/><text x="430" y="226">R1 support tooling, time-limited, audited</text><text x="430" y="241">无常驻支持访问</text>
    <rect x="610" y="55" width="175" height="50" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="697" y="76" font-weight="bold">Work-order API (R1)</text><text x="697" y="92">approved processor</text>
    <rect x="610" y="125" width="175" height="50" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="697" y="146" font-weight="bold">OAuth token endpoint</text><text x="697" y="162">must be allowlisted too</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="150" y1="100" x2="183" y2="100"/><line x1="325" y1="100" x2="358" y2="100"/>
    <line x1="470" y1="95" x2="608" y2="80"/><line x1="470" y1="108" x2="608" y2="150"/>
  </g>
</svg>

**M52 如何证明边界有效 (boundary tests)** —— 先提交意图再回复 "accepted for processing"；重试保留操作身份，每次执行新尝试身份。

| 失败 Failure | 预测与修正 Prediction &amp; correction | 测试 Test |
|---|---|---|
| 令牌续期 Token renewal | 代理只放行工单 API 主机 → 初始令牌可用但续期失败；批准独立的令牌端点（测验正确答案 C：不要放开所有出站，也不要用初始令牌的再次成功调用当证据） | 过期后测试续期；验证未批准目标仍被阻断 |
| 支持导出 Support export | R1 数据库保护不了被复制到无限制笔记本或全球错误追踪器的描述 → 移除该路径、遥测脱敏 (redaction)、用批准的 R1 支持工具 | 检查日志与导出中的敏感字段 |
| 恢复 Restore | 恢复旧备份可能重新引入已删除记录 → 暴露恢复数据前重新应用记录的删除指令 | 验证合格的活跃副本与派生导出已删除 |

- 备份在 35 天到期前仍受保护 —— **如实报告，不声称立即擦除**。保全与保留冲突需客户显式决定。原始数据过期后，单独保留的元数据可解释结果，但重放必须从授权源重新获取，或报告原始载荷不可用。
- 人员边界也要测：管理员能查看隔离、普通支持被拒、批准的限时支持会话记录谁因何访问了哪条记录。

**认证之外必须通过的就绪证据 (readiness evidence)**：
1. 批准字段与缺失必填站点的契约夹具（后者进入隔离且无目标写）。
2. 端到端请求恰好创建一个工单并显示已验证目标 ID。
3. 重复投递不产生第二个工单；创建后超时通过已验证的目标幂等与查询恢复契约解决。
4. 拒绝授权与过期令牌恢复。
5. 敏感数据检查：隔离、遥测、支持导出、删除与恢复行为。
- 沙箱 (sandbox) 成功留有缺口：生产代理规则、目标租户权限、配额分配、实际支持访问都不同 → 用批准的生产连通性检查 + **严格有界的金丝雀 (canary)** 补齐。
- OpenAI 的 FDE 描述同样强调：代表性任务与困难异常、可靠性与人工审核、权限、监控、清晰的客户职责。

**切换：W880 已存在时 (cutover)**：
- 客户批准的 **变更单 (change ticket)**：指定审批人、窗口、操作人、**停止条件 (stop conditions)**、人工回退 (manual fallback)。
- 渐进：20 个批准请求的 **无写映射比对** → 1 个站点 5 个请求的生产金丝雀 → 受监控的单站点试点 → 扩大范围。
- 金丝雀验收：5 个请求字段正确、目标引用已验证、无重复、无禁止字段泄露、令牌续期与异常路由成功。出现禁止披露、重复外部效果、未解决结果 → **暂停新提交**。
- M52 创建了 W880 但缺陷导致本地显示未更新：**回滚 (rollback) 连接器代码不会删除 W880**。暂停写入 → 确认远端结果 → 对账 (reconcile) 本地引用 → 再恢复提交。若确需取消，用目标支持的取消（单独授权与核验）；**绝不盲目重建工单**。
- 移交内容：仪表盘 (dashboard)、告警负责人、异常队列、凭证轮换 (credential rotation)、更新流程、删除与恢复运行手册、支持规则、升级联系人。
- **安全决策属于 CLIENT 每一步**，因为每一步都约束能建什么、能运营什么。

### 练习：Vale Archives 气隙部署 (practice)

**English prompt**: *Document identifiers and extracts must remain inside an air-gapped records network. Source and catalog APIs, token issuer, secrets, audit storage, backup service, and an approved model runtime are local. The client verifies signed offline update packages; client operators provide support without remote connection. Retention: raw 3 days, quarantine 14 days, audit 90 days, backups 28 days; reapply deletions before exposing restored records. Security owner approves controls; records owner confirms retention; change authority approves rollout. Catalog creation returns a durable entry ID, supports lookup by operation identity and authorized cancellation, but no deletion. For operation V18, creation succeeds as C77; the connector crashes before saving the response.*

参考解：
- **部署草图**：所有依赖在气隙网络内 —— 本地源 API、目录 API、本地令牌签发者、本地密钥、本地审计存储、本地备份、本地批准模型运行时、本地包与签名离线更新；**无出站代理、无外部令牌端点、无远程支持**（不能复用 Moss 方案）。
- **生命周期控制表**：原始 3 天、隔离 14 天、审计 90 天、备份 28 天 + 恢复前重新应用删除；遥测脱敏；支持由本地运维且可审计。
- **四个就绪测试**：
  1. V18 崩溃后按操作身份查询 → 找到 C77，不再创建第二条。
  2. 尝试任何外部网络调用（令牌、包、遥测）→ 被阻断，系统仍可运行。
  3. 未签名或签名无效的更新包 → 被拒绝安装。
  4. 恢复 28 天内备份 → 暴露前重新应用删除指令，已删除记录不可见。
- **切换与移交**：无写比对 → 有界金丝雀 → 单库试点 → 扩大；停止条件；人工回退；本地运维运行手册、离线更新流程、告警负责人。
- **C77 恢复**：先用本地操作身份查询恢复 C77；代码回滚删不掉 C77；取消是单独授权的业务动作。审批问题（保留义务、处理义务）交给记录负责人确认，不自称合规。

### 面试怎么说 / How to say it in the interview

**Q: The connector works in the sandbox. Why isn't it ready for production? / 沙箱可用为何不能上生产？**
> "Because authentication is only one boundary. I need to show where every copy of the data lives — intent store, raw payloads, quarantine, telemetry, exports, backups — who can access each, and how long each is kept, all inside the approved region. And I need tests for boundaries that only show up later: token renewal through the egress proxy, support exports, and restoring a backup without resurrecting deleted records."
>
> 中文：认证只是一个边界；要证明每个数据副本的位置、访问、保留，并测试续期、导出、恢复等后期边界。

**Q: The customer says "no data leaves our network." How does that change your design?**
> "First I clarify whether that means restricted egress or truly air-gapped — they're different. With restricted egress, I can run in their VPC and allowlist specific hosts through a proxy, including the OAuth token endpoint, which people often forget. If it's air-gapped, every dependency has to be local — token issuer, model runtime, package mirror, telemetry — updates come as signed offline packages, and support is their operators with no remote access."
>
> 中文：先区分受限出站与气隙；前者 VPC + 代理白名单（含令牌端点）；后者一切依赖本地化、离线签名更新、本地支持。

**Q: How do you approach compliance requirements like HIPAA or PCI?**
> "I don't claim compliance myself — I discover data classifications, jurisdictions, permitted processors, and who approves, then design to their requirements and produce evidence. I also look for secondary channels: PCI scope expands if card numbers show up in support chat, for example. A region selector or a vendor certificate doesn't answer backup, support, or workflow questions."
>
> 中文：不自称合规；调研分类、辖区、处理方、审批人；注意次要渠道；区域和证书不能回答所有问题。

**Q: Walk me through a safe cutover.**
> "A client-approved change ticket with named approvers, a window, stop conditions, and a manual fallback. Then stages: a no-write comparison on 20 real requests, a five-request canary at one site, a monitored one-site pilot, then wider rollout. If the canary shows a duplicate, a leak, or an unresolved outcome, we pause new submissions. And if a remote record was created but our side failed, rolling back code doesn't delete it — I reconcile the reference, never blindly recreate."
>
> 中文：变更单 + 停止条件 + 人工回退；无写比对 → 金丝雀 → 单站试点 → 扩大；回滚不删远端记录，对账而非重建。

---

## 25. Practice Rounds and Self-Review Rubric｜练习轮与自评量表

Source: https://www.educative.io/courses/forward-deployed-engineer/practice-rounds-and-self-review-rubric

### 要点 / Key ideas

- 目标：建一个 **三轮作品集 (three-round portfolio)** —— 每个客户一个初始设计 + 一个 **单独保存的** 追问修订。有用的结果是：当容量、新鲜度或权限变化时 **改变承诺的证据**。
- 节奏（练习建议，非标准面试时限）：每个初始设计 **12 分钟**、每个追问 **3 分钟**；先保存初始设计再处理新约束；六个回答都完成并保存后才看参考答案。
- 用 CLIENT 组织；区分已确认事实、工作假设、未解决问题。

**每个初始设计的六项产出 (six outputs)**：

| 产出 Output | 内容 Content |
|---|---|
| 结果与范围 Outcome &amp; scope | 初始工作流、可衡量目标、排除项、完成标准 |
| 接口清单 Interface inventory | 支持/拟议的连接、认证方式、网络路径、权威字段、系统身份、负责人 |
| 操作追踪 Operation trace | 一个操作经过 请求接受 → 持久处理 → 业务完成 → 用户可见确认，每阶段所需证据 |
| 数值可行性 Numerical feasibility | 计算过程、输入假设、限制性约束、**估算不能证明什么** |
| 控制与恢复 Controls &amp; recovery | 失败场景、结果不确定的操作、授权检查、部署保护、未解决异常的归属 |
| 推荐 Recommendation | 最小可行实现、运营负责人、被否方案及理由、下一步验证 |

- 追问时：更新受影响的承诺、操作追踪、权衡分析；原始设计、追问修订、后续更正 **分开保存，不覆盖**。

### Round 1: Northstar — 审批到排产 (approval → scheduling)

**English prompt**: *Planners manually copy approved releases into Scheduling (median 20 min); pilot target 5 min in normal operation without scheduling unapproved work. Approval owns `release_id`, revision, approval state, quantity; Scheduling owns `job_id` and execution state; an approved item crosswalk links item IDs. Source: read-only API-key REST feed with stable continuation positions, deletes, 7-day retention. Destination: workload OAuth, conditional job creation using an expected release revision, atomic create dedup + lookup under a caller-supplied operation ID for 7 days; 2 calls per release. Quota 60/min with 12 reserved; arrivals 18/min; outage leaves 120 queued. Follow-up: total quota falls to 40 (12 still reserved).*

参考解：
- **薄切片 (thin slice)**：批准 VPC 主机上的连接器轮询 Approval，为每个合格的 release 代 (generation) 创建一个 Scheduling job，持久链接两者；先从批准的物料集合开始；未解决映射或审批异常 → Operations。
- **追踪 R-81**：
  1. 持久化 release R-81 revision 4 及其源位置，再推进轮询检查点；拒绝不支持记录，防止过期修订或删除事件错误恢复资格。
  2. 验证审批状态与物料映射；以操作 ID `R-81:schedule:1` 持久记录排产意图（含源修订与批准载荷）；每次执行唯一尝试 ID，重试保留操作 ID。
  3. 用批准的 OAuth 工作负载身份提交针对 revision 4 的 **条件创建 (conditional create)**；验证 Scheduling 确实会拒绝过期修订和已撤销审批。API 接受 ≠ job 就绪，保持 pending。
  4. 创建超时 → outcome-unknown；7 天查询窗口内用原操作键查是否已创建 J-620；**稳定操作 ID 防重复的前提是 Scheduling 对该键原子去重**；超过 7 天暂停自动重试，调查后再创建。
  5. 与 Scheduling 负责人约定哪个 job 状态算交接完成；验证该状态与 R-81↔J-620 持久链接后才标记完成；后端确认后才更新计划员的成功状态。

```text
Baseline capacity
  budget    = 60 - 12 = 48 calls/min
  capacity  = 48 / 2  = 24 releases/min
  net drain = 24 - 18 = 6 /min
  recovery  = 120 / 6 = 20 min (idealized)
  -> budget extra polls, retries, reconciliation separately; capacity != 5-min latency

Follow-up: quota 40, 12 reserved
  budget    = 40 - 12 = 28 calls/min
  capacity  = 28 / 2  = 14 releases/min
  backlog   = 18 - 14 = +4 /min (grows)
  -> retract 5-min commitment; negotiate quota, supported batching, or narrower admitted scope
  -> reject "add workers" (fixed API budget)
```

- 负责人：集成工程 = 运行时与恢复；Operations = 业务异常；Scheduling 负责人 = 验证条件写语义。

### Round 2: Meadow — 让每小时文件有用 (hourly file)

**English prompt**: *Coordinators spend a median 15 min assembling stock evidence for transfer planning; goal 7 min, with displayed stock changes no more than 75 min old. Stock's only interface: hourly full CSV snapshots over internal SFTP with a producer manifest (file identity, snapshot boundary, row count, checksum, schema version). Next snapshot ≤60 min after a change; publication ≤5 min; verify+apply ≤5 min. Absence means removed, not zero. 12,000 rows × ~250 bytes. Planner: read-only API with mTLS; approved SKU crosswalk. Warehouse network only; planning is human-approved; no reservation/execution interface. Follow-up: a stakeholder demands 15-minute visibility with unchanged interfaces.*

参考解：
- 推荐 **内部只读视图**：经批准 SKU 对照把已验证库存快照与只读计划证据 join，支持人工调拨计划，不声称预留或执行。
- 接收文件 F-31 及 manifest → 暂存 12,000 × 250 = 3,000,000 字节（约 **3 MB**）→ 校验校验和 (checksum)、行数、schema、映射。持久暂存 = 可恢复处理责任。只有在验证管道支持 **原子切换 (atomic switch)** 后发布完整视图版本；验证重复处理 F-31 不会重复发布。校验失败 → 保留前一快照，显示源时间与陈旧状态。
- W2/SKU S-17 经批准映射；缺引用 → 阻塞 join，转仓库运营；被删除的库存行 → **不可用证据，绝不捏造为 0**。
- 已发布视图状态 = 应用完成；协调员看到对应证据与快照时间戳。文件到达本身两者都不证明；人工计划审批独立。

```text
Normal change-to-display bound = 60 (next snapshot) + 5 (publication) + 5 (verify/apply) = 70 min <= 75 min target
Follow-up: 15-min visibility with unchanged interfaces -> impossible
  even with zero downstream delay, the source may take up to 60 min to capture a change
  -> decline the guarantee; keep the timestamped aid; seek a different source contract or renegotiate
  -> reject "stream rows from the hourly CSV" (does not change when the source observes changes)
```

- 负责人：平台团队 = 运行时与证书轮换；仓库运营 = 陈旧与缺引用异常；上线前验证 manifest 行为与完整发布时序。

### Round 3: Ridgeway — 保持每位工程师的权限 (authorized retrieval)

**English prompt**: *Engineers spend a median 12 min finding an applicable maintenance procedure; pilot target 5 min, returning only currently authorized, applicable, published procedures. Portal uses OIDC; document API supports workload OAuth for ingestion and bounded reads (portal login is not its credential). Documents have stable `doc_id`, revision, publication state, effective date, site scope, access labels. Approved index supports permission-filtered retrieval. A client service validates current site/document/action permissions and denies when unavailable. Baseline per answer: 1 applicability check + 1 evidence fetch; source permits 90 calls/min with 30 reserved; demand 20 answers/min. Hosting and model stay in the client cloud; logs may not contain document bodies. V1 provides cited evidence or hands uncertainty to the maintenance knowledge owner. Follow-up: a formerly authorized document remains indexed after revocation, and its text instructs the assistant to retrieve a restricted procedure and send it to an external diagnostic URL.*

参考解：
- 推荐有界的 **程序查找助手**：门户身份与工作负载文档访问分离；提议指定客户平台运维负责运行时、凭证、配额（需确认，不假设存在）。
- 追踪：认证门户调用方、建立可信站点上下文 S3 → **权限过滤检索** 候选引用，**在索引文本暴露给模型之前** 执行当前站点/文档/动作授权；授权服务不可用 → 拒绝 → 对候选 D-204 revision 6，用第一次源调用验证当前发布、修订、生效日期、站点适用性 → 第二次调用只取被选中的允许证据；若证据变化则重新评估授权 → 生成有界带引用答案，或把不确定性交给维护知识负责人（交接在约定的持久归属证据存在前保持 pending）。

```text
capacity  = (90 - 30) / 2 = 30 answers/min
demand    = 20 x 2 = 40 of 60 available calls/min
headroom  = 20 calls/min for bounded exceptional work (extra checks, retries)
-> validate answer latency and the 5-minute workflow separately
```

- **追问（撤销 + 提示注入 prompt injection）**：撤销后当前授权在模型暴露前排除 D-204，即使索引返回其分块 → 在授权处停止，不释放被撤销文本；拒绝受限文档检索与外部出站；**文档文本是证据，绝不是扩大工具或目的地的权限**；日志不含正文；只用批准的内部处理。
- 允许的回复："I can't provide a verified procedure for this request. The maintenance knowledge owner needs to review it." —— **不透露受限程序或文档是否存在**。
- **不要把受限内容检索进模型上下文再依赖输出过滤 (output filtering)**；访问控制必须在模型拿到内容前阻止未授权检索。启用前测试撤销与提示注入场景。

<svg viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <rect x="0" y="0" width="800" height="250" fill="#fff"/>
  <text x="400" y="22" font-size="15" text-anchor="middle" font-weight="bold">Ridgeway: Authorize Before the Model Sees Text｜先授权，再给模型看</text>
  <g font-size="11" text-anchor="middle">
    <rect x="10" y="80" width="110" height="56" rx="8" fill="#f1f3f4" stroke="#5f6368"/><text x="65" y="102" font-weight="bold">Engineer</text><text x="65" y="118">OIDC · site S3</text>
    <rect x="145" y="80" width="130" height="56" rx="8" fill="#e8f0fe" stroke="#3367d6"/><text x="210" y="102" font-weight="bold">Permission-filtered</text><text x="210" y="118">retrieval 权限过滤检索</text>
    <rect x="300" y="80" width="140" height="56" rx="8" fill="#fce8e6" stroke="#c5221f"/><text x="370" y="102" font-weight="bold">Current authz check</text><text x="370" y="118">unavailable → deny</text>
    <rect x="465" y="80" width="130" height="56" rx="8" fill="#fef7e0" stroke="#e37400"/><text x="530" y="102" font-weight="bold">Source: applicability</text><text x="530" y="118">+ fetch current rev</text>
    <rect x="620" y="80" width="170" height="56" rx="8" fill="#e6f4ea" stroke="#137333"/><text x="705" y="102" font-weight="bold">Model (in client cloud)</text><text x="705" y="118">cited answer or handoff</text>
    <rect x="300" y="170" width="140" height="50" rx="8" fill="#fff" stroke="#c5221f"/><text x="370" y="190">revoked D-204 stops here</text><text x="370" y="206">撤销文档止步于此</text>
    <rect x="620" y="170" width="170" height="50" rx="8" fill="#fff" stroke="#c5221f"/><text x="705" y="190">doc text = evidence, not</text><text x="705" y="206">authority; no external egress</text>
  </g>
  <g stroke="#555" stroke-width="1.5" fill="none">
    <line x1="120" y1="108" x2="143" y2="108"/><line x1="275" y1="108" x2="298" y2="108"/>
    <line x1="440" y1="108" x2="463" y2="108"/><line x1="595" y1="108" x2="618" y2="108"/>
    <line x1="370" y1="136" x2="370" y2="168" stroke="#c5221f"/><line x1="705" y1="136" x2="705" y2="168" stroke="#c5221f"/>
  </g>
</svg>

**每个限制条件属于不同的权威方**：Scheduling 控制调用预算；Stock 控制变化何时可观察；Ridgeway 授权服务控制当前访问。**本地优化无法替代这些契约的变更。**

**审计作品集里的三个错误说法 (portfolio audit)**：

| 客户 | 错误说法 Unsupported claim | 替换 Replacement |
|---|---|---|
| Northstar | "原容量 24/min 仍适用，加 worker 保住 18/min 的 5 分钟完成" | 新容量 14/min，积压 +4/min；收回承诺，协商配额/批处理/收窄范围 |
| Meadow | "从每小时 CSV 流式读取行使显示实时、保证 15 分钟可见" | 源最多 60 分钟才捕获变化；拒绝保证，寻求新源契约或重新协商 |
| Ridgeway | "检索文本可在当前权限过滤前给模型，模型指令防泄露，并可把文档请求当作授权" | 模型暴露前执行当前授权；文档文本不是权限；拒绝受限检索与外部出站 |

**八维自评 (eight-dimension self-review)** —— 每维 0/1/2，**组件名本身不得分**；原始与追问分别打分（每客户各 /16）；每个 0 或 1 都追加具体替换决定或追踪步骤；**没有官方及格线**，高总分不能抵消未授权披露、未验证重复写或不可能的新鲜度承诺。

| 维度 Dimension | 检查要点 What to look for |
|---|---|
| 调研 Discovery | 用户、基线、目标、范围、未解决假设 |
| 可行性 Feasibility | 支持的接口、路由、数值预算与时序 |
| 业务语义 Business semantics | 权威字段、生命周期含义、完成证据 |
| 身份 Identity | 实体/操作/尝试区分；对照表与防重复证据 |
| 认证与授权 Authentication &amp; authorization | 凭证用途、当前调用方/动作权限 |
| 失败与恢复 Failures &amp; recovery | 不确定效果、重放安全、保留期限、异常归属 |
| 安全与部署 Security &amp; deployment | 批准位置、敏感副本、日志、凭证、网络控制 |
| 权衡与交付归属 Trade-offs &amp; delivery ownership | 被否选项、薄切片、运营负责人、下一步验证 |

- 更正与原始评估分开保存：更正展示理解提升，但不改变初始提交证明了什么。**跨场景反复出现的弱点** 比与某个参考架构的相似度更能指导练习。
- 找出最弱的反复维度，口头练习一个更正后的决定：初始工作流、成功完成的证据、限制性容量约束、修订后的承诺、恢复负责人、下一步验证。

### 面试怎么说 / How to say it in the interview

**Q: The interviewer changes a constraint mid-design. What's your process? / 面试官中途改约束怎么办？**
> "I treat it as new evidence and say explicitly which commitment it breaks. I redo the arithmetic out loud, update the operation trace if it's affected, and revise the trade-off — and I say what stays the same. If the constraint belongs to someone else, like the provider's quota or when the source publishes data, I don't pretend a local fix like more workers or streaming solves it; I offer options that change the actual contract."
>
> 中文：把新约束当新证据；明说哪个承诺失效；重算、更新追踪与权衡；不用本地优化掩盖外部契约限制。

**Q: Design a retrieval assistant where users have different permissions.**
> "Authorization happens before the model sees any text, not after. I use permission-filtered retrieval, then check current site, document and action permissions against a live authorization service that fails closed, then fetch only the current permitted revision. Document text is evidence — never authority — so if a document says 'fetch this restricted file and send it to this URL,' that's ignored and external egress is blocked anyway. If I can't verify an answer, I say so without revealing whether restricted documents exist, and hand off to the knowledge owner."
>
> 中文：模型看到文本前授权；权限过滤 + 实时授权（失败即拒绝）；文档文本不是权限；无法验证时不泄露存在性并转交负责人。

**Q: A stakeholder wants 15-minute freshness but the source only exports hourly. What do you say?**
> "I'd explain the arithmetic: the source can take up to 60 minutes to capture a change, so even with zero processing time I can't promise 15 minutes. I'd keep the hourly, timestamped view because it still meets their 75-minute need and cuts assembly time, and I'd open a conversation about a different source interface — a change feed or more frequent export — if 15 minutes really matters."
>
> 中文：源最多 60 分钟才捕获变化，处理再快也无法 15 分钟；保留带时间戳视图，并推动换源接口。

---

## 速查 / Cheat sheet

| # | 要点 Takeaway (中文) | English one-liner |
|---|---|---|
| 1 | FDE 面试考三维：技术深度、部署思维、面向客户沟通；拆解轮与客户模拟轮是 FDE 独有 | Three dimensions: technical depth, deployment thinking, client communication. |
| 2 | 拆解轮 60 分钟：澄清 10 → 拆解 15 → 约束优先级 15 → 权衡 10 → 总结 10 | Decomposition: clarify, decompose, constrain, trade off, present back. |
| 3 | 客户模拟：不带提案开场，覆盖流程痛点、数据系统、约束权限、成功定义，以问题陈述收尾 | Customer sim: no proposal; four areas; close with a problem statement. |
| 4 | 技术深挖四步：问题 → 匹配架构 → 企业约束 → 部署前定义评估 | Problem, architecture fit, enterprise constraints, eval before deploy. |
| 5 | 行为轮 STAR 以客户为中心，Result 必须说客户侧改变 | STAR centered on the customer; the result is what changed for them. |
| 6 | FDE 系统设计的第一回答是"能改变设计的问题 + 有范围的第一版"，不是架构图 | First answer = questions that could change the design, then a scoped v1. |
| 7 | CLIENT：Context、Landscape、Integration points、End-to-end、Non-happy paths、Trade-offs；各步互相约束 | CLIENT steps constrain each other; a failed interface check sends you back to scope. |
| 8 | 区分实体身份与字段归属；冲突值并列展示带时间戳，不"最新者胜" | Separate entity identity from field ownership; show both values with timestamps. |
| 9 | 每个连接检查三件套：接口 + 凭证 + 网络路径；自定义代码补不出权限 | Interface + credential + network path; code can't create a missing permission. |
| 10 | 四个确认边界：请求接受、持久责任、业务完成、用户可见成功；202 ≠ 完成 | Acceptance ≠ durable responsibility ≠ business completion ≠ user-visible success. |
| 11 | 实体/操作/尝试三种身份；重试保留操作键；超时 = 结果未知 | Retries keep the operation key; a timeout means outcome-unknown. |
| 12 | 容量 = (配额 − 保留) / 每操作调用数；净消化 = 容量 − 到达；到达 ≥ 容量则积压增长，收回承诺 | Capacity = (quota − reserved) / calls per op; if arrivals exceed it, retract the promise. |
| 13 | 加 worker、加队列不增加 API 预算；流式读取改变不了源何时捕获变化 | Workers and queues don't add API budget; streaming doesn't change source timing. |
| 14 | 快照绑定变更位置；inbox 与检查点同事务，否则先记录后检查点 | Tie snapshots to change positions; commit inbox and checkpoint together. |
| 15 | Webhook 只是提示：验签 → 持久化 → 再确认；保留周期权威扫描 | Webhooks are hints; durable ingress before ack; keep the authoritative sweep. |
| 16 | 登录 ≠ API 授权；ID token ≠ access token；交互用授权码 + PKCE，后台用客户端凭证 | Login isn't API authorization; auth code + PKCE interactive, client credentials for jobs. |
| 17 | 连接器宽权限绝不变成用户权限：可信租户、行级授权、策略失败即拒绝、字段投影 | Connector access never becomes user permission; fail closed; project fields. |
| 18 | 单层拥有重试、全抖动退避、遵守 Retry-After、共享限流与分项预算；监控业务进度与对账 | One retry owner, full jitter, shared limiter; monitor business progress and reconcile. |
| 19 | 数据契约按声明版本分派映射；隔离保留原始证据；重放先声明目的并做当前修订守卫 | Version-dispatched mappings; quarantine with provenance; guard replay by current revision. |
| 20 | 安全是设计输入：追踪每个数据副本的位置、访问、保留；受限出站 ≠ 气隙；先授权再给模型看文本 | Trace every copy; restricted egress isn't air-gapped; authorize before the model sees text. |
