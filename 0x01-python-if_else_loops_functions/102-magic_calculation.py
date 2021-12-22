#!/usr/bin/python3
import dis
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif b < c:
        return a + b
    return a * b - c
