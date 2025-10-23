import allure
from pom.D_steps import *
from pom.C_pages.page_login import PageLogin
from utils.dummy import default_admin_authentication
from utils.auth import load_logged_on_cookies


class StepLogin(PageCommon, PageLogin):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Step: Log in")
    def step_login(self, authentication_info: dict = None):
        authentication_info = {} if not authentication_info else authentication_info
        data = default_admin_authentication()
        data.update(authentication_info)

        result = load_logged_on_cookies(self.driver, data['username'])
        if not result:
            (self
             .enter_username(data['username'])
             .enter_password(data['password'])
             .click_login()
             .verify_login_successfully()
             .get_cookies_after_login(data['username'])
             )