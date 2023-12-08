#!/usr/bin/python3


def only_diff_elements(set_1: set, set_2: set) -> set:
    """
    Returns a set of all elements present in only one set

    Args:
        set_1 (set): the first set
        set_2 (set): the second set

    Returns:
        set: a set containing all elements present in only one set
    """
    return set(set_1.symmetric_difference(set_2))
