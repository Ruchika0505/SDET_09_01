from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

# book_name = driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr/th').text
#total rows
rows = driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr')
print("rows: ",len(rows))

#total columns
column = driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr/th')
print("columns",len(column))

# cell_value = driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th').text
# # print(cell_value)
#
# for r in range(2,len(rows)):
#     for c in range(1,len(column)):
#         data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[" + str(r) +"]/td[" + str(c) + "]").text
#         print(data)

#
for r in range(2,len(rows)+1):
    author_name = driver.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[2]').text
    if (author_name == "Amit"):
        book_name = driver.find_element(By.XPATH,f'//table[@name="BookTable"]/tbody/tr[{r}]/td[1]').text
        price = driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[{r}]/td[4]").text
        print(book_name,author_name, price)


