#!/usr/bin/python3

"""A module with a function to add 2 matrices."""


def matrix_mul(m_a, m_b):
    """
    Returns the product of 2 matrices.

    Args:
        m_a (list[list]): Matrix 1.
        m_b (list[list]): Matrix 2.

    Raises:
        TypeError: When the matrix doesn't conform to the expected standards
        ValueError: When the matrix contains more than 2 rows.

    Returns:
        list[list]: The result of matrix multiplication
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    row = 0
    while row < len(m_a):
        if row == 0:
            row += 1
            continue
        elif len(m_a[row]) >= 3 or len(m_b[row]) >= 3:
            raise ValueError("m_a and m_b can't be multiplied")
        elif len(m_a[row]) != len(m_a[row - 1]):
            raise TypeError("each row of m_a must be of the same size")
        else:
            for elem in m_a[row]:
                if not isinstance(elem, (float, int)):
                    raise TypeError(
                        "m_a should contain only integers or floats"
                    )
        row += 1

    row = 0
    while row < len(m_b):
        if row == 0:
            row += 1
            continue
        elif len(m_b[row]) != len(m_b[row - 1]):
            raise TypeError("each row of m_b must be of the same size")
        else:
            for elem in m_b[row]:
                if not isinstance(elem, (float, int)):
                    raise TypeError(
                        "m_b should contain only integers or floats"
                    )
        row += 1

    result = [
        [sum(a * b for a, b in zip(row, col)) for col in zip(*m_b)]
        for row in m_a
    ]

    return result
