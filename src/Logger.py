from pathlib import Path
from functools import wraps
import logging
import os

from Settings import get_log_path

__all__ = 'log'


# Attempt to create logs folder from path in env variables if it doesn't already exist, returns new path
def _generate_log_dir(path):
    try:
        Path(path).mkdir(exist_ok=True)
        return path
    except Exception as e:
        print(f'Error creating logging folder in specified location {path}')
        raise e


# Basic logger that creates/writes to path returned from _generate_log_dir
def _generate_log(path):
    logging.basicConfig(filename=f'{path}\\rekka_logs.log', filemode='a+')
    logger = logging.getLogger()
    logger.setLevel(os.environ['LOG_LEVEL'])
    file_handler = logging.FileHandler(f'{path}\\rekka_logs.log')
    log_format = '%(levelname)s %(asctime)s %(message)s'
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


# Wraps decorated function, logs arguments used to call function when DEBUG is enabled in env variables
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        path = get_log_path()
        logger = _generate_log(_generate_log_dir(path))
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.debug(f"function {func.__name__} called with args {signature}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")
            raise e
    return wrapper
