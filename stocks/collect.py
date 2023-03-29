import pandas as pd

# 读取 stock_sh_a_spot.csv 文件为 DataFrame
stock_sh_a_spot_df = pd.read_csv('stock_sh_a_spot.csv')

# 日期列表
dates = [
    "20200331", "20200630", "20200930", "20201231",
    "20210331", "20210630", "20210930", "20211231",
    "20220331", "20220630", "20220930", "20221231"
]

# 为每个日期添加营业收入和净利润列
for date in dates:
    stock_sh_a_spot_df[f'{date}_营业收入'] = None
    stock_sh_a_spot_df[f'{date}_净利润'] = None

# 从不同日期的财报文件中找到对应的营业收入和净利润，并添加到 DataFrame 中
for date in dates:
    # 读取对应日期的财报文件
    csv_filename = f'stock_yjbb_em_{date}.csv'
    stock_yjbb_em_df = pd.read_csv(csv_filename)
    
    for stock_code in stock_sh_a_spot_df['代码']:
        try:
            # 获取该股票在该财报日期的营业收入和净利润
            yysr = stock_yjbb_em_df.loc[stock_yjbb_em_df['股票代码'] == stock_code, '营业收入-营业收入'].values[0]
            jlr = stock_yjbb_em_df.loc[stock_yjbb_em_df['股票代码'] == stock_code, '净利润-净利润'].values[0]
            
            # 将营业收入和净利润添加到 DataFrame
            stock_sh_a_spot_df.loc[stock_sh_a_spot_df['代码'] == stock_code, f'{date}_营业收入'] = yysr
            stock_sh_a_spot_df.loc[stock_sh_a_spot_df['代码'] == stock_code, f'{date}_净利润'] = jlr
        except IndexError:
            print(f"股票 {stock_code} 在 {date} 的财报数据未找到")

# 保存为csv文件到当前目录
stock_sh_a_spot_df.to_csv('stock_sh_a.csv', index=False)

# 打印保存成功的提示
print('保存成功')
