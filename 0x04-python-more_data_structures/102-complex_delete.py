#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None

    keys_del = [key for key, val in a_dictionary.items() if val == value]

    for key in keys_del:
        a_dictionary.pop(key)

    return a_dictionary
