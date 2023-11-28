#!/usr/bin/python3


def fizzbuzz() -> None:
    """
    Solves the FizzBuzz challenge for the first 100 counting numbers

    For multiples of 3 only, it prints "Fizz"
    For multiples of 5 only, it prints "Buzz"
    For multiples of 3 and 5, it prints "FizzBuzz"
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
