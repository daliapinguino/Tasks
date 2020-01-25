from selenium import webdriver
import requests
import pandas as pd

url = 'https://ballotpedia.org/Main_Page'

Pages = []
Name = []
BirthPlace = []
GradYear = []


def search(driver):
    searcher = driver.find_element_by_id('searchInput')
    searcher.send_keys("Bachelor's Stanford University\n")


def links_of_bach(driver):
    links = driver.find_elements_by_xpath("//ul[@class = 'mw-search-results']//a")

    for f in links:
        link = f.get_attribute("href")

        link = {
            'href': link
        }

        Pages.append(link)


def collect_info(driver):
    counter = 0

    for f in Pages:
        if counter < 10:
            driver.get(f['href'])

            Name.append(driver.find_element_by_xpath("//h1[@id = 'firstHeading']//span").text)

            value = driver.find_elements_by_xpath("//div[@class = 'widget-value']//p")

            for f in value:
                str_ = f.text

                if str_.find('Stanford University') != -1:
                    if str_.split()[-1].isdigit():
                        GradYear.append(str_.split()[-1])
                    else:
                        GradYear.append('NONE')

            row = driver.find_elements_by_class_name("widget-row")

            text = []

            for f in row:
                text.append(f.text)

            if text.count("Personal") == 1:
                if text.count("Contact") == 1:
                    BirthPlace.append(text[-3].split('\n')[-1])
                else:
                    BirthPlace.append(text[-1].split('\n')[-1])
            else:
                BirthPlace.append("NONE")

            counter = counter + 1

        else:
            break


def main():
    driver = webdriver.Chrome('/Users/gio/PycharmProjects/untitled8/chromedriver')
    driver.get(url)

    search(driver)
    links_of_bach(driver)
    collect_info(driver)

    data = pd.DataFrame({
        'Name': Name,
        'Birthplace': BirthPlace,
        'Graduation': GradYear,
    })

    print(data)
    data.to_csv("data.csv")


if __name__ == "__main__":
    main()