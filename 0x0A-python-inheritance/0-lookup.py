#!/usr/bin/python3
"""
Prints all the attributes of an object
Author:
    Oigbochie Blessed
"""


def lookup(obj):
    """
    Thus function gets all tye attributes of obj
    Args:
        obj (object): the object to check.
    Return:
        list of all the attributes
    """
    return dir(obj)
