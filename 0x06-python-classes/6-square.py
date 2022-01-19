#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """A class Square that defines a square by:
        - Private instance attribute: size
        - Private instance attribute: position
        - Public instance method: def area(self).
        - Public instance method: def my_print(self)"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data"""
        self.size = size
        self.position = position

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
        if type(value) is not tuple or len(value) != 2\
           or type(value[0]) is not int or type(value[1]) is not int\
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Public instance method:
            Return: The current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints in
            stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for space in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
