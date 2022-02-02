#!/usr/bin/python3
"""
This is the ``100-append_after`` module.
"""


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file, after each line
            containing a specific string"""
    with open(filename, mode='r') as file:
        lines = file.readlines()
    idx = 0
    lines.insert(idx, new_string)
    with open(filename, mode='w') as file:
        file.writelines(lines)
