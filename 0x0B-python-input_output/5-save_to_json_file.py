#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This functikn writes the my_obj to a file in json.
    Args:
        my_obj (obj): the object to write as json in the file.
        filename (str): the name of the fole to write to.
    """
    with open(filename, "w", encoding="UTF-8") as a_file:
        json_format = json.dumps(my_obj)
        return a_file.write(json_format)
