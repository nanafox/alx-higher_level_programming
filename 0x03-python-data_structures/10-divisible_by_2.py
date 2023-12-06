#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list

    Args:
        my_list (list): the list of integers. Defaults to an empty list

    Returns:
        list: True and/or False values depending on whether the element was a
        multiple of 2 or not
    """
    return [True if x % 2 == 0 else False for x in my_list]
