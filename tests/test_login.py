import pytest
from utils.logg import logg
from pom.B_bases.base_test import BaseTest
from pom.D_steps.step_login import StepLogin


class TestLogin(BaseTest):

    # @logg
    @pytest.mark.parametrize('username, passwd', [('Admin', 'admin123')])
    def test_login_successfully(self, username, passwd):
        self.login\
            .enter_username(username)\
            .enter_password(passwd)\
            .click_login()\
            .verify_login_successfully()

    # @logg
    @pytest.mark.parametrize('username, passwd, message', [('Admin', 'wrong pw', 'Invalid credential')])
    def test_login_invalid(self, username, passwd, message):
        self.login\
            .enter_username(username)\
            .enter_password(passwd)\
            .click_login()\
            .verify_login_error_message(message)