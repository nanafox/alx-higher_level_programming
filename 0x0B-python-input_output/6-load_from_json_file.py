#!/usr/bin/python3

"""A module with a function that creates an Object from a JSON file."""

import json


def load_from_json_file(filename: str) -> object:
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The file containing the object's JSON reprensentation.

    Returns:
        object: The associated Python object  represented in the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
