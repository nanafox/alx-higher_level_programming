#!/usr/bin/python3


def common_elements(set_1: set, set_2: set) -> set:
    """
    Returns a set of common elements in two sets

    Args:
        set_1 (set): the first set
        set_2 (set): the second set

    Returns:
        set: the common elements in both sets (the intersection)
    """
    return set(set_1.intersection(set_2))
