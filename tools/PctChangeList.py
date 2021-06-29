import numpy as np
import pandas as pd
import baostock as bs
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    #### 获取历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节
    rs = bs.query_history_k_data_plus("sh.688001",
          "date,code,open,high,low,close,preclose,volume,amount,pctChg",
          start_date='2019-07-22', end_date='2021-12-31',
          frequency="d", adjustflag="3")  # frequency="d"取日k线，adjustflag="3"默认不复权
    print('query_history_k_data_plus respond error_code:' + rs.error_code)
    print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    print(result.info)
    result['date'] = result['date'].astype('string')
    result['code'] = result['code'].astype('string')
    for each in ['open', 'high', 'low', 'close', 'preclose', 'volume', 'amount', 'pctChg']:
        result[each] = result[each].astype("float")
    print(result.head(5))

    fig, ax = plt.subplots()

    # We can set the number of bins with the `bins` kwarg
    ax.hist(result.pctChg, bins=10)
    plt.show()
