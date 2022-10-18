#!/usr/bin/python3
"""
    2-matrix_divided module
    This function divides all elements of a matrix
    return [ [matrix[0][0]/div ... ] [matrix[1][0]/div ...] ...]
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    Args:
        matrix (list): Matrix containing elements to be divided
        div (int or float): Number to divide matrix elements

    Returns:
        return [ [matrix[0][0]/div ... ] [matrix[1][0]/div ...] ...]
    """
    err_1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_2 = "Each row of the matrix must have the same size"
    err_3 = "div must be a number"
    err_4 = "division by zero"

    if (type(matrix) != list or any(type(a) != list for a in matrix)
            or len(matrix) == 0 or any(len(a) == 0 for a in matrix)):
        raise TypeError(err_1)

    for i in matrix:
        for c in i:
            if type(c) != int and type(c) != float:
                raise TypeError(err_1)

    if any((len(matrix[0]) != len(p)) for p in matrix):
        raise TypeError(err_2)

    if not (type(div) is int or type(div) is float):
        raise TypeError(err_3)

    if div == 0:
        raise ZeroDivisionError(err_4)

    return [[round(i / div, 2) for i in c] for c in matrix]
