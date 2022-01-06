#!/usr/bin/python3
def common_elements(set_1, set_2):
    return set_1.intersection(set_2)

    # También da de este modo
    # for elm in set_1:
    #     if elm in set_2:
    #         return list(elm)
