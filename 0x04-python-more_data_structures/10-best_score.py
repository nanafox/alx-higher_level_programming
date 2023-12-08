#!/usr/bin/python3


def best_score(a_dictionary: dict) -> str:
    """
    Returns the key with the biggest integer value

    Args:
        a_dictionary (dict): the dictionary to search through

    Returns:
        str: the key with the biggest integer value
    """
    return (
        # sort based on the number field
        sorted(a_dictionary.items(), key=lambda *items: items[0][1])[-1][0]
        # let's ensure the dictionary is not empty and contains some data
        if a_dictionary is not None and len(a_dictionary) >= 1
        # well, there was nothing here so do nothing
        else None
    )
