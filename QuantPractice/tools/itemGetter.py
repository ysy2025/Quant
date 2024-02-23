import time
import random

import akshare as ak
import pandas as pd
import numpy as np

import sqlalchemy


class dateGetter:
    """
    用来获取指定日期
    """

    def __init__(self, db="ods"):
        self.db = db
        self.engine = sqlalchemy.create_engine(
            'mysql+pymysql://root:sun123456@localhost:3306/{}?charset=utf8'.format(self.db))

    def latest(self, table, column):
        sql = "select max({1}) as a from {0}".format(table, column)

        res = pd.read_sql(sql, self.engine)

        return res['a'][0]

    def earliest(self, table, column):
        sql = "select min({1}) as a from {0}".format(table, column)

        res = pd.read_sql(sql, self.engine)

        return res['a'][0]

    def latest_of_trade(self, table, column, code="600519"):
        sql = "select max({1}) as a from {0} where code = {2}".format(table, column, code)

        res = pd.read_sql(sql, self.engine)

        return res['a'][0]

class codeGetter:
    """
    用来获取指定日期
    """

    def __init__(self, db="ods"):
        self.db = db
        self.engine = sqlalchemy.create_engine(
            'mysql+pymysql://root:sun123456@localhost:3306/{}?charset=utf8'.format(self.db))

    def codes(self):
        sql = "select code from ods.ods_stock_basic_info_full_tbl"

        res = pd.read_sql(sql, self.engine)

        return res['code'].to_list()