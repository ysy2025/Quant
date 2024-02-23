import pymysql
import pandas as pd

class mysqlTool:
    def __init__(self, host, db, user, pwd):
        # MySQL
        self.host = host
        self.db = db
        self.MYSQ_USER = user
        self.pwd = pwd
        self.connect = pymysql.connect(
            host=self.host,
            db=self.db,
            port=3306,
            user=self.MYSQ_USER,
            passwd=self.pwd,
            charset='utf8',
            use_unicode=False
        )
        print(self.connect)
        self.cursor = self.connect.cursor()

    def create_table(self, sql):
        self.cursor.execute(sql)

    # 关闭游标和数据库连接
    def close(self):
        self.cursor.close()
        self.connect.close()