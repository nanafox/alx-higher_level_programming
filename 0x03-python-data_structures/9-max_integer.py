#!/usr/bin/python3


def max_integer(my_list=[]):
    """
    Returns the largest number in a list of integers

    Args:
        my_list (list): the list of integers. Defaults to an empty list

    Returns:
        int: the maximum number in the list, else None if the list is empty
    """
    return None if not my_list else sorted(my_list)[-1]
