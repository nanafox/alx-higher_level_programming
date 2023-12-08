#!/usr/bin/python3


def multiply_by_2(a_dictionary: dict) -> dict:
    """
    Returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary (dict): the dictionary to update (modified in-place)

    Returns:
        dict: a new dictionary with all values multiplied by 2
    """
    return {
        key: value * 2
        for key, value in a_dictionary.items()
        if isinstance(value, int)
    }
