import selenium
from selenium.webdriver import Chrome
import time, sys, os
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


os.mkdir('Screenshorts')


def readJson(driver):
    with open('Data.json', 'r') as file:
        file_name = json.load(file)

        print(file_name)

        print(type(file_name))
        for key, values in file_name.items():
            print(key, values)



            os.chdir("/Users/gio/PycharmProjects/untitled21/venv/Screenshorts")
            os.mkdir(key)

            for value in values:

                print(value)
                driver.get('http://' + value)
                os.chdir('/Users/gio/PycharmProjects/untitled21/venv/Screenshorts/' + key)
                driver.save_screenshot(value + '.png')



def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1280,720")
    driver = selenium.webdriver.Chrome('/Users/gio/PycharmProjects/untitled8/chromedriver', options=options)

    readJson(driver)




if __name__ == '__main__':
    main()
