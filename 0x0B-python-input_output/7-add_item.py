#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """
    This module loads content from json file and writes i
    to a new file in json.
    """
    filename = "add_item.json"
    if os.path.exists(filename):
        arg_list = load_from_json_file(filename)
    else:
        arg_list = []
    arg_list.extend(sys.argv[1:])
    save_to_json_file(arg_list, filename)
