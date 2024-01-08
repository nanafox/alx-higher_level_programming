#!/usr/bin/python3


"""A module with a class that models geometric shapes."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Returns the area of a shape"""
        raise Exception("area() is not implemented")
