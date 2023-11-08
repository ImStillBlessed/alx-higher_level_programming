#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


def write_file(filename="", text=""):
    """
    This function writes inout text to a file
    Args:
        filename (str): the name of the file to wfite to.
        text (str, int): the content to write to the file.

    the file is created if it doesnt exist and overwritten if it has content.
    """
    with open(filename, "w", encoding="UTF-8") as a_file:
        return a_file.write(str(text))
