#!/usr/bin/python3
"""Singly Linked Lists module.

This module contains methods for creating and handling SinglyLinkedList
and Node objects.

"""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a Node object with the given data and next_node.

        Args:
            data (int): The value of the node.
            next_node (Node, optional): The next Node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data value of a node."""
        return self.__data
    @data.setter
    def data(self, value):
        """Sets the data value of a node.

        Args:
            value (int): The value to set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Get or set the next node of the current node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node of the current node.

        Args:
            value (Node or None): The next Node object or None.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes an empty SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.

        The list is sorted in increasing order.

        Args:
            value (int): The value to insert.
        """
        temp = self.__head
        if not self.__head or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            temp.next_node = Node(value, temp.next_node)

    def __str__(self):
        """Returns a string representation of the SinglyLinkedList."""
        nodes = []
        temp = self.__head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next_node
        return '\n'.join(nodes)
