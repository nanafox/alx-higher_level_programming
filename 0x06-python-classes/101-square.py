#!/usr/bin/python3

"""
Defines a blueprint for a Square as part of the OOP tasks
"""


class Square:
    """
    A blueprint for working with squares
    """

    def __init__(self, size: int = 0, position: "tuple[int, int]" = (0, 0)):
        """
        Initializes the Square class

        Args:
            size (int, optional): the size of the square. Defaults to 0.
            position (tuple, optional): the coordinates of the square.
            Defaults to (0, 0)
        """
        self.size = size
        self.position = position

    def __str__(self) -> str:
        """
        Returns the string representation of the square

        Returns:
            str: the visual representation of the square
        """
        return self.__custom_print_with_position

    @property
    def size(self) -> int:
        """
        Retrieves the size of the square

        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value) -> None:
        """
        Sets or updates the size of the square

        Args:
            value (int): the size of the square

        Raises:
            TypeError: when either the size
            ValueError: when the size if not a positive integer
        """
        # size must be an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # it should be greater than or equal to zero
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self) -> "tuple[int, int]":
        """
        Retrieves the 2-tuple containing the coordinates of the square

        Returns:
            tuple[int, int]: a 2-tuple containing the coordinates of the square
        """
        return self.__position

    @position.setter
    def position(self, value: "tuple[int, int]") -> None:
        """
        Sets or updates the coordinate of the square

        Args:
            position (tuple[int, int]): a 2-tuple containing the
            coordinates of the square

        Raise:
            TypeError: when the argument received is not a 2-tuple or if any of
            the values in the 2-tuple is not an integer
        """
        # ensure we are receiving a 2-tuple
        if not isinstance(value, tuple) or len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        # ensure each element in the 2-tuple is an integer as well
        if sum(1 for i in value if isinstance(i, int) and i >= 0) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    @property
    def __custom_print_with_position(self) -> str:
        """
        Hides the implementation of the 'my_print' function

        Returns:
            str: the representation of the square using hashes '#' along
            with the width and height if applicable
        """
        if self.__size == 0:
            return ""  # there's nothing to do here

        # this will hold the string representation we want to print
        custom_str = "\n" * self.__position[1]  # update it with the height

        # generate the square with hashes along with the expected width
        for _ in range(self.__size):
            custom_str += f"{' ' * self.__position[0]}{'#' * self.__size}\n"

        return custom_str[:-1]

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
        print(self.__custom_print_with_position)
