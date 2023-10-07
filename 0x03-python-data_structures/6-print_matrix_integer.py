#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i, j = 0, 0
    for i in matrix:
        for j in i:
            print("{}" .format(j), end="")
        print("")
