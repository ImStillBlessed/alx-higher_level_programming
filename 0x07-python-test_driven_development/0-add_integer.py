#!/usr/bin/python3
"""This module adds two integers a and b
"""
def add_integer(a, b=98):
    """
    adds integers a and b
        b has a default value of 98

    args:
        a: first integer
        b: second integer default set to 98
    Returns:
        the sum of both integers
    Raises:
        TypeError with message a or b must be integers
    """
    if not instance(a, int):
        raise TypeError ("a must be an integer")
    if not instance(b, int):
        raise TypeError ("b must be an integer")
    return (a + b)
