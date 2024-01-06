#!/usr/bin/python3

"""A module that defines a locked class"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes, except
    if the new instance attribute is called `first_name`
    """

    __slots__ = ["first_name"]
