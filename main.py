from house_raw_data import *
from make_chart import *
from rent_roi import *

if __name__ == "__main__":
    download_raw_data()
    make_plt_chart()
    combine_rent_price_roi_2023()
    rent_price_roi_df2gsheet()
