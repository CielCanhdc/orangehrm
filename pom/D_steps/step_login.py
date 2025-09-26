from pom.D_steps import *
from pom.C_pages.page_login import PageLogin
from utils.dummy import default_admin_authentication


class StepLogin(PageCommon, PageLogin):

    def __init__(self, driver):
        super().__init__(driver)

    def step_login(self, authentication_info: dict = None):
        authentication_info = {} if not authentication_info else authentication_info
        data = default_admin_authentication()
        data.update(authentication_info)

        (self
         .enter_username(data['username'])
         .enter_password(data['password'])
         .click_login()
         .verify_login_successfully()
         )