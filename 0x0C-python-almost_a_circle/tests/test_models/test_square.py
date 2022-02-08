#!/usr/bin/python3
"""
Unittest for Square([..])
"""
from re import S
import unittest
import pep8
from models.square import Square


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
        self.assertEqual(Square(3).id, 23)
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

    def test_raises_rectangle(self):
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
