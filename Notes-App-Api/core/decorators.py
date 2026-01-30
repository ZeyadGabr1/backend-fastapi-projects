from .logger import logging
from .exceptions import InternalError


def logging_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                reslut = func(*args, **kwargs)
                return reslut
            except Exception as e:
                logging.error(f"Error in {func.__name__}, error: {str(e)}")
                raise InternalError
        return wrapper