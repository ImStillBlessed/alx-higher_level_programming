#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if 96 < ord(ch) < 123:
            ch = ord(ch) - 32
            print("{}" .format(chr(ch)), end="")
        else:
            print("{}" .format(chr(ch)), end="")
    print("\n")
# change the letters to upper first then, print the string 
