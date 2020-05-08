import datetime
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options

date_parsing = datetime.datetime.today().strftime('%Y-%m-%d')
obj = []
left_list = []
text = []


def RunBrowser(driver):
    driver.get('https://sc-dhec.maps.arcgis.com/apps/opsdashboard/index.html#/3732035614af4246877e20c3a496e397')


def Scraping(driver):
    # try:
        full=driver.find_element_by_tag_name('full-container')
        featureList = full.find_element_by_class_name('feature-list')

        for div in featureList.find_elements_by_tag_name('span'):
            c = div.find_elements_by_tag_name("strong")
            for d in c:
                text.append(d.text)
        print(text)

        object = pd.DataFrame({
            'STATE': 'South Carolina',
            'COUNTY': text[0::5],
            'COUNT': text[2::5],
            'DEATHS': text[3::5],
            'DATE': date_parsing
        })

        object.to_csv('South_Carolina.csv')

        driver.out
    # except:
    #     print('Try later...')
    #
    #

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
