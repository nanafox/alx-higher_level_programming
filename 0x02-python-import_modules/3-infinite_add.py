#!/usr/bin/python3

from sys import argv


def infinite_add() -> None:
    """
    Prints the result of the addition of all arguments
    """
    # handle when no numbers are given
    if not argv[1:]:
        print("0")
        return

    sum = 0
    for operand in argv[1:]:
        try:
            sum += int(operand)
        except ValueError:
            print("Expected an integer!")
            return
    print(sum)


if __name__ == "__main__":
    infinite_add()
