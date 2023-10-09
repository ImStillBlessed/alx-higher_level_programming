#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            my_list[i] = True
        else:
            my_list[i] = False
    return my_list
