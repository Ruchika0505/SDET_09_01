import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClass:

    def test_chrome(self):
     try:
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/")
        driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys("Selenium with python")
        title=driver.title
        assert  driver.title==title
     finally:
        driver.close()

    def test_edge(self):
     try:
        driver = webdriver.Edge()
        driver.get("https://www.google.com/")
        driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys("Selenium with python")
        title = driver.title
        assert driver.title == title

     finally:
       driver.close()
    def test_firefox(self):
      try:
        driver = webdriver.Firefox()
        driver.get("https://www.google.com/")
        driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys("Selenium with python")
        title = driver.title
        assert driver.title == title
      finally:
          driver.close()