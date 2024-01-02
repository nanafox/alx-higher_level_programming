#!/usr/bin/python3

"""
A module with function that prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text: str) -> None:
    """
    Prints a text with 2 lines after each of '.', '?' and ':'.

    Args:
        text (str): The text to parse and print.

    Raises:
        TypeError: When the argument received as 'text' as not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i, char in enumerate(text, start=1):
        if char in (".", "?", ":"):
            print(f"{char}\n")

        elif text[i - 2] not in (".", "?", ":") or text[i - 1] != " ":
            print(char, end="")
