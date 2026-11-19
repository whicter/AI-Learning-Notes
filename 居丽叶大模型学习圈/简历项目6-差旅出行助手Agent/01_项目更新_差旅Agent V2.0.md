# 项目更新|差旅Agent V2.0

> 来源（Source）：https://articles.zsxq.com/id_8gfpxk2jqcdi.html  
> 日期：2026年11月01日 22:54

本项目是[差旅Agent](https://t.zsxq.com/QvkcT) 的改进版本，版本一发布于2026年3月14日，是随着skills概念大火而生的项目，实现逻辑较为简单。

但随着AI coding工具的日益强大，原版项目已经难以满足水涨船高的面试需求，因此发布版本二，同样是Agent harness的项目，不涉及模型训练，定位是面向个人长期服务的差旅出行规划Personal Agent，引入了约束求解与规则校验、持久化执行与请求防重，并完善评测机制。

**没有看过第一版的同学不用再学习版本一的代码，只需大致阅读版本一的面试文档，理解其基本思想后即可直接开始学习版本二。**

**面试准备文档：**

飞书链接：https://my.feishu.cn/wiki/BHhmwgIpwi6n4ikaQctcqMFTnlg?from=from_copylink

密码：&863u676

还是老样子，去面试的时候如果问到了超出这个文档范围的问题，就：

1、在文档边上写评论、或者在这个帖子下面写评论，我看到就会补充

2、去原代码里找答案

3、看看《八股文速记》里面有没有

**代码解析文档和视频讲解：**

![](01_项目更新_差旅Agent%20V2.0/images/b104bb1c8d42.png)

**代码：**

链接: https://pan.baidu.com/s/17qObVpJ_Pi6rToJhkGJdnw?pwd=bkiq

提取码: bkiq

有同学说没有百度网盘的会员，所以夸克网盘也上传了一份：

我用夸克网盘给你分享了「居丽叶简历项目11：差旅出行助手V2.0」，点击链接或复制整段内容，打开「夸克APP」即可获取。

/~f9153bzZHi~:/

链接：[https://pan.quark.cn/s/b60c23081dee](https://pan.quark.cn/s/b60c23081dee)

**本项目涉及的技术栈**有：FastAPI · AgentScope · pi-durable · PostgreSQL · Redis · Milvus · CP-SAT · Harness Engineering· DAG· Skill Workflow· Memory Engineering· RAG · 模型评测

**代码与文档的区别：**

1. 代码里只有实现了 100 条单轮 + 3 组多轮，基线指标和当前系统的指标是基于这些数据评测得到的。Recall@5、MRR没有实际评测，知识库只提供了一些参考文档。

2. 「线上日志全量回流」没有落地，目前只处理评测结果，没有线上日志，

3. 无压测、无并发指标、无部署上线，单机单实例实现

4. Personal Agent 的主动工作相关没有实现，系统为纯被动应答。

5. Loop Engineering 、 Skill 自进化、部署上线相关参考[项目9](https://t.zsxq.com/ZdX8S)，可以迁移到本项目
