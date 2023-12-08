#!/usr/bin/python3


def simple_delete(a_dictionary: dict, key: str = "") -> dict:
    """
    Deletes a key in a dictionary if it exists

    Args:
        a_dictionary (dict): the dictionary to delete from
        key (str, optional): the key to delete. Defaults to "".

    Returns:
        dict: the new dictionary with the key removed if it was present, else
        the same dictionary is return
    """
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
