import os
import time

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

import XLUtils
driver=webdriver.Chrome()
driver.get("https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator")
driver.maximize_window()

file=os.getcwd() + r"\caldata.xlsx"
# rows=XLUtils.getRowCount(file,"Sheet1")

rows=XLUtils.getRowCount(file,"Sheet2")

print(rows)
for r in range(2,rows+1):
    deposit=XLUtils.readData(file,"Sheet1",r,1)
    length=XLUtils.readData(file,"Sheet1",r,2)
    rate=XLUtils.readData(file,"Sheet1",r,3)
    compounding=XLUtils.readData(file,"Sheet1",r,4)
    exp_mvalue=XLUtils.readData(file,"Sheet1",r,5)
    driver.find_element(By.ID,"mat-input-0").send_keys(deposit)
    driver.find_element(By.ID,"mat-input-1").send_keys(length)
    driver.find_element(By.ID,"mat-input-2").send_keys(rate)
    driver.find_element(By.XPATH,"//*[@id='lEcE7Em2UkSqUmHuYCEnK']/div/div/div/div/app-cd-calculator/div/div[1]/form/div/div[4]/mat-form-field/div/div[1]").send_keys(compounding)
    # c_drp=driver.find_element(By.CLASS_NAME,"mat-select-arrow-wrapper ng-tns-c109-4").click()
    time.sleep(5)

    num_btn=driver.find_element(By.CLASS_NAME,"mdc-button__ripple")
    driver.execute_script("arguments[0].click();",num_btn)

    act_mvalue=driver.find_element(By.CLASS_NAME,"CIT-margin--0").text
    if float(exp_mvalue)==float(act_mvalue):
        print("Passed")
        XLUtils.writeData(file,"Sheet1",r,7,"Passed")
        XLUtils.fillGreenColor(file, "Sheet1", r, 7)
    else:
        print("Failed")
        XLUtils.writeData(file,"Sheet1",r,7,"Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 7)


