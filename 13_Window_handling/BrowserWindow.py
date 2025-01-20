import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(7)

#driver.close() # close single browser window (where driver focused)

driver.quit() #close multiple browser windows ( this will kill the process)
time.sleep(7)