import pytest
from abc import ABC
from pom.D_steps.step_login import StepLogin
from pom.D_steps.step_PIM import StepPIM


@pytest.mark.usefixtures("init_driver")
class BaseTest(ABC):
    @pytest.fixture(autouse=True)
    def setup(self, init_driver):
        self.driver = init_driver
        self.login = StepLogin(self.driver)
        self.pim = StepPIM(self.driver)
        self.login.goto()
