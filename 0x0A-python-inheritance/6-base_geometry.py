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
