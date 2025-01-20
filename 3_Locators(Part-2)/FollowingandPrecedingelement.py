from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://www.facebook.com")

driver.maximize_window()

preceding_elements = driver.find_elements(By.XPATH, "//*[@id='email']/preceding::*")
print(f"Total number of preceding elements: {len(preceding_elements)}")

# Find all following sibling elements (elements after the email field in the DOM)
following_elements = driver.find_elements(By.XPATH, "//*[@id='email']/following::*")
print(f"Total number of following elements: {len(following_elements)}")

print("Tags of preceding elements:")
for elem in preceding_elements:
    print(elem.tag_name)

print("Tags of following elements:")
for elem in following_elements:
    print(elem.tag_name)

# Close the browser after the action
driver.quit()
