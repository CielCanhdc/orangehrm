import logging

from pom.D_steps import *
from pom.C_pages.page_login import PageLogin


class StepLogin(PageCommon, PageLogin):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver