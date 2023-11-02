#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


def text_indentation(text):
    """
    This function indents a string anytime it encounters
        '.' '?' and ':'
    Args:
        text (str): the strimg to read through and indent.
    Raises:
        TypeError: if the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char == "." or char == "?" or char == ":":
            print("{}".format(char), end="")
            print("")
            print("")
        else:
            print("{}".format(char), end="")
