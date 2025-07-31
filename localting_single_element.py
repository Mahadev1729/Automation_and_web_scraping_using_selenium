from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
query="laptops"
driver.get(f"https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={query}&crid=1IFDC1YF9N37Z&sprefix=laptop%2Caps%2C573")

elem=driver.find_element(By.CLASS_NAME,"puis-card-container")
print(elem.text)
time.sleep(8)
driver.close()


