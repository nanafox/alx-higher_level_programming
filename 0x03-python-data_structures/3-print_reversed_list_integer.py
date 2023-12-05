#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    Prints a list in reversed order

    Args:
        my_list (list, optional): the list to print in reverse. Defaults to [].
    """
    for element in range(len(my_list), 0, -1):
        print("{:d}".format(element))
