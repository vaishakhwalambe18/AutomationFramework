import time
from builtins import str
import requests
from PageObjects.LoginPage import LoginPage
from selenium import webdriver
from Framework.lib_util import *
from Framework.lib_logger import LogGen
import pytest


class Test_TC001_Module:
    curr_TcFileName = "TC001_TestCase_001"
    ModuleName = "Module1"
    base_url = ReadConfig.getValue('common path', 'base_url_google')
    current_module_TestData_path = ReadConfig.getValue('common path', 'testdata_path') + ModuleName + ".xlsx"
    dict_testcasedata = {}
    dict_testcasedata = ReadExcel.loadDatafromExcel(current_module_TestData_path, curr_TcFileName, "ENV")
    current_module_TestData_path = ReadConfig.getValue('common path', 'testdata_path') + ModuleName + ".xlsx"

    logger = LogGen.loggen()

    def descope_test_loginIntoApp(self,setup):
        self.logger.info("**************TEST CASE ID " + self.curr_TcFileName + "****************")
        self.driver = setup
        self.driver.get(self.base_url)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.loginIntoApp()
        assert self.driver.title == 'Google'
        self.driver.save_screenshot(".\\Reports\\" + "sc1.png")
        self.driver.close()
        str_end_point = 'https://reqres.in/api/users/?q=id=507'
        response = requests.get(str_end_point)
        assert response.status_code == 200
        pass
        print(response)
    def descope_test_lauchGoogle(self,setup):
        self.logger.info("**************TEST CASE ID 2" + self.curr_TcFileName + "****************")
        self.driver = setup
        self.driver.get(self.base_url)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.loginIntoApp()
        self.driver.save_screenshot(".\\Reports\\" + "sc3.png")
        self.driver.close()