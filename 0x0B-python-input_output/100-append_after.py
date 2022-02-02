#!/usr/bin/python3
"""
This is the ``100-append_after`` module.
"""


from hashlib import new


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file, after each line
            containing a specific string"""
    with open(filename, mode='r') as file:
        lines = file.readlines()
    data = ""
    for line in lines:
        data += line
        if search_string in line:
            data += new_string

    with open(filename, mode='w') as file:
        file.writelines(data)
