import time

import allure
import pytest
from utils.jiraa import jiraa
from utils.logg import logg
from pom.B_bases.base_test import BaseTest
from utils import assertion


class TestLogin(BaseTest):

    @logg
    @pytest.mark.parametrize('login_info', [{'username': 'Admin', 'password': 'admin123'}])
    @allure.epic("Web interface")
    @allure.feature("Essential features")
    @allure.story("Authentication")
    @allure.id("TC-LOGIN-001")
    @allure.tag("NewUI", "Essentials", "Authentication")
    @allure.description("This test case is to verify that user can log in successfully with valid credentials.")
    @allure.issue("ABC-01")
    @allure.severity("Critical")
    @allure.title("Check log in successfully5")
    def test_login_successfully(self, login_info):
        self.login.step_login(login_info)
        time.sleep(50)

    @logg
    @pytest.mark.parametrize('login_info', [{'username': 'Admin', 'password': 'admin123'}])
    @allure.title("Check log in successfully66")
    def test_login_successfully66(self, login_info):
        self.login.step_login(login_info)
        time.sleep(10)

    # @logg
    # @pytest.mark.parametrize('username, passwd, message', [('Admin', 'wrong pw', 'Invalid credentials')])
    # @allure.epic("Web interface fail")
    # @allure.feature("Essential features")
    # @allure.story("Authentication")
    # @allure.id("TC-LOGIN-002")
    # @allure.title("Check log in fail5")
    # def test_login_invalid(self, username, passwd, message):
    #     (self.login
    #         .enter_username(username)
    #         .enter_password(passwd)
    #         .click_login()
    #         .verify_login_error_message(message)
    #      )
