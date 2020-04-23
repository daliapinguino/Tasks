import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
# import data
import xlrd
import pandas as pd
import os
import datetime
time_of_parsing=datetime.datetime.today().strftime('%Y-%m-%d')

options = Options()
options.add_argument('--headless')
options.add_argument("download.default_directory=/Users/giova/Documents/Data Mining/COVID-19")#change path what you want

driver = selenium.webdriver.Chrome('/Users/giova/Documents/Data Mining/chromedriver', options=options)

driver.get('https://www.dshs.state.tx.us/coronavirus/TexasCOVID19CaseCountData.xlsx')
time.sleep(5)
df = pd.read_excel('CaseCountData.xlsx')
df.insert(1,'State','Texas')
df.insert(5,'Date',time_of_parsing)
df.to_csv('Texas_cases.csv')
os.remove('CaseCountData.xlsx')