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

# Fill password field
password_box = driver.find_element(By.NAME, "my-password")
password_box.send_keys("1234567890")

# Fill textarea
textarea = driver.find_element(By.NAME, "my-textarea")
textarea.send_keys("This is my first Selenium automation project")

# Select dropdown
dropdown = Select(driver.find_element(By.NAME, "my-select"))
dropdown.select_by_visible_text("Two")

# Datalist input
datalist = driver.find_element(By.NAME, "my-datalist")
datalist.send_keys("New York")

# Upload file (change path according to your computer)
file_upload = driver.find_element(By.NAME, "my-file")
file_upload.send_keys("/home/user/PycharmProjects/PythonProject/test.txt")

# Click checkbox
checkbox = driver.find_element(By.ID, "my-check-1")
checkbox.click()

# Click radio button
radio = driver.find_element(By.ID, "my-radio-1")
radio.click()

# Default checkbox
default_checkbox = driver.find_element(By.ID, "my-check-1")
default_checkbox.click()

# Checked checkbox
checked_checkbox = driver.find_element(By.ID, "my-check-2")
checked_checkbox.click()


# Pick color
color_picker = driver.find_element(By.NAME, "my-colors")
color_picker.send_keys("#ff0000")

# Pick date
date_picker = driver.find_element(By.NAME, "my-date")
date_picker.send_keys("03/10/2026")


# Submit form
submit_button = driver.find_element(By.CSS_SELECTOR, "button")
submit_button.click()

# Wait to see result
time.sleep(20)

driver.quit()