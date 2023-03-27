import akshare as ak

stock_yjbb_em_df = ak.stock_yjbb_em(date="20221231")
print(stock_yjbb_em_df)

# 保存为csv文件到当前目录
stock_yjbb_em_df.to_csv('stock_yjbb_em.csv', index=False)