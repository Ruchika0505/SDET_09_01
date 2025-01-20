import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,'/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a').click()

frm1=driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(frm1)

#index
#this is embedded frame so default content is not required.
driver.switch_to.frame(0)

driver.find_element(By.XPATH,'/html/body/section/div/div/div/input').send_keys("Hello Frames")
time.sleep(7)