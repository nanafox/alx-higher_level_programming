#!/usr/bin/python3

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices

    Args:
        m_a: Matrix 1.
        m_b: Matrix 2.

    Returns:
        The result of multiplying two matrices.
    """
    return np.matmul(m_a, m_b)
