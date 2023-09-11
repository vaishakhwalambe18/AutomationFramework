from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import ChromeDriver


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = webdriver.ChromeDriver(ChromeDriverManager().install)
    request.cls.driver = ch_driver

    yield
    ch_driver.close()
