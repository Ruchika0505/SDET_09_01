import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

# Contect_click(element)--ActionChains
# Right Click on Element

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

button=driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/p/span')
copy=driver.find_element(By.XPATH,'/html/body/ul/li[3]/span')

act=ActionChains(driver)
time.sleep(5)
act.context_click(button).perform() #right click
time.sleep(5)
copy.click()
time.sleep(5)
driver.switch_to.alert.accept()

time.sleep(5)

# a=driver.switch_to.alert
# a.accept()