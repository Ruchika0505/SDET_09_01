import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.firefox.options import Options

download_dir = os.getcwd()  # Current Working directory

# Function to set Chrome options
def chrome_driver_setup():
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,  # Set download directory
        "download.prompt_for_download": False,       # Do not ask for download location
        "download.directory_upgrade": True,          # Allow directory upgrade
        "safebrowsing.enabled": True                 # Enable safe browsing
    }
    chrome_options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(options=chrome_options)



# Function to set Edge options
def edge_driver_setup():
    edge_options = webdriver.EdgeOptions()
    prefs = {
        "download.default_directory": download_dir,  # Set download directory
        "download.prompt_for_download": False,       # Do not ask for download location
        "download.directory_upgrade": True,          # Allow directory upgrade
        "safebrowsing.enabled": True                 # Enable safe browsing
    }
    edge_options.add_experimental_option("prefs", prefs)
    return webdriver.Edge(options=edge_options)

# Function to set Firefox options
def firefox_driver_setup():
    options = Options()
    # Set preferences for Firefox

    options.set_preference("browser.download.dir", download_dir)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")
    options.set_preference("pdfjs.disabled", True)  # Disable the built-in PDF viewer
    return webdriver.Firefox(options=options)


#validation
def download_file(driver):

    driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
    time.sleep(2)

    # Use JavaScript to click the download button directly to bypass the iframe
    download_button = driver.find_element(By.XPATH, "//a[text()='Download sample DOC file']")
    driver.execute_script("arguments[0].click();", download_button)
    time.sleep(2)

    downloaded_file_name = "file-sample_100kB.doc"
    downloaded_file_path = os.path.join(download_dir, downloaded_file_name)

    # Validation to check if the file has been downloaded
    if os.path.exists(downloaded_file_path):
        print(f"File downloaded successfully: {downloaded_file_name}")
    else:
        print(f"File download failed: {downloaded_file_name}")


    driver.quit()

# Select browser (You can switch between Chrome, Firefox, or Edge)
# driver = chrome_driver_setup()  # For Chrome
driver = firefox_driver_setup()  # For Firefox
# driver = edge_driver_setup()  # For Edge

download_file(driver)
