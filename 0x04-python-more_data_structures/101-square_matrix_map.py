#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if not matrix:
        return None
    new_mat = [for y in matrix list(map(lambda x: x**2, for x in y))]
    return new_mat
