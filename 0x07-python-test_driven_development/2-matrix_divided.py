#!/usr/bin/python3
"""
This is the ``matrix_divided`` module.

The matrix_divided module supplies one function, matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]"""
    new_mtrx = []
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    # iterate through rows of matrix
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        # iterate through elements of rows
        for elements in rows:
            if type(elements) is not int and type(elements) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) " +
                    "of integers/floats")
        if len(rows) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mtrx = [[round(columns / div, 2) for columns in rows]
                for rows in matrix]
    return new_mtrx
