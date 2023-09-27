from Framework.lib_web import webOperations
from Framework.lib_logger import LogGen as lg


class Nop_loginPage:
    textbox_username = "Email"
    textbox_password = "Password"
    button_login = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    label_welcome = "/html/body/div[3]/div[1]/div[1]/h1"

    def __init__(self, driver):
        self.driver = driver

    def loginIntoApp(self, username, password):
        # Declaration
        webOp = webOperations()
        # Actions
        webOp.kyPerformWebOperationWS("UserName", self.driver, "id", self.textbox_username, "sendkeys", username)
        webOp.kyPerformWebOperationWS("Password", self.driver, "id", self.textbox_password, "sendkeys", password)
        webOp.kyPerformWebOperationWS("Login button", self.driver, "xpath", self.button_login, "click", "")
        webOp.kyWaitUntilElementIsDisplayed("Welcome label", self.driver, "xpath", self.label_welcome)
        assert self.driver.title == 'Dashboard / nopCommerce administration'
        lg.save_screenshot(self.driver)
