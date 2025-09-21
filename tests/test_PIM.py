import pytest
from utils.logg import logg
from pom.B_bases.base_test import BaseTest
from utils.jiraa import jiraa


class TestPIM(BaseTest):

    @jiraa(test_id='PIM_01')
    def test_create_a_basic_employee_successfully(self):
        self.login.step_login_successfully()
        self.pim.step_create_a_basic_employee()

    @jiraa(test_id='PIM-02')
    def test_create_a_basic(self):
        print(1111)