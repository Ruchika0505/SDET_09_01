#Open browser---chrome,firefox,edge
#Pass URL "https://www.google.com/"  driver.get("")
#capture the text box
#send values"Selenium"
# validate

# service class



import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#approch-1
# driver=webdriver.
service_obj= Service(r"D:\SDET_Data\4_SDET,October-March 2024\Module3_SeleniumWithPython\driver_SDET\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

#approch-2
#this will  open the browser
# driver=webdriver.Chrome()
time.sleep(5)
#open the url to the browser
driver.get("https://www.google.com/")
time.sleep(5)
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("selenium")
time.sleep(5)
driver.find_element(By.NAME,"btnK").click()
# time.sleep(5)
# search_box.click()
time.sleep(5) #python
# print("The title of the page is ", driver.title)
title=driver.title

if title=="selenium - Google Search":
    print("Test Passed")
else:
    print("Test Failed")
driver.close() #close the page where driver instance is pointing