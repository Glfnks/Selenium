from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
from multiprocessing import Pool


s = Service("C:\\Users\\HRV\\PycharmProjects\\Selen\\FirefoxDriver\\geckodriver.exe")

options = webdriver.FirefoxOptions()
options.add_argument("user-agent=Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)

# options.headless = True

urls_list = ["https://www.avito.ru", "https://instagram.com", "https://vk.com"]


def get_data(url):
    global driver
    try:
        driver = webdriver.Chrome(
            service=s,
            options=options
        )
        driver.get(url=url)
        time.sleep(5)
        driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(processes=3)
    p.map(get_data, urls_list)
