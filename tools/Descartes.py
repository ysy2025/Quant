import pandas as pd
import numpy as np
import itertools
from tools.calc import *
if __name__ == '__main__':

    keep_stock_list = np.arange(2,30,2).tolist()
    print(keep_stock_list)

    buy_change_list = (np.arange(-5, -16, -1)/100).tolist()
    print(buy_change_list)

    print(len(keep_stock_list))
    print(type(keep_stock_list))
    print(len(buy_change_list))

    result = []
    for keep_stock_threshold, buy_change_threshold in itertools.product(keep_stock_list, buy_change_list):
        result.append(calc(keep_stock_threshold, buy_change_threshold))

    print(result)