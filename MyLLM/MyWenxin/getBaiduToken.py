import requests
import json

def main():
    # client id = API Key, client_secret = Secret Key 修改成自己的API Key 和Sercet Key
    client_id = "PykYEOa4Mtc1hSqxQQAZVDKl"
    client_secret = "iDibot290FyTOlFnGkshcreE57gatRRs"
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}&client_secret={1}".format(client_id, client_secret)

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    main()

# 会再终端打印一行文本即acess token