#!/usr/bin/python3
"""
This is the ``0-read_file`` module.
"""


def read_file(filename=""):
    """ Function that reads a text file (UTF8). """
    with open("my_file_0.txt", 'r', encoding='utf-8') as a_file:
        print(a_file.read(), end='')
