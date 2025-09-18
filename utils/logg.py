import functools
import logging


def logg(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        payload = str(args) if args else ''
        payload += str(kwargs) if kwargs else ''

        try:
            logging.info(f"|{func.__name__}| {payload}| Go:> ")
            result = func(*args, **kwargs)
            logging.info(f"|{func.__name__}| {payload}| Return: {result}")
            return result
        except Exception as e:
            logging.error(f"|{func.__name__}| {payload}| error: {e}")
            raise e
    return wrapper
