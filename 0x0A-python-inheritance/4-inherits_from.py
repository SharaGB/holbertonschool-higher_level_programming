#!/usr/bin/python3
"""
This is the ``inherits_from`` module.

This module supplies one function, inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    return (False if type(obj) is a_class else issubclass(type(obj), a_class))
