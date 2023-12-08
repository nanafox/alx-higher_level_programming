#!/usr/bin/python3


def weight_average(my_list=[]) -> float:
    """
     returns the weighted average of all integers tuple (<score>, <weight>)

    Args:
        my_list (list, optional): the list of tuples. Defaults to [].

    Returns:
        int: the weighted average

    """
    return (
        # get the sum of the product for each score and weight pair
        sum(list(map(lambda *data: data[0][0] * data[0][1], my_list)))
        /
        # compute sum of weight
        sum(list(map(lambda *data: data[0][1], my_list)))
        # do this only when there is enough data
        if my_list is not None and len(my_list) >= 1 else 0
    )
