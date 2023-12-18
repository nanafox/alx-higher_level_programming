#!/usr/bin/python3


def safe_print_list(my_list=[], x=0) -> int:
    """
    Safely prints the contents in a list that contains any type of data

    Args:
        my_list (list, optional): the list containing elements to print.
        x (int, optional): the number of elements to print. Defaults to 0.

    Raises:
        TypeError: If the argument passed as 'my_list' is not a list,
        an error is raised and the flow terminated. The argument must be a list
        Also, the number of elements to print must be an integer since slicing
        requires integers. An error is printed when the argument is not of the
        integer (int) type.

    Returns:
        int: the number of elements printed
    """
    try:
        # ensure we received a list
        if not isinstance(my_list, list) and my_list is not None:
            raise TypeError("'my_list' must be a list")
        # ensure the number of elements to print is an integer
        if not isinstance(x, int):
            raise TypeError(
                "expected an integer for the number of elements to print, but"
                + f" received {type(x).__repr__(x)} of type {type(x).__name__}"
            )
    except TypeError as err:
        print(f"Error: {err}")
    else:
        # print the contents of the list if no exceptions occurred
        print("".join(str(c) for c in my_list[:x]))

        return my_list[:x].__len__()

    # return this when an exception occur
    return 0
