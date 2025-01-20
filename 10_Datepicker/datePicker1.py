import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(4)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
#Method-1
#Handling with sendkeys method
# driver.switch_to.frame(0)
# driver.find_element(By.XPATH,'//*[@id="datepicker"]').send_keys("10/18/2024")
# time.sleep(5)

#Method-2 When sendkeys not work

driver.switch_to.frame(0)
driver.find_element(By.XPATH,'//*[@id="datepicker"]').click()

year='2020'
month='May'
date='10'

while True:
    mon=driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[1]').text #month
    yr= driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[2]').text#year

    if(mon==month and yr==year):
        break
    else:
        #driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[2]').click() #future arrow

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[1]/span').click() #previous arrow

#Select date

dates=driver.find_elements(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')

for i in dates:
    if i.text==date:
        i.click()
        break

time.sleep(5)
