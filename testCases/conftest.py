from selenium import webdriver
import pytest
import pytest_html

@pytest.fixture()
def setup(browser):
    print('----------------------------------------SET UP-----------------------------------')
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    return driver

    # yield
    # print('----------------------------------------TEAR DOWN-----------------------------------')
    # driver.quit()

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")



########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata["foo"] = "bar"
#     config._metadata['Project Name'] = 'TAF'
#     config._metadata['Module Name'] = 'DEBUG'
#     config._metadata['Tester'] = 'Admin'
#
# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)