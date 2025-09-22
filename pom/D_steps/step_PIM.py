from pom.D_steps import *
from pom.C_pages.page_PIM import PagePIM
from utils.dummy import fake_employee_info


class StepPIM(PageCommon, PagePIM):

    def __init__(self, driver):
        PageCommon.__init__(self, driver)
        self.resCommon = self.response

        PagePIM.__init__(self, driver)
        self.resPIM = self.response
        self.driver = driver

    @logg
    def step_create_a_basic_employee(self, basic_employee: dict = None):
        basic_employee = {} if not basic_employee else basic_employee
        data = fake_employee_info()
        data.update(basic_employee)

        self.click_menu_by_name(menu_item='PIM')

        (self
         .click_add()
         .enter_employee_firstname(data['firstname'])
         .enter_employee_middlename(data['middlename'])
         .enter_employee_lastname(data['lastname'])
         .enter_employee_id(data['employee_id'])
         .click_save()
         )

        self.verify_toast_message('Successfully Saved')

        self.click_top_bar_by_name(menu_item='Employee List')
        self.search_filter({"Employee Name": self.resPIM['lastname']})

        self.get_table_headers()
        self.get_table()


