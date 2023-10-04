#!/usr/bin/python3
i = 90
while i > 65:
    if i % 2 == 0:
        k = 32
    print("{}" .format(chr(i + k)), end="")
    i -= i
    k = 0
