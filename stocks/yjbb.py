import akshare as ak
import time

dates = [
    "20200331", "20200630", "20200930", "20201231",
    "20210331", "20210630", "20210930", "20211231",
    "20220331", "20220630", "20220930", "20221231"
]

def get_stock_yjbb_em(date, retries=10, delay=1):
    attempts = 0
    while attempts < retries:
        try:
            stock_yjbb_em_df = ak.stock_yjbb_em(date=date)
            return stock_yjbb_em_df
        except Exception as e:
            print(f"请求错误")
            attempts += 1
            if attempts < retries:
                print(f"重试 {attempts}/{retries}")
                time.sleep(delay)
    print(f"到达最大重试次数, 无法获取 {date} 财报")
    return None

for date in dates:
    stock_yjbb_em_df = get_stock_yjbb_em(date)
    csv_filename = f'stock_yjbb_em_{date}.csv'
    stock_yjbb_em_df.to_csv(csv_filename, index=False)

# 打印保存成功的提示
print('全部保存成功')