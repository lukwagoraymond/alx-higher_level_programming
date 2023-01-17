#!/usr/bin/python3
"""
Displays body of response but also manages HTTPErrors
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            html_page = response.read().decode("utf-8")
            print(html_page)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
