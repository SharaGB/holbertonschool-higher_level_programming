#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Write unittests for the function def max_integer(list=[])
    """

    def test_max_int(self):
        self.assertEqual(max_integer([6, 6, 6]), 6)
        self.assertAlmostEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([9, 6, 3]), 9)
        self.assertAlmostEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([27, 36, 45, 54]), 54)

    def test_max_negative(self):
        self.assertEqual(max_integer([101, 666, -8]), 666)
        self.assertEqual(max_integer([-100, -35, -14, -6]), -6)
        self.assertEqual(max_integer([21, 20, 2022, 7, -13]), 2022)
        self.assertEqual(max_integer([-3.33, -3.5, -16.0, -7.1, -10.1]), -3.33)


    def test_max_float(self):
        self.assertEqual(max_integer([2.25, 16, 66.6]), 66.6)
        self.assertEqual(max_integer([1024, 9876543, 12345, 2001, 9]), 9876543)

    def test_max_none(self):
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer([]), 2)
        self.assertIsNone(max_integer([None]))
        self.assertEqual(max_integer([]), None)

    def test_max_error(self):
        with self.assertRaises(TypeError):
            max_integer(6)
            max_integer(None)
            max_integer(6, 7, 8, 9)

    def test_max_str(self):
        with self.assertRaises(TypeError):
            max_integer(["World!", 5])
            max_integer([1, 2, 3, 4, 5], ":3")
            max_integer(["Orión", 16, 9], "Orión")

    def test_max_bool(self):
        with self.assertRaises(TypeError):
            max_integer([98, 61, 200], True)
            max_integer(False)


if __name__ == '__main__':
    unittest.main()
