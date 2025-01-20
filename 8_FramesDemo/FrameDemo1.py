import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="name"]').send_keys("Hello Frames")
time.sleep(7)
# laocate the drop down which is avaiable inside the frame
# name of the frame
# id of the frame
# Webelement
# Index-- when we have less no of frames

##laocating the frame with its id/name attribute
driver.switch_to.frame("frm1")

drp1=Select(driver.find_element(By.XPATH,'//*[@id="selectnav2"]'))
drp1.select_by_visible_text("Home")
time.sleep(7)

driver.switch_to.default_content() # driver is pointing on degault location ie web page

#locating the frame with web element

frame2=driver.find_element(By.XPATH,'//*[@id="frm2"]')
driver.switch_to.frame(frame2)

driver.find_element(By.XPATH,'//*[@id="firstName"]').send_keys("David")
time.sleep(7)

#Frame-3

driver.switch_to.default_content()
#locating the frame with web element

frame3=driver.find_element(By.XPATH,'//*[@id="frm3"]')
driver.switch_to.frame(frame3)
#DropDown using select
drp2=Select(driver.find_element(By.XPATH,'//*[@id="selectnav1"]'))
drp2.select_by_visible_text("-- XPath")
time.sleep(5)

