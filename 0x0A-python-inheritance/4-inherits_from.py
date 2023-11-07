#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


def inherits_from(obj, a_class):
    """
    Checks if the obj is a sunclass inheriting from a_class
    Args:
        obj (object): the object inheriting.
        a_class (class): the super class.
    Return:
        True or False.
    """
    return issubclass(type(obj), a_class)
