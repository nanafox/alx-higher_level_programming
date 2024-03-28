#!/usr/bin/python3
"""Send a POST request to the passed URL with the email as a parameter."""

import requests
import sys


if __name__ == "__main__":
    if (len(sys.argv) != 3):
        sys.stderr.write(f"Usage: {sys.argv[0]} <URL> <email>\n")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={"email": email})
    print(response.text)
