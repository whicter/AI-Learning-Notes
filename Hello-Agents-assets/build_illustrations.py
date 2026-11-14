from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import re

ROOT = Path(__file__).resolve().parent
ROOT.mkdir(exist_ok=True)
FONT = '/System/Library/Fonts/Hiragino Sans GB.ttc'
INK = '#20324B'
MUTED = '#56677D'
BLUE = '#2563EB'
TEAL = '#087F8C'
ORANGE = '#B96619'
LINE = '#A7B6C8'
PALE = '#EEF4FF'
GREEN = '#E8F6F3'
CREAM = '#FFF4E5'
W = 1400
S = 2
fonts = {}

def font(size):
    if size not in fonts:
        fonts[size] = ImageFont.truetype(FONT, size * S)
    return fonts[size]

class Figure:
    def __init__(self, num, title, subtitle, height):
        self.im = Image.new('RGB', (W*S, height*S), '#FFFFFF')
        self.d = ImageDraw.Draw(self.im)
        self.h = height
        self.text(52, 35, f'FIG {num:02d}', 20, BLUE)
        self.text(52, 75, title, 38)
        self.text(52, 136, subtitle, 23, MUTED)

    def text(self, x, y, txt, size=26, color=INK, center=False):
        f = font(size)
        lines = txt.split('\n')
        for i, line in enumerate(lines):
            width = self.d.textlength(line, font=f)/S
            xx = x-width/2 if center else x
            assert xx >= 0 and xx+width <= W, (line, xx, width)
            self.d.text((xx*S, (y+i*(size+12))*S), line, font=f, fill=color)

    def box(self, x, y, w, h, title, body='', fill=PALE, color=BLUE):
        self.d.rounded_rectangle((x*S,y*S,(x+w)*S,(y+h)*S), radius=16*S, fill=fill)
        self.d.rounded_rectangle((x*S,y*S,(x+5)*S,(y+h)*S), radius=2*S, fill=color)
        self.text(x+22,y+18,title,28,color)
        if body:
            for line in body.split('\n'):
                assert self.d.textlength(line,font=font(23))/S <= w-44, (title,line)
            self.text(x+22,y+62,body,23)

    def arrow(self, points, color=LINE, width=3):
        pts=[(int(x*S),int(y*S)) for x,y in points]
        self.d.line(pts,fill=color,width=width*S,joint='curve')
        a,b=points[-2],points[-1]
        ang=math.atan2(b[1]-a[1],b[0]-a[0])
        n=12
        heads=[b,(b[0]-n*math.cos(ang-.45),b[1]-n*math.sin(ang-.45)),(b[0]-n*math.cos(ang+.45),b[1]-n*math.sin(ang+.45))]
        self.d.polygon([(int(x*S),int(y*S)) for x,y in heads],fill=color)

    def note(self, txt):
        self.d.line((52*S,(self.h-76)*S,(W-52)*S,(self.h-76)*S),fill='#E2E8F0',width=S)
        self.text(52,self.h-54,txt,21,MUTED)

    def save(self,name):
        self.im.resize((W,self.h),Image.Resampling.LANCZOS).save(ROOT/name)

f=Figure(1,'Agent 如何完成一次任务','模型提出行动，程序执行工具，工具结果再交给模型。',780)
for x,title,color in [(52,'用户',INK),(492,'模型',BLUE),(932,'程序与工具',TEAL)]:
    f.text(x+180,205,title,26,color,True)
f.box(52,265,360,120,'提出目标','查北京天气并推荐景点',fill='#F1F5F9',color=INK)
f.box(492,265,360,120,'选择行动','需要先查询天气')
f.box(932,265,360,120,'执行天气查询','返回：下雨，18°C',GREEN,TEAL)
f.arrow([(412,325),(492,325)])
f.arrow([(852,325),(932,325)])
f.box(492,450,360,120,'根据结果继续决策','下雨，搜索室内景点')
f.box(932,450,360,120,'执行景点搜索','返回：候选景点与资料',GREEN,TEAL)
f.arrow([(1112,385),(1112,420),(672,420),(672,450)])
f.arrow([(852,510),(932,510)])
f.text(52,470,'下一轮输入中包含\n上一轮工具的返回结果。',25,MUTED)
f.box(492,610,360,78,'综合资料，生成回答')
f.arrow([(1112,570),(1112,649),(852,649)])
f.arrow([(492,649),(232,649),(232,385)])
f.note('图中天气和景点是流程示例，不是实时查询；输出“正在查询”不等于工具已执行。')
f.save('01-agent-loop.png')

f=Figure(2,'模型每次到底看到了什么','上下文是本次调用提供的信息，不等于电脑里存放的全部资料。',620)
for i,(title,body) in enumerate([('任务与约束','城市、预算、偏好'),('工具说明','名称、用途、参数'),('资料与历史','检索片段、工具结果')]):
    x=52+i*440
    f.box(x,220,360,120,title,body)
    f.arrow([(x+180,340),(x+180,385),(672,385),(672,420)])
f.box(442,420,460,105,'本轮模型调用','依据当前可见信息生成输出',GREEN,TEAL)
f.note('保存文件、建立知识库或存储记忆后，还需要读取并选取有关内容，提供给模型。')
f.save('02-context-input.png')

f=Figure(3,'第一章代码中的五个协作部件','沿着数据流读代码：谁给指令，谁决定，谁执行，谁保存结果。',750)
f.box(52,220,370,125,'系统提示词','AGENT_SYSTEM_PROMPT\n说明工具和输出格式')
f.box(52,405,370,125,'历史记录','prompt_history\n保存任务、行动和观察')
f.box(502,310,370,125,'模型客户端','llm.generate(...)\n返回行动描述')
f.box(952,220,370,125,'解析与工具注册','available_tools\n按名称找到实际函数',GREEN,TEAL)
f.box(952,405,370,125,'工具执行','天气函数 / 搜索函数\n返回 Observation',GREEN,TEAL)
f.arrow([(422,280),(460,280),(460,345),(502,345)])
f.arrow([(422,465),(460,465),(460,400),(502,400)])
f.arrow([(872,372),(912,372),(912,280),(952,280)])
f.arrow([(1137,345),(1137,405)])
f.arrow([(952,468),(895,468),(895,580),(237,580),(237,530)],TEAL)
f.text(520,605,'for 循环控制重复执行；Finish 或次数上限使其停止。',24,MUTED,True)
f.note('模型返回的是行动描述；Python 程序解析后才会执行函数。停止运行也不代表任务成功。')
f.save('03-code-map.png')

f=Figure(4,'三种经典范式的区别','范式是任务的组织方式，可以组合使用，也可以使用同一个底层模型。',805)
rows=[(225,'ReAct','依据反馈选择下一步',['判断下一步','执行工具','观察结果']),
      (400,'Plan-and-Solve','先规划，再逐步求解',['生成计划','执行步骤','整合结果']),
      (575,'Reflection','先做一版，再检查修订',['生成初稿','检查反馈','修改结果'])]
for y,title,sub,labels in rows:
    f.text(52,y+10,title,28,BLUE)
    f.text(52,y+58,sub,21,MUTED)
    for i,label in enumerate(labels):
        x=400+i*305
        f.box(x,y,250,105,label,fill=GREEN if title=='Reflection' else PALE,color=TEAL if title=='Reflection' else BLUE)
        if i<2:f.arrow([(x+250,y+52),(x+305,y+52)])
    if title=='ReAct':f.arrow([(1135,y+105),(1135,y+135),(525,y+135),(525,y+105)],BLUE)
f.note('Reflection 的检查可能出错；真实资料、规则检查和测试结果能为反馈提供依据。')
f.save('04-paradigms.png')

f=Figure(5,'工具调用和框架分别负责什么','结构化调用描述不等于工具已执行，框架负责把各个部件连接起来。',660)
items=[('模型','选择工具并生成参数'),('控制程序','检查参数、查找工具'),('工具函数','执行查询或操作'),('执行结果','交回模型继续处理')]
for i,(a,b) in enumerate(items):
    x=52+i*335
    f.box(x,245,290,140,a,b,fill=GREEN if i==2 else PALE,color=TEAL if i==2 else BLUE)
    if i<3:f.arrow([(x+290,315),(x+335,315)])
f.box(52,465,1295,100,'框架的职责','统一管理模型客户端、消息历史、工具登记、执行循环与配置',fill='#F1F5F9',color=INK)
f.note('Function Calling 帮助模型输出结构化请求；实际执行仍由应用程序完成。')
f.save('05-tools-framework.png')

f=Figure(6,'记忆如何跨越两次对话','写入和取回是两个独立环节；保存了信息，还需要在适当时机使用它。',650)
f.box(52,225,360,115,'第一次对话','用户：我偏好历史文化')
f.box(492,225,360,115,'提取并保存','记忆：偏好历史文化',GREEN,TEAL)
f.box(932,225,360,115,'持久化存储','程序重启后仍可读取',GREEN,TEAL)
f.arrow([(412,282),(492,282)])
f.arrow([(852,282),(932,282)])
f.box(52,440,360,115,'第二次对话','用户：推荐一个景点')
f.box(492,440,360,115,'检索相关记忆','取回用户偏好')
f.box(932,440,360,115,'加入本轮上下文','模型结合偏好推荐')
f.arrow([(412,497),(492,497)])
f.arrow([(852,497),(932,497)])
f.arrow([(1112,340),(1112,390),(672,390),(672,440)],TEAL)
f.note('只有保存在进程内的列表通常会随进程结束而丢失；跨会话记忆依赖实际存储实现。')
f.save('06-memory.png')

f=Figure(7,'RAG 从资料到答案的全过程','先准备可检索的资料，再根据问题找片段，最后让模型依据片段回答。',790)
f.text(52,215,'资料准备',27,TEAL)
for i,(title,body) in enumerate([('读取文档','课程笔记、说明文档'),('切分片段','保留必要的上下文'),('建立检索索引','可使用向量等检索方式')]):
    x=52+i*440
    f.box(x,270,360,120,title,body,GREEN,TEAL)
    if i<2:f.arrow([(x+360,330),(x+440,330)],TEAL)
f.text(52,445,'回答问题',27,BLUE)
for i,(title,body) in enumerate([('提出问题','ReAct 是什么意思？'),('检索相关片段','找到定义与例子'),('模型生成答案','结合片段回答并标明依据')]):
    x=52+i*440
    f.box(x,500,360,120,title,body)
    if i<2:f.arrow([(x+360,560),(x+440,560)])
f.arrow([(1112,390),(1112,440),(672,440),(672,500)],TEAL)
f.note('RAG 通常不修改模型参数。检索错误和生成错误是不同问题，需要分别检查。')
f.save('07-rag.png')

f=Figure(8,'上下文工程如何组织本轮输入','GSSC：收集、选择、结构化、压缩，让有限输入保留会影响决策的信息。',710)
labels=[('Gather 收集','历史、记忆、工具结果、资料'),('Select 选择','保留当前任务相关内容'),('Structure 组织','分清目标、约束、状态和证据'),('Compress 压缩','减少重复，保留预算与闭馆等约束')]
for i,(a,b) in enumerate(labels):
    x=52+i*335
    f.box(x,250,290,172,a,b.replace('、工具结果、','、\n工具结果、').replace('、状态和','、\n状态和').replace('预算与闭馆等约束','预算\n与闭馆等约束'),fill=PALE)
    if i<3:f.arrow([(x+290,336),(x+335,336)])
f.box(242,495,900,115,'本轮可用上下文','用户预算 100 元；偏好文化活动；有雨；候选 A 已闭馆。',GREEN,TEAL)
f.arrow([(1202,422),(1202,470),(692,470),(692,495)])
f.note('压缩不是一味删字：一旦丢失关键约束，输入更短也可能使答案更差。')
f.save('08-context-engineering.png')

f=Figure(9,'Function Calling 和 MCP 处在不同位置','模型选择行动，应用负责执行，协议为跨系统连接提供约定。',745)
f.box(52,245,340,130,'模型','生成工具名和参数\nFunction Calling')
f.box(512,245,340,130,'应用程序','解析请求、管理执行\n包含 MCP 客户端')
f.box(972,245,340,130,'MCP 服务端','暴露工具和数据\n执行并返回结果',GREEN,TEAL)
f.arrow([(392,310),(512,310)])
f.arrow([(852,310),(972,310)],TEAL)
f.text(910,210,'MCP',22,TEAL,True)
f.arrow([(1142,375),(1142,425),(682,425),(682,375)],TEAL)
f.box(232,515,370,110,'智能体 A','研究资料')
f.box(802,515,370,110,'智能体 B','接收任务并协作')
f.arrow([(602,570),(802,570)])
f.text(702,525,'A2A',24,BLUE,True)
f.note('这是层次关系示意：MCP 连接应用与外部能力，A2A 关注智能体之间的通信协作。')
f.save('09-protocols.png')

f=Figure(10,'一次回答出错时怎样定位','把结果拆成可检查的环节，避免只凭回答是否流畅来判断质量。',735)
nodes=[('理解目标','城市和预算是否正确'),('选择与调用工具','工具和参数是否正确'),('获得资料','结果是否相关、有效'),('综合回答','结论是否符合证据')]
for i,(a,b) in enumerate(nodes):
    x=52+i*335
    f.box(x,245,290,135,a,b)
    if i<3:f.arrow([(x+290,312),(x+335,312)])
f.text(52,445,'每个环节保留可检查的记录',28,TEAL)
f.box(52,505,620,120,'质量维度','任务完成、事实正确、约束遵守',GREEN,TEAL)
f.box(722,505,620,120,'效率与失败处理','耗时、调用成本、超时和资料缺失',CREAM,ORANGE)
f.note('运行结束只说明执行停止。任务是否成功，需要用固定案例和明确标准评估。')
f.save('10-evaluation.png')

# Place each illustration beside the concept it explains.
note=ROOT.parent/'Hello-Agents 零基础学习笔记.md'
s=note.read_text()
s=s.replace('# Hello-Agents 零基础学习笔记','# Hello-Agents 零基础图文笔记',1)
blocks=[
('### 1.1 用旅行助手理解 Agent','01-agent-loop.png','图 1　旅行助手中的决策、执行与反馈。'),
('### 2.3 Prompt 和 Context','02-context-input.png','图 2　只有提供给本轮调用的信息，才是模型此刻可见的上下文。'),
('## 4 第一章旅行助手的代码拆解','03-code-map.png','图 3　提示词、历史、模型客户端、解析器和工具如何连接。'),
('## 5 三种经典智能体范式','04-paradigms.png','图 4　ReAct、Plan-and-Solve 和 Reflection 的流程对比。'),
('## 6 工具调用和框架','05-tools-framework.png','图 5　调用描述、程序执行和框架职责的关系。'),
('## 7 记忆系统','06-memory.png','图 6　跨会话记忆需要保存、检索和重新提供给模型。'),
('## 8 RAG 检索增强生成','07-rag.png','图 7　RAG 的资料准备与回答过程。'),
('## 9 上下文工程','08-context-engineering.png','图 8　用 GSSC 组织有限的模型输入。'),
('## 10 智能体通信协议和多智能体','09-protocols.png','图 9　工具调用、MCP 和 A2A 的不同位置。'),
('## 12 智能体评估','10-evaluation.png','图 10　沿着执行链路定位错误，再评估结果与效率。')]
for anchor,filename,caption in blocks:
    absolute=str(ROOT/filename)
    if absolute not in s:
        s=s.replace(anchor+'\n',anchor+f'\n\n![{caption}]({absolute})\n\n*{caption}*\n',1)
# Replace the first text-only diagram where the adjacent image now explains it.
start=s.index('一个可调用工具的智能体可以这样处理：')
end=s.index('这里有三个不同的角色：',start)
s=s[:start]+s[end:]
note.write_text(s)
print(f'Generated {len(blocks)} illustrations and updated {note.name}')
