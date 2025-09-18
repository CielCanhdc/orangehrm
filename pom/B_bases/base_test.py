import pytest

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, init_driver):
        self.driver = init_driver
        self.login = LoginStep(self.driver)
        self.employee = EmployeeStep(self.driver)