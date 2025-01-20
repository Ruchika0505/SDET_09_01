#Bootstrap dropdown which are placed using span of input/div tag--select class is not workable on such dropdowns.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# driver.implicitly_wait(5)

driver.find_element(By.XPATH,'//span[@id="select2-billing_state-container"]').click()


stateNames=driver.find_elements(By.XPATH,'//*[@id="billing_state"]/option')
print(len(stateNames)) #38


for state in stateNames:
    if state.text=="Chandigarh":
        print(state.text)
        state.click()
        break

time.sleep(15)


