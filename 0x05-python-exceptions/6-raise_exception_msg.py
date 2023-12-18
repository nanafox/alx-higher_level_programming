#!/usr/bin/python3


def raise_exception_msg(message=""):
    """
    Raises a NameError exception and exit

    Args:
        message (str, optional): the error message to print.
        Defaults to an empty string.

    Raises:
        NameError: a name error exception when an object is not defined
    """
    raise NameError(message)
