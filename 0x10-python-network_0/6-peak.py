#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Sorts and returns the peak numberof integers in a list. """
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
