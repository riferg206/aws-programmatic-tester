import functools
import logging
import os


def _generate_log(path):
    logging.basicConfig(filename='testlog.log', filemode='w')
    logger = logging.getLogger()
    logger.setLevel(os.environ['LOG_LEVEL'])
    file_handler = logging.FileHandler(path)
    log_format = '%(levelname)s %(asctime)s %(message)s'
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


def log(func, path='./src/apt/apt_logs/testlog.log'):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = _generate_log(path)
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.info(f"function {func.__name__} called with args {signature}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")
            raise e

    return wrapper
