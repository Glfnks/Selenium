from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from var import base_url, login, password, url_for_constructor, value_in_filter

s = Service("C:\\Users\\HRV\\PycharmProjects\\Selenium_D_n_D\\Chrome\\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_argument("Mozilla/5.0(Linux;Android6.0;Nexus5Build/MRA58N)AppleWebKit/537.36(KHTML,likeGecko)Chrome/109.0.0.0MobileSafari/537.36")
# options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(
    service=s,
    options=options
)

try:
    driver.get(base_url)
    time.sleep(1)

    login_input = driver.find_element("id", "login")
    login_input.clear()
    login_input.send_keys(login)
    # time.sleep(3)
    driver.implicitly_wait(3)

    password_input = driver.find_element("id", "password")
    password_input.clear()
    password_input.send_keys(password)
    # time.sleep(1)
    driver.implicitly_wait(3)
    password_input.send_keys(Keys.ENTER)
    time.sleep(1)

    driver.get(url_for_constructor)
    time.sleep(2)

    unwrap_table = driver.find_element("xpath", "//*[@id='rc-tabs-0-panel-sources']/div/div[1]/div[2]/div")
    unwrap_table.click()
    driver.implicitly_wait(2)
    unwrap_table = driver.find_element("xpath", "//*[@id='rc-tabs-0-panel-sources']/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div")
    unwrap_table.click()
    time.sleep(1)
    unwrap_table = driver.find_element("xpath", "//*[@id='rc-tabs-0-panel-sources']/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div[1]")
    unwrap_table.click()
    time.sleep(1)
    unwrap_table = driver.find_element("xpath", "/html/body/div/section/section/aside/div/div[1]/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div")
    unwrap_table.click()
    time.sleep(1)

    drag_table = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "catalog-Item-widget-item--MggsK")))
    drop_table = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section/main")))
    ActionChains(driver).drag_and_drop(drag_table, drop_table).perform()
    time.sleep(3)
    # print("Таблица перенесена")

    open_contmenu_on_table = driver.find_element(By.CLASS_NAME, "node-add-attributes-button-button--HX48p")
    open_contmenu_on_table.click()
    time.sleep(1)
    # print("Контекстное меню в таблице открыто")

    check_box = driver.find_element("xpath", "//*[@id='root']/section/section/main/div/div/div[6]/div/div/div/div[1]/div/div[1]/div[3]/div/div[2]/label[1]")  # Отчетная дата
    check_box.click()
    check_box = driver.find_element("xpath", "//*[@id='root']/section/section/main/div/div/div[6]/div/div/div/div[1]/div/div[1]/div[3]/div/div[2]/label[4]")  # Код НП
    check_box.click()
    # print("Чекбоксы установлены")

    close_contmenu_on_table = driver.find_element(By.CLASS_NAME, "node-add-attributes-button-button--HX48p")
    close_contmenu_on_table.click()
    time.sleep(1)
    # print("Контекстное меню в таблице закрыто")

    driver.maximize_window()
    time.sleep(3)

    drag_filter = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/section/section/main/div/div/div[2]/div/div[7]/button")))
    drop_filter = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section/main")))
    ActionChains(driver).drag_and_drop(drag_filter, drop_filter).perform()
    time.sleep(1)
    # print("Фильтр перетащен")

    join_table = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/section/main/div/div/div[6]/div/div/div/div[1]/div/div[3]")))
    join_filter = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/section/main/div/div/div[6]/div/div/div/div[2]/div/div[1]/div")))
    ActionChains(driver).drag_and_drop(join_table, join_filter).perform()
    time.sleep(2)
    # print("Таблица с фильтром соединена")

    set_value_in_filter = driver.find_element("xpath", "//*[@id='root']/section/section/main/div/div/div[6]/div/div/div/div[2]/div/div[4]/div/textarea")
    set_value_in_filter.clear()
    set_value_in_filter.send_keys(value_in_filter)
    time.sleep(1)
    # print("Значения в фильтре установлено")

    open_context_rmb = driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main")
    ActionChains(driver).context_click(open_context_rmb).perform()
    time.sleep(1)
    # print("Контекстное меню ПКМ открыто")

    create_ouput_entity = driver.find_element("xpath", "//*[@id='root']/section/section/main/div/div/div[6]/div[2]/div[1]")
    time.sleep(0.5)
    create_ouput_entity.click()
    time.sleep(1)
    # print("Выходная сущность создана")

    join_filter1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/section/main/div/div/div[6]/div/div/div/div[2]/div/div[2]")))
    join_entity = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/section/main/div/div/div[6]/div/div/div/div[3]/div/div[1]")))
    ActionChains(driver).drag_and_drop(join_filter1, join_entity).perform()
    time.sleep(5)
    # print("Фильтр с сущностью соединён")

    select_all_on_entity = driver.find_element(By.CLASS_NAME, "srd-default-node__button-select-all ")
    select_all_on_entity.click()
    time.sleep(1)
    # print("В сущности выбраны все атрибуты")

    launch_algorithm = driver.find_element(By.XPATH, "//*[@id='root']/section/section/main/div/div/div[1]/div[2]/div[2]/span")
    launch_algorithm.click()
    time.sleep(5)
    # print("Запуск начат")

    # delete_table = driver.find_element("xpath", "/html/body/div/section/section/main/div/div/div[6]/div/div/div/div/div/div[1]/button/i")
    # delete_table.click()
    # time.sleep(2)
    # delete_table_confirm = driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/button[2]/span")
    # delete_table_confirm.click()

    time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    # driver.close()
    driver.quit()
