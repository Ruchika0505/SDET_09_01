from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()

#get()--it will open the url on the browser
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#title-- return the title of the page
print("The title of the page is ", driver.title) #OrangeHRM

#current_url--- return the current url of the page

print("The url of the page is ",driver.current_url) # https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

#page_source---get source code

print("the source code of the page is ", driver.page_source)
