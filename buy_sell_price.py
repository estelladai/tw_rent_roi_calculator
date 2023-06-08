import os
import pandas as pd
import configparser

'''
國民身分證統一編號英文代碼與配賦縣市對照表
https://bthr.gov.taipei/News_Content.aspx?n=A75E2BF58F8BC883&s=A0B263D2B83B811B
'''

config = configparser.ConfigParser()
config.read('./config/config.ini')
filename = config.get('buy_sell', 'buy_sell_filename')

def get_city():
    city_dict = {'a': '台北市', 'f': '新北市', 'h': '桃園', 'j': '新竹縣', 'o': '新竹市', 'b': '台中市',
                 'd': '台南市', 'e': '高雄市', 'm': '南投縣'}
    city = city_dict[filename[0]]
    return city

def get_data_type():
    data_3type = {'a': '房屋買賣交易', 'b': '新成屋交易', 'c': '租房交易'}
    data_type = data_3type[filename.split('.')[0][-1]]
    return data_type


def buy_sell_price_all():
    # 歷年資料夾
    dirs = [d for d in os.listdir("raw_data") if d[:4] == 'real']

    dfs = []

    for d in dirs:
        # print(d)
        df = pd.read_csv(os.path.join("raw_data", d, filename), index_col=False, low_memory=False)
        df['Q'] = d[-1]
        dfs.append(df.iloc[1:])

    df = pd.concat(dfs, sort=True)

    # 將'交易年月日'欄位轉換為字串型態
    df['交易年月日'] = df['交易年月日'].astype(str)
    # 新增交易年份
    df['year'] = df['交易年月日'].str[:-4].astype(int) + 1911
    # 平方公尺換成坪
    df['單價元平方公尺'] = df['單價元平方公尺'].astype(float)
    df['單價元坪'] = df['單價元平方公尺'] * 3.30579
    # 建物型態
    df['建物型態2'] = df['建物型態'].str.split('(').str[0]
    # 刪除有備註之交易（多為親友交易、價格不正常之交易）
    df = df[df['備註'].isnull()]
    # 將index改成年月日
    df.index = pd.to_datetime((df['交易年月日'].str[:-4].astype(int) + 1911).astype(str) + df['交易年月日'].str[-4:],
                              errors='coerce')

    # print(df)
    return df

def buy_sell_price():
    """
    主要用途: 住家用
    df以['year', '鄉鎮市區', '單價元坪']呈現
    """
    # 歷年資料夾
    dirs = [d for d in os.listdir("raw_data") if d[:4] == 'real']

    dfs = []

    for d in dirs:
        # print(d)
        df = pd.read_csv(os.path.join("raw_data", d, filename), index_col=False, low_memory=False)
        df['Q'] = d[-1]
        dfs.append(df.iloc[1:])

    df = pd.concat(dfs, sort=True)

    # 將'交易年月日'欄位轉換為字串型態
    df['交易年月日'] = df['交易年月日'].astype(str)
    # 新增交易年份
    df['year'] = df['交易年月日'].str[:-4].astype(int) + 1911
    # 平方公尺換成坪
    df['單價元平方公尺'] = df['單價元平方公尺'].astype(float)
    df['單價元坪'] = df['單價元平方公尺'] * 3.30579
    # 建物型態
    df['建物型態2'] = df['建物型態'].str.split('(').str[0]
    # 刪除有備註之交易（多為親友交易、價格不正常之交易）
    df = df[df['備註'].isnull()]
    # 篩選主要用途為'住家用'的數據
    df = df[df['主要用途'] == '住家用']
    # 將index改成年月日
    df.index = pd.to_datetime((df['交易年月日'].str[:-4].astype(int) + 1911).astype(str) + df['交易年月日'].str[-4:] ,errors='coerce')

    df_buy_sell_price = df[['year', '鄉鎮市區', '單價元坪']]

    print(df_buy_sell_price)
    return df_buy_sell_price



def avg_buy_sell_price():
    df = buy_sell_price()
    # 以 'year' 和 '鄉鎮市區' 來進行分組，並計算 '單價元坪' 的平均值
    avg_buy_sell_price_df = df.groupby(['year', '鄉鎮市區'])['單價元坪'].mean()

    # print(avg_buy_sell_price_df)
    return avg_buy_sell_price_df

def avg_buy_sell_price_2023():
    """
    過濾出2023年的資料
    """
    df = buy_sell_price()
    # 過濾出2023年的資料
    df_2023 = df[df['year'] == 2023]
    # 以'鄉鎮市區'來進行分組，並計算2023年的'單價元坪'平均值
    avg_buy_sell_price_23 = df_2023.groupby('鄉鎮市區')['單價元坪'].mean()

    print(avg_buy_sell_price_23)
    return avg_buy_sell_price_23


def buy_sell_pandasSeries2df():
    avg_buy_sell_price_2023_df = avg_buy_sell_price_2023().reset_index().rename(
        columns={"鄉鎮市區": "鄉鎮市區", 0: "avg_buy_sell_price_2023"})
    return avg_buy_sell_price_2023_df

'''
buy_sell_price()
avg_buy_sell_price_2023()
'''
