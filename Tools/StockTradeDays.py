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
        pp_array = [(price1, price2) for price1, price2 in zip((price_float_array[:-1], price_float_array[1:]))]

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
        change_array = map(lambda pp : reduce(lambda a, b : round((b-a)/a, 3), pp), pp_array)

        change_array.insert(0, 0)

        return change-array
