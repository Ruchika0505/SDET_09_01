import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClass:
    @pytest.mark.parametrize("email,passwd",[("sdet12","test"),("sdetsdet@gmail.com","123"),("sdet@gmail.com","123"),("sdetsdet12@gmail.com","test123")])
    def test_login(self,email,passwd):
        driver=webdriver.Edge()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(email)
        driver.find_element(By.XPATH,'//*[@id="passwd"]').send_keys(passwd)

        driver.find_element(By.XPATH,'//*[@id="SubmitLogin"]/span').click()
        try:
            text=driver.find_element(By.XPATH,'//*[@id="center_column"]/h1').text
            assert text=='MY ACCOUNT'
        except:
            driver.close()
            assert False

