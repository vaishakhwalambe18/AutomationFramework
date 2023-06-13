from Framework.lib_util import ReadConfig
from selenium import webdriver


class LoginPage:
    input_username = "username"
    input_id_search = "APjFqb"

    def __init__(self, driver):
        self.driver = driver


    def loginIntoApp(self):
        print('Testing test case')
        self.driver.find_element("id",self.input_id_search).clear()
        self.driver.find_element("id",self.input_id_search).send_keys(ReadConfig.getValue('common path','base_url_google'))
        # self.driver.get_url(ReadConfig.getValue('base_url_google'))
        # self.driver.find_element_by_id(self.input_username).clear()

        # print(dict_testcasedata['Browser'])

