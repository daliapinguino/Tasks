from typing import List, Any

import requests
import simplejson as json
import pandas as pd
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
from itertools import groupby

APIKEY = "AIzaSyBmODL4WJ5xSxzM5eB6rhe36FECN-k6ydQ"
Place_id = []
Name = []
Opening_hours = []
Website = []
Name2 = []
Phone = []
Address = []
Rating = []
links = []
Links = []
Place_idies = []
Place_idies2 = []
Filtered_place_id = []


url = 'https://www.google.by/search?hl=ru&q=law+firms+in+massachusetts&npsic=0&rflfq=1&rlha=0&rllag=42362515,-71081908,1878&tbm=lcl&ved=2ahUKEwjIlo_kueDnAhXCwsQBHTcMAg4QjGp6BAgLEDk&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m5!1u15!2m2!15m1!1shas_1wheelchair_1accessible_1entrance!4e2!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:;mv:[[42.6914696,-70.8312938],[41.837384,-71.8580018]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2'


def Search(driver):
    driver.get(url)
    r2 = driver.find_elements_by_class_name('dbg0pd')  # find firms
    for r3 in r2:
        r3.click()
        time.sleep(4)
        r = driver.find_element_by_id('wrkpb').get_attribute('data-pid')  # take place id from each firm
        print(r)
        Place_idies2.append(r)



def Plc_id(driver):
    for i in range(20, 380, 20):
        link = "https://www.google.by/search?q=law+firms+in+massachusetts&hl=ru&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=WpFOXs3UPIvOrgSivbS4Bg&start=" + str(
            i) + "&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCJkC"

        links.append(link)
        print(link)

    for l in links:
        driver.get(l)
        time.sleep(4)
        r2 = driver.find_elements_by_class_name('dbg0pd')  # find firms
        for r3 in r2:
            r3.click()
            time.sleep(4)
            r = driver.find_element_by_id('wrkpb').get_attribute('data-pid')  # take place id from each firm
            print(r)
            Place_idies.append(r)

    Place_idies.extend(Place_idies2)
    print(type(Place_idies))
    p = None
    for n in Place_idies:
        if n == p:
            continue
        Filtered_place_id.append(n)
        p = n
        # Filtered_place_id = [ii for n, ii in enumerate(Place_idies) if ii not in Place_idies[:n]]

    for plc in Filtered_place_id:
        APIKEY2 = 'AIzaSyClgt6mOSkM_OFIGmYlAyvnS8gUWlA4H8Y'
        fields = 'name,formatted_address,international_phone_number,rating,opening_hours/weekday_text,website'
        url2 = "https://maps.googleapis.com/maps/api/place/details/json?&place_id={place_id}&fields={fields}&key={APIKEY}".format(
            place_id=plc, fields=fields, APIKEY=APIKEY2)
        r2 = requests.get(url2)
        res = json.loads(r2.text)

        results2 = res.get('result')

        open_hours = results2.get('opening_hours')
        if open_hours is None:
            Opening_hours.append('None')
        else:
            Opening_hours.append(open_hours.get('weekday_text'))

        Phone.append(results2.get('international_phone_number'))
        Address.append(results2.get('formatted_address'))
        Website.append(results2.get('website'))
        Rating.append(results2.get('rating'))
        Name2.append(results2.get('name'))


def main():
    options = Options()
    options.add_argument("--headless")
    driver = selenium.webdriver.Chrome('/Users/gio/PycharmProjects/untitled8/chromedriver', options=options)

    driver.get(url)
    Search(driver)
    Plc_id(driver)

    data = pd.DataFrame({
        'Name': Name2,
        'Address': Address,
        'Phone': Phone,
        'Website': Website,
        'Opening hours': Opening_hours,
        'Rating': Rating

    })

    data.to_csv('Law_firms.csv')


if __name__ == '__main__':
    main()
