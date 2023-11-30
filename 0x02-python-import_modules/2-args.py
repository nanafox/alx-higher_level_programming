#!/usr/bin/python3

from sys import argv


def print_args() -> None:
    """
    Prints the number of command line arguments with
    each argument on a new line
    """
    # get the command line arguments without the filename
    size = len(argv[1:])

    print(f"{size} argument{'s' if size == 0 or size > 1 else ''}", end="")

    # check for when there is no arguments passed
    if not argv[1:]:
        print(".")
        return

    # we had arguments passed on the command line, let's print them
    print(":")
    for position, arg in enumerate(argv[1:], start=1):
        print(f"{position}: {arg}")


if __name__ == "__main__":
    print_args()
