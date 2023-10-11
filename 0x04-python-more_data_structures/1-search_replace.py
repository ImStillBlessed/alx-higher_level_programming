#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search in my_list:
        my_list[my_list.index(search)] = replace
    return my_list
