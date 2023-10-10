#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) <= idx or idx < 0:
        return my_list
    i = 0
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
    my_list.clear()
    my_list.extend(new_list)
    return my_list
