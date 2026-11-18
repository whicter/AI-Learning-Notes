# 项目更新|股票Agent V2.0

> 来源（Source）：https://articles.zsxq.com/id_hxesvb0i8d1b.html  
> 日期：2026年11月15日 21:58

本项目是[股票Agent 的](https://t.zsxq.com/A3RIO)改进版本，版本一发布于2025年8月19日，是随着MCP概念大火而生的项目，并且其中有较多模型训练的内容。

然而随着模型能力的增强，公司内部无论是算法岗还是开发岗都把注意力转向了Harness的搭建，模型训练逐渐式微，因此本次更新的重点在于Harness 治理、证据分级、多专家对抗、版本化记忆、受控自进化（RSI）、Jev决策模型，不再涉及模型训练。

**没有看过第一版的同学不用再学习版本一的代码，只需大致阅读版本一的面试文档，理解其基本思想后即可直接开始学习版本二。**

**面试准备文档：**

飞书链接：https://my.feishu.cn/wiki/USVBwcRSjiWZjskRD2scLwa3nPc?from=from_copylink

密码：823295p@

还是老样子，去面试的时候如果问到了超出这个文档范围的问题，就：

1、在文档边上写评论、或者在这个帖子下面写评论，我看到就会补充

2、去原代码里找答案

3、看看《八股文速记》里面有没有

**代码：**

链接: https://pan.baidu.com/s/1_wBkF3l1Jb7pF2BiT_FpbA?pwd=mdhb

提取码: mdhb

有同学说没有百度网盘的会员，所以夸克网盘也上传了一份：

我用夸克网盘给你分享了「居丽叶的简历项目12：股票投研V2.0」，点击链接或复制整段内容，打开「夸克APP」即可获取。

/~e01e3cJlFN~:/

链接：https://pan.quark.cn/s/873677ecdbb5

**代码解读文档：**

飞书链接：https://my.feishu.cn/wiki/BGFxwHHf1iAvNkktG6PcMfSmngb

密码：74&e8867

**本项目涉及的技术栈**有：

LangGraph、Pydantic v2、FastMCP、DeepSeek（对话 + Search/Fetch）、Jev、MongoDB、AKShare、FastAPI、React、OpenTelemetry

**文档和代码实现的差距点：**

代码基本实现了面试文档中描述的方案的95%，只有以下三点没有实现：

1. 模型没分强弱： 配置里分了classify、draft、reason三种角色，但三种用的是同模型，只是推理力度设得不同，没有分别配置更合适的模型。

2. Kev 的温度没调好：现在的温度 0.75 是按之前 DeepSeek 测试调出来的。按 Kev 自己的测试，0.5 更合适，拒判率偏高（20.8%）的问题也还在。这个点在 面试准备文档 里写成了一个后续优化方向。

3. 公告只有标题：现在只拿了网站公告的文章标题，模型根据原文总结摘要的代码还未做。
