import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()

alertwindow =driver.switch_to.alert

alertwindow.send_keys("Welcome to the world of Alerts")

#print("The text of the alert window is ", alertwindow.text)
time.sleep(6)


alertwindow.accept() # click on OK option from Alert window
time.sleep(6)

#alertwindow.dismiss() #click on the cancle button

#validation
exp="You entered: Welcome to the world of Alerts"
actual=driver.find_element(By.XPATH,'//*[@id="result"]').text

if(exp==actual):
    print("Test Passed")
else:
    print("Test Failed")


