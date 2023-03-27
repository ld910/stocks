import akshare as ak
import pandas as pd
import time

def get_listing_time(stock_code, retries=5, delay=1):
    attempts = 0
    while attempts < retries:
        try:
            listing_time = ak.stock_individual_info_em(symbol=stock_code).loc[lambda df: df['item'] == '上市时间', 'value'].values[0]
            return listing_time
        except Exception as e:
            print(f"请求错误")
            attempts += 1
            if attempts < retries:
                print(f"重试 {attempts}/{retries}")
                time.sleep(delay)
    print(f"到达最大重试次数, {stock_code} 无法获取上市时间")
    return None

# 获取上证a股实时行情数据
stock_sh_a_spot_df = ak.stock_sh_a_spot_em()

# 删除ST股票
stock_sh_a_spot_df = stock_sh_a_spot_df[~stock_sh_a_spot_df['名称'].str.contains('ST')]

# 筛选市值小于50亿的股票
stock_sh_a_spot_df = stock_sh_a_spot_df[stock_sh_a_spot_df['总市值'] < 50e8]

# 给dataframe添加一列，列名为'上市时间'，填入None
stock_sh_a_spot_df['上市时间'] = None

# 使用接口: stock_individual_info_em获取这些股票的上市时间并填入dataframe
for stock_code in stock_sh_a_spot_df['代码']:
    listing_time = get_listing_time(stock_code)
    stock_sh_a_spot_df.loc[stock_sh_a_spot_df['代码'] == stock_code, '上市时间'] = listing_time

# 将字符串格式的上市时间转换为日期格式
stock_sh_a_spot_df['上市时间'] = pd.to_datetime(stock_sh_a_spot_df['上市时间'], format='%Y%m%d', errors='coerce')

# 筛选2018年之后上市的股票
stock_sh_a_spot_df = stock_sh_a_spot_df[stock_sh_a_spot_df['上市时间'] > pd.to_datetime('2018-01-01')]

# 只保留'代码','名称','总市值','上市时间'四列
stock_sh_a_spot_df = stock_sh_a_spot_df[['代码','名称','总市值','上市时间']]

# 保存为csv文件到当前目录
stock_sh_a_spot_df.to_csv('stock_sh_a_spot.csv', index=False)

# 打印保存成功的提示
print('保存成功')