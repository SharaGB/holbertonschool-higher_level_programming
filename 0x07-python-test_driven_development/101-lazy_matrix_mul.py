#!/usr/bin/python3
"""
This is the ``lazy_matrix_mul`` module.

The lazy_matrix_mul module supplies one function, add_integer(a, b=98)
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices by using the module NumPy
    """
    return np.dot(m_a, m_b)
