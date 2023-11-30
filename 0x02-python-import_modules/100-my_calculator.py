#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import exit, argv


def perform_calculation(x: int, y: int, operator: str) -> None:
    """
    Performs simple math operations

    Args:
        x (int): operand 1
        y (int): operand 2
        operator (str): the operator
    """
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    # handle invalid operators
    if operator not in operators.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(f"{x} {operator} {y} = {operators[operator](x, y)}")


if __name__ == "__main__":
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    try:
        # let's perform some basic math operations
        perform_calculation(int(argv[1]), int(argv[3]), argv[2])
    except ValueError:
        # handle invalid operands
        print("Operands must be integers")
        exit(1)
