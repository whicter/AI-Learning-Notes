### 知识点讲解

**什么是 undertrigger 问题？**

Undertrigger 是指：Claude 在**应该触发 Skill 的情况下，没有触发**。这是 Skill 系统实践中发现的一个系统性偏差，不是个例问题，而是模型的内在倾向。

**为什么 Claude 有 undertrigger 倾向？**

有几个可能的原因：

- Claude 默认倾向于「用已有能力直接解决问题」，而不是主动寻找额外工具
- description 如果写得过于保守/概括，模型对「这个 Skill 是否匹配当前任务」的判断会偏向保守
- 触发 Skill 有一定的不确定性成本，模型在模糊情况下倾向于不触发

**"Pushy" 描述的写法原则**

「Pushy」不是让描述夸张或不准确，而是：

1. **主动枚举触发场景**，而不是只写功能摘要
    - 保守写法：「处理 Word 文档的工具」
    - Pushy 写法：「当用户提到 Word、.docx、文档格式、表格、修订记录、邮件附件中的文档时，使用此 Skill」
2. **使用包容性触发语言**
    - 加入「even if they don't explicitly ask for...」
    - 加入「whenever」、「always use」等强触发词
3. **覆盖用户的间接表达**
    - 用户不会说「请帮我用 docx Skill」，而是说「帮我整理一份报告」「给我出一份正式文件」——这些间接表达都要在 description 里体现

**Pushy 的边界**

Pushy 不是无限扩大触发范围。描述仍然要准确，不能把和这个 Skill 无关的场景也写进去，否则会导致 overtrigger——在不该触发的时候触发，同样是问题。

---

### 面试标准回答

"description 要写得 pushy，是因为实践中发现 Claude 有 undertrigger 的系统性倾向——就是该用 Skill 的时候没用。这不是偶发情况，是模型的内在偏差，所以需要在 description 的设计上主动对抗它。

具体来说，pushy 有几层意思。第一，主动枚举触发场景，不要只写这个 Skill 是干嘛的，要写'用户说了什么话就要触发它'，覆盖用户可能用到的各种自然语言表达。第二，用包容性的触发语言，比如'whenever'、'even if the user doesn't explicitly ask for'，降低触发的门槛。第三，要考虑用户的间接表达——用户不会说'请用某某 Skill'，他们会说'帮我弄个报告'、'整理一份文件'，这些间接表达要在 description 里映射到 Skill。

当然 pushy 是有边界的，不是说越宽泛越好。描述仍然要准确，不能把不相关的场景也拉进来，那就从 undertrigger 变成 overtrigger 了，一样是问题。核心是在准确的前提下，尽量主动、具体地描述触发条件。"
