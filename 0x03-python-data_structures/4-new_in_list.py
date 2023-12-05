#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    replaces an element in a list at a specific position without modifying
    the original list (like in C).

    Args:
        my_list (list): the list containing the data
        idx (int): the index position
        element (Any): the replacement value

    Returns:
        list: a duplicate of the original list with the value updated to the
        new element's value
    """
    dup_list = my_list.copy()

    if not (0 <= idx < len(dup_list)):
        return dup_list

    for i in range(len(dup_list)):
        if i == idx:
            dup_list[i] = element
            return dup_list
