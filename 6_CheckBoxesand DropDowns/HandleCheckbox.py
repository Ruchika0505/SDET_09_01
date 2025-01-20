import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6) # use it only one time in script

driver.get("https://testautomationpractice.blogspot.com/")

#select the specific checkbox

# driver.find_element(By.XPATH,'//*[@id="monday"]').click()
# time.sleep(5)
# driver.close()

# select all the checkboxes

chk=driver.find_elements(By.XPATH,"//*[@class='form-check-input' and @type='checkbox']")
print("The total no of checkboxes are ", len(chk)) #7

#appraoch-1

# for i in range(len(chk)):
#     chk[i].click()
# time.sleep(5)


#appraoch-2

# for i in chk:
#     i.click()
# time.sleep(5)

#Select checkboxes by choice


# for i in chk:
#     weekname=i.get_attribute("id")
#     if weekname=='monday' or weekname=='saturday':
#         i.click()
#
# time.sleep(5)

#select the last 2 option

# 1--0
# 2--1
# 3--2
# 4--3
# 5--4
# 6--5
# 7--6
#
# range(5,7)
# total no of element-3=starting point
#
# for i in range(len(chk)-2,len(chk)):
#     chk[i].click()
#
# time.sleep(5)

#Select first two

# for i in range(len(chk)):
#     if i<2:
#         chk[i].click()
# time.sleep(5)

#clearing all the check boxes

# for i in chk:
#     if i.is_selected():
#         i.click()
#
# time.sleep()


