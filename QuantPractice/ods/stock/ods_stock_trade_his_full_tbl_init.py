import os
import random
import time

import akshare as ak

import numpy as np
import pandas as pd
import sqlalchemy

from tools import itemGetter


def getTradeHis(code)->pd.DataFrame:
    df = ak.stock_zh_a_hist(symbol=code, period="daily", start_date="19700101", end_date='20500101',
                                            adjust="qfq")
    # columns 重命名
    df.columns = ["date", "open", "close", "highest", "lowest", "volume", "amount",
                  "vibration", "updown", "updown_yuan", "turnover"]
    # 增加一列
    df["code"] = [code for i in range(len(df))]
    # 重置df
    df = df[["code", "date", "open", "close", "highest", "lowest", "volume", "amount", "vibration", "updown",
                 "updown_yuan"]]

    return df

def connect_db(host, name, pwd, db):
    engine = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}:3306/{3}?charset=utf8'.format(name, pwd, host, db))
    return engine

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
    # 读取基础数据
    codeGetter = itemGetter.codeGetter("root", "Alicloud123456!", "39.101.76.35")
    codes = codeGetter.codes()

    # 初始化一个空df
    trade_his = pd.DataFrame()

    # 初始化engine
    engine = connect_db("root", "sun123456", "localhost", "ods")

    k = 0
    for code in codes:
        print("======> code is {0}".format(code))
        sleeptime = random.randint(1, 10)
        time.sleep(sleeptime / 1000)
        k += 1
        temp = getTradeHis(code)
        trade_his = pd.concat([trade_his, temp], axis=0)
        # 每过500个就保存一下
        if k % 500 == 0:
            sleeptime = random.randint(1, 10)
            time.sleep(sleeptime)
            # 保存数据
            trade_his.to_sql('ods_stock_trade_his_full_tbl', con=engine, if_exists='append', index=False)
            trade_his=pd.DataFrame()

    # 最后剩下的再存一下
    trade_his.to_sql('ods_stock_trade_his_full_tbl', con=engine, if_exists='append', index=False)
