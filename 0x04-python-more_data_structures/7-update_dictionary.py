#!/usr/bin/python3


def update_dictionary(a_dictionary: dict, key: str, value) -> dict:
    """
    Replaces or adds key/value in a dictionary

    Args:
        a_dictionary (dict): the dictionary to update
        key (str): the key.
        value (Any): the value to add.

    Returns:
        dict: the new dictionary with the added key/value pairs
    """
    a_dictionary[key] = value  # modifies the original dictionary

    return a_dictionary
