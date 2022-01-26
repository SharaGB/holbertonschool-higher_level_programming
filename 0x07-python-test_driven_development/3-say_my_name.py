#!/usr/bin/python3
"""
This is the ``say_my_name`` module.

This supplies one function, say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is first_name last_name:
        >>> say_my_name("Jon", "Snow")
        My name is Jon Snow"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
