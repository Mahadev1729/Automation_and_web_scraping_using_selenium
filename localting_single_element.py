from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
query="Laptops"
driver.get(f"https://www.amazon.com/s?k={query}&crid=1SMWAVY9D61VS&sprefix=laptop%2Caps%2C760&ref=nb_sb_noss_1")
elem=driver.find_element(By.CLASS_NAME,"a-section")
print(elem.text)
time.sleep(2)
driver.close()


