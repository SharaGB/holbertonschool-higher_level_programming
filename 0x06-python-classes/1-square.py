#!/usr/bin/python3
"""Empty class Square definition"""


class Square:
    """A class Square that defines a square by:
        - Private instance attribute: size
        - Instantiation with size (no type/value verification)"""
    def __init__(self, size):
        """Initializes the data"""
        self.__size = size
