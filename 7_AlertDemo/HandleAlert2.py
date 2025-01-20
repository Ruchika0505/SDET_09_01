import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver

driver=webdriver.Chrome()

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")

#validation

text="Congratulations! You must have the proper credentials."

msg=driver.find_element(By.XPATH,'//*[@id="content"]/div/p').text
print(msg)

if(msg==text):
    print("Passed")
else:
    print("Failed")