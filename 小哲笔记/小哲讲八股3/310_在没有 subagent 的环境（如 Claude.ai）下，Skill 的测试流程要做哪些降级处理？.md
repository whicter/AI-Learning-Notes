### 知识点讲解

**完整环境（Claude Code / Cowork）的测试流程**

在有 subagent 的环境中，测试流程是：

- 并行 spawn 多个独立 subagent，每个 subagent 独立运行一个测试用例
- subagent 不知道 Skill 是谁写的，避免"作者偏见"
- 同时运行 baseline（不带 Skill）和 with-Skill 两组，做对照比较
- 用 `generate_review.py` 生成交互式 HTML review 页面
- 跑定量 benchmark，获得可靠的统计指标

**Claude.ai 环境的降级处理**

由于 Claude.ai 没有 subagent，需要逐项降级：

| 完整流程 | Claude.ai 降级方案 |
| --- | --- |
| 并行执行多个测试用例 | **串行执行**，一个一个来 |
| 独立 subagent 运行（避免作者偏见） | **作者自己运行**，效果打折扣，用人工 review 补偿 |
| 浏览器打开 HTML review | **跳过**（无 display），直接在对话中展示结果和文件路径 |
| 跑 baseline 对照组 | **跳过**（没有独立 subagent，baseline 无意义） |
| 定量 benchmark | **跳过**，改为用户定性反馈为主 |
| Description 优化（run_loop） | **跳过**（依赖 `claude -p`<br> CLI，Claude.ai 不可用） |

**降级后的核心迭代逻辑保持不变**

虽然工具受限，核心闭环仍然是：草稿 → 测试 → 用户反馈 → 修改 → 重复。只是精度更低、更依赖人工判断。

---

### 面试标准回答（口语形式）

"Claude.ai 环境最大的限制是没有 subagent，这导致几个地方需要降级。

第一，测试用例只能串行跑，不能并行。第二，测试是作者自己跑自己写的 Skill，不是独立的 subagent，所以有'作者知道意图'的偏见，这个偏差需要靠更严格的人工 review 来补偿。第三，baseline 对照组要跳过，因为 baseline 的意义依赖于独立执行，作者来跑没有参考价值。第四，定量 benchmark 也跳过，改成以用户定性反馈为主。第五，description 优化的 run_loop 也不能用，因为它底层依赖 `claude -p` 这个 CLI 工具，Claude.ai 环境里没有。

不过核心的迭代逻辑是不变的——草稿、测试、反馈、修改、再来一轮。只是精度降低了，更依赖人工判断，而不是自动化指标。这是在工具约束下的合理权衡，不是说就不用迭代了。"
