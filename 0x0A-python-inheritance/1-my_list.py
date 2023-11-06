#!/usr/bin/python3
"""gets and sorts a list
Author: Oigbochie Blessed
"""


class MyList(list):
    """
    inherits from list and prints it sorted
    Args:
        list (obj): superclass
    Return: nothimg
    """
    def print_sorted(self):
        sorted_list = sorted(list)
        print(sorted_list)
