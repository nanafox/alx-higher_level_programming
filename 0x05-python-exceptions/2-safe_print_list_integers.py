#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0) -> int:
    """
    Safely prints all integer values in a list

    Args:
        my_list (list, optional): the list to print from. Defaults to [].
        x (int, optional): the number of elements to print. Defaults to 0.

    Returns:
        int: the number of integer elements printed
    """
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
        else:
            count += 1  # increment the counter only when integers are printed
    print()

    return count
