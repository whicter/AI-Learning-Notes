from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ROOT = Path(__file__).resolve().parent
FONT = '/System/Library/Fonts/STHeiti Light.ttc'
S = 2
W = 1200
COLORS = dict(blue='#3168d5', teal='#138c84', purple='#7953b9', orange='#cc7429', ink='#20304a', muted='#65748b', line='#dbe3ef')

class Figure:
    def __init__(self, name, title, sub, height=600):
        self.name, self.h = name, height
        self.im = Image.new('RGB', (W*S,height*S), '#f5f8fd')
        self.d = ImageDraw.Draw(self.im)
        self.text(45,32,title,32)
        self.text(45,82,sub,19,'muted')
    def text(self,x,y,t,size=23,color='ink',anchor=None):
        self.d.text((x*S,y*S),str(t),font=ImageFont.truetype(FONT,int(size*S)),fill=COLORS.get(color,color),anchor=anchor,spacing=10*S)
    def rect(self,x,y,w,h,fill='#ffffff',outline='#dbe3ef',r=16):
        self.d.rounded_rectangle((x*S,y*S,(x+w)*S,(y+h)*S),radius=r*S,fill=fill,outline=outline,width=2*S)
    def box(self,x,y,w,h,title,body='',color='blue'):
        self.rect(x,y,w,h)
        self.d.rounded_rectangle((x*S,y*S,(x+5)*S,(y+h)*S),radius=2*S,fill=COLORS[color])
        self.text(x+18,y+19,title,25,color)
        for i,l in enumerate(body.split('\n')):
            self.text(x+18,y+62+i*29,l,19,'muted')
    def arrow(self,x1,y1,x2,y2,color='muted',width=3):
        c=COLORS.get(color,color)
        self.d.line((x1*S,y1*S,x2*S,y2*S),fill=c,width=width*S)
        a=math.atan2(y2-y1,x2-x1)
        pts=[(x2*S,y2*S)]
        for k in [-0.48,0.48]:
            pts.append(((x2-13*math.cos(a+k))*S,(y2-13*math.sin(a+k))*S))
        self.d.polygon(pts,fill=c)
    def note(self,t):
        self.rect(45,self.h-93,1110,53,fill='#e9effa',outline='#e9effa')
        self.text(65,self.h-79,t,20)
    def save(self):
        self.im.save(ROOT/(self.name+'.png'),optimize=True)

f=Figure('01-generation','一句话怎样从输入变成回答','先把文字变成数字，再计算下一个 token 的概率。')
for x,title,body,c in [(45,'文字','我喜欢','blue'),(275,'分词与编号','[0, 1]','teal'),(505,'模型计算','结合已有上下文','purple'),(735,'概率分布','学习 67%\n苹果 24% · 其他 9%','orange')]:
    f.box(x,180,195,155,title,body,c)
    if x<735:f.arrow(x+195,257,x+225,257)
f.box(960,180,195,155,'选出 token','学习','teal');f.arrow(930,257,957,257)
f.arrow(1057,350,1057,415);f.arrow(1057,415,145,415);f.arrow(145,415,145,343)
f.text(390,430,'把“学习”接回前文，继续预测下一步',23,'blue')
f.note('图中概率为示意。概率高表示更符合模型预测，不保证事实正确。');f.save()

f=Figure('02-tokenizer','分词与嵌入是两次不同的转换','Tokenizer 决定切分和编号；Embedding 把编号转换为可学习的向量。')
f.box(45,160,300,115,'原始文字','我喜欢学习大模型')
f.arrow(350,217,410,217)
f.box(420,160,735,115,'一种教学切分','我        喜欢        学习        大模型','teal')
f.arrow(775,280,775,317)
f.box(420,325,735,100,'token ID','0           1             2              3','blue')
f.box(45,325,300,100,'嵌入表的一行','2 → [0.12, -0.35, …]','purple')
f.arrow(410,375,350,375)
f.note('编号只是标签，没有数值大小的语义；向量中的数值会随训练更新。');f.save()

f=Figure('03-tensor','张量形状就是数据的尺寸说明','例子：[B, T, D] = [2, 5, 8]，共有 2 × 5 × 8 = 80 个数字。',650)
for b,x in enumerate([110,650]):
    f.text(x,145,f'第 {b+1} 条序列：5 个 token',24,'blue')
    for row in range(5):
        f.text(x-65,207+row*47,str(row+1),17,'muted')
        for col in range(8):
            f.rect(x+col*48,195+row*47,40,38,fill=['#dce8ff','#c5d8fb','#a6c1ef'][(row+col)%3],r=6)
    f.text(x,448,'每一行 = 一个 token 的 8 维向量',19,'muted')
f.text(85,510,'B = 一批有几条序列     T = 每条有几个 token     D = 每个向量有几个数',23)
f.note('不要只记住三个字母：先明确每个维度在当前代码里表示什么。');f.save()

f=Figure('04-transformer','一个现代 Transformer 层的简化结构','这里使用常见的 Pre Norm 结构；多层堆叠后再接最终归一化与输出层。',700)
items=[('输入 x','已有的位置向量'),('归一化 → 注意力','让各位置交流信息'),('残差相加','原输入 + 注意力输出'),('归一化 → FFN','加工每个位置的表示'),('残差相加','本段输入 + FFN 输出')]
for i,(a,b) in enumerate(items):
    y=140+i*88;f.box(330,y,600,73,a,'',color='purple' if i in [1,3] else 'blue');f.text(570,y+26,b,18,'muted')
    if i<4:f.arrow(630,y+74,630,y+86)
f.arrow(315,176,230,176);f.arrow(230,176,230,352);f.arrow(230,352,320,352)
f.arrow(315,352,170,352);f.arrow(170,352,170,528);f.arrow(170,528,320,528)
f.text(43,260,'保留输入',20,'teal');f.text(43,441,'再加回来',20,'teal')
f.note('注意力汇总上下文，FFN 加工表示；残差和归一化帮助深层网络稳定训练。');f.save()

f=Figure('05-attention','注意力如何做加权汇总','用一个标量示例看懂“匹配 → 权重 → 汇总”；真实 Value 通常是向量。')
f.box(45,175,240,150,'当前位置的 Q','我要找哪些信息？','purple')
for i,(k,v,w) in enumerate([('位置 A',10,0.1),('位置 B',20,0.2),('位置 C',30,0.7)]):
    x=350+i*275
    f.box(x,150,245,150,k,f'K：用于匹配\nV：{v}','blue')
    f.arrow(x+122,305,x+122,345)
    f.text(x+42,358,f'权重 {w:.1f}',30,'teal')
f.arrow(290,245,340,225)
f.rect(350,420,795,56,fill='#e8f5f1',outline='#e8f5f1')
f.text(375,435,'0.1 × 10 + 0.2 × 20 + 0.7 × 30 = 26',26,'teal')
f.note('Q 与 K 生成匹配得分，经 softmax 变成权重；权重再与 V 相乘并求和。');f.save()

f=Figure('06-causal-mask','因果遮罩防止模型提前看到答案','行 = 当前处理的位置；列 = 它准备读取的位置。',670)
words=['我','爱','学习','大模型'];x0=410;y0=210;step=72
for i,w in enumerate(words):
    f.text(x0+i*step+30,165,w,20,'ink',anchor='mt')
    f.text(360,y0+i*step+22,w,20,'ink',anchor='rt')
    for j in range(4):
        fill='#d8eee9' if j<=i else '#e4e8ef'
        f.rect(x0+j*step,y0+i*step,62,62,fill=fill,outline=fill,r=8)
        f.text(x0+j*step+31,y0+i*step+19,'可见' if j<=i else '遮住',17,'teal' if j<=i else 'muted',anchor='mt')
f.box(770,250,370,165,'例：在“爱”的位置','只能使用“我、爱”\n据此预测下一个词“学习”','blue')
f.note('训练可以同时计算多个位置，但每个位置仍只能读取自己及前面的位置。');f.save()

f=Figure('07-training','训练把预测错误变成参数更新','同一批数据经过前向计算、损失计算、反向传播，再由优化器更新参数。',660)
for i,(a,b,c) in enumerate([('输入与目标','x：我 / 爱 / 学习\ny：爱 / 学习 / 大模型','blue'),('模型预测','给每个候选 token 打分\n转成预测概率','purple'),('计算损失','正确答案概率越低\n惩罚通常越大','orange')]):
    x=45+i*385;f.box(x,160,340,155,a,b,c)
    if i<2:f.arrow(x+345,238,x+379,238)
f.box(815,360,340,115,'反向传播','计算各参数的梯度','orange')
f.box(430,360,340,115,'优化器更新','参数 ← 参数 − 步长 × 梯度','teal')
f.box(45,360,340,115,'下一批数据','重复，逐步学习规律','blue')
f.arrow(985,320,985,353);f.arrow(810,418,775,418);f.arrow(425,418,390,418);f.arrow(215,355,215,320)
f.note('生成时通常固定模型参数；训练时才根据目标计算损失并更新参数。');f.save()

f=Figure('08-stages','预训练与几种后训练方法','数据形式不同，优化的行为也不同；这些方法可按需要组合。')
cards=[('预训练','文章、代码等文本','预测后续 token','blue'),('SFT','指令 + 优质回答','学习如何回应要求','teal'),('偏好优化','同题回答 A 优于 B','调整回答偏好','purple'),('可验证奖励','答案或测试的判分','提高可验证任务表现','orange')]
for i,(a,b,c,col) in enumerate(cards):
    x=45+i*285;f.box(x,175,255,230,a,b+'\n\n'+c,col)
f.note('SFT 提供示范，偏好数据提供比较，可验证奖励提供可由程序检查的反馈。');f.save()

f=Figure('09-kv-cache','KV Cache 复用前文的键和值','生成新 token 时，缓存减少旧位置的重复投影计算。')
f.text(50,153,'已处理的前文',25,'blue')
for i,w in enumerate(['我','喜欢','学习']):
    x=50+i*215;f.box(x,210,180,120,w,'已存 K、V','teal')
f.box(760,210,390,120,'新位置','计算新的 Q、K、V','purple')
f.arrow(680,270,745,270)
f.box(250,385,700,95,'新 Q 读取已有 K、V 和本位置 K、V','','blue')
f.arrow(950,340,850,380);f.arrow(350,340,450,380)
f.note('缓存减少重复计算，但仍占用显存；新位置的注意力还需要读取相关历史信息。');f.save()

f=Figure('10-memory','训练显存不只是模型权重','以下是组成示意，色块长度不表示真实比例。')
for i,(a,b,c) in enumerate([('模型权重','训练与生成都需要','blue'),('梯度','用于训练更新','teal'),('优化器状态','例如 Adam 的统计量','purple'),('中间激活','反向传播常需使用','orange')]):
    f.box(45+i*285,180,255,170,a,b,c)
f.rect(45,395,1110,78,fill='#e9effa',outline='#e9effa');f.text(70,418,'示例：10 亿参数 × 每个 2 字节 ≈ 2 GB，仅表示权重存储',25)
f.note('生成还可能需要 KV Cache 与临时空间；权重能放下，不代表所有配置都能运行。');f.save()

f=Figure('11-parallel','数据并行与模型拆分的区别','前者让同一个模型处理不同数据；后者把模型计算分给不同设备。',650)
f.text(50,145,'数据并行',27,'blue');f.text(650,145,'模型拆分示例',27,'purple')
f.box(50,205,230,135,'GPU 1','完整模型\n处理数据 A','blue');f.box(330,205,230,135,'GPU 2','完整模型\n处理数据 B','blue')
f.arrow(285,270,325,270);f.arrow(325,288,285,288)
f.text(100,380,'汇总梯度，再保持一致更新',24,'teal')
f.box(650,205,220,135,'GPU 1','模型前几层','purple');f.box(930,205,220,135,'GPU 2','模型后几层','purple');f.arrow(875,270,925,270)
f.text(660,380,'中间结果从一张卡传给另一张卡',22,'purple')
f.note('跨卡通信需要时间；增加 GPU 数量不一定能按比例缩短训练时间。');f.save()

f=Figure('12-moe','MoE 为每个 token 选择少数专家','以 4 选 2 为例：彩色路径参与本次计算，灰色专家本次未选中。',650)
f.box(45,270,185,115,'token 表示','','blue');f.box(295,270,205,115,'路由器','计算选择得分','purple');f.arrow(235,325,290,325)
for i in range(4):
    y=145+i*95;active=i in [0,2]
    f.box(650,y,200,76,f'专家 {i+1}','',color='teal' if active else 'blue')
    if not active:f.rect(652,y+2,196,72,fill='#e8ebf0',outline='#e8ebf0');f.text(670,y+21,f'专家 {i+1}',25,'muted')
    if active:f.arrow(505,325,640,y+38,'teal');f.arrow(855,y+38,970,325,'teal')
f.box(980,270,175,115,'汇总输出','','teal')
f.note('专家通常是子网络；少量激活不等于无需存储其他专家，也不等于没有通信开销。');f.save()

f=Figure('13-multimodal','图像特征怎样接入语言模型','一种常见视觉语言架构：视觉编码器 + 适配器 + 语言模型。')
for x,a,b,c in [(45,'图像','切块与特征提取','blue'),(335,'视觉编码器','图像 → 特征向量','teal'),(625,'适配器','转换表示形式','purple'),(915,'语言模型','结合图像和问题回答','orange')]:
    f.box(x,210,240,145,a,b,c)
    if x<915:f.arrow(x+245,282,x+283,282)
f.box(625,405,240,75,'文字问题','','blue');f.arrow(870,442,1035,363)
f.note('图像表示不一定是文本词表中的离散 token；不同模型也可能采用其他融合方式。');f.save()

print('Generated',len(list(ROOT.glob('*.png'))),'illustrations')
