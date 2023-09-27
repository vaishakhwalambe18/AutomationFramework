import shutil
import pytest
from selenium import webdriver
from selenium.common import WebDriverException
from Framework.lib_logger import ReportFolder
from Framework.lib_util import ReadConfig
import allure


# '====================================================================================================================================================
# 'Function Description   : Fixture - Session Level
# 'Input Parameters:
# 'Return Value:
# 'Author: Vaishakh
# 'UPDATED BY:
# 'Date Created :
# '====================================================================================================================================================
@pytest.fixture(scope='session')
def setup_class():
    try:
        rp = ReportFolder()
        current_exec_folder = rp.subCreateExecutionResultFolder()

        # Yield the folder to tests
        yield current_exec_folder
    finally:
        # Teardown code to copy the default report
        try:
            default_report_filepath = ReadConfig().getValue('common path', 'report_folder_path') + 'report.html'
            print(default_report_filepath, current_exec_folder)
            shutil.copy(default_report_filepath, current_exec_folder)
        except Exception as e:
            # Handle any exceptions during teardown gracefully
            print(f"Error during teardown: {str(e)}")


# '====================================================================================================================================================
# 'Function Description   : Fixture - Default
# 'Input Parameters:
# 'Return Value:
# 'Author: Vaishakh
# 'UPDATED BY:
# 'Date Created :
# '====================================================================================================================================================
@pytest.fixture
def setup(setup_class, browser):
    supported_browsers = {
        'chrome': webdriver.Chrome,
        'firefox': webdriver.Firefox,
        'edge': webdriver.Edge,
        'safari': webdriver.Safari,
        'opera': webdriver.Opera,
        # You can add more browsers as needed
    }

    if browser in supported_browsers:
        try:
            driver = supported_browsers[browser]()
        except WebDriverException as e:
            pytest.fail(f"Failed to create WebDriver for '{browser}': {str(e)}")
    else:
        pytest.fail(f"Unsupported browser: '{browser}'")

    implicit_wait_time = int(ReadConfig().getValue('common_variable', 'implicit_wait'))
    driver.implicitly_wait(implicit_wait_time)

    yield driver

    driver.quit()

# @pytest.fixture()
# def pytest_adoption(parser):  # This will get the value from CLI /hooks
#     parser.addoption("--browser")


# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata["foo"] = "bar"
#     config._metadata['Project Name'] = 'TAF'
#     config._metadata['Module Name'] = 'DEBUG'
#     config._metadata['Tester'] = 'Admin'
# #
# # # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
