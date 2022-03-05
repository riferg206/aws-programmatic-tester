from pathlib import Path
import yaml

from Settings import get_config_path
from Logger import log

__all__ = ("list_config_files", "parse_config", "generate_config_path")


def list_config_files():
    return Path.iterdir(get_config_path())


@log
def parse_config(config_file):
    if read_config(config_file).values() is None: return "Empty configuration file. Aborting process"
    return [value for value in read_config(config_file).values()]


def read_config(config_file):
    try:
        with open(f'{get_config_path()}\\{config_file}.yml') as file:
            configuration = yaml.safe_load(file)
            return configuration
    except Exception(f'Error reading config in specified location: {get_config_path()}') as e:
        raise e


def generate_config_path(path):
    try:
        Path(path).mkdir(exist_ok=True)
        return path
    except Exception(f'Error creating config folder in specified location: {path}') as e:
        raise e
