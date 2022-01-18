#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    result = 0
    for i in range(a, b):
        try:
            if a < i:
                raise Exception
            else:
                result += (a ** b) / i
        except:
            result = b + a
            pass
    return result
