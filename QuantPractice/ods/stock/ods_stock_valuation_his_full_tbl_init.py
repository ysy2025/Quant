import random
import time
import pandas as pd
import sqlalchemy
from tools import DBHelper, itemGetter
import baostock as bs

def getValuationHis(code)->pd.DataFrame:
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
                                          start_date='1900-01-01', end_date='2099-12-31',
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

        return result
    except:
        return pd.DataFrame()

def connect_db(host, name, pwd, db):
    engine = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}:3306/{3}?charset=utf8'.format(name, pwd, host, db))
    return engine

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

    # 读取基础数据;从数据库中读取
    engine = connect_db("root", "sun123456", "localhost", "ods")

    codeGetter = itemGetter.codeGetter("root", "sun123456", "localhost")
    codes_df = codeGetter.codes()

    # 针对code进行处理.baostock中需要调整code.
    codes_df['city'] = codes_df["code"].apply(lambda x: "sh." if x.startswith("6") else "sz.")
    codes_df["new_code"] = codes_df["city"] + codes_df["code"]
    codes = codes_df["new_code"].to_list()

    # 初始化一个空df
    valuation_his = pd.DataFrame()

    # print(codes[2999:3002])
    k = 0
    for code in codes:
        print("======> code is {0}".format(code))
        sleeptime = random.randint(1, 10)
        time.sleep(sleeptime / 1000)
        k += 1
        temp = getValuationHis(code)
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
            valuation_his=pd.DataFrame()

    # 最后剩下的再存一下
    valuation_his.to_sql('ods_stock_valuation_his_full_tbl', con=engine, if_exists='append', index=False)

    # 更新索引
    dbhelper = DBHelper.DBHelper('127.0.0.1', "root", "sun123456", "ods")
    drop_index = "alter table ods_stock_valuation_his_full_tbl drop index value_code;"
    add_index = "alter table ods_stock_valuation_his_full_tbl add index value_code (code) ;"

    dbhelper.exec(drop_index)
    dbhelper.exec(add_index)

    #### 登出 baostock 系统 ####
    bs.logout()