import requests
import json
import datetime
import os
import pandas as pd

# import selenium
# from selenium import webdriver
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
time_of_parsing = datetime.datetime.today().strftime('%Y-%m-%d')
Dict = []
Full_name = []
Short_name = []
County = []
Cases = []
Deaths = []
State = []

# options = Options()
# options.add_argument('--headless')
# driver = selenium.webdriver.Chrome('/Users/giova/Documents/Data Mining/chromedriver',options=options)
# driver.get('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')
# table=driver.find_elements_by_class_name('wikitable')[0]
# tbody=table.find_element_by_tag_name('tbody')
#
# th=tbody.find_elements_by_tag_name('tr')
# for i in th:
#     Full_name.append(i.find_element_by_tag_name('th').text)
#
#     Short_name.append(i.find_elements_by_tag_name('td')[0].text)
# driver.quit()
#
# counter=0
# for counter in range(3194):


for info in requests.get('https://www.cdc.gov/coronavirus/2019-ncov/json/county-map-data.json').json()['data']:
    Dict.append(info)

with open('All_states.json', 'w') as fp:
    json.dump(Dict, fp, )

with open('All_states.json', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    State.append(distro['state'])
    County.append(distro['county_name'])
    Cases.append(distro['cases'])
    Deaths.append(distro['deaths'])

data = pd.DataFrame({
    'State': State,
    'County': County,
    'Cases': Cases,
    'Deaths': Deaths,
    'Date_of_minig': time_of_parsing
})

data.to_csv('All_states.csv')
os.remove('All_states.json')
