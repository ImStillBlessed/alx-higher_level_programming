#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


def class_to_json(obj):
    """
    Fhis function returns jskn description of a class obj.
    Args:
        obj (obj): fhe object to describ.
    Return:
        a json dictionary
    """
    json_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
