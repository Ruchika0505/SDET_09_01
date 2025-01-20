from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time

driver=webdriver.Chrome()

# Open Expedia website
driver.get("https://www.expedia.com/")
driver.maximize_window()

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# Function to select a date dynamically in the date picker
def select_date(target_date):
    # Open the date picker
    date_picker_button = wait.until(EC.element_to_be_clickable((By.ID, "d1-btn")))
    date_picker_button.click()

    # Format the target date for matching (e.g., "Feb 15, 2024")
    formatted_date = target_date.strftime("%b %d, %Y")

    # Locate the date elements and select the target date
    dates = driver.find_elements(By.XPATH, "//button[@data-day]")
    for date in dates:
        if date.get_attribute("aria-label") == formatted_date:
            date.click()
            break

    # Confirm date selection by clicking the Done button
    done_button = driver.find_element(By.XPATH, "//button[text()='Done']")
    done_button.click()

# Calculate dates
current_date = datetime.now()
date_7_days_later = current_date + timedelta(days=7)
specific_date = (current_date.replace(day=1) + timedelta(days=45)).replace(day=15)  # "15th of next month"
print(current_date)
print(date_7_days_later)
print(specific_date)

# # Select Today's Date
# select_date(current_date)
# time.sleep(2)
#
# # Select Date 7 Days Later
# select_date(date_7_days_later)
# time.sleep(2)
#
# # Select Specific Date (15th of next month)
# select_date(specific_date)
# time.sleep(2)

# Close the browser
driver.quit()
