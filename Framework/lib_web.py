from selenium.webdriver.common.by import By

from Framework.lib_logger import LogGen
from selenium import webdriver as driver

lg = LogGen.loggen()


class webOperations:
    lg = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def kyGetObject(self, driver, findBy, obj):
        element = ""
        if findBy.lower() == "id":
            element = driver.find_element(By.ID, obj)
        if findBy.lower() == "xpath":
            element = driver.find_element(By.XPATH, obj)
        if findBy.lower() == "xpath":
            element = driver.find_element(By.LINK_TEXT, obj)

        return element

    def kyPerformWebOperationWS(self, objectNm, driver, findBy, obj, sAction, sData):
        element = self.kyGetObject(driver, findBy, obj)
        if sAction.lower() == "click":
            element.click()
        if sAction.lower() == "sendkeys":
            element.send_keys(sData)
        self.lg.INFO(objectNm, sAction, sData)
