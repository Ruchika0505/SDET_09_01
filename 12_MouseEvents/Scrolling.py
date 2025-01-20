import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Chrome
# usage of javascript executor class in selenium---execute_script

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.orangehrm.com")
driver.maximize_window()
#
# 1. Scroll down page by pixel
driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value) #3000
time.sleep(5)
# 2. Scroll down page till the element is visible
logo=driver.find_element(By.XPATH,"/html/body/div/div/div/section[3]/div[1]/div/div[1]/div/img")
driver.execute_script("arguments[0].scrollIntoView();",logo)
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value) #5038.3330078125
time.sleep(5)
#3.scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value) #5990.8330078125
time.sleep(5)
#
# # #Scroll up to starting position
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
# value=driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:",value) #0
# time.sleep(5)