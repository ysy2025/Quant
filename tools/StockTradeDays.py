from collections import namedtuple, OrderedDict
# python3 需要先引入reduce
from functools import reduce

from collections import Iterable

class StockTradeDays(object):
    def __init__(self, price_array, start_date, date_array = None):
        # 初始化私有价格序列
        self.__price_array = price_array
        # 初始化私有日期序列
        self.__date_array = self._init_days(start_date, date_array)
        #初始化 涨跌序列
        self.__change_array = self.__init_change()

        #dict组装
        self.stock_dict = self._init_stock_dict()

    def __init_change(self):
        """
        从price_array中,产生change_array;涨跌幅
        :return:
        """
        # 获取价格array
        price_float_array = [float(price_str) for price_str in self.__price_array]
        """
        时间平移,形成交错的收盘价序列;
        比如,茅台,600519
        [(20210101, 2000.1), (20210102, 2010.1), (20210103, 2011.1)]-> [(2000.1, 2010.1), (2010.1, 2011.1)]
        """
        pp_array = [(price1, price2) for price1, price2 in zip(price_float_array[:-1], price_float_array[1:])]

        # 有了交错的收盘价,就可以计算delta了
        """
        https://www.runoob.com/python/python-func-reduce.html
        def add(x, y) :            # 两数相加
            return x + y
        sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
        sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
        print(sum1)
        print(sum2)
        reduce函数用法如上;前面是方法,后面是需要调用方法的对象
        change_array, 首先针对pp_array的成分,调用pp
        pp呢,则是,针对pp中的成分,a和b,做delta
        所以层级调用后得到针对pp_array中的成分,的两个成分,做delta
        """
        """
        原来的change_array是map类型,并且可以insert;python3版本中不能用map.insert了
        将change_array转换为list,再insert就可以了
        """
        # change_array = map(lambda pp : reduce(lambda a, b : round((b-a)/a, 3), pp), pp_array)
        change_array = list(map(lambda pp: reduce(lambda a, b: round((b - a) / a, 3), pp), pp_array))
        change_array.insert(0, 0)

        return change_array

    def _init_days(self, start_date, date_array):
        """
        protect级别方法
        :param start_date:
        :param date_array:
        :return:
        """
        # 如果开始时, date_array是空的
        if date_array is None:
            # 通过start_date和self.__price_array来确定日期序列
            date_array = [str(start_date + ind) for ind, _ in enumerate(self.__price_array)]
        else:
            # 稍后内容使用外部直接设置的方式;如果外面设置了date_array, 就直接转换成str类型组成新的date_array
            date_array = [str(date) for date in date_array]
        return date_array

    def _init_stock_dict(self):
        """
        使用namedtuple, OrderedDict将结果合并
        :return:
        """
        stock_namedtuple = namedtuple("stock", ("date", "price", "change"))
        # 使用已经被复制的 __date_array等进行OrderedDict的组装
        stock_dict = OrderedDict((date, stock_namedtuple(date, price, change)) for date, price, change in zip(self.__date_array, self.__price_array, self.__change_array))

        return stock_dict

    def filter_stock(self, want_up = True, want_calc_sum = False):
        """
        筛选子集结果
        :param want_up:是否筛选上涨
        :param want_calc_sum: 是否计算涨跌幅和
        :return:
        """
        filter_func = (lambda day: day.change > 0) if want_up else (lambda day: day.change < 0)
        # 确定需要的days
        want_days = filter(filter_func, self.stock_dict.values())

        # 如果不需要计算涨跌幅和,就返回want_days;反之计算涨跌幅和
        if not want_calc_sum:
            return want_days
        # 计算涨跌幅和
        else:
            change_sum = 0.0
            for day in want_days:
                change_sum += day.change
            return change_sum

    """
    __str__, __iter__, __getitem__, __len__,后面再说
    """

    def __str__(self):
        return str(self.stock_dict)
    def __iter__(self):
        """
        通过代理stock_dict的迭代,产生元素
        :return:
        """
        for key in self.stock_dict:
            yield self.stock_dict[key]
    def __getitem__(self, index):
        date_key = self.__date_array[index]
    def __len__(self):
        return len(self.stock_dict)


if __name__ == "__main__":
    price_array = ["133.77", "134.32", "133.23", "133.70", "133.70"]
    """
    ["133.77", "134.32", "133.23", "133.70", "133.70"]
    """
    print(price_array)

    date_base = 20170101
    trade_days = StockTradeDays(price_array, date_base)
    """
    OrderedDict([('20170101', stock(date='20170101', price='133.77', change=0)), 
    ('20170102', stock(date='20170102', price='134.32', change=0.004)),
    ('20170103', stock(date='20170103', price='133.23', change=-0.008)), 
    ('20170104', stock(date='20170104', price='133.70', change=0.004)), 
    ('20170105', stock(date='20170105', price='133.70', change=0.0))])
    
    这里通过自定义 repr和str函数,可以打印
    def __str__(self):
        return str(self.stock_dict)
    而 __repr__ = __str__
    """
    print(trade_days)


    # 判断是否可以迭代
    if isinstance(trade_days, Iterable):
        for each in trade_days:
            print(each)

    change_sum = trade_days.filter_stock()

    """
    stock(date='20170102', price='134.32', change=0.004)
    stock(date='20170104', price='133.70', change=0.004)
    """
    for each in change_sum:
        print(each)