#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    """
    Prints all the names defined by the compiled module
    """
    for name in dir(hidden_4):
        if name.startswith("__"):
            continue
        print(name)
