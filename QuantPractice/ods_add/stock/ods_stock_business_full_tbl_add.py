#coding=utf-8
import datetime
import os, sys
import random
import time

import akshare as ak

import numpy as np
import pandas as pd
import sqlalchemy
sys.path.append("E:\\MyGitHub\\myPython\\QuantPractice\\tools")
sys.path.append("/code")
from tools import itemGetter, DBHelper


def getBusiness(code):
    df = ak.stock_zyjs_ths(symbol=code)
    # columns 重命名
    df.columns = ["code", "main_business", "product_type", "product", "business_area"]
    return df

if __name__ == '__main__':
    """
    接口: stock_zyjs_ths
    目标地址: http://basic.10jqka.com.cn/new/000066/operate.html
    描述: 同花顺-主营介绍
    限量: 单次返回所有数据
    """
    # 读取基础数据;从数据库中读取;直接查询增量即可;由于basic_info更新在前,因此需要拿到最新更新的
    # 读取基础数据;从数据库中读取;直接查询增量即可
    if datetime.datetime.now().weekday() > 4:
        print("-" * 32 + "> 周末啦,不开工!")
    else:
        engine = itemGetter.conGetter.connect_db("root", "Alicloud123456!", "localhost", "ods")

        sql = """
        select code from ods_stock_basic_info_full_tbl
        where ipo_time in(
        select max(ipo_time)from ods_stock_basic_info_full_tbl
        )
        """
        codes_df = pd.read_sql(sql, engine)
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

        # 首先删除已有的,确保重跑没问题
        dbhelper = DBHelper.DBHelper('localhost', "root", "Alicloud123456!", "ods")
        for each in codes:
            print("=" * 32 + "> 需要删除的code = {0}\n".format(each))
            drop_bigger = "delete from ods_stock_business_full_tbl where code = '{0}'".format(each)
            dbhelper.exec(drop_bigger)

        # 最后剩下的再存一下
        business.to_sql('ods_stock_business_full_tbl', con=engine, if_exists='append', index=False)
        print("=" * 32 + "> 更新结束!\n")