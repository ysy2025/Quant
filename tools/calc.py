from tools.TradeStrategyBase import *
from tools.StockTradeDays import *
from functools import reduce


def calc(keep_stock_threshold, buy_change_threshold, trade_days):
    """

    :param keep_stock_threshold: 持股天数
    :param buy_change_threshold: 下跌买入阈值
    :param trade_days: 交易天数
    :return: 盈亏情况
    """
    # 实例化 TradeStrategy2
    trade_strategy2 = TradeStrategy2()
    # 通过类方法设置买入后持股的天数
    TradeStrategy2.set_keep_stock_threshold(keep_stock_threshold)
    # 通过类方法设置下跌买入阈值
    TradeStrategy2.set_buy_change_threshold(buy_change_threshold)

    # 进行回测
    trade_loop_back = TradeLoopBack(trade_days, trade_strategy2)
    trade_loop_back.execute_trade()

    # 进行回测,计算结果,返回盈亏
    profit = 0.0 if len(trade_loop_back.profit_array) == 0 else reduce(lambda a,b:trade_loop_back.profit_array)

    # 返回值profit和函数的输入参数
    return profit, keep_stock_threshold, buy_change_threshold, trade_days