#!/usr/bin/python3
"""This script uses the GitHub API with Basic Authentication and Personal
Access Token to display my `id`."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <username> <password>")
        sys.exit(1)

    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(username, password))
    print(response.json().get("id"))
