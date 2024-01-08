#!/usr/bin/python3

"""
A module that inherits from the BaseGeometry class and models a
Rectangle object
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A class that models a Rectangle."""

    def __init__(self, width: int, height: int) -> None:
        """
        Initializes an instance of a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): the width of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
