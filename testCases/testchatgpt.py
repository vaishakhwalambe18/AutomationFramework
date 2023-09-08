from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome()

# Step 1: Navigate to https://tietoevry.sharepoint.com/
driver.get("https://tietoevry.sharepoint.com/")

# Step 2: Click on tools & app
tools_app_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Tools & app"))
)
tools_app_link.click()

# Step 3: Click on all tools
all_tools_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "All tools"))
)
all_tools_link.click()

# Close the WebDriver
driver.quit()