#!/usr/bin/python3

"""
A module with a function that returns a Python object represented by JSON
string
"""

import json


def from_json_string(my_str: str) -> object:
    """
    Returns a Python object represented by a JSON string, if it represents a
    Python object. If the JSON string does not represent a valid Python object,
    the behavior is undefined.

    Args:
        my_obj (str): The string containing the JSON representation.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
