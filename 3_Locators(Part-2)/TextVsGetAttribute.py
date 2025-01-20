import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.automationpractice.pl/index.php")
#text---inner text of the element
time.sleep(2)
# search=driver.find_element(By.XPATH,"//input[@id='search_query_top']")
# search.send_keys("T-shirt")
# print("Result of text ",search.text) # print Nothing bcoz it doesnot have inner text
#
# print("Result of getAttribute()", search.get_attribute("value")) #T-shirt
# print("Result of getAttribute()", search.get_attribute("id")) # search_query_top

#
button=driver.find_element(By.XPATH,"//div[@class='banner']")
print("Result of text", button.text ) #search
print("Result of getAttribute()",button.get_attribute('value')) #None
print("Result of getAttribute()",button.get_attribute('type')) #submit