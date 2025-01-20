from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

#get()--it will open the url on the browser
driver.get("https://demo.nopcommerce.com/register")
#is_displayed()--return true if the element is displayed on the webpage

logo=driver.find_element(By.XPATH,"//img[@alt='nopCommerce demo store']")
print("Logo display status ", logo.is_displayed())
print("Logo enabled status ", logo.is_enabled())

searchBox=driver.find_element(By.NAME,'q')

print("The search box status ", searchBox.is_displayed())

#is_enabled--- is check the enabled feature of the webelement
print("The search box is enabled", searchBox.is_enabled())

#is_selected---to check which option is selected --radio button,checkboxes
# print(driver.find_element(By.XPATH,"//input[@id='gender-male']").is_selected()) #False

rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

rd_male.click()

print("Male Radio Button Status ", rd_male.is_selected()) #True
print("Female Radio Button Status ", rd_female.is_selected()) #False

rd_female.click()

print("Male Radio Button Status ", rd_male.is_selected()) #False
print("Female Radio Button Status ", rd_female.is_selected()) #True



driver.close()

