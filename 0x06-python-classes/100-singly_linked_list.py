#!/usr/bin/python3

""" Node of Singly linked list"""
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        temp = self.__head
        if not self.__head or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            temp.next_node = Node(value, temp.next_node)

    def __str__(self):
        nodes = []
        temp = self.__head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next_node
        return '\n'.join(nodes)
