import allure
from pom.C_pages import *
from pom.A_locators.loc_login import locators
from config import Routes
from utils import assertion


class PageLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.response = {}  # Update this variable if you want return value

    @logg
    @allure.step("Enter username: {username}")
    def enter_username(self, username: str):
        self.find_element_heavy(locators.loc_username).send_keys(username)
        return self


    @logg
    @allure.step("Enter password: {password}")
    def enter_password(self, password: str):
        self.find_element_light(locators.loc_password).send_keys(password)
        return self

    @logg
    @allure.step("Click login button")
    def click_login(self):
        self.find_element_light(locators.loc_login).click()
        return self

    @logg
    @allure.step("verify login error")
    def verify_login_error_message(self, message: str) -> None:
        actual_message = self.find_element_heavy(locators.loc_login_error_msg).text

        assertion.equal(actual_message, message)
        return self

    @logg
    @allure.step("verify login successfully")
    def verify_login_successfully(self) -> None:
        self.find_element_heavy(locators.loc_home_page)
        assertion.is_in(Routes.dashboard, self.driver.current_url, "Home page dashboard not found")
        return self
