#!/usr/bin/python3
"""
This is the ``100-my_int`` module.
"""


class MyInt(int):
    """ Class MyInt that inherits from int. """

    def __eq__(self, x) -> bool:
        return False

    def __ne__(self, x) -> bool:
        return True
