#!/usr/bin/python3
"""
This is the ``9-student`` module.
"""


class Student:
    """ Class Student that defines a student by:
        - Public instance attributes:
            first_name
            last_name
            age.
        - Public method def to_json(self) """

    def __init__(self, first_name, last_name, age):
        """  Initializes the data. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student. """
        return self.__dict__
