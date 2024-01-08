#!/usr/bin/python3

"""
A module that inherits from the Rectangle class and models a
Square object
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Models a square shape object."""

    def __init__(self, size: int) -> None:
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size

    def area(self) -> int:
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2
