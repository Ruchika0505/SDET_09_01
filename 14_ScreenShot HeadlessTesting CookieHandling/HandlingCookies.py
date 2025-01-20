from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()

# Capture cookies from the browser

cookies=driver.get_cookies()  # list of cookies
print("Size of cookies", len(cookies)) #4

#print all the details of cookies:

# for c in cookies:
#     print(c.get('name'), ":" ,c.get('value'))
# #     print(c)


# Add new cookies to the browser

driver.add_cookie({"name":"MyCookie","value":"123456"})
cookies=driver.get_cookies()
print("Size of cookies after adding ", len(cookies)) #5
#
# # delete specific cookies from the browser
#
# driver.delete_cookie("MyCookie")
# cookies=driver.get_cookies()
# print("After deleting one cookie ", len(cookies)) #4
#
# # delete all the cookies
#
# driver.delete_all_cookies()
# cookies=driver.get_cookies()
# print("After deleting all the cookies ", len(cookies)) #0


