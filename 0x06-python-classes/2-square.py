#!/usr/bin/python3
"""Empty class Square definition"""


class Square:
    """A class Square that defines a square by:
        - Private instance attribute: size
        - Instantiation with optional size: def __init__(self, size=0)"""

    def __init__(self, size=0):
        """Initializes the data:
            - size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer
            - If size is less than 0, raise a ValueError exception with the
            message size must be >= 0"""
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
