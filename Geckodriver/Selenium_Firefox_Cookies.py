from pyautogui import click
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.common.keys import Keys
import pickle
from Auth_Data import instagram_login, instagram_password
# import random
# from fake_useragent import UserAgent


s = Service("C:\\Users\\HRV\\PycharmProjects\\Selen\\FirefoxDriver\\geckodriver.exe")

# useragent = UserAgent()

options = webdriver.FirefoxOptions()
options.add_argument("user-agent=Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11")

driver = webdriver.Firefox(
    service=s,
    options=options
)

try:
    # driver.get("https://www.instagram.com")
    # time.sleep(1)
    #
    # email_input = driver.find_element("name", "username")
    # email_input.clear()
    # email_input.send_keys(instagram_login)
    # # time.sleep(2)
    # # email_input.send_keys(Keys.ENTER)
    # # time.sleep(10)
    #
    # password_input = driver.find_element("name", "password")
    # password_input.clear()
    # password_input.send_keys(instagram_password)
    # time.sleep(1)
    # password_input.send_keys(Keys.ENTER)
    # time.sleep(10)

    # cookies
    # pickle.dump(driver.get_cookies(), open(f"{instagram_login}_cookies", "wb"))

    driver.get("https://www.instagram.com")
    time.sleep(2)

    for cookie in pickle.load(open(f"{instagram_login}_cookies", "rb")):
        driver.add_cookie(cookie)

    # time.sleep(0.5)
    driver.refresh()
    time.sleep(1)

    email_input = driver.find_element("id", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
    email_input.click()
    time.sleep(2)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
