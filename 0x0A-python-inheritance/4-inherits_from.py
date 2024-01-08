#!/usr/bin/python3

"""
A module with a function that returns True if an object is an
instance of a class that inherits from the specified class.
"""


def inherits_from(obj, a_class) -> bool:
    """
    returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check if `obj` is an instance of.

    Returns:
        bool: True if `obj` inherits from `a_class`, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
