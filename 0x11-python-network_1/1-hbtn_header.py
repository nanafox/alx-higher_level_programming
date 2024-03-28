#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""

import urllib.request
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.stderr.write(f"Usage: {sys.argv[0]} <URL>\n")
        sys.exit(1)

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
