#!/usr/bin/python3


def islower(c: str) -> bool:
    """
    Returns True if character 'c' is lowercase else False

    Args:
        c (string): the character to check

    Returns:
        bool: True if the character 'c' is a lower case else False

    Notes:
        If the the argument received is a non-string, the results will
        be unexpected
    """
    return ord("a") <= ord(c) <= ord("z")
