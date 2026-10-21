from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://yassparfums.com/")
assert "YASS Parfums" in driver.title

#elem= driver.find_element(By.NAME,"")
