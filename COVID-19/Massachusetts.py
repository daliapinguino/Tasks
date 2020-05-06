from selenium import webdriver
import time
import zipfile
import tkinter
import camelot
# import data
import pandas as pd
from selenium.webdriver.chrome.options import Options
import datetime
import os

date_parsing = datetime.datetime.today().strftime('%Y-%M-%d')
link_date = datetime.datetime.today().strftime('%B-%d')
pdf_date = datetime.datetime.today().strftime('%m-%d')
now = datetime.datetime.now()
current_time=now.strftime("%H:%M")
print(current_time)
a=datetime.datetime='16:'




def Parse():
    prefs = {"download.default_directory": "/Users/giova/Documents/Documents/Data Mining/COVID-19"}
    options = Options()
    options.add_argument('--headless')
    # options.add_argument("download.default_directory=/Users/giova/Documents/Documents/Data Mining/COVID-19")#change path what you want
    options.add_experimental_option('prefs', prefs)
    # options.add_experimental_option('prefs', {
    # "download.default_directory=/Users/giova/Documents/Documents/Data Mining/COVID-19"
    # "download.prompt_for_download": False, #To auto download the file
    # "download.directory_upgrade": True,
    # "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
    # })
    driver = webdriver.Chrome('/Users/giova/Documents/Documents/Data Mining/chromedriver', options=options)

    driver.get('https://www.mass.gov/info-details/covid-19-response-reporting')

    time.sleep(5)

    div = driver.find_element_by_partial_link_text('COVID-19 Raw Data')
    download = div.get_attribute('href')
    driver.get(download)
    time.sleep(10)
    driver.quit()


def Csv():
    with zipfile.ZipFile(f'COVID-19%20Dashboard%20Files%2005-05-2020.zip') as myzip:
        myzip.extract('County.csv')

    data = pd.read_csv('County.csv')[-16:]
    output = pd.DataFrame({
        'State': 'Massachusetts',
        'County': data['County'],
        'Cases': data['Count'],
        'Death': data['Deaths'],
        'Date': date_parsing

    })
    output.to_csv('Massachusetts.csv')


    os.remove('COVID-19%20Dashboard%20Files%2005-05-2020.zip')
    os.remove('County.csv')


def main():
    if current_time >= a:

        Parse()
        Csv()


if __name__ == '__main__':
    main()
