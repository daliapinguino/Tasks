from selenium import webdriver
import time
# import data
import pandas as pd
import datetime
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
time_of_parsing = datetime.datetime.today().strftime('%Y-%m-%d')
try:
    driver = webdriver.Chrome(executable_path='/Users/giova/Documents/Documents/Data Mining/chromedriver',
                              options=options)
    driver.get('https://www.health.state.mn.us/diseases/coronavirus/situation.html#map1')
    time.sleep(3)

    County = []
    County_cases = []
    Death_by_county = []
    State_cases = []
    Death_by_state = []

    div_table = driver.find_elements_by_class_name('panel-heading')[10]

    div_table.click()

    time.sleep(6)

    r = driver.find_element_by_id('map')
    i = r.find_elements_by_tag_name('tr')[1:]

    for ii in i:
        County.append(ii.find_elements_by_tag_name('td')[0].text)
        County_cases.append(ii.find_elements_by_tag_name('td')[1].text)
        Death_by_county.append(ii.find_elements_by_tag_name('td')[2].text)

    print(County, County_cases, Death_by_county)

    data = pd.DataFrame({
        'State': 'Minnesota',
        'County': County,
        'Cases': County_cases,
        'Deaths': Death_by_county,
        'Date': time_of_parsing,

    })

    data.to_csv('Minnesota.csv')

except:
    print('Sorry, data is unavailable, try later... ')
