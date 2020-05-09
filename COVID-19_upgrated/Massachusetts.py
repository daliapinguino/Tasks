from selenium import webdriver
import time
import zipfile
# import data
import pandas as pd
from selenium.webdriver.chrome.options import Options
import datetime
import os

date_parsing = datetime.datetime.today().strftime('%Y-%m-%d')
link_date = datetime.datetime.today().strftime('%B-%d')
pdf_date = datetime.datetime.today().strftime('%m-%d')
now = datetime.datetime.now()
current_time = now.strftime("%H:%M")
print(current_time)
a = datetime.datetime = '16:'
pdf_date.split('-')
right_data=int(pdf_date[4])-1


try:
    def Parse():
        prefs = {"download.default_directory": "/Users/giova/Documents/Documents/Data Mining/Tesr"}
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
        driver = webdriver.Chrome(executable_path='/Users/giova/Documents/Documents/Data Mining/chromedriver',
                                  options=options)

        driver.get('https://www.mass.gov/info-details/covid-19-response-reporting')

        time.sleep(5)

        div = driver.find_element_by_partial_link_text('COVID-19 Raw Data')
        download = div.get_attribute('href')
        driver.get(download)
        time.sleep(10)
        driver.quit()


    def Csv():
        with zipfile.ZipFile(f'COVID-19%20Dashboard%20Files%20{pdf_date[0:3]+str(0)+str(right_data)}-2020.zip') as myzip:
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

        os.remove(f'COVID-19%20Dashboard%20Files%20{pdf_date[0:3]+str(0)+str(right_data)}-2020.zip')
        os.remove('County.csv')


    def main():
        if current_time >= a:
            Parse()
            Csv()
except:
    print('Sorry, data is unavailable, try later... ')



if __name__ == '__main__':
    main()
