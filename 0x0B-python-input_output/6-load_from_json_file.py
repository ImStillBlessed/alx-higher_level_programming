#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


import json


def load_from_json_file(filename):
    """
    This function loads and object from a file in json format to python.
    Args:
        filename (str): the name of the file.
    """
    with open(filename, encoding="UTF-8") as a_file:
        return json.loads(a_file.read())
