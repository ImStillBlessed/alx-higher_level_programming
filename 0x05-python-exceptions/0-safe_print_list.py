#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for item in my_list:
            if (i >= x):
                break
            print(item, end="")
            i += 1
        print("")
    except Exception as err:
        print(err)
    return i
