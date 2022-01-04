#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        n_max = sorted(my_list)
        return n_max[-1]
    else:
        return None
