from typing import List, Any
import csv
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
Part_link=[]

Links_of_companies = []
Name_of_company = []
Google = []
Facebook = []
LinkedIn = []
Scripts = []
Pages=[]
Head=[]



url = 'https://www.google.com/'


def Search(driver):
    requests.get(url)
    search_pannel= driver.find_element_by_name('q')
    search_pannel.send_keys(input(),'\n')
    time.sleep(3)
    driver.find_element_by_xpath("//div[@class='cXedhc']//div").click()
    time.sleep(4)
    next_page = driver.find_element_by_xpath("//a[@class='fl']")
    link = next_page.get_attribute('href')
    print('Collecting place_id, please wait...')
    Part_link.append(link)



    r2 = driver.find_elements_by_class_name('dbg0pd')  # find firms
    for r3 in r2:
        r3.click()
        time.sleep(4)
        r = driver.find_element_by_id('wrkpb').get_attribute('data-pid')  # take place id from each firm
        print(r)
        Place_idies2.append(r)



def Plc_id(driver):
    link2 = ''.join(Part_link)
    part_link = link2.split('20')
    for i in range(20, 10000, 20):
        link = part_link[0]+str(i)+part_link[1]
        links.append(link)
    print('Collecting place_id, please wait...')

    for l in links:
        driver.get(l)
        time.sleep(4)
        r2 = driver.find_elements_by_class_name('dbg0pd')
        if r2 != None:
            for r3 in r2:
                r3.click()
                time.sleep(4)
                r = driver.find_element_by_id('wrkpb').get_attribute('data-pid')  # take place id from each firm
                print(r)
                Place_idies.append(r)
        else:
            quit(Plc_id(driver))

    Place_idies.extend(Place_idies2)
    print(type(Place_idies))
    p = None
    for n in Place_idies:
        if n == p:
            continue
        Filtered_place_id.append(n)
        p = n


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










def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["Name"]),
        print(line["Website"])

        Links_of_companies.append(line['Website'])
        Name_of_company.append(line['Name'])

    print('We are collecting data, please wait...')



def Search_scripts(driver):
    for Link in Links_of_companies:
        if Link != '':
            driver.get(Link)
            time.sleep(5)
            page = driver.page_source
            Pages.append(page)
        else:
            LinkedIn.append('None')
            Facebook.append('None')
            Google.append('None')

    for page in Pages:



        google=page.find('www.google-analytics.com/')
        if google !=-1:
            Google.append('Yes')
        else:
            Google.append('None')

        facebook=page.find('connect.facebook.net')
        if facebook !=-1:
            Facebook.append('Yes')
        else:
            Facebook.append('None')

        linkedin= page.find('dc.ads.linkedin.com')
        if linkedin !=-1:
            LinkedIn.append('Yes')
        else:
            LinkedIn.append('None')


    print(Name_of_company)
    print(Facebook)
    print(Google)
    print(LinkedIn)














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

    data.to_csv('File_of_firms.csv')


    with open("File_of_firms.csv") as f_obj:
        csv_dict_reader(f_obj)

    Search_scripts(driver)

    data = pd.DataFrame({
        "Name": Name2,
        'Google': Google,
        'Facebook': Facebook,
        'LinkedIn': LinkedIn

    })

    data.to_csv('File_of_scripts.csv')

if __name__ == '__main__':
    main()
