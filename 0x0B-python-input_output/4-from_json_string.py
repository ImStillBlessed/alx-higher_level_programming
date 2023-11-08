#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


import json


def from_json_string(my_str):
    """
    This function prints a string represented in json format
    Args:
        my_str (str): the string to convert
    """
    return json.loads(my_str)
