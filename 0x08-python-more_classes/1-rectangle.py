#!/usr/bin/python3
"""
a rectangle class
Author:
    Oigbochie Blessed
"""


class Rectangle():
    """
    This class defines a rectangle

    Attributes:
        __width (int): private attribute that defines width of the rectangle
        __height (int): private atribute that defines height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Constructs a rectangle with given width and height

        Args:
            width (int): the width of the rectangle, default 0.
            height (int): the height ofbthe rectangle, default 0.
        Raises:
            ValueError: if the value is less that 0.
            TypeError: if the values are not integers.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            This method retreives the value of the width attribute
            Returns:
                int: value of __width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an interger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            This method retreives the value of the height attribute
            Returns:
                int: value of __height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("haight must be >= 0")
        self.__height = value

