import six
from abc import ABCMeta, abstractmethod
"""
TradeStrategyBase类通过继承ABCMeta,@abstractmethod声明方法为借口.
@是装饰器:http://c.biancheng.net/view/2270.html
#funA 作为装饰器函数
def funA(fn):
    #...
    fn() # 执行传入的fn参数
    #...
    return '...'
@funA
def funB():
    #...
    
上面的代码等价于
def funA(fn):
    #...
    fn() # 执行传入的fn参数
    #...
    return '...'
def funB():
    #...
funB = funA(funB)
*args表示任意数量的未知参数,是list列表
**kwargs,表示键值对参数
"""
class TradeStrategyBase(six.with_metaclass(ABCMeta, object)):
    """
    交易策略抽象基类
    """
    @abstractmethod
    def buy_strategy(self, *args, **kwargs):
        """
        买入策略基类
        :param args:
        :param kwargs:
        :return:
        """
        pass
    @abstractmethod
    def sell_strategy(self, *args, **kwargs):
        """
        卖出策略基类
        :param args:
        :param kwargs:
        :return:
        """
        pass

class TradeStrategy1(TradeStrategyBase):
    """
    交易策略1,追涨,当股价涨超过一个阈值,默认7%,买入股票并持有s_keep_stock_threshold(20)天
    """
    s_keep_stock_threshold = 20

    def __init__(self):
        # 持有了多少天
        self.keep_stock_day = 0
        # 7%上涨
        self.__buy_stock_threshold = 0.07

    def buy_strategy(self, trade_index, trade_day, trade_days):
        # 没有持股(keep_stock_day = 0),而且涨幅>7%,买入
        if self.keep_stock_day == 0 and trade_day.change > self.__buy_stock_threshold:
            self.keep_stock_day += 1
        elif self.keep_stock_day > 0:
            # 已经持有股票了,持有股票天数递增
            self.keep_stock_day += 1
    def sell_strategy(self, trade_index, trade_day, trade_days):
        # 持有超过阈值
        if self.keep_stock_day >= TradeStrategy1.s_keep_stock_threshold:
            self.keep_stock_day = 0
        """
        property 属性
        我们可以使用@property装饰器来创建只读属性
        @property装饰器会将方法转换为相同名称的只读属性,可以与所定义的属性配合使用,这样可以防止属性被修改.
        class DataSet(object):
          @property
          def method_with_property(self): ##含有@property
              return 15
          def method_without_property(self): ##不含@property
              return 15
        
        l = DataSet()
        print(l.method_with_property) # 加了@property后,可以用调用属性的形式来调用方法,后面不需要加().
        print(l.method_without_property())  #没有加@property , 必须使用正常的调用方法的形式,即在后面加()
        
        由于python进行属性的定义时,没办法设置私有属性,因此要通过@property的方法来进行设置.这样可以隐藏属性名,让用户进行使用的时候无法随意修改
        """
        @property
        def buy_change_threshold(self):
            return self.__buy_stock_threshold
        @buy_change_threshold.setter
        def buy_change_threshold(self, buy_change_threshold):
            """
            阈值需要为float;
            :param self:
            :param buy_change_threshold:
            :return:
            """
            if not isinstance(buy_change_threshold, float):
                raise TypeError("buy_change_threshold must be a float. Please re-input.")
            self.__buy_stock_threshold = round(buy_change_threshold, 2)

"""
交易回测系统
"""
class TradeLoopBack(object):
    def __init__(self, trade_days, trade_strategy):
        """
        trade_strategy,可以用上面的TradeStrategyBase或者TradeStrategy1
        使用前面封装的StockTradeDays类和本节编写的交易策略类TradeStrategyBase类,初始化交易系统
        :param trade_days: StockTradeDays交易数据序列
        :param trade_strategy: TradeStrategyBase交易策略
        """
        self.trade_days = trade_days
        self.trade_strategy = trade_strategy
        # 交易盈亏结果序列
        self.profit_array = []
    def execute_trade(self):
        """
        执行交易回测
        :return:
        """
        for index, day in enumerate(self.trade_days):
            """
            以时间驱动,完成交易回测
            """
            # 如果持有时间>0,加入交易盈亏结果序列
            if self.trade_strategy.keep_stock_day > 0:
                self.profit_array.append(day.change)
            # hasattr:用于查询对象有没有实现某个方法
            if hasattr(self.trade_strategy, "buy_strategy"):
                # 买入策略执行
                self.trade_strategy.buy_strategy(index, day, self.trade_days)
            if hasattr(self.trade_strategy, "sell_strategy"):
                self.trade_strategy.sell_strategy(index, day, self.trade_days)

"""
交易策略2:股价连续两个交易日下跌并且跌幅超过阈值,买入并持有s_keep_stock_threshold = 10天
"""
class TradeStrategy2(TradeStrategyBase):
    """
    交易策略2:均值回归策略,股价连续两个交易日下跌并且跌幅超过阈值,买入并持有s_keep_stock_threshold = 10天
    """
    # 持有天数门槛
    s_keep_stock_threshold = 10
    # 下跌买入阈值
    s_buy_stock_threshold = -0.10
    def __init__(self):
        self.keep_stock_day = 0
        # pass
    def but_strategy(self, trade_index, trade_day, trade_days):
        if self.keep_stock_day == 0 and trade_index > 1:
            """
            当你没有股票时,self.keep_stock_day=0,而且trade_index>1,不是交易开始的第一天,因为需要昨天的数据
            trade_down 在trade_day.change<0才可以;判断今天估价是否下跌
            yesterday_down,昨天是否跌
            trade_day是交易当天
            trade_days是交易日记录
            trade_index是交易日index
            """
            today_down = trade_day.change < 0
            yesterday_down = trade_days[trade_index-1].change<0
            # 两天总跌幅
            down_rate = trade_day.change + trade_days[trade_index-1].change
            # 买入条件,跌幅超过阈值s_buy_change_threshold
            if today_down and yesterday_down and down_rate < TradeStrategy2.s_buy_stock_threshold:
                self.keep_stock_day += 1
            elif self.keep_stock_day > 0:
                self.keep_stock_day += 1
    def sell_strategy(self, trade_index, trade_day, trade_days):
        # 当持有天数>阈值,卖出
        if self.keep_stock_day > TradeStrategy2.s_keep_stock_threshold:
            self.keep_stock_day = 0

    """
    关于 classmethod staticmethod
    python staticmethod 返回函数的静态方法
    class C(object):
    @staticmethod
    def f(arg1, arg2, ...):
        ...
    以上实例声明了静态方法 f,从而可以实现实例化使用 C().f(),当然也可以不实例化调用该方法 C.f().
    classmethod 修饰符对应的函数不需要实例化,不需要 self 参数,但第一个参数需要是表示自身类的 cls 参数,可以来调用类的属性,类的方法,实例化对象等
    class A(object):
    bar = 1
    def func1(self):  
        print ('foo') 
    @classmethod
    def func2(cls):
        print ('func2')
        print (cls.bar)
        cls().func1()   # 调用 foo 方法
    A.func2()# 不需要实例化
    输出结果为：
    func2
    1
    foo
    """
    @classmethod
    def set_keep_stock_threshold(cls, keep_stock_threshold):
        cls.s_keep_stock_threshold = keep_stock_threshold
    @staticmethod
    def set_buy_change_threshold(buy_change_threshold):
        TradeStrategy2.s_buy_stock_threshold = buy_change_threshold

import baostock as bs
import pandas as pd
from tools.StockTradeDays import *
if __name__ == '__main__':
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    # 获取茅台的收盘价
    maotai = bs.query_history_k_data_plus("sz.300750", "date,code,open,high,low,close", start_date='2018-01-01',
                                          end_date='2021-12-31', frequency="d", adjustflag="3")
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
    # print(trade_days)

    trade_strategy1 = TradeStrategy1()
    # TradeStrategy2.set_keep_stock_threshold(20)
    # TradeStrategy2.set_buy_change_threshold(-0.1)
    trade_loop_back = TradeLoopBack(trade_days, trade_strategy1)
    trade_loop_back.execute_trade()
    profit = 0.0 if len(trade_loop_back.profit_array) == 0 else reduce(lambda a, b: a+b, trade_loop_back.profit_array)
    print(profit)

    ts2 = TradeStrategy2
    print(ts2)