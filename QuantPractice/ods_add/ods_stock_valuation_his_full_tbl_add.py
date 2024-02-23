import datetime
import random
import time

import akshare as ak
import pandas as pd

import os

import sqlalchemy

from tools import DBHelper, itemGetter


def getValuationHis(code, pdate)->pd.DataFrame:
    """
    拿到历史估值数据,提取增量数据
    :param code: 代码
    :param pdate: 日期
    :return: 一个dataframe

    columns 已经标准化为英语了
    ["trade_date","pe","pe_ttm","pb","ps","ps_ttm","dv_ratio","dv_ttm","total_mv"]
    """
    df = ak.stock_a_indicator_lg(symbol=code)
    # columns 已经标准化为英语了
    # 增加一列
    df["code"] = [code for i in range(len(df))]
    df.columns = ['pdate', 'pe', 'pe_ttm', 'pb', 'ps', 'ps_ttm', 'dv_ratio', 'dv_ttm', 'total_mv', 'code']
    df = df[['code', 'pdate', 'pe', 'pe_ttm', 'pb', 'ps', 'ps_ttm', 'dv_ratio', 'dv_ttm', 'total_mv']]

    # 针对时间进行处理
    year, month, day = pdate[:4], pdate[5:7], pdate[8:]
    pdatetime = datetime.date(year, month, day)

    # 提取增量
    return df[df['trade_date']>pdatetime]

def connect_db(db):
    engine = sqlalchemy.create_engine('mysql+pymysql://root:sun123456@localhost:3306/{}?charset=utf8'.format(db))
    return engine


if __name__ == '__main__':
    
    # 需要拿到code列表
    codeGetter = itemGetter.codeGetter()
    codes = codeGetter.codes()

    # 需要初始化pdate;这个应该从mysql里面查询;用贵州茅台做索引,去查
    dateGetter = itemGetter.dateGetter()
    table = "ods_stock_valuation_his_full_tbl"
    column = "pdate"
    pdate= dateGetter.latest_of_trade(table, column)

    # 初始化一个空df
    valuation_his = pd.DataFrame()

    # 初始化engine
    engine = connect_db("ods")

    k = 0
    for code in codes:
        print("======> code is {0}".format(code))
        sleeptime = random.randint(1, 10)
        time.sleep(sleeptime / 1000)
        k += 1
        temp = getValuationHis(code, pdate)
        valuation_his = pd.concat([valuation_his, temp], axis=0)
        # 每过500个就保存一下
        if k % 500 == 0:
            sleeptime = random.randint(1, 10)
            time.sleep(sleeptime)
            # 保存数据
            valuation_his.to_sql('ods_stock_valuation_his_full_tbl', con=engine, if_exists='append', index=False)
            valuation_his=pd.DataFrame()

    # 最后剩下的再存一下
    valuation_his.to_sql('ods_stock_valuation_his_full_tbl', con=engine, if_exists='append', index=False)

    # 更新索引
    dbhelper = DBHelper.DBHelper("ods")
    drop_index = "alter table ods_stock_valuation_his_full_tbl drop index stock_code;"
    add_index = "alter table ods_stock_valuation_his_full_tbl add index stock_code (code) ;"

    dbhelper.exec(drop_index)
    dbhelper.exec(add_index)