#!/usr/bin/python3
"""This script finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers) -> "int | None":
    """This function finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int | None: The peak of the list of integers.
    """
    if not list_of_integers:
        return None

    list_of_integers.sort()
    return list_of_integers[-1]
