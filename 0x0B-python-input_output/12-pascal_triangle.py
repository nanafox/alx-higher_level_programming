#!/usr/bin/python3

"""Solves the Pascal's triangle problem"""


def pascal_triangle(n: int) -> "list[list[int]]":
    """
    Returns a list of lists of integers representing ou arethe Pascal's
    triangle up to height `n`.

    Args:
        n (int): The height of the triangle.

    Returns:
        list[list[int]]: The reprentation of the triangle.
    """
    if n <= 0:
        return []

    p_triangle = [[1]]

    for _ in range(n - 1):
        current_row = p_triangle[-1]
        new_row = (
            [1]
            + [
                current_row[i] + current_row[i + 1]
                for i in range(len(current_row) - 1)
            ]
            + [1]
        )

        p_triangle.append(new_row)

    return p_triangle
