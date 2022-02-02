#!/usr/bin/python3
"""
This is the ``5-save_to_json`` module.
"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file, using a JSON representation. """
    with open(filename, mode='w') as a_file:
        json.dump(my_obj, a_file)
    # dump() convierte los objetos Python en objetos json
