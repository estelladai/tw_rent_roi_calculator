import requests
import os
import zipfile
import time

'''
資料來源: 內政部地政司_不動產成交案件_實際資訊資料供應系統
全國 (含不動產買賣+預售屋買賣+不動產租賃)
https://plvr.land.moi.gov.tw/Index

參考資料: finlab
https://www.finlab.tw/real-estate-analasys-histograms/
'''


def real_estate_crawler(year, season):
    if year > 1000:
        year -= 1911

    # download real estate zip file
    res = requests.get("https://plvr.land.moi.gov.tw//DownloadSeason?season=" + str(year) + "S" + str(
        season) + "&type=zip&fileName=lvr_landcsv.zip")

    # save content to file
    fname = str(year) + str(season) + '.zip'
    open(fname, 'wb').write(res.content)

    # make additional folder for files to extract
    folder = 'real_estate' + str(year) + str(season)
    if not os.path.isdir(folder):
        os.mkdir(folder)

    # extract files to the folder
    with zipfile.ZipFile(fname, 'r') as zip_ref:
        zip_ref.extractall(folder)

    time.sleep(10)


# save to directory
os.chdir('./raw_data')

start_year = 106
end_year = 113

# year資料取出106~112年
for year in range(start_year, end_year):
    for season in range(1, 5):
        # season資料取出112年Q1
        if year == 112 and season > 1:
            break
        real_estate_crawler(year, season)
        print(f'downloaded year:{year},season:{season}')
