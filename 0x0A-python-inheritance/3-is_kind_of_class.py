#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


def is_kind_of_class(obj, a_class):
    """checks if an object is a subvlass of a specific class
    Args:
        obj (obj): the object to check.
        a_class (obj): The specific class to check.
    Return:
        True or False.
    """
    return isinstance(obj, a_class)
