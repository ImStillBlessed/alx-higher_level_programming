#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a new line of text after a specific string
        in that file.
    Args:
        filename (str): the name of the file.
        search_string: the specific strimg to get position from.
        new_strimg: the new string to add.
    """
    with open(filename, encoding="utf-8") as a_file:
        lines = a_file.readlines()
    with open(filename, "w" encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search string in line:
                file.write(new_string)
