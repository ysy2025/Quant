import random
import time

import akshare as ak
import pandas as pd
import sqlalchemy
import sys

sys.path.append("E:\\MyGitHub\\myPython\\QuantPractice\\tools")
from tools import itemGetter

def addShenzhen(pdate):
    # 深证的列表
    shenzhen_df = ak.stock_info_sz_name_code("A股列表")
    shenzhen_df = shenzhen_df[['板块', 'A股代码', 'A股简称', 'A股上市日期', 'A股总股本', 'A股流通股本', '所属行业']]
    #对列进行处理
    shenzhen_df.columns = ["board", "code", "name", "ipo_time", "sum_share", "fluent_share", "industry"]
    shenzhen_df["fluent_share"] = shenzhen_df["fluent_share"].apply(lambda x: x.replace(",", '')).astype(float)
    shenzhen_df["sum_share"] = shenzhen_df["sum_share"].apply(lambda x: x.replace(",", '')).astype(float)
    shenzhen_df["sum_share"] = shenzhen_df["sum_share"] / 100000000
    shenzhen_df["fluent_share"] = shenzhen_df["fluent_share"] / 100000000
    shenzhen_df["industry"] = shenzhen_df["industry"].apply(lambda x: x[2:])
    shenzhen_df["city"] = ["深圳" for i in range(len(shenzhen_df))]
    #过滤
    shenzhen_add = shenzhen_df[shenzhen_df["ipo_time"]>pdate]
    return shenzhen_add

def addShanghai(pdate):
    # 上证的,主板和科创板分开
    shanghai_main_df = ak.stock_info_sh_name_code("主板A股")
    shanghai_kc_df = ak.stock_info_sh_name_code("科创板")
    shanghai_main_df["板块"] = ["主板" for i in range(len(shanghai_main_df))]
    shanghai_kc_df["板块"] = ["科创板" for i in range(len(shanghai_kc_df))]
    # 拼接
    shanghai_df = pd.concat([shanghai_main_df, shanghai_kc_df], axis=0)
    # 处理列
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
    # 重新排列
    shanghai_add_res = shanghai_add[["board", "code", "name", "ipo_time", "sum_share", "fluent_share", "industry", "city"]]
    return shanghai_add_res

def connect_db(host, name, pwd, db):
    engine = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}:3306/{3}?charset=utf8'.format(name, pwd, host, db))
    return engine

def mergeDf(shenzhen_df, shanghai_df):
    df = pd.concat([shenzhen_df, shanghai_df], axis=0)
    df = df[["code", "name", "ipo_time", "sum_share", "fluent_share", "industry", "city", "board"]]
    return df

if __name__ == '__main__':

    # 需要初始化pdate;这个应该从mysql里面查询
    dateGetter = itemGetter.dateGetter("root", "Alicloud123456!", "39.101.76.35")
    table = "ods_stock_basic_info_full_tbl"
    column = "ipo_time"
    pdate= dateGetter.latest(table, column)

    # 然后传入pdate,找到ipo大于pdate的code,拿到
    shenzhen_df = addShenzhen(pdate)

    shanghai_df = addShanghai(pdate)

    df = mergeDf(shenzhen_df, shanghai_df)

    # 初始化engine
    engine = connect_db("root", "sun123456", "localhost", "ods")

    # 写入mysql中
    df.to_sql('ods_stock_basic_info_full_tbl', con=engine, if_exists='append', index=False)