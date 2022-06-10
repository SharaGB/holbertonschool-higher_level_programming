#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if(i > a):
                raise Exception
            else:
                result += (a ** b) / i
        except Exception as e:
            result = b + a
    return result
