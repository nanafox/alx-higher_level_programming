#!/usr/bin/python3


def multiple_returns(sentence: str) -> tuple:
    """
    Returns a tuple with the length of a string and its first character

    Args:
        sentence (str): the string to check

    Returns:
        tuple: the length of the string and its first character
    """
    return len(sentence), sentence[0] if sentence else None
