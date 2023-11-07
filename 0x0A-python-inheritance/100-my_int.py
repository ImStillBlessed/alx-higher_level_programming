#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


class MyInt(int):
    """
    This module inverts == and !=
    Args:
        int (int): a valid integer
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
