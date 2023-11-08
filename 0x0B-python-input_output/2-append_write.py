#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


def append_write(filename="", text=""):
    """
    This function appends text to a file
    Args:
        filename (str): name of the file.
        text (str): content tk append.
    """
    with open(filename, "a", encoding="UTF-8") as a_file:
        return a_file.write(str(text))
