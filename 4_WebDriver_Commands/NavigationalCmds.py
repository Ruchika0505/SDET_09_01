import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.flipkart.com/")

time.sleep(2)

driver.get("https://www.amazon.com/")

time.sleep(2)

driver.back() #flipkart

time.sleep(2)

driver.forward() #amazon

time.sleep(2)

driver.refresh() #refresh the page

time.sleep(2)


# find_elements---single or multiple,list,
# find_element-



