import pytest
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import Config, Grid
from utils.constant import ErrorCode
from utils.screenshot import screenshot_failure


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
    """Set up logging"""
    today = datetime.now().strftime("%Y-%m-%d")
    log_filename = f"report/logs_{today}.log"
    logging.basicConfig(
        filename=log_filename,
        filemode="a",  # append, not overwrite
        level=logging.INFO,
        format="%(asctime)s %(levelname)s:> %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    #  Set up report types
    if Config.USE_REPORT_HTML:
        config.option.htmlpath = "report/report.html"
        config.option.self_contained_html = True
    if Config.USE_REPORT_ALLURE:
        config.option.allure_report_dir = "report/allure-results"

    # Setup num processes for pytest-xdist
    config.option.numprocesses = Config.NUM_PROCESSES

    # Set up others
    config.option.disable_warnings = True
    config.option.pythonwarnings = "ignore::DeprecationWarning"


class MemoryLogHandler(logging.Handler):
    """Collect logs in memory for each test"""
    def __init__(self):
        super().__init__()
        self.logs = []

    def emit(self, record):
        msg = self.format(record)
        self.logs.append(msg)


@pytest.fixture(autouse=True)
def capture_logs_per_test(request):
    """Trích xuất Log steps ra, push lên googlesheet realtime"""
    handler = MemoryLogHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)s:> %(message)s",
                                  datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(handler)

    yield

    # # --- Teardown section ---
    # print("\n------ Captured logs (from logger) ------")
    # for line in handler.logs:
    #     print(line)
    print(handler.logs)
    logger.removeHandler(handler)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attact ảnh chụp màn hình tại thời điểm fail vào report html
    """
    outcome = yield
    report = outcome.get_result()

    pytest_html = item.config.pluginmanager.getplugin("html")
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            screenshot_path = screenshot_failure(item)
            extra.append(pytest_html.extras.image(screenshot_path, '')) if screenshot_path else None

        report.extra = extra