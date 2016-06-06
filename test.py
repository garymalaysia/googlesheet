import json
import gspread
from os import system
import re
from array import * 

#hardy-binder-128720@appspot.gserviceaccount.com share this link with google spreadsheet

from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('googleSheet-ec36ec5a91d3.json'))
scope=['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc= gspread.authorize(credentials)
sh =gc.open_by_url('https://docs.google.com/spreadsheets/d/1oGD5icabw-9ktcoqeh3dR8HTv3Mf2ZeasEOvnEnSv8s/edit#gid=2072757837')
#worksheet_list= sh.worksheets()
#sheet = raw_input ('Which Worksheet -> ')
#worksheet=sh.worksheet("%s" % sheet)
worksheet=sh.worksheet("Site_X_DMZ_m900xn")
count=0
count_2=0
index=0
#val = worksheet.acell('A1').value
plugin_id= "19506"
plugin_id2="11936"
plugin_list = worksheet.col_values(1)
#host_list = worksheet.col_values(5)
#output_list = worksheet.col_values(13)

#print output_list,'\n'
x= open('text2.txt', 'r+')
f= open ('text.txt','r+' )


for plugin_num in plugin_list:
	count +=1
	if plugin_num==plugin_id2:

		output_list1= str(re.split('\n', worksheet.acell('M%d'%count).value))
		host =  worksheet.acell('E%d'%count).value
		output_list1= re.sub('\['," ",output_list1)
		output_list1= re.sub('\]'," ",output_list1)
		#output_list1= str(re.split('\n+', output_list1))
		x.write(host+' '+output_list1+'\n')
		print count

for plugin_num in plugin_list:
	count_2+=1
	if plugin_num == plugin_id:
		index+=1
		host= worksheet.acell('E%d'%count_2).value
		output_list = str(re.split('\n+',worksheet.acell('M%d'%count_2).value))

		output_list= re.sub('\['," ",output_list)
		output_list= re.sub('\]'," ",output_list)
		#output_list= str(re.split('\n+', output_list))
				#print count_2, host
		
		#f.write(host)
		f.write(host+" , "+ output_list+'\n')
		#f.write(host+" , "+ output_list1)

print "total index :", index
f.closed		
x.closed
system('perl perl_test.pl')
