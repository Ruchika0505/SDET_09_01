from selenium.webdriver.common.by import By


class LoginPage:
    # Locators
    txt_useremail_id = 'email'
    txt_passwd_id = 'passwd'
    btn_signin_xpath = '//*[@id="SubmitLogin"]/span'

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions:

    def setUserName(self, username):
        usertxt = self.driver.find_element(By.ID, self.txt_useremail_id)
        usertxt.send_keys(username)


    def setUserPasswd(self, pwd):
        passtxt = self.driver.find_element(By.ID, self.txt_passwd_id)
        passtxt.send_keys(pwd)

    def clickLogin(self):
        button = self.driver.find_element(By.XPATH, self.btn_signin_xpath)
        button.click()
