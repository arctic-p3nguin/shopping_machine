from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

search = input()
PATH = "/Users/user/chromedriver-win32/chromedriver.exe"
options = webdriver.ChromeOptions()
service = Service(PATH)
driver = webdriver.Chrome(service=service, options=options)

url = "https://mall.e-muse.com.tw/"
driver.get(url)
search_bar = driver.find_element(By.ID, "ns-search-input")
search_bar.send_keys(search)
search_bar.send_keys(Keys.RETURN)
valid = driver.find_elements(By.CLASS_NAME, "sc-dmqHEX")
if len(valid):
    print("no information found")
else:
    a_tag = driver.find_element(By.CLASS_NAME, "sc-hImiYT")  # class只能一個
    item = a_tag.get_attribute("href")
    driver.get(item)
    is_sold_out = driver.find_element(By.CLASS_NAME, "custom-btn-text")
    if is_sold_out.text == "貨到通知我":
        print("sold out")
    else:
        button = driver.find_element(By.CSS_SELECTOR, 'button[data-qe-id="body-to-checkout-btn"]')
        button.click()
        time.sleep(7)  # 等頁面加載
        buy = driver.find_element(By.CSS_SELECTOR, 'button[data-qe-id="fixed-bottom-to-checkout-btn"]')
        driver.execute_script("arguments[0].click();", buy)  # 用javascript
        login = driver.find_element(By.CSS_SELECTOR, 'button[data-qe-id="common-confirm-button"]')
        login.click()
        time.sleep(1)
        phone = driver.find_element(By.NAME, "cellPhone")
        phone.send_keys("cell_phone_number")
        phone.send_keys(Keys.RETURN)
        time.sleep(3)
        password = driver.find_element(By.NAME, "password")
        password.send_keys("password")
        password.send_keys(Keys.RETURN)
        time.sleep(8)
        buy = driver.find_element(By.CSS_SELECTOR, 'button[data-qe-id="fixed-bottom-to-checkout-btn"]')
        driver.execute_script("arguments[0].click();", buy)
        time.sleep(3)
        order = driver.find_element(By.CSS_SELECTOR, 'button[data-qe-id="fixed-bottom-submit-order-btn"]')
        driver.execute_script("arguments[0].click();", order)
        time.sleep(100)


