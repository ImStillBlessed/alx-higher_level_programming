#!/usr/bin/python3
"""
This module takes arguments first name & or last name
    and prints out the result
Authors:
    Oigbochie Blessed
"""


def say_my_name(first_name, last_name=""):
    """This function prints
        a greeting
        Args:
            first_name (str): the first name of the person.
            last_name (str): the last name default empty
        Raises:
            TypeError:
                if either values are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
