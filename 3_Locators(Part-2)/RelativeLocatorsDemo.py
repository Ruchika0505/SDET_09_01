from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Chrome()
driver.get("https://automationbookstore.dev/")

book2=driver.find_element(By.XPATH,"//*[@id='pid2']")
BookName=driver.find_element(locate_with(By.TAG_NAME,"li").to_right_of(book2)).text  #Agile Testing
print(BookName)

#Test Automation in real world
BookName=driver.find_element(locate_with(By.TAG_NAME,"li").to_left_of(book2)).text  #
print(BookName)

#Advanced selenium in java

BookName=driver.find_element(locate_with(By.TAG_NAME,"li").below(book2)).text
print(BookName)

#above

book6=driver.find_element(By.XPATH,"//*[@id='pid6']")

BookName=driver.find_element(locate_with(By.TAG_NAME,"li").above(book6)).text  #Agile Testing

print(BookName)