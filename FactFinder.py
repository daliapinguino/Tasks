import selenium
from selenium.webdriver import Chrome
import pandas as pd

URL = "https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml"

Countys = ['Bristol County, Rhode Island', 'Kent County, Rhode Island', 'Newport Conty, Rhode Island', 'Providence Island, Rhode Island', 'Washington County, Rhode Island']

Population = []
Median_age = []
Companies = []
Place_name_ = []

def search(driver, url):
    driver.find_element_by_id("cfsearchtextboxmain").send_keys(url, ' \n')

def scraping(driver):
    driver.implicitly_wait(10)
    driver.find_elements_by_xpath("//div[@id = 'leftnav']//a")[-1].click()
    driver.implicitly_wait(10)

    Place_name_.append(driver.find_element_by_xpath("//div[@id = 'cf-content']//h2[@id = 'geo-name']").text)
    Population.append(driver.find_elements_by_xpath("//table//tbody//tr//td[@class = 'ng-binding']")[1].text)
    Median_age.append(driver.find_elements_by_xpath("//table//tbody//tr//td[@class = 'ng-binding ng-scope']")[2].text)
    Companies.append(driver.find_elements_by_xpath("//table//tbody//tr//td[@class = 'ng-binding ng-scope']")[4].text)

def main():
    driver = selenium.webdriver.Chrome('/Users/gio/PycharmProjects/untitled8/chromedriver')
    driver.get(URL)

    for County in Countys:
        search(driver, County)
        scraping(driver)
        driver.get(URL)

    data = pd.DataFrame({
        'Placename': Place_name_,
        'Population': Population,
        'Median_age': Median_age,
        'Companies': Companies
    })

    print(data)
    data.to_csv('data_of_countys_RhIsl.csv')

if __name__ == '__main__':
    main()



