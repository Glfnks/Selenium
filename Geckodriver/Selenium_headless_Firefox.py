from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.common.keys import Keys
from Auth_Data import instagram_login, instagram_password

options = webdriver.FirefoxOptions()
options.add_argument("user-agent=Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11")

s = Service("C:\\Users\\HRV\\PycharmProjects\\Selen\\FirefoxDriver\\geckodriver.exe")

options.headless = True

driver = webdriver.Firefox(
    service=s,
    options=options
)

try:
    driver.get("https://www.instagram.com")
    time.sleep(1)
    print("Passing authentication... ")
    email_input = driver.find_element("name", "username")
    email_input.clear()
    email_input.send_keys(instagram_login)

    inst_pass = driver.find_element("name", "password")
    inst_pass.clear()
    inst_pass.send_keys(instagram_password)
    time.sleep(0.5)
    inst_pass.send_keys(Keys.ENTER)
    time.sleep(5)

    notice_off = driver.find_element("xpath",
                                     "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
    notice_off.click()
    time.sleep(1)

    notice2_off = driver.find_element("xpath",
                                      "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
    notice2_off.click()
    time.sleep(1)

    driver.get("https://www.instagram.com/p/Ckz8iqcJrNf/")
    print("Going to view...")
    time.sleep(1)
    view_video = driver.find_element("xpath",
                                     "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/button")
    view_video.click()
    time.sleep(2)
    print("Finish watching video")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
