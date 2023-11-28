#!/usr/bin/python3


def print_combination() -> None:
    """
    prints numbers from 0 to 99
    """
    for number in range(0, 100):
        # print combinations, separating them with commas and spaces
        print("{:02d}".format(number), end=", " if number < 99 else "\n")


if __name__ == "__main__":
    print_combination()
