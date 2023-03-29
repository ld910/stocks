import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
my_font = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')

# 读取 'stock_sh_a.csv' 文件为 DataFrame
stock_sh_a_df = pd.read_csv('stock_sh_a.csv')

# 准备用于绘图的数据
dates = [
    "20200331", "20200630", "20200930", "20201231",
    "20210331", "20210630", "20210930", "20211231",
    "20220331", "20220630", "20220930", "20221231"
]
dates_readable = [pd.to_datetime(date, format='%Y%m%d').strftime('%Y-%m') for date in dates]

# 获取用户输入的股票代码
stock_code_input = input("请输入要绘制的股票代码：")

# 从 DataFrame 中查找相应的股票数据
stock_data = stock_sh_a_df.loc[stock_sh_a_df['代码'] == int(stock_code_input)]

if not stock_data.empty:
    # 提取股票名称、营业收入数据和净利润数据
    stock_name = stock_data['名称'].values[0]
    yysr_values = [stock_data[f'{date}_营业收入'].values[0] for date in dates]
    jlr_values = [stock_data[f'{date}_净利润'].values[0] for date in dates]

    # 创建两个子图
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # 绘制营业收入-日期图
    ax1.plot(dates_readable, yysr_values, marker='o')
    ax1.set_xlabel('日期', fontproperties=my_font)
    ax1.set_ylabel('营业收入', fontproperties=my_font)
    ax1.set_title(f'{stock_name} ({stock_code_input}) 营业收入', fontproperties=my_font)
    ax1.grid()

    # 绘制净利润-日期图
    ax2.plot(dates_readable, jlr_values, marker='o', color='orange')
    ax2.set_xlabel('日期', fontproperties=my_font)
    ax2.set_ylabel('净利润', fontproperties=my_font)
    ax2.set_title(f'{stock_name} ({stock_code_input}) 净利润', fontproperties=my_font)
    ax2.grid()

    # 显示图像
    plt.tight_layout()
    plt.show()
else:
    print("找不到该股票代码，请检查输入是否正确。")
