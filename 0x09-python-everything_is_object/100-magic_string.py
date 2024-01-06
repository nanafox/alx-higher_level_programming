#!/usr/bin/python3
def magic_string():
    magic_string.calls = getattr(magic_string, 'calls', 0) + 1
    return ", ".join(["BestSchool" for _ in range(magic_string.calls)])
