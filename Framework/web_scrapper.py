import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def highlight(element, effect_time, color, border):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)

    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)


def get_all_elements(url):
    # service = Service()
    # options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()

    # Navigate to the Google homepage
    driver.get("https://www.google.com")

    highlight(driver.find_element(By.CSS_SELECTOR, "textarea#APjFqb.gLFyf[jsname='yZiJbe']"), 3, "blue", 5)

    # Get all web elements on the page
    all_elements = driver.find_element(By.XPATH, "//*")
    driver.implicitly_wait(10)
    # Print the tag name of each element
    for element in all_elements:
        print(element.tag_name)

    # Close the browser
    driver.quit()


get_all_elements("https://www.google.com")
