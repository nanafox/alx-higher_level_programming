#!/usr/bin/python3

"""
A module with a function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(
    filename: str = "", search_string: str = "", new_string: str = ""
) -> None:
    """
    Inserts a line of text to a file, after each line containing a
    specific string.

    Args:
        filename (str, optional): The name of the file. Defaults to "".
        search_string (str, optional): The string to search. Defaults to "".
        new_string (str, optional): The new string to insert. Defaults to "".
    """
    with open(filename, "r+", encoding="utf-8") as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] += new_string

        # get back to the beginning of the file and write the changes
        file.seek(0)
        file.writelines(lines)
