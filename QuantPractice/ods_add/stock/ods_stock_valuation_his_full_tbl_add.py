import datetime
import random
import sys
import time

import pandas as pd

sys.path.append("E:\\MyGitHub\\myPython\\QuantPractice\\tools")
sys.path.append("/code")
from tools import DBHelper, itemGetter
import baostock as bs

def getValuationHis(code, start_date):
    """
    拿到历史估值数据
    :param code: 代码
    :return: 一个dataframe

    columns 已经标准化为英语了
    date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST

    date    交易所行情日期
    code    证券代码
    open    开盘价
    high    最高价
    low 最低价
    close   收盘价
    preclose    前收盘价
    volume  成交量（累计
    amount  成交额（单位：人民币元）
    adjustflag  复权状态
    turn    换手率
    tradestatus 交易状态
    pctChg  涨跌幅（百分比）
    peTTM   滚动市盈率
    pbMRQ   市净率
    psTTM   滚动市销率
    pcfNcfTTM   滚动市现率
    isST    是否ST股，1是，0否

    adjustflag:复权状态(1：后复权， 2：前复权，3：不复权）
    """
    try:
        rs = bs.query_history_k_data_plus(code,
                                          "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
                                          start_date=start_date, end_date='2099-12-31',
                                          frequency="d", adjustflag="2")
        print('query_history_k_data_plus respond error_code:' + rs.error_code)
        print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        result = result[["date","code","open","peTTM","pbMRQ","psTTM","pcfNcfTTM"]]
        result["code"] = [code[3:] for i in range(len(result))]
        print("=" * 32 + "> 拿到了{0} 大于{1} 的数据!".format(code, pdate))
        return result

    except:
        return pd.DataFrame()

def func(a):
    if a == "":
        return 0
    else:
        return eval(a)

if __name__ == '__main__':
    #### 登陆 baostock 系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    # 需要初始化date;这个应该从mysql里面查询;用贵州茅台做索引,去查
    dateGetter = itemGetter.dateGetter("root", "Alicloud123456!", "localhost")
    table = "ods_stock_valuation_his_full_tbl"
    column = "date"
    date= dateGetter.latest_of_trade(table, column)
    pdate = str(date)
    print("-" * 32 + "> 准备好了 {0}!".format(pdate))

    # 最大时间等于当天,说明已经同步了,就不用add了
    if pdate == datetime.datetime.now().strftime('%Y-%m-%d'):
        print("-" * 32 + "> 已经add过 {0} 的数据了".format(pdate))
    # 或者周六周日不同步
    elif datetime.datetime.now().weekday() > 4:
        print("-" * 32 + "> 周末啦,不开工!")
    else:
        # 首先删除大于pdate的
        dbhelper = DBHelper.DBHelper('localhost', "root", "Alicloud123456!", "ods")
        drop_bigger = "delete from ods_stock_valuation_his_full_tbl where date > '{0}'".format(pdate)
        dbhelper.exec(drop_bigger)

        # 读取基础数据;从数据库中读取
        engine = itemGetter.conGetter.connect_db("root", "Alicloud123456!", "localhost", "ods")
        codes_df = pd.read_sql("select code from ods_stock_basic_info_full_tbl", engine)

        # 针对code进行处理.baostock中需要调整code.
        codes_df['city'] = codes_df["code"].apply(lambda x: "sh." if x.startswith("6") else "sz.")
        codes_df["new_code"] = codes_df["city"] + codes_df["code"]
        codes = codes_df["new_code"].to_list()
        print("-" * 32 + "> 准备好了 codes, 长度是{0}!".format(len(codes)))

        # 初始化一个空df
        valuation_his = pd.DataFrame()

        # 初始化engine
        # engine = connect_db("ods")
        k = 0
        for code in codes:
            print("======> code is {0}".format(code))
            sleeptime = random.randint(1, 10)
            time.sleep(sleeptime / 1000)
            k += 1
            temp = getValuationHis(code, pdate)
            valuation_his = pd.concat([valuation_his, temp], axis=0)
            # 每过500个就保存一下
            if k % 500 == 0:
                sleeptime = random.randint(1, 10)
                time.sleep(sleeptime)
                # 处理数据
                valuation_his['open'] = valuation_his['open'].map(lambda x: func(x))
                valuation_his['peTTM'] = valuation_his['peTTM'].map(lambda x: func(x))
                valuation_his['pbMRQ'] = valuation_his['pbMRQ'].map(lambda x: func(x))
                valuation_his['psTTM'] = valuation_his['psTTM'].map(lambda x: func(x))
                valuation_his['pcfNcfTTM'] = valuation_his['pcfNcfTTM'].map(lambda x: func(x))
                # 保存数据
                valuation_his.to_sql('ods_stock_valuation_his_full_tbl', con=engine, if_exists='append', index=False)
                print("!" * 32 + "> 保存了500条记录!")
                valuation_his=pd.DataFrame()

        # 最后剩下的再存一下
        valuation_his.to_sql('ods_stock_valuation_his_full_tbl', con=engine, if_exists='append', index=False)
        print("!" * 32 + "> 保存完毕!")

        # 更新索引
        print("=" * 32 + "> 准备处理索引!")
        drop_index = "alter table ods_stock_valuation_his_full_tbl drop index value_code;"
        add_index = "alter table ods_stock_valuation_his_full_tbl add index value_code (code) ;"

        drop_index2 = "alter table ods_stock_valuation_his_full_tbl drop index value_cdate;"
        add_index2 = "alter table ods_stock_valuation_his_full_tbl add index value_date (date) ;"

        dbhelper.exec(drop_index)
        dbhelper.exec(add_index)

        dbhelper.exec(drop_index2)
        dbhelper.exec(add_index2)
        print("!" * 32 + "完成.退出!")
        #### 登出 baostock 系统 ####
    bs.logout()