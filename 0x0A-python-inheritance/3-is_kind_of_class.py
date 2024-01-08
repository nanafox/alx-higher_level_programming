#!/usr/bin/python3

"""
A module with a function that returns True if the object is an
instance of the specified class.
"""


def is_kind_of_class(obj: object, a_class) -> bool:
    """
    Returns True if `obj` is an instance of `a_class`.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check if `obj` is an instance of.

    Returns:
        bool: True if `obj` is an instance of `a_class`, False otherwise.
    """
    return isinstance(obj, a_class)
