from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\Selenium\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com") # Opens browser window

# driver.get("https://www.amazon.com/dp/B0773ZY26F?ref_=cm_sw_r_cp_ud_dp_MXXJE8623PZ3JPH8B488")
# price = driver.find_element(By.CSS_SELECTOR, "span.a-offscreen+span")
# print(price.text)


#driver.get("https://www.python.org")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)
#
# submit_website_bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_website_bug_link.text)


# Challenge: Use Selenium to Scrape Website Data
# driver.get("https://www.python.org")
# driver.maximize_window() # Year was missing so i maximized the window
# events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul').text.splitlines()
# print(events)
# dict = {i: {"time":events[2*i] ,"name":events[2*i+1] } for i in range(0,5)}
# print(dict)



# driver.close()  # Closes tab
driver.quit()  # Closes browser
