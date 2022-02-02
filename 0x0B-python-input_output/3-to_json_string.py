#!/usr/bin/python3
"""
This is the ``3-to_json_string`` module.
"""
import json


def to_json_string(my_obj):
    """ Returns the JSON representation of an object (string). """
    return json.dumps(my_obj)
    # La función json.dumps() convierte un objeto Python en una cadena json.
