#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix

    Args:
        matrix: the list of matrix values. Default to an empty list

    Returns:
        a matrix(list of lists) with each element squared
    """
    return [list(map(lambda element: element**2, row)) for row in matrix]
