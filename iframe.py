from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/frame_switching_tests/bug4876.html")

# find the iframe first
frame1 = driver.find_element(By.XPATH, '//*[@id="iframe"]')

# switch to iframe
# driver.switch_to.frame(frame1)

# Bu in dex values (0,1,2)
driver.switch_to.frame(0)

# now find the button inside iframe
message = driver.find_element(By.ID,"inputText")
message.send_keys("jgfghd25")
driver.find_element(By.ID, "submitButton").click()

time.sleep(20)

driver.quit()