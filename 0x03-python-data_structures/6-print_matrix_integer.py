#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i, j = 0, 0
    for i in range(0, len(matrix)):
        for j in range(0, len(i)):
            print("{}" .format(i[j]), end="")
            if j != (len(i) - 1):
                print(" ", end="")
        print("")
