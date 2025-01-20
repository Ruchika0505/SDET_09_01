import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

# Contect_click(element)--ActionChains
# Right Click on Element

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")

driver.switch_to.frame("iframeResult")

field1=driver.find_element(By.XPATH,'//*[@id="field1"]')
field1.clear()
field1.send_keys("Welcome")

button =driver.find_element(By.XPATH,'/html/body/button')

act=ActionChains(driver)
time.sleep(5)
act.double_click(button).perform() #double click
time.sleep(7)

#validation

