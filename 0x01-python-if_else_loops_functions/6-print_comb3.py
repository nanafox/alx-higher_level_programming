#!/usr/bin/python3


def print_combination() -> None:
    """
    prints the combinations of two numbers
    """
    for num1 in range(0, 9):
        for num2 in range(num1 + 1, 10):
            print(
                "{:d}{:d}".format(num1, num2),
                end="\n" if (num1 == 8 and num2 == 9) else ", ",
            )


if __name__ == "__main__":
    print_combination()
