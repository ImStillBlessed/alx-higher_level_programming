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
        if name != 'first_name':
            error = "'LockedClass' object has no attribute '{}'".format(name)
            raise AttributeError(error)
        else:
            super().__setattr__(name, value)
