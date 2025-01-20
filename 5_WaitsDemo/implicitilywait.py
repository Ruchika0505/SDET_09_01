import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6) # use it only one time in script

driver.get("https://www.google.com/")

searchbox=driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
searchbox.send_keys("selenium")
searchbox.submit()
time.sleep(5)
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
time.sleep(5)
driver.quit()


