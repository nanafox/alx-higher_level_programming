#!/usr/bin/python3

"""
Module with a function that adds two numbers. It checks for the validity of
arguments given as operands before trying to add them. In the event of an
error, an exception is raised. Notable amongst these exceptions is the
TypeError which is raised when the operands fail to be an integer.
"""


def add_integer(a: "float | int", b: "float | int" = 98) -> int:
    """Returns the sum of two integers.

    Args:
        a (float | int): The first number.
        b (float | int, optional): The second number. Defaults to 98.

    Raises:
        TypeError: When the operands given are not of a valid type (integers).

    Returns:
        int: The sum of the two numbers as an integer.

    Tests:
        >>> add_integer(0)
        98
        >>> add_integer(1, -2)
        -1
        >>> add_integer('1', '67')
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # ensure the operands are of integer type
    try:
        int(a)
        int(b)
    except Exception as err:
        raise err

    return int(a) + int(b)
