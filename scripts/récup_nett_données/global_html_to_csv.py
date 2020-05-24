############ DATA recover from webpages
# Author(s) : Asmae DADI
# Date of last change : 04/05/2020
# Last modified by : Asmae DADI
####################################

#import libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

#import function from script
from data_scrapping_script import data_scrapper 
from data_scrapping_script import data_scrapper_headings
from data_scrapping_script import tuple_values_to_list_values
from data_scrapping_script_complemental import data_scrapper_url
from data_scrapping_script_complemental import data_scrapper_headings_add
from data_scrapping_script_complemental import data_scrapper_add
from data_scrapping_script_complemental import data_scrapper_add_routes_only

## Start with 1st layer of data scrapping page by page, by year 

#global variables 
complete_list_table_content = []
complete_list_table_urls = []
complete_list_table_content_add = []
complete_list_table_routes_add = []
driver = webdriver.Chrome("/home/dadi/Téléchargements/chromedriver")
url_incident_regex = re.compile('/database/record.php?.*')
country_regex = re.compile("\(.*\)")
url_head = "https://aviation-safety.net/database/dblist.php?Year=1919&lang=&page=1"
route_headings = ["incident_country","departure_airport","destination_airport"]

#search headings name
headings_table = data_scrapper_headings(driver, url_head)


#beginning of page by page data recovering
for i in list(range(1919,1930,1)) : #i represents year
		
	for j in range(1,100,1): # j represents page index
		
		#change rul accorind to year and page
		url = "https://aviation-safety.net/database/dblist.php?Year="+str(i)+"&lang=&page="+str(j)	
		
		#catch all list of elements in table of page 
		try :
			table_elements = data_scrapper(driver,url)
			table_elements[0] #provoke indexerror if empty list
		except IndexError: break
		else :
			#add new row elements to the complete list
			complete_list_table_content+=table_elements
		
		#catch all urls in table giving additional info 
		try :
			table_urls = data_scrapper_url(driver,url_incident_regex,url)
			table_urls[0]#provoke indexerror if empty list
			
		except IndexError: break
		else :
			#add new url to the complete list
			complete_list_table_urls+=table_urls
			
#verification
#print(complete_list_table_urls)
	
#search headings for additional info table
headings_table_add = data_scrapper_headings_add(driver, complete_list_table_urls[0])

#search table informations accroding to new urls found		
# ~ for add_url in complete_list_table_urls :
	# ~ #put all table elements in list
	# ~ table_elements_additional = data_scrapper_add(driver,add_url)
	# ~ #create list of lists for dataframe
	# ~ complete_list_table_content_add.append( table_elements_additional)


#search table info on routes only in the additional url  **Temporary fix for data conformity**
for add_url in complete_list_table_urls :
	#put route info elements in list
	table_elements_additional = data_scrapper_add_routes_only(driver,add_url)
	#create list of lists for dataframe of route info only
	complete_list_table_routes_add.append(table_elements_additional)


############Data frame creation 


#create initial dataframe
df = pd.DataFrame(complete_list_table_content, columns=headings_table)
	
df2 = pd.DataFrame(complete_list_table_routes_add, columns=route_headings)

#Change date format to year only
for i in range(len(df['date'])):
	year_only = re.findall(r"[0-9]{4,4}", df['date'][i])
	df['date'][i] = year_only[0]
	
#Country isolation in incident location
for i in range(len(df2['incident_country'])):
	#find all instances of parenthesis
	country_parenthesis = re.findall(r"\( .*\)", df2['incident_country'][i])
	
	#isolate if exists the country in the parenthesis
	country_only = re.findall(r"[A-Za-z ]*",country_parenthesis[0].replace(u'\xa0', u'') )
	
	#delete all empty instances
	while("" in country_only) :
		country_only.remove("")
		
	#add country of incident
	df2['incident_country'][i] = country_only[0]
	
#create complete data frame with 2 dataframes
df = df.join(df2, how='outer')
	
print(df.head())

#create csv file containing all info
df.to_csv('plain_incidents_web_content.csv', encoding='UTF-8')
