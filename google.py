import json
import gspread
from array import * 

#hardy-binder-128720@appspot.gserviceaccount.com share this link with google spreadsheet

from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('googleSheet-ec36ec5a91d3.json'))
scope=['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc= gspread.authorize(credentials)
sh =gc.open_by_url('https://docs.google.com/spreadsheets/d/1NxvA9OW3XM_QfrHwgrTIzNs7HezglTkww2uKov_Iq3I/edit#gid=2081839951')
#worksheet_list= sh.worksheets()
sheet = raw_input ('Which Worksheet -> ')

worksheet=sh.worksheet("%s" % sheet)

#worksheet=sh.worksheet("Sheet2")
#val = worksheet.acell('B1').value
#update = "1234"
no_comma= open('no_comma.txt', 'r')
servers=no_comma.read()
many_server=servers.split()
index = 2
indexQ=0
for server in many_server:
	index+=1
	

env =raw_input ("Enviroment -> ") 
if env == "same":
	pass
else:
	worksheet.update_acell('a3', env)

 
softw = raw_input ("Software(Version)->")
if softw == "same":
	pass
else:
	worksheet.update_acell('c3',softw)

num= raw_input ("Count -> ")
if num == "same":
	pass
else: 
	worksheet.update_acell('f3',num)


mouse = raw_input('Enter range [begin] -> ')
if mouse != "top":
	#cat = raw_input ('Enter range [end] -> ')
	int_mouse = int(mouse)
	indexQ= index-2
	rat = indexQ+int_mouse
	cell_list = worksheet.range('g%d:g%d' % (int_mouse,rat))
	softw = raw_input ("Software(Version)->")
	worksheet.update_acell('c%d'% (int_mouse),softw)
else:
	cell_list = worksheet.range('g3:g%d' % index)
	softw = raw_input ("Software(Version)->")
	worksheet.update_acell('c3',softw)




for cell in cell_list:
	count = 0
	for each_server in many_server:
	
		cell_list[count].value=each_server
		count +=1

worksheet.update_cells(cell_list)


print "Total server impotted:", count
