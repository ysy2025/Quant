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