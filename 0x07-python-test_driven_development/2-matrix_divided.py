#!/usr/bin/python3
"""
This module divides all elements of a matrix
Author:
    Oigbochie Blessed
"""


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
    """
    if not isinstance(matrix, list):
        for value in matrix[int
