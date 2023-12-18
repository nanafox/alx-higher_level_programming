#!/usr/bin/python3


def safe_print_integer(value) -> bool:
    """
    Safely prints an integer value

    Args:
        value (Any): the value to print

    Returns:
        bool: True if 'value' is an integer, else False
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False  # the value was not an integer

    # the value was indeed an integer and was printed safely
    return True
