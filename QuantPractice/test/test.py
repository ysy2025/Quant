import random
import time

import akshare as ak
import pandas as pd

import os

import sqlalchemy

from tools import DBHelper


def getValuationHis(code)->pd.DataFrame:
    """
    拿到历史估值数据
    :param code: 代码
    :return: 一个dataframe

    columns 已经标准化为英语了
    ["trade_date","pe","pe_ttm","pb","ps","ps_ttm","dv_ratio","dv_ttm","total_mv"]
    """
    try:
        # columns 已经标准化为英语了 不用重置了
        # 增加一列
        df = ak.stock_a_indicator_lg(symbol=code)
        df["code"] = [code for i in range(len(df))]

        df.columns = ['pdate', 'pe', 'pe_ttm', 'pb', 'ps', 'ps_ttm', 'dv_ratio', 'dv_ttm', 'total_mv', 'code']

        df = df[['code', 'pdate', 'pe', 'pe_ttm', 'pb', 'ps', 'ps_ttm', 'dv_ratio', 'dv_ttm', 'total_mv']]

        return df
    except:
        return pd.DataFrame()

def connect_db(db):
    engine = sqlalchemy.create_engine('mysql+pymysql://root:sun123456@localhost:3306/{}?charset=utf8'.format(db))
    return engine


if __name__ == '__main__':
    # 读取基础数据;从数据库中读取
    engine = connect_db("ods")
    codes_df = pd.read_sql("select code from ods_stock_basic_info_full_tbl", engine)
    codes = codes_df["code"].to_list()
    # 初始化一个空df
    business = pd.DataFrame()

    # 初始化一个空df
    valuation_his = pd.DataFrame()

    # 初始化engine
    engine = connect_db("ods")

    k = 0
    a = codes[:500]
    b = codes[500:1000]
    c = codes[1000:1500]
    d = codes[1500:2000]
    e = codes[2000:2500]
    f = codes[2500:3000]
    g = codes[3000:3500]
    h = codes[3500:4000]
    i = codes[4000:4500]
    j = codes[4500:]

    for code in a:
        print("======> code is {0}".format(code))
        sleeptime = random.randint(1, 10)
        time.sleep(sleeptime / 1000)
        k += 1
        temp = getValuationHis(code)
        valuation_his = pd.concat([valuation_his, temp], axis=0)
    valuation_his.to_sql('ods_stock_valuation_his_full_tbl', con=engine, if_exists='append', index=False)
    valuation_his=pd.DataFrame()

    # 更新索引
    dbhelper = DBHelper.DBHelper("ods")
    drop_index = "alter table ods_stock_valuation_his_full_tbl drop index value_code;"
    add_index = "alter table ods_stock_valuation_his_full_tbl add index value_code (code) ;"

    dbhelper.exec(drop_index)
    dbhelper.exec(add_index)