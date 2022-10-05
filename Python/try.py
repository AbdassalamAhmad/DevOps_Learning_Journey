from selenium import webdriver

driver = webdriver.Chrome('E:\DevOps\Python\chromedriver.exe')
driver.implicitly_wait(30)
print ("hello")