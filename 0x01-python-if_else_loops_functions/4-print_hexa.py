#!/usr/bin/python3


def print_dec_hex() -> None:
    """
    Prints all decimals and their hexadecimal equivalent
    """
    for dec in range(0, 99):
        print("{:d} = 0x{:x}".format(dec, dec))


if __name__ == "__main__":
    print_dec_hex()
