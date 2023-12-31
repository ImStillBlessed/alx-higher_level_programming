#!/usr/bin/python3
"""
This module defines a square with private size
by Oigbochie Blessed
"""


class Square:
    """
    This class defines a square

    Attributes:
        __size (int): This is the size f the square
    """
    def __init__(self, size):
        """
        Constructs a square with the given size

        Args:
            size (int): the size of the square. Default of 0 if not provided
        """
        self.__size = size
