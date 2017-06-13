
import gspread
from oauth2client.service_account import ServiceAccountCredentials



def accessSheet(sheet, data_type= None):
	'''
	function to access all the data from a speadsheet, output = json file
	test = ok
	need to implement 'else' to choose which type of data
	'''
	if data_type == None:
		return sheet.get_all_records()
	else:
		return

def accessRow(sheet, num_row):
	'''
	function to access a specific row 
	'''

def getLastRow(sheet):
	#get all the values in a list of an x col
	col_values = sheet.col_values(1)
	ct = 0

	while col_values[ct] != "":
		ct += 1
	return ct+1


def main():
	'''VARIABLES'''
	user_info_speadsheet = "medirechner_WS17_18_v02 (Haslreiter).xlsx"
	model_speadsheet = "Wintersemester 2017-18 v27.xlsx"

	#access the right data with autorization
	scope = ['https://spreadsheets.google.com/feeds']
	#autentify the account with the secret key of the json file
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)

	#open the speadsheet
	spreadsheet = client.open(model_speadsheet)
	#set the output sheet of the spreadsheet
	output_worksheet = spreadsheet.worksheet("EINGABE")
	print(getLastRow(output_worksheet))
	
	
if __name__ == '__main__':
	main()

