import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#Select is the class in Selenium use to handle the drop down

drpdwn=Select(driver.find_element(By.XPATH,'//*[@id="country"]'))


#Select By Value
#select by Index

#Approach-1 #selectByVisibilityName
drpdwn.select_by_visible_text("India")
time.sleep(5)

#Approach-2 Select By Value
# drpdwn.select_by_value("uk")
# time.sleep(5)

#Approach-3 Select By Index

# drpdwn.select_by_index(1)
# time.sleep(5)

# capture all the options from the dropdown--options

alloptions=drpdwn.options #return all the options avaiable in dropdown

#total no of elements in dropdown

# print("The total no of elements are",len(alloptions))
#
# for opt in alloptions:
#     print(opt.text)


# select the option from dropdown without using builin method

for opt in alloptions:
    if(opt.text=="India"):
        opt.click()
        break
time.sleep(5)
