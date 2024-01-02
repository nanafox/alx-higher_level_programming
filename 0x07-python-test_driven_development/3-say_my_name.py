#!/usr/bin/python3

"""A module with a function that prints the first and last name of a person"""


def say_my_name(first_name: str, last_name: str = "") -> None:
    """
    Prints the first and last name of a person.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The person's surname. Defaults to "".

    Raises:
        TypeError: When the first name or last name is a non-string.

    Tests:
        >>> say_my_name("John", "Doe")
        My name is John Doe
        >>> say_my_name(1024)
        Traceback (most recent call last):
        ...
        TypeError: first_name must be a string
        >>> say_my_name("John", 45)
        Traceback (most recent call last):
        ...
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
