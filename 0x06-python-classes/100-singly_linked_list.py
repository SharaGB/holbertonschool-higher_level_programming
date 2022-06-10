#!/usr/bin/python3
""" Empty class Square definition """


class Node:
    """Class Node that defines a node of a singly linked list by:
        - Private instance attribute: data
        - Private instance attribute: next_node"""

    def __init__(self, data, next_node=None):
        """Initializes the data"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """To retrieve it"""
        return self.__data

    @data.setter
    def data(self, value):
        """To set it"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """To retrieve it"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """To set it"""
        if isinstance(value, Node) or value is None:
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
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in
            the list (increasing order)"""
        new_node = Node(value)
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node and ((tmp.next_node).data < value)):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Print singly linked list"""
        tmp = self.__head
        result = ""
        while (tmp):
            result = result + str(tmp.data)
            tmp = tmp.next_node
            if (tmp):
                result = result + "\n"
        return (result)
