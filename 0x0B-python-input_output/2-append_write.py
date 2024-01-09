#!/usr/bin/python3

"""A module with a function that appends data to a file."""


def append_write(filename: str = "", text: str = "") -> int:
    """
    Appends data at the end of a file.

    Args:
        filename (str): The name of the file to append data to.
        text (str): The new data to append to `filename`.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
