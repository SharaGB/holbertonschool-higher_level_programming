#!/usr/bin/python3
"""
This is the ``rectangle`` module.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle that inherits from BaseGeometry. """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator('width', self.__width)
        self.integer_validator('height', self.__height)
