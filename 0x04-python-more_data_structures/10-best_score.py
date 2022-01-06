#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    biggest = max(a_dictionary.items(), key = lambda x: x[1]) [0]
    return biggest
