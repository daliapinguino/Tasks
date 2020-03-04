from typing import List, Any
import csv
import requests
import simplejson as json
import pandas as pd
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from itertools import groupby

APIKEY = "AIzaSyBmODL4WJ5xSxzM5eB6rhe36FECN-k6ydQ"
Name = []
Opening_hours = []
Website = []
Name_for_scripts = []
Phone = []
Address = []
Rating = []
Links_of_companies = []
Name_of_company = []
Google = []
Facebook = []
LinkedIn = []




url = 'https://www.google.com/'


def Search_and_get_link(driver):

    requests.get(url)
    search_pannel = driver.find_element_by_name('q')
    search_pannel.send_keys(input(), '\n')
    time.sleep(3)
    driver.find_element_by_xpath("//div[@class='cXedhc']//div").click()
    time.sleep(4)
    next_page = driver.find_elements_by_xpath("//a[@class='fl']")
    link_of_page = next_page[0].get_attribute('href')
    print(link_of_page)
    return (link_of_page)


def mining_links(driver, first_link):
    Each_page_links = []
    part_link = first_link.split('20')
    print(part_link)
    for i in range(0, 10000, 20):
        link = part_link[0] + str(i) + part_link[1]
        print(link)
        driver.get(link)
        time.sleep(4)
        try:
            driver.find_element_by_class_name("dbg0pd")!= None
            Each_page_links.append(link)
        except NoSuchElementException:
            break
    return Each_page_links

def get_place_id(driver,each_links):
    Filtered_place_id=[]
    Place_ides=[]
    for link in each_links:
        driver.get(link)
        time.sleep(4)
        find_place_field = driver.find_elements_by_class_name('dbg0pd')
        for place_field in find_place_field:
            place_field.click()
            time.sleep(4)
            get_place_id2 = driver.find_element_by_id('wrkpb').get_attribute('data-pid')  # take place id from each firm
            print(get_place_id2)
            Place_idies.append(get_place_id2)
    p = None
    for doubles_in_place_id in Place_idies:
        if doubles_in_place_id == p:
            continue
        Filtered_place_id.append(doubles_in_place_id)
        p = doubles_in_place_id
    return (Filtered_place_id)

def find_all_information_of_firms(requests, filtered_place_id):
    for one_place_id in filtered_place_id:
        APIKEY2 = 'AIzaSyClgt6mOSkM_OFIGmYlAyvnS8gUWlA4H8Y'
        fields = 'name,formatted_address,international_phone_number,rating,opening_hours/weekday_text,website'
        url_google_api = "https://maps.googleapis.com/maps/api/place/details/json?&place_id={place_id}&fields={fields}&key={APIKEY}".format(
            place_id=one_place_id, fields=fields, APIKEY=APIKEY2)
        data_of_each_place = requests.get(url_google_api)
        json_file_of_data_of_each_place = json.loads(data_of_each_place.text)

        results_in_json_file = json_file_of_data_of_each_place.get('result')

        open_hours = results_in_json_file.get('opening_hours')
        if open_hours is None:
            Opening_hours.append('None')
        else:
            Opening_hours.append(open_hours.get('weekday_text'))

        Phone.append(results_in_json_file.get('international_phone_number'))
        Address.append(results_in_json_file.get('formatted_address'))
        Website.append(results_in_json_file.get('website'))
        Rating.append(results_in_json_file.get('rating'))
        Name_for_scripts.append(results_in_json_file.get('name'))


def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["Name"]),
        print(line["Website"])

        Links_of_companies.append(line['Website'])
        Name_of_company.append(line['Name'])

    print('We are collecting data, please wait...')


def Search_scripts(driver):
    Pages=[]
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

        google = page.find('www.google-analytics.com/')
        if google != -1:
            Google.append('Yes')
        else:
            Google.append('None')

        facebook = page.find('connect.facebook.net')
        if facebook != -1:
            Facebook.append('Yes')
        else:
            Facebook.append('None')

        linkedin = page.find('dc.ads.linkedin.com')
        if linkedin != -1:
            LinkedIn.append('Yes')
        else:
            LinkedIn.append('None')

    print(Name_of_company)
    print(Facebook)
    print(Google)
    print(LinkedIn)

def write_in_csv_data_of_each_place(pd):
    data = pd.DataFrame({
        'Name': Name_for_scripts,
        'Address': Address,
        'Phone': Phone,
        'Website': Website,
        'Opening hours': Opening_hours,
        'Rating': Rating

    })
    data.to_csv('File_of_firms.csv')


def write_in_csv_scripts_of_each_place(pd):
    data = pd.DataFrame({
        "Name": Name_for_scripts,
        'Google': Google,
        'Facebook': Facebook,
        'LinkedIn': LinkedIn

    })
    data.to_csv('File_of_scripts.csv')



def main():
    options = Options()
    options.add_argument("--headless")
    driver = selenium.webdriver.Chrome('/Users/gio/PycharmProjects/untitled8/chromedriver', options=options)

    driver.get(url)
    print('Enter you searching request below(s.a."dentists in california, law firms in Washington": ')
    first_link = Search_and_get_link(driver)
    each_links = mining_links(driver, first_link)
    filtered_place_id=get_place_id(driver,each_links)
    find_all_information_of_firms(requests,filtered_place_id)
    write_in_csv_data_of_each_place(pd)




    with open("File_of_firms.csv") as f_obj:
        csv_dict_reader(f_obj)

    Search_scripts(driver)
    write_in_csv_scripts_of_each_place(pd)



if __name__ == '__main__':
    main()
