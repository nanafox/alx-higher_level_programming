#!/usr/bin/python3

"""A Magic Class Bytecode to Python Code task"""

import math


class MagicClass:
    """A Magic Circle Class"""

    def __init__(self, radius=0):
        """
        Initialize the Magic Circle Class

        Args:
            radius (int, optional): the radius. Defaults to 0.

        Raises:
            TypeError: when the radius is not a number type
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """
        Returns the area of the circle

        Returns:
            float: the area of the circle
        """
        return (self.__radius**2) * math.pi

    def circumference(self):
        """
        Returns the circumference of a circle

        Returns:
            float: the circumference of the circle
        """
        return 2 * math.pi * self.__radius
