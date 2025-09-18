import logging
from urllib.parse import urljoin
from abc import ABC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import Config
from utils.constant import ErrorCode


class BasePage(ABC):
    """The abstract class named BasePage class that is initialized on every page object class."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Config.EXPLICIT_WAIT_TIME)

    @staticmethod
    def classify_locator(locator: str) -> tuple:
        if locator.startswith('//'):
            return By.XPATH, locator
        elif any(char in locator for char in ['.', '#', '[', '*', ']']):
            return By.CSS_SELECTOR, locator
        else:
            return By.ID, locator

    def goto(self, url: str = '') -> None:
        if not url:
            url = Config.BASE_URL
        else:
            url = urljoin(Config.BASE_URL, url)
        self.driver.get(url)
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT_TIME)

    def find_element_light(self, main_locator, *backup_locator):
        """
        Use for static of website state
        """
        for _ in range(Config.RETRY_FIND_ELEMENT_TIMES):
            try:
                return self.driver.find_element(*self.classify_locator(main_locator))
            except Exception as e:
                logging.error(f"Element '{main_locator}' not found")

        if backup_locator:
            for loc in backup_locator:
                try:
                    return self.driver.find_element(*self.classify_locator(loc))
                except Exception as e:
                    logging.error(f"Backup element '{loc}' not found")
        raise Exception(ErrorCode.ELEMENT_NOT_FOUND)

    def find_elements_light(self, main_locator, *backup_locator):
        for _ in range(Config.RETRY_FIND_ELEMENT_TIMES):
            try:
                return self.driver.find_elements(*self.classify_locator(main_locator))
            except Exception as e:
                logging.error(f"Elements '{main_locator}' not found")

        if backup_locator:
            for loc in backup_locator:
                try:
                    return self.driver.find_elements(*self.classify_locator(loc))
                except Exception as e:
                    logging.error(f"Backup elements '{loc}' not found")
        raise Exception(ErrorCode.ELEMENT_NOT_FOUND)

    def find_element_heavy(self, main_locator, *backup_locator):
        """
            Use for dynamic of website state
        """
        for _ in range(Config.RETRY_FIND_ELEMENT_TIMES):
            try:
                return self.wait.until(EC.presence_of_element_located(self.classify_locator(main_locator)))
            except Exception as e:
                logging.error(f"Element '{main_locator}' not found")

        if backup_locator:
            for loc in backup_locator:
                try:
                    return self.wait.until(EC.presence_of_element_located(self.classify_locator(loc)))
                except Exception as e:
                    logging.error(f"Backup element '{loc}' not found")
        raise Exception(ErrorCode.ELEMENT_NOT_FOUND)

    def find_elements_heavy(self, main_locator, *backup_locator):
        for _ in range(Config.RETRY_FIND_ELEMENT_TIMES):
            try:
                return self.wait.until(EC.presence_of_all_elements_located(self.classify_locator(main_locator)))
            except Exception as e:
                logging.error(f"Element '{main_locator}' not found")

        if backup_locator:
            for loc in backup_locator:
                try:
                    return self.wait.until(EC.presence_of_all_elements_located(self.classify_locator(loc)))
                except Exception as e:
                    logging.error(f"Backup element '{loc}' not found")
        raise Exception(ErrorCode.ELEMENT_NOT_FOUND)

    def get_title(self):
        return self.driver.title

    def refresh(self):
        self.driver.refresh()
