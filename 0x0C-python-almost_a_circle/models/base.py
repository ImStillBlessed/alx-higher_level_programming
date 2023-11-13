#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


class Base:
    """
    This is the base class for managing id
    Attributes:
        nb_object
        id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor
        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
