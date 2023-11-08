#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


import json


def to_json_string(my_obj):
    """
    This function returns a string in json format.
    Args:
        my_obj (str): the objevt to read as json.
    """
    return json.dumps(my_obj)
