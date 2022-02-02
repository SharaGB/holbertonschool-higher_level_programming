#!/usr/bin/python3
"""
This is the ``8-class_to_json`` module.
"""


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure. """
    return obj.__dict__  # vars(obj)
