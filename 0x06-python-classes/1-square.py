#!/usr/bin/python3

"""
Defines a blueprint for a Square as part of the OOP tasks
"""


class Square:
    """
    A blueprint for working with squares
    """

    def __init__(self, size):
        """
        Initializes the Square class

        Args:
            size (Any): the size of the square
        """
        self.__size = size
