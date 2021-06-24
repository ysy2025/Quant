from abupy import ABuSymbolPd

# 阿布量化网址:https://www.abuquant.com/discover
# https://github.com/bbfamily/abu/tree/master/abupy_ui
# https://notebook.community/bbfamily/abu/abupy_lecture/20-A%E8%82%A1%E5%85%A8%E5%B8%82%E5%9C%BA%E5%9B%9E%E6%B5%8B%28ABU%E9%87%8F%E5%8C%96%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3%29

if __name__ == '__main__':
    # 两年的TSLA收盘数据 -> list
    price_array = ABuSymbolPd.make_kl_df('600519', n_folds = 2).close.tolist()
    print(price_array)