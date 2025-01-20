import os
from selenium import webdriver
from datetime import datetime

# Function to capture and save a screenshot
def capture_screenshot():
    try:

        driver = webdriver.Chrome()
        driver.get("https://www.orangehrm.com/")

        # Generate a timestamped filename for the screenshot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join("screenshots", f"screenshot_{timestamp}.png")

        # Capture the screenshot
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

# Call the function

capture_screenshot()
