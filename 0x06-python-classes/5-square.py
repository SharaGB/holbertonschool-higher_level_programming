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
        """To retrieve it"""
        return self.__size

    @size.setter
    def size(self, size):
        """To set it"""
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public instance method"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints in
            stdout the square with the character #"""
        if self.__size == 0:
            print()
        for x in range(self.__size):
            print(' '.join("#".format() for i in range(self.__size)))
