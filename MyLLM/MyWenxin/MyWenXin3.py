import requests
import json

AK = "PykYEOa4Mtc1hSqxQQAZVDKl"
SK = "iDibot290FyTOlFnGkshcreE57gatRRs"

def get_access_token():
    """
    使用ak sk鉴权,得到签名
    :return: access_token
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": AK, "client_secret": SK}
    return str(requests.post(url, params=params).json().get("access_token"))
def main():
    # 首先鉴权
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()

    # 循环
    while(1):
        s=input()
        # 注意message必须是奇数条
        payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": s
            }
        ]
        })
        headers = {
            'Content-Type': 'application/json'
        }

        res = requests.request("POST", url, headers=headers, data=payload).json()
        print(res['result'])

if __name__ == '__main__':
    # res = get_access_token()
    # print(res)

    main()
    """
    会报,超过每日访问次数限制了
    """