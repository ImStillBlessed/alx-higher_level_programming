#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i, items in enumerate(my_list):
            if i < (x + 1):
                print(item, end="")
            if i != x:
                print(", ", end="")
        print("")
    except Exception as err:
        print(err)
    return i
