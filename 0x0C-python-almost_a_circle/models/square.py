#!/usr/bin/python3
"""
This is the ``square`` module.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square inherits from Rectangle. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor. """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ To getter the instance attribute size. """
        return self.width

    @size.setter
    def size(self, value):
        """ To set the value of size. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value
        if value <= 0:
            raise ValueError("width must be > 0")

    def __str__(self):
        """ Return string representation. """
        str = "[Square] ({}) {}/{} - {}"
        return str.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Assigns attributes. """
        value = len(args)
        attributes = ('id', 'size', 'x', 'y')
        if value > 0:
            for n in range(value):
                # Asignar al atributo del objeto su valor
                setattr(self, attributes[n], args[n])
            return value
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square. """
        dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dict
