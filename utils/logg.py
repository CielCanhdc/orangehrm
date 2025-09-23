import functools
import logging
from typing import TypeVar, Callable, cast

F = TypeVar("F", bound=Callable[..., object])

def logg(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        payload = ''
        if args:
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
    return cast(F, wrapper)
