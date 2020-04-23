from selenium import webdriver
import time
# import data
import pandas as pd
import datetime

time_of_parsing=datetime.datetime.today().strftime('%Y-%m-%d')

driver = webdriver.Chrome('/Users/giova/Documents/Data Mining/chromedriver')
driver.get('https://www.michigan.gov/coronavirus/0,9753,7-406-98163-520743--,00.html')

County_cases=[]
Death_by_county=[]
State_cases=[]
Death_by_state=[]
County=[]

div_table=driver.find_element_by_class_name('fullContent')
info_table=div_table.find_element_by_tag_name('tbody')
datas =info_table.find_elements_by_tag_name('tr')

for info in datas:
    county_info=info.find_elements_by_tag_name('td')[0].text
    cases_info=info.find_elements_by_tag_name('td')[1].text
    death_info=info.find_elements_by_tag_name('td')[2].text
    # print(county_info, cases_info,death_info)
    County_cases.append(cases_info)
    Death_by_county.append(death_info)
    County.append(county_info)


driver.quit()

data = pd.DataFrame({
        'State': 'Michigan',
        'County': County,
        'Cases': County_cases,
        'Deaths': Death_by_county,
        'Date': time_of_parsing,

})


data.to_csv('Michigan.csv')
