from buy_sell_price import *

def save_df_to_csv():
    df = buy_sell_price_all()
    df.to_csv('./static/csv/buy_sell_price_all.csv', encoding='utf_8_sig')


'''
save_df_to_csv()
'''
