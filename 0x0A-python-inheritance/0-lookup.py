#!/usr/bin/python3
"""
This is the ``lookup`` module.

The lookup module supplies one function, lookup(obj)
"""


def lookup(obj):
    """ Returns the list of available attributes and methods of an objec. """
    return dir(obj)
