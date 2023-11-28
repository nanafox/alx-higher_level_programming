#!/usr/bin/python3


def print_alphabet() -> None:
    """
    Prints the latin alphabets in lower case

    Notes:
        ASCII lowercase letters are in the range 97 through 122
    """
    for letter in range(97, 123):
        print("{:c}".format(letter), end="")


if __name__ == "__main__":
    print_alphabet()
