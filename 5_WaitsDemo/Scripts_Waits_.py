from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Explicit wait for the username field
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    # Enter the username
    username_field.send_keys("Admin")

    # Explicit wait for the password field
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    # Enter the password
    password_field.send_keys("admin123")

    # Explicit wait for the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )
    # Click the login button
    login_button.click()

    # Verify successful login by waiting for the dashboard header
    dashboard_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6'))
    )
    print("Login successful. Dashboard header found.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
