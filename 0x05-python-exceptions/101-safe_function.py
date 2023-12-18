#!/usr/bin/python3

from sys import stderr


def safe_function(fct, *args):
    """
    Safely executes a function

    Args:
        fct (function): the function to execution
        args (list): a list of arguments to pass to the function

    Returns:
        Any: the results is whatever the function executed returns,
        else None on error
    """
    try:
        return fct(*args)
    except Exception as err:
        stderr.write(f"Exception: {err}\n")
        return None
