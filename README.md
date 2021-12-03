# README #

Tiny framework designed for using pre-populated configuration files for rapid AWS testing

This project is implemented using a mostly functional style!

# Usage #

clone down and install

import apt

apt.invoke(*args)

to run in headless mode, substitute *args for a list names of your config files (as strings)

to run interactively, apt.invoke()

populate config files into the following directory structure to run your own custom configs:

\apt \ config\ configs\ {*service*}\ {*api_operation*}

See example files in source for formatting

Reference boto3 documentation for specific payloads and arguments to use in your config:
https://boto3.amazonaws.com/v1/documentation/api/1.9.88/reference/services/index.html
