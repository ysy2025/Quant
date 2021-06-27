import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 股票数量
    stock_cnt = 200
    # 504个交易日
    view_days = 504
    # 生成服从正态分布的均值期望=0,标准差=1的序列
    stock_day_change = np.random.standard_normal((stock_cnt, view_days))
    # 打印
    print(stock_day_change.shape)
    # 打印第一只股票的前5个交易日的涨跌幅情况
    print(stock_day_change[0:1, :5])

    # 保留后50天的随机数据作为验证数据
    keep_days = 50
    # calculate 200 stocks in 454 days, up or down, split 0-454day, view_days = 504
    stock_day_change_test = stock_day_change[:stock_cnt, 0:view_days - keep_days] # view_days - keep_days, means 504-50=454days, need to calculate

    # print most downsize in 454 days, np.sum to sum the downsize;np.sort to sort result
    print(np.sort(np.sum(stock_day_change_test, axis = 1))[:3])

    # argsort to sort stocks with biggest downsize. list them.
    stock_lower_array = np.argsort(np.sum(stock_day_change_test, axis=1))[:3]

    #output stock index
    print(stock_lower_array)

    # 均值回归策略
    def show_buy_lower(stock_index):
        """
        均值回归策略
        :param stock_index:需要购买的股票代号
        :return:
        """
        #设置一个一行两列的可视化图表
        _, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (16,5))
        # view_days, 504, keey_days = 50
        axes[0].plot(np.arange(0, view_days - keep_days), stock_day_change_test[stock_index].cumsum())
        # 计算从454-505天的股票走势
        cs_buy = stock_day_change[stock_index][view_days-keep_days:view_days].cumsum()

        # 绘制454-504的股票走势
        axes[1].plot(np.arange(view_days-keep_days, view_days), cs_buy)

        #返回454-604计算盈亏序列的最后一个值
        return cs_buy[-1]

    #最后输出的盈亏比例
    profit = 0
    #遍历跌幅最大的3只股票序列序号
    for stock_index  in stock_lower_array:
        #profit,就是3只股票从454天买入开始计算,知道最后一天的盈亏比例
        profit += show_buy_lower(stock_index)

    #str.format
    print(stock_lower_array, profit)