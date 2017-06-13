import gspread
from oauth2client.service_account import ServiceAccountCredentials


def main():

	scope = ['https://spreadsheets.google.com/feeds']
	print('1')
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	print('2')
	client = gspread.authorize(creds)
	print('3')
	sheet = client.open("medirechner_WS17_18_v02 (Haslreiter).xlsx").sheet1
	print('4')
	list_of_hashes = sheet.get_all_records()
	print(list_of_hashes)




if __name__ == '__main__':
	main()

