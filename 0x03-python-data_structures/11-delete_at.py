#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) <= idx or idx < 0:
        return my_list
    i = 0
    new_list = my_list
    while i < len(my_list):
        if i != idx:
            new_list.remove(my_list[i])
        i += 1
    return new_list
