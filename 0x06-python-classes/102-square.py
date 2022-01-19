#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """"A class Square that defines a square by:
        - Private instance attribute: size
        - Public instance method: def area(self)"""

    def __init__(self, size=0):
        """Initializes the data"""
        self.__size = size

    @property
    def size(self):
        """To retrieve it"""
        return self.__size

    @size.setter
    def size(self, size):
        """To set it:
            - size must be a number (float or integer),
            otherwise raise a TypeError exception with
            the message size must be a number
            - If size is less than 0, raise a ValueError
            exception with the message size must be >= 0"""
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public instance method:
            Return: The current square area"""
        return self.__size ** 2

    def __eq__(self, area2):
        """Compare Square instance: =="""
        return self.size == area2.size

    def __ne__(self, area2):
        """Compare Square instance: !="""
        return self.size != area2.size

    def __gt__(self, area2):
        """Compare Square instance: >"""
        return self.size > area2.size

    def __ge__(self, area2):
        """Compare Square instance: >="""
        return self.size >= area2.size

    def __lt__(self, area2):
        """Compare Square instance: <"""
        return self.size < area2.size

    def __le__(self, area2):
        """Compare Square instance: <="""
        return self.size <= area2.size
