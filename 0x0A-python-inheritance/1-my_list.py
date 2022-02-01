#!/usr/bin/python3
"""
This is the ``my_list`` module.

The my_list module supplies one function, print_sorted(self)
"""


class MyList(list):
    """ Class MyList that inherits from list. """

    def __init__(self):
        """ Initializes the data. """
        self.__init__ = list()

    def print_sorted(self):
        """ Prints the sorted list. """
        print(sorted(self))
