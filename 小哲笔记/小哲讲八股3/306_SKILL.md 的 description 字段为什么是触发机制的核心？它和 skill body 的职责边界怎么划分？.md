## 知识点讲解

### 触发机制的工作原理

### Claude 在每次对话中能看到所有已安装 Skill 的 `name + description`（第一层元数据）。Claude 根据这段描述来判断：「当前用户的请求，是否需要调用这个 Skill？」

这意味着 `description` 承担的是**路由决策**职责——它是 Claude 决定要不要"打开这本书"的唯一依据。

**两个字段的职责边界**

| 字段 | 职责 | 放什么内容 |
| --- | --- | --- |
| `description` | **触发判断**：什么时候用这个 Skill | 触发场景、适用条件、关键词映射、不适用的边界 |
| `body` | **执行指导**：怎么用这个 Skill | 具体步骤、代码示例、注意事项、资源引用 |

**为什么所有 "when to use" 信息必须在 description 而不是 body？**

因为 body 只有在 Skill 被触发**之后**才会加载。如果把触发条件写在 body 里，模型在决策阶段根本看不到它，相当于把开门密码锁在门里面——逻辑上行不通。

**"Pushy" 描述的设计原则**

实践发现 Claude 有「undertrigger」倾向——在该用 Skill 的时候不用。因此 description 要主动枚举触发场景，甚至带一点"催促感"，而不是写得过于克制。

---

### 面试标准回答

"description 是触发机制的核心，原因很直接：Claude 在每次对话开始时，能看到的只有所有 Skill 的名字和描述，正文是不加载的。所以 Claude 对'要不要用这个 Skill'的判断，完全依赖 description 这段文字。这相当于一个路由器，description 是路由规则。

职责边界上，description 负责回答'什么时候用'，body 负责回答'怎么用'。两者不能混淆。如果你把触发条件写在 body 里，那 Skill 还没被触发，body 就没加载，模型永远看不到那个触发条件，逻辑上就死循环了。

另外有一个细节，description 要写得稍微'pushy'一点——就是主动列出各种触发场景，甚至用'whenever'、'even if they don't explicitly ask'这样的措辞。因为测试发现模型有 undertrigger 的倾向，描述写得太保守会导致该用的时候没用上。"
