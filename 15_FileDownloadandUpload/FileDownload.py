import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location=os.getcwd()
def chrome_setup():
    #download files in desired location
    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(options=ops)
    return driver

def edge_setup():

    #download files in desired location
    preferences={"download.default_directory":location}
    ops=webdriver.EdgeOptions()
    ops.add_argument('--download.default_directory={os.path.abspath(location)}')
    driver = webdriver.Edge(options=ops)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service

    #settings
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.dir",location)
    driver = webdriver.Firefox(options=ops)
    return driver

#Automation code
driver=chrome_setup()  #function call
# driver=edge_setup()
# driver=firefox_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")

driver.maximize_window()
time.sleep(4)
print(location)
time.sleep(5)
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(5)