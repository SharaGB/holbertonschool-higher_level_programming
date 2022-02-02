#!/usr/bin/python3
"""
This is the ``12-pascal_triangle`` module.
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers
    representing the Pascal’s triangle of n. """
    if n <= 0:
        return []
    elif n == 1:  # Si el número de filas es 1
        # devolvemos triángulo con una sola fila.
        return [[1]]
    else:  # De lo contrario armamos el triángulo segun el número de filas
        new_n = [1]
        result = pascal_triangle(n - 1)
        last_n = result[-1]
        for i in range(len(last_n) - 1):
            new_n.append(last_n[i] + last_n[i + 1])
    new_n += [1]
    result.append(new_n)
    return result
