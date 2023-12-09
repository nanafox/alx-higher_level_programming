#!/usr/bin/python3


def square_matrix_map(matrix: list = []) -> list[list]:
    """
    computes the square value of all integers of a matrix using map

    Args:
        matrix (list, optional): the matrix. Defaults to [].

    Returns:
        list[list]: a new matrix with all values squared
    """
    if matrix is None:
        return [[]]

    def operate_on_row(row: list) -> list:
        """
        Returns the square for each row in the matrix

        Args:
            row (list): the row in the matrix

        Returns:
            list: the current row with the values squared
        """
        return list(map(lambda x: x**2, row))

    return list(map(operate_on_row, matrix))
