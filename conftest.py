import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import Config, Grid
from utils.constant import ErrorCode


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=cfg['runner']['browser'])

@pytest.fixture
def get_browser(request):
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture(scope='session')
def init_driver(request, get_browser):
    if get_browser == "chrome":
        driver = webdriver.Chrome()
    elif get_browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ErrorCode.BROWSER_NOT_FOUND
    driver.maximize_window()
    driver.implicitly_wait(Config.IMPLICIT_WAIT_TIME)

    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', params=Config.BROWSERS)
def driver_for_grid(request, get_browser):
    if get_browser == "chrome":
        options = ChromeOptions()
        # driver = webdriver.Chrome()
    elif get_browser == "firefox":
        options = FirefoxOptions()
        # driver = webdriver.Firefox()
    else:
        raise ErrorCode.BROWSER_NOT_FOUND

    driver = webdriver.Remote(command_executor=Grid.GRID_URL, options=options)


    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()