import datetime
import random
import sys
import time

import akshare as ak
import pandas as pd

sys.path.append("E:\\MyGitHub\\myPython\\QuantPractice\\tools")
sys.path.append("/code")
from tools import itemGetter, DBHelper

def getTradeHis(code, start_date)->pd.DataFrame:
    # start_date 包含在内的,因此需要对pdate处理加1
    df = ak.stock_zh_a_hist(symbol=code, period="daily", start_date=start_date, end_date='20500101',
                                            adjust="qfq")
    # columns 重命名
    df.columns = ["date", "open", "close", "highest", "lowest", "volume", "amount",
                  "vibration", "updown", "updown_yuan", "turnover"]
    # 增加一列
    df["code"] = [code for i in range(len(df))]
    # 重置df
    df = df[["code", "date", "open", "close", "highest", "lowest", "volume", "amount", "vibration", "updown",
                 "updown_yuan"]]
    print("=" * 32 + "> 拿到了{0} 大于{1} 的数据!".format(code, start_date))
    return df

if __name__ == '__main__':
    if datetime.datetime.now().weekday() > 4:
        print("-" * 32 + "> 周末啦,不开工!")
    else:
        # 需要拿到code列表
        codeGetter = itemGetter.codeGetter("root", "Alicloud123456!", "localhost")
        codes = codeGetter.codes()

        # 需要初始化date;这个应该从mysql里面查询;用贵州茅台做索引,去查
        dateGetter = itemGetter.dateGetter("root", "Alicloud123456!", "localhost")
        table = "ods_stock_trade_his_full_tbl"
        column = "date"
        date= dateGetter.latest_of_trade(table, column)

        # stock_zh_a_hist 接口是左笔画的,因此需要处理,加一天
        pdate = (date+datetime.timedelta(days=1)).strftime("%Y%m%d")

        # 首先删除大于pdate的
        dbhelper = DBHelper.DBHelper('localhost', "root", "Alicloud123456!", "ods")
        drop_bigger = "delete from ods_stock_trade_his_full_tbl where date > '{0}'".format(str(date))
        dbhelper.exec(drop_bigger)

        # 初始化一个空df
        trade_his = pd.DataFrame()

        # 初始化engine
        engine = itemGetter.conGetter.connect_db("root", "Alicloud123456!", "localhost", "ods")

        k = 0
        for code in codes:
            print("======> code is {0}".format(code))
            sleeptime = random.randint(1, 10)
            time.sleep(sleeptime / 1000)
            k += 1
            temp = getTradeHis(code, date)
            trade_his = pd.concat([trade_his, temp], axis=0)
            # 每过500个就保存一下
            if k % 500 == 0:
                sleeptime = random.randint(1, 10)
                time.sleep(sleeptime)
                # 保存数据
                trade_his.to_sql('ods_stock_trade_his_full_tbl', con=engine, if_exists='append', index=False)
                trade_his=pd.DataFrame()

        # 最后剩下的再存一下
        trade_his.to_sql('ods_stock_trade_his_full_tbl', con=engine, if_exists='append', index=False)

        # 更新索引
        dbhelper = DBHelper.DBHelper('127.0.0.1', "root", "sun123456", "ods")
        drop_index = "alter table ods_stock_trade_his_full_tbl drop index stock_code;"
        add_index = "alter table ods_stock_trade_his_full_tbl add index stock_code (code) ;"

        drop_index2 = "alter table ods_stock_trade_his_full_tbl drop index stock_date;"
        add_index2 = "alter table ods_stock_trade_his_full_tbl add index stock_date (date) ;"

        dbhelper.exec(drop_index)
        dbhelper.exec(add_index)

        dbhelper.exec(drop_index2)
        dbhelper.exec(add_index2)
