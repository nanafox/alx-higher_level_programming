#!/usr/bin/python3
"""Send a POST request to the passed URL with the email as a parameter."""

import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    if (len(sys.argv) != 3):
        sys.stderr.write(f"Usage: {sys.argv[0]} <URL> <email>\n")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email})
    data = data.encode("ascii")

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
