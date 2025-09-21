import functools
import logging
from utils.logg import logg


def jira_decorator(test_id: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if test_id:
                logging.info(f'---------------- {test_id} ----------------')
            result = func(*args, **kwargs)
            logging.info("Uploaded test result into Jira")
            return result
        return wrapper
    return decorator


def jiraa(test_id):
    """Combine jira with log. Use this decorator in test file"""
    def decorator(func):
        return jira_decorator(test_id)(logg(func))
    return decorator
