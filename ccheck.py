import json
import gspread
import re
from array import * 

#hardy-binder-128720@appspot.gserviceaccount.com share this link with google spreadsheet

from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('googleSheet-ec36ec5a91d3.json'))
scope=['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc= gspread.authorize(credentials)
sh =gc.open_by_url('https://docs.google.com/spreadsheets/d/12IaxqL2CmyJG2dzQP6hKtSUk5DnmoS3pgaD3R4uBtp8/edit#gid=213942210')
sh2=gc.open_by_url('https://docs.google.com/spreadsheets/d/1NDO3rCLJYm3UOwQLeWF5RrTnsq65TCHK7AUPnwFsbNw/edit#gid=0')
#worksheet_list= sh.worksheets()
#sheet = raw_input ('Which Worksheet -> ')
#worksheet=sh.worksheet("%s" % sheet)
worksheet=sh.worksheet("Site_X_Test_Servers_g2tsb5.csv")
worksheet2=sh2.worksheet("Sheet1")

cell_list=worksheet2.range('f2:f3')

s=open('text.txt','r')
wins=s.read()
many_wins=wins.split(",")

print many_wins[0]

#many_wins=many_wins(']')
#Many_wins=str(re.sub(r'\W','',many_wins))
#many_wins=str(re.sub("\[","\n",many_wins))
#many_wins=many_wins.split()



for cell in cell_list:
	index2 = 0
	for win_machine in many_wins:
	
		cell_list[index2].value=win_machine
		index2 +=1
worksheet2.update_cells(cell_list)

#worksheet2.update_acell('%s%d'% (colA,scan) , mac+str(index))

s.closed













