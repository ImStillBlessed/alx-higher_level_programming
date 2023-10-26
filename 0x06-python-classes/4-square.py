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
        self.size = size

    @property
    def size(self):
        """
        This method retrives the value of the size attribute

        Returns:
            int: the value of the __size attribute.
        """
        return self.__size

    def area(self):
        """
        This method calc the current square area using size

        Returns: The square area
        """
        return (self._Square__size ** 2)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        if value < 0:
             raise TypeError("size must be >= 0")
        self.__size = value
