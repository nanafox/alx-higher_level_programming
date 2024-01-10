#!/usr/bin/python3
"""Reads from standard input and computes metrics"""

from typing import Dict, List, Tuple

VALID_CODES = {"200", "301", "400", "401", "403", "404", "405", "500"}


def print_stats(size: int, status_codes: Dict[str, int]) -> None:
    """
    Print accumulated metrics.

    Args:
        size (int): Total file size.
        status_codes (Dict[str, int]): Dictionary containing status codes
        and their counts.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


def process_line(
    line: List[str], size: int, status_codes: Dict[str, int]
) -> Tuple[int, Dict[str, int]]:
    """
    Process a single line and update metrics.

    Args:
        line (List[str]): List of strings representing a line.
        size (int): Current total file size.
        status_codes (Dict[str, int]): Dictionary containing status codes
        and their counts.

    Returns:
        Tuple[int, Dict[str, int]]: Updated size and status_codes.
    """
    try:
        size += int(line[-1])
    except (IndexError, ValueError):
        pass

    try:
        if line[-2] in VALID_CODES:
            status_codes[line[-2]] = status_codes.get(line[-2], 0) + 1
    except IndexError:
        pass

    return size, status_codes


def process_input() -> None:
    """Reads from standard input, processes lines, and prints metrics."""
    size = 0
    status_codes: Dict[str, int] = {}
    count = 0

    try:
        for line in sys.stdin:
            count = (count + 1) % 10
            size, status_codes = process_line(line.split(), size, status_codes)

            if count == 0:
                print_stats(size, status_codes)

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise


if __name__ == "__main__":
    import sys

    process_input()
