#!/usr/bin/python3
"""
This module divides all elements of a matrix
Author:
    Oigbochie Blessed
"""
import math

def matrix_divided(matrix, div):
    """
    this function divides the integers in the matrix

    Args:
        matrix (list of lists) (int): matrix to be divided
        div (int): the divider for the elements in the matrix
    Returns:
        a new matrix
    Raises:
        TypeError: if any value in the function is not an integer
            if each row are not the same lenght
            if the divider is not an interger
        ZeroDivisionError: if the divider is 0 or less than 0.
    """
    type_error_1 = "matrix must be a matrix (list of lists) of integers/floats"
    type_error_2 = "Each row of the matrix must have the same size"
    type_error_3 = "div must be a number"
    zero_div_error = "division by zero"
    cap = 0
    for i in matrix[0]:
        cap += 1

    if not isinstance(div, (int, float)):
        raise TypeError(type_error_3)
    if div <= 0:
        raise ZeroDivisionError(zero_div_error)
    for row in matrix:
        count = 0
        for i in row:
            if count > cap:
                raise TypeError(type_error_2)
            else:
                count += 1
            if not isinstance(i, (int, float)):
                raise TypeError(type_error_1)
    return [[round(x / div, 2) for x in row] for row in matrix]
