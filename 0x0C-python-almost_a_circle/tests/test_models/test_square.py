#!/usr/bin/python3
"""
Unittest for Square([..])
"""
import unittest
import pep8
import os
import io
from contextlib import redirect_stdout
from models.square import Square
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Write unittests for the class Square
    """

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8(self):
        """ Checking a single file. """
        fchecker = pep8.Checker('models/base.py', show_source=True)
        file_errors = fchecker.check_all()
        print("Found %s errors (and warnings)" % file_errors)

    def test_square(self):
        # ID
        Base._Base__nb_objects = 0
        self.assertEqual(Square(3).id, 1)
        self.assertEqual(Square(6, 7, 8, 9).id, 9)
        # Width
        self.assertEqual(Square(3).width, 3)
        self.assertEqual(Square(15, 14, 13, 12).width, 15)
        # Height
        self.assertEqual(Square(3).height, 3)
        self.assertEqual(Square(15, 14, 13, 12).height, 15)
        # x
        self.assertEqual(Square(3).x, 0)
        self.assertEqual(Square(15, 14, 13, 12).x, 14)
        # y
        self.assertEqual(Square(3).y, 0)
        self.assertEqual(Square(15, 14, 13, 12).y, 13)
        # Size
        self.assertEqual(Square(6).size, 6)
        self.assertEqual(Square(5, 7, 8, 9).size, 5)

    def test_raises_Square(self):
        # TypeError
        with self.assertRaises(TypeError):
            Sqr = Square()

        with self.assertRaises(TypeError):
            Sqr = Square(5, 6).area(6)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Sqr = Square("Hello", 6)

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Sqr = Square(6, "Holberton")

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Sqr = Square(6, 6, "Sarah")
        # ValueError
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Sqr = Square(-6, 6)

        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Sqr = Square(6, -6)

        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Sqr = Square(6, 6, -3)

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls.sq1 = Square(6)
        cls.sq2 = Square(2, 3)
        cls.sq3 = Square(5, 6, 7)
        cls.sq4 = Square(11, 12, 13, 14)

    def test_str(self):
        self.assertEqual(str(self.sq1), "[Square] (1) 0/0 - 6")
        self.assertEqual(str(self.sq2), "[Square] (2) 3/0 - 2")
        self.assertEqual(str(self.sq3), "[Square] (3) 6/7 - 5")
        self.assertEqual(str(self.sq4), "[Square] (14) 12/13 - 11")

    def test_to_dictionary(self):
        dict1 = self.sq1.to_dictionary()
        self.assertEqual({'id': 1, 'size': 6, 'x': 0, 'y': 0}, dict1)
        dict2 = self.sq2.to_dictionary()
        self.assertEqual({'id': 2, 'size': 2, 'x': 3, 'y': 0}, dict2)
        dict3 = self.sq3.to_dictionary()
        self.assertEqual({'id': 3, 'size': 5, 'x': 6, 'y': 7}, dict3)
        dict4 = self.sq4.to_dictionary()
        self.assertEqual({'id': 14, 'size': 11, 'x': 12, 'y': 13}, dict4)

    def test_update(self):
        sq = Square(6, 0, 0, 6)
        self.assertEqual(str(Square(6, 6, 0, 0)),
                         "[Square] (0) 6/0 - 6")
        sq.update()
        self.assertEqual(str(sq), "[Square] (6) 0/0 - 6")
        sq.update(89)
        self.assertEqual(str(sq), "[Square] (89) 0/0 - 6")
        sq.update(89, 1)
        self.assertEqual(str(sq), "[Square] (89) 0/0 - 1")
        sq.update(89, 1, 2)
        self.assertEqual(str(sq), "[Square] (89) 2/0 - 1")
        sq.update(89, 1, 2, 3)
        self.assertEqual(str(sq), "[Square] (89) 2/3 - 1")

    def test_create(self):
        sq1 = Square.create(**{'id': 89})
        sq2 = Square.create(**{'id': 89, 'size': 1})
        sq3 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        sq4 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual("[Square] (89) 0/0 - 6", str(sq1))
        self.assertEqual("[Square] (89) 0/0 - 1", str(sq2))
        self.assertEqual("[Square] (89) 2/0 - 1", str(sq3))
        self.assertEqual("[Square] (89) 2/3 - 1", str(sq4))

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open('Square.json', mode='r') as file:
            self.assertEqual("[]", file.read())

    def test_load_from_file(self):
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertEqual(Square.load_from_file(), [])

        try:
            os.remove("Square.json")
        except:
            pass
        open("Square.json", 'a').close()
        self.assertEqual(Square.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()
