#!/usr/bin/python3
"""
Author: Oigbochie Blessed
Task 2.
"""
class Square:
    """
    This is a class of a square with size

    Attributes:
        __size (int): this is the size of the square.
    """
    def __init__(self, size=0):
        """
        Constructs a square with a given size.

        Args:
            size (int): The size of the square.
                Default is 0 if not provided.
        Raises:
            TypeError: If the size given is not a number
            ValueError: If the value is less than 0.
        """
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
