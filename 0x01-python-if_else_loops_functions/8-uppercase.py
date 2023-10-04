#!/usr/bin/python3
def uppercase(str):
    result = ""
    for ch in str:
        if 96 < ord(ch) < 123:
            ch = chr(ord(ch) - 32)
        result += ch
    print("{}" .format(result))
