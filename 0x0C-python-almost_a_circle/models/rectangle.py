#!/usr/bin/python3
"""
This is the ``rectangle`` module.
"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from Base.
        Private instance attributes:
        __width -> width
        __height -> height
        __x -> x
        __y -> y """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ To getter the private instance attribute width. """
        return self.__width

    @width.setter
    def width(self, value):
        """ To set the value of width. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.__width = value
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """To getter the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """To set the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.__height = value
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """To getter the private instance attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """To set the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        self.__x = value
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """To getter the private instance attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """To set the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        self.__y = value
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """ Returns the area value of the Rectangle instance. """
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character #. """
        row = ' ' * self.__x + '#' * self.__width
        for h in range(self.__y):
            print()
        for w in range(self.__height):
            print(row)

    def __str__(self):
        """ Return string representation. """
        rect = "[Rectangle] ({}) {}/{} - {}/{}"
        return rect.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute. """
        value = len(args)
        attributes = ('id', 'width', 'height', 'x', 'y')
        if value > 0:
            for n in range(value):
                # Asignar al atributo del objeto su valor
                setattr(self, attributes[n], args[n])
            return value
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle. """
        dict = {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
        return dict
