from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time


s = Service("C:\\Users\\HRV\\PycharmProjects\\Selen\\FirefoxDriver\\geckodriver.exe")

# user-agent

options = webdriver.FirefoxOptions()
options.add_argument("user-agent=Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)

driver = webdriver.Firefox(
    service=s,
    options=options
)

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(3)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
