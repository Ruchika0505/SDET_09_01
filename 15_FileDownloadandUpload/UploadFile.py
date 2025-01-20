import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.filemail.com/share/upload-file")

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_path = r"C:\Users\ruchika\Desktop\Samplefile.odt"
time.sleep(5)
file_input.send_keys(file_path)
time.sleep(15)

# Close the browser
driver.quit()

