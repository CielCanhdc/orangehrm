from pom.D_steps import *
from pom.C_pages.page_login import PageLogin


class StepLogin(PageCommon, PageLogin):

    pass

    # def step_login_successfully(self, username, password):
    #     self.enter_username(username) \
    #         .enter_password(password) \
    #         .click_login() \
    #         .verify_login_successfully()
    #
    #     return self
    #
    # def step_login_with_invalid_data(self, username, password, expected_msg):
    #     self.enter_username(username) \
    #         .enter_password(password) \
    #         .click_login() \
    #         .verify_login_error_message(expected_msg)
    #
    #     error_msg = self.get_login_state_message()
    #     assert error_msg == expected_msg, "Step: login message with invalid data failed"