from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Use Selenium in a Blank Project & Scrape a Different Piece of Data

chrome_driver_path = "D:\Selenium\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.maximize_window()
#
# article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')     # "." for classes, "#" for id's
# #print(article_count.text)
# #article_count.click()
#
# #all_portals = driver.find_element(By.LINK_TEXT, "All portals")  # Specific for link texts
# #all_portals.click()
#
#
# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)


# Challenge

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Ömer")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Dikyol")

email_address = driver.find_element(By.NAME, "email")
email_address.send_keys("omer@dikyol.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()