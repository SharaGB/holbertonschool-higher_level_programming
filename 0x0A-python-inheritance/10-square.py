#!/usr/bin/python3
"""
This is the ``square`` module.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle (9-rectangle.py) """

    def __init__(self, size):
        """ Initializes the data. """
        self.__size = size
        super().__init__(size, size)  # Evita usar el nombre de la clase base
        self.integer_validator('size', self.__size)

    def are(self):
        """ Returns the area of the square. """
        return self.__size ** 2
