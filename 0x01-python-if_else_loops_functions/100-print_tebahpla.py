#!/usr/bin/python3


def print_reversed_alpha() -> None:
    """
    prints the latin alphabets in toggled case and reversed
    """
    for char in range(ord("z"), ord("a") - 1, -1):
        print("{:c}".format(char - 32 if char % 2 != 0 else char), end="")


if __name__ == "__main__":
    print_reversed_alpha()
