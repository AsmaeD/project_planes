############ DATA recover from webpages
# Author(s) : Asmae DADI
# Date of last change :  04/05/2020
# Last modified by : Asmae DADI
####################################

#import libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

#declaration of functions
def tuple_values_to_list_values(t) :
	list_values = []
	for i in t:
		list_values.append(i[1])
	return list_values
	
def data_scrapper_headings(driver, url_head): #returns headings for table in html page

	#driver search for web scrapping
	driver.get(url_head)	
	
	#search all html content of web page
	content = driver.page_source
	
	#convert in soup format	
	soup = BeautifulSoup(content, "lxml")
	
	#search all info in table type
	table = soup.find("table")
	headings = [th.get_text() for th in table.find("tr").find_all("th")]
	
	return headings
		
		
def data_scrapper(driver,url):
	#initialize variables 
	dataset = [] 
	list_elements = []
	#driver search for web scrapping
	driver.get(url)	
	
	#search all html content of web page
	content = driver.page_source
	
	#convert in soup format	
	soup = BeautifulSoup(content, "lxml")
	
	#search all info in table type
	table = soup.find("table")
		
	try : #try to find all tr linked content of table
		headings = [th.get_text() for th in table.find("tr").find_all("th")]
	except AttributeError : return [] #tr type info not found in webpage
	else:
		#tr type info found
		#create zip of rows of table
		for row in table.find_all("tr")[1:]:
			   dataset.append(zip(headings, (td.get_text() for td in row.find_all("td"))))
	
		#transform zip of tuples into list of tuples
		#than transform list of tuples into list of values			   
		for elements in dataset:
			list_elements += [tuple_values_to_list_values(list(elements))]
			
	#create dataframe with headings as column name and values given in tuples		
	return list_elements
	
