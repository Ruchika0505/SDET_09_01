from selenium import webdriver
from selenium.webdriver.common.by import By

# 1) Count number of rows & columns
# 2) Read specific row & Column data--cell value
# 3) Read all the rows & Columns data
# 4) Read data based on condition(List books name whose author is Mukesh)

driver=webdriver.Chrome()


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Count number of rows & columns

rows=driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table//tbody//tr')
print("The no of rows are",len(rows))

col=driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table//tbody//tr[1]//th')
print("The no of cols are",len(col))

# #Read specific row & Column data--cell value
# cellvalue=driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[5]/td[1]').text
# print(cellvalue)

# 3) Read all the rows & Columns data

for r in range(2,len(rows)+1): #rows
    for c in range(1,len(col)+1): #cols
        data=driver.find_element((By.XPATH,"//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]")).text
        print(data)

# 4) Read data based on condition(List books name whose author is Mukesh)

# for r in range(2,len(rows)+1): #rows
#     authername = driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table//tbody/tr[" + str(r) + "]/td[2]").text
#     if (authername == "Mukesh"):
#         bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
#         price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
#         print(bookname,authername, price)




