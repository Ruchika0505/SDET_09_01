import os

from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()

#driver.save_screenshot(r"C:\Users\ruchika\Desktop\Python_Experienced Batch\3_Selenium With Python\New folder\Screenshot\Home.png")
# driver.save_screenshot(os.getcwd() + "\\HomePage.png")
driver.get_screenshot_as_file(os.getcwd() + "\\HomePage.png")



driver.close()
