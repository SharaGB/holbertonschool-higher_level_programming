#!/usr/bin/python3
"""
Unittest for rectangle([..])
"""
import unittest
import pep8
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Write unittests for the class Rectangle
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

    def test_class_rectangle(self):
        self.assertEqual(6, 6)
        self.assertAlmostEqual(Rectangle(4, 5).width, 4)
        self.assertAlmostEqual(Rectangle(5, 6).height, 6)
        self.assertAlmostEqual(Rectangle(5, 6).area(), 30)
        self.assertAlmostEqual(Rectangle(5, 6, 7).area(), 30)
        self.assertAlmostEqual(Rectangle(8, 9, 10, 11).area(), 72)

    def test_raises_rectangle(self):
        # TypeError
        with self.assertRaises(TypeError):
            rec = Rectangle()

        with self.assertRaises(TypeError):
            rec = Rectangle(5, 6).area(6)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            rec = Rectangle("Hello", 6)

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            rec = Rectangle(6, "World!")

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rec = Rectangle(6, 6, "Holberton")

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            rec = Rectangle(6, 6, 6,  "Sarah")
        # ValueError
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            rec = Rectangle(-6, 6)

        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            rec = Rectangle(6, -6)

        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            rec = Rectangle(6, 6, -6)

        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            rec = Rectangle(6, 6, 6, -3)
