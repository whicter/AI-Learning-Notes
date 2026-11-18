# RAG学习记录（Langchain+文心一言）

> 来源（Source）：https://blog.csdn.net/qq_32623209/article/details/149018027  
> 日期：04-23

1.无法加载藜麦txt

报错缺 langchain -community

安装即可

2.如果是直接用OS包里面的加载txt会不会有什么不同呢

没有

3.如何获取对应网页内容

[【浅学】RAG检索增强生成（Retrieval Augmented Generation）案例实践-CSDN博客](https://blog.csdn.net/qq_44894943/article/details/137025290?spm=1001.2014.3001.5502)

中的下面代码

```python
import requests
from bs4 import BeautifulSoup

url = "https://baike.baidu.com/item/%E8%97%9C%E9%BA%A6/5843874"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 获取词条名称
title = soup.find("div", class_="lemmaTitleBox_tfjaT").find("h1").text

summary_list = soup.find('div', class_='lemmaSummary_pGhoA J-summary').find_all('div',class_='para_guwWB summary_SdukW MARK_MODULE')

print('词条：'+ title)
print('简介：')

with open("./藜.txt","w") as file:    ##打开读写文件，逐行将列表读入文件内
    for summary in summary_list:
        file.write(summary.text+"\n")
        print(summary.text)  
```

使用其中代码

关于百科会修改那个变量名字，只需要打开下载的soup，看这几个部分进行对应修改即可

词条名称：检索lemmaTitleBox_

简介内容：分别检索lemmaSummary_          para_

如果觉着这样处理太短了，下面是整个soup的处理模块

```python
# 创建列表存储提取结果
extracted_content = []

# 提取所有标题和段落
for element in soup.find_all(['div', 'h2', 'h3']):
    # 处理一级标题
    if element.name == 'div' and 'level-1' in element.get('class', []):
        h2_tag = element.find('h2')
        if h2_tag:
            extracted_content.append(f"\n【标题】{h2_tag.get_text(strip=True)}")

    # 处理二级标题
    elif element.name == 'div' and 'level-2' in element.get('class', []):
        h3_tag = element.find('h3')
        if h3_tag:
            extracted_content.append(f"\n【小标题】{h3_tag.get_text(strip=True)}")

    # 处理正文段落
    elif element.name == 'div' and 'para_e7uVn' in element.get('class', []):
        # 提取所有文本内容，忽略引用标记[数字]
        text_spans = element.find_all('span', class_='text_jc0vX')
        if text_spans:
            paragraph = ''.join(span.get_text(strip=True) for span in text_spans)
            extracted_content.append(paragraph)

# 写入TXT文件
with open('./藜麦.txt', 'w', encoding='utf-8') as f:
    for item in extracted_content:
        f.write(item + '\n')

print("内容已成功提取到藜麦.txt文件")
```

4.text_splitter.split_documents(documents)拆分块不对，chunk长度过长

文本可能存在格式上的问题。这时候就不要调用

```undefined
CharacterTextSplitter
```

而是应该调用

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 方案1：增大chunk_size（推荐）
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,  # 根据嵌入模型调整（如text-embedding-ada-002支持8191）
    chunk_overlap=50,
    separators=["\n\n", "\n", "。", "！", "？", " ", ""]  # 优化分隔符
)
```

可以循环进行分割，这样通过调节就不会超长。

5.连不上huggingface，报错We couldn‘t connect to 'https://huggingface.co'

代码里面加：

```python
import os
# huggingface 镜像地址
os.environ['HF_ENDPOINT'] = "https://hf-mirror.com"
```

进入镜像网站

如果无效，可以手动下载模型，下面是教程

[【错误记录】本地部署大模型 从 Hugging Face 的模型库下载模型报错 ( OSError: We couldn‘t connect to ‘https://huggingface.co‘ )_no sentence-transformers model found with name-CSDN博客](https://blog.csdn.net/shulianghan/article/details/146018551)

6.报错ImportError: cannot import name 'configure_hf' from 'huggingface_hub'

解决方案：[【错误记录】Hugging Face 模型库下载模型报错 ( huggingface_hub 函数库使用 configure_hf 函数 报错 | 更新到最新版本 | 使用旧版本兼容方法设置镜像源 )_importerror: huggingface-hub>=0.30.0,<1.0 is requi-CSDN博客](https://blog.csdn.net/shulianghan/article/details/146025627)

都解决不了的话，走魔塔社区

```python
import torch
from modelscope import snapshot_download, AutoModel, AutoTokenizer
import os
model_dir = snapshot_download('AI-ModelScope/m3e-base', 
cache_dir='/root/autodl-tmp', revision='master')
```

下载之后对应修改代码，**主要是model_name这里**

```python
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import Chroma
import os

# 使用本地模型路径
model_path = "/root/autodl-tmp/AI-ModelScope/m3e-base"

# 确保模型路径存在
if not os.path.exists(model_path):
    raise FileNotFoundError(f"模型路径不存在: {model_path}")

# 配置embedding模型参数
model_kwargs = {'device': 'cpu'}  # 使用CPU
encode_kwargs = {'normalize_embeddings': True}  # 标准化嵌入向量

# 创建embedding模型实例
embedding = HuggingFaceBgeEmbeddings(
    model_name=model_path,  # 使用本地路径而非HuggingFace ID
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs,
    query_instruction="为文本生成向量表示用于文本检索"  # M3E模型不需要特定指令，但保留不影响
)
```

7.报错pydantic

这个是库升级了所以没有匹配的了，查看 文心一言  的新代码，原来只支持那个复杂的AKSK认证，现在接口保持和openai那一套一样了，下面是例子

```python
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek-v3", # 使用千帆modelbuilder上的deepseek-v3
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="",  # 你的api-key，在这里创建：https://console.bce.baidu.com/iam/#/iam/apikey/list
    base_url="https://qianfan.baidubce.com/v2/", # 千帆modelbuilder 的base_url
    # organization="...",
    # other params...
)
retriever = db.as_retriever()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
qa = ConversationalRetrievalChain.from_llm(llm, retriever, memory=memory)
qa({"question": "藜怎么防治虫害？"})
```

目前没有遇到别的错误了，如果报错缺包就安装包，remote不了的就安装本地吧
