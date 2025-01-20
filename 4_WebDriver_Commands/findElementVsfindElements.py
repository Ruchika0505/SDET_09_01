import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.automationpractice.pl/index.php")
# #findelement()--return only one element
#
# # when Locator is matching with single element
# # time.sleep(6)
# # driver.find_element(By.XPATH,"//input[@id='search_query_top']").send_keys("Apple MacBook Pro 13-inch")
# time.sleep(2)
#
# # when Locator is matching with multiple element
# # text=driver.find_element(By.XPATH,'//*[@class="row"]')
# # print(len(text))
#
# #when Locator is not matching with any element
# driver.find_element(By.XPATH,'abc') #Exception




#findelements()--return the list of multiple elements

# when Locator is matching with single element

# text=driver.find_elements(By.XPATH,"//div[@class='banner']")
# print(len(text))
time.sleep(2)

# when Locator is matching with multiple element
# text=driver.find_elements(By.XPATH,'//*[@class="row"]')
# print(len(text)) #6

#when Locator is not matching with any element

text=driver.find_elements(By.XPATH,'abc')
print(len(text)) #0

# Difference between findelement and findelements
# 1) Locator is matching with single
# 2) Locator is matching with multiple
# 3) Locator is not matching with any element