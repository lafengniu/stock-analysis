# 使用AKShare获取实时数据
import akshare as ak

def get_market_data():
    # 沪深京A股整体行情
    df = ak.stock_zh_a_spot_em()
    # 大盘指数数据
    index_df = ak.stock_zh_index_daily(symbol="sh000001")  # 上证指数
    return df, index_df

# 调用函数并获取数据
market_data, index_data = get_market_data()

# 筛选涨幅在9.98%以上的股票
high_gain_stocks = market_data[market_data['涨跌幅'] >= 9.98]

# 打印结果
print("涨幅在9.98%以上的股票：")
print(high_gain_stocks)
