#!/usr/bin/python3


def print_alphabet() -> None:
    """
    Prints the latin alphabets in lower case except 'e' and 'q'
    """
    for letter in range(97, 123):
        if chr(letter) in "eq":
            continue  # skip letters 'e' and 'q'
        print("{:c}".format(letter), end="")


if __name__ == "__main__":
    print_alphabet()
