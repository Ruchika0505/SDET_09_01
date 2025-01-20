import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)

driver.get("https://www.flipkart.com/")
electronics=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/span/span[1]')
act=ActionChains(driver)
act.move_to_element(electronics).perform()
time.sleep(5)
bluetooth_speakes=driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/object/a[5]')
bluetooth_speakes.click()
# print(bluetooth_speakes.title)
expected_title="Speakers Buy Online Get Up to 80% Off on Top Brands"
time.sleep(5)

assert expected_title in driver.title, f"Assertion failed! Expected title '{expected_title}', but got '{driver.title}'"


