
#declare
#usage

import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# import expected.condition

driver=webdriver.Chrome()
driver.maximize_window()

#mywait=WebDriverWait(driver,10)  #explicit wait--decalre
mywait=WebDriverWait(driver,30,poll_frequency=5,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,
                                                                    Exception])

driver.get("https://www.google.com/")

searchbox=driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
searchbox.send_keys("selenium")
searchbox.submit()

#use
#link=mywait.until(EC.presence_of_element_located(By.XPATH,"//h3[text()='Selenium']"))
link=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))


link.click()
# time.sleep(6)
driver.close()

