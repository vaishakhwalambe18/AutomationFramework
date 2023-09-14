import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Framework.lib_logger import LogGen

lg = LogGen.loggen()


class webOperations:
    lg = LogGen.loggen()

    # '====================================================================================================================================================
    # 'Function Description   : Get Element
    # 'Input Parameters:
    # 'Return Value:
    # 'Author: Vaishakh
    # 'UPDATED BY:
    # 'Date Created :
    # '====================================================================================================================================================
    @staticmethod
    def kyGetObject(self, driver, findBy, obj):
        try:
            locators = {
                "id": By.ID,
                "xpath": By.XPATH,
                "link_text": By.LINK_TEXT,
                "partial_link_text": By.PARTIAL_LINK_TEXT,
                "name": By.NAME,
                "tag_name": By.TAG_NAME,
                "class_name": By.CLASS_NAME,
                "css_selector": By.CSS_SELECTOR
                # Add more locators here if needed
            }

            if findBy.lower() in locators:
                return driver.find_element(locators[findBy.lower()], obj)
            else:
                raise ValueError(f"Invalid 'findBy' value: {findBy}")
        except Exception as e:
            self.lg.error(f"Error in kyGetObject: {str(e)}")

    # '====================================================================================================================================================
    # 'Function Description   : Action on element
    # 'Input Parameters:
    # 'Return Value:
    # 'Author: Vaishakh
    # 'UPDATED BY:
    # 'Date Created :
    # '====================================================================================================================================================
    def kyPerformWebOperationWS(self, objectNm, driver, findBy, obj, sAction, sData):
        try:
            element = self.kyGetObject(self, driver, findBy, obj)

            sAction = sAction.lower()  # Convert to lowercase for case-insensitive comparison

            if sAction == "click":
                element.click()
            elif sAction == "sendkeys":
                element.clear()
                element.send_keys(sData)
            elif sAction == "clear":
                element.clear()
            elif sAction == "submit":
                element.submit()
            elif sAction == "select":
                # Assuming you want to select an option from a dropdown
                from selenium.webdriver.support.ui import Select
                select = Select(element)
                select.select_by_visible_text(sData)
            elif sAction == "scroll_into_view":
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
            elif sAction == "hover":
                from selenium.webdriver.common.action_chains import ActionChains
                action = ActionChains(driver)
                action.move_to_element(element).perform()
            elif sAction == "double_click":
                from selenium.webdriver.common.action_chains import ActionChains
                action = ActionChains(driver)
                action.double_click(element).perform()
            elif sAction == "right_click":
                from selenium.webdriver.common.action_chains import ActionChains
                action = ActionChains(driver)
                action.context_click(element).perform()
            elif sAction == "press_enter":
                element.send_keys(Keys.ENTER)
            elif sAction == "press_tab":
                element.send_keys(Keys.TAB)
            elif sAction == "get_text":
                return element.text
            elif sAction == "get_attribute":
                return element.get_attribute(sData)  # sData should specify the attribute name

            str_log = f"Element : {objectNm} || Locator: {obj}  || Action : {sAction}  || Test Data: {sData}"
            time.sleep(1)
            self.lg.info(str_log)
        except Exception as e:
            self.lg.error(f"Error in kyPerformWebOperationWS: {str(e)}")

    # '====================================================================================================================================================
    # 'Function Description   : Navigate to required URL
    # 'Input Parameters:
    # 'Return Value:
    # 'Author: Vaishakh
    # 'UPDATED BY:
    # 'Date Created :
    # '====================================================================================================================================================
    def kyGetUrl(self, driver, url):
        driver = self.driver
        try:
            driver.get(url)
            driver.maximize_window()
            str_log = f"Launch URL: {url}"
            self.lg.info(str_log)
        except Exception as e:
            self.lg.error(f"Error while navigating to URL: {url} - {str(e)}")
