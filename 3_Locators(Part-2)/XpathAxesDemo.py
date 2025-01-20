import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

#self

Nodetext=driver.find_element(By.XPATH,"//*[contains(text(),'Surya Roshni Ltd')]/self::a").text
print("The text at self node is", Nodetext) # Surya Roshni Ltd

#parent
parenttext= driver.find_element(By.XPATH,"//*[contains(text(),'Surya Roshni Ltd')]/parent::td").text
print("The text at parent node is", parenttext) ## Surya Roshni Ltd

#ancestor

#find_elements--list of webelements
#find_element--WEbelement

ancestorNO=driver.find_elements(By.XPATH,"//*[contains(text(),'Surya Roshni Ltd')]/ancestor::tr") #list 1
print(len(ancestorNO)) #1


#child
childnode =driver.find_elements(By.XPATH,"//*[contains(text(),'Surya Roshni Ltd')]/ancestor::tr/child::td")
print(len(childnode)) #6

#descendant
descendantnodes=driver.find_elements(By.XPATH,"//*[contains(text(),'Surya Roshni Ltd')]/ancestor::tr/descendant::td")
print(len(descendantnodes))
##print the descendant

for i in descendantnodes:
    print(i.text)

#following nodes
followelements=driver.find_elements(By.XPATH,"//*[contains(text(),'Surya Roshni Ltd')]/ancestor::tr/following::*")
print(len(followelements))

#following sibling nodes

followelements=driver.find_elements(By.XPATH,"//*[contains(text(),'Surya Roshni Ltd')]/ancestor::tr/following-sibling::tr")
print(len(followelements))


#precending nodes

driver.find_elements(By.XPATH,"//*[contains(text(),'Surya Roshni Ltd')]/ancestor::tr/precending::*")
#len
#precending-sibling nodes

driver.find_elements("//*[contains(text(),'Surya Roshni Ltd')]/ancestor::tr/preceding-sibling::tr")
#len