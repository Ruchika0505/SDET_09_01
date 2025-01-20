import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(2)
#absolute Xpath--- nodes/tags

# driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirts")
# time.sleep(2)
# driver.find_element(By.XPATH,'/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button').click()
#
# time.sleep(2)

# Relative Xpath--attributes
# //tag[@attribute='value'] oR //*[@attribute='value']
#
# driver.find_element(By.XPATH,"//*[@placeholder='Search']").send_keys("T-shirts")
# driver.find_element(By.XPATH,"//button[@name='submit_search']").click()


# and or in relative xpath

# driver.find_element(By.xpath("//*[@name='submit_search' or @id='search_query_top']")).send_keys('T-shirt')
# driver.find_element(By.xpath("//*[@name='submit_query' and @id='search_query_top']")).send_keys('T-shirt')

# function--- contains(),starts-with(),text()
# contains()--2 parameters---
#with attributes

# driver.find_element(By.XPATH,"//input[contains(@id,'search_query_top')]").send_keys('T-shirt')

#with text()

# # starts-with()
# driver.find_element(By.XPATH,"//*[starts-with(@name,'su') and @class='btn btn-default button-search']").click()

# text()
# mytext=driver.find_element(By.XPATH,"//*[text()='Women']").text  #return you the inner text of the element
# print(mytext)



