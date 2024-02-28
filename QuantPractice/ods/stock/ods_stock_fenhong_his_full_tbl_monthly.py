import os
import random
import time

import akshare as ak
import pandas as pd

from tools import itemGetter


def func(money):
    if money == "--":
        return 0
    else:
        foo = money.replace('万', 'e4').replace('亿', 'e8')
        foo = eval(foo)
        return int(foo)

def getCodeDividend(code):
    try:
        div_df = ak.stock_fhps_detail_ths(symbol=code)
        div_df.columns = ["report_date", "board_date", "share_date", "implement_date",
                          "dividend_project", "register_date", "dividend_date", "amount",
                          "process", "dividend_rate", "pre_tax_rate"]

        div_df = div_df[["amount"]]
        div_df["amount"] = div_df["amount"].map(func)
        div_df["amount"] = div_df["amount"] / 100000000
        dividend = round(sum(list(div_df['amount'])), 2)

        dividend_times = int(div_df[div_df["amount"]>0].count())
        return dividend, dividend_times
    except:
        return 0.0, 0

if __name__ == '__main__':
    """
    首先拿到股票清单
    然后遍历
    注意每1个月跑一次就够了
    
    a = {
        "code":["600519"],
        "dividend":[111],
        "dividend_times":[3]
    }
    b = pd.DataFrame(a)
    形成如上数据结构
    """
    codeGetter = itemGetter.codeGetter("root", "sun123456", "localhost")
    codes = codeGetter.codes()

    dividend = []
    dividend_times = []
    k = 0
    for code in codes:
        print("======> code is {0}".format(code))
        sleeptime = random.randint(1, 10)
        time.sleep(sleeptime / 1000)
        k += 1
        if k % 500 == 0:
            sleeptime = random.randint(1, 10)
            time.sleep(sleeptime)
        code_dividend, code_dividend_times = getCodeDividend(code)
        dividend.append(code_dividend)
        dividend_times.append(code_dividend_times)

    res = {
        "code":codes,
        "dividend":dividend,
        "dividend_times":dividend_times
    }

    res_df = pd.DataFrame(res)
    path = os.getcwd()
    file = path + "\ods_stock_fenhong_his_full_tbl_monthly.csv"
    res_df.to_csv(file,index=False)  # index 是为了去掉索引