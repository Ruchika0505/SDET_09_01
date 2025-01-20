import pytest
from selenium import webdriver
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
    elif browser=='edge':
        driver = webdriver.Edge()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
    elif browser =="firefox":
        driver = webdriver.Firefox()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver

def pytest_addoption(parser):    # This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):       # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


