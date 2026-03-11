# importing webdriver from selenium
from selenium import webdriver


# Here Chrome  will be used
driver = webdriver.Chrome()
# Opening the website
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver.save_screenshot("image.png")
# Showing the image
driver.quit()