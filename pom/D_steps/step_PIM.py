import logging
from pom.D_steps import *
from pom.C_pages.page_PIM import PagePIM
from utils.dummy import fake_employee_info


class StepPIM(PagePIM):

    def __init__(self, driver):
        super().__init__(driver)
        self.common = PageCommon(driver)

    @logg
    def step_create_a_basic_employee(self, basic_employee: dict = None):
        basic_employee = {} if not basic_employee else basic_employee
        data = fake_employee_info()
        data.update(basic_employee)

        self.common.click_menu_by_name(menu_item='PIM')

        (self
         .click_add()
         .enter_employee_firstname(data['firstname'])
         .enter_employee_middlename(data['middlename'])
         .enter_employee_lastname(data['lastname'])
         .enter_employee_id(data['employee_id'])
         .click_save()
         )

        (self.common
         .click_top_bar_by_name(menu_item='Employee List')
         .search_filter({"Employee Name": self.response['lastname']})
         .get_table_headers()
         .get_table())

        logging.info(f"resCommon :> {self.common.response}")
        logging.info(f"res PIM:> {self.response}")


        # lastname_table_index = self.response['table_header'].index('Last Name')
        # data_column = list(map(lambda i: i[lastname_table_index], self.response['data_table']))
        # for it in data_column:
        #     assert self.resPIM['lastname'] in it
