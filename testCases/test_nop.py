import pytest
from selenium import webdriver
from PageObjects.nop_login_page import Nop_loginPage


class Test_001_NopLogin:
    base_url = "https://admin-demo.nopcommerce.com/"
    user_name = ""
    password = ""

    def test_homepageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)
        nopLP = Nop_loginPage(self.driver)
        nopLP.loginIntoApp()
        self.driver.close()
