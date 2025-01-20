from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Set up the driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# Open the OrangeHRM demo site
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Login
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for the dashboard to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
)

# Navigate to Leave -> Leave List
leave_menu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='Leave']"))
)
leave_menu.click()

leave_list_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[text()='Leave List']"))
)
leave_list_option.click()


# Handle "From Date" picker
from_date_picker = driver.find_element((By.XPATH, "//label[text()='From Date']/following-sibling::div//input"))


from_date_picker.click()
from_date_picker.clear()
from_date_picker.send_keys("2023-12-01")
from_date_picker.send_keys(Keys.RETURN)

# Handle "To Date" picker
to_date_picker = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//label[text()='To Date']/following-sibling::div//input"))
)
to_date_picker.click()
to_date_picker.clear()
to_date_picker.send_keys("2023-12-31")
to_date_picker.send_keys(Keys.RETURN)

# Handle Leave Status dropdown
leave_status_dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//label[text()='Leave Status']/following-sibling::div//div[@class='oxd-select-text-input']"))
)
leave_status_dropdown.click()

# Select an option (e.g., "Pending Approval")
status_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='Pending Approval']"))
)
status_option.click()

# Click Search Button
search_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Search']")
search_button.click()

# Wait and observe the results
time.sleep(5)

# Close the browser
driver.quit()
