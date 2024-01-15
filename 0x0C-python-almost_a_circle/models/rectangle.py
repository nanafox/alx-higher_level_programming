#!/usr/bin/python3

"""Defines a Rectangle object."""

from models.base import Base


class Rectangle(Base):
    """Models a Rectangle object."""

    def __init__(
        self, width: int, height: int, x: int = 0, y: int = 0, id=None
    ) -> None:
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

    def __str__(self) -> str:
        """
        Returns information about the Rectangle instance.

        Returns:
            str: Information about the Rectangle instance.
        """
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

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

    def display(self) -> None:
        """
        Prints the visual of the Rectangle instance with the `#` character.
        """
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs) -> None:
        """
        Updates attributes with the values in the provided `args`.
        """
        if args is not None and len(args) > len(self.__dict__.keys()):
            raise ValueError("excess positional arguments than expected")

        # attempt to use the *args if it's present and not empty
        if args is not None and len(args) > 0:
            keys = list(self.__dict__)

            for i, arg in enumerate(args):
                self.__dict__[keys[i]] = arg

            return  # we are done here if the *args was not empty, return

        # use the keyword arguments instead since the *args was unavailable
        for attr, value in kwargs.items():
            if not hasattr(self, attr):
                raise AttributeError(f"invalid attribute name: '{attr}'")

            setattr(self, attr, value)

    def to_dictionary(self) -> dict:
        """
        Returns the dictionary representation of a Rectangle instance.

        Returns:
            dict: The dictionary representation of a Rectangle instance.
        """
        return {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
        }
