#!/usr/bin/python3
def weight_average(my_list=[]):
    normalization = 0
    val = 0
    for value, weight in my_list:
        val += value * weight
        normalization += weight
    return val / normalization
