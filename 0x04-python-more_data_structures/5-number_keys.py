#!/usr/bin/python3


def number_keys(a_dictionary: dict) -> int:
    """
    Returns the number of keys in a dictionary

    Args:
        a_dictionary (dict): the dictionary to count keys from

    Returns:
        int: the number of keys in the dictionary
    """
    return len(a_dictionary.keys()) if isinstance(a_dictionary, dict) else None
