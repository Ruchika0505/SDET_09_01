import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
# Contect_click(element)--ActionChains
# Right Click on Element

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

min=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]') #{'x': 59, 'y': 250}
max=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]') #{'x': 412, 'y': 250}

print("Before sliding...")

print("The location of min slider",min.location)
print("The location of max slider",max.location)

act=ActionChains(driver)

act.drag_and_drop_by_offset(min,100,0).perform()  # only x axis will change
time.sleep(5)
act.drag_and_drop_by_offset(max,-36,0).perform()
time.sleep(5)

print("After sliding...")

print("The location of min slider",min.location)
print("The location of max slider",max.location)



