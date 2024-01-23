"""
作者：池塘春草梦
链接：https://www.zhihu.com/question/627706463/answer/3358597163
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
"""
@author: HeroZhang（池塘春草梦）
@contact:herozhang101@gmail.com
@version: 1.0.0
@file: law_ques.py
@time: 2024/1/11 16:25
@description: 调用文心一言api,实现批量回答问题
"""

import json

# import pandas as pd
import requests
from tqdm import tqdm

filename = "一列问题.CSV"
# 格式：一列问题
filepath = "E:\MyGitHub\myPython"

API_KEY = "PykYEOa4Mtc1hSqxQQAZVDKl"
SECRET_KEY = "iDibot290FyTOlFnGkshcreE57gatRRs"

def ask_Q(question):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response
    # print(response.text)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


# questions = pd.read_csv(filepath + filename, encoding="gbk", header=None, names=['questions'])
question = "请给出美国历年GDP，以美元为单位"

Input = question + '并给出具体的法律条文'
ans = ask_Q(Input)
ans = json.loads(ans.text)

print(ans)