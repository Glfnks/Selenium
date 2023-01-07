from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
import pickle
import random
from Auth_data import vk_phone, vk_password
# from fake_useragent import UserAgent


s = Service("C:\\Users\\HRV\\PycharmProjects\\Selen\\ChromeDriver\\chromedriver.exe")

# useragent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11")

driver = webdriver.Chrome(
    service=s,
    options=options
)

try:
    driver.get("https://vk.com/")
    time.sleep(1)

    email_input = driver.find_element("id", "index_email")
    email_input.clear()
    email_input.send_keys(vk_phone)

    password_input = driver.find_element("id", "index_pass")
    password_input.clear()
    password_input.send_keys(vk_password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(50)

    # cookies
    pickle.dump(driver.get_cookies(), open(f"{vk_phone}_cookies", "wb"))

    # driver.get("https://vk.com/")
    # time.sleep(1)
    #
    # for cookie in pickle.load(open(f"{vk_phone}_cookies", "rb")):
    #     driver.add_cookie(cookie)
    #
    # # time.sleep(1)
    # # driver.refresh()
    # # time.sleep(5)


except Exception as ex:
    print(ex)
# finally:
#     driver.close()
#     driver.quit()
