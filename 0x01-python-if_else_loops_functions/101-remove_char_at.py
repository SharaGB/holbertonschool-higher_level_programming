#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for x in range(len(str)):
        if x == n:
            continue
        new += str[x]
    return new
