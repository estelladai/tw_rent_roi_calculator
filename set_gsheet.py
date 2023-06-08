import gspread
from google.oauth2 import service_account
import configparser

def set_gsheet():
    config = configparser.ConfigParser()
    config.read('./config/config.ini')
    # 設定 Google Sheets API 服務帳戶金鑰json檔路徑、表格 ID
    Key_file_path = config.get('gsheet', 'KEY_FILE_PATH')
    sheet_id = config.get('gsheet', 'SHEET_ID')
    sheet_name = config.get('gsheet', 'SHEET_NAME')

    # Set up the Google Sheets API client
    credentials = service_account.Credentials.from_service_account_file(Key_file_path)
    scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/spreadsheets'])
    client = gspread.authorize(scoped_credentials)

    # Open the Google Sheet
    spreadsheet = client.open_by_key(sheet_id)
    worksheet = spreadsheet.worksheet(sheet_name)

    return worksheet
