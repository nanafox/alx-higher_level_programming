#!/usr/bin/python3

"""Defines a Rectangle object."""

from models.base import Base


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

        Raises:
            TypeError: If the `value` provided is not an integer.
            ValueError: If the `value` is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

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

        Raises:
            TypeError: If the `value` provided is not an integer.
            ValueError: If the `value` is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

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

        Raises:
            TypeError: If the `value` provided is not an integer.
            ValueError: If the `value` is less than zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

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

        Raises:
            TypeError: If the `value` provided is not an integer.
            ValueError: If the `value` is less than zero.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self) -> int:
        """
        Returns the area of the Rectangle object.

        Returns:
            int: The area of the Rectangle object.
        """
        return self.width * self.height
