from .config.ConfigService import list_config_files, parse_config
from .resources.ResourceMap import *

session = get_boto3_session()


def interactive():
    config_file = input(f'{list_config_files()}\n'
                        f'Please select a configuration file from the directory:  ')
    service, operation, config_params = parse_config(config_file)
    return invoke_operation(session, *config_params)


def headless(*config_files):
    print("Running headless...\n\n"
          "Here's the config files you've selected: ")
    for file in config_files:
        print(f"File: {file}\n")
        print("Executing configuration file...\n")
        invoke_operation(session, *parse_config(file))
    return print("Finished processing all configuration files.")


def _repeat():
    repeat_flow = input('AWS request complete. Would you like to run more tests?:\n'
                        'Y/N?:   ')
    if repeat_flow == 'N':
        return
    elif repeat_flow == 'Y':
        return interactive()
    else:
        return
