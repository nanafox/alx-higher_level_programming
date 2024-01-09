#!/usr/bin/python3

"""A module with a function that writes/overwrites to a file."""


def write_file(filename: str = "", text: str = "") -> int:
    """
    Writes to a file.

    Args:
        filename (str): The name of the file to write to. It is overwritten if
                        it exists.
        text (str): The data to put in the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
