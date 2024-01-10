#!/usr/bin/python3

"""
A script that adds all arguments to a Python list, and then save them to a
JSON file.
"""

import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def update_json_file(args, json_file: str = "add_item.json") -> None:
    """
    Adds command line all arguments to a Python list, and then save them to
    a JSON file.

    Args:
        args (list): A list command line arguments.
        json_file (str): The name of JSON file to write to. Defaults to
        "add_item.json"
    """
    py_list = []

    # create the Python list from the JSON file, and handle errors as needed
    try:
        py_list = load_from_json_file(json_file)
    except Exception:
        # let's create the file, it doesn't exist
        save_to_json_file([], json_file)

    # add all the arguments to the lists
    for arg in args:
        py_list.append(arg)

    save_to_json_file(py_list, json_file)


if __name__ == "__main__":
    update_json_file(sys.argv[1:])
