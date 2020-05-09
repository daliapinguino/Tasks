import datetime
from selenium import webdriver
import time
# import data
import pandas as pd
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
time_of_parsing=datetime.datetime.today().strftime('%Y-%m-%d')
print(time_of_parsing)
try:
    driver = webdriver.Chrome(executable_path='/Users/giova/Documents/Documents/Data Mining/chromedriver',
                                  options=options)
    driver.get('https://health.mo.gov/living/healthcondiseases/communicable/novel-coronavirus/results.php')
    time.sleep(3)
    total_cases=driver.find_elements_by_class_name('text-danger')[0]
    total_deaths=driver.find_elements_by_class_name('text-danger')[1]
    print(total_cases.text)
    print(total_deaths.text)
    County=[]
    County_cases=[]
    Death_by_county=[]
    State_cases=[total_cases.text]
    Death_by_state=[total_deaths.text]


    div_table=driver.find_element_by_class_name('panel-heading')

    div_table.click()

    time.sleep(3)
    div_body= driver.find_element_by_class_name('panel-body')
    tbody=div_body.find_element_by_tag_name('tbody')
    table = tbody.find_elements_by_tag_name('tr')
    for i in table:
        counties = i.find_elements_by_tag_name('td')[::2]
        caseses = i.find_elements_by_tag_name('td')[1::1]
        for ii in counties:
            county = ii.text
            County.append(county)
        for i2 in caseses:
            cases = i2.text
            County_cases.append(cases)
    print(County)
    print(County_cases)



    deaths=driver.find_element_by_link_text('Deaths by County')
    deaths.click()
    time.sleep(2)
    death_table=driver.find_element_by_id('collapseDeaths')
    tbody2=death_table.find_element_by_tag_name('tbody')
    tr=tbody2.find_elements_by_tag_name('tr')
    print('Deaths________________________')
    for info in tr:
        deathes=info.find_elements_by_tag_name('td')[::1]



        for ii2 in deathes:
            death= ii2.text
            Death_by_county.append(death)
    a= Death_by_county[0::2]
    b= Death_by_county[1::2]



    driver.quit()

    data = pd.DataFrame({
            'State': 'Missouri',
            'County': County,
            'Cases': County_cases,
            'Date': time_of_parsing





    })


    data.to_csv('Missouri_County_cases.csv')

    deathss= pd.DataFrame({
        'State': 'Missouri',
        'County': a,
        'Deaths': b,
        'Date': time_of_parsing
    })

    deathss.to_csv('Missouri_County_deaths.csv')

    info = pd.DataFrame({
        'State': 'Missouri',
        'date_of_mining': time_of_parsing,
        'Total_cases': State_cases,
        'Total_deaths': Death_by_state
    })
    info.to_csv('Missouri_total_info.csv')

except:
    print('Sorry, data is unavailable, try later... ')

