#!/usr/bin/python3
"""
This is the ``square`` module.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle (9-rectangle.py).
                (task based on 10-square.py).
    """
    def __init__(self, size):
        """ Initializes the data. """
        self.__size = size
        self.integer_validator('size', size)

    def area(self):
        """ Returns the area of the square. """
        return self.__size ** 2

    def __str__(self):
        """ Return str square. """
        return "[Square] {}/{}".format(self.__size, self.__size)
