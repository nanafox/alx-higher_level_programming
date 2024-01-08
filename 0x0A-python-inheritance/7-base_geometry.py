#!/usr/bin/python3


"""A module with a class that models geometric shapes."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Returns the area of a shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int) -> None:
        """
        Performs validation of integer values.

        Args:
            name (str): The name of the object.
            value (int): The value of the object.

        Raises:
            TypeError: When the `value` given to the object is not an integer.
            ValueError: When the the `value` is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
