import pytest
from Framework.lib_web import webOperations as wb
from Framework.lib_logger import LogGen
from Framework.lib_util import ReadConfig, ReadExcel
from PageObjects.nop_login_page import Nop_loginPage


@pytest.mark.usefixtures('setup')
class Test_001_NopLogin:
    # Declarations
    lg = LogGen.loggen()
    curr_TcFileName = "Test_001_NopLogin"
    ModuleName = "NOP"
    dict_TestCaseData = {}
    lg.info(f"******************** {curr_TcFileName} *******************")

    # 'Load Test Data from test data sheet
    current_module_TestData_path = ReadConfig.getValue('common path', 'testdata_path') + ModuleName + ".xlsx"
    dict_TestCaseData = ReadExcel.loadDatafromExcel(current_module_TestData_path, curr_TcFileName, "ENV")
    browser = str(dict_TestCaseData.get('Browser'))

    def test_homepageTitle(self, setup):
        self.lg.info("******************** Test: Home Page Title *******************")
        self.driver = setup
        # self.driver.get(self.dict_TestCaseData.get('URL'))
        wb.kyGetUrl(self, self.driver, self.dict_TestCaseData.get('URL'))
        nopLP = Nop_loginPage(self.driver)
        nopLP.loginIntoApp(self.dict_TestCaseData.get('UserName'), self.dict_TestCaseData.get('Password'))
        self.lg.info("******************** End Test: Login into app successful *******************")


@pytest.mark.usefixtures('setup')
class Test_002_NopLogin:
    # Declarations
    lg = LogGen.loggen()
    curr_TcFileName = "Test_001_NopLogin"
    ModuleName = "NOP"
    dict_TestCaseData = {}
    lg.info(f"******************** {curr_TcFileName} *******************")

    # 'Load Test Data from test data sheet
    current_module_TestData_path = ReadConfig.getValue('common path', 'testdata_path') + ModuleName + ".xlsx"
    dict_TestCaseData = ReadExcel.loadDatafromExcel(current_module_TestData_path, curr_TcFileName, "ENV")
    browser = str(dict_TestCaseData.get('Browser'))

    def test_homepageTitle(self, setup):
        self.lg.info("******************** Test: Home Page Title *******************")
        self.driver = setup
        # self.driver.get(self.dict_TestCaseData.get('URL'))
        wb.kyGetUrl(self, self.driver, self.dict_TestCaseData.get('URL'))
        print(self.driver.get_title())
        self.lg.info("******************** End Test: Login into app successful *******************")
