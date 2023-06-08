import os
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('./config/config.ini')
filename = config.get('rent', 'rent_filename')

def rent_price_all():
    # 歷年資料夾
    dirs = [d for d in os.listdir("raw_data") if d[:4] == 'real']

    dfs = []

    for d in dirs:
        # print(d)
        df = pd.read_csv(os.path.join("raw_data", d, filename), index_col=False)
        df['Q'] = d[-1]
        dfs.append(df.iloc[1:])

    df = pd.concat(dfs, sort=True)

    # 將'租賃年月日'欄位轉換為字串型態
    df['租賃年月日'] = df['租賃年月日'].astype(str)
    # 新增租賃年份
    df['year'] = df['租賃年月日'].str[:-4].astype(int) + 1911
    # 平方公尺換成坪
    df['單價元平方公尺'] = df['單價元平方公尺'].astype(float)
    df['單價元坪'] = df['單價元平方公尺'] * 3.30579
    # 建物型態
    df['建物型態2'] = df['建物型態'].str.split('(').str[0]

    # 將index改成年月日
    df.index = pd.to_datetime((df['租賃年月日'].str[:-4].astype(int) + 1911).astype(str) + df['租賃年月日'].str[-4:],
                              errors='coerce')

    # print(df)
    return df

def rent_price():
    """
    主要用途: 住家用
    df以['year', '鄉鎮市區', '單價元坪']呈現
    """
    # 歷年資料夾
    dirs = [d for d in os.listdir("raw_data") if d[:4] == 'real']

    dfs = []

    for d in dirs:
        # print(d)
        df = pd.read_csv(os.path.join("raw_data", d, filename), index_col=False)
        df['Q'] = d[-1]
        dfs.append(df.iloc[1:])

    df = pd.concat(dfs, sort=True)

    # 將'租賃年月日'欄位轉換為字串型態
    df['租賃年月日'] = df['租賃年月日'].astype(str)
    # 新增租賃年份
    df['year'] = df['租賃年月日'].str[:-4].astype(int) + 1911
    # 平方公尺換成坪
    df['單價元平方公尺'] = df['單價元平方公尺'].astype(float)
    df['單價元坪'] = df['單價元平方公尺'] * 3.30579
    # 建物型態
    df['建物型態2'] = df['建物型態'].str.split('(').str[0]
    # 篩選主要用途為'住家用'的數據
    df = df[df['主要用途'] == '住家用']
    # 將index改成年月日
    df.index = pd.to_datetime((df['租賃年月日'].str[:-4].astype(int) + 1911).astype(str) + df['租賃年月日'].str[-4:] ,errors='coerce')

    df_rent_price = df[['year', '鄉鎮市區', '單價元坪']]

    print(df_rent_price)
    return df_rent_price

def avg_rent_price():
    df = rent_price()
    # 以 'year' 和 '鄉鎮市區' 來進行分組，並計算 '單價元坪' 的平均值
    avg_buy_sell_price = df.groupby(['year', '鄉鎮市區'])['單價元坪'].mean()

    # print(avg_buy_sell_price)
    return avg_buy_sell_price

def avg_rent_price_2023():
    """
    過濾出2023年的資料
    """
    df = rent_price()
    # 過濾出2023年的資料
    df_2023 = df[df['year'] == 2023]
    # 以 '鄉鎮市區' 來進行分組，並計算 2023 年的 '單價元坪' 平均值
    avg_rent_price_23 = df_2023.groupby('鄉鎮市區')['單價元坪'].mean()

    print(avg_rent_price_23)
    return avg_rent_price_23


def rent_pandasSeries2df():
    avg_rent_price_2023_df = avg_rent_price_2023().reset_index().rename(
        columns={"鄉鎮市區": "鄉鎮市區", 0: "avg_rent_price_2023"})
    return avg_rent_price_2023_df


'''
rent_price()
avg_rent_price_2023()
'''