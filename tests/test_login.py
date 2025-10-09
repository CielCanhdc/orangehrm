import pytest
from utils.jiraa import jiraa
from pom.B_bases.base_test import BaseTest
from utils import assertion

class TestLogin(BaseTest):

    @jiraa(test_id='LOGIN-01')
    @pytest.mark.parametrize('username, passwd', [('Admin', 'admin123')])
    def test_login_successfully(self, username, passwd):
        # (self.login
        #     .enter_username(username)
        #     .enter_password(passwd)
        #     .click_login()
        #     .verify_login_successfully()
        #  )
        assertion.equal(1,1, 'test1')
        self.login.goto('https://facebook.com')


    @jiraa(test_id='LOGIN-02')
    @pytest.mark.parametrize('username, passwd, message', [('Admin', 'wrong pw', 'Invalid credential')])
    def test_login_invalid(self, username, passwd, message):
        # (self.login
        #     .enter_username(username)
        #     .enter_password(passwd)
        #     .click_login()
        #     .verify_login_error_message(message)
        #  )
        assertion.equal(1, 2, 'test2')
        self.login.goto('https://facebook.com')
