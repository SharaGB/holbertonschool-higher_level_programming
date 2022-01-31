#!/usr/bin/python3
"""
This is the ``is_same_class`` module.

The is_same_class module supplies one function, is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of
        the specified class; otherwise False.
    """
    return (True if type(obj) is a_class else False)
