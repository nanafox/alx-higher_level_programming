#!/usr/bin/python3


def element_at(my_list: list, idx: int) -> int:
    """
    Returns the element at a particular index in a list in C-style

    Args:
        my_list (list): the list to search
        idx (int): the index

    Returns:
        int: the value of the element if found, else None
    """
    # handle invalid index ranges - negatives not accepted as well
    if 0 > idx >= len(my_list):
        return None

    for i, data in enumerate(my_list):
        if i == idx:
            return data

    return None  # element not found
