#!/usr/bin/python3
"""This script displays the last 10 commits from a GitHub repository."""


import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <repo> <owner>")
        sys.exit(1)

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Not a valid repository")
        sys.exit(1)

    top_10_commits = response.json()[:10]
    for commit in top_10_commits:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f"{sha}: {author}")
