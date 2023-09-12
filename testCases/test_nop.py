import pytest

from Framework.lib_logger import LogGen
from Framework.lib_util import ReadConfig, ReadExcel
from PageObjects.nop_login_page import Nop_loginPage


@pytest.mark.usefixtures('setup')
class Test_001_NopLogin:
    # Declarations
    curr_TcFileName = "Test_001_NopLogin"
    ModuleName = "NOP"
    dict_testcasedata = {}
    lg = LogGen.loggen()

    # 'Load Test Data from test data sheet
    current_module_TestData_path = ReadConfig.getValue('common path', 'testdata_path') + ModuleName + ".xlsx"
    dict_testcasedata = ReadExcel.loadDatafromExcel(current_module_TestData_path, curr_TcFileName, "ENV")
    browser = str(dict_testcasedata.get('Browser'))

    def test_homepageTitle(self, setup):
        self.driver = setup
        self.lg.info(f"******************** {self.curr_TcFileName} *******************")

        self.driver.get(self.dict_testcasedata.get('URL'))
        self.driver.maximize_window()

        nopLP = Nop_loginPage(self.driver)
        self.lg.info("******************** Login into app *******************")
        nopLP.loginIntoApp(self.dict_testcasedata.get('UserName'), self.dict_testcasedata.get('Password'))
        self.lg.info("******************** Login into app successfull *******************")
