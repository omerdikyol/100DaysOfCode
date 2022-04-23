from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "D:\Selenium\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

timeout = time.time() + 5
five_min = time.time() + 300

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

while True:
    cookie.click()

    if time.time() > timeout:  # Every 5 secs

        right_panel = driver.find_elements(By.CSS_SELECTOR, "#store b")[:-1]
        item_prices = [int(price.text.split("-")[1].strip().replace(",", "")) for price in right_panel]
        upgrades = {item_prices[n]: item_ids[n] for n in range(len(item_prices))}

        cookie_amount_str = driver.find_element(By.ID, "money").text
        if "," in cookie_amount_str:
            cookie_amount_str = cookie_amount_str.replace(",", "")
        cookie_amount = int(cookie_amount_str)
        #print(cookie_amount)

        upgrades_available = {cost: id for cost, id in upgrades.items() if cost < cookie_amount}

        max_upgrade = max(upgrades_available)

        #print(upgrades_available[max_upgrade])
        driver.find_element(By.ID, upgrades_available[max_upgrade]).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cps = driver.find_element(By.ID, "cps").text
        print(cps)
        break
