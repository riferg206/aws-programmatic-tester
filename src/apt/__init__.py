from .FlowService import interactive, headless


#: Pass in valid config file names as strings to run headless, call without args to run interactively
def invoke(*config_files):
    return headless(*config_files) if config_files else interactive()


__all__ = 'invoke'
