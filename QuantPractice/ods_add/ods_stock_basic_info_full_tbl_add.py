import time
import random

import akshare as ak
import pandas as pd
import numpy as np
import sqlalchemy

"""
获取沪深上市公司基本情况
code,代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本(亿)
totals,总股本(亿)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
esp,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期
undp,未分利润
perundp, 每股未分配
rev,收入同比(%)
profit,利润同比(%)
gpr,毛利率(%)
npr,净利润率(%)
holders,股东人数

目前只能拿到
名称	类型	描述
A股代码	object	-
A股简称	object	-
A股上市日期	object	-
A股总股本	object	-
A股流通股本	object	-
所属行业	object	-
"""

def addShenzhen(pdate):
    # 深证的
    shenzhen_df = ak.stock_info_sz_name_code(symbol="A股列表")
    shenzhen_df.columns = ["board", "code", "name", "ipo_time", "sum_share", "fluent_share", "industry"]
    shenzhen_df["fluent_share"] = shenzhen_df["fluent_share"].apply(lambda x: x.replace(",", '')).astype(float)
    shenzhen_df["sum_share"] = shenzhen_df["sum_share"].apply(lambda x: x.replace(",", '')).astype(float)
    shenzhen_df["sum_share"] = shenzhen_df["sum_share"] / 100000000
    shenzhen_df["fluent_share"] = shenzhen_df["fluent_share"] / 100000000

    shenzhen_df["industry"] = shenzhen_df["industry"].apply(lambda x: x[2:])
    shenzhen_df["city"] = ["深圳" for i in range(len(shenzhen_df))]

    shenzhen_add = shenzhen_df[shenzhen_df["ipo_time"]>pdate]
    return shenzhen_add

def addShanghai(pdate):
    # 上证的,主板和科创板分开
    shanghai_main_df = ak.stock_info_sh_name_code(symbol="主板A股")
    shanghai_kc_df = ak.stock_info_sh_name_code(symbol="科创板")
    shanghai_main_df["板块"] = ["主板" for i in range(len(shanghai_main_df))]
    shanghai_kc_df["板块"] = ["科创板" for i in range(len(shanghai_kc_df))]

    # 拼接
    shanghai_df = pd.concat([shanghai_main_df, shanghai_kc_df], axis=0)

    shanghai_df.columns = ["code", "name", "full_name", "ipo_time", "board"]
    shanghai_df["city"] = ["上海" for i in range(len(shanghai_df))]

    # 上证的总股本,行业,需要通过东方财富的接口拿;历史的不用了,需要获取新的
    shanghai_add = shanghai_df[shanghai_df["ipo_time"]>pdate]

    shanghai_stocks = list(shanghai_add["code"])
    shanghai_sum_share = []
    shanghai_fluent_share = []
    shanghai_industry = []
    for stock in shanghai_stocks:
        sleeptime=random.randint(1, 100)
        time.sleep(sleeptime/1000)
        temp = ak.stock_individual_info_em(symbol=stock)
        shanghai_industry.append(temp["value"][2])
        shanghai_sum_share.append(temp["value"][6])
        shanghai_fluent_share.append(temp["value"][7])

    # 拿到之后拼接处理
    shanghai_add["industry"] = shanghai_industry
    shanghai_add["sum_share"] = shanghai_sum_share
    shanghai_add["fluent_share"] = shanghai_fluent_share
    shanghai_add["sum_share"] = shanghai_add["sum_share"] / 100000000
    shanghai_add["fluent_share"] = shanghai_add["fluent_share"] / 100000000

    shanghai_add_res = shanghai_add[["board", "code", "name", "ipo_time", "sum_share", "fluent_share", "industry", "city"]]
    return shanghai_add_res

def connect_db(db):
    engine = sqlalchemy.create_engine('mysql+pymysql://root:sun123456@localhost:3306/{}?charset=utf8'.format(db))
    return engine

def mergeDf(shenzhen_df, shanghai_df):
    df = pd.concat([shenzhen_df, shanghai_df], axis=0)
    df = df[["code", "name", "ipo_time", "sum_share", "fluent_share", "industry", "city", "board"]]
    return df

if __name__ == '__main__':

    # 需要初始化pdate;这个应该从mysql里面查询
    pdate="2024-02-20"
    shenzhen_df = addShenzhen(pdate)
    print(shenzhen_df.info())
    shanghai_df = addShanghai(pdate)
    print(shanghai_df.info())
    df = mergeDf(shenzhen_df, shanghai_df)

    # 初始化
    engine = connect_db("ods")

    # df.to_csv("E:\Learning\Git\myPython\QuantPractice\ods\ods_stock_basic_info_full_tbl_add.csv", index=False) # index 是为了去掉索引
    df.to_sql('ods_stock_trade_his_full_tbl', con=engine, if_exists='append', index=False)