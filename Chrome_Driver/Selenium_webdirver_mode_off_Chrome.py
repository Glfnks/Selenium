from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


s = Service("C:\\Users\\HRV\\PycharmProjects\\Selen\\ChromeDriver\\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11")

options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
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
