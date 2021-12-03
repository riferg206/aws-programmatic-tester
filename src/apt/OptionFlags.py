import functools
import base64
from time import sleep


def decode_b64(encoded_data):
    return base64.standard_b64decode(encoded_data)

    
