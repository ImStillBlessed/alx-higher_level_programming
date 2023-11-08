#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


def read_file(filename=""):
    """
    This function opens, reads and prints the content of a file
    Args:
        filename (str): the name of the file to read
    """
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
