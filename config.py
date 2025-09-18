class Config:
    BASE_URL = 'https://opensource-demo.orangehrmlive.com/'
    BROWSERS = ['chrome', 'firefox']
    HEADLESS = False
    ENV_LOCATORS = 'dev'  # Default locator by environment


    RETRY_FIND_ELEMENT_TIMES = 3  # second. use in base page
    EXPLICIT_WAIT_TIME = 5  # use in base page
    IMPLICIT_WAIT_TIME = 1  # use in base page
    RETRY_TEST_FAILURE = 1


class Routes:
    LOGIN = 'web/index.php/auth/login'


class Grid:
    GRID_URL = 'http://localhost:4444/wd/hub'
