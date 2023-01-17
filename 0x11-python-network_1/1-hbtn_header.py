#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable found in Header response
"""
from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = Request(url)
    with urlopen(req) as response:
        header = response.info()
    print(header.get("X-Request-Id"))
