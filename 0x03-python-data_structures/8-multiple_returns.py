#!/usr/bin/python3
def multiple_returns(sentence):
    i = len(sentence)
    return (i, None if i == 0 else sentence[0])
