#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """
    Prints the elements(integers) in a list

    Args:
        my_list: the list containing the integers to print
    """
    for element in my_list:
        print("{:d}".format(element))
