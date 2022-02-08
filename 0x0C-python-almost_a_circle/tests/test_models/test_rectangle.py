#!/usr/bin/python3
"""
Unittest for rectangle([..])
"""
import unittest
import pep8
import os
import io
from contextlib import redirect_stdout
from models.base import Base
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
        Base._Base__nb_objects = 0
        self.assertEqual(6, 6)
        self.assertIsInstance(Rectangle(6, 3), Base)
        self.assertAlmostEqual(Rectangle(4, 5).width, 4)
        self.assertAlmostEqual(Rectangle(5, 6).height, 6)
        self.assertAlmostEqual(Rectangle(5, 6).area(), 30)
        self.assertAlmostEqual(Rectangle(5, 6, 7).area(), 30)
        self.assertAlmostEqual(Rectangle(8, 9, 10, 11).area(), 72)

    def test_id(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Rectangle(1, 6).id, 1)
        self.assertEqual(Rectangle(1, 2, 3).id, 2)
        self.assertEqual(Rectangle(4, 5, 6, 7).id, 3)
        self.assertEqual(Rectangle(8, 9, 10, 11, 12).id, 12)

    def test_raises_rectangle(self):
        # TypeError
        with self.assertRaises(TypeError):
            rec = Rectangle()

        with self.assertRaises(TypeError):
            rec = Rectangle(6)

        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, 3, 4, 5, 6)

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

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            rec = Rectangle(0, 2)

        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            rec = Rectangle(6, -6)

        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            rec = Rectangle(6, 0)

        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            rec = Rectangle(6, 6, -6)

        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            rec = Rectangle(6, 6, 6, -3)

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(6, 6)
        cls.r2 = Rectangle(2, 3, 4)
        cls.r3 = Rectangle(5, 6, 7, 8, 9)
        cls.r4 = Rectangle(1, 2, 3, 4)

    def test_str(self):
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 6/6")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")
        self.assertEqual(str(self.r3), "[Rectangle] (9) 7/8 - 5/6")
        self.assertEqual(str(self.r4), "[Rectangle] (3) 3/4 - 1/2")

    def test_display(self):
        r = Rectangle(2, 3, 0, 0, 1)
        with io.StringIO() as display, redirect_stdout(display):
            Rectangle(1, 2, 3, 4, 5).display()

        with io.StringIO() as display, redirect_stdout(display):
            Rectangle(3, 4, 5, 6).display()

        with io.StringIO() as display, redirect_stdout(display):
            Rectangle(11, 12, 13).display()

        with io.StringIO() as display, redirect_stdout(display):
            Rectangle(3, 4).display()

        with self.assertRaises(TypeError):
            Rectangle(3, 4).display(1)

        with io.StringIO() as display, redirect_stdout(display):
            self.r1.display()
            output = display.getvalue()
            self.assertEqual(output, ("#" * 10 + "\n") * 10)

        with io.StringIO() as display, redirect_stdout(display):
            r.display()
            output = display.getvalue()
            self.assertEqual(output, ("#" * 2 + "\n") * 3)

    def test_to_dictionary(self):
        dict1 = self.r1.to_dictionary()
        self.assertEqual({'id': 1, 'width': 6, 'height': 6,
                          'x': 0, 'y': 0}, dict1)
        dict2 = self.r2.to_dictionary()
        self.assertEqual({'id': 2, 'width': 2, 'height': 3,
                          'x': 4, 'y': 0}, dict2)
        dict3 = self.r3.to_dictionary()
        self.assertEqual({'id': 9, 'width': 5, 'height': 6,
                          'x': 7, 'y': 8}, dict3)
        dict4 = self.r4.to_dictionary()
        self.assertEqual({'id': 3, 'width': 1, 'height': 2,
                          'x': 3, 'y': 4}, dict4)

    def test_update(self):
        rec = Rectangle(6, 6, 0, 0, 3)
        self.assertEqual(str(Rectangle(6, 6, 0, 0, 3)),
                         "[Rectangle] (3) 0/0 - 6/6")
        rec.update()
        self.assertEqual(str(rec), "[Rectangle] (3) 0/0 - 6/6")
        rec.update(89)
        self.assertEqual(str(rec), "[Rectangle] (89) 0/0 - 6/6")
        rec.update(89, 1)
        self.assertEqual(str(rec), "[Rectangle] (89) 0/0 - 1/6")
        rec.update(89, 1, 2)
        self.assertEqual(str(rec), "[Rectangle] (89) 0/0 - 1/2")
        rec.update(89, 1, 2, 3)
        self.assertEqual(str(rec), "[Rectangle] (89) 3/0 - 1/2")
        rec.update(89, 1, 2, 3, 4)
        self.assertEqual(str(rec), "[Rectangle] (89) 3/4 - 1/2")

    def test_create(self):
        rec1 = Rectangle.create(**{'id': 89, 'width': 1})
        rec2 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        rec3 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        rec4 = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual("[Rectangle] (89) 0/0 - 1/6", str(rec1))
        self.assertEqual("[Rectangle] (89) 0/0 - 1/2", str(rec2))
        self.assertEqual("[Rectangle] (89) 3/0 - 1/2", str(rec3))
        self.assertEqual("[Rectangle] (89) 3/4 - 1/2", str(rec4))

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open('Rectangle.json', mode='r') as file:
            self.assertEqual("[]", file.read())

    def test_load_from_file(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

        try:
            os.remove("Rectangle.json")
        except:
            pass
        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()
