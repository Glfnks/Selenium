# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.firefox.service import Service
import time
from fake_useragent import UserAgent
from proxy_auth_data import login, password

# url = 'https://www.vk.com/'

useragent = UserAgent()

options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", useragent.random)

s = Service("C:\\Users\\HRV\\PycharmProjects\\Selen\\FirefoxDriver\\geckodriver.exe")


#set proxy
# proxy = "1.179.148.33:1080"
# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilities["marionette"] = True
#
# firefox_capabilities["proxy"] = {
#     "ProxyType": "MANUAL",
#     "httpProxy": proxy,
#     "ftpProxy": proxy,
#     "sslProxy": proxy
# }
proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@190.61.88.147:8080"
    }

}

driver = webdriver.Firefox(
    service=s,
    seleniumwire_options=proxy_options
)

try:
    # driver.get(url='https://whatmyuseragent.com/')
    # time.sleep(5)

    driver.get("https://2ip.ru")
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
