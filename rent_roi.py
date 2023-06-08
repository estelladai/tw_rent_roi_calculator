from buy_sell_price import avg_buy_sell_price_2023, buy_sell_pandasSeries2df
from rent_price import avg_rent_price_2023, rent_pandasSeries2df
import pandas as pd
from set_gsheet import set_gsheet
from gspread_dataframe import set_with_dataframe

'''
存至gsheet
https://docs.google.com/spreadsheets/d/1qSuhjntSfDnmu9lnagC09AbsrHQ8Q0qDM3eVSb07LVw/edit#gid=609529863
'''

def calculate_rental_yield_2023():
    # 2023年的平均單坪購買價格和租金價格
    avg_buy_sell_price = avg_buy_sell_price_2023()
    avg_rent_price = avg_rent_price_2023()

    # 計算租金報酬率，租金*12除以購買價格
    rental_yield_2023 = avg_rent_price * 12 / avg_buy_sell_price

    print(rental_yield_2023)
    return rental_yield_2023

def rent_roi_pandasSeries2df():
    calculate_rental_yield_df = calculate_rental_yield_2023().reset_index().rename(
        columns={"鄉鎮市區": "鄉鎮市區", 0: "rental_yield"})
    return calculate_rental_yield_df


def combine_rent_price_roi_2023():
    # 呼叫Pandas Series轉換成DataFrame的函數
    avg_buy_sell_price_2023_df = buy_sell_pandasSeries2df().rename(columns={"單價元坪": "2023年平均買賣價/坪"})
    avg_rent_price_2023_df = rent_pandasSeries2df().rename(columns={"單價元坪": "2023年平均租金/坪"})
    rental_yield_2023_df = rent_roi_pandasSeries2df().rename(columns={"單價元坪": "2023年租金報酬率"})

    # 將3個DataFrame透過'鄉鎮市區'進行合併
    rent_price_roi_df_1 = pd.merge(avg_buy_sell_price_2023_df, avg_rent_price_2023_df, on='鄉鎮市區')
    rent_price_roi_df = pd.merge(rent_price_roi_df_1, rental_yield_2023_df, on='鄉鎮市區')

    print(rent_price_roi_df)
    return rent_price_roi_df

def rent_price_roi_df2gsheet():
    worksheet = set_gsheet()
    rent_price_roi_df = combine_rent_price_roi_2023()
    # 新增一欄 "2023年租金報酬率%"
    rent_price_roi_df["2023年租金報酬率%"] = rent_price_roi_df["2023年租金報酬率"] * 100
    # 使用gspread_dataframe的set_with_dataframe方法將df輸出到gsheet
    set_with_dataframe(worksheet, rent_price_roi_df)

'''
combine_rent_price_roi_2023()
rent_price_roi_df2gsheet()
'''