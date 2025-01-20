from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with your browser driver if not using Chrome

# Open the registration page
driver.get("https://demo.automationtesting.in/Register.html")

# Maximize the browser window
driver.maximize_window()

# Fill in the First Name and Last Name
driver.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']").send_keys("John")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']").send_keys("Doe")

# Fill in the Address
driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']").send_keys("123 Main Street, New York")

# Fill in the Email and Phone
driver.find_element(By.CSS_SELECTOR, "input[ng-model='EmailAdress']").send_keys("johndoe@example.com")
driver.find_element(By.CSS_SELECTOR, "input[ng-model='Phone']").send_keys("9876543210")

# Select Gender
driver.find_element(By.XPATH, "//input[@value='Male']").click()

# Select Hobbies
driver.find_element(By.ID, "checkbox1").click()  # Cricket
driver.find_element(By.ID, "checkbox2").click()  # Movies

# Select Language
time.sleep(5)
driver.find_element(By.ID, "msdd").click()
time.sleep(2)


element = driver.find_element(By.XPATH, "//a[text()='English']")
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# driver.find_element(By.XPATH, "//a[text()='English']").click()
driver.find_element(By.XPATH, "//a[text()='Spanish']").click()
driver.find_element(By.XPATH, "//body").click()  # Close the language dropdown

# Select Skills from Dropdown
skills_dropdown = Select(driver.find_element(By.ID, "Skills"))
skills_dropdown.select_by_visible_text("Java")

# Select Country
# country_dropdown = Select(driver.find_element(By.ID, "countries"))
# country_dropdown.select_by_visible_text("India")


# Select Country (Searchable Dropdown)
#
# driver.find_element(By.XPATH, "//span[@role='combobox']").click()
# wait = WebDriverWait(driver, 25)
# country_option = wait.until(EC.presence_of_element_located((By.XPATH, "//li[text()='India']")))
# country_option.click()

# Select Year, Month, and Day of Birth
year_dropdown = Select(driver.find_element(By.ID, "yearbox"))
year_dropdown.select_by_visible_text("1990")

month_dropdown = Select(driver.find_element(By.XPATH, "//select[@placeholder='Month']"))
month_dropdown.select_by_visible_text("February")

day_dropdown = Select(driver.find_element(By.ID, "daybox"))
day_dropdown.select_by_visible_text("15")

# Set Password and Confirm Password
driver.find_element(By.ID, "firstpassword").send_keys("Password123")
driver.find_element(By.ID, "secondpassword").send_keys("Password123")

# Click the Submit Button
# driver.find_element(By.ID, "submitbtn").click()

time.sleep(5)
# element1 = driver.find_element(By.ID, "submitbtn")
# driver.execute_script("arguments[0].scrollIntoView();", element1)
# element1.click()

# Wait for a few seconds to observe the result
time.sleep(5)

# Close the browser
driver.quit()
