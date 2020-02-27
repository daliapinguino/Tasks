import selenium
from selenium.webdriver import Chrome
import pandas as pd
import csv
import time
from selenium.webdriver.chrome.options import Options

Links = []
Name = []
Google = []
Facebook = []
LinkedIn = []
Scripts = []
Pages=[]
Head=[]


def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["Name"]),
        print(line["Website"])

        Links.append(line['Website'])
        Name.append(line['Name'])





def Search_scripts(driver):
    for Link in Links:
        if Link !='':
            driver.get(Link)
            time.sleep(5)
            page = driver.page_source
            Pages.append(page)
        else:
            LinkedIn.append('None')
            Facebook.append('None')
            Google.append('None')

    for page in Pages:

        print(type(Pages))
        head = page.split('</head>')


        head2=head.pop(0)
        print(head2)
        print(type(head2))

        google=head2.find('www.google-analytics.com/')
        if google !=-1:
            Google.append('Yes')
        else:
            Google.append('None')

        facebook=head2.find('connect.facebook.net')
        if facebook !=-1:
            Facebook.append('Yes')
        else:
            Facebook.append('None')

        linkedin= head2.find('dc.ads.linkedin.com')
        if linkedin !=-1:
            LinkedIn.append('Yes')
        else:
            LinkedIn.append('None')


    print(Name)
    print(Facebook)
    print(Google)
    print(LinkedIn)



if __name__ == "__main__":
    with open("Law_firms.csv") as f_obj:
        csv_dict_reader(f_obj)
    options = Options()
    options.add_argument("--headless")
    driver = selenium.webdriver.Chrome('/Users/gio/PycharmProjects/untitled8/chromedriver', options=options)

    Search_scripts(driver)

    data = pd.DataFrame({
        "Name": Name,
        'Google': Google,
        'Facebook': Facebook,
        'LinkedIn': LinkedIn

    })

    data.to_csv('Law_scripts.csv')
