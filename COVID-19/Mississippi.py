from selenium import webdriver
import time
# import data
import pandas as pd
import datetime
time_of_parsing=datetime.datetime.today().strftime('%Y-%m-%d')
driver = webdriver.Chrome('/Users/giova/Documents/Data Mining/chromedriver')
driver.get('https://msdh.ms.gov/msdhsite/_static/14,0,420.html#caseTable')
time.sleep(3)

County=[]
County_cases=[]
Death_by_county=[]
State_cases=[]
Death_by_state=[]

div_table=driver.find_element_by_id('msdhTotalCovid-19Cases')

div_body= div_table.find_element_by_tag_name('tbody')
counties=div_body.find_elements_by_tag_name('td')[0::4]
cases=div_body.find_elements_by_tag_name('td')[1::4]
deaths=div_body.find_elements_by_tag_name('td')[2::4]
for i in counties:
    County.append(i.text)
for ii in cases:
    County_cases.append(ii.text)
for iii in deaths:
    Death_by_county.append(iii.text)




driver.quit()

data = pd.DataFrame({
        'State': 'Mississippi',
        'County': County,
        'Cases': County_cases,
        'Deaths': Death_by_county,
        'Date': time_of_parsing,

})


data.to_csv('Mississippi.csv')
