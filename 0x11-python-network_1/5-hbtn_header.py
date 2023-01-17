#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable found in Header response
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
