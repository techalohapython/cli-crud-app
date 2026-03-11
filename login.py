from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

text_box = driver.find_element(By.NAME, "my-text")
text_box.send_keys("Admin")

password_box = driver.find_element(By.NAME, "my-password")
password_box.send_keys("1234567890")

time.sleep(20)

driver.quit()