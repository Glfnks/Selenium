from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time


s = Service("C:\\Users\\HRV\\PycharmProjects\\Selen\\FirefoxDriver\\geckodriver.exe")

options = webdriver.FirefoxOptions()
options.add_argument("user-agent=Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)

options.headless = True

driver = webdriver.Firefox(
    service=s,
    options=options
)

try:

    driver.get("https://www.avito.ru/sankt-peterburg/avtomobili")
    # print(driver.window_handles)
    # print(f"Currently URL is: {driver.current_url}")
    # time.sleep(3)
    driver.implicitly_wait(10)

    items = driver.find_elements("xpath", "//div[@data-marker='item-photo']")
    items[0].click()
    # print(driver.window_handles)
    # time.sleep(5)
    driver.implicitly_wait(10)

    driver.switch_to.window(driver.window_handles[1])
    # time.sleep(2)
    driver.implicitly_wait(10)
    # print(f"Currently URL is: {driver.current_url}")

    title = driver.find_element("class name", "title-info-title-text")
    print(f"Currently URL is: {driver.current_url}")
    print(f"Title is: {title.text}")
    price = driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div/span/span/span[1]")
    print(f"Price is: {price.text}")
    print(" #" * 20)
    # time.sleep(2)
    driver.implicitly_wait(10)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    # time.sleep(3)
    driver.implicitly_wait(10)
    # print(f"Currently URL is: {driver.current_url}")

    items[1].click()
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    print(f"Currently URL is: {driver.current_url}")
    title = driver.find_element("class name", "title-info-title-text")
    price = driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div/span/span/span[1]")
    print(f"Title is: {title.text}")
    print(f"Price is: {price.text}")
    print(" #" * 20)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])


except Exception as ex:
    print(ex)
# finally:
#     driver.close()
#     driver.quit()
