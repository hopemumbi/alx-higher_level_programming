#!/usr/bin/python3
"""This module creates a node of a singly linked list
    called Node.
    It then stores the node data and adress of the next node
"""


class Node:
    """ defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize an instance of Node

        Args:
            data: Data stored in the node
             next_node: Address of the next node
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Retrieve the data"""
            return self.__data

        @data.setter
        def data(self, value):
            """Set the value of the data"""
            # Raise TypeError if data is not an integer
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """Retrieve the address of the next node"""
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            """Set the value of the next node"""
            # Raise TypeError if next node isn't either `None` or `Node`
            if not isinstance(value, Node) or value is not None:
                raise TypeError("next_node must be a Node object")
            self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """Initialize the head of the linked list to None"""
        self.head = None

    def sorted_insert(self, value):
        # Create a new node with the given value
        new_node = Node(value)
        # Check if the linked list is empty or
        # the new value is smaller than the head's value
        if self.head is None or value < self.head.data:
            # then insert the new node at the beginning of the linked list
            new_node.next_node = self.head
            self.head = new_node
            return
        # Traverse the linked list, find correct position, insert the new node
        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        # Insert the new node in the correct position
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """print the entire list in stdout
        one node number by line
        """
        result = ""
        current = self.head
        # Traverse the linked list
        while current is not None:
            # append each node's data to the result string
            result += str(current.data)
            # No new line at the end
            if current.next_node is not None:
                result += "\n"
            current = current.next_node
        return result
