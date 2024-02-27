import pymysql
import sqlalchemy
import pandas as pd

from tools import DBHelper, itemGetter

def ali_connect_db():
    engine = sqlalchemy.create_engine('mysql+pymysql://root:Alicloud123456!@39.101.76.35:3306/ods?charset=utf8')
    return engine


if __name__ == '__main__':
    ali_engine = ali_connect_db()
    test = pd.read_sql("show tables", ali_engine)
    test.head()