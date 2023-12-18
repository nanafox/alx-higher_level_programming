#!/usr/bin/python3

from sys import stderr


def safe_print_integer_err(value) -> bool:
    """
    Safely prints an integer value

    Args:
        value (Any): the value to print

    Returns:
        bool: True if 'value' is an integer, else False
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        stderr.write(f"Exception: {err}\n")
        return False  # the value was not an integer

    # the value was indeed an integer and was printed safely
    return True
