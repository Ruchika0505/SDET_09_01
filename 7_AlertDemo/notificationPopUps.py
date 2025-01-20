from selenium import webdriver

ops= webdriver.ChromeOptions()

ops.add_argument("--disable-notification")

driver=webdriver.Chrome(ops)


driver.get("https://whatmylocation.com/")
driver.maximize_window()
