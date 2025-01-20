import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.severity(allure.severity_level.NORMAL)

class TestClass:
    @allure.severity(allure.severity_level.MINOR)
    @allure.feature("Display LOGO")
    def test_logo(self, setup):
        self.driver = setup
        logo = self.driver.find_element(By.XPATH, '//*[@id="header_logo"]/a/img').is_displayed()
        self.driver.close()
        assert logo == True

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Login")
    def test_login(self,setup):
        self.driver = setup
        self.driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("sdetsdet12@gmail.com")
        self.driver.find_element(By.XPATH,'//*[@id="passwd"]').send_keys("test123")

        self.driver.find_element(By.XPATH,'//*[@id="SubmitLogin"]/span').click()
        try:
            text=self.driver.find_element(By.XPATH,'//*[@id="center_column"]/h1').text
            assert text=='MY ACCOUNT'
        except:
            allure.attach(self.driver.get_full_page_screenshot_as_png(), name="testloginscreen",
                          attachment_type=AttachmentType.png)

            self.driver.close()
            assert False


