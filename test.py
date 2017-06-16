import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread.httpsession import HTTPSession



user_info_speadsheet = "medirechner_WS17_18_v02 (Haslreiter).xlsx"
model_speadsheet = "Wintersemester 2017-18 v27.xlsx"

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
'''

http_session = HTTPSession(headers={'Connection':'Keep-Alive'})
client = gspread.Client(creds, http_session)
client.login()
'''


spreadsheet = client.open(model_speadsheet)
raw_data_worksheet = spreadsheet.worksheet("EINGABE")


raw_data_worksheet.insert_row('1', 11)