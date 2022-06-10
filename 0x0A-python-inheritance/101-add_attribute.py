#!/usr/bin/python3
" Add attribute "


def add_attribute(object, key, value):
    """ Adds a new attribute to an object if it’s possible """

    if hasattr(object, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(object, key, value)
