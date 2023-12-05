#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replaces the element of a list at a specific position in C-tyle

    Args:
        my_list (list): the list containing the values needing to be changed
        idx (int): the index position
        element (Any): the element (data) to replace

    Returns:
        list: a new list with the value replaced (updated), else None on error.
        The original list is not modified
    """
    # check for invalid index positions, if found, don't modify the list
    if not (0 <= idx < len(my_list)):
        return my_list

    for i in range(len(my_list)):
        if i == idx:
            # update the list with the replacement's value
            my_list[i] = element

            return my_list
