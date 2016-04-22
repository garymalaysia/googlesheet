import json
import gspread
from array import * 

from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('googleSheet-ec36ec5a91d3.json'))
scope=['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc= gspread.authorize(credentials)
sh =gc.open_by_url('https://docs.google.com/spreadsheets/d/10YcMsSzoFNN8GtNoJAL4UuMp8Uq0qgo-5Lck7M6bnnw/edit#gid=434747921')
#worksheet_list= sh.worksheets()
worksheet=sh.worksheet("Microsoft .NET")
#worksheet=sh.worksheet("Sheet2")
#val = worksheet.acell('B1').value
#update = "1234"
no_comma= open('no_comma.txt', 'r')
servers=no_comma.read()
many_server=servers.split()

#env =raw_input ("Enviroment -> ") 


#worksheet.update_acell('a3', env)

#softw = raw_input ("Software(Version)->")

#worksheet.update_acell('c3',softw)

#num= raw_input ("Count -> ")

#worksheet.update_acell('f3',num)

cell_list = worksheet.range('g148:g301')

for cell in cell_list:
	count = 0
	for each_server in many_server:
	
		cell_list[count].value=each_server
		count +=1

worksheet.update_cells(cell_list)


print count