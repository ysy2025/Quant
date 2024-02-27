import random
import time

import akshare as ak

import numpy as np
import pandas as pd
import sqlalchemy
from tools import itemGetter
from tools import DBHelper


def getTradeHis(code, start_date)->pd.DataFrame:
    # start_date 不包含在内的
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

def connect_db(host, name, pwd, db):
    engine = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}:3306/{3}?charset=utf8'.format(name, pwd, host, db))
    return engine

if __name__ == '__main__':

    # 需要拿到code列表
    codeGetter = itemGetter.codeGetter()
    codes = codeGetter.codes()

    # 需要初始化pdate;这个应该从mysql里面查询;用贵州茅台做索引,去查
    dateGetter = itemGetter.dateGetter()
    table = "ods_stock_trade_his_full_tbl"
    column = "pdate"
    pdate= dateGetter.latest_of_trade(table, column)

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
        temp = getTradeHis(code, pdate)
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

    # 更新索引
    dbhelper = DBHelper.DBHelper('127.0.0.1', "root", "sun123456", "ods")
    drop_index = "alter table ods_stock_trade_his_full_tbl drop index stock_code;"
    add_index = "alter table ods_stock_trade_his_full_tbl add index stock_code (code) ;"

    dbhelper.exec(drop_index)
    dbhelper.exec(add_index)
