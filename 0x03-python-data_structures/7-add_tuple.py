#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Returns the sum of a 2-tuple

    Args:
        tuple_a (tuple): the first 2-tuple. Defaults to an empty tuple
        tuple_b (tuple): the second 2-tuple. Defaults to an empty tuple

    Returns:
        tuple: a 2-tuple of the sum of tuple_a and tuple_b
    """
    # ensure we have a 2-tuple at minimum
    tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    tuple_b = tuple_b + (0,) * (2 - len(tuple_b))

    return tuple(sum(x) for x in zip(tuple_a[:2], tuple_b[:2]))
