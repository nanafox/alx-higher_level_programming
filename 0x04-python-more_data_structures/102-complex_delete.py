#!/usr/bin/python3


def complex_delete(a_dictionary: dict, value: str) -> dict:
    """
    Deletes the keys values with a specific value

    Args:
        a_dictionary (dict): the dictionary to remove from
        value (str): the value to search for

    Returns:
        dict: a new dictionary with the key/value removed
    """
    if a_dictionary:
        # grab all the keys with the specified value
        key_values = list(
            filter(lambda *x: x[0][1] == value, a_dictionary.items())
        )

        # remove all the keys found
        for key, value in key_values:
            del a_dictionary[key]

    return a_dictionary
