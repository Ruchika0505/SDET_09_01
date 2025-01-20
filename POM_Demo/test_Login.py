import pytest
from selenium import webdriver
from LoginPageObject import LoginPage

class TestLogin:
    def test_login(self):
        driver=webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(5)
        driver.maximize_window()
        lp=LoginPage(driver)
        lp.setUserName("sdetsdet12@gmail.com")
        lp.setUserPasswd("test123")
        lp.clickLogin()
        act_title= driver.title
        assert act_title=="My account - My Shop"


