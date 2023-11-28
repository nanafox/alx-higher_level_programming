#!/usr/bin/python3


def print_last_digit(number: int) -> int:
    """
    Prints the last digit of a number

    Args:
        number (int): the number to print the last digit

    Returns:
        int: the last digit of 'number'
    """
    print(abs(number) % 10, end="")
    return abs(number) % 10
