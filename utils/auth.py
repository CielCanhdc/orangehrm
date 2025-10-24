import os
import pickle
import logging
from config import Path
auth_dir = os.path.join(Path.root, '.auth')


def save_logged_on_cookies(driver, username):
    """Save logged-on cookies from a Selenium WebDriver to a file."""

    cookie_path = os.path.join(auth_dir, f'cookies_{username}.pkl')
    os.makedirs(auth_dir, exist_ok=True)  # tạo folder nếu chưa có

    with open(cookie_path, 'wb') as file:
        pickle.dump(driver.get_cookies(), file)
    logging.info(f"Saved cookies to {cookie_path}")


def load_logged_on_cookies(driver, username):
    """Load logged-on cookies into Selenium WebDriver from a file."""
    # filepath = f'.auth/cookies_{username}.pkl'
    cookie_path = os.path.join(auth_dir, f'cookies_{username}.pkl')

    if not os.path.exists(cookie_path):
        logging.info(f"Cookie file not found: {cookie_path}")
        return False
    driver.delete_all_cookies()

    with open(cookie_path, 'rb') as file:
        cookies = pickle.load(file)
        logging.info(cookies)

    for cookie in cookies:
        driver.add_cookie(cookie)

    logging.info(f"Loaded cookies from {cookie_path}")
    driver.refresh()
    driver.implicitly_wait(5)
    return True
