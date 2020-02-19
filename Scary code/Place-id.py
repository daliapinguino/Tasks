import requests
import selenium
from selenium.webdriver import Chrome
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pickle

Links = []
Place_idies=[]
Place_idies2=[]
url = 'https://www.google.by/search?q=law+firms+massachusetts&npsic=0&rflfq=1&rlha=0&rllag=42358302,-71059628,78&tbm=lcl&ved=2ahUKEwjd6KvS2dvnAhXU5KYKHTk2DjEQjGp6BAgLEDk&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m5!1u15!2m2!15m1!1shas_1wheelchair_1accessible_1entrance!4e2!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:;mv:[[42.367024199999996,-71.03914],[42.3488452,-71.1079729]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2'

url2 = 'https://www.google.by/search?q=law%20firms%20massachusetts&npsic=0&rflfq=1&rlha=0&rllag=42358302,-71059628,78&tbm=lcl&ved=2ahUKEwjd6KvS2dvnAhXU5KYKHTk2DjEQjGp6BAgLEDk&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&rldoc=1&rlst=f#rldoc=1&rlfi=hd:;si:;mv:[[42.3752478,-71.0320742],[42.300169,-71.2308279]];start:'


def Search(driver):
    r2 = driver.find_elements_by_class_name('dbg0pd')  # find firms
    for r3 in r2:
        r3.click()
        time.sleep(2)
        r = driver.find_element_by_id('wrkpb').get_attribute('data-pid')  # take place id from each firm
        print(r)
        Place_idies2.append(r)



def scraping(driver):
    r77 = driver.find_elements_by_class_name('fl')[0:10]
    for r78 in r77:
        f21 = r78.get_attribute("href")

        f21: {
            'href': link
        }

        print(f21)

        Links.append(f21)

    del Links[0]



def Plc_id(driver):

    Link=["https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=20&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCJkC",
"https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=40&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCJsC",
"https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=60&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCJ0C",
"https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=80&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCJ8C",
"https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=100&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCKEC",
"https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=120&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCKMC",
"https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=140&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCKUC",
"https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=160&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCKcC",
"https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=180&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCKkC",
"https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=200&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCKkC",
"https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=220&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCKkC",
"https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=240&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCKkC",
"https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=u7ZNXu_qFuzzqwGCyIToCQ&start=260&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwivtJKM1d7nAhXs-SoKHQIkAZ0Q8tMDCKkC"
]


    for l in Link:
            driver.get(l)
            time.sleep(3)
            r2 = driver.find_elements_by_class_name('dbg0pd')  # find firms
            for r3 in r2:
                r3.click()
                time.sleep(3)
                r = driver.find_element_by_id('wrkpb').get_attribute('data-pid')  # take place id from each firm
                print(r)
                Place_idies.append(r)


# def Pages(driver):
#     driver.get('https://www.google.by/search?q=law+firms+massachusetts&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&ei=O6RNXv2qD-7HrgTWzJbABA&start=180&sa=N&rllag=42358302,-71059628,78&rlha=0&rlst=f&ved=0ahUKEwi9tOS5w97nAhXuo4sKHVamBUgQ8tMDCKkC')
#     time.sleep(3)
#     r80 = driver.find_elements_by_class_name('fl')[-2:-5]
#     for r90 in r80:
#         f24 = r90.get_attribute('href')
#
#         f24: {
#             'href':link
#         }
#
#         print(f24)

# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='dbg0pd']")))
# r9 = driver.find_elements_by_class_name('dbg0pd')
# for r7 in r9:
#     r7.click()
#     time.sleep(3)
#     r8 = driver.find_element_by_id('wrkpb').get_attribute('data-pid')# take each place_id
#     print(r8)


def main():
    # opts = Options()
    # opts.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0")
    driver = selenium.webdriver.Chrome('/Users/gio/PycharmProjects/untitled8/chromedriver')

    driver.get(url)
    Search(driver)
    scraping(driver)
    data = pd.DataFrame({
        'Place_id': Place_idies+Place_idies2
    })

    data.to_csv('Links_pages.csv')
    Plc_id(driver)



if __name__ == '__main__':
    main()
