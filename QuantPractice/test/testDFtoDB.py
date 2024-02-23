import akshare as ak
import pandas as pd
import numpy as np
import pymysql
import sqlalchemy


def connect_db(db):
    engine = sqlalchemy.create_engine('mysql+pymysql://root:sun123456@localhost:3306/{}?charset=utf8'.format(db))
    return engine

if __name__ == '__main__':
    df = pd.read_csv("E:\MyGitHub\myPython\QuantPractice\ods\ods_stock_basic_info_full_tbl_init.csv",
                     dtype={'code': str})

    engine = connect_db("ods")

    # 将 DataFrame 写入 MySQL 表格
    df.to_sql('ods_stock_basic_info_full_tbl', con=engine, if_exists='append', index=False)


    # pd.read_sql("show tables", engine)
