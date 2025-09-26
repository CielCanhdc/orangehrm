import pytest
from utils.logg import logg
from pom.B_bases.base_test import BaseTest
from utils.jiraa import jiraa


class TestPIM(BaseTest):

    @jiraa(test_id='PIM_01')
    def test_create_a_basic_employee_successfully(self):
        self.login.step_login()
        self.pim.step_create_a_basic_employee()

        # Verify created record in table (example: lastname)
        lastname_table_index = self.pim.common.response['table_header'].index('Last Name')
        data_column = list(map(lambda i: i[lastname_table_index], self.pim.common.response['data_table']))
        for it in data_column:
            assert self.pim.response['lastname'] in it
