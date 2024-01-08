#!/usr/bin/python3

"""
A module with a class that inherits and uses the 'list' class.
"""


class MyList(list):
    """A class that uses the list as it's base class."""

    def print_sorted(self) -> None:
        """
        Prints the list in sorted (ascending) order.
        """
        print(sorted(self))
