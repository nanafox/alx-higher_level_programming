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

    def __str__(self) -> str:
        """
        Returns information about the Rectangle, mainly the width/height.

        Returns:
            str: The width and height data of the rectangle object.
        """
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"

    def area(self) -> int:
        """
        Returns the area of a rectangle.

        Returns:
            int: The area of the rectangle. <width> * <height>
        """
        return self.__width * self.__height
