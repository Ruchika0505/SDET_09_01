import time

import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
# import mysql.connector

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
time.sleep(5)
try:
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="ruchika0505",
        database="youtube")

    curs = con.cursor()  # create cursor
    curs.execute("select * from cal_data")

    for row in curs:

        # reading data from excel
        pric =row[0]
        rateofinterest =row[1]
        per1 =row[2]
        per2 =row[3]
        fre =row[4]
        exp_mvalue =row[5]
        # passing data to the application
        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(pric)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofinterest)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)
        perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))

        perioddrp.select_by_visible_text(per2)
        frequencydrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        frequencydrp.select_by_visible_text(fre)

        click_button = driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[1]/img')
        driver.execute_script("arguments[0].click();", click_button)  # calculate button

        act_mvalue = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        # Validation
        if float(exp_mvalue) == float(act_mvalue):
            print("test passed")
        else:
            print("test failed")
        clear_button = driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img")
        driver.execute_script("arguments[0].click();", clear_button)
        time.sleep(2)
    con.close()
except Exception as e:
    print(e)

driver.close()
