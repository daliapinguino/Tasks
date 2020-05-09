import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
# import data
import pandas as pd
import os
import datetime
import pyperclip

time_of_parsing = datetime.datetime.today().strftime('%Y-%m-%d')

options = Options()
options.add_argument('--headless')
# options.add_argument("download.default_directory=/Users/giova/Documents/Data Mining/COVID-19")#change path what you want

driver = webdriver.Chrome(executable_path='/Users/giova/Documents/Documents/Data Mining/chromedriver',
                              options=options)
try:

    driver.get('https://looker-dashboards.ok.gov/embed/dashboards/44')
    time.sleep(20)

    div_table = driver.find_elements_by_class_name('header-menu')[0]

    div_table.click()
    time.sleep(2)
    button = driver.find_elements_by_id('eName')[1]
    button.click()
    time.sleep(3)
    county = pyperclip.paste()
    div_table = driver.find_elements_by_class_name('header-menu')[1]

    div_table.click()
    time.sleep(2)
    button = driver.find_elements_by_id('eName')[1]
    button.click()
    time.sleep(3)
    county_cases = pyperclip.paste()
    div_table = driver.find_elements_by_class_name('header-menu')[2]

    div_table.click()
    time.sleep(2)
    button = driver.find_elements_by_id('eName')[1]
    button.click()
    time.sleep(3)
    deaths = pyperclip.paste()
    County = county.replace('\n', ' ').split()
    County_cases = county_cases.replace('\n', ' ').split()
    Death_by_county = deaths.replace('\n', ' ').split()
    print(County[6::])
    print(County_cases[6::])
    print(Death_by_county[6::])

    data = pd.DataFrame({
        'State': 'Oklahoma',
        'County': County,
        'Cases': County_cases,
        'Deaths': Death_by_county,
        'Date': time_of_parsing
    })

    driver.quit()
    data.to_csv("Oklahoma_cases.csv")

except:
    print('Sorry, data is unavailable, try later... ')

