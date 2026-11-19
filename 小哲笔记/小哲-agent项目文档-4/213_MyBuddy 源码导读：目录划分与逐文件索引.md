这份索引配合《课前-MyBuddy工程设计说明》使用。先理解运行关系，再沿一个请求读代码；遇到陌生文件，回到这里查它负责什么。

下面按当前 `src/mybuddy/` 目录列出每个源码文件。根目录、配置和案例单独说明。读的时候先选一条阅读路线，再进逐文件表。

## 先分清三个位置

**源码、业务项目和会话记录放在三个不同的地方，别混在一起看。**

| 位置 | 保存什么 | 阅读时怎样区分 |
| --- | --- | --- |
| MyBuddy 项目目录 | Harness 源码、依赖声明、配置和案例 | 源码在 `src/mybuddy/`；源码运行时默认读本项目的 `config/config.toml` |
| 业务工作区 | 运费程序、收银台或你要修改的项目 | 由 `--workspace` 指定；换工作区不会改变配置文件的位置 |
| 会话状态目录 | 会话数据库、执行历史和长结果文件 | 用于继续、追溯和恢复；源码运行默认在 `output/mvp/`，可以在配置里改 |

一次普通请求这样走：`session_startup.py` 的 `create_configured_session` 按启动配置创建 `MyBuddySession`；用户输入从 `ask` 进入 `goal.py` 的 `run_goal_turns`，再经 `_ask_turn` 和 `turn.py` 的 `TurnCoordinator.run`，最后运行 `AgentLoop.run_turn`。一个用户请求轮次（Turn）可以包含多个模型决策周期（Step）。

会话事件由 `SessionJournal` 检查后交给 Store 写入数据库。子任务由父会话通过 `session_delegation.py` 和 `continuation.py` 创建受限子会话。

## 目录地图

`core/` **放循环和协议，**`platform/` **放真正接触模型、文件、终端的实现。**

```latex
项目根目录/
├── pyproject.toml          # 依赖、命令入口与构建配置
├── uv.lock                 # 锁定依赖版本
├── config/                 # MyBuddy 启动配置及示例
├── src/
│   └── mybuddy/
│       ├── __main__.py      # python -m 入口
│       ├── mybuddy.py       # 终端启动函数
│       ├── cli.py           # 终端输入与命令分发
│       ├── builtin_skills/ # 随程序发布的审查、提交说明和测试方法
│       ├── frontmatter.py   # Buddy 与 Skill 共用的 YAML 字段解析
│       ├── resources.py     # 协议文件与默认状态目录定位
│       ├── api/             # 给其他 Python 程序用的会话入口
│       ├── spi/             # 模型适配器扩展接口
│       ├── features/        # Buddy 预设读取
│       ├── core/
│       │   ├── ports/      # 写入会话事件的接口
│       │   ├── protocol/   # 协议数据和 Schema 校验
│       │   └── runtime/    # AgentLoop 与它需要的接口
│       ├── web/            # 本地 Web 界面
│       └── platform/
│           ├── application/ # 会话装配、命令与请求处理
│           ├── cli/         # 终端解析与显示
│           ├── models/      # 模型目录、请求格式与调用
│           ├── memory/      # 共享 Memory 与文件存储
│           ├── hooks/       # 会话、轮次、工具与压缩事件的 Hook 命令
│           ├── buddy/       # Buddy 预设的选择与检查
│           ├── instructions/ # 根指令与给模型的提示
│           ├── artifacts/   # 长结果的保存与读取
│           ├── context/    # 请求组装、预算，compaction/ 负责压缩
│           ├── sessions/   # 会话运行、历史保存与恢复，state/ 从历史算状态
│           ├── sandbox/    # Bash 的可选系统沙箱（macOS / Linux）
│           ├── tools/      # 工具检查、审批与执行
│           ├── subagents/   # 委派、后台任务与 Team
│           ├── worktrees/   # Git 工作副本隔离与差异检查
│           ├── skills/     # 本地 Skill 的发现与加载
│           └── mcp_stdio/  # MCP 服务接入（stdio 和 HTTP）
├── demo-project/           # 运费与麦当当等业务样例
└── examples/               # Buddy、Skill、MCP、Hook、研究任务、嵌入调用样例
```

| 源码目录 | 为什么放在一起 | 看代码时关注什么 |
| --- | --- | --- |
| `src/mybuddy/` | 放程序入口，再分出 api、core 和 platform | 从哪个命令进入，谁创建组件 |
| `api/`、`spi/` | `api/` 给其他程序调用会话，`spi/` 让模型适配器接进来 | 两者都拿不到会话数据库 |
| `web/` | 把浏览器操作接到同一套会话，静态文件在 `web/static/` | 审批、请求展示怎样复用后端 |
| `features/` | 读取 Markdown 里的 Buddy 预设 | 只检查格式，不执行内容 |
| `core/runtime/` | 模型与工具交替推进的循环和它的接口 | 每个 Step 怎样开始、继续、取消、结束 |
| `core/ports/`、`core/protocol/` | 写事件的接口，以及跨模块传递的数据和校验 | 谁能写哪类事件，数据长什么样 |
| `platform/context/` | 组装模型请求、估算用量；压缩在 `compaction/` | 历史怎样变成模型输入 |
| `platform/sessions/` | 会话历史的保存、读取和恢复；`state/` 从历史算出状态 | Journal 和 Store 各管什么 |
| `platform/tools/` | 工具的检查、审批、执行和结果放在一个入口 | 调用建议何时变成真实操作 |
| `platform/sandbox/` | 生成可选的系统沙箱启动计划（macOS Seatbelt / Linux bubblewrap）；进程管理在 `tools/coding_bash.py` | 沙箱配置和命令执行分开 |
| `platform/skills/` | Skill 的发现、加载和资源读取 | 内容怎样进请求，为什么它不授予权限 |
| `platform/mcp_stdio/` | MCP 服务的连接、工具目录和调用 | 连接、子进程和调用的生命周期 |
| `platform/subagents/` | 委派计划、子会话和结果回传 | 子任务权限和结束状态怎样核对 |
| `platform/worktrees/` | Git 工作副本的创建、差异检查和清理 | 副本不等于沙箱，看差异不会自动合并 |

## 这种划分遵循什么逻辑

**按"要观察什么变化"找入口：循环找** `core/runtime/`**，真实模型和工具找** `platform/`**，输入与装配找** `cli.py` **和** `platform/application/`**。**

划分的原因见《课前-MyBuddy工程设计说明》“按什么逻辑划分”。同一项功能可能横跨多个目录。先沿下面的接口路线找到动作由谁接住，再用逐文件表查职责：

```latex
cli.py → application_session.py：接受请求、装配组件
AgentLoop → 模型接口 / 工具运行接口 / 事件提交接口
ToolRuntime → 策略 / 用户交互 / Provider / 事件提交接口
各提交接口 → SessionJournal → Store 接口 → SQLite 实现
```

箭头表示调用与接口实现关系。

几个容易误会的地方：

- 恢复会话时，程序会检查事件格式、顺序和会话状态；结果未知的工具执行不会自动重跑。
- `/diff` 用临时 Git 目录比较修改；仓库配置了 filter 等转换时直接拒绝，不运行仓库里的辅助程序。
- 工作副本只是独立目录，不是沙箱。子任务在工作副本里运行时，沙箱会禁止它写父工作区和 Git 目录。

## 根目录、配置和案例怎样配合

**找命令入口看** `pyproject.toml`**，找配置看** `config/`**，找练习材料看** `demo-project/` **和** `examples/`**。**

| 文件或目录 | 用途与阅读提示 |
| --- | --- |
| `README.md` | 项目启动和功能入口概览；课程的学习顺序以本目录为准 |
| `AGENTS.md` | 给在本仓库工作的编码 Agent 的约定；和业务项目自己的根指令分开 |
| `pyproject.toml` | Python 版本、依赖、终端命令入口和打包资源 |
| `uv.lock` | 锁定依赖版本，让不同机器装到同一组依赖 |
| `.python-version` | 本地 Python 版本提示；允许范围见 `pyproject.toml` |
| `.gitignore` | 哪些生成物和本地文件不纳入版本控制 |
| `config/README.md` | 启动配置的维护说明；课程里的用法见《课前-MyBuddy使用导读》 |
| `config/config.example.toml` | 可对照填写的配置模板；它不会被自动加载 |
| `config/config.toml` | 本机实际配置；源码运行默认读它。密钥通过配置指定的环境变量提供 |
| `demo-project/` | 业务样例与准备脚本；收银台见《课前-麦当当收银台介绍》，练习副本按《实践准备》建立 |
| `examples/buddies/README.md` | Buddy 预设样例，预设正文在 `buddies.md` |
| `examples/skills/README.md` | 把项目 Skill 复制到练习工作区的使用说明 |
| `src/mybuddy/builtin_skills/` | 随程序发布的 code-review、commit-message、test-writing |
| `examples/skills/shipping-review/SKILL.md` | 运费检查 Skill 的入口说明与方法 |
| `examples/skills/shipping-review/references/checklist.md` | Skill 按需读取的补充检查清单 |
| `examples/mcp/README.md` | 配送与研究 MCP 样例的配置和体验说明；配置由 `mcp_example_configuration.py` 生成，两个示例服务在 `servers/` |
| `examples/hooks/README.md` | 工具前检查、工具后反馈、启动状态与轮末日志样例 |
| `examples/research-task/README.md` | 研究任务用的两份示例资料 |
| `examples/embedding/README.md` | 在其他 Python 程序里调用会话的样例 |
| `demo-project/exercises/` | 作业准备脚本和业务 case |
| `demo-project/practice/` | 准备脚本生成的练习副本，不进版本库 |
| `output/` | 源码运行的默认会话数据在这里（`output/mvp/`），不进版本库，不要整体删掉 |
| `.venv/`、`__pycache__/` | 本地环境和 Python 缓存，不是源码 |

`src/mybuddy/_contracts/` 目录里是机器校验用的 Schema，由 `resources.py` 定位。它就在包目录里，打包时会自动带上，源码运行和安装后运行读的是同一份。它不是业务代码。

## 按问题选择阅读路线

**每条路线回答一个问题；路线只表示查阅顺序，文件之间不一定直接调用。**

| 问题 | 建议路线 | 本次要找到的边界 |
| --- | --- | --- |
| 输入一句话后发生什么？ | `__main__.py` → `mybuddy.py` 的 `main` → `cli.py` 的 `run_cli` → `platform/application/application_session.py` 的 `MyBuddySession.ask` → `platform/application/goal.py` → `platform/application/turn.py` → `core/runtime/agent_loop.py` → `platform/context/request.py` → `platform/models/model_gateway.py` → `platform/models/openai_model.py` | 输入解析、会话管理、循环、请求组装和网络发送分别在哪里 |
| 模型怎么修改本地文件？ | `platform/application/tool_composition.py` → `platform/tools/tool_registry.py` → `coding_tools.py` → `coding_mutations.py`；检查顺序看 `platform/tools/tool_runtime.py`，执行 Shell 再看 `coding_bash.py` | 工具建议怎样经过检查和审批变成实际执行 |
| 为什么退出还能继续？ | `platform/sessions/agent_session.py` → `session_journal.py` → `sqlite_session_store.py` → `continuation_checks.py` | 内存里的运行对象和磁盘上的历史有什么区别 |
| 怎么把编码分给子任务？ | `platform/subagents/tool.py` → `session_delegation.py` → `service.py`、`continuation.py` → `platform/worktrees/session_worktrees.py`、`tool.py` | 任务计划、子任务权限、结束状态和副本差异；子任务的修改不会自动合并 |
| 压缩到底改了什么？ | `platform/context/compaction/session.py`、`auto.py`、`service.py` → `projection.py` → `recovery_files.py` → `request.py`、`summary.py` → `platform/sessions/compaction_events.py` → `platform/context/compaction/render.py` | 用一次不带工具的调用生成概要；小档保留最后两组消息，大档保留近期窗口并补读文件；结果存成一条事件 |
| Goal 怎样跨轮继续？ | `platform/application/goal_commands.py` → `application_session.py` → `goal.py` → `platform/sessions/state/goal.py` | 设置后立即开始；符合条件的正常轮末才用 low 档模型评估，未达成且没有停止条件时自动继续；提问后等待回答 |

第二条路线中省略目录的文件在 `platform/tools/`，第三条在 `platform/sessions/`，压缩路线在 `platform/context/compaction/`，委派路线在 `platform/subagents/`。压缩各阶段的数据变化见 Context 阅读入口 `src/mybuddy/platform/context/README.md`。

可选能力的阅读入口：WebSearch 从 `tools/web_search_policy.py` 到 `tools/web_search.py`；Bash 沙箱从 `tools/coding_bash.py` 到 `sandbox/`；Hook 从工具、会话和压缩主流程进入 `hooks/` 的事件入口。Hook 命令由可信配置授权，不逐次审批，复用 Bash 的沙箱和进程管理。

## 逐文件索引

**以下路径相对** `src/mybuddy/`**，每行一句话说清文件负责什么。**

先按目录找功能，再挑要读的文件。

### .

| 文件 | 负责什么 |
| --- | --- |
| `GLOSSARY.md` | 集中解释源码中的中英文名称，供沿运行流程读代码时回查。 |
| `README.md` | 说明 Python 源码的阅读入口，以及应用、Core 和平台模块之间的分工。 |
| `__init__.py` | 包标记；给其他 Python 程序用的入口在 api/。 |
| `__main__.py` | 让 `python -m mybuddy` 能启动终端程序。 |
| `cli.py` | 接收终端输入，把请求交给会话，并显示运行过程和结果。 |
| `frontmatter.py` | 读取 Markdown 开头的 YAML 字段，并保留后面的正文。 |
| `mybuddy.py` | 根据启动参数选择终端会话或历史查询。 |
| `py.typed` | 声明这个包带类型信息，供类型检查工具使用。 |
| `resources.py` | 查找程序需要的协议文件和默认状态目录。 |

### api

| 文件 | 负责什么 |
| --- | --- |
| `api/__init__.py` | 提供其他 Python 应用可以使用的会话入口。 |
| `api/session.py` | 为其他 Python 应用提供创建会话、提问和退出的入口。 |

### core

| 文件 | 负责什么 |
| --- | --- |
| `core/README.md` | 说明 Core 的协议、循环与提交接口，沿一次 Turn 找到模型和工具的交接。 |
| `core/__init__.py` | 集中导出会话运行循环需要的类型和接口。 |

### core/ports

| 文件 | 负责什么 |
| --- | --- |
| `core/ports/__init__.py` | 提供向会话历史提交事件的接口。 |
| `core/ports/commit_ports.py` | 定义会话运行过程中写入事件的接口。 |

### core/protocol

| 文件 | 负责什么 |
| --- | --- |
| `core/protocol/declarations.py` | 列出协议用到的 Schema 文件，以及各类事件用哪份 Schema 检查。 |
| `core/protocol/__init__.py` | 会话事件的格式检查错误和数据库写入确认信息。 |
| `core/protocol/schema.py` | 加载 JSON Schema，检查会话历史中的事件和准备提交的数据。 |
| `core/protocol/task_contract.py` | 用任务的 Schema 检查数据，也能为数据计算哈希值。 |
| `core/protocol/value.py` | 在普通 JSON 数据和只读容器之间转换。 |

### core/runtime

| 文件 | 负责什么 |
| --- | --- |
| `core/runtime/__init__.py` | 集中导出运行循环及它需要的接口和数据类型。 |
| `core/runtime/agent_loop.py` | 按顺序调用模型、处理工具结果并记录一次用户请求的处理过程。 |
| `core/runtime/cancellation.py` | 帮助调用方等待异步任务完成，即使等待期间又收到取消请求。 |
| `core/runtime/model_output_admission.py` | 保存模型回复前，检查其中是否出现凭证或疑似凭证。 |
| `core/runtime/ports.py` | 列出运行循环需要的模型、工具、用户交互、时间和 ID 接口。 |

### features

| 文件 | 负责什么 |
| --- | --- |
| `features/__init__.py` | 包标记；Buddy 预设读取在 buddy_catalog.py。 |
| `features/buddy_catalog.py` | 从一份 Markdown 文件读取全部 Buddy 预设，不执行文件内容。 |

### platform

| 文件 | 负责什么 |
| --- | --- |
| `platform/README.md` | platform 的阅读入口：各主题目录和普通请求的调用链。 |
| `platform/__init__.py` | 导出常用的会话与工具类型。 |
| `platform/activity.py` | 把传入的事件整理成界面上的活动进度。 |
| `platform/archive_cursor.py` | 把会话列表或历史记录的分页位置编码成游标，也负责解析游标。 |
| `platform/runtime_values.py` | 提供 CLI 运行时使用的时钟、随机编号和 JSON 编码方法。 |
| `platform/terminal_text.py` | 提供终端显示时使用的文本过滤函数。 |

### platform/application

| 文件 | 负责什么 |
| --- | --- |
| `platform/application/turn.py` | 把一次用户请求从保存输入、运行模型到整理结果串起来。 |
| `platform/application/session_tools.py` | 根据会话配置整理模型能看到的工具，并检查 MCP 工具由哪个服务提供。 |
| `platform/application/session_settings.py` | 整理会话的启动设置：功能开关和 Buddy 预设取当前配置；重新打开的会话，权限模式、模型和项目说明从历史读回来。也准备 Memory 路径、扩展和配置记录。 |
| `platform/application/session_initialization.py` | 初始化会话的根指令、模型选择、权限模式和共享 Memory。 |
| `platform/application/session_runtime.py` | 在会话取得运行权、写完初始事件之后，接好模型和 MCP，组装工具并创建 AgentLoop。 |
| `platform/application/resume_checks.py` | 检查已有会话能否继续运行：工作区和 Buddy 要相同，必需记录要完整，不能有没做完的工作；配置或工具说明变了可以继续，并列出变化项用于提示。 |
| `platform/application/goal.py` | 负责设置、查看和清除目标，也负责在一轮结束后判断是否继续。 |
| `platform/application/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/application/TURN_FLOW.md` | 按接收输入、准备、运行、接受结果讲一次普通请求，并标出取消分支。 |
| `platform/application/__init__.py` | 包标记；会话装配与请求处理在本目录各文件。 |
| `platform/application/application_session.py` | 负责创建、启动和关闭应用会话，并协调用户请求和会话控制操作。 |
| `platform/application/application_state.py` | 定义 CLI 和交互界面读取的会话状态、切换选项和请求结果。 |
| `platform/application/memory_extraction.py` | 在一轮用户请求结束后，尝试从对话中提取值得记住的内容。 |
| `platform/application/session_commands.py` | 处理 CLI 和 Web 共用的会话命令。 |
| `platform/application/diagnostics.py` | 列出 CLI 和 Web 共用的固定错误说明，按错误码查找对应文字。 |
| `platform/application/command_registry.py` | 列出应用支持的命令，并用同一份列表处理解析、帮助和补全。 |
| `platform/application/control_input.py` | 定义用户取消界面输入时使用的异常。 |
| `platform/application/embedding_session.py` | 让其他 Python 程序通过客户端使用 MyBuddy 会话。 |
| `platform/application/file_edit_restore.py` | 处理把单个文件恢复到某次编辑之前的请求。 |
| `platform/application/goal_commands.py` | 处理 /goal 的查看、设置和清除命令，并生成界面提示。 |
| `platform/application/mybuddy_composition.py` | 整理创建会话时的模型、工具和功能配置，并检查恢复所需的历史。 |
| `platform/application/pending_continuation.py` | 协调等待发送的输入，让同一会话一次处理一条。 |
| `platform/application/pending_input.py` | 在内存中管理等待处理的补充输入和插队输入。 |
| `platform/application/permission_mode_use_case.py` | 解析用户输入的权限模式，并交给会话处理切换。 |
| `platform/application/planning_candidate.py` | 保存规划模式的提示词。 |
| `platform/application/planning_policy.py` | 在运行工具前检查规划模式下的限制。 |
| `platform/application/questions.py` | 把用户对 AskUserQuestion 问题的回答整理成普通用户消息，并检查问题编号和回答大小。 |
| `platform/application/session_branching.py` | 准备从已有对话创建分支，并检查新会话要继承的对话和配置。 |
| `platform/application/session_lifecycle.py` | 帮助界面判断当前会话是否可以安全切换。 |
| `platform/application/session_permission_modes.py` | 确定新会话的初始权限模式，或从历史中找回已有会话的权限模式。 |
| `platform/application/session_selection.py` | 读取已有会话，供用户用 /resume 选择要继续的会话。 |
| `platform/application/session_construction.py` | 说明创建会话需要哪些输入（外部依赖、装配值、配置记录），并检查这些输入能否一起使用。 |
| `platform/application/session_startup.py` | 根据启动配置准备工作目录、模型和其他资源，再创建会话对象。 |
| `platform/application/startup_config.py` | 读取并检查 MyBuddy 的启动 TOML，整理出程序需要的配置。 |
| `platform/application/tool_composition.py` | 为当前会话登记可用工具，并把权限检查和真正运行工具的代码接起来。 |
| `platform/application/workspace_diff.py` | 用临时 Git 目录读取工作区未提交的修改，供 `/diff` 显示。 |

### platform/artifacts

| 文件 | 负责什么 |
| --- | --- |
| `platform/artifacts/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/artifacts/__init__.py` | 包标记；长结果存储在 artifact_store.py。 |
| `platform/artifacts/artifact_store.py` | 在本地保存和读取 Artifact，也就是较长工具结果的内容文件。 |

### platform/buddy

| 文件 | 负责什么 |
| --- | --- |
| `platform/buddy/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/buddy/__init__.py` | 包标记；Buddy 预设的选择与检查在本目录各文件。 |
| `platform/buddy/buddy_capabilities.py` | 筛选 Buddy 可选的工具和模型，并核对 MCP 工具由哪个服务提供。 |
| `platform/buddy/buddy_configuration.py` | 解析启动配置中选择的 Buddy 预设文件和默认 ID。 |
| `platform/buddy/startup.py` | 读取 Buddy 预设，并检查预设要求的工具是否在允许选择的列表里。 |

### platform/cli

| 文件 | 负责什么 |
| --- | --- |
| `platform/cli/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/cli/__init__.py` | 包标记；终端解析与显示在本目录各文件。 |
| `platform/cli/archive_views.py` | 把会话列表和历史分页整理成终端文字，不启动会话。 |
| `platform/cli/cli_activity.py` | 把模型和工具的活动追加显示在终端，不移动光标。 |
| `platform/cli/cli_approval.py` | 在终端展示需要用户批准的一次操作，并等待用户选择。 |
| `platform/cli/cli_compaction.py` | 把上下文整理结果转换成终端提示。 |
| `platform/cli/cli_control.py` | 处理终端里的会话选择、方案确认和停止请求。 |
| `platform/cli/cli_diagnostics.py` | 把运行错误转换成终端显示的固定提示。 |
| `platform/cli/cli_input.py` | 负责终端里的草稿、按键和审批输入。 |
| `platform/cli/cli_mcp.py` | 把 MCP 连接状态整理成终端文字。 |
| `platform/cli/cli_memory.py` | 在终端显示共享记忆的入口位置和命令错误。 |
| `platform/cli/cli_models.py` | 把本地模型目录、当前选择和切换错误整理成终端文字。 |
| `platform/cli/cli_permissions.py` | 读取会话的权限模式，并生成终端里看到的说明。 |
| `platform/cli/cli_planning.py` | 处理终端里的规划模式和用户对方案的选择。 |
| `platform/cli/cli_progress.py` | 在任务运行时定时读取会话历史，把新活动交给终端显示。 |
| `platform/cli/cli_sessions.py` | 协调终端在不同会话间切换：先等旧会话释放，再启动新会话。 |
| `platform/cli/cli_status.py` | 把会话事件和状态整理成 `/status` 显示的文字。 |
| `platform/cli/cli_stream.py` | 在终端显示模型逐段返回的文字，并与后来保存的完整消息比较。 |
| `platform/cli/cli_trace.py` | 从会话历史整理 `/trace` 显示的步骤、工具和 Goal 评估。 |
| `platform/cli/cli_views.py` | 读取已打开的会话状态，并整理成终端上的状态和诊断文字。 |
| `platform/cli/startup_arguments.py` | 在启动会话或查询历史前解析命令行参数，并读取启动配置。 |

### platform/context

| 文件 | 负责什么 |
| --- | --- |
| `platform/context/README.md` | context 的阅读入口：请求组装、预算和压缩。 |
| `platform/context/__init__.py` | 包标记；阅读入口见本目录 README.md。 |
| `platform/context/branch_context.py` | 从会话历史中整理对话分支要继承的消息。 |
| `platform/context/business_model_input.py` | 检查保存的模型请求，并整理成供应商适配器共用的输入。 |
| `platform/context/file_change_notice.py` | 读过的文件后来被改动时，生成下一次模型请求前加入历史的系统提醒。 |
| `platform/context/governance.py` | 核对模型选择，并将请求估算与会话选定的本地预算比较。 |
| `platform/context/local_context_policy.py` | 把一次模型请求的估算输入与本地预算进行比较。 |
| `platform/context/profile.py` | 保存一套本地请求预算，并估算发给模型的输入有多大。 |
| `platform/context/progress_guard.py` | 检查模型是否反复执行相同的工具操作，主会话和子任务共用。 |
| `platform/context/report.py` | 估算下一次模型请求的上下文用量，并生成终端报告。 |
| `platform/context/request.py` | 把历史消息、系统指令和工具定义组合成模型请求。 |
| `platform/context/request_answer_guidance.py` | 根据会话历史生成给模型的回答提醒，比如上一轮被取消。 |
| `platform/context/request_blocks.py` | 为模型请求中的内容建立索引，方便查看每一部分在哪里。 |
| `platform/context/request_history.py` | 从最近一条能力记录读取当时是否处于规划模式，不用当前工具定义推测历史模式。 |
| `platform/context/request_history_view.py` | 定义组装模型请求时需要读取的历史数据。 |
| `platform/context/request_meter.py` | 为状态页面整理最近一次模型请求的大小和用量。 |
| `platform/context/retained_context.py` | 检查并读取子任务或对话分支继承来的消息。 |
| `platform/context/selected_model_profile.py` | 保存选定模型的文档容量和程序设置的请求预算。 |
| `platform/context/system_collection_projection.py` | 把用户要求恢复文件的结果整理成历史消息。 |
| `platform/context/turn_step_policy.py` | 定义一轮请求如何继续运行，并生成用于识别这份规则的记录。 |
| `platform/context/usage_anchor.py` | 用上次模型返回的输入用量和请求变化量，估算当前输入大小。 |

### platform/context/compaction

| 文件 | 负责什么 |
| --- | --- |
| `platform/context/compaction/session.py` | 串起会话的手动和自动压缩，保存当前进程中的失败次数和调用次数。 |
| `platform/context/compaction/README.md` | 压缩流程的阅读入口：各阶段做什么，为什么不删原始历史。 |
| `platform/context/compaction/__init__.py` | 包标记；压缩流程从 session.py 开始读。 |
| `platform/context/compaction/auto.py` | 在模型下一次决策前检查上下文大小，必要时尝试压缩。 |
| `platform/context/compaction/calls.py` | 从会话历史中的事件统计一次用户请求的模型调用次数。 |
| `platform/context/compaction/gateway.py` | 定义生成历史概要的模型请求、响应和调用接口。 |
| `platform/context/compaction/policy.py` | 用本地估算的 token 数和字节数比较压缩前后的请求。 |
| `platform/context/compaction/projection.py` | 把历史消息分组，并选出哪些较早的消息可以整理成概要。 |
| `platform/context/compaction/prompt_registry.py` | 保存手动和自动压缩共用的概要提示词及版本号。 |
| `platform/context/compaction/prompt_source.py` | 为上下文压缩规则生成一份会话配置记录。 |
| `platform/context/compaction/render.py` | 把已保存的历史概要和之后的原始消息组合起来，交给模型。 |
| `platform/context/compaction/report.py` | 从会话历史中的压缩事件统计成功次数和最近一次的 token 变化。 |
| `platform/context/compaction/request.py` | 组装让模型生成历史概要的请求。 |
| `platform/context/compaction/retention_focus.py` | 检查用户希望本次压缩重点保留的内容。 |
| `platform/context/compaction/service.py` | 把较早的消息交给模型生成概要，检查压缩后是否值得保存。 |
| `platform/context/compaction/summary.py` | 检查模型返回的工作概要是否可以作为文本使用。 |
| `platform/context/compaction/recovery_files.py` | 大档压缩时，选择并补读最近用过的工作区文件，限制内容大小，再把快照随概要保存。 |

### platform/hooks

| 文件 | 负责什么 |
| --- | --- |
| `platform/hooks/events.py` | 七种事件的短入口，工具前检查与工具后反馈在这里区分。 |
| `platform/hooks/commands.py` | 七种事件共用的命令启动、限时等待、输出读取和进程停止。 |
| `platform/hooks/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/hooks/__init__.py` | 检查七种 Hook 事件的配置，也为会话配置生成识别用的哈希值。 |

### platform/instructions

| 文件 | 负责什么 |
| --- | --- |
| `platform/instructions/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/instructions/__init__.py` | 包标记；各类指令在本目录各文件。 |
| `platform/instructions/coding_check_guidance.py` | 提供给模型的项目检查提示。 |
| `platform/instructions/evidence_use_guidance.py` | 提供给模型的证据使用提示。 |
| `platform/instructions/init_request.py` | 保存 /init 使用的项目导航请求文字。 |
| `platform/instructions/loader.py` | 按用户、项目逐级、本地顺序读取说明，展开 @ 引用并限制合计大小。 |
| `platform/instructions/root_instructions.py` | 保存会话冻结的说明、来源哈希与诊断，生成模型提示和状态明细。 |
| `platform/instructions/turn_cancellation_guidance.py` | 根据历史中的取消记录和当前输入，生成给模型的提醒。 |

### platform/mcp_stdio

| 文件 | 负责什么 |
| --- | --- |
| `platform/mcp_stdio/session.py` | 管理会话中的 MCP 工具目录和服务连接。 |
| `platform/mcp_stdio/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/mcp_stdio/__init__.py` | 包标记；MCP 连接从 session.py 开始读。 |
| `platform/mcp_stdio/configuration.py` | 解析 MCP 服务配置；解析本身不批准连接。 |
| `platform/mcp_stdio/connection_plan.py` | 把 MCP 连接计划整理成供人查看的文字。 |
| `platform/mcp_stdio/host.py` | 连接 MCP 服务，读取工具目录，并把工具调用交给服务执行。 |
| `platform/mcp_stdio/host_group.py` | 一起管理最多八个 MCP 服务连接。 |
| `platform/mcp_stdio/http_profile.py` | 检查 HTTP 服务配置，并整理连接计划。 |
| `platform/mcp_stdio/http_transport.py` | 通过 MCP SDK 打开和关闭 Streamable HTTP 连接。 |
| `platform/mcp_stdio/profile.py` | 准备 stdio 方式连接 MCP 服务所需的配置，并核对连接计划。 |
| `platform/mcp_stdio/projection.py` | 把 MCP 服务和工具目录整理成模型请求需要的数据。 |
| `platform/mcp_stdio/schema_validation.py` | 检查 MCP 工具使用的 JSON Schema 和数据是否符合 Schema。 |
| `platform/mcp_stdio/server_configuration.py` | 读取并检查用户填写的 MCP 服务配置。 |
| `platform/mcp_stdio/session_initialization.py` | 在会话启动时请求用户批准连接 MCP 服务，并取得工具列表。 |
| `platform/mcp_stdio/tool_search.py` | 提供 `search_tools`，并从历史里的搜索结果判断哪些 MCP 工具已被找到。 |
| `platform/mcp_stdio/tools.py` | 检查 MCP 工具调用的参数和权限，再交给对应服务执行。 |
| `platform/mcp_stdio/transport.py` | 启动本地 MCP 服务进程，用标准输入输出传消息，并负责关闭进程。 |

### platform/memory

| 文件 | 负责什么 |
| --- | --- |
| `platform/memory/session_memory.py` | 保存用户输入前读取共享记忆，保存后确认本轮使用的内容。 |
| `platform/memory/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/memory/__init__.py` | 包标记；共享 Memory 的代码在本目录各文件。 |
| `platform/memory/extraction_notice.py` | 根据会话历史生成自动记忆提示，供 CLI 和 Web 共用。 |
| `platform/memory/extraction_request.py` | 为自动提取记忆构造模型请求，并检查模型返回的内容。 |
| `platform/memory/shared_memory_catalog.py` | 定义共享记忆给模型的说明和可用工具。 |
| `platform/memory/shared_memory_entry.py` | 检查记忆写入请求，并根据当前记忆内容准备写入计划。 |
| `platform/memory/shared_memory_projection.py` | 从会话历史中取出已确认使用的记忆索引，整理成模型请求中的文本。 |
| `platform/memory/shared_memory_request_history.py` | 保存当前请求使用的历史，并从事件中算出共享记忆状态。 |
| `platform/memory/shared_memory_session.py` | 管理当前会话使用的共享记忆内容。 |
| `platform/memory/shared_memory_write_session.py` | 把记忆写入交给工具运行，整批结束后更新会话使用的记忆。 |
| `platform/memory/shared_memory_write_tools.py` | 为记忆写入做权限判断，并把实际执行交给 SharedMemoryWriteSession。 |

### platform/memory/files

| 文件 | 负责什么 |
| --- | --- |
| `platform/memory/files/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/memory/files/__init__.py` | 包标记；Memory 文件存储在本目录各文件。 |
| `platform/memory/files/filesystem.py` | 负责打开、读取和修改保存在本机的 Memory 文件。 |
| `platform/memory/files/format.py` | 检查、读取和生成保存 Memory 条目的 Markdown 文本。 |
| `platform/memory/files/identity.py` | 确定 MyBuddy 源码目录，以及全局和项目 Memory 应存放的位置。 |
| `platform/memory/files/mutations.py` | 根据工具参数生成修改后的 Memory 内容，但不负责保存文件。 |
| `platform/memory/files/plans.py` | 保存一次 Memory 修改准备写入的内容、原请求和检查信息。 |
| `platform/memory/files/query.py` | 在已读入的 Memory 内容里分页读取或搜索条目。 |
| `platform/memory/files/read_tool.py` | 定义 read_memory_file 工具的名称、版本和参数。 |
| `platform/memory/files/store.py` | 读写按主题组织的 Memory 文件，并保存每次文件修改的结果。 |
| `platform/memory/files/tools.py` | 提供会话中 Memory 的读取、查找和搜索工具。 |
| `platform/memory/files/write_tools_contract.py` | 定义模型可以使用的 Memory 写入工具及其参数。 |

### platform/models

| 文件 | 负责什么 |
| --- | --- |
| `platform/models/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/models/__init__.py` | 包标记；模型配置与调用在本目录各文件。 |
| `platform/models/anthropic_model.py` | 按配置地址通过 Anthropic Messages 协议发送请求并读取回复。 |
| `platform/models/anthropic_wire_codec.py` | 在程序内部格式和 Anthropic Messages 请求、回复之间转换。 |
| `platform/models/openai_model.py` | 按 OpenAI Chat Completions 协议发送请求并读取回复。 |
| `platform/models/openai_stream.py` | 检查流式回复片段。 |
| `platform/models/openai_wire_codec.py` | 在程序内部格式和 OpenAI 请求、回复之间转换。 |
| `platform/models/model_adapters.py` | 根据配置中的协议装配请求编码和适配器。 |
| `platform/models/model_catalog.py` | 读取配置中的 Provider、模型、预算和预设。 |
| `platform/models/model_credentials.py` | 在实际调用时读取模型凭据。 |
| `platform/models/model_codec.py` | 列出模型请求的编码、回复的解码和请求大小估算需要提供的方法。 |
| `platform/models/model_factory.py` | 定义会话需要的模型接口，并为模型配上供应商和预算。 |
| `platform/models/model_failure_boundary.py` | 检查模型调用失败后的事件是否描述了同一次失败。 |
| `platform/models/model_gateway.py` | 调用模型前检查请求，收到后检查完整回复。 |
| `platform/models/text_model.py` | 发送不使用工具的文本请求，并检查请求和回复。 |
| `platform/models/model_runtime.py` | 为会话创建调用模型的接口，分别用于普通回复、概要、记忆提取和目标评估。 |
| `platform/models/model_selection_state.py` | 整理会话选过的模型配置，并为新选择生成待保存的数据。 |
| `platform/models/model_selection_use_case.py` | 把用户输入的预设名或模型键交给会话，供 CLI 等入口共用。 |
| `platform/models/model_stream.py` | 把流式回复拼成完整回复，并提供临时文字预览。 |
| `platform/models/model_wire.py` | 保存模型请求的正文和规范 JSON 字节。 |
| `platform/models/provider_json.py` | 解析模型供应商返回的 JSON，也负责转换工具结果的文本形式。 |
| `platform/models/session_model_selection.py` | 根据模型目录确定会话使用哪个模型及其预算。 |

### platform/sandbox

| 文件 | 负责什么 |
| --- | --- |
| `platform/sandbox/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/sandbox/__init__.py` | 为命令和 stdio MCP 服务准备系统沙箱启动计划（macOS Seatbelt / Linux bubblewrap）。 |
| `platform/sandbox/bubblewrap.py` | 为 Linux 生成 bubblewrap 沙箱的启动参数，限制和 macOS Seatbelt 规则相同。 |

### platform/sessions

| 文件 | 负责什么 |
| --- | --- |
| `platform/sessions/input_validation.py` | 检查准备放进等待队列的文本。 |
| `platform/sessions/continuation_checks.py` | 检查已读取的会话历史能否继续处理新输入。 |
| `platform/sessions/session_trash.py` | 把顶层会话及其子会话的文件移入状态目录下的回收站。 |
| `platform/sessions/session_state.py` | 转发导入入口；会话状态的实现在 state/。 |
| `platform/sessions/event_checks.py` | 检查单个事件的字段和格式；事件顺序由调用方检查。 |
| `platform/sessions/session_events.py` | 组装会话历史中的事件，供不同的会话操作共同使用。 |
| `platform/sessions/turn_events.py` | 组装步骤和轮次结束时要一起保存的事件。 |
| `platform/sessions/HISTORY_CHECKS.md` | 说明正常续接和异常恢复各要核对哪些历史记录。 |
| `platform/sessions/README.md` | sessions 的阅读入口：会话运行、历史保存与恢复。 |
| `platform/sessions/__init__.py` | 导出会话运行、历史保存和读取的常用类型。 |
| `platform/sessions/agent_session.py` | 安排本地会话的启动、运行和关闭。 |
| `platform/sessions/compaction_events.py` | 从会话事件中找出最近一次上下文压缩生成的概要，并统计压缩次数。 |
| `platform/sessions/errors.py` | 定义会话运行时使用的异常。 |
| `platform/sessions/execution_facts.py` | 按顺序检查会话历史，整理模型请求、工具调用和执行结果之间的关系。 |
| `platform/sessions/history_json.py` | 复制和比较会话历史里的 JSON 值，并保留整数与浮点数的区别。 |
| `platform/sessions/lossless_json.py` | 在事件进入会话时复制 JSON 值，避免调用方后来修改原来的容器。 |
| `platform/sessions/mcp_initialization.py` | 生成连接 MCP 服务时的审批提示。 |
| `platform/sessions/memory_extraction_events.py` | 检查一轮结束后的 Memory 提取事件是否与已有会话历史一致。 |
| `platform/sessions/message_closure.py` | 从模型消息中读出按顺序声明的工具调用，供会话结束检查使用。 |
| `platform/sessions/model_selection_events.py` | 为会话保存的模型选择生成哈希值，并检查何时可以写入新的选择。 |
| `platform/sessions/permission_mode_events.py` | 检查会话保存的权限模式，并构造准备写入的模式记录。 |
| `platform/sessions/root_instruction_events.py` | 保存逐级展开的说明、来源和诊断，也从基线事件重建冻结内容。 |
| `platform/sessions/session_journal.py` | 检查会话历史和写入请求，再把事件交给 Store 保存。 |
| `platform/sessions/session_title.py` | 清理和读取会话列表里显示的标题；标题不会进入模型消息或会话配置的身份计算。 |
| `platform/sessions/shared_memory_events.py` | 从会话历史中的事件算出共享 Markdown 记忆状态，并检查会话配置里的共享记忆设置。 |
| `platform/sessions/sqlite_session_store.py` | 用 SQLite 保存会话事件和当前程序的独占运行权。 |
| `platform/sessions/sqlite_team_store.py` | 用 SQLite 保存协作组、成员、消息和共享任务。 |
| `platform/sessions/store_port.py` | 定义 SessionJournal 读写会话数据库时使用的数据类型和只读接口。 |
| `platform/sessions/system_calls.py` | 检查程序自己提出的工具调用（v4 版本）及其结果的格式；这里不运行工具。 |
| `platform/sessions/turn_boundary.py` | 根据已读出的会话状态，检查当前这一轮能否在此处结束。 |
| `platform/sessions/turn_closure.py` | 根据完整事件历史检查取消后的状态，以及当前轮能否在步骤之间结束。 |
| `platform/sessions/turn_supplements.py` | 标识需要在上下文中显示的用户输入事件。 |

### platform/sessions/state

| 文件 | 负责什么 |
| --- | --- |
| `platform/sessions/state/turns.py` | 从事件算出用户输入和每一轮执行的状态。 |
| `platform/sessions/state/tools.py` | 从事件算出工具调用和审批相关的状态。 |
| `platform/sessions/state/subagents.py` | 从事件算出子任务的状态。 |
| `platform/sessions/state/metadata.py` | 从事件中记录会话配置、模型选择、标题，以及其他事件可能引用的记录。 |
| `platform/sessions/state/memory.py` | 根据事件记录共享记忆的使用情况和写入进度，不直接读写记忆文件。 |
| `platform/sessions/state/goal.py` | 记录会话的当前目标，并处理轮次结束和目标评估事件。 |
| `platform/sessions/state/core.py` | 从历史事件算出当前状态，并检查事件之间是否矛盾。 |
| `platform/sessions/state/compaction.py` | 检查何时可以使用上下文压缩生成的概要，并记录最新概要。 |
| `platform/sessions/state/catalog.py` | 记录会话初始配置阶段是否结束，以及创建时保存的根指令。 |
| `platform/sessions/state/__init__.py` | 导出会话状态和 `fold`；实现在 core.py。 |

### platform/skills

| 文件 | 负责什么 |
| --- | --- |
| `platform/skills/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/skills/__init__.py` | 提供读取本地 Skill 目录的接口。 |
| `platform/skills/catalog.py` | 按项目、用户、内置的顺序自动发现 Skill，记录 SKILL.md 和资源文件的大小与哈希值。 |
| `platform/skills/configuration.py` | 提供三个发现位置，只读取可选的 disabled 名单。 |
| `platform/skills/projection.py` | 从本会话成功的工具结果取回正文，跨轮、压缩和恢复后继续加入请求。 |
| `platform/skills/tools.py` | 通过 ToolRuntime 提供加载 Skill 和读取资源两个只读工具。 |

### platform/subagents

| 文件 | 负责什么 |
| --- | --- |
| `platform/subagents/ports.py` | 列出创建子会话时需要的工厂、配置和父会话方法。 |
| `platform/subagents/README.md` | subagents 的阅读入口：父子权限、调用路线、取消和结果。 |
| `platform/subagents/__init__.py` | 包标记；委派从 tool.py 和 session_delegation.py 开始读。 |
| `platform/subagents/approval_channel.py` | 让多个子任务依次借用父会话的界面向用户请求批准。 |
| `platform/subagents/background_control.py` | 检查后台任务控制请求的参数和相关执行记录。 |
| `platform/subagents/bash_execution_facts.py` | 从子会话的 Bash 结果中提取命令、退出状态和输出节选。 |
| `platform/subagents/child_extensions.py` | 为子会话挑选和检查父会话允许使用的 Skill 与 MCP 工具。 |
| `platform/subagents/child_scope.py` | 记录子会话能使用的工具、权限模式和工作副本。 |
| `platform/subagents/configuration.py` | 生成子任务配置记录；恢复时使用当前配置。记录本身不安装工具，也不授予权限。 |
| `platform/subagents/continuation.py` | 负责开始或继续运行子会话，并把结果写入父会话。 |
| `platform/subagents/continuation_history.py` | 从父会话的记录中查找子任务的首次运行和后续继续运行。 |
| `platform/subagents/contracts.py` | 定义子任务的配置、运行计划和返回结果，并检查传入的数据。 |
| `platform/subagents/control_tool.py` | 提供查询、等待和停止后台任务的工具。 |
| `platform/subagents/delegation_history.py` | 检查父会话保存的子任务计划，并计算已经使用的运行额度。 |
| `platform/subagents/fork_context.py` | 从父会话的模型请求中取出消息，供子任务继承上下文。 |
| `platform/subagents/model_admission.py` | 检查首次交给后台运行的子任务记录。 |
| `platform/subagents/report_guidance.py` | 定义父任务和子任务使用的报告要求。 |
| `platform/subagents/result_receipt.py` | 检查并整理一批子任务的结果，供父会话保存。 |
| `platform/subagents/service.py` | 启动父会话已经保存的子任务，等待结果，并处理取消和超时。 |
| `platform/subagents/session_delegation.py` | 准备并跟踪父会话交给子会话的任务。 |
| `platform/subagents/session_runner.py` | 创建子会话、跟踪它的运行，并从历史中整理结果。 |
| `platform/subagents/team_session.py` | 管理父会话和子会话之间的团队消息、成员和任务。 |
| `platform/subagents/team_source.py` | 整理队友消息的发送信息和正文，供消息传递与历史检查使用。 |
| `platform/subagents/team_tool.py` | 提供 Team 工具，让会话查询成员、发送消息和管理共享任务。 |
| `platform/subagents/tool.py` | 为 delegate_tasks 工具准备权限检查、审批内容和返回结果。 |
| `platform/subagents/tracking.py` | 为父会话界面整理子任务的状态和历史。 |

### platform/tools

| 文件 | 负责什么 |
| --- | --- |
| `platform/tools/coding_policy_validation.py` | 检查要保存的审批提示是否与代码工具的执行计划一致。 |
| `platform/tools/coding_edit_text.py` | 把文件编辑的结果整理成模型可以读的文字。 |
| `platform/tools/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `platform/tools/__init__.py` | 包标记；工具治理从 tool_runtime.py 开始读。 |
| `platform/tools/approval_denials.py` | 为用户拒绝过的操作计算哈希值，用来比较两次操作是否相同。 |
| `platform/tools/builtin_policy.py` | 检查读取已保存工具结果的分页请求是否符合要求。 |
| `platform/tools/code_outline.py` | 提取单个 Python 文件中的类、函数和参数，用来定位代码。 |
| `platform/tools/coding_bash.py` | 准备并运行前台 Bash 命令，处理进程、输出、超时和取消。 |
| `platform/tools/coding_contract.py` | 定义模型能看到的文件和命令工具，以及运行这些工具所需的计划检查。 |
| `platform/tools/coding_mutations.py` | 准备单个文件的修改内容，并在检查后把它写入工作区。 |
| `platform/tools/coding_search.py` | 在工作区里按路径查找文件，或在文件中搜索文字。 |
| `platform/tools/ask_user.py` | 向用户提问的工具 AskUserQuestion：检查问题格式，提问后这一轮结束。 |
| `platform/tools/coding_tools.py` | 为文件工具和 Bash 准备执行计划、判断权限，并调用具体工具。 |
| `platform/tools/coding_workspace.py` | 负责在工作区内打开目录和读取文件，并限制每次读取的数据量。 |
| `platform/tools/execution_eligibility.py` | 检查当前处理位置是否与下一步或自动维护的请求一致。 |
| `platform/tools/file_edit_snapshots.py` | 把编辑前的文件内容按会话存入 SQLite，供文件恢复时读取。 |
| `platform/tools/lifecycle.py` | 定义工具运行前、结果保存后要调用的方法。 |
| `platform/tools/managed_process_lifecycle.py` | 帮助前台工具停止进程组，并等待进程输出读完。 |
| `platform/tools/model_result_budget.py` | 决定工具结果怎样展示给模型，以及展示内容的字节上限。 |
| `platform/tools/permission_modes.py` | 根据权限模式，判断一个代码工具调用应允许、询问还是拒绝。 |
| `platform/tools/readonly_commands.py` | 检查命令是否符合只读白名单，决定能否省去普通审批；它不执行命令，也不隔离文件访问。 |
| `platform/tools/session_tool_allowances.py` | 保存本次会话选择“本次会话都允许”的代码操作，供后续权限检查使用；名单只保存在内存中。 |
| `platform/tools/policy_decisions.py` | 整理工具检查的决定和拒绝时的错误信息。 |
| `platform/tools/process_group_observation.py` | 检查 POSIX 进程组是否还存在。 |
| `platform/tools/provider.py` | 定义工具提供方的调用接口，并实现已保存工具结果的分页读取。 |
| `platform/tools/result_artifacts.py` | 把较长的工具结果保存到本地，需要时再一页页读给模型。 |
| `platform/tools/root_agents_file.py` | 逐级打开目录并安全读取说明文件，拒绝符号链接和不合要求的文件。 |
| `platform/tools/runtime_policy.py` | 根据本次打开会话使用的配置，决定工具失败结果怎样保留，以及哪些未知结果会阻止后续执行。 |
| `platform/tools/sandbox_binding.py` | 为命令沙箱配置生成一条可保存的配置记录。 |
| `platform/tools/tool_catalog.py` | 组合本次可以提供给模型的工具说明。 |
| `platform/tools/tool_display.py` | 为实时活动和 Trace 记录准备简短的工具名称、目标和子任务标题。 |
| `platform/tools/tool_names.py` | 管理 Memory 工具的内部名称和发给模型供应商的名称。 |
| `platform/tools/tool_registry.py` | 保存会话中工具名称与处理函数的对应关系。 |
| `platform/tools/tool_runtime.py` | 检查工具调用、请求必要的批准、运行工具并保存结果。 |
| `platform/tools/tool_scope.py` | 计算模型可以使用哪些工具，并拒绝范围之外的调用。 |
| `platform/tools/web_search.py` | 通过智谱接口搜索网页概要，并检查返回的链接和内容。 |
| `platform/tools/web_search_policy.py` | 检查网络搜索是否可用，以及发送查询前是否需要用户批准。 |
| `platform/tools/plan_file.py` | 规划模式的方案文件和提交方案的工具 ExitPlanMode。 |
| `platform/tools/web_fetch.py` | 读取一个公开网页，检查地址和大小，把正文转成文字。 |
| `platform/tools/web_fetch_policy.py` | 检查网页读取是否可用并决定是否询问用户；bypass 模式直接放行，需要批准时显示完整网址。 |

### platform/worktrees

| 文件 | 负责什么 |
| --- | --- |
| `platform/worktrees/README.md` | worktrees 的阅读入口：副本创建、差异核对和清理。 |
| `platform/worktrees/__init__.py` | 集中导出创建和检查 Git 工作副本需要的类型与后端。 |
| `platform/worktrees/backend.py` | 从 Git 已提交的版本创建、检查和清理独立工作副本。 |
| `platform/worktrees/configuration.py` | 决定 Git 工作副本放在哪里；恢复主会话时采用当前工作树配置。 |
| `platform/worktrees/session_worktrees.py` | 帮助父会话准备、找回和检查子任务的工作副本。 |
| `platform/worktrees/tool.py` | 提供检查工作副本的只读工具。 |

### spi

| 文件 | 负责什么 |
| --- | --- |
| `spi/README.md` | 本目录的阅读入口：职责和阅读顺序。 |
| `spi/__init__.py` | 包标记；模型适配器接口在 model_adapter.py。 |
| `spi/model_adapter.py` | 定义模型调用的输入、完整回复和流式回复片段。 |

### web

| 文件 | 负责什么 |
| --- | --- |
| `web/interactive_session.py` | 为 Web 界面提供发送输入、查看事件和取消操作的接口。 |
| `web/request_details.py` | 根据保存的模型请求内容生成只读详情，供网页查看。 |
| `web/tool_presentation.py` | 把已经记录的工具调用和结果整理成网页卡片。 |
| `web/README.md` | 本地 Web 界面的启动方法和结构。 |
| `web/__init__.py` | 包标记；Web 服务从 **main**.py 启动。 |
| `web/__main__.py` | 是本机 Web 服务的启动入口。 |
| `web/bridge.py` | 把浏览器操作交给会话，并管理页面的控制权和通知。 |
| `web/context_reader.py` | 把根据记录还原的模型请求整理成网页可阅读的目录和正文。 |
| `web/interaction.py` | 把审批请求展示在浏览器中，等待用户回答后交还给原来的请求。 |
| `web/messages.py` | 检查网页发来的消息，并整理发回网页的响应。 |
| `web/server.py` | 提供本机 HTTP 和 WebSocket 入口，把页面操作交给 WebBridge。 |
| `web/key_points.py` | 从事件里挑出值得先看的要点，显示在原始 JSON 之前。 |
| `web/views.py` | 把会话事件整理成聊天、时间线和详情页面需要的数据。 |

### web/static

| 文件 | 负责什么 |
| --- | --- |
| `web/static/app.js` | 维护浏览器界面的状态和交互事件。 |
| `web/static/context-reader.js` | 在浏览器里显示模型请求的内容块和明细。 |
| `web/static/dompurify.LICENSE.txt` | 保留随代码提供的 DOMPurify 文本净化组件的许可证。 |
| `web/static/index.html` | Web 主页面的结构和控件。 |
| `web/static/markdown.js` | 在浏览器里渲染助手回复的 Markdown。 |
| `web/static/marked.LICENSE.txt` | 保留随代码提供的 Marked Markdown 解析组件的许可证。 |
| `web/static/marked.umd.js` | 随代码提供的第三方 Markdown 解析器发行文件，供界面渲染使用。 |
| `web/static/purify.min.js` | 随代码提供的第三方 HTML 净化组件，处理渲染内容的安全过滤。 |
| `web/static/style.css` | 定义本地 Web 页面布局、组件样式和内容展示方式。 |
| `web/static/vendor-manifest.json` | 登记第三方前端文件的版本、许可证和校验值。 |
