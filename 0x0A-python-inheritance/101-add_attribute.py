#!/usr/bin/python3
"""
Author: Oigbochie Blessed
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Thus module checks if its possinle to add new attributes
    Args:
        attr_name (str): the name of new attribute.
        attr_value (obj): the value for the new attribute.
    Raise:
        TypeError: if mo more attributes can be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
