### 知识点讲解

**run_loop 的工作流程**

`run_loop` 是自动化优化 Skill description 的迭代脚本，流程如下：

```
输入评估集
    ↓
[Split] 60% train / 40% test（随机切分，固定不变）
    ↓
[Eval] 对当前 description 跑所有 train 查询，每条跑 3 次取平均触发率
    ↓
[Analyze] Claude 分析哪些 train 查询没触发成功，找出 description 的缺陷
    ↓
[Propose] Claude 提出改进后的新 description 候选
    ↓
[Eval] 对新 description 同时评估 train 和 test 分数
    ↓
重复最多 5 次迭代
    ↓
[Select] 选 test score 最高的描述作为最终结果
    ↓
输出 best_description + HTML 报告
```

**每条查询跑 3 次的原因**

LLM 的触发决策有随机性，单次结果不稳定。跑 3 次取平均，得到一个更可靠的触发率估计。

**为什么用 test score 而不是 train score 选最优？**

这是机器学习中防止**过拟合（overfitting）**的标准做法。

- **train score** 衡量的是 description 对它「见过」的查询的拟合程度
- **test score** 衡量的是 description 对它「没见过」的查询的泛化能力

run_loop 的优化过程中，Claude 不断分析 train 集的失败案例并修改 description。如果只用 train score 来选最优，Claude 可能会过度拟合 train 集里的特定措辞，对 train 以外的真实用户查询反而表现差。

用 test score 选最优，确保选出的 description 具有真实的泛化能力——在实际使用中遇到各种没见过的用户表达方式，依然能稳定触发。

---

### 面试标准回答

"run_loop 的核心流程是这样：先把评估集按 6:4 切分成 train 和 test，这个切分在整个优化过程中保持不变。然后对当前的 description 跑 train 集，每条查询跑 3 次取平均触发率，3 次是为了消除 LLM 输出的随机性。接着分析哪些查询没有触发成功，让 Claude 根据失败案例提出改进后的 description 候选，再同时评估新描述在 train 和 test 上的分数。这个循环最多跑 5 轮，最后输出一份 HTML 报告。

为什么选 test score 而不是 train score？这是防过拟合的标准思路。整个迭代过程 Claude 一直在看 train 集的失败案例，description 很可能慢慢被调成对这些特定查询高度适配，但对没见过的查询反而不行。test 集在优化过程中从来没有被用来指导修改，所以 test score 反映的是真正的泛化能力。选 train score 最高的描述，本质上是在选最会'背题'的那个；选 test score 最高的，才是选最会'举一反三'的那个。"
