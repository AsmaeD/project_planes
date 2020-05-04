############ additionnal DATA recover from webpages
# Author(s) : Asmae DADI
# Date of last change :  04/05/2020
# Last modified by : Asmae DADI
####################################

#import libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

def data_scrapper_headings_add(driver, url_head): #returns headings for table in html page

	#driver search for web scrapping
	driver.get(url_head)	
	
	#search all html content of web page
	content = driver.page_source
	
	#convert in soup format	
	soup = BeautifulSoup(content, "lxml")
	
	#search all info in table type
	table = soup.find("table")
	headings = [th.get_text() for th in table.find_all("td", {"class": "caption"})]
	
	return headings
		
		
def data_scrapper_url(driver,url_incident_regex,url):
	#initialize variable
	incident_info_url_info=[]
	
	#beginning of page by page url recovering
	driver.get(url)	
	
	#search all html content of web page
	content = driver.page_source
	
	#convert in soup format	
	soup = BeautifulSoup(content, "lxml")

	try :
		#verification of table content non empty
		href = soup.find_all('a', {'href' : url_incident_regex})
		href[0] #provoke error if the list is empty
	except IndexError : return []
	else :
		#seperate each in url in the complete list of url
		for a in href:
			incident_info_url_info.append("https://aviation-safety.net/"+a['href'])
					
	return incident_info_url_info
	
def data_scrapper_add(driver, url): #returns elements of  table in html page

	#driver search for web scrapping
	driver.get(url)	
	
	#search all html content of web page
	content = driver.page_source
	
	#convert in soup format	
	soup = BeautifulSoup(content, "lxml")
	
	#search all info in table type
	table = soup.find("table")
	
	try : 
		table_elements = [th.get_text() for th in table.find_all("td", {"class": "desc"})]
	except AttributeError : return []
	else :
		return table_elements


def data_scrapper_add_routes_only(driver, url): #returns elements of  table in html page
	#var initialize
	route_elements = []
	
	#departure and destination heandings regex
	route_elements_regex = re.compile("^D.* airport.*")
	
	#location of accident regex
	location_regex = re.compile("Location.*")
	
	#driver search for web scrapping
	driver.get(url)	
	
	#search all html content of web page
	content = driver.page_source
	
	#convert in soup format	
	soup = BeautifulSoup(content, "lxml")
	
	#search all info in table type
	table = soup.find("table")
	
	#tbody
	try:
		table_body = table.find('tbody')
	except AttributeError:#check if valid url
		return [ '', '','']
	else:
		#rows of table
		rows = table_body.find_all('tr')
	
		#keep only departure and destination airports info
		for row in rows :
			cols = row.find_all('td')
			cols = [ele.text.strip() for ele in cols]
			
			#Add route info
			if re.match(route_elements_regex, cols[0]):
				route_elements.append(cols[1])
				
			#add location information
			if re.match(location_regex, cols[0]):
				route_elements.append(cols[1])
					
		return route_elements

