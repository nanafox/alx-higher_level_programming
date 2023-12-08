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
        if a_dictionary is not None
        else None
    )
