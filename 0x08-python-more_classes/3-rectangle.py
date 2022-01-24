#!/usr/bin/python3
"""
Module to write a class Rectangle
"""


class Rectangle:
    """Write a class Rectangle that defines a rectangle by:
    - Private instance attribute: width
    - Private instance attribute: height
    - Public instance method: def area(self)
    - Public instance method: def perimeter(self)
    - print() and str() should print the rectangle with the character #"""

    def __init__(self, width=0, height=0):
        """Initializes the data"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """To getter the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.__width = value
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """To getter the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """To set the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.__height = value
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Print the rectangle with the character #"""
        str = ""
        if self.__width != 0 or self.__height != 0:
            for h in range(self.__height):
                for w in range(self.__width):
                    str += "#"
                if h < self.__height - 1:
                    str += "\n"
        return str
