# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
import time
# import random
from fake_useragent import UserAgent
from proxy_auth_data import login, password


# url = 'https://www.instagram.com/'
# user_agents_list = [
#     "Hello",
#     "GoodDay",
#     "Wazap"
# ]

useragent = UserAgent()

options = webdriver.ChromeOptions()

# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
options.add_argument(f"user-agent={useragent.random}")

s = Service("C:\\Users\\HRV\\PycharmProjects\\Selen\\ChromeDriver\\chromedriver.exe")

proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@190.61.88.147:8080"
    }

}

# options.add_argument("--proxy-server=207.236.12.216:10643")

driver = webdriver.Chrome(
    service=s,
    seleniumwire_options=proxy_options
)

try:
#     driver.get(url='https://whatmyuseragent.com/')
#     time.sleep(2)

    driver.get("https://2ip.ru")
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
