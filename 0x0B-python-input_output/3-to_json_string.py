#!/usr/bin/python3

"""A module with a function that returns the JSON representation an object."""

import json


def to_json_string(my_obj) -> str:
    """
    Returns the JSON representation of an object, if serialazable. If the
    object can't be serialized, the behavior is undefined.

    Args:
        my_obj: The object to return JSON representation for.

    Returns:
        str: The JSON reprensentation of the object.
    """
    return json.dumps(my_obj)
