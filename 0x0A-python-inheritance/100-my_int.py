#!/usr/bin/python3


"""
A module with a class that inherits from the `int` class and inverts
the `==` and `!=` operators
"""


class MyInt(int):
    """Inverts the `==` and `!=` operators"""

    def __eq__(self, __value: object) -> bool:
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        return super().__eq__(__value)
