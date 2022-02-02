#!/usr/bin/python3
"""
This is the ``3-from_json_string`` module.
"""
import json


def from_json_string(my_str):
    """ Returns an object represented by a JSON string. """
    return json.loads(my_str)
    # Se utiliza para analizar una cadena JSON y convertirla
    # en un diccionario de Python
