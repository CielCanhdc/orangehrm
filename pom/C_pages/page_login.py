from pom.C_pages import *
from pom.A_locators.loc_login import locators
from config import Routes


class PageLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self, username: str):
        self.find_element_heavy(locators.loc_username).send_keys(username)
        return self

    def enter_password(self, password: str):
        self.find_element_light(locators.loc_password).send_keys(password)
        return self

    def click_login(self):
        self.find_element_light(locators.loc_login).click()
        return self

    def verify_login_error_message(self, message: str) -> None:
        assert self.find_element_heavy(locators.loc_login_error_msg).text == message, AssertionMsg.LOGIN_FAIL_MESSAGE

    def verify_login_successfully(self) -> None:
        self.find_element_heavy(locators.loc_home_page)
        assert Routes.DASHBOARD in self.driver.current_url, AssertionMsg.LOGIN_FAIL_MESSAGE