# 阿布量化网址:https://www.abuquant.com/discover
# https://github.com/bbfamily/abu/tree/master/abupy_ui
# https://notebook.community/bbfamily/abu/abupy_lecture/20-A%E8%82%A1%E5%85%A8%E5%B8%82%E5%9C%BA%E5%9B%9E%E6%B5%8B%28ABU%E9%87%8F%E5%8C%96%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3%29

# https://blog.crackcreed.com/diy-xue-qiu-app-shu-ju-api/,雪球api

import baostock as bs
# http://baostock.com/baostock/index.php/Python_API%E6%96%87%E6%A1%A3,baostock的API
import pandas as pd
from tools import calc
from tools.StockTradeDays import *
from tools.TradeStrategyBase import *
import numpy as np

if __name__ == '__main__':
    # 两年的TSLA收盘数据 -> list
    # price_array = ABuSymbolPd.make_kl_df('600519', n_folds = 2).close.tolist()
    # price_array = 1
    # print(price_array)

    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    #### 获取历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节
    # rs = bs.query_history_k_data_plus("sh.600519",
    #                                   "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
    #                                   start_date='2018-01-01', end_date='2021-12-31',
    #                                   frequency="d", adjustflag="3")  # frequency="d"取日k线，adjustflag="3"默认不复权
    # print('query_history_k_data_plus respond error_code:' + rs.error_code)
    # print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)
    #
    # #### 打印结果集 ####
    # data_list = []
    # while (rs.error_code == '0') & rs.next():
    #     # 获取一条记录，将记录合并在一起
    #     data_list.append(rs.get_row_data())
    # result = pd.DataFrame(data_list, columns=rs.fields)
    #
    # print(result.info)

    # 获取茅台的收盘价
    maotai = bs.query_history_k_data_plus("sh.600519","date,code,open,high,low,close", start_date='2018-01-01', end_date='2021-12-31',frequency="d", adjustflag="3")
    data_list = []
    while (maotai.error_code == '0') & maotai.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(maotai.get_row_data())
    mt = pd.DataFrame(data_list, columns=maotai.fields)
    # print(mt.head(5))

    # date_array = mt["date"].to_list()
    price_array = mt['close'].to_list()
    # print(date_array[:10])
    print(price_array[:10])
    print(type(price_array))

    date_base = 20180101
    trade_days = StockTradeDays(price_array, date_base)
    print(len(trade_days))
    print(trade_days)

    trade_strategy2 = TradeStrategy2
    TradeStrategy2.set_keep_stock_threshold(20)
    TradeStrategy2.set_buy_change_threshold(-0.1)
    trade_loop_back = TradeLoopBack(trade_days, trade_strategy2)
    trade_loop_back.execute_trade()
    profit = 0.0 if len(trade_loop_back.profit_array) == 0 else reduce(lambda a, b: trade_loop_back.profit_array)
    print(profit)