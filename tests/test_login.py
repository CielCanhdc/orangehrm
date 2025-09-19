import logging

import pytest
from utils.logg import logg
from pom.B_bases.base_test import BaseTest


class TestLogin(BaseTest):

    @logg(test_id='LOGIN_01')
    @pytest.mark.parametrize('username, passwd', [('Admin', 'admin123')])
    def test_login_successfully(self, username, passwd):
        (self.login
            .enter_username(username)
            .enter_password(passwd)
            .click_login()
            .verify_login_successfully()
         )

    @logg(test_id='LOGIN_02')
    @pytest.mark.parametrize('username, passwd, message', [('Admin', 'wrong pw', 'Invalid credential')])
    def test_login_invalid(self, username, passwd, message):
        (self.login
            .enter_username(username)
            .enter_password(passwd)
            .click_login()
            .verify_login_error_message(message)
         )

