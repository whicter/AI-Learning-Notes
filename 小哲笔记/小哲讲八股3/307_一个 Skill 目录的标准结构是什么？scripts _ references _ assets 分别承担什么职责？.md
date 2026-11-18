### 知识点讲解

**标准目录结构**

```
skill-name/
├── SKILL.md              （必须）
│   ├── YAML frontmatter  （name, description 必填）
│   └── Markdown 正文指令
└── 捆绑资源/              （可选）
    ├── scripts/           可执行代码
    ├── references/        参考文档
    └── assets/            输出用文件
```

**三类资源的职责**

**scripts/**

- 存放可以直接运行的脚本（Python、Shell 等）
- 适合处理**确定性、重复性**的任务，比如文件格式转换、XML 解包、校验等
- 关键优势：脚本可以**不加载全文直接执行**，不占 context

**references/**

- 存放较长的参考文档、API 文档、领域知识等
- 适合**大体量、有选择性查阅**需求的内容
- 建议超过 300 行的文件附上目录（table of contents），方便模型定向跳转

**assets/**

- 存放输出时需要用到的静态文件，比如 Word 模板、图标、字体
- 这些文件不是给模型"读"的，而是**作为素材参与最终输出**

**多域组织模式**

当一个 Skill 支持多个子方向时（比如云部署支持 AWS / GCP / Azure），推荐按变体组织：

```
cloud-deploy/
├── SKILL.md          （workflow + 选择逻辑）
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

Claude 只读取当前任务对应的那一个 reference 文件，避免加载无关内容。

---

### 面试标准回答

"标准结构是一个根目录下必须有 SKILL.md，然后可选地有一个资源文件夹，里面分三类：scripts、references、assets。

scripts 放可执行脚本，一般是处理确定性任务的，比如格式转换、文件校验，好处是可以直接运行而不用把代码内容加载进 context，很省 token。

references 放参考文档，适合那些内容量比较大、但不是每次都全部用到的知识，比如某个 API 的完整文档。建议超过 300 行就要加个目录，方便模型跳转查阅。

assets 放静态文件，像模板、字体、图标这类，是给输出用的素材，不是给模型读的。

另外有个多域组织的技巧，就是当一个 Skill 支持多个子场景时，按变体拆成多个 reference 文件，SKILL.md 里写清楚选哪个的逻辑，这样 Claude 每次只加载当前相关的那一份，保持上下文的精简。"
