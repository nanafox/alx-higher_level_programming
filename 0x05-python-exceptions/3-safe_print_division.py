#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Safely print the quotient of 'a' and 'b'

    Args:
        a (int): the first operand
        b (_type_): the second operand

    Returns:
        float: the quotient of 'a' and 'b', else None on exceptions
    """
    c = None
    try:
        c = a / b
        return c
    except (ZeroDivisionError, TypeError, ValueError):
        return None
    finally:
        print("Inside result: {}".format(c))
