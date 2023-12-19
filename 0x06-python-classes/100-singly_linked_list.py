#!/usr/bin/python3

"""A Python implementation of Singly Linked Lists"""


class Node:
    """Blueprint for the node"""

    def __init__(self, data: int, next_node=None):
        """
        Creates a new node

        Args:
            data (int): the data integer value to store
            next_node (Node, optional): reference to the next node.
            Defaults to None.

        Raises:
            TypeError: when the data given is an integer or when an invalid
            object is received as the next_node

        Returns:
            Node: an instance of the Node class
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self) -> int:
        """
        Retrieves the data part of a node

        Returns:
            int: the value stored in the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets or updates the data part of a node"""
        self.__init__(value, self.__next_node)

    @property
    def next_node(self):
        """
        Retrieves the reference to the next node

        Returns:
            Node: reference to the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets or updates the reference to the next node"""
        self.__init__(self.__data, value)


class SinglyLinkedList:
    """A Singly Linked List Implementation"""

    def __init__(self):
        """Initializes the Linked list"""
        self.head = None

    def __str__(self) -> str:
        """
        Returns all data part of Node type in a linked list

        Returns:
            str: the data part of all nodes in a linked list
        """
        nodes = []
        cur = self.head

        while cur is not None:
            nodes.append(str(cur.data))
            cur = cur.next_node

        return "\n".join(nodes)

    def sorted_insert(self, value: int) -> None:
        """
        Insert a node into a linked list while keeping it sorted in
        ascending order

        Args:
            value (int): the integer value to insert
        """
        element = Node(value, None)

        # handle cases where the list is empty or the
        # value needs to be inserted at the beginning of the list
        if not self.head or self.head.data > value:
            element.next_node = self.head
            self.head = element
        else:
            # perform sorted insertion
            cur = self.head
            while cur.next_node and cur.next_node.data < value:
                cur = cur.next_node

            # adjust links to insert node
            element.next_node = cur.next_node
            cur.next_node = element
