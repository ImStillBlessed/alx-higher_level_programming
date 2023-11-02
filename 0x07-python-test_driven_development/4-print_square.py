#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


def print_square(size):
    """
    This function prints a square of size 'size' using '#'
    Args:
        size (int): size of the square
    Raises:
        TypeError: if the size is not integer or a float but less than 
        ValueError: if size is < 0.
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")
    for i in range(int(size)):
        for j in range(int(size)):
            print("#", end="")
        print("")
