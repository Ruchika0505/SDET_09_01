import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestClass:

   def test_login(self,setup):
        #print(setup) #chrome
        self.driver=setup
        self.driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("sdetsdet12@gmail.com")
        self.driver.find_element(By.XPATH,'//*[@id="passwd"]').send_keys("test123")

        self.driver.find_element(By.XPATH,'//*[@id="SubmitLogin"]/span').click()
        try:
            text=self.driver.find_element(By.XPATH,'//*[@id="center_column"]/h1').text
            assert text=='MY ACCOUNT'
        except:
            self.driver.close()
            assert False

