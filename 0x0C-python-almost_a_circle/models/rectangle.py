#!/usr/bin/python3

"""Defines a Rectangle object."""

from .base import Base


class Rectangle(Base):
    """Models a Rectangle object."""

    def __init__(
        self, width: int, height: int, x: int = 0, y: int = 0, id=None
    ):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the shape.
            height (int): The height of the shape.
            x (int, optional): x value. Defaults to 0.
            y (int, optional): y value. Defaults to 0.
            id (int, optional): The ID of the object. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        """
        Returns the width.

        Returns:
            int: The width of the shape.
        """
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """
        Sets and/or updates the shape's width.

        Args:
            value (int): The value to assign to width.
        """
        self.__width = value

    @property
    def height(self) -> int:
        """
        Returns the height.

        Returns:
            int: The height of the shape.
        """
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """
        Sets and/or updates the shape's height.

        Args:
            value (int): The value to assign to height.
        """
        self.__height = value

    @property
    def x(self) -> int:
        """
        Returns the value of `x`.

        Returns:
            int: The value of `x`.
        """
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        """
        Sets and/or updates the value of `x`.

        Args:
            value (int): The value to assign to x.
        """
        self.__x = value

    @property
    def y(self) -> int:
        """
        Returns the width.

        Returns:
            int: The width of the shape.
        """
        return self.__y

    @y.setter
    def y(self, value: int) -> None:
        """
        Sets and/or updates the value of `y`.

        Args:
            value (int): The value to assign to width.
        """
        self.__y = value
