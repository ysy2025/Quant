import os
import time
import random

import akshare as ak
import pandas as pd
import numpy as np
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

def getShenzhen():
    # 深证的
    shenzhen_df = ak.stock_info_sz_name_code("A股列表")
    shenzhen_df.columns = ["board", "code", "name", "ipo_time", "sum_share", "fluent_share", "industry"]
    shenzhen_df["fluent_share"] = shenzhen_df["fluent_share"].apply(lambda x: x.replace(",", '')).astype(float)
    shenzhen_df["sum_share"] = shenzhen_df["sum_share"].apply(lambda x: x.replace(",", '')).astype(float)
    shenzhen_df["sum_share"] = shenzhen_df["sum_share"] / 100000000
    shenzhen_df["fluent_share"] = shenzhen_df["fluent_share"] / 100000000

    shenzhen_df["industry"] = shenzhen_df["industry"].apply(lambda x: x[2:])
    shenzhen_df["city"] = ["深圳" for i in range(len(shenzhen_df))]
    return shenzhen_df

def getShanghai():
    # 上证的,主板和科创板分开
    shanghai_main_df = ak.stock_info_sh_name_code("主板A股")
    shanghai_kc_df = ak.stock_info_sh_name_code("科创板")
    shanghai_main_df["板块"] = ["主板" for i in range(len(shanghai_main_df))]
    shanghai_kc_df["板块"] = ["科创板" for i in range(len(shanghai_kc_df))]

    # 拼接
    shanghai_df = pd.concat([shanghai_main_df, shanghai_kc_df], axis=0)

    shanghai_df.columns = ["code", "name", "full_name", "ipo_time", "board"]
    shanghai_df["city"] = ["上海" for i in range(len(shanghai_df))]
    shanghai_df["ipo_time"] = shanghai_df["ipo_time"].astype(str)

    # 上证的总股本,行业,需要通过东方财富的接口拿
    shanghai_stocks = list(shanghai_df["code"])
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
    shanghai_df["industry"] = shanghai_industry
    shanghai_df["sum_share"] = shanghai_sum_share
    shanghai_df["fluent_share"] = shanghai_fluent_share
    shanghai_df["sum_share"] = shanghai_df["sum_share"] / 100000000
    shanghai_df["fluent_share"] = shanghai_df["fluent_share"] / 100000000

    shanghai_df_res = shanghai_df[["board", "code", "name", "ipo_time", "sum_share", "fluent_share", "industry", "city"]]
    return shanghai_df_res

def mergeDf(shenzhen_df, shanghai_df):
    df = pd.concat([shenzhen_df, shanghai_df], axis=0)
    df = df[["code", "name", "ipo_time", "sum_share", "fluent_share", "industry", "city", "board"]]
    return df

if __name__ == '__main__':
    shenzhen_df = getShenzhen()
    print(shenzhen_df.info())
    shanghai_df = getShanghai()
    print(shanghai_df.info())
    df = mergeDf(shenzhen_df, shanghai_df)

    path = os.getcwd()
    file = path + "\ods_stock_basic_info_full_tbl_init.csv"
    df.to_csv(file, index=False, mode='a') # index 是为了去掉索引;append是追加模式