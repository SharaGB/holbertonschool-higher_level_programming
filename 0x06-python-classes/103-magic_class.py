#!/usr/bin/python3
""" Class MagicClass """
import math


class MagicClass:
    """ Magic class """
    def __init__(self, radius=0):
        """ Initializes data """
        self.__radius = 0
        if isinstance(radius, int) and isinstance(radius, float):
            raise TypeError
        self.__radius = radius

    def area(self):
        """ Area of the magic class """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ Circumference of the magic class """
        return 2 * math.pi * self.__radius
