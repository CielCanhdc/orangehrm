class Config:
    BASE_URL = 'https://opensource-demo.orangehrmlive.com/'
    BROWSERS = ['chrome', 'firefox']
    HEADLESS = False
    ENV_LOCATORS = ''  # Locator by environment: Default | Staging based on class name in A_locator classes

    RETRY_FIND_ELEMENT_TIMES = 3  # second. use in base page
    EXPLICIT_WAIT_TIME = 10  # use in base page
    IMPLICIT_WAIT_TIME = 1  # use in base page
    RETRY_TEST_FAILURE = 1


class Routes:
    LOGIN = 'web/index.php/auth/login'
    DASHBOARD = 'web/index.php/dashboard/index'


class Grid:
    GRID_URL = 'http://localhost:4444/wd/hub'
