import os


def get_config_path():
    return f'{os.environ["CONFIG_PATH"]}\\rekka_configs'


def get_log_path():
    return f'{os.environ["LOG_PATH"]}\\rekka_logs'

