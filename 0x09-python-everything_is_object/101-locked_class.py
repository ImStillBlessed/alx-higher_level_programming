#!/usr/bin/python3
"""This module creates a locked class
Author:
    Oigbochie Blessed
"""


class LockedClass:
    """
        This class defines a class first name on5ly
            any other objects or class is rejected

        Attributes:
            none
    """
    def __setattr__(self, name, value):
        """
        Args:
            name (str): the name of the object <firstname>
            value (str): value passed to the firstname
        Raises:
            AttributeError: if the attribute is mot first name
        """
        if name != 'first_name':
            error = "'LockedClass' object has no attribute '{}'".format(name)
            raise AttributeError(error)
        else:
            super().__setattr__(name, value)
