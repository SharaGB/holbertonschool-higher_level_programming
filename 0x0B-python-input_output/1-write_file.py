#!/usr/bin/python3
"""
This is the ``1-write_file`` module.
"""


def write_file(filename="", text=""):
    """ Returns the number of characters written. """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
