from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from Auth_data import avito_login, avito_password


s = Service("C:\\Users\\HRV\\PycharmProjects\\Selen\\ChromeDriver\\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11")

options.headless = True
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=s,
    options=options
)

try:


    driver.get("https://www.avito.ru/all/zapchasti_i_aksessuary/shiny_diski_i_kolesa/shiny-ASgBAgICAkQKJooLgJ0B?cd=1")
    # print(driver.window_handles)
    # print(f"Currently URL is: {driver.current_url}")
    time.sleep(3)

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
    price = driver.find_element("xpath", "//*[@id='app']/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/span/span/span[1]")
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
    # time.sleep(3)
    driver.implicitly_wait(10)

    driver.switch_to.window(driver.window_handles[1])
    # time.sleep(3)
    driver.implicitly_wait(10)
    print(f"Currently URL is: {driver.current_url}")
    title = driver.find_element("class name", "title-info-title-text")
    price = driver.find_element("xpath", "//*[@id='app']/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/span/span/span[1]")
    print(f"Title is: {title.text}")
    print(f"Price is: {price.text}")
    print(" #" * 20)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
