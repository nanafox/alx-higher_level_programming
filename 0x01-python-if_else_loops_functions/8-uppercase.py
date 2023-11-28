#!/usr/bin/python3


def uppercase(str: str) -> None:
    """
    Prints a string in uppercase

    Args:
        c (string): the string

    Notes:
        If the the argument received is a non-string, the results will
        be unexpected
    """
    for letter in str:
        # check for lowercase letters and convert them to uppercase
        if "a" <= letter <= "z":
            letter = chr(ord(letter) - (ord("a") - ord("A")))
        print("{}".format(letter), end="")
    print()
