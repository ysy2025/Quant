DROP TABLE IF EXISTS ods_stock_trade_his_full_tbl;
CREATE TABLE ods_stock_trade_his_full_tbl(
    code VARCHAR(32) NOT NULL   COMMENT '代码' ,
    pdate DATETIME NOT NULL   COMMENT '日期' ,
    open DECIMAL(24,6)    COMMENT '开盘;开盘价' ,
    close DECIMAL(24,6)    COMMENT '收盘;收盘价' ,
    highest DECIMAL(24,6)    COMMENT '最高;最高价' ,
    lowest DECIMAL(24,6)    COMMENT '最低;最低价' ,
    volume INT    COMMENT '成交量;成交量; 注意单位: 股' ,
    amount DECIMAL(24,6)    COMMENT '成交额;成交额; 注意单位: 元' ,
    vibration DECIMAL(24,6)    COMMENT '振幅;振幅' ,
    updown DECIMAL(24,6)    COMMENT '涨跌幅;收盘涨跌幅度' ,
    updown_yuan DECIMAL(24,6)    COMMENT '涨跌额;收盘涨跌,元'
    PRIMARY KEY (code,pdate)
)  COMMENT = 'ods_stock_trade_his_full_tbl;akshare-历史行情数据
这个表统一做前复权,以当前股价为基准，保持当前价格不变，降低前期价格，将复权前的k线下移，以达到图形的匹配，保持股价走势的连续性。
根据scode和pdate进行处理,加上索引?目前历史数据加起来应该在百万量级,短期也不会暴增到千万级别.加个索引就够了.
每天insert进当天的数据即可.';

DROP TABLE IF EXISTS ods_stock_business_basic_info_full_tbl;
CREATE TABLE ods_stock_business_basic_info_full_tbl(
    code VARCHAR(32) NOT NULL   COMMENT '代码' ,
    business VARCHAR(255)    COMMENT '主营业务' ,
    product_type VARCHAR(255)    COMMENT '产品类型' ,
    product_name VARCHAR(255)    COMMENT '产品名称' ,
    bus_scope VARCHAR(900)    COMMENT '经营范围' ,
    PRIMARY KEY (code)
)  COMMENT = 'akshare-主营介绍-同花顺
接口: stock_zyjs_ths
公司主营业务介绍.没那么核心.';

DROP TABLE IF EXISTS ods_stock_business_detail_info_full_tbl;
CREATE TABLE ods_stock_business_detail_info_full_tbl(
    code VARCHAR(32) NOT NULL   COMMENT '代码' ,
    pdate DATETIME NOT NULL   COMMENT '报告日期' ,
    classify_type VARCHAR(255)    COMMENT '分类类型' ,
    main_business_compose VARCHAR(255)    COMMENT '主营构成' ,
    main_business_income DECIMAL(24,6)    COMMENT '主营收入' ,
    main_business_income_ratio DECIMAL(24,6)    COMMENT '收入比例' ,
    main_business_cost DECIMAL(24,6)    COMMENT '主营成本' ,
    main_business_cost_ratio DECIMAL(24,6)    COMMENT '成本比例' ,
    main_business_profit DECIMAL(24,6)    COMMENT '主营利润' ,
    main_business_profit_ratio DECIMAL(24,6)    COMMENT '利润比例' ,
    gross_profit_margin DECIMAL(24,6)    COMMENT '毛利率' ,
    PRIMARY KEY (code,pdate)
)  COMMENT = 'akshare
主营构成-东财
接口: stock_zygc_em
公司主营业务介绍.没那么核心.';

DROP TABLE IF EXISTS ods_stock_financial_info_full_tbl;
CREATE TABLE ods_stock_financial_info_full_tbl(
    code VARCHAR(32) NOT NULL   COMMENT '代码' ,
    pdate DATETIME    COMMENT '日期' ,
    pe DECIMAL(24,6)    COMMENT '市盈率' ,
    pe_ttm DECIMAL(24,6)    COMMENT '市盈率TTM' ,
    pb DECIMAL(24,6)    COMMENT '市净率' ,
    ps DECIMAL(24,6)    COMMENT '市销率' ,
    ps_ttm DECIMAL(24,6)    COMMENT '市销率TTM' ,
    dv DECIMAL(24,6)    COMMENT '股息率' ,
    dv_ttm DECIMAL(24,6)    COMMENT '股息率TTM' ,
    total_mv DECIMAL(24,6)    COMMENT '总市值' ,
    PRIMARY KEY (code)
)  COMMENT = 'ods_stock_financial_info_full_tb;A 股个股指标
接口: stock_a_indicator_lg
目标地址: https://www.legulegu.com/stocklist
描述: 乐咕乐股-A 股个股指标: 市盈率, 市净率, 股息率
限量: 单次获取指定 symbol 的所有历史数据
核心基础表.代码,简称,上市时间,股本,行业.
每天insert进新的即可.';

DROP TABLE IF EXISTS dim_industry_full_tbl;
CREATE TABLE dim_industry_full_tbl(
    id VARCHAR(32)    COMMENT 'id' ,
    industry VARCHAR(32)    COMMENT '行业' 
)  COMMENT = '同花顺-同花顺行业一览表
接口: stock_board_industry_summary_ths
目标地址: http://q.10jqka.com.cn/thshy/';

DROP TABLE IF EXISTS dim_industry_stock_mapping_full_tbl;
CREATE TABLE dim_industry_stock_mapping_full_tbl(
    id INT    COMMENT 'id' ,
    industry VARCHAR(90)    COMMENT '行业' ,
    code INT    COMMENT '代码' ,
    name VARCHAR(90)    COMMENT '名称' 
)  COMMENT = '同花顺-同花顺行业一览表
接口: stock_board_industry_summary_ths
目标地址: http://q.10jqka.com.cn/thshy/
同花顺-成份股-行业代码
接口: stock_board_cons_ths';

DROP TABLE IF EXISTS ods_industry_trade_daily_full_tbl;
CREATE TABLE ods_industry_trade_daily_full_tbl(
    TENANT_ID VARCHAR(32)    COMMENT '租户号' ,
    REVISION VARCHAR(32)    COMMENT '乐观锁' ,
    CREATED_BY VARCHAR(32)    COMMENT '创建人' ,
    CREATED_TIME DATETIME    COMMENT '创建时间' ,
    UPDATED_BY VARCHAR(32)    COMMENT '更新人' ,
    UPDATED_TIME DATETIME    COMMENT '更新时间' 
)  COMMENT = '同花顺-指数
接口: stock_board_industry_index_ths
目标地址: http://q.10jqka.com.cn/gn/detail/code/301558/
描述: 同花顺-板块-行业板块-指数日频率数据';

DROP TABLE IF EXISTS ods_industry_summary_full_tbl;
CREATE TABLE ods_industry_summary_full_tbl(
    id INT    COMMENT 'id' ,
    industry VARCHAR(90)    COMMENT '行业' ,
    updown DECIMAL(24,6)    COMMENT '代码' ,
    volume DECIMAL(24,6)    COMMENT '总成交量;注意单位: 万手' ,
    amount DECIMAL(24,6)    COMMENT '总成交额;注意单位: 亿元' ,
    up_num INT    COMMENT '上涨家' ,
    down_num INT    COMMENT '下跌家' ,
    leader VARCHAR(90)    COMMENT '领涨股' ,
    leader_price DECIMAL(24,6)    COMMENT '领涨股-最新价' ,
    leader_updown DECIMAL(24,6)    COMMENT '领涨股-涨跌幅;注意单位: %' 
)  COMMENT = '同花顺-同花顺行业一览表
接口: stock_board_industry_summary_ths
目标地址: http://q.10jqka.com.cn/thshy/
同花顺-成份股-行业代码
接口: stock_board_cons_ths';

DROP TABLE IF EXISTS dim_stock_info_full_tbl;
CREATE TABLE dim_stock_info_full_tbl(
    code VARCHAR(32) NOT NULL   COMMENT '代码' ,
    name VARCHAR(90)    COMMENT '简称' ,
    ipo_time DATETIME    COMMENT '上市时间' ,
    sum_share DECIMAL(24,6)    COMMENT '总股本' ,
    fluent_share DECIMAL(24,6)    COMMENT '流动股本' ,
    industry VARCHAR(90)    COMMENT '行业' ,
    sum_fenhong DECIMAL(24,6)    COMMENT '总分红;单位:亿' ,
    sum_ipo DECIMAL(24,6)    COMMENT '总融资;单位:亿' ,
    PRIMARY KEY (code)
)  COMMENT = 'dim_stock_info_full_tbl;核心维度表.代码,简称,上市时间,股本,行业.
akshare-股票市场总貌
每天insert进新的即可.';

DROP TABLE IF EXISTS ods_stock_fenhong_his_full_tbl;
CREATE TABLE ods_stock_fenhong_his_full_tbl(
    code VARCHAR(32) NOT NULL   COMMENT '代码' ,
    ptime DATETIME NOT NULL   COMMENT '分红日期' ,
    amount DECIMAL(24,6)    COMMENT '分红总额' ,
    PRIMARY KEY (code,ptime)
)  COMMENT = '分红配送详情-同花顺
接口: stock_fhps_detail_ths
目标地址: https://basic.10jqka.com.cn/new/603444/bonus.html
描述: 同花顺-分红融资
限量: 单次获取指定股票的分红融资数据';

DROP TABLE IF EXISTS ods_stock_ipo_info_full_tbl;
CREATE TABLE ods_stock_ipo_info_full_tbl(
    code VARCHAR(32)    COMMENT '代码' ,
    name VARCHAR(90)    COMMENT '名称' ,
    ipo_pdate DATETIME    COMMENT '上市日期' ,
    sum_fenhong DECIMAL(24,6)    COMMENT '累计分红;注意单位: 亿' ,
    fenhong_times INT    COMMENT '分红次数' ,
    sum_ipo DECIMAL(24,6)    COMMENT '融资总额;注意单位: 亿' ,
    ipo_times INT    COMMENT '融资次数' 
)  COMMENT = '接口: stock_history_dividend
目标地址: http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/lsfh/index.phtml?p=1&num=5000
描述: 新浪财经-发行与分配-历史分红
限量: 单次获取所有股票的历史分红数据';

DROP TABLE IF EXISTS ods_stock_basic_info_full_tbl;
CREATE TABLE ods_stock_basic_info_full_tbl(
    code VARCHAR(32) NOT NULL   COMMENT '代码' ,
    name VARCHAR(90)    COMMENT '简称' ,
    ipo_time DATETIME    COMMENT '上市时间' ,
    sum_share DECIMAL(24,6)    COMMENT '总股本' ,
    fluent_share DECIMAL(24,6)    COMMENT '流动股本' ,
    industry VARCHAR(90)    COMMENT '行业' ,
    city VARCHAR(90)    COMMENT '城市' ,
    board VARCHAR(90)    COMMENT '板块' ,
    PRIMARY KEY (code)
)  COMMENT = 'ods_stock_basic_info_full_tbl;核心维度表.代码,简称,上市时间,股本,行业.
akshare-股票市场总貌
每天insert进新的即可.';

https://blog.csdn.net/zhh_920509/article/details/129757516
python金融数据分析和可视化--03利用Akshare获取股票数据
以及存mysql

https://zhuanlan.zhihu.com/p/638056122
下载并可视化
https://zhuanlan.zhihu.com/p/641150441