#!/usr/bin/python3

"""A module that models a Rectangle"""


class Rectangle:
    """Models a Rectangle"""

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """
        Initializes a Rectangle object

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """
        Returns the width of a Rectangle object.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """
        Sets and updates the width of a Rectangle object.

        Args:
            value (int): The value for the width.

        Raises:
            TypeError: When the value provided is not an integer.
            ValueError: When the value provided is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self) -> int:
        """
        Returns the width of a Rectangle object.

        Returns:
            int: The width of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """
        Sets and updates the height of a Rectangle object.

        Args:
            value (int): The value for the height.

        Raises:
            TypeError: When the value provided is not an integer.
            ValueError: When the value provided is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self) -> int:
        """
        Returns the area of a rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self) -> int:
        """
        Returns the perimeter of a rectangle. The perimeter is zero if either
        height or width is equal to zero

        Returns:
            int: The perimeter of the rectangle.
        """
        return (
            2 * (self.width + self.height) if self.width and self.height else 0
        )

    def __str__(self) -> str:
        """
        Returns the string representation of a rectangle using '#' characters.

        Returns:
            str: The string representation of the rectangle.

        Tests:
            >>> rectangle_1 = Rectangle(4, 2)
            >>> print(rectangle_1)
            ####
            ####
            >>> rectangle_2 = Rectangle()
            >>> print(rectangle_2)
            <BLANKLINE>
        """
        return self.__generate_rectangle()

    def __generate_rectangle(self) -> str:
        """
        Abstracts the generation of the representation of a rectangle
        using '#' characters.

        Returns:
            str: The representation of the rectangle with '#' characters.
        """
        img = ""

        if not self.height or not self.width:
            return ""

        for _ in range(self.height):
            img += "#" * self.width + "\n"

        return img[:-1]
