#!/usr/bin/python3
"""
This is the ``print_square`` module.

The matrix_divided module supplies one function, print_square(size)
"""


def print_square(size):
    """
    Function that prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        print("#" * size)
