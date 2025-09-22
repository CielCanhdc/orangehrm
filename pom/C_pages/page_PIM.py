from pom.C_pages import *
from pom.A_locators.loc_PIM import locators


class PagePIM(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.response = {}  # Update this variable if you want return value

    @logg
    def enter_employee_firstname(self, firstname: str = None):
        self.find_element_heavy(locators.loc_txt_firstName).send_keys(firstname)

        self.response['employee_firstname'] = firstname
        return self

    @logg
    def enter_employee_middlename(self, middlename: str = None):
        self.find_element_light(locators.loc_txt_middleName).send_keys(middlename)

        self.response['middlename'] = middlename
        return self

    @logg
    def enter_employee_lastname(self, lastname: str = None):
        self.find_element_light(locators.loc_txt_lastName).send_keys(lastname)

        self.response['lastname'] = lastname
        return self

    @logg
    def enter_employee_id(self, employee_id: str):
        element = self.find_element_light(locators.loc_txt_employeeId)
        element.clear()
        element.send_keys(employee_id)
        self.response['employee_id'] = employee_id
        return self

    @logg
    def click_save(self):
        self.find_element_light(locators.loc_btn_save).click()
        return self

    @logg
    def click_add(self):
        self.find_element_heavy(locators.loc_btn_add).click()
        return self
