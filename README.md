# tw_rent_roi_calculator

# 概要
從內政部地政司_不動產成交案件_實際資訊資料供應系統 (https://plvr.land.moi.gov.tw/Index) 爬取房地產全國數據，含不動產買賣、預售屋買賣、不動產租賃，透過資料繪製「近5年不動產買賣單坪價格走勢圖」，以及計算台灣各區域租金投資回報率

# 資料說明
1. 第1個字母代表縣市
2. 最後1個字母代表不動產資料類型

name|schema|description
-|-|-
a_lvr_land_a.csv|schema-main.csv|臺北市不動產買賣
a_lvr_land_b.csv|schema-main-sale.csv|臺北市預售屋買賣
a_lvr_land_c.csv|schema-main-rent.csv|臺北市不動產租賃

![所有資料說明表](https://docs.google.com/spreadsheets/d/1qSuhjntSfDnmu9lnagC09AbsrHQ8Q0qDM3eVSb07LVw/edit#gid=609529863)

# 使用方法
1. git clone此repo到您的本地電腦
2. 透過requirements.txt來安裝所需Python套件
3. 更改config.ini的相關設定
5. 執行main.py以抓取不動產資料，並計算租金投資回報率

# 台灣各地區租金投資回報率
![台灣各地區租金投資回報率](https://docs.google.com/spreadsheets/d/1qSuhjntSfDnmu9lnagC09AbsrHQ8Q0qDM3eVSb07LVw/edit#gid=609529863)

# 近5年台北市不動產買賣單坪價格走勢圖
![台北市不動產買賣單坪價格走勢圖](static/charts/台北市_房屋買賣交易_plt_chart.png)
