import random
import time

import akshare as ak

import numpy as np
import pandas as pd

def getTradeHis(code)->pd.DataFrame:
    df = ak.stock_zh_a_hist(symbol=code, period="daily", start_date="19700101", end_date='20500101',
                                            adjust="qfq")
    # columns 重命名
    df.columns = ["pdate", "open", "close", "highest", "lowest", "volume", "amount",
                  "vibration", "updown", "updown_yuan", "turnover"]
    # 增加一列
    df["code"] = [code for i in range(len(df))]
    # 重置df
    df = df[["code", "pdate", "open", "close", "highest", "lowest", "volume", "amount", "vibration", "updown",
                 "updown_yuan"]]

    return df

if __name__ == '__main__':
    """
    前复权价格
    历史交易数据

    a = {
        "code":["600519"],
        "dividend":[111],
        "dividend_times":[3]
    }
    b = pd.DataFrame(a)
    形成如上数据结构
    """
    df = pd.read_csv("E:\MyGitHub\myPython\QuantPractice\ods\ods_stock_basic_info_full_tbl_init.csv",
                     dtype={'code': str})
    codes = df['code'].to_list()

    trade_his = getTradeHis(codes[0])
    # print("======> code is {0}".format(codes[0]))
    # print("length of his is {0}".format(len(trade_his)))
    k = 0
    for code in codes[1:]:
        print("======> code is {0}".format(code))
        sleeptime = random.randint(1, 10)
        time.sleep(sleeptime / 1000)
        k += 1
        if k % 500 == 0:
            # print("======> code is {0}".format(code))
            sleeptime = random.randint(1, 10)
            time.sleep(sleeptime)
        temp = getTradeHis(code)
        # print("length of temp is {0}".format(len(temp)))
        trade_his = pd.concat([trade_his, temp], axis=0)
        # print("length of his is {0}".format(len(trade_his)))
    print(len(trade_his))