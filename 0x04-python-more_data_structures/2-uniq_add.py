#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Returns the sum of unique value in a list of integers

    Args:
        my_list (list, optional): the list to add from. Defaults to [].

    Returns:
        int: the result of the sum operation on unique integer values
    """
    return sum(set(my_list))
