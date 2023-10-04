#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    i = 0
    while i < len(str):
        if i == n:
            continue
        else:
            new_str[i] = str[i]
        i += 1
