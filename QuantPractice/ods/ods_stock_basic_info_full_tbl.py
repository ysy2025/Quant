import akshare as ak

"""
获取沪深上市公司基本情况
code,代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本(亿)
totals,总股本(亿)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
esp,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期
undp,未分利润
perundp, 每股未分配
rev,收入同比(%)
profit,利润同比(%)
gpr,毛利率(%)
npr,净利润率(%)
holders,股东人数

目前只能拿到
名称	类型	描述
A股代码	object	-
A股简称	object	-
A股上市日期	object	-
A股总股本	object	-
A股流通股本	object	-
所属行业	object	-
"""
if __name__ == '__main__':
    shanghai_df = ak.stock_info_sh_name_code(symbol="主板A股")
    print(shanghai_df)
    # 上证的总股本,行业,需要通过东方财富的接口拿
    stock_individual_info_em_df = ak.stock_individual_info_em(symbol="600000")
    print(stock_individual_info_em_df)