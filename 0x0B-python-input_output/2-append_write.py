#!/usr/bin/python3
"""
This is the ``2-append_write`` module.
"""


def append_write(filename="", text=""):
    """ Returns the number of characters added. """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
