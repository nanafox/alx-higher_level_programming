#!/usr/bin/python3

"""
A module with a function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object
"""


def class_to_json(obj: object) -> dict:
    """
    Returns the dictionary representation of a simple data structure for
    JSON serialization of an object.

    Args:
        obj (object): The object (a instance of a Class) to ready for
        JSON serialization.

    Returns:
        dict: The dictionary description of the object.
    """
    return (obj.__dict__)
