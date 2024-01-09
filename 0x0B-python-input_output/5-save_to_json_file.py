#!/usr/bin/python3

"""
A module with a function that writes an Object to a text file, using a JSON
representation.
"""

import json


def save_to_json_file(my_obj: object, filename: str) -> None:
    """
    Writes a Python object to a text file, using JSON representation.

    Args:
        my_obj (object): The Python object to write.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
