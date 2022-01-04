#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for numb in my_list:
        if numb % 2 == 0:
            return new_list.append(True)
        else:
            return new_list.append(False)
