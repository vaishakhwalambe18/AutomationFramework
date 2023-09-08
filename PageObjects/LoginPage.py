from Framework.lib_util import ReadConfig
from selenium import webdriver


class nop_loginPage:
    textbox_username = "Email"
    textbox_password = "password"
    button_login = "Log in"
    label_welcome = "Welcome to your store!"
    def __init__(self, driver):
        self.driver = driver


    def loginIntoApp(self):
        self.driver.find_element("id",self.textbox_username).clear()
        self.driver.find_element("id",self.textbox_username).send_keys('admin@yourstore.com')
        self.driver.find_element("id",self.textbox_password).send_keys('123445')
        self.driver.find_element("linktext",self.button_login).click()
        self.driver.find_element("linktext", self.label_welcome).
        # self.driver.get_url(ReadConfig.getValue('base_url_google'))
        # self.driver.find_element_by_id(self.input_username).clear()

        # print(dict_testcasedata['Browser'])

