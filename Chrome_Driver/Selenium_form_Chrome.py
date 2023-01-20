from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
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
    email_input.send_keys("**********")
    # time.sleep(2)
    # email_input.send_keys(Keys.ENTER)
    # time.sleep(10)

    password_input = driver.find_element("id", "index_pass")
    password_input.clear()
    password_input.send_keys("*************")
    time.sleep(1)
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

    # Auth = driver.find_element("class", "FlatButton FlatButton--primary FlatButton--size-l FlatButton--wide ")
    # time.sleep(4)
    # Auth.click()
    # time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
