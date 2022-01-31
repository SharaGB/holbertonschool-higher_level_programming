#!/usr/bin/python3
"""
This is the ``rectangle`` module.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle that inherits from BaseGeometry
        (7-base_geometry.py). (task based on 8-rectangle.py)
    """
    def __init__(self, width, height):
        """ Initializes the data. """
        self.__width = width
        self.__height = height
        self.integer_validator('width', self.__width)
        self.integer_validator('height', self.__height)

    def area(self):
        """ Rreturns the area of the rectangle. """
        return self.__width * self.__height

    def __str__(self):
        """ Return str rentangle. """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
