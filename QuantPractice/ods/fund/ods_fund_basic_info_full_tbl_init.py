import akshare as ak
import sqlalchemy


def connect_db(host, name, pwd, db):
    engine = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}}@{2}:3306/{3}?charset=utf8'.format(name, pwd, host, db))
    return engine

if __name__ == '__main__':
    # 初始化引擎
    engine = connect_db("root", "sun123456", "localhost", "ods")

    df = ak.fund_name_em()
    df.columns = ["code", "abbr_name", "name", "type", "full_name"]

    df = df[['code']]
    # 保存
    df.to_sql('ods_fund_basic_info_full_tbl', con=engine, if_exists='append', index=False)
