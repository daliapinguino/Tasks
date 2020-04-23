import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
# import data
import pandas as pd
import os
import datetime
time_of_parsing=datetime.datetime.today().strftime('%Y-%m-%d')

options = Options()
options.add_argument('--headless')
options.add_argument("download.default_directory=/Users/giova/Documents/Data Mining/COVID-19")#change path what you want

driver = selenium.webdriver.Chrome('/Users/giova/Documents/Data Mining/chromedriver', options=options)

driver.get('https://www.health.nd.gov/diseases-conditions/coronavirus/north-dakota-coronavirus-cases')
time.sleep(5)

County=[]
County_cases=[]
Death_by_county=[]
State_cases=[]
Death_by_state=[]

div_table=driver.find_elements_by_class_name('highcharts-button-symbol')[5]
div_table.click()

# time.sleep(1)
menu=driver.find_element_by_class_name('highcharts-contextmenu')
tbody=menu.find_elements_by_class_name('highcharts-menu-item')[5]
tbody.click()
time.sleep(10)
df = pd.read_csv("chart.csv")
# df['State']='North Dakota'
df.insert(0,'State','North Dakota')
df["Date"] = time_of_parsing
df.to_csv("North_Dakota_cases.csv", index=False)
os.remove("chart.csv")

