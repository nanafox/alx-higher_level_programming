#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    Prints a list in reversed order

    Args:
        my_list (list, optional): the list to print in reverse. Defaults to [].
    """
    # check for empty lists
    if not my_list:
        return

    for element in my_list[::-1]:
        print("{:d}".format(element))
