from pom.C_pages import *
from pom.A_locators.loc_common import locators
from utils.constant import fields_type, FieldTypes


class PageCommon(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.response = {}  # Update this variable if you want return value

    @logg
    def click_menu_by_name(self, menu_item: str):
        self.find_element_heavy(locators.loc_mnu_menuItem % menu_item).click()
        return self

    @logg
    def click_top_bar_by_name(self, menu_item: str, sub_menu_item: str = None):
        self.find_element_light(locators.loc_mnu_topBarItem % menu_item).click()
        if sub_menu_item:
            self.find_element_heavy(locators.loc_mnu_topBarSubItem % sub_menu_item).click()
        return self

    @logg
    def verify_toast_message(self, message):
        self.response['toast_message'] = self.find_element_heavy(locators.loc_tos_toastMessage).text

        check.is_in(message, self.response['toast_message'])
        return self

    def input_search_by_dealer(self, item: dict[str, str]):
        """
        item = {"Employee Name": "test name"}

        :flow: Based on field type defined "fields_type". Deliver the corresponding actions
        """
        (key, value) = item
        if fields_type[key] == FieldTypes.TEXT:
            self.find_element_light(locators.loc_txt_inSearchTextBox % key).send_keys(value)
        elif fields_type[key] == FieldTypes.SELECT:
            self.find_element_light(locators.loc_dpd_inSearchSelectBox % key).click()
            self.find_element_heavy(locators.loc_opt_inSearchSelectOption % value).click()
        elif fields_type[key] == FieldTypes.DATE:
            pass

    @logg
    def search_filter(self, search_payload: dict = None):
        if search_payload:  # is not None
            for item in search_payload.items():
                self.input_search_by_dealer(item)

            self.find_element_light(locators.loc_btn_search).click()  # Click search
        return self

    @logg
    def get_table_headers(self):
        self.response['table_header'] = list(map(lambda i: i.text,
                                                 self.find_elements_light(locators.loc_lbl_tableHeaders)))

    @logg
    def get_table(self, page: int = 0):
        rows = self.find_elements_heavy(locators.loc_tbl_tableRows)
        data_table = []
        for row in rows:
            data_table.append(list(map(lambda i: i.text,
                                       row.find_element(locators.loc_tbl_tableCells))))

        self.response['data_table'] = data_table
