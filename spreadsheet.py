
import gspread
from oauth2client.service_account import ServiceAccountCredentials



def getDataSheet(sheet, data_type= None):
	'''
	function to access all the data from a speadsheet, output = json file
	test = ok
	need to implement 'else' to choose which type of data
	'''
	if data_type == None:
		return sheet.get_all_records()
	else:
		return

def getLastRow(sheet):
	'''
	function to get the last empty row (verification on the first column)
	'''

	#get all the values in a list of an x col
	col_values = sheet.col_values(1)
	ct = 0
	#loop until find an empty cell 
	while col_values[ct] != "":
		ct += 1
	return ct+1

def getUserData(sheet):
	'''
	function to get all the new user from the spreadsheet
	'''
	# creation of the list whch contains all the data
	user_data = []
	# compteur to get the new data without taking the label
	ct = 2

	#loop to put all the values of the row in a list
	while getLastRow(sheet) != ct:
		user_data.append(sheet.row_values(ct))
		ct+=1
	return user_data



def setUserDataIntoOutput(sheet, user_data):
	'''
	function to set all the user data into the spreadsheet 
	'''

	



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
	getUserData(output_worksheet)

	

	
	
if __name__ == '__main__':
	main()

