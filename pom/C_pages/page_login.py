from pom.C_pages import *
from pom.A_locators.loc_login import locators
from config import Routes
from utils.logg import logg


class PageLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.response = {}  # Update this variable if you want return value

    @logg
    def enter_username(self, username: str):
        self.find_element_heavy(locators.loc_username).send_keys(username)
        return self

    @logg
    def enter_password(self, password: str):
        self.find_element_light(locators.loc_password).send_keys(password)
        return self

    @logg
    def click_login(self):
        self.find_element_light(locators.loc_login).click()
        return self

    @logg
    def verify_login_error_message(self, message: str) -> None:
        actual_message = self.find_element_heavy(locators.loc_login_error_msg).text
        self.response['actual_message'] = actual_message

        check.equal(actual_message, message, msg=AssertionMsg.LOGIN_FAIL_MESSAGE)
        return self

    @logg
    def verify_login_successfully(self) -> None:
        self.find_element_heavy(locators.loc_home_page)
        check.is_in(Routes.DASHBOARD, self.driver.current_url, msg=AssertionMsg.LOGIN_FAIL_MESSAGE)
        return self
