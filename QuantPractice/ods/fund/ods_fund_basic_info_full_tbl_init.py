import random
import time
import akshare as ak
import pandas as pd
import os
import sqlalchemy
from tools import DBHelper

def connect_db(db):
    engine = sqlalchemy.create_engine('mysql+pymysql://root:sun123456@localhost:3306/{}?charset=utf8'.format(db))
    return engine

if __name__ == '__main__':
    # 初始化引擎
    engine = connect_db("ods")

    df = ak.fund_name_em()
    df.columns = ["code", "abbr_name", "name", "type", "full_name"]

    df = df[['code']]
    # 保存
    df.to_sql('ods_fund_basic_info_full_tbl', con=engine, if_exists='append', index=False)
