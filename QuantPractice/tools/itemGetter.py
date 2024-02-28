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

    def __init__(self, user, pwd, host, db="ods"):
        self.user = user
        self.pwd = pwd
        self.host = host
        self.db = db
        self.engine = sqlalchemy.create_engine(
            'mysql+pymysql://{0}:{1}@{2}:3306/{3}?charset=utf8'.format(self.user, self.pwd, self.host, self.db))

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

    def __init__(self, user, pwd, host, db="ods"):
        self.user = user
        self.pwd = pwd
        self.host = host
        self.db = db
        self.engine = sqlalchemy.create_engine(
            'mysql+pymysql://{0}:{1}@{2}:3306/{3}?charset=utf8'.format(self.user, self.pwd, self.host, self.db))

    def codes(self):
        sql = "select code from ods.ods_stock_basic_info_full_tbl"

        res = pd.read_sql(sql, self.engine)

        return res['code'].to_list()

class conGetter:
    def connect_db(host, name: object, pwd: object, db: object) -> object:
        engine = sqlalchemy.create_engine(
            'mysql+pymysql://{0}:{1}@{2}:3306/{3}?charset=utf8'.format(name, pwd, host, db))
        return engine