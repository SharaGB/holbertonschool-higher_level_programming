#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for elm in range(len(my_list)):
        if my_list[elm] == search:
            my_list[elm] = replace
    return new_list
