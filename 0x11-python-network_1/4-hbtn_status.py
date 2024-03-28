#!/usr/bin/python3
"""Fetches the status of the ALX intranet server
Link: https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    page = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print(f"\t- type: {type(page.text)}")
    print(f"\t- content: {page.text}")
