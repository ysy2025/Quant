import akshare as ak
import sqlalchemy

from tools import itemGetter

if __name__ == '__main__':
    # 初始化引擎
    engine = itemGetter.conGetter.connect_db("localhost", "root", "Alicloud123456!", "ods")

    df = ak.index_stock_info()
    df.columns = ["index_code", "display_name", "publish_date"]

    df = df[['code']]
    # 保存
    df.to_sql('ods_index_stock_info_full_tbl', con=engine, if_exists='append', index=False)
