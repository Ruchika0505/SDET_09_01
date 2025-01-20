import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# steps for Testing Login Functinality
#
# 1) open browser
# 2) send URL "https://opensource-demo.orangehrmlive.com/auth/login"
# 3) enter Username :Admin
# 4) Enter password: admin123
# 5) Click login button
# 6) validation  (title of the page)

# open browser
driver=webdriver.Chrome()
# send URL "https://opensource-demo.orangehrmlive.com/auth/login"
driver.get("https://opensource-demo.orangehrmlive.com/auth/login")

# enter Username :Admin
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(2)
# Enter password: admin123
driver.find_element(By.NAME,"password").send_keys("admin")
time.sleep(2)
# Click login button
driver.find_element(By.CLASS_NAME,"oxd-button").click()

# validation  (title of the page)
expected_title="OrangeHRM"

actual_title= driver.title

if(expected_title==actual_title):
    print("Test Passed")
else:
    print("Test Failed")

#Assignment: write the login script for https://demo.guru99.com/test/newtours/