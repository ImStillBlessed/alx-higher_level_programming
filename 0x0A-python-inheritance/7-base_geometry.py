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
