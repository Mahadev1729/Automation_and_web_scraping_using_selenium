from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
query="laptop"
driver.get(f"https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={query}&crid=1IFDC1YF9N37Z&sprefix=laptop%2Caps%2C573")

elem=driver.find_element(By.NAME,'q')
driver.close()


