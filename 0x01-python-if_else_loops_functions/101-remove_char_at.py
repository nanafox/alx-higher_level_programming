#!/usr/bin/python3


def remove_char_at(str: str, n: int) -> str:
    """
    Removes a character at a given index using C-style

    Args:
        str (str): the string to remove a character from
        n (int): the index position

    Returns:
        str: the modified string without the character if the index was valid
        else the string is return as is
    """
    updated_str = ""

    for i in range(len(str)):
        if i == n:
            continue
        updated_str += str[i]

    return updated_str
