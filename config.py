class Config:
    baseUrl: str = 'https://opensource-demo.orangehrmlive.com/'
    browsers: list = ['chrome', 'firefox']
    headless: bool = False
    envLocator: str = 'default'  # Locator by environment: "Default | Staging" based on class name in A_locator classes
    numProcesses: int = 0  # <= Can not be use. it just store. please config in pytest.ini - addopts
    retryTestFailed: int = 0  # Config in pytest.ini

    useReportHtml: bool = False
    useReportAllure: bool = True
    reportHtmlPath: str = 'report/report.html'
    reportAllureDir: str = 'report/allure-results'

    retryFindElementTimes: int = 3  # second. use in base page
    explicitWait: int = 10  # use in base page
    implicitWait: int = 1  # use in base page
    screenshotFailure: bool = True


class Routes:
    login = 'web/index.php/auth/login'
    dashboard = 'web/index.php/dashboard/index'


class Grid:
    gridUrl = 'http://localhost:4444/wd/hub'
