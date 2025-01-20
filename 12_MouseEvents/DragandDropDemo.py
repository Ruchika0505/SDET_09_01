import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
# Contect_click(element)--ActionChains
# Right Click on Element

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")


time.sleep(5)
rome=driver.find_element(By.XPATH,'//*[@id="box6"]')
italy=driver.find_element(By.XPATH,'//*[@id="box106"]')

act=ActionChains(driver)
time.sleep(5)

act.drag_and_drop(rome,italy).perform()

time.sleep(5)
#validation

assert "box6" in italy.get_attribute("innerHTML"),"Rome was not dropped in Italy"

