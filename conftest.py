import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import Config, Grid
from utils.constant import ErrorCode


@pytest.fixture(scope='function', params=['chrome'])
def init_driver(request):
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ErrorCode.BROWSER_NOT_FOUND

    yield driver
    driver.quit()


@pytest.fixture(scope='function', params=Config.BROWSERS)
def driver_for_grid(request):
    browser = request.param
    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    else:
        raise ErrorCode.BROWSER_NOT_FOUND

    driver = webdriver.Remote(command_executor=Grid.GRID_URL, options=options)

    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()


def pytest_configure(config):
    logging.basicConfig(
        filename="report/logs_all.log",
        filemode="a",  # append, not overwrite
        level=logging.INFO,
        format="%(asctime)s %(levelname)s:> %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
