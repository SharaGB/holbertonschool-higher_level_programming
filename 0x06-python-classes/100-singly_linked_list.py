#!/usr/bin/python3
"""Empty class Square definition"""


from lib2to3.pytree import Node


class Nose:
    """lass Node that defines a node of a singly linked list by:
        - Private instance attribute: data
        - Private instance attribute: next_node"""

    def __init__(self, data, next_node=None):
        """Initializes the data"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """To retrieve it"""
        return self.__data

    @data.setter
    def data(self, value):
        """To set it"""
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """To retrieve it"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """To set it"""
        if value is None and type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """A class SinglyLinkedList that defines a singly linked list by:
        - Private instance attribute: head (no setter or getter)
        - Public instance method: def sorted_insert(self, value)"""

    def __init__(self):
        """Should be printable:
            - Print the entire list in stdout
            - One node number by line"""
        self.__headval = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in
            the list (increasing order)"""
        print_list = self.__headval
        new_node = Node(value)
        if self.__headval is None:
            self.__headval = new_node
            return
        while print_list is not None:
            print(print_list.data)
            print_list = print_list.nex_node
            # Incompleto
