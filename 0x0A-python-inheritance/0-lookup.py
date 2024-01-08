#!/usr/bin/python3

"""
A module with a function that returns the list of available attributes and
methods of an object
"""


def lookup(obj: object) -> list:
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (object): The object to check attributes and methods for.

    Returns:
        list: The list of available attributes and methods for object `obj`.
    """
    return dir(obj)
