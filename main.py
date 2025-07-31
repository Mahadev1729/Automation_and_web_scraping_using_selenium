from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org")
print(driver.title)
driver.implicitly_wait(5)

search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.ID, "submit")

search_box.send_keys("Selenium")
search_button.click()

time.sleep(2)
print(driver.title)

first_result = driver.find_element(By.CSS_SELECTOR, ".list-recent-events li a")
print(first_result.text)

time.sleep(4)
driver.quit()
