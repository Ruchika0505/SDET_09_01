import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(5)
#ID
# driver.find_element(By.ID,"search_query_top").send_keys("T-Shirts")
#
# # search=driver.find_element(By.ID,"search_query_top")
# # search.send_keys()
#
# #NAme
# driver.find_element(By.NAME,"submit_search").click()
# #LinkedText
# # driver.find_element(By.LINK_TEXT,"Faded Short Sleeve T-shirts").click();
# # time.sleep(5)
#
# #PartialLinkedText
# driver.find_element(By.PARTIAL_LINK_TEXT,"Sleeve T-shirts").click();
# time.sleep(5)

text=driver.find_element(By.PARTIAL_LINK_TEXT,"Women").text
print("The first option is ",text)


#className
# slider=driver.find_elements(By.CLASS_NAME,"homeslider-container") #list
# print("The total no of images in slider are : ", len(slider))
#
# #Tag NAme
#
# #total no of images
#
# images=driver.find_elements(By.TAG_NAME,"img")
# print("The total no of images in page are : ", len(images))

#total no of links
