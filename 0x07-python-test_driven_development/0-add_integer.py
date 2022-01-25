#!/usr/bin/python3
"""
This is the ``add_integer`` module.

The add_integer module supplies one function, add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """Function that adds 2 integers:
        >>> my_function(2, 3)
        5"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
