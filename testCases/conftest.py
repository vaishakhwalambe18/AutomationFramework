from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
        driver = webdriver.Chrome()
        return driver
        # browser = 'chrome'
        # if browser == 'chrome':
        #     driver = webdriver.Chrome()
        #     print("Launching chrome browser.........")
        # elif browser == 'firefox':
        #     driver = webdriver.Firefox()
        #     print("Launching firefox browser.........")
        # return driver
