from configparser import RawConfigParser
from pathlib import Path, PurePath

from ..Logger import log
import ast

__all__ = ("list_config_files", "parse_config")

path_lib = Path
pure_path_lib = PurePath
package_path = Path(__file__).parent.resolve()


def list_config_files(service, operation):
    return [pure_path_lib(path).name for path in path_lib.iterdir(package_path / 'configs' / service / operation)]


def parse_config(config_file):
    parser = RawConfigParser()
    parser.optionxform = lambda option: option
    arg_dict = {}
    file = sorted(path_lib().rglob(config_file))
    parser.read(f'{pure_path_lib(file[0])}')
    parent_path = str(pure_path_lib(file[0].parents[0]))
    service, operation = parent_path.split('\\')[4:]
    for section_name in parser.sections():
        for name, value in parser.items(section_name):
            arg_dict.update(_interpolate_config_values(name, value))
        return service, operation, arg_dict


@log
def _interpolate_config_values(arg_name, arg_val):
    if arg_val.startswith("\'{"):
        return {arg_name: arg_val.strip("'")}
    else:
        return {arg_name: ast.literal_eval(arg_val)}
