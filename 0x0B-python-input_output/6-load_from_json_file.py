#!/usr/bin/python3
"""
This is the ``3-from_json_string`` module.
"""
import json


def load_from_json_file(filename):
    """ Creates an Object from a “JSON file”. """
    with open(filename, mode='r') as a_file:
        return json.load(a_file)
