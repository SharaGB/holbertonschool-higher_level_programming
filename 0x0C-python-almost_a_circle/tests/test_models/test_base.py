#!/usr/bin/python3
"""
Unittest for base([..])
"""
import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Write unittests for the class Base
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

    def test_class_base(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(6).id, 6)
        self.assertEqual(Base(-6).id, -6)
        self.assertEqual(Base(None).id, 2)
        self.assertEqual((5, 6), Base((5, 6)).id)
        self.assertEqual(Base("Holberton").id, "Holberton")

    def test_base_raises(self):
        with self.assertRaises(TypeError):
            class_base = Base(6, 6)
            self.assertEqual(Base().id, 6)
            self.assertEqual(Base(101).id, 101)

        with self.assertRaises(AttributeError):
            print(Base(6).__nb_objects)

    def test_base_json_string(self):
        json = [Base(3).__dict__]
        self.assertEqual(Base.to_json_string(json), '[{"id": 3}]')

        dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        dict_ = {'x': 2, 'y': 10, 'id': 2, 'height': 3, 'width': 11}
        base = Base.to_json_string([dict, dict_])
        self.assertTrue(type(base) is str)
        # If is None or empty
        self.assertEqual(Base.from_json_string([]), [])
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.from_json_string('[]'), [])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Base.to_json_string([{'id': 6}]), '[{"id": 6}]')

if __name__ == "__main__":
    unittest.main()
