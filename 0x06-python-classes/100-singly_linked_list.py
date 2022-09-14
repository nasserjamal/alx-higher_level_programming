#!/usr/bin/python3
"""Defination of classes to implement linked list data structure"""


class Node:
    """A node class of a linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if(type(value) != int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) == Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """As the name says, singlyLinkedList :)"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
            return
        current = self.__head
        if value <= current.data:
            self.__head = Node(value, current)
            return
        while current.next_node is not None:
            if value <= current.next_node.data:
                newNode = Node(value, current.next_node)
                current.next_node = newNode
                return
            current = current.next_node
        current.next_node = Node(value)

    def __str__(self):
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
