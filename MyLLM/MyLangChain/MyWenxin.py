"""
作者：求索
链接：https://www.zhihu.com/question/627706463/answer/3263554079
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

https://zhuanlan.zhihu.com/p/648605546

https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
"""
from langchain.chat_models import ErnieBotChat
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import requests
from bs4 import BeautifulSoup
import os

headers = {'User-Agent': 'Mozilla/5.0'}


url = "https://zhuanlan.zhihu.com/p/657336303"

response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code != 200:
    print(f"Failed to get URL. Status code: {response.status_code}")
    exit(0)

# 解析HTML内容
soup = BeautifulSoup(response.text, 'html.parser')


# ernie_client_id = os.getenv('BAIDU_API_KEY')
#
# ernie_client_secret = os.getenv('BAIDU_CLIENT_SECRET')

ernie_client_id = "PykYEOa4Mtc1hSqxQQAZVDKl"
ernie_client_secret = "iDibot290FyTOlFnGkshcreE57gatRRs"
model_name = 'ERNIE-Bot-4'

template = """

你是文学大师卡尔维诺，按照你的风格对用户输入的内容进行总结：

用户输入：
{input}

"""

llm_model = ErnieBotChat(ernie_client_id = ernie_client_id, ernie_client_secret = ernie_client_secret, model_name = model_name, temperature =0.01 )

prompt_template = PromptTemplate(input_variables=['input'],template=template)

llmchain = LLMChain(llm=llm_model, prompt= prompt_template)

response = llmchain.run(soup.text)

print(response)