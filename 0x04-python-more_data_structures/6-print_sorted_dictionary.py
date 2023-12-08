#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary: dict) -> None:
    """
    Prints a dictionary by ordered keys

    Args:
        a_dictionary (dict): the dictionary to print
    """
    if a_dictionary:
        for key, value in sorted(a_dictionary.items()):
            print(f"{key}: {value}")
