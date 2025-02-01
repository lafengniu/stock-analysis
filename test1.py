# 使用AKShare获取实时数据
import akshare as ak

def get_market_data():
    # 沪深京A股整体行情
    df = ak.stock_zh_a_spot_em()
    # 大盘指数数据
    index_df = ak.stock_zh_index_daily(symbol="sh000001")  # 上证指数
    return df, index_df

# 调用函数并打印结果
market_data, index_data = get_market_data()
print("沪深京A股行情：")
print(market_data.head())  # 打印前5行数据
print("\n上证指数历史数据：")
print(index_data.head())  # 打印前5行数据
