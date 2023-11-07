#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


class BaseGeometry():
    """
    This class defines basic geometry
    Attributes:
        area(): finds the area of the shape.
    Raises:
        Exception as the area is not implemented.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates if name is an integer.
        Args:
            name (str): the value name.
            value (int): rhe value assigned to the name.
        Raises:
            TypeError: if value is not type int.
            ValueError: if value is less < 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value


class Rectangle(BaseGeometry):
    """
    This class defines a rectangle shape
    Attributes:
        height (int): the height of the rectangle.
        width (int): the width of the rectangle.
    """
    def __init__(self, width, height):
        """
        initializes the rectangle class with width and height
        Args:
            height (int): height.
            width (int): width
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle]: {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    Defines a squarr form rectangle
    Attributes:
        size (int): the size of the square.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """finds the area of the square
        Returns:
            the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
