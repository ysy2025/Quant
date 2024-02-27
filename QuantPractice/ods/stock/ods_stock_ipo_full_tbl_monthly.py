import os

import akshare as ak
import requests
import pandas as pd
import numpy as np

def getIPO(code):
    url = "https://basic.10jqka.com.cn/new/{0}/company.html".format(code)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.90 Safari/537.36",
    }
    r = requests.get(url, headers=headers)
    r.encoding = "gbk"
    temp_df = pd.read_html(r.text)
    return temp_df

def getOtherIPO(code):
    url = "https://basic.10jqka.com.cn/new/{0}/bonus.html".format(code)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.90 Safari/537.36",
    }
    r = requests.get(url, headers=headers)
    r.encoding = "gbk"
    temp_df = pd.read_html(r.text)
    return temp_df

if __name__ == '__main__':
    # 融资数据不太准确,但是先用吧.先凑合用.
    df = ak.stock_history_dividend()
    df.columns = ["code", "name", "ipo_time", "sum_dividend", "avg_dividend", "dividend_times", "ipo_amount", "ipo_times"]

    df = df[["code", "name", "ipo_time","ipo_amount", "ipo_times"]]
    df.head()

    path = os.getcwd()
    file = path + "\oods_stock_ipo_full_tbl_monthly.csv"

    df.to_csv(file,index=False)  # index 是为了去掉索引

