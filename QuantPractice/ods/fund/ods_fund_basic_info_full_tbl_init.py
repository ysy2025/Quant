import akshare as ak
import sqlalchemy

from tools import itemGetter


if __name__ == '__main__':
    # 初始化引擎
    engine = itemGetter.conGetter.connect_db("root", "sun123456", "localhost", "ods")

    df = ak.fund_name_em()
    df.columns = ["code", "abbr_name", "name", "type", "full_name"]

    df = df[['code']]
    # 保存
    df.to_sql('ods_fund_basic_info_full_tbl', con=engine, if_exists='append', index=False)
