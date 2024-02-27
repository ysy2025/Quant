import os
import random
import time

import akshare as ak

import numpy as np
import pandas as pd
import sqlalchemy


def getBusiness(code)->pd.DataFrame:
    df = ak.stock_zyjs_ths(symbol=code)
    # columns 重命名
    df.columns = ["code", "main_business", "product_type", "product", "business_area"]
    return df

def connect_db(host, name, pwd, db):
    engine = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}:3306/{3}?charset=utf8'.format(name, pwd, host, db))
    return engine

if __name__ == '__main__':
    """
    接口: stock_zyjs_ths
    目标地址: http://basic.10jqka.com.cn/new/000066/operate.html
    描述: 同花顺-主营介绍
    限量: 单次返回所有数据
    """
    # 读取基础数据;从数据库中读取
    engine = connect_db("root", "sun123456", "localhost", "ods")
    codes_df = pd.read_sql("select code from ods_stock_basic_info_full_tbl", engine)
    codes = codes_df["code"].to_list()
    # 初始化一个空df
    business = pd.DataFrame()

    k = 0
    for code in codes:
        print("======> code is {0}".format(code))
        sleeptime = random.randint(1, 10)
        time.sleep(sleeptime / 1000)
        k += 1
        temp = getBusiness(code)
        business = pd.concat([business, temp], axis=0)
        # 每过500个就保存一下
        if k % 500 == 0:
            sleeptime = random.randint(1, 10)
            time.sleep(sleeptime)
            # 保存数据
            business.to_sql('ods_stock_business_full_tbl', con=engine, if_exists='append', index=False)
            business=pd.DataFrame()

    # 最后剩下的再存一下
    business.to_sql('ods_stock_business_full_tbl', con=engine, if_exists='append', index=False)
