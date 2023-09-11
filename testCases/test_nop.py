from Framework.lib_util import ReadConfig, ReadExcel
from PageObjects.nop_login_page import Nop_loginPage


class Test_001_NopLogin:
    # Declarations
    curr_TcFileName = "Test_001_NopLogin"
    ModuleName = "NOP"
    dict_testcasedata = {}

    # 'Load Test Data from test data sheet
    current_module_TestData_path = ReadConfig.getValue('common path', 'testdata_path') + ModuleName + ".xlsx"
    dict_testcasedata = ReadExcel.loadDatafromExcel(current_module_TestData_path, curr_TcFileName, "ENV")

    def test_homepageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.dict_testcasedata.get('URL'))
        nopLP = Nop_loginPage(self.driver)
        nopLP.loginIntoApp(self.dict_testcasedata.get('UserName'), self.dict_testcasedata.get('Password'))
