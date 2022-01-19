#!/usr/bin/python3
"""Empty class Square definition"""


class Square:
    """A class Square that defines a square by:
        - Private instance attribute: size
        - Private instance attribute: position
        - Public instance method: def area(self).
        - Public instance method: def my_print(self)"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """To retrieve it"""
        return self.__size

    @size.setter
    def size(self, size):
        """To set it:
            - size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer.
            - If size is less than 0, raise a ValueError exception with the
            message size must be >= 0"""
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """To retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        """To set it:
            - position must be a tuple of 2 positive integers, otherwise
            raise a TypeError exception with the message position must be
            a tuple of 2 positive integers"""
        if type(value) is tuple or len(value) < 2\
            or type(value[0]) is int or type(value[1]) is int\
                or value[0] > 0 or value[1] > 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Public instance method:
            Return: The current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints in
            stdout the square with the character #"""
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            for space in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()
