#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if 64 < ord(ch) < 91:
            continue
        elif 96 < ord(ch) < 123:
            ch = ord(ch) - 32
            print("{}" .format(ch))
