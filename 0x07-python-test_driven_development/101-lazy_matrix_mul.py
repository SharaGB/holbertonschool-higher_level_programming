#!/usr/bin/python3
"""
This is the ``lazy_matrix_mul`` module.

The lazy_matrix_mul module supplies one function, add_integer(a, b=98)
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices by using the module NumPy
    """
    return numpy.dot(m_a, m_b)
