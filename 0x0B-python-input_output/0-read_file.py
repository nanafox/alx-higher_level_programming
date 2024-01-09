#!/usr/bin/python3

"""A module with a function that reads from a file"""


def read_file(filename: str = "") -> None:
    """
    Reads from a file.

    Args:
        filename (str): The name of the file to read from.
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
