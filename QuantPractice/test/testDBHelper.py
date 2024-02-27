from tools import DBHelper
import pymysql
if __name__ == '__main__':

    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='sun123456', charset='utf8')
    # cursor = conn.cursor()
    db = DBHelper.DBHelper('127.0.0.1', "root", "sun123456", "test")
    res = db.fetch_all("show tables")
    print(res)
