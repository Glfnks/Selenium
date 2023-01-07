from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from Auth_data import vk_phone, vk_password


s = Service("C:\\Users\\HRV\\PycharmProjects\\Selen\\ChromeDriver\\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

options.headless = True
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=s,
    options=options
)

try:
    driver.get("https://vk.com/")
    time.sleep(0.5)

    print("Passing authentication... ")
    email_input = driver.find_element("id", "index_email")
    email_input.clear()
    email_input.send_keys(vk_phone)
    email_input.send_keys(Keys.ENTER)
    time.sleep(2)

    password_input = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/input")
    password_input.clear()
    password_input.send_keys(vk_password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

    print("Going to profile page...")
    profile = driver.find_element("xpath", "/html/body/div[11]/div/div/div[2]/div[1]/div/nav/ol/li[1]/a/span[1]")
    profile.click()
    time.sleep(3)

    print("Start watching video...")
    video_block = driver.find_element("id", "wpt762696368_1")
    video_block.click()
    time.sleep(3)
    print("Finish watching video")


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
