import functools
import logging
from typing import TypeVar, Callable, cast
from utils import current_test_id

F = TypeVar("F", bound=Callable[..., object])

def logg(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        test_id = current_test_id.get()
        prefix = f"[{test_id}]" if test_id else ""

        payload = ''
        if args:
            if hasattr(args[0], func.__name__):
                payload = str(args[1:]) if args[1:] else ''
            else:
                payload = str(args)
        if kwargs:
            payload += str(kwargs)
        try:
            logging.info(f"{prefix}|{func.__module__}|{func.__name__}|{payload}| Go:> ")
            result = func(*args, **kwargs)
            result_log = result if isinstance(result, (int, float, str, bool, type(None))) else getattr(result, "response", result)
            logging.info(f"{prefix}|{func.__module__}|{func.__name__}|{payload}| Return: {result_log}")
            return result
        except AssertionError as e:
            logging.error(f"{prefix}|{func.__module__}|{func.__name__}|{payload}| Assertion failed: {e}")
            raise
        except Exception as e:
            logging.error(f"{prefix}|{func.__module__}|{func.__name__}|{payload}| Error: {e}")
            raise
    return cast(F, wrapper)
