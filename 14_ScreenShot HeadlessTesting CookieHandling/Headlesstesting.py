from selenium import webdriver

def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")  # Correct way to set headless mode
    driver = webdriver.Chrome(options=ops)  # Initialize the Chrome WebDriver
    return driver

def headless_edge():

    ops=webdriver.EdgeOptions()
    ops.add_argument("--headless")
    driver=webdriver.Edge(options=ops)
    return driver


def headless_firefox():

    ops=webdriver.FirefoxOptions()
    ops.add_argument("--headless")
    driver=webdriver.Edge(options=ops)
    return driver

# driver=headless_chrome()
driver=headless_edge()
# driver=headless_firefox()


driver.get("https://www.foundit.in/seeker/registration")
driver.implicitly_wait(10)
print(driver.title)
print(driver.current_url)
driver.close()