#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    replaces all occurrences of an element by another in a new list

    Args:
        my_list (list): the list to search through
        search (Any): the element to search for
        replace (Any): the value to replace the searched (found) element with

    Returns:
        list: a list with all occurrences of the searched element replaced
    """
    return list(
        map(lambda element: replace if element == search else element, my_list)
    )
