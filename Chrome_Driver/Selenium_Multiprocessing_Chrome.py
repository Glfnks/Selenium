from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from multiprocessing import Pool
import random


s = Service("C:\\Users\\HRV\\PycharmProjects\\Selen\\ChromeDriver\\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# options.headless = True
options.add_argument("--disable-blink-features=AutomationControlled")

urls_list = ["https://www.avito.ru", "https://instagram.com", "https://vk.com"]


# def get_data(url):
#     try:
#         driver = webdriver.Chrome(
#             service=s,
#             options=options
#         )
#         driver.get(url=url)
#         time.sleep(5)
#         driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#
#
# if __name__ == '__main__':
#     p = Pool(processes=3)
#     p.map(get_data, urls_list)


def get_data(url):
    try:
        driver = webdriver.Chrome(
            service=s,
            options=options
        )
        driver.get(url=url)
        time.sleep(5)
        driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div/div/video").click()
        time.sleep(random.randrange(3, 10))
    except Exception as ex:
        print(ex)
    # finally:
    #     driver.close()
    #     driver.quit()


if __name__ == '__main__':
    process_count = int(input("Enter the number of processes: "))
    url = input("Enter the URL: ")
    urls_list = [url] * process_count
    print(urls_list)
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)
