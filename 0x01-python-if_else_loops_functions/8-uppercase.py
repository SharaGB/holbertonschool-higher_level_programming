#!/usr/bin/python3
def uppercase(str):
    aux = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            aux += chr(ord(c) - 32)
        else:
            aux += chr(ord(c))
    print("{}".format(aux))
    return aux
