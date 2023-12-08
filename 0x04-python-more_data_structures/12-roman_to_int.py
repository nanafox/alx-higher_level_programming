#!/usr/bin/python3


def roman_to_int(roman_string: str) -> int:
    """
    Converts a Roman numeral to an integer

    Args:
        roman_string (str): the string containing the Roman numeral

    Returns:
        int: the decimal equivalent of the Roman numeral
    """
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # compute and return the decimal equivalent of the roman numeral received
    return sum(
        roman_numerals.get(roman_string[i], 0)
        if i == 0
        or roman_numerals.get(roman_string[i], 0)
        <= roman_numerals[roman_string[i - 1]]
        # handle subtractive cases
        else roman_numerals.get(roman_string[i], 0)
        - 2 * roman_numerals.get(roman_string[i - 1], 0)
        for i in range(len(roman_string))
    )
