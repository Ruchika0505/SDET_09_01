# CSS Selectors
# tag and id
# tag and class
# tag and attribute
# tag,class and attribute

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/login/")
# time.sleep(2)
# tag and id----tag#id
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@gmail.com")
# time.sleep(2)

#tag and class--- tag.classname
time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")

# tag and attribute ---tag[name='abc']

# driver.find_element(By.CSS_SELECTOR,"input[placeholder='Email address or phone number']").send_keys("abc@gmail.com")
# time.sleep(2)

# tag,class and attribute---input.classname[name='abc']

driver.find_element(By.CSS_SELECTOR,"input.inputtext[name='email']").send_keys("abc@gmail.com")
time.sleep(2)

