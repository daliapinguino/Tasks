from selenium import webdriver
import pandas as pd

urlLinkedIn = 'https://www.linkedin.com/'
urlSearch = 'https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%2210667%22%2C%221441%22%5D&facetPastCompany=%5B%2210667%22%2C%221441%22%5D&origin=FACETED_SEARCH'

Name = []
URL = []
Link = []
Job = []

def authorization(driver):
    driver.get(urlLinkedIn)
    driver.find_element_by_class_name('nav__button-secondary').click()
    driver.find_element_by_id('username').send_keys('daliapinguino21@gmail.com')
    driver.find_element_by_id('password').send_keys('Gio21Vanni96')
    driver.find_element_by_class_name('btn__primary--large').click()

def mining(driver):
    driver.get(urlSearch)
    ulPageCounter = driver.find_elements_by_class_name('artdeco-pagination__indicator')
    # liPageCounter = int(ulPageCounter[0].find_element_by_tag_name('span').text)

    counter = 0

    for i in range(1, 10):
        driver.get(urlSearch + '&page=' + str(i))

        listPeoples = driver.find_elements_by_class_name('search-result__wrapper')

        if counter < 10:
            for people in listPeoples:
                peopleName = people.find_element_by_class_name('actor-name').text

                if peopleName != 'Участник LinkedIn':
                    Name.append(peopleName)
                    Job.append(people.find_element_by_class_name('subline-level-1').text)


                    link =people.find_element_by_class_name('search-result__result-link').get_attribute('href')
                    Link.append(link)
                    counter = counter + 1
        else:
            break

def main():
    driver = webdriver.Chrome('/Users/gio/PycharmProjects/untitled8/chromedriver')
    authorization(driver)
    mining(driver)


    data = pd.DataFrame({
        'Name': Name,
        'Job': Job,
        'Links': Link,
    })

    print(data)
    data.to_csv(data)
if __name__ == '__main__':
    main()
