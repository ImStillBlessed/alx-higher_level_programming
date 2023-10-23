#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i, item in enumerate(my_list):
            while i <= x:
                print(item, end="")
                if i != x:
                    print(", ", end="")
        print("")
    except Exception as err:
        print(err)
    return i
