#!/usr/bin/python3
"""
This is the ``10-student`` module.
"""


class Student:
    """ Class Student that defines a student by:
        - Public instance attributes:
            first_name
            last_name
            age.
        - Public method def to_json(self, attrs=None) """

    def __init__(self, first_name, last_name, age):
        """ """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student. """
        attribute_names = {}
        if isinstance(attrs, list):
            for x in attrs:
                if x in self.__dict__:
                    attribute_names[x] = self.__dict__[x]
            return attribute_names
        return self.__dict__
