#!/usr/bin/python3
"""
Displays body of response but also manages HTTPErrors
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if int(r.status_code) < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
