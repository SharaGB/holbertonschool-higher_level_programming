#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_mtrx = [list(map(lambda x: x ** 2, lists)) for lists in matrix]
    return new_mtrx
