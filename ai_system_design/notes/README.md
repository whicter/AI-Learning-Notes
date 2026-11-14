# AI 系统设计 · 零基础笔记

> 从 Educative 三门订阅课里挑出值得读的部分，按"完全没接触过 AI"的起点重写，2026-10-26 完成。面试级内容由另一路整理进了 06，两边互相链接、不重复。
> **原课不用再读**。图都是我自己画的 SVG（在 `images/` 里），没有复制课程图片。
> 面试冲刺版在 [../06-ai-system-design.md](../06-ai-system-design.md)。这里是它的前置课：先看懂这里，再去看 06。

## 阅读顺序

| # | 笔记 | 讲什么 | 约需时间 | 来自 |
|---|---|---|---|---|
| 01 | [LLM 到底是什么](01-llm-basics.md) | 神经网络（neural network）、token、embedding、attention、逐字生成、temperature | 25 分钟 | GenAI 课 Ch.2 |
| 02 | [推理为什么贵、怎么省、怎么估算](02-inference-and-estimation.md) | prefill/decode、KV cache（key-value cache，键值缓存）显存（GPU memory）、量化（quantization）、缓存、连续 batching（continuous batching）、GPU 估算（**含对课程公式的纠错**） | 35 分钟 | GenAI 课 Ch.2–3 + 补充 |
| 03 | [GenAI 系统长什么样](03-genai-system-architecture.md) | SCALED 框架（framework） vs 06 的框架、ChatGPT 式对话系统、RAG（retrieval-augmented generation，检索增强生成）系统 | 25 分钟 | GenAI 课 Ch.4、5、11 |
| 04 | [Agent 入门](04-agent-basics.md) | 模型 vs agent、循环、三大组件、三层记忆（memory）、六种编排（orchestration）、什么时候不该用 agent | 30 分钟 | Agentic 课 Ch.1 + 附录 |
| 05 | [让 agent 可信](05-agent-safety.md) | 三个关口的护栏（guardrails）、HITL（human-in-the-loop，人在回路）/HOTL（human-on-the-loop，人在环上监督）/HATL（human-above-the-loop，人在环外事后监督）、六大难题 | 20 分钟 | Agentic 课 Ch.1 |
| 06 | [两个完整案例](06-case-studies.md) | 常驻个人助理（OpenClaw）、网页 agent（WebVoyager） | 30 分钟 | Agentic 课 Ch.7、11 |
| 07 | [模型是怎么训练出来的](07-how-models-are-trained.md) | 训练循环（training loop）、训练 vs 推理（inference）、预训练（pre-training） → SFT（supervised fine-tuning，监督微调） → RLHF（reinforcement learning from human feedback，基于人类反馈的强化学习）/DPO（Direct Preference Optimization，直接偏好优化）、CPU/GPU/TPU（Tensor Processing Unit，**含对课程训练课的纠错**） | 25 分钟 | GenAI 课 Ch.5、13 + 补充 |
| 08 | [三道 agent 设计练习](08-design-exercises.md) | 智能停车、自我改进的网页 agent、AI 医院：课程答案 + Staff 级改法 | 45 分钟（自己先做） | Agentic 课思考题 |

每篇结尾都有**中英术语表**、**英文面试话术**和**自测题**。自测答不上来，就回到对应小节重看。

**中英双语约定**（面试用英语）：正文用中文讲清楚；关键名词和术语第一次出现时写成"中文（English）"；每篇的术语表在第三列给出面试里可以直接说的英文句子。图里的标签以中文为主，对应英文查术语表。

## 图索引

| 图 | 用在 |
|---|---|
| ![](images/01-neural-net.svg) | 01 §2 神经网络（neural network） |
| ![](images/01-token-embedding.svg) | 01 §3 token 与 embedding |
| ![](images/01-attention.svg) | 01 §4 attention |
| ![](images/01-autoregressive.svg) | 01 §5 逐字生成 |
| ![](images/02-prefill-decode.svg) | 02 §2 prefill / decode |
| ![](images/02-gpu-memory.svg) | 02 §3 显存（GPU memory）账本 |
| ![](images/02-batching.svg) | 02 §4.3 batching |
| ![](images/02-botec.svg) | 02 §5 估算 |
| ![](images/03-chat-system.svg) | 03 §2 对话系统 |
| ![](images/03-rag-system.svg) | 03 §3 RAG（retrieval-augmented generation，检索增强生成） |
| ![](images/04-agent-loop.svg) | 04 §2 agent 循环 |
| ![](images/04-memory-layers.svg) | 04 §3 三层记忆 |
| ![](images/04-orchestration.svg) | 04 §4 编排方式 |
| ![](images/05-guardrails.svg) | 05 §2 护栏与人工介入（human oversight） |
| ![](images/06-openclaw.svg) | 06 §A 个人助理 |
| ![](images/06-webvoyager.svg) | 06 §B 网页 agent |
| ![](images/03-chunking.svg) | 03 §3.3 切块方式 |
| ![](images/07-training-loop.svg) | 07 §2 训练循环（training loop） |
| ![](images/07-training-stages.svg) | 07 §4 三个训练阶段 |
| ![](images/07-hardware.svg) | 07 §6 CPU / GPU / TPU（Tensor Processing Unit，张量处理单元） |
| ![](images/08-parking-agents.svg) | 08 练习 1 |
| ![](images/08-skill-library.svg) | 08 练习 2 |
| ![](images/08-ai-hospital.svg) | 08 练习 3 |

06（面试版）用的 7 张图也放在这里，文件名以 `i06-` 开头：

| 图 | 用在 06 |
|---|---|
| ![](images/i06-tool-call-patterns.svg) | §2.3 工具调用（tool calling）形态与错误恢复 |
| ![](images/i06-agent-control-plane.svg) | §2.3 控制面（control plane） |
| ![](images/i06-generate-verify-loop.svg) | §2.3 生成 → 验证 → 反思（reflection） → 选择 |
| ![](images/i06-eval-metric-map.svg) | §2.6 指标速查 |
| ![](images/i06-llm-regression-gate.svg) | §2.6 回归门禁 |
| ![](images/i06-semantic-cache-layers.svg) | §2.8 语义缓存（semantic cache） |
| ![](images/i06-parallelism.svg) | §2.8 并行 |
| ![](images/i06-langgraph-triage.svg) | §2.12 用 LangGraph 实现工单分诊 |
| ![](images/q01-enterprise-rag.svg) | 06c Q1 架构图 |
| ![](images/q02-support-agent.svg) | 06c Q2 架构图 |
| ![](images/q03-coding-agent.svg) | 06c Q3 架构图 |
| ![](images/q04-llm-gateway.svg) | 06c Q4 架构图 |
| ![](images/q05-eval-platform.svg) | 06c Q5 架构图 |
| ![](images/q06-triage-agent.svg) | 06c Q6 架构图 |
| ![](images/q07-kyc-doc-pipeline.svg) | 06c Q7 架构图 |
| ![](images/q08-llm-serving.svg) | 06c Q8 架构图 |
| ![](images/q09-catalog-search.svg) | 06c Q9 架构图 |
| ![](images/q10-voice-assistant.svg) | 06c Q10 架构图 |
| ![](images/q11-moderation.svg) | 06c Q11 架构图 |
| ![](images/q12-summarization.svg) | 06c Q12 架构图 |
| ![](images/q13-text-to-sql.svg) | 06c Q13 架构图 |
| ![](images/q14-agent-safeguards.svg) | 06c Q14 架构图 |
| ![](images/q15-gpu-quota.svg) | 06c Q15 架构图 |
| ![](images/q16-personal-assistant.svg) | 06c Q16 架构图 |
| ![](images/q17-browser-agent.svg) | 06c Q17 架构图 |

## 跳过了什么，为什么

| 课程内容 | 处理 | 理由 |
|---|---|---|
| GenAI 课：文生图、TTS（text-to-speech，语音合成）、文生视频、ASR（automatic speech recognition，语音识别）、看图说话（Ch.6–10） | 跳过 | 偏 ML（machine learning，机器学习）工程师，Staff SWE 面试很少考 |
| GenAI 课：评估（evaluation）指标、并行（parallel，DP / PP / TP）、语义缓存（semantic cache）分层、工具调用（tool calling）形态、回归测试 | notes 不写，**06 已收录**面试级要点 | 见 [06 §2.3](../06-ai-system-design.md)、§2.6、§2.8 |
| GenAI 课：图像 / 语音 / 视频各章的"训练（training）基础设施" | 跳过 | 训练侧内容；文本模型的训练已在 07 |
| Agentic 课：MACRS、Eureka、MuLan 等案例 | notes 不写，**06 已收录**可迁移部分 | 共同骨架"生成 → 验证 → 反思（reflection） → 选择"见 [06 §2.3](../06-ai-system-design.md)（来自 *Agentic System Design Crash Course*） |
| Agentic 课：ChainBuddy、MuLan 实现等 | 跳过 | 论文复述；AI Hospital 已整理成 08 练习 3 |
| Agentic 课：Google ADK / AutoGen 动手实现、AutoGen 项目 | 跳过 | 框架（framework）实操；框架选型见 06 §2.12 |
| 两门课的 AI mock interview | 保留 | Phase 2 想练时再用 |

## 可信度说明

- 课程里的规模数字（1 亿 DAU（daily active users，日活跃用户数）、每次交互 2 KB 等）都是**课程的假设**，不是真实系统的数据。
- 我补充的内容（prefill/decode、连续 batching（continuous batching）、显存（GPU memory）估算、对 9.6 ms 公式的纠错）都附了来源：NVIDIA 规格页、vLLM / Orca / 投机解码（speculative decoding）论文。
- AutoGen 和 CrewAI 的现状已于 2026-10-26 查证（见 04 §4）。仍标【待核实】的只有 OpenClaw 的组件细节。
