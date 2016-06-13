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
sh =gc.open_by_url('https://docs.google.com/spreadsheets/d/1dbcJ-WKFdfgjKi07PAeDP-_rHB3mgX4bbUoPzsb0Pug/edit#gid=1061048305')
sh2=gc.open_by_url('https://docs.google.com/spreadsheets/d/1NDO3rCLJYm3UOwQLeWF5RrTnsq65TCHK7AUPnwFsbNw/edit#gid=0')
#worksheet_list= sh.worksheets()
#sheet = raw_input ('Which Worksheet -> ')
#worksheet=sh.worksheet("%s" % sheet)
worksheet=sh.worksheet("Site_X_DMZ_en4m9f.csv")
worksheet2=sh2.worksheet("ic-nm01")
count=0
count_2=3
index=0
count_3=0

#val = worksheet.acell('A1').value
plugin_id= "19506"
plugin_id2="11936"
plugin_list = worksheet.col_values(1)
#host_list = worksheet.col_values(5)
#output_list = worksheet.col_values(13)

#print output_list,'\n'
#x= open('text2.txt', 'r+')
f= open ('text.txt','r+' )
colA=raw_input("Enter Column ->")
env= raw_input("Enter Enviorment ->")
mac="Total Machines scanned :"
for plugin_num in plugin_list:
	count +=1
	
	if plugin_num==plugin_id2:

		#output_list1= str(re.split('\n', worksheet.acell('M%d'%count).value))
		output_list1= str(worksheet.acell('M%d'%count).value).split('\n')
		host =  worksheet.acell('E%d'%count).value
		host= str(host.split("\n"))

		F= host+"->"+output_list1[1]+"\n"
		F=F.split("->")
		print F


	if plugin_num == plugin_id:
		index+=1
		output_list = str(worksheet.acell('M%d'%count).value).split('\n')
		host1= worksheet.acell('E%d'%count).value
		host1= str(host1.split("\n"))
		X= host1+"->" + output_list[16]+"\n"
		X=X.split("->")
		print X
		print "-----------------"

		#print "***********Windows machines with no Credential ckecks************"
		if "Microsoft" in F[1] and "Credentialed checks : no" in X[1]:
			if F[0]== X[0]:
				count_3+=1
				count_2+=1
				many_wins=F[0]+","
				#many_wins=str(re.su("\]","",many_wins))
				
				f.write(many_wins)
				worksheet2.update_acell('%s1' % colA, env)
				#worksheet2.update_acell('%s%d' % (colA, scan), mac+str(index))
				cell_list = worksheet2.range('%s2:%s%d' % (colA,colA,count_2))
				

			
		else:
			count_2+=1
			
			many_wins="No Windows Machine"
			
			worksheet2.update_acell('%s1' % colA, env)
			cell_list=worksheet2.range('%s2:%s%d' % (colA,colA,count_2))

f.closed



s=open('text.txt','r')
wins=s.read()
many_wins=wins.split(',')


if "No Windows Machine" in many_wins:
	scan= 4
	print scan			
	print index
	#worksheet2.update_acell('%s%d'% (colA,scan) , mac+str(index))
else: 
	scan = 3 + count_3
	print count_3
	#worksheet2.update_acell('%s%d'% (colA,scan) , mac+str(index))

for cell in cell_list:
	index2 = 0
	for win_machine in many_wins:
	
		cell_list[index2].value=win_machine
		index2 +=1
worksheet2.update_cells(cell_list)

worksheet2.update_acell('%s%d'% (colA,scan) , mac+str(index))

s.closed
#x.closed
#('perl perl_test.pl')
