import functools
import logging


def logg(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        payload = ''
        # Handle clean log for payload. Remove "self" argument in log
        if args:
            # If first arg looks like "self", skip it
            if hasattr(args[0], func.__name__):
                payload = str(args[1:])
            else:
                payload = str(args)
        if kwargs:
            payload += str(kwargs)

        try:
            logging.info(f"{func.__module__}|{func.__name__}| {payload}| Go:> ")

            result = func(*args, **kwargs)

            result_log = result if isinstance(result, (int, float, str, bool, type(None))) else getattr(result, "response", result)
            logging.info(f"{func.__module__}|{func.__name__}| {payload}| Return: {result_log}")
            return result
        except Exception as e:
            logging.error(f"{func.__module__}|{func.__name__}| {payload}| Error: {e}")
    return wrapper
