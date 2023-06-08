import plotly.express as px
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker
from buy_sell_price import *
from PIL import Image
import io

df = buy_sell_price_all()


def make_plt_chart():
    city = get_city()
    data_type = get_data_type()

    myfont = FontProperties(fname='./static/fonts/TaipeiSansTCBeta-Regular.ttf')

    prices = {}
    for district in set(df['鄉鎮市區']):
        cond = (
                (df['主要用途'] == '住家用')
                & (df['鄉鎮市區'] == district)
                & (df['單價元坪'] < df["單價元坪"].quantile(0.95))
                & (df['單價元坪'] > df["單價元坪"].quantile(0.05))
        )

        groups = df[cond]['year']

        # 將資料轉換為浮點數並計算平均值
        prices[district] = df[cond]['單價元坪'].astype(float).groupby(groups).mean().loc[2018:]

    price_history = pd.DataFrame(prices)

    plt.figure(figsize=(10, 5))
    price_history.plot()

    # 自定義y軸刻度格式為千分位
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    plt.title(f'{city}近5年{data_type}歷年單坪價格走勢圖', fontproperties=myfont)
    plt.xlabel('年份', fontproperties=myfont)
    plt.ylabel('單價元/坪', fontproperties=myfont)
    plt.legend(prop=myfont)

    # 將圖例移到圖形外的右邊
    plt.legend(prop=myfont, bbox_to_anchor=(1.05, 1), loc='upper left')
    # 自動調整子圖參數
    plt.tight_layout()

    plt.savefig(f'./static/charts/{city}_{data_type}_plt_chart.png')


def make_px_chart():
    city = get_city()
    data_type = get_data_type()

    prices = {}
    for district in set(df['鄉鎮市區']):
        cond = (
                (df['主要用途'] == '住家用')
                & (df['鄉鎮市區'] == district)
                & (df['單價元坪'] < df["單價元坪"].quantile(0.95))
                & (df['單價元坪'] > df["單價元坪"].quantile(0.05))
        )

        groups = df[cond]['year']

        # 將資料轉換為浮點數並計算平均值
        prices[district] = df[cond]['單價元坪'].astype(float).groupby(groups).mean().loc[2018:]

    price_history = pd.DataFrame(prices)

    fig = px.line(price_history)
    fig.update_layout(
        title=f'{city}近5年{data_type}歷年單坪價格走勢圖',
        xaxis_title='年份',
        yaxis_title='單價元/坪',
        legend_title='鄉鎮市區',
        font=dict(family='TaipeiSansTCBeta-Regular')
    )
    fig.update_yaxes(tickformat=',')
    fig.show()

'''
make_plt_chart()
'''

