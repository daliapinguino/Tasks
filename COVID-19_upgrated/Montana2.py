import datetime
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options

date_parsing = datetime.datetime.today().strftime('%Y-%m-%d')
obj = []
left_list = []
text = []

try:
    def RunBrowser(driver):
        driver.get('https://montana.maps.arcgis.com/apps/opsdashboard/index.html#/6a55cf30ec4e4a65a682021b7db3dd91')


    def Scraping(driver):
        try:
            featureList = driver.find_element_by_class_name('feature-list')

            for div in featureList.find_elements_by_tag_name('span'):
                c = div.find_elements_by_tag_name("strong")
                for d in c:
                    text.append(d.text)

            object = pd.DataFrame({
                'STATE': 'Montana',
                'COUNTY': text[0::5],
                'COUNT': text[1::5],
                'DEATHS': 'N/A',
                'DATE': date_parsing
            })

            object.to_csv('Montana2.csv')


        except:
            print('Try later...')



    def Main():
        # try:

        options = Options()
        options.add_argument('headless')
        driver = webdriver.Chrome(executable_path='/Users/giova/Documents/Documents/Data Mining/chromedriver',
                                  options=options)

        RunBrowser(driver)
        time.sleep(30)
        Scraping(driver)


    Main()

except:
    print('Sorry, data is unavailable, try later... ')
