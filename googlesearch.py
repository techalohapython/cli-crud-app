from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random

# 1. Setup Options
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
# Optional: Keeps the browser open if the script finishes
options.add_experimental_option("detach", True)

# 2. Pass options to the driver (CRITICAL STEP)
driver = webdriver.Chrome(options=options)

# 3. Execution
driver.get("https://www.google.com")

# Small human-like delay
time.sleep(random.uniform(1.5, 3.0))

try:
    searchbar = driver.find_element(By.NAME, "q")

    # Typing simulation: typing one character at a time looks more human
    search_query = "selenium by python"
    for char in search_query:
        searchbar.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))

    searchbar.send_keys(Keys.RETURN)

except Exception as e:
    print(f"Error finding element: {e}")

# Long sleep as requested
time.sleep(200)
driver.quit()