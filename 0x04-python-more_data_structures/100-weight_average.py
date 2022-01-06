#!/usr/bin/python3
def weight_average(my_list=[]):
    normalization = 0
    val = 0
    if len(my_list) == 0:
        return 0
    for value, weight in my_list:
        val += value * weight
        normalization += weight
    return val / normalization
