from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests 

# List of Bright Stars
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

#Getting page
page = requests.get(START_URL)

temp_list=[]

soup=BeautifulSoup(page.text, "html.parser")
star_table = soup.find_all("table", attrs={"class", "wikitable sortable"})
total_table = len(star_table)

table_rows = star_table[1].find_all('tr')

for rows in table_rows:
    td = rows.find_all('td')
    row = [i.text.rstrip()for i in td]
    temp_list.append(row)

Star_name=[]
Distance=[]
Mass=[]
Radius=[]
print (temp_list)

for i in range(i, len(temp_list)):
    Star_name.append(temp_list [i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

headers = ['Star_name', 'Distance', 'Mass', 'Radius']

star_df_2 = pd.DataFrame(list(zip(Star_name, Distance, Mass, Radius)), columns=['Star_name', 'Distance', 'Mass', 'Radius'])
print(star_df_2)

star_df_2.to_csv('dwarf_stars.csv', index=True, index_label='id')
