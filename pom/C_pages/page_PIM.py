from pom.C_pages import *
from pom.A_locators.loc_PIM import locators


class PagePIM(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.response = {}  # Update this variable if you want return value

    def enter_employee_firstname(self, firstname: str = None):
        firstname = 'fake' if not firstname else firstname

        self.find_element_heavy(locators.loc_txt_firstName).send_keys(firstname)

        self.response['firstname'] = firstname
        return self

    def enter_password(self, password: str):
        self.find_element_light(locators.loc_password).send_keys(password)
        return self

    def click_login(self):
        self.find_element_light(locators.loc_login).click()
        return self