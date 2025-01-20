import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print("The url of the page is ",driver.current_url)
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a').click()
print("The url of the page is ",driver.current_url)
time.sleep(5)

driver.close()


