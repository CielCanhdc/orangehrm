import os
import pickle
import logging


def save_logged_on_cookies(driver, username):
    """Save logged-on cookies from a Selenium WebDriver to a file."""
    os.makedirs('.auth', exist_ok=True)  # tạo folder nếu chưa có
    filepath = f'.auth/cookies_{username}.pkl'

    with open(filepath, 'wb') as file:
        pickle.dump(driver.get_cookies(), file)
    logging.info(f"Saved cookies to {filepath}")


def load_logged_on_cookies(driver, username):
    """Load logged-on cookies into Selenium WebDriver from a file."""
    filepath = f'.auth/cookies_{username}.pkl'

    if not os.path.exists(filepath):
        logging.info(f"Cookie file not found: {filepath}")
        return False
    driver.delete_all_cookies()

    with open(filepath, 'rb') as file:
        cookies = pickle.load(file)
        logging.info(cookies)

    for cookie in cookies:
        driver.add_cookie(cookie)

    logging.info(f"Loaded cookies from {filepath}")
    driver.refresh()
    driver.implicitly_wait(5)
    return True
