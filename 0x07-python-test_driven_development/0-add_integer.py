#!/usr/bin/python3
"""This module adds two integers a and b
Authour:
    Oigbochie Blessed
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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
