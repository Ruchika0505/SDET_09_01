import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

# cntrl +A
# cntrl+ C
# Tab
# Cntrl+V
driver=webdriver.Chrome()
driver.get("https://text-compare.com/")

time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="textCompareForm"]/div/textarea[1]').send_keys("Welcome to Selenium")

act=ActionChains(driver) #mouse events

#input 1== cntrl +A
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(5)
# act.key_down(keys.CONTROL).send_keys("a").act.key_up(keys.CONTROL).perform()

#input 1== cntrl +C

act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(5)
#press TAB to navigate input box 2

act.send_keys(Keys.TAB).perform()
time.sleep(5)

#input 2== cntrl +V

#
# act.key_down(Keys.CONTROL)
# act.send_keys("v")
# act.key_up(Keys.CONTROL)
# act.perform()
input2 = driver.find_element(By.XPATH, '//*[@id="textCompareForm"]/div/textarea[2]')
input2.send_keys(Keys.CONTROL, 'v') #paste the text
time.sleep(10)



