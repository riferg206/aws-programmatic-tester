from boto3 import Session

from .Logger import log
from .config.ConfigService import list_config_files, parse_config
from .resources.ResourceMap import *

session = get_boto3_session()


def interactive():
    service_prompt = input(f'{list_available_services(session)}\n'
                           f'Please select a service:  ')
    operation = input(f'{list_service_methods(session, service_prompt)}\n'
                      f'Please select an operation for your chosen resource {service_prompt}:  ')
    config_file = input(f'{list_config_files(service_prompt, operation)}\n'
                        f'Please select a configuration file from the {service_prompt} directory:  ')
    service, operation, config_params = parse_config(config_file)
    return invoke_operation(session, service_prompt, operation, config_params)


def headless(*config_files):
    print("I'm the sequential flow! Here's the config files you've selected: ")
    for file in config_files:
        print(f"\n{file}")
        print("Executing configuration file...")
        invoke_operation(session, parse_config(file))
    return print("Finished processing all configuration files.")


def _repeat():
    repeat_flow = input('AWS request complete. Would you like to run more tests?:\n'
                        'Y/N?:   ')
    if repeat_flow == 'N':
        return
    else:
        interactive()
