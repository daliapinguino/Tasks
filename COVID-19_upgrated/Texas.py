import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
# import data

import pandas as pd
import os
import datetime

time_of_parsing = datetime.datetime.today().strftime('%Y-%m-%d')
print(time_of_parsing)
options = Options()
options.add_argument('--headless')
options.add_argument(
    "download.default_directory=/Users/giova/Documents/Data Mining/COVID-19")  # change path what you want
try:
    driver = webdriver.Chrome(executable_path='/Users/giova/Documents/Documents/Data Mining/chromedriver',
                              options=options)

    driver.get('https://www.dshs.state.tx.us/coronavirus/TexasCOVID19CaseCountData.xlsx')
    time.sleep(5)
    df = pd.read_excel('CaseCountData.xlsx')
    df.insert(1, 'State', 'Texas')
    df.insert(4, 'Date', time_of_parsing)
    df.to_csv('Texas.csv')
    os.remove('CaseCountData.xlsx')


except:
    print('Sorry, data is unavailable, try later... ')

