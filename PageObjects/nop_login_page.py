import time

from selenium.webdriver.common.by import By
from Framework.lib_web import webOperations
from Framework.lib_logger import LogGen as lg


class Nop_loginPage:
    textbox_username = "Email"
    textbox_password = "Password"
    button_login = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    label_welcome = "/html/body/div[3]/div[1]/div[1]/h1"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, driver):
        webOp = webOperations()
        webOp.kyPerformWebOperationWS(self.driver, "UserName", "id", self.textbox_username, "sendkeys", "TEST")

    def loginIntoApp(self, username, password):
        self.setUserName()
        # webOp = webOperations()
        #
        # webOp.kyPerformWebOperationWS(self.driver, "UserName", "id", self.textbox_username, "sendkeys", "TEST")

        self.driver.find_element(By.ID, self.textbox_username).clear()
        self.driver.find_element(By.ID, self.textbox_username).send_keys(username)

        self.driver.find_element(By.ID, self.textbox_password).clear()
        self.driver.find_element(By.ID, self.textbox_password).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_login).click()
        time.sleep(3)
        assert self.driver.title == 'Dashboard / nopCommerce administration'
        lg.save_screenshot(self.driver)
