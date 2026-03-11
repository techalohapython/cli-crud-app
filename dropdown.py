from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
options = Options()
driver = webdriver.Chrome(options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")


dropdown= Select(driver.find_element(By.NAME,"my-select"))
# dropdown.select_by_value("3")
dropdown.select_by_visible_text('Two')
time.sleep(20)

driver.quit()