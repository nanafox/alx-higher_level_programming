#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers

    Args:
        matrix (list, optional): the list to print. Defaults to [[]].
    """
    if not matrix:
        return

    for row in matrix:
        print(" ".join("{:d}".format(data) for data in row))
