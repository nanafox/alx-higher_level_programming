#!/usr/bin/python3

"""
Defines a blueprint for a Square as part of the OOP tasks
"""


class Square:
    """
    A blueprint for working with squares
    """

    def __init__(self, size: int = 0):
        """
        Initializes the Square class

        Args:
            size (int, optional): the size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self) -> int:
        """
        Retrieves the size of the square

        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, size) -> None:
        """
        Sets or updates the size of the square

        Args:
            size (int): the size of the square

        Raises:
            TypeError: when the size received is not an integer
            ValueError: when the size if not a positive integer
        """
        # size must be an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # it should be greater than or equal to zero
        if size < 0:
            raise ValueError("size must be >= 0")

        # set the size of the Square if all goes well
        self.__size = size

    def area(self) -> int:
        """
        Computes and returns the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size**2

    def my_print(self) -> None:
        """
        Prints the representation of the square using hashes '#'
        """
        if self.__size == 0:
            print()  # print a newline only, when the size is zero

        # the size is non-zero, let's print the square with hashes
        for _ in range(self.__size):
            print("#" * self.__size)
