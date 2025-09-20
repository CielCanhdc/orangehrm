from pom.C_pages import *
from pom.A_locators.loc_common import locators


class PageCommon(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.response = {}  # Update this variable if you want return value

    def click_menu_by_name(self, menu_item: str):
        self.find_element_heavy(locators.loc_mnu_menuItem % menu_item).click()
        return self

    def click_top_bar_by_name(self, menu_item: str, sub_menu_item: str = None):
        self.find_element_light(locators.loc_mnu_topBarItem % menu_item).click()
        if not sub_menu_item:
            self.find_element_heavy(locators.loc_mnu_topBarSubItem % sub_menu_item).click()
        return self

    @logg
    def verify_toast_message(self, message):
        # self.response['toast_message'] = ''
        self.response['toast_message'] = self.find_element_heavy(locators.loc_tos_toastMessage).text
        # try:
        #
        # except Exception as e:
        #     pass

        check.is_in(message, self.response['toast_message'])
        return self
