from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests 

# List of Bright Stars
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

#Getting page
page = requests.get(START_URL)

temp_list=[]

soup=BeautifulSoup(page.text, "html.parser")
star_table = soup.find("table")
total_table = len(star_table)

table_rows = star_table.find_all('tr')

for rows in table_rows:
    td = rows.find_all('td')
    row = [i.text.rstrip()for i in td]
    temp_list.append(row)

Star_name=[]
Distance=[]
Mass=[]
Radius=[]
Lum = []
print (temp_list)

for i in range(i, len(temp_list)):
    Star_name.append(temp_list [i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])

headers = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']

star_df_2 = pd.DataFrame(list(zip(Star_name, Distance, Mass, Radius, Lum)), columns=['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity'])
print(star_df_2)

star_df_2.to_csv('bright_stars.csv', index=True, index_label='id')
