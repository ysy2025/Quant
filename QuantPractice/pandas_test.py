import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 获取股票信息
import baostock as bs

if __name__ == '__main__':
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    # 获取茅台的收盘价
    maotai = bs.query_history_k_data_plus("sz.300750", "date,code,open,high,low,close", start_date='2020-01-01',
                                          end_date='2021-06-28', frequency="d", adjustflag="3")
    """
    type(ningde)
    Out[8]: baostock.data.resultset.ResultData
    ningde.get_row_data()
    Out[10]: ['2020-01-02', 'sz.300750', '107.2100', '108.8500', '105.7000', '107.5200']
    可以看到,ningde的结果是ResultData
    是可以迭代的
    每一行都是list数据类型
    """
    data_list = []
    while (maotai.error_code == '0') & maotai.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(maotai.get_row_data())
    mt = pd.DataFrame(data_list, columns=maotai.fields)
    print(mt.head(5))

    # date_array = mt["date"].to_list()
    price_array = mt['close'].to_list()
    # print(date_array[:10])
    print(price_array[:10])
    print(type(price_array))


    """
    series.resample('3T', label='right').sum()
    resample,取平均数,用.mean试一试
    """