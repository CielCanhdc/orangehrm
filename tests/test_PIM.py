import pytest
from utils.logg import logg
from pom.B_bases.base_test import BaseTest


class TestPIM(BaseTest):

    @logg(test_id='PIM_01')
    # @pytest.mark.parametrize('username, passwd', [('Admin', 'admin123')])
    def test_create_a_basic_employee_successfully(self):
        self.login.step_login_successfully()
        self.pim.step_create_a_basic_employee()
