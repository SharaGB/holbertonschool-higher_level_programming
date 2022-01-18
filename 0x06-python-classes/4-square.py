#!/usr/bin/python3
"""Empty class Square definition"""


class Square:
    """A class Square that defines a square by:
        - Private instance attribute: size"""

    def __init__(self, size=0):
        """Initializes the data"""
        self.__size = size

    @property
    def size(self):
        """Property def size(self): to retrieve it"""
        return self.__size

    @size.setter
    def size(self, size):
        """Property setter def size(self, size): to set it"""
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public instance method"""
        return self.__size ** 2
