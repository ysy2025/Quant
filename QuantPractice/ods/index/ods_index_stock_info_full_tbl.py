import akshare as ak
import sqlalchemy

def connect_db(db):
    engine = sqlalchemy.create_engine('mysql+pymysql://root:sun123456@localhost:3306/{}?charset=utf8'.format(db))
    return engine

if __name__ == '__main__':
    # 初始化引擎
    engine = connect_db("ods")

    df = ak.index_stock_info()
    df.columns = ["index_code", "display_name", "publish_date"]

    df = df[['code']]
    # 保存
    df.to_sql('ods_index_stock_info_full_tbl', con=engine, if_exists='append', index=False)
