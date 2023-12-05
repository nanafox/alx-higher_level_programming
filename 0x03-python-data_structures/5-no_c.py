#!/usr/bin/python3


def no_c(my_string: str) -> str:
    """
    Removes characters C and c from a string and returns the new string

    Args:
        my_string (str): the string to use

    Returns:
        str: the updated string with no letter C or c
    """
    return "".join(char for char in my_string if char not in "Cc")
