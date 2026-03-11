from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

# Open Selenium test form page
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Fill text input
text_box = driver.find_element(By.NAME, "my-text")
text_box.send_keys("kunal")

# text_id = driver.find_element(By.ID, "my-text-id")

# Fill password field
password_box = driver.find_element(By.NAME, "my-password")
password_box.send_keys("1234567890")

# Submit form
submit_button = driver.find_element(By.CSS_SELECTOR, "button")
submit_button.click()

#//*[@id="my-text-id"]
# Wait to see result
time.sleep(10)

driver.quit()