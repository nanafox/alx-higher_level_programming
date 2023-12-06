#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list

    Args:
        my_list (list): the list containing the items. Defaults to an empty
        list
        idx (int): the index of the items to delete at

    Returns:
        list: the list with the element at the given index deleted else the
        same the list is return on error
    """
    # handle out of range indexes and empty list
    if not (0 <= idx < len(my_list)) or not my_list:
        return my_list

    # perform the deletion and return the updated the list
    del my_list[idx]
    return (my_list)
