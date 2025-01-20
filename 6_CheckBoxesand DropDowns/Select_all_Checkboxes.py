from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the webpage with multiple checkboxes
    driver.get("https://the-internet.herokuapp.com/checkboxes")  # Example URL
    driver.maximize_window()

    # Find all checkboxes on the page
    checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

    # Select all checkboxes
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()

    print("All checkboxes selected.")
finally:
    driver.quit()
